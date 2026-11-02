"""Tests for authority/semantic.py"""

import pytest

from authority.semantic import Semantic
from core.action import Action


@pytest.fixture
def action():
    return Action(verb="read", target="/data/file.txt")


def test_semantic_valid(action):
    semantic = Semantic(intent="read_file", scope=["/data/file.txt"])
    verdict = semantic.verify(action)
    assert verdict.passed is True
    assert verdict.tier == "semantic"


def test_semantic_missing_intent(action):
    semantic = Semantic(intent="", scope=["/data/file.txt"])
    verdict = semantic.verify(action)
    assert verdict.passed is False
    assert "missing_intent" in verdict.reason


def test_semantic_missing_scope(action):
    semantic = Semantic(intent="read_file", scope=[])
    verdict = semantic.verify(action)
    assert verdict.passed is False
    assert "missing_scope" in verdict.reason


def test_semantic_target_out_of_scope(action):
    semantic = Semantic(intent="read_file", scope=["/other/path"])
    verdict = semantic.verify(action)
    assert verdict.passed is False
    assert "target_out_of_scope" in verdict.reason


def test_semantic_wildcard_scope(action):
    semantic = Semantic(intent="read_file", scope=["*"])
    verdict = semantic.verify(action)
    assert verdict.passed is True


def test_semantic_evidence(action):
    semantic = Semantic(intent="read_file", scope=["/data/file.txt"])
    verdict = semantic.verify(action)
    assert verdict.evidence["intent"] == "read_file"
    assert "/data/file.txt" in verdict.evidence["scope"]


def test_semantic_constraints(action):
    semantic = Semantic(
        intent="read_file",
        scope=["/data/file.txt"],
        constraints={"max_size": "1MB"},
    )
    verdict = semantic.verify(action)
    assert verdict.passed is True


def test_semantic_preconditions(action):
    semantic = Semantic(
        intent="read_file",
        scope=["/data/file.txt"],
        preconditions=["user_authenticated"],
    )
    verdict = semantic.verify(action)
    assert verdict.passed is True
