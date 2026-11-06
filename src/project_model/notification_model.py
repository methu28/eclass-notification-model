"""Mesa notification-ordering model, with repeated six-hour updates."""
from __future__ import annotations

from statistics import mean

import mesa

from .dataset import NotificationRecord
from .notification_agent import NotificationAgent
from .ordering import order_notifications


class NotificationModel(mesa.Model):
    """Fixed-population Mesa model comparing a platform-level ordering policy.

    No new notifications are generated after initialization. Every step
    advances time and updates deadline urgency; the model then reorders the
    same 20 agents and records the top-five opportunity for encounter.
    """

    def __init__(
        self,
        records: list[NotificationRecord],
        policy: str,
        reserved_urgent_positions: int = 2,
        hours_per_step: int = 6,
        urgency_threshold_hours: int = 72,
        visible_positions: int = 5,
        seed: int = 42,
    ):
        super().__init__(seed=seed)
        if policy not in {"recency", "hybrid"}:
            raise ValueError("policy must be 'recency' or 'hybrid'")
        if len(records) != 20:
            raise ValueError("This DEL02 slice uses exactly 20 notifications")
        if hours_per_step <= 0 or urgency_threshold_hours <= 0:
            raise ValueError("Step and urgency threshold must be positive")
        if not 0 <= reserved_urgent_positions <= visible_positions:
            raise ValueError("Reserved positions must be between 0 and visible positions")
        if visible_positions <= 0 or visible_positions > len(records):
            raise ValueError("Invalid number of visible positions")

        self.policy = policy
        self.reserved_urgent_positions = reserved_urgent_positions
        self.hours_per_step = hours_per_step
        self.urgency_threshold_hours = urgency_threshold_hours
        self.visible_positions = visible_positions
        self.step_index = 0
        self.elapsed_hours = 0
        self.ordered_agents: list[NotificationAgent] = []

        # Keep strong references to every agent, independent of Mesa registry internals.
        self.notification_agents = [NotificationAgent(self, record) for record in records]

        self.datacollector = mesa.DataCollector(
            model_reporters={
                "step": "step_index",
                "elapsed_hours": "elapsed_hours",
                "policy": "policy",
                "urgent_total": "urgent_total",
                "urgent_top5_count": "urgent_top5_count",
                "urgent_top5_share": "urgent_top5_share",
                "average_urgent_rank": "average_urgent_rank",
                "recent_nonurgent_top5": "recent_nonurgent_top5",
                "initial_recent_nonurgent_top5": "initial_recent_nonurgent_top5",
                "top_five_ids": "top_five_ids",
            },
            agent_reporters={
                "notification_id": "notification_id",
                "category": "category",
                "urgent": "urgent",
                "rank": "rank",
                "in_top_five": "in_top_five",
                "posted_hours_ago": "posted_hours_ago",
                "hours_until_deadline": "hours_until_deadline",
            },
        )
        self._order_and_record()  # Initial snapshot: step 0, elapsed_hours 0

    @property
    def urgent_total(self) -> int:
        return sum(agent.urgent for agent in self.agents)

    @property
    def urgent_top5_count(self) -> int:
        return sum(agent.urgent and agent.in_top_five for agent in self.agents)

    @property
    def urgent_top5_share(self) -> float:
        total = self.urgent_total
        return self.urgent_top5_count / total if total else 0.0

    @property
    def average_urgent_rank(self) -> float:
        positions = [a.rank for a in self.agents if a.urgent]
        return mean(positions) if positions else float("nan")

    @property
    def recent_nonurgent_top5(self) -> int:
        return sum(
            a.in_top_five and not a.urgent and a.posted_hours_ago <= 24
            for a in self.agents
        )

    @property
    def initial_recent_nonurgent_top5(self) -> int:
        return sum(a.in_top_five and a.initially_recent_nonurgent for a in self.agents)

    @property
    def top_five_ids(self) -> str:
        return "|".join(a.notification_id for a in self.ordered_agents[: self.visible_positions])

    def _order_and_record(self) -> None:
        self.ordered_agents = order_notifications(
            self.agents,
            self.policy,
            self.reserved_urgent_positions,
        )
        assert len(self.ordered_agents) == 20
        for rank, agent in enumerate(self.ordered_agents, start=1):
            agent.rank = rank
            agent.in_top_five = rank <= self.visible_positions
        assert sum(a.in_top_five for a in self.agents) == self.visible_positions
        self.datacollector.collect(self)

    def step(self) -> None:
        """Advance by a fixed number of simulated hours, then rerank and collect."""
        self.step_index += 1
        self.elapsed_hours += self.hours_per_step
        self.agents.do("step")  # Mesa 3 AgentSet activation, no random shuffle
        self._order_and_record()
