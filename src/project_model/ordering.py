"""Pure, deterministic ordering policies used by the Mesa model.

This module deliberately does not import Mesa, so the ordering rules can be
verified independently of the agent framework.
"""
from __future__ import annotations

from typing import Iterable, Protocol, TypeVar


class SortableNotification(Protocol):
    notification_id: str
    posted_hours_ago: float
    urgent: bool


T = TypeVar("T", bound=SortableNotification)


def order_notifications(
    notifications: Iterable[T],
    policy: str,
    reserved_urgent_positions: int = 2,
) -> list[T]:
    """Return every notification exactly once, in the selected display order.

    Ties use notification_id so the result is deterministic across runs.
    Hybrid: reserve up to K positions for the most recently posted urgent
    items, then order *all remaining items* (including urgent ones) by recency.
    """
    items = list(notifications)
    if policy not in {"recency", "hybrid"}:
        raise ValueError(f"Unsupported policy: {policy!r}")
    if not isinstance(reserved_urgent_positions, int) or reserved_urgent_positions < 0:
        raise ValueError("reserved_urgent_positions must be a nonnegative integer")

    by_recency = lambda item: (item.posted_hours_ago, item.notification_id)
    if policy == "recency":
        return sorted(items, key=by_recency)

    selected = sorted((item for item in items if item.urgent), key=by_recency)[
        :reserved_urgent_positions
    ]
    selected_ids = {item.notification_id for item in selected}
    remaining = sorted(
        (item for item in items if item.notification_id not in selected_ids),
        key=by_recency,
    )
    result = selected + remaining
    if len(result) != len(items) or len({i.notification_id for i in result}) != len(items):
        raise AssertionError("Ordering lost or duplicated notifications")
    return result


def is_urgent(hours_until_deadline: float | None, threshold_hours: float = 72) -> bool:
    """An approaching, not overdue, deadline is urgent."""
    return hours_until_deadline is not None and 0 < hours_until_deadline <= threshold_hours
