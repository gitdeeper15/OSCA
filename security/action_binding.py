"""action_binding.py — Atomic binding of action to authorization."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass

from core.action import Action
from core.authorization import Authorization


@dataclass(frozen=True)
class ActionBinding:
    """A cryptographic binding of an action to its authorization."""
    action_fingerprint: str
    authorization_hash: str
    binding_hash: str

    @classmethod
    def create(cls, action: Action, authorization: Authorization) -> "ActionBinding":
        action_fp = action.fingerprint()
        auth_hash = hashlib.sha256(
            f"{authorization.decision.value}:{authorization.trace_id}".encode()
        ).hexdigest()
        binding_hash = hashlib.sha256(f"{action_fp}:{auth_hash}".encode()).hexdigest()
        return cls(
            action_fingerprint=action_fp,
            authorization_hash=auth_hash,
            binding_hash=binding_hash,
        )

    def verify(self, action: Action, authorization: Authorization) -> bool:
        expected = ActionBinding.create(action, authorization)
        return expected.binding_hash == self.binding_hash
