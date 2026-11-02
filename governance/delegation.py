"""delegation.py — Delegation of authority between agents."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(frozen=True)
class Delegation:
    """A delegation of authority from one agent to another."""
    delegator: str
    delegate: str
    scope: list[str] = field(default_factory=list)
    issued_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    expires_at: datetime | None = None

    def is_active(self) -> bool:
        if self.expires_at is None:
            return True
        return datetime.now(timezone.utc) < self.expires_at
