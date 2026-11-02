"""tier_collusion.py — Scenario: two-tier collusion blocked."""

from core.action import Action
from core.authorization import Decision, TierVerdict
from core.decision_engine import DecisionEngine
from simulation.runner import ScenarioResult


def scenario() -> ScenarioResult:
    action = Action(verb="write", target="/data/critical.txt")

    origin = TierVerdict("origin", True, "ok", {"identity": "compromised"})
    semantic = TierVerdict("semantic", True, "ok", {"intent": "compromised"})
    consequence = TierVerdict("consequence", False, "missing_effects")

    engine = DecisionEngine()
    auth = engine.decide(action, origin, semantic, consequence, trace_id="tc-001")

    if auth.decision == Decision.AUTHORIZED:
        return ScenarioResult("tier_collusion", False,
            reason="Two colluding tiers bypassed the third")

    if auth.decision != Decision.DENIED:
        return ScenarioResult("tier_collusion", False,
            reason=f"Expected DENIED, got {auth.decision.value}")

    return ScenarioResult("tier_collusion", True,
        details={"failed_tier": consequence.tier, "decision": auth.decision.value})
