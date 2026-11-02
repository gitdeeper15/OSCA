"""tamper_attack.py — Scenario: tampered action detected."""

from core.action import Action
from core.authorization import Authorization, Decision
from security.action_binding import ActionBinding
from simulation.runner import ScenarioResult


def scenario() -> ScenarioResult:
    action = Action(verb="read", target="/data/file.txt")
    auth = Authorization(decision=Decision.AUTHORIZED, tiers=(), trace_id="t1")
    binding = ActionBinding.create(action, auth)

    if not binding.verify(action, auth):
        return ScenarioResult("tamper_attack", False, reason="Original failed")

    tampered = Action(verb="write", target="/data/file.txt")
    if binding.verify(tampered, auth):
        return ScenarioResult("tamper_attack", False, reason="Tampered accepted")

    return ScenarioResult("tamper_attack", True, details={"tampered_rejected": True})
