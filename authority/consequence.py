"""
consequence.py — Consequence tier: what the action produces in the world.

The consequence tier establishes effects, side effects, reversibility, and
audit footprint. It is the third tier in the authorization chain.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from core.action import Action
from core.authorization import TierVerdict


class Reversibility(str):
    REVERSIBLE = "reversible"
    IRREVERSIBLE = "irreversible"
    CONDITIONAL = "conditional"


@dataclass(frozen=True)
class Consequence:
    """Consequence tier evidence."""
    effects: list[str] = field(default_factory=list)
    side_effects: list[str] = field(default_factory=list)
    reversibility: str = Reversibility.CONDITIONAL
    audit_footprint: dict = field(default_factory=dict)

    def verify(self, action: Action) -> TierVerdict:
        if not self.effects:
            return TierVerdict("consequence", False, "missing_effects")
        if self.reversibility not in (
            Reversibility.REVERSIBLE,
            Reversibility.IRREVERSIBLE,
            Reversibility.CONDITIONAL,
        ):
            return TierVerdict("consequence", False, "invalid_reversibility")
        return TierVerdict(
            "consequence", True, "ok",
            evidence={"effects": self.effects, "reversibility": self.reversibility},
        )
