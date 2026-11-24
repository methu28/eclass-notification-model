"""Verify the four-condition experiment independently from the sorting helper."""
import csv
import json
from pathlib import Path

import pandas as pd
import pytest

pytest.importorskip("mesa")

from src.project_model.run_del03 import main


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/notifications.csv"


def test_four_condition_exports_against_independent_calculation(tmp_path):
    output = tmp_path / "del03"
    assert main(["--input", str(DATA), "--output-dir", str(output)]) == 0
    with DATA.open(newline="", encoding="utf-8") as file:
        records = list(csv.DictReader(file))
    initial_cohort = {
        r["notification_id"] for r in records
        if float(r["posted_hours_ago"]) <= 24
        and (not r["deadline_hours_remaining"] or float(r["deadline_hours_remaining"]) > 72)
    }
    tables = {}
    for condition, reserved in [("recency", 0), ("hybrid_1", 1), ("hybrid_2", 2), ("hybrid_3", 3)]:
        df = pd.read_csv(output / f"{condition}_raw_model.csv")
        agents = pd.read_csv(output / f"{condition}_raw_agent_states.csv")
        assert len(df) == 7 and len(agents) == 140
        tables[condition] = df
        for step in range(7):
            items = []
            for r in records:
                deadline = float(r["deadline_hours_remaining"]) - step * 6 if r["deadline_hours_remaining"] else None
                items.append({"id": r["notification_id"], "category": r["category"],
                              "age": float(r["posted_hours_ago"]) + step * 6,
                              "deadline": deadline, "urgent": deadline is not None and 0 < deadline <= 72})
            newest = sorted(items, key=lambda x: (x["age"], x["id"]))
            promoted = [x for x in newest if x["urgent"]][:reserved]
            ordered = promoted + [x for x in newest if x not in promoted]
            urgent_ranks = [rank for rank, x in enumerate(ordered, 1) if x["urgent"]]
            top = ordered[:5]
            row = df.iloc[step]
            assert row["step"] == step and row["elapsed_hours"] == step * 6
            assert row["urgent_total"] == len(urgent_ranks)
            assert row["urgent_top5_count"] == sum(x["urgent"] for x in top)
            assert row["urgent_top5_share"] == pytest.approx(sum(x["urgent"] for x in top) / len(urgent_ranks))
            assert row["average_urgent_rank"] == pytest.approx(sum(urgent_ranks) / len(urgent_ranks))
            assert row["recent_nonurgent_top5"] == sum(not x["urgent"] and x["age"] <= 24 for x in top)
            assert row["initial_recent_nonurgent_top5"] == sum(x["id"] in initial_cohort for x in top)
            assert row["top_five_ids"] == "|".join(x["id"] for x in top)
            state = agents[agents["Step"] == step].set_index("notification_id")
            assert len(state) == 20 and state.index.is_unique
            for rank, item in enumerate(ordered, 1):
                a = state.loc[item["id"]]
                assert a["category"] == item["category"]
                assert a["rank"] == rank and bool(a["in_top_five"]) == (rank <= 5)
                assert bool(a["urgent"]) == item["urgent"]
                assert a["posted_hours_ago"] == item["age"]
                if item["deadline"] is None:
                    assert pd.isna(a["hours_until_deadline"])
                else:
                    assert a["hours_until_deadline"] == item["deadline"]

    for condition, prefix in [("recency", "baseline"), ("hybrid_2", "alternative")]:
        pd.testing.assert_frame_equal(tables[condition], pd.read_csv(ROOT / "outputs" / f"{prefix}_raw_00_urgent_visibility.csv"), check_exact=True)
        pd.testing.assert_frame_equal(pd.read_csv(output / f"{condition}_raw_agent_states.csv"), pd.read_csv(ROOT / "outputs" / f"{prefix}_raw_01_agent_states.csv"), check_exact=True)

    combined = pd.read_csv(output / "comparison_raw_model_metrics.csv")
    wide = pd.read_csv(output / "comparison_processed_metrics_wide.csv")
    summary = pd.read_csv(output / "comparison_processed_summary.csv").set_index("condition")
    for condition, df in tables.items():
        pd.testing.assert_frame_equal(combined[combined["condition"] == condition][df.columns].reset_index(drop=True), df)
        for metric in ["urgent_top5_count", "urgent_top5_share", "average_urgent_rank", "recent_nonurgent_top5", "initial_recent_nonurgent_top5"]:
            assert wide[f"{condition}_{metric}"].tolist() == pytest.approx(df[metric].tolist())
            for suffix, value in [("initial", df[metric].iloc[0]), ("final", df[metric].iloc[-1]), ("snapshot_mean", df[metric].mean())]:
                assert summary.loc[condition, f"{metric}_{suffix}"] == pytest.approx(value)
    assert len(combined) == 28
    metadata = json.loads((output / "run_metadata.json").read_text(encoding="utf-8"))
    assert metadata["urgency_threshold_hours"] == 72 and metadata["visible_positions"] == 5
    assert len(metadata["conditions"]) == 4
    assert len(list(output.glob("*.png"))) == 6
    sentinel = output / "recency_raw_model.csv"
    before = sentinel.read_bytes()
    with pytest.raises(SystemExit) as error:
        main(["--output-dir", str(output)])
    assert error.value.code == 2 and sentinel.read_bytes() == before


@pytest.mark.parametrize("args", [["--steps", "0"], ["--hours-per-step", "0"], ["--steps", "8"]])
def test_invalid_time_configuration_creates_no_outputs(tmp_path, args):
    output = tmp_path / "invalid"
    with pytest.raises(SystemExit) as error:
        main(["--output-dir", str(output), *args])
    assert error.value.code == 2 and not output.exists()
