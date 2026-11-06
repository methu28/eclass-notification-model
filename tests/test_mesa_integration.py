"""Run only when Mesa is installed. No fallback Mesa implementation is shipped."""
from pathlib import Path

import pytest

mesa = pytest.importorskip("mesa")

from src.project_model.dataset import load_notifications
from src.project_model.notification_agent import NotificationAgent
from src.project_model.notification_model import NotificationModel


DATA = Path(__file__).resolve().parents[1] / "data" / "notifications.csv"


def test_real_mesa_agent_model_and_collection():
    records = load_notifications(DATA)
    baseline = NotificationModel(records, "recency")
    hybrid = NotificationModel(records, "hybrid", reserved_urgent_positions=2)
    assert isinstance(baseline, mesa.Model)
    assert all(isinstance(agent, mesa.Agent) for agent in baseline.agents)
    assert len(baseline.agents) == 20
    assert baseline.urgent_total == 4
    assert baseline.urgent_top5_count == 0
    assert hybrid.urgent_top5_count == 2
    assert hybrid.initial_recent_nonurgent_top5 == 3
    for _ in range(6):
        baseline.step()
        hybrid.step()
    assert baseline.elapsed_hours == hybrid.elapsed_hours == 36
    assert baseline.urgent_total == hybrid.urgent_total == 8
    assert len(baseline.datacollector.get_model_vars_dataframe()) == 7
    assert len(hybrid.datacollector.get_model_vars_dataframe()) == 7
    assert all(agent.hours_until_deadline is None or agent.hours_until_deadline > 0 for agent in hybrid.agents)
    assert sorted(agent.rank for agent in hybrid.agents) == list(range(1, 21))
    assert baseline.urgent_top5_count == 0
    assert hybrid.urgent_top5_count == 2


def test_repeated_mesa_run_is_deterministic():
    records = load_notifications(DATA)
    a = NotificationModel(records, "hybrid", seed=42)
    b = NotificationModel(records, "hybrid", seed=42)
    for _ in range(6):
        a.step()
        b.step()
    assert a.datacollector.get_model_vars_dataframe().equals(
        b.datacollector.get_model_vars_dataframe()
    )
