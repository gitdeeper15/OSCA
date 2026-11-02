"""escalation.py — Escalation of authorization decisions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Escalation:
    """An escalation of an authorization decision to a higher authority."""
    reason: str
    escalated_to: str
    original_decision: str
