"""replay_attack.py — Scenario: nonce replay rejected."""

from authority.origin import Origin
from core.action import Action
from security.replay_protection import ReplayProtection
from simulation.runner import ScenarioResult


def scenario() -> ScenarioResult:
    action = Action(verb="read", target="/data/file.txt")
    origin = Origin(identity="agent:123", credential="token_abc", nonce="nonce_001")
    rp = ReplayProtection()

    if not rp.check_and_record(origin.nonce):
        return ScenarioResult("replay_attack", False, reason="First use rejected")

    if rp.check_and_record(origin.nonce):
        return ScenarioResult("replay_attack", False, reason="Replay accepted")

    return ScenarioResult("replay_attack", True, details={"replay_rejected": True})
