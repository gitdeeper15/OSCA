"""Adversarial tests for OSCA.

These tests check the invariants hold under hostile conditions:
  - compromised origin
  - semantic drift
  - consequence escalation
  - replay
"""

import pytest

from authority.origin import Origin
from authority.semantic import Semantic
from authority.consequence import Consequence, Reversibility
from core.action import Action
from core.authorization import Decision, TierVerdict
from core.decision_engine import DecisionEngine
from core.execution_gateway import ExecutionGateway
from security.action_binding import ActionBinding
from security.replay_protection import ReplayProtection


def test_compromised_origin_missing_credential():
    action = Action(verb="read", target="/data/file.txt")
    origin = Origin(identity="agent:123", credential="")
    verdict = origin.verify(action)
    assert verdict.passed is False
    assert "missing_credential" in verdict.reason


def test_semantic_drift_scope_escalation():
    """Attacker tries to read a target outside the declared scope."""
    action = Action(verb="read", target="/etc/passwd")
    semantic = Semantic(intent="read_file", scope=["/data/file.txt"])
    verdict = semantic.verify(action)
    assert verdict.passed is False
    assert "target_out_of_scope" in verdict.reason


def test_consequence_escalation_missing_effects():
    action = Action(verb="write", target="/data/file.txt")
    consequence = Consequence(effects=[])
    verdict = consequence.verify(action)
    assert verdict.passed is False
    assert "missing_effects" in verdict.reason


def test_non_override_all_tiers_required():
    """If any tier fails, the decision cannot be AUTHORIZED."""
    action = Action(verb="read", target="/data/file.txt")
    origin = TierVerdict("origin", True, "ok")
    semantic = TierVerdict("semantic", False, "target_out_of_scope")
    consequence = TierVerdict("consequence", True, "ok")
    engine = DecisionEngine()
    auth = engine.decide(action, origin, semantic, consequence)
    assert auth.decision == Decision.DENIED


def test_atomicity_gateway_does_not_run_when_denied():
    """Execution gateway must not execute if authorization is denied."""
    executed = {"ran": False}

    def executor(a):
        executed["ran"] = True
        return "ran"

    action = Action(verb="read", target="/data/file.txt")
    from core.authorization import Authorization
    denied = Authorization(decision=Decision.DENIED, tiers=(), trace_id="t")
    gateway = ExecutionGateway(executor)
    result = gateway.execute(action, denied)
    assert result.executed is False
    assert executed["ran"] is False


def test_replay_protection_rejects_second_use():
    rp = ReplayProtection()
    assert rp.check_and_record("nonce_001") is True
    assert rp.check_and_record("nonce_001") is False


def test_action_binding_detects_tampered_authorization():
    action = Action(verb="read", target="/data/file.txt")
    from core.authorization import Authorization
    auth1 = Authorization(decision=Decision.AUTHORIZED, tiers=(), trace_id="t1")
    auth2 = Authorization(decision=Decision.DENIED, tiers=(), trace_id="t1")
    binding = ActionBinding.create(action, auth1)
    assert binding.verify(action, auth1) is True
    assert binding.verify(action, auth2) is False


def test_full_pipeline_happy_path():
    """All three tiers pass, decision authorized, execution runs."""
    action = Action(verb="read", target="/data/file.txt")
    origin = Origin(identity="agent:123", credential="token_abc")
    semantic = Semantic(intent="read_file", scope=["/data/file.txt"])
    consequence = Consequence(effects=["file:read"], reversibility=Reversibility.REVERSIBLE)

    v_origin = origin.verify(action)
    v_semantic = semantic.verify(action)
    v_consequence = consequence.verify(action)

    engine = DecisionEngine()
    auth = engine.decide(action, v_origin, v_semantic, v_consequence, trace_id="t-full")

    assert auth.decision == Decision.AUTHORIZED
    assert auth.authorized is True

    gateway = ExecutionGateway(lambda a: f"read:{a.target}")
    result = gateway.execute(action, auth)
    assert result.executed is True
    assert result.output == "read:/data/file.txt"
