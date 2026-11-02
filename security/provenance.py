"""provenance.py — Provenance tracking for actions and decisions."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Provenance:
    """A provenance record for a single action."""
    action_id: str
    source: str
    parent_action_id: str | None = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    metadata: dict = field(default_factory=dict)
