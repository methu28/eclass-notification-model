"""CLI: run recency and hybrid Mesa models and save comparable outputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import mesa
import pandas as pd

from .dataset import load_notifications
from .notification_model import NotificationModel


ROOT = Path(__file__).resolve().parents[2]


def run_condition(records, policy, steps, hours_per_step, reserved, seed):
    model = NotificationModel(
        records=records,
        policy=policy,
        reserved_urgent_positions=reserved,
        hours_per_step=hours_per_step,
        seed=seed,
    )
    for _ in range(steps):
        model.step()
    results = model.datacollector.get_model_vars_dataframe().reset_index(drop=True)
    agent_states = model.datacollector.get_agent_vars_dataframe().reset_index()
    return model, results, agent_states


def save_plot(df: pd.DataFrame, policy: str, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(df["elapsed_hours"], df["urgent_top5_count"], marker="o", linewidth=2)
    ax.set(xlabel="Simulated hours elapsed", ylabel="Urgent notifications in top five",
           title=f"Top-five urgent visibility: {policy}")
    ax.set_ylim(0, 5)
    ax.set_yticks(range(0, 6))
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def save_comparison_plot(baseline: pd.DataFrame, alternative: pd.DataFrame, path: Path) -> None:
    fig, ax = plt.subplots(figsize=(8, 4.6))
    for label, df in [("Recency", baseline), ("Hybrid (2 reserved)", alternative)]:
        ax.plot(df["elapsed_hours"], df["urgent_top5_count"], marker="o", linewidth=2, label=label)
    ax.set(xlabel="Simulated hours elapsed", ylabel="Urgent notifications in top five",
           title="Top-five visibility under two ordering policies")
    ax.set_ylim(0, 5)
    ax.set_yticks(range(0, 6))
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run DEL02 eClass-style Mesa comparison")
    parser.add_argument("--input", type=Path, default=ROOT / "data" / "notifications.csv")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "outputs")
    parser.add_argument("--steps", type=int, default=6)
    parser.add_argument("--hours-per-step", type=int, default=6)
    parser.add_argument("--reserved", type=int, default=2)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args(argv)
    if args.steps < 1 or args.hours_per_step < 1:
        parser.error("steps and hours-per-step must be positive")
    if not 0 <= args.reserved <= 5:
        parser.error("reserved must be between 0 and 5")
    records = load_notifications(args.input)
    deadlines = [r.deadline_hours_remaining for r in records if r.deadline_hours_remaining is not None]
    if args.steps * args.hours_per_step >= min(deadlines):
        parser.error("Simulation would reach an overdue deadline; this slice excludes overdue items")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    outputs = {}
    for policy, prefix in [("recency", "baseline"), ("hybrid", "alternative")]:
        model, df, agent_df = run_condition(
            records, policy, args.steps, args.hours_per_step, args.reserved, args.seed
        )
        df.to_csv(args.output_dir / f"{prefix}_raw_00_urgent_visibility.csv", index=False)
        agent_df.to_csv(args.output_dir / f"{prefix}_raw_01_agent_states.csv", index=False)
        save_plot(df, policy, args.output_dir / f"{prefix}_processed_00_urgent_visibility.png")
        outputs[policy] = df
        print(f"{policy.upper()} ({len(model.agents)} agents):")
        print(df[["step", "elapsed_hours", "urgent_total", "urgent_top5_count", "initial_recent_nonurgent_top5"]].to_string(index=False))
        print()

    baseline = outputs["recency"]
    alternative = outputs["hybrid"]
    if baseline["urgent_total"].tolist() != alternative["urgent_total"].tolist():
        raise AssertionError("Unfair comparison: different urgency trajectories")
    save_comparison_plot(
        baseline, alternative,
        args.output_dir / "comparison_processed_00_urgent_visibility.png",
    )
    difference = alternative[["step", "elapsed_hours", "urgent_top5_count", "initial_recent_nonurgent_top5"]].copy()
    difference = difference.rename(columns={
        "urgent_top5_count": "hybrid_urgent_top5",
        "initial_recent_nonurgent_top5": "hybrid_initial_recent_nonurgent_top5",
    })
    difference["recency_urgent_top5"] = baseline["urgent_top5_count"]
    difference["recency_initial_recent_nonurgent_top5"] = baseline["initial_recent_nonurgent_top5"]
    difference["urgent_visibility_difference"] = difference["hybrid_urgent_top5"] - difference["recency_urgent_top5"]
    difference.to_csv(args.output_dir / "comparison_processed_01_visibility_differences.csv", index=False)
    metadata = {
        "mesa_version": getattr(mesa, "__version__", "unknown"),
        "model_type": "Mesa agent-based selective representation",
        "input_file": str(args.input),
        "initial_notifications": 20,
        "initial_urgent": 4,
        "steps": args.steps,
        "hours_per_step": args.hours_per_step,
        "hybrid_reserved_urgent_positions": args.reserved,
        "top_visible_positions": 5,
        "urgency_threshold_hours": 72,
        "seed": args.seed,
        "same_input_for_both_conditions": True,
        "interpretation_limit": "Synthetic model outputs; not evidence of eClass internal ordering or student behavior.",
    }
    (args.output_dir / "run_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote Mesa results and figures to: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
