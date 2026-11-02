"""runner.py — OSCA scenario runner."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class ScenarioResult:
    """Result of running one scenario."""
    name: str
    passed: bool
    details: dict = field(default_factory=dict)
    reason: str = ""


def run_scenario(name: str, fn: Callable[[], ScenarioResult]) -> ScenarioResult:
    try:
        result = fn()
        result.name = name
        return result
    except Exception as e:
        return ScenarioResult(
            name=name, passed=False,
            reason=f"Exception: {type(e).__name__}: {e}",
        )


def run_all(scenarios: dict[str, Callable[[], ScenarioResult]]) -> list[ScenarioResult]:
    return [run_scenario(name, fn) for name, fn in scenarios.items()]


def print_summary(results: list[ScenarioResult]) -> None:
    print("=" * 60)
    print("OSCA Simulation Summary")
    print("=" * 60)
    for r in results:
        status = "✅ PASS" if r.passed else "❌ FAIL"
        print(f"  {status}  {r.name}")
        if not r.passed and r.reason:
            print(f"         reason: {r.reason}")
    total = len(results)
    passed = sum(1 for r in results if r.passed)
    print("-" * 60)
    print(f"  {passed}/{total} scenarios passed")
    print("=" * 60)
