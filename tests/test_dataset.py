from pathlib import Path

import pytest

from src.project_model.dataset import load_notifications
from src.project_model.ordering import is_urgent


DATA = Path(__file__).resolve().parents[1] / "data" / "notifications.csv"


def test_fixed_synthetic_dataset():
    records = load_notifications(DATA)
    assert len(records) == 20
    assert len({r.notification_id for r in records}) == 20
    assert sum(is_urgent(r.deadline_hours_remaining) for r in records) == 4
    assert sum(r.deadline_hours_remaining is None for r in records) == 12
    assert sum(r.deadline_hours_remaining is not None for r in records) == 8


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        load_notifications(DATA.parent / "not-a-file.csv")
