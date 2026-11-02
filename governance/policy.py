"""policy.py — Policy definitions governing authorization."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Policy:
    """A policy is a named set of rules governing authorization."""
    name: str
    rules: list[str] = field(default_factory=list)
    description: str = ""

    def applies_to(self, action_verb: str) -> bool:
        return not self.rules or action_verb in self.rules
