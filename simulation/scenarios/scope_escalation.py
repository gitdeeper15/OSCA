"""scope_escalation.py — Scenario: out-of-scope action denied."""

from authority.consequence import Consequence, Reversibility
from authority.origin import Origin
from authority.semantic import Semantic
from core.action import Action
from core.authorization import Decision
from core.decision_engine import DecisionEngine
from core.execution_gateway import ExecutionGateway
from simulation.runner import ScenarioResult


def scenario() -> ScenarioResult:
    action = Action(verb="read", target="/etc/passwd")

    origin = Origin(identity="agent:123", credential="token_abc")
    semantic = Semantic(intent="read_file", scope=["/data/file.txt"])
    consequence = Consequence(
        effects=["file:read"], reversibility=Reversibility.REVERSIBLE,
    )

    v_origin = origin.verify(action)
    v_semantic = semantic.verify(action)
    v_consequence = consequence.verify(action)

    if v_semantic.passed:
        return ScenarioResult("scope_escalation", False,
            reason="Semantic tier should have failed")

    engine = DecisionEngine()
    auth = engine.decide(action, v_origin, v_semantic, v_consequence, trace_id="se-001")

    if auth.decision != Decision.DENIED:
        return ScenarioResult("scope_escalation", False,
            reason=f"Expected DENIED, got {auth.decision.value}")

    executed = {"ran": False}
    def executor(a):
        executed["ran"] = True
        return "should_not_run"

    gateway = ExecutionGateway(executor)
    result = gateway.execute(action, auth)

    if result.executed or executed["ran"]:
        return ScenarioResult("scope_escalation", False,
            reason="Executor ran despite DENIED")

    return ScenarioResult("scope_escalation", True,
        details={"semantic_reason": v_semantic.reason, "decision": auth.decision.value})
