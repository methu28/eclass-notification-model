"""Mesa agent representing one passive course-notification entity."""
from __future__ import annotations

import mesa

from .dataset import NotificationRecord
from .ordering import is_urgent


class NotificationAgent(mesa.Agent):
    """An entity whose time-based state updates; it does not choose its rank."""

    def __init__(self, model: mesa.Model, record: NotificationRecord):
        super().__init__(model)
        self.notification_id = record.notification_id
        self.category = record.category
        self.posted_hours_ago = record.posted_hours_ago
        self.hours_until_deadline = record.deadline_hours_remaining
        self.initially_recent_nonurgent = (
            record.posted_hours_ago <= 24
            and not is_urgent(record.deadline_hours_remaining, model.urgency_threshold_hours)
        )
        self.urgent = is_urgent(self.hours_until_deadline, model.urgency_threshold_hours)
        self.rank = 0
        self.in_top_five = False

    def step(self) -> None:
        hours = self.model.hours_per_step
        self.posted_hours_ago += hours
        if self.hours_until_deadline is not None:
            self.hours_until_deadline -= hours
        self.urgent = is_urgent(self.hours_until_deadline, self.model.urgency_threshold_hours)
