"""
decision_engine.py — Combine tier verdicts into an authorization decision.

The decision engine enforces the architectural invariants:
  - independence: each tier is evaluated without trusting the others
  - non-override: no tier can override another
  - atomicity: all tiers must pass, or the action is denied/escalated
"""

from __future__ import annotations

from core.action import Action
from core.authorization import Authorization, Decision, TierVerdict


class DecisionEngine:
    """Combine tier verdicts into a single authorization decision."""

    def decide(
        self,
        action: Action,
        origin_verdict: TierVerdict,
        semantic_verdict: TierVerdict,
        consequence_verdict: TierVerdict,
        trace_id: str = "",
    ) -> Authorization:
        verdicts = (origin_verdict, semantic_verdict, consequence_verdict)
        failed = [v for v in verdicts if not v.passed]

        if not failed:
            decision = Decision.AUTHORIZED
        elif any("escalate" in v.reason.lower() for v in failed):
            decision = Decision.ESCALATED
        else:
            decision = Decision.DENIED

        return Authorization(decision=decision, tiers=verdicts, trace_id=trace_id)
