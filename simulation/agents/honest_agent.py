"""honest_agent.py — Proposes in-scope actions."""

from dataclasses import dataclass

from authority.consequence import Consequence, Reversibility
from authority.origin import Origin
from authority.semantic import Semantic
from core.action import Action


@dataclass
class HonestAgent:
    identity: str
    credential: str
    intent: str
    scope: list[str]

    def origin(self) -> Origin:
        return Origin(identity=self.identity, credential=self.credential)

    def semantic(self) -> Semantic:
        return Semantic(intent=self.intent, scope=self.scope)

    def consequence(self, action: Action) -> Consequence:
        return Consequence(
            effects=[f"file:{action.verb}"],
            reversibility=Reversibility.REVERSIBLE,
        )

    def propose(self, verb: str, target: str) -> Action:
        if target not in self.scope and "*" not in self.scope:
            raise ValueError(f"Refusing out-of-scope action: {target}")
        return Action(verb=verb, target=target)
