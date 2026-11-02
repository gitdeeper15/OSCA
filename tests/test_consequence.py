"""Tests for authority/consequence.py"""

import pytest

from authority.consequence import Consequence, Reversibility
from core.action import Action


@pytest.fixture
def action():
    return Action(verb="read", target="/data/file.txt")


def test_consequence_valid(action):
    consequence = Consequence(effects=["file:read"])
    verdict = consequence.verify(action)
    assert verdict.passed is True
    assert verdict.tier == "consequence"


def test_consequence_missing_effects(action):
    consequence = Consequence(effects=[])
    verdict = consequence.verify(action)
    assert verdict.passed is False
    assert "missing_effects" in verdict.reason


def test_consequence_reversible(action):
    consequence = Consequence(effects=["file:read"], reversibility=Reversibility.REVERSIBLE)
    verdict = consequence.verify(action)
    assert verdict.passed is True
    assert verdict.evidence["reversibility"] == "reversible"


def test_consequence_irreversible(action):
    consequence = Consequence(effects=["file:delete"], reversibility=Reversibility.IRREVERSIBLE)
    verdict = consequence.verify(action)
    assert verdict.passed is True
    assert verdict.evidence["reversibility"] == "irreversible"


def test_consequence_invalid_reversibility(action):
    consequence = Consequence(effects=["file:read"], reversibility="unknown")
    verdict = consequence.verify(action)
    assert verdict.passed is False
    assert "invalid_reversibility" in verdict.reason


def test_consequence_side_effects(action):
    consequence = Consequence(
        effects=["file:read"],
        side_effects=["log:write"],
    )
    verdict = consequence.verify(action)
    assert verdict.passed is True


def test_consequence_audit_footprint(action):
    consequence = Consequence(
        effects=["file:read"],
        audit_footprint={"user": "agent:123", "timestamp": "2026-01-01"},
    )
    assert consequence.audit_footprint["user"] == "agent:123"
    assert consequence.verify(action).passed is True
