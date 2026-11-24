"""Compare the existing recency rule with hybrid reservations of 1, 2, and 3."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import mesa
import pandas as pd

from .dataset import load_notifications
from .run_comparison import ROOT, run_condition


CONDITIONS = (
    ("recency", "Recency (baseline)", "recency", 0),
    ("hybrid_1", "Hybrid (1 reserved)", "hybrid", 1),
    ("hybrid_2", "Hybrid (2 reserved)", "hybrid", 2),
    ("hybrid_3", "Hybrid (3 reserved)", "hybrid", 3),
)
METRICS = {
    "urgent_top5_count": "Urgent notifications in top five",
    "urgent_top5_share": "Share of all urgent notifications in top five",
    "average_urgent_rank": "Average urgent rank (lower is better)",
    "recent_nonurgent_top5": "Currently recent nonurgent notifications in top five",
    "initial_recent_nonurgent_top5": "Initial recent nonurgent cohort in top five",
}
STYLES = (("#333333", "o", "-"), ("#0072B2", "s", "--"),
          ("#D55E00", "^", "-."), ("#009E73", "D", ":"))


def plot_metric(ax, results, metric):
    for (key, label, _, _), (color, marker, linestyle) in zip(CONDITIONS, STYLES):
        df = results[key]
        ax.plot(df["elapsed_hours"], df[metric], label=label, color=color,
                marker=marker, linestyle=linestyle, linewidth=2, markersize=5)
    ax.set(xlabel="Simulated hours elapsed", ylabel=METRICS[metric])
    ax.set_xticks(results["recency"]["elapsed_hours"])
    if metric == "urgent_top5_share":
        ax.set_ylim(0, 1)
        ax.yaxis.set_major_formatter(PercentFormatter(1))
    elif metric == "average_urgent_rank":
        ax.set_ylim(1, 20)
    else:
        ax.set_ylim(0, 5)
        ax.set_yticks(range(6))
    ax.grid(alpha=0.25)


def save_figures(results, output_dir):
    for metric in METRICS:
        fig, ax = plt.subplots(figsize=(9, 5.5))
        plot_metric(ax, results, metric)
        ax.set_title("DEL03: " + METRICS[metric])
        ax.legend(loc="best")
        fig.tight_layout()
        fig.savefig(output_dir / f"comparison_processed_{metric}.png", dpi=160)
        plt.close(fig)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    for ax, metric in zip(axes.flat, list(METRICS)[:4]):
        plot_metric(ax, results, metric)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=4)
    fig.suptitle("DEL03: four ordering conditions, one fixed synthetic dataset")
    fig.tight_layout(rect=(0, 0.05, 1, 0.96))
    fig.savefig(output_dir / "comparison_processed_overview.png", dpi=160)
    plt.close(fig)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=ROOT / "data/notifications.csv")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "outputs/del03")
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--hours-per-step", type=int, default=6)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args(argv)
    if args.steps < 1 or args.hours_per_step < 1:
        parser.error("steps and hours-per-step must be positive")
    records = load_notifications(args.input)
    deadlines = [r.deadline_hours_remaining for r in records
                 if r.deadline_hours_remaining is not None]
    if args.steps * args.hours_per_step >= min(deadlines):
        parser.error("Simulation would reach an overdue deadline; this slice excludes overdue items")
    if args.output_dir.exists() and (not args.output_dir.is_dir() or any(args.output_dir.iterdir())):
        parser.error("Output directory must be new or empty; refusing to overwrite existing results")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    results, frames, summaries = {}, [], []
    reference_states = None
    state_columns = ["Step", "AgentID", "notification_id", "category", "urgent",
                     "posted_hours_ago", "hours_until_deadline"]
    for key, label, policy, reserved in CONDITIONS:
        model, df, agents = run_condition(
            records, policy, args.steps, args.hours_per_step, reserved, args.seed
        )
        assert model.urgency_threshold_hours == 72 and model.visible_positions == 5
        if reference_states is None:
            reference_states = agents[state_columns]
        else:
            pd.testing.assert_frame_equal(reference_states, agents[state_columns], check_exact=True)
        df.to_csv(args.output_dir / f"{key}_raw_model.csv", index=False)
        agents.to_csv(args.output_dir / f"{key}_raw_agent_states.csv", index=False)
        results[key] = df
        frames.append(df.assign(condition=key, condition_label=label,
                                reserved_urgent_positions=reserved))
        summary = {"condition": key, "condition_label": label, "snapshots": len(df)}
        for metric in METRICS:
            summary.update({f"{metric}_initial": df[metric].iloc[0],
                            f"{metric}_final": df[metric].iloc[-1],
                            f"{metric}_snapshot_mean": df[metric].mean()})
        summaries.append(summary)

    combined = pd.concat(frames, ignore_index=True)
    combined.to_csv(args.output_dir / "comparison_raw_model_metrics.csv", index=False)
    wide = results["recency"][["step", "elapsed_hours", "urgent_total"]].copy()
    for key, _, _, _ in CONDITIONS:
        for metric in METRICS:
            wide[f"{key}_{metric}"] = results[key][metric]
    wide.to_csv(args.output_dir / "comparison_processed_metrics_wide.csv", index=False)
    summary_df = pd.DataFrame(summaries)
    summary_df.to_csv(args.output_dir / "comparison_processed_summary.csv", index=False)
    save_figures(results, args.output_dir)
    metadata = {
        "python_version": platform.python_version(), "mesa_version": mesa.__version__,
        "pandas_version": pd.__version__, "matplotlib_version": matplotlib.__version__,
        "input_file": args.input.resolve().relative_to(ROOT).as_posix()
        if args.input.resolve().is_relative_to(ROOT) else str(args.input.resolve()),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "initial_notifications": len(records), "initial_urgent": 4,
        "urgency_threshold_hours": 72, "visible_positions": 5,
        "recent_window_hours": 24, "steps": args.steps,
        "hours_per_step": args.hours_per_step, "seed": args.seed,
        "conditions": [{"condition": key, "label": label, "policy": policy,
                        "reserved_urgent_positions": reserved}
                       for key, label, policy, reserved in CONDITIONS],
        "same_input_and_time_states_verified": True,
        "summary_mean_definition": "Unweighted mean of recorded snapshots including step 0; not independent replications or a continuous-time average.",
        "interpretation_limit": "One deterministic synthetic scenario; visibility is list position, not student attention or actual eClass behavior.",
    }
    (args.output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )
    print(wide.to_string(index=False))
    print(f"Wrote four-condition results to: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
