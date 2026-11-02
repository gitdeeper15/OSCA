"""replay_protection.py — Protect against replay attacks."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ReplayProtection:
    """Track seen nonces to reject replays."""
    _seen: set[str] = field(default_factory=set)

    def check_and_record(self, nonce: str) -> bool:
        """Return True if the nonce is fresh, False if it was seen before."""
        if nonce in self._seen:
            return False
        self._seen.add(nonce)
        return True
