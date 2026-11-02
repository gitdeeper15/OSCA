"""happy_path.py — Scenario: fully authorized action executes."""

from authority.consequence import Consequence, Reversibility
from authority.origin import Origin
from authority.semantic import Semantic
from core.action import Action
from core.authorization import Decision
from core.decision_engine import DecisionEngine
from core.execution_gateway import ExecutionGateway
from simulation.runner import ScenarioResult


def scenario() -> ScenarioResult:
    action = Action(verb="read", target="/data/file.txt")

    origin = Origin(identity="agent:123", credential="token_abc")
    semantic = Semantic(intent="read_file", scope=["/data/file.txt"])
    consequence = Consequence(
        effects=["file:read"], reversibility=Reversibility.REVERSIBLE,
    )

    engine = DecisionEngine()
    auth = engine.decide(
        action,
        origin.verify(action),
        semantic.verify(action),
        consequence.verify(action),
        trace_id="hp-001",
    )

    if auth.decision != Decision.AUTHORIZED:
        return ScenarioResult("happy_path", False,
            reason=f"Expected AUTHORIZED, got {auth.decision.value}")

    gateway = ExecutionGateway(lambda a: f"read:{a.target}")
    result = gateway.execute(action, auth)

    if not result.executed:
        return ScenarioResult("happy_path", False,
            reason=f"Expected executed=True, got {result.reason}")

    if result.output != "read:/data/file.txt":
        return ScenarioResult("happy_path", False,
            reason=f"Unexpected output: {result.output}")

    return ScenarioResult("happy_path", True,
        details={"output": result.output, "trace_id": auth.trace_id})
