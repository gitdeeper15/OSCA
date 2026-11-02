"""Tests for authority/origin.py"""

import pytest
from datetime import datetime, timezone

from authority.origin import Origin
from core.action import Action


@pytest.fixture
def action():
    return Action(verb="read", target="/data/file.txt")


def test_origin_valid(action):
    origin = Origin(identity="agent:123", credential="token_abc")
    verdict = origin.verify(action)
    assert verdict.passed is True
    assert verdict.tier == "origin"
    assert verdict.reason == "ok"


def test_origin_missing_identity(action):
    origin = Origin(identity="", credential="token_abc")
    verdict = origin.verify(action)
    assert verdict.passed is False
    assert "missing_identity" in verdict.reason


def test_origin_missing_credential(action):
    origin = Origin(identity="agent:123", credential="")
    verdict = origin.verify(action)
    assert verdict.passed is False
    assert "missing_credential" in verdict.reason


def test_origin_evidence(action):
    origin = Origin(identity="agent:123", credential="token_abc")
    verdict = origin.verify(action)
    assert verdict.evidence["identity"] == "agent:123"
    assert "timestamp" in verdict.evidence


def test_origin_timestamp_default(action):
    origin = Origin(identity="agent:123", credential="token_abc")
    assert origin.timestamp is not None
    assert origin.timestamp.tzinfo == timezone.utc


def test_origin_timestamp_custom(action):
    ts = datetime(2026, 1, 1, tzinfo=timezone.utc)
    origin = Origin(identity="agent:123", credential="token_abc", timestamp=ts)
    assert origin.timestamp == ts


def test_origin_nonce(action):
    origin = Origin(identity="agent:123", credential="token_abc", nonce="unique_001")
    assert origin.nonce == "unique_001"
    assert origin.verify(action).passed is True


def test_origin_attestation(action):
    origin = Origin(
        identity="agent:123",
        credential="token_abc",
        attestation="sgx_quote_xyz",
    )
    assert origin.attestation == "sgx_quote_xyz"
    assert origin.verify(action).passed is True
