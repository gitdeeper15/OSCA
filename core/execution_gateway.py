"""
execution_gateway.py — Execute an action only if authorized.

The gateway enforces atomic execution binding: the action executes only
when all three tiers have authorized it. It does not re-evaluate the tiers.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from core.action import Action
from core.authorization import Authorization


@dataclass(frozen=True)
class ExecutionResult:
    """Result of attempting to execute an action."""
    executed: bool
    output: Any = None
    reason: str = ""


class ExecutionGateway:
    """Execute an action if and only if it is authorized."""

    def __init__(self, executor: Callable[[Action], Any]) -> None:
        self._executor = executor

    def execute(self, action: Action, authorization: Authorization) -> ExecutionResult:
        if not authorization.authorized:
            return ExecutionResult(
                executed=False,
                reason=f"Not authorized: {authorization.decision.value}",
            )
        try:
            output = self._executor(action)
            return ExecutionResult(executed=True, output=output, reason="ok")
        except Exception as e:
            return ExecutionResult(
                executed=False,
                reason=f"Execution error: {type(e).__name__}: {e}",
            )
