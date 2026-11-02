"""
semantic.py — Semantic tier: what the action means in context.

The semantic tier establishes intent, scope, constraints, and preconditions.
It is the second tier in the authorization chain.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from core.action import Action
from core.authorization import TierVerdict


@dataclass(frozen=True)
class Semantic:
    """Semantic tier evidence."""
    intent: str
    scope: list[str] = field(default_factory=list)
    constraints: dict = field(default_factory=dict)
    preconditions: list[str] = field(default_factory=list)

    def verify(self, action: Action) -> TierVerdict:
        if not self.intent:
            return TierVerdict("semantic", False, "missing_intent")
        if not self.scope:
            return TierVerdict("semantic", False, "missing_scope")
        if action.target not in self.scope and "*" not in self.scope:
            return TierVerdict(
                "semantic", False, "target_out_of_scope",
                evidence={"target": action.target, "scope": self.scope},
            )
        return TierVerdict(
            "semantic", True, "ok",
            evidence={"intent": self.intent, "scope": self.scope},
        )
