"""Load and validate the fixed, fictional notification dataset."""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from .ordering import is_urgent


@dataclass(frozen=True)
class NotificationRecord:
    notification_id: str
    category: str
    posted_hours_ago: float
    deadline_hours_remaining: float | None


def load_notifications(path: str | Path) -> list[NotificationRecord]:
    with Path(path).open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"notification_id", "category", "posted_hours_ago", "deadline_hours_remaining"}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError(f"Input CSV must contain: {sorted(required)}")
        records = []
        for row in reader:
            raw_deadline = (row["deadline_hours_remaining"] or "").strip()
            deadline = float(raw_deadline) if raw_deadline else None
            record = NotificationRecord(
                notification_id=row["notification_id"].strip(),
                category=row["category"].strip(),
                posted_hours_ago=float(row["posted_hours_ago"]),
                deadline_hours_remaining=deadline,
            )
            if not record.notification_id or not record.category:
                raise ValueError("Notification ID and category cannot be empty")
            if record.posted_hours_ago < 0:
                raise ValueError("Posting age must be nonnegative")
            if deadline is not None and deadline <= 0:
                raise ValueError("Initial deadlines must be in the future")
            records.append(record)
    if len(records) != 20:
        raise ValueError(f"DEL02 prototype expects exactly 20 notifications, found {len(records)}")
    if len({r.notification_id for r in records}) != len(records):
        raise ValueError("Duplicate notification IDs")
    urgent_count = sum(is_urgent(r.deadline_hours_remaining) for r in records)
    if urgent_count != 4:
        raise ValueError(f"Expected 4 initially urgent notifications, found {urgent_count}")
    return records
