"""Tests for core/execution_gateway.py and security/action_binding.py"""

import pytest

from core.action import Action
from core.authorization import Authorization, Decision
from core.execution_gateway import ExecutionGateway, ExecutionResult
from security.action_binding import ActionBinding


@pytest.fixture
def action():
    return Action(verb="read", target="/data/file.txt")


@pytest.fixture
def authorized():
    return Authorization(decision=Decision.AUTHORIZED, tiers=(), trace_id="t1")


@pytest.fixture
def denied():
    return Authorization(decision=Decision.DENIED, tiers=(), trace_id="t2")


# ---------- ExecutionGateway ----------

def test_gateway_executes_when_authorized(action, authorized):
    def executor(a):
        return f"read:{a.target}"

    gateway = ExecutionGateway(executor)
    result = gateway.execute(action, authorized)
    assert result.executed is True
    assert result.output == "read:/data/file.txt"
    assert result.reason == "ok"


def test_gateway_refuses_when_denied(action, denied):
    def executor(a):
        return "should_not_run"

    gateway = ExecutionGateway(executor)
    result = gateway.execute(action, denied)
    assert result.executed is False
    assert "Not authorized" in result.reason


def test_gateway_captures_executor_exception(action, authorized):
    def executor(a):
        raise RuntimeError("boom")

    gateway = ExecutionGateway(executor)
    result = gateway.execute(action, authorized)
    assert result.executed is False
    assert "RuntimeError" in result.reason


def test_execution_result_dataclass():
    r = ExecutionResult(executed=True, output=42, reason="ok")
    assert r.executed is True
    assert r.output == 42
    assert r.reason == "ok"


# ---------- ActionBinding ----------

def test_action_binding_create(action, authorized):
    binding = ActionBinding.create(action, authorized)
    assert binding.action_fingerprint == action.fingerprint()
    assert len(binding.binding_hash) == 64


def test_action_binding_verify_ok(action, authorized):
    binding = ActionBinding.create(action, authorized)
    assert binding.verify(action, authorized) is True


def test_action_binding_verify_tampered_action(action, authorized):
    binding = ActionBinding.create(action, authorized)
    other = Action(verb="write", target="/data/file.txt")
    assert binding.verify(other, authorized) is False
