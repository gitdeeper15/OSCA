"""
origin.py — Origin tier: who authorized the action.

The origin tier establishes identity, credential, and attestation.
It is the first tier in the authorization chain.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from core.action import Action
from core.authorization import TierVerdict


@dataclass(frozen=True)
class Origin:
    """Origin tier evidence."""
    identity: str
    credential: str
    attestation: str | None = None
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    nonce: str | None = None

    def verify(self, action: Action) -> TierVerdict:
        if not self.identity:
            return TierVerdict("origin", False, "missing_identity")
        if not self.credential:
            return TierVerdict("origin", False, "missing_credential")
        return TierVerdict(
            "origin", True, "ok",
            evidence={"identity": self.identity, "timestamp": self.timestamp.isoformat()},
        )
