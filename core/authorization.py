"""
authorization.py — The authorization decision for a single action.

An Authorization aggregates the three tier verdicts (origin, semantic,
consequence) into a single decision. It does not execute the action.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Decision(str, Enum):
    AUTHORIZED = "authorized"
    DENIED = "denied"
    ESCALATED = "escalated"


@dataclass(frozen=True)
class TierVerdict:
    """Verdict from one tier."""
    tier: str
    passed: bool
    reason: str = ""
    evidence: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Authorization:
    """Aggregated authorization decision."""
    decision: Decision
    tiers: tuple[TierVerdict, ...]
    trace_id: str = ""

    @property
    def authorized(self) -> bool:
        return self.decision == Decision.AUTHORIZED
