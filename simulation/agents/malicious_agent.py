"""malicious_agent.py — Proposes out-of-scope actions."""

from dataclasses import dataclass

from authority.consequence import Consequence, Reversibility
from authority.origin import Origin
from authority.semantic import Semantic
from core.action import Action


@dataclass
class MaliciousAgent:
    identity: str
    credential: str
    declared_intent: str
    declared_scope: list[str]

    def origin(self) -> Origin:
        return Origin(identity=self.identity, credential=self.credential)

    def semantic(self) -> Semantic:
        return Semantic(intent=self.declared_intent, scope=self.declared_scope)

    def consequence(self, action: Action) -> Consequence:
        return Consequence(
            effects=["file:read"],
            reversibility=Reversibility.REVERSIBLE,
        )

    def propose(self, verb: str, target: str) -> Action:
        return Action(verb=verb, target=target)
