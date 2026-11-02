"""Tests for governance/escalation.py"""

from governance.escalation import Escalation


def test_escalation_dataclass():
    esc = Escalation(
        reason="ambiguous_scope",
        escalated_to="admin:001",
        original_decision="denied",
    )
    assert esc.reason == "ambiguous_scope"
    assert esc.escalated_to == "admin:001"
    assert esc.original_decision == "denied"


def test_escalation_immutability():
    esc = Escalation(reason="r", escalated_to="a", original_decision="d")
    try:
        esc.reason = "changed"
        assert False, "Should have raised FrozenInstanceError"
    except Exception:
        pass


def test_escalation_equality():
    e1 = Escalation(reason="r", escalated_to="a", original_decision="d")
    e2 = Escalation(reason="r", escalated_to="a", original_decision="d")
    assert e1 == e2


def test_escalation_repr():
    esc = Escalation(reason="r", escalated_to="a", original_decision="d")
    assert "Escalation" in repr(esc)


def test_escalation_empty_reason():
    esc = Escalation(reason="", escalated_to="a", original_decision="d")
    assert esc.reason == ""
