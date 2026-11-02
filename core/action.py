"""
action.py — The atomic unit of authorized execution.

An Action is the object that the three tiers (origin, semantic, consequence)
each evaluate. It carries the intent, the parameters, and the target.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Action:
    """A single action proposed by an agent."""

    verb: str
    target: str
    parameters: dict[str, Any] = field(default_factory=dict)
    context: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.verb:
            raise ValueError("Action verb must be non-empty.")
        if not self.target:
            raise ValueError("Action target must be non-empty.")

    def fingerprint(self) -> str:
        """Return a stable fingerprint for the action (for binding)."""
        import hashlib
        import json
        payload = json.dumps(
            {"verb": self.verb, "target": self.target, "params": self.parameters},
            sort_keys=True, default=str,
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()
