from dataclasses import dataclass

import pytest

from src.project_model.ordering import is_urgent, order_notifications


@dataclass
class Item:
    notification_id: str
    posted_hours_ago: float
    urgent: bool


def example_items():
    return [
        Item("older_urgent", 30, True),
        Item("newer_general", 1, False),
        Item("newest_urgent", 20, True),
        Item("second_general", 2, False),
        Item("other_urgent", 40, True),
    ]


def test_recency_order():
    assert [x.notification_id for x in order_notifications(example_items(), "recency")] == [
        "newer_general", "second_general", "newest_urgent", "older_urgent", "other_urgent"
    ]


def test_hybrid_reserves_two_then_sorts_all_remaining_by_recency():
    assert [x.notification_id for x in order_notifications(example_items(), "hybrid", 2)] == [
        "newest_urgent", "older_urgent", "newer_general", "second_general", "other_urgent"
    ]


def test_hybrid_never_duplicates_agents():
    items = example_items()
    result = order_notifications(items, "hybrid", 4)
    assert len(result) == len(items)
    assert {x.notification_id for x in result} == {x.notification_id for x in items}


def test_zero_reserved_positions_matches_recency():
    items = example_items()
    assert order_notifications(items, "hybrid", 0) == order_notifications(items, "recency")


def test_urgency_threshold_boundaries():
    assert is_urgent(72)
    assert is_urgent(0.01)
    assert not is_urgent(72.01)
    assert not is_urgent(0)
    assert not is_urgent(-1)
    assert not is_urgent(None)


def test_invalid_policy_and_reservation():
    with pytest.raises(ValueError):
        order_notifications(example_items(), "urgency")
    with pytest.raises(ValueError):
        order_notifications(example_items(), "hybrid", -1)
