"""Tests for core/authorization.py and core/decision_engine.py"""

import pytest

from core.action import Action
from core.authorization import Authorization, Decision, TierVerdict
from core.decision_engine import DecisionEngine


@pytest.fixture
def action():
    return Action(verb="read", target="/data/file.txt")


@pytest.fixture
def all_pass():
    return (
        TierVerdict("origin", True, "ok"),
        TierVerdict("semantic", True, "ok"),
        TierVerdict("consequence", True, "ok"),
    )


def test_decision_enum_values():
    assert Decision.AUTHORIZED.value == "authorized"
    assert Decision.DENIED.value == "denied"
    assert Decision.ESCALATED.value == "escalated"


def test_tier_verdict_dataclass():
    v = TierVerdict("origin", True, "ok", {"k": "v"})
    assert v.tier == "origin"
    assert v.passed is True
    assert v.reason == "ok"
    assert v.evidence["k"] == "v"


def test_authorization_authorized_flag():
    auth = Authorization(
        decision=Decision.AUTHORIZED,
        tiers=(),
        trace_id="trace_001",
    )
    assert auth.authorized is True
    assert auth.trace_id == "trace_001"


def test_authorization_denied_flag():
    auth = Authorization(decision=Decision.DENIED, tiers=())
    assert auth.authorized is False


def test_decision_engine_all_pass(action, all_pass):
    engine = DecisionEngine()
    auth = engine.decide(action, *all_pass, trace_id="t1")
    assert auth.decision == Decision.AUTHORIZED
    assert auth.authorized is True
    assert len(auth.tiers) == 3


def test_decision_engine_one_fail(action, all_pass):
    origin, semantic, consequence = all_pass
    bad = TierVerdict("semantic", False, "target_out_of_scope")
    engine = DecisionEngine()
    auth = engine.decide(action, origin, bad, consequence)
    assert auth.decision == Decision.DENIED
    assert auth.authorized is False


def test_decision_engine_escalated(action, all_pass):
    origin, semantic, consequence = all_pass
    escalate = TierVerdict("origin", False, "escalate_to_admin")
    engine = DecisionEngine()
    auth = engine.decide(action, escalate, semantic, consequence)
    assert auth.decision == Decision.ESCALATED


def test_decision_engine_multiple_fails(action, all_pass):
    origin, _, consequence = all_pass
    bad_semantic = TierVerdict("semantic", False, "missing_scope")
    bad_consequence = TierVerdict("consequence", False, "missing_effects")
    engine = DecisionEngine()
    auth = engine.decide(action, origin, bad_semantic, bad_consequence)
    assert auth.decision == Decision.DENIED
