# OSCA — Authorization Model

**OSCA — Origin, Semantic, and Consequence Authority**
*A Multi-Tier Authorization Architecture for Autonomous AI Agents*

---

## 1. Overview

OSCA separates authority into three independently verifiable tiers:

- **Origin** — who authorized the action.
- **Semantic** — what the action means in context.
- **Consequence** — what the action produces in the world.

An action is authorized if and only if **all three tiers pass**. No tier can override another. This is the architectural invariant that distinguishes OSCA from single-tier authorization systems.

---

## 2. The Three Tiers

### 2.1 Origin Tier

The origin tier establishes identity, credential, and attestation.

**Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `identity` | `str` | Yes | Agent, user, or service identifier (e.g., `agent:123`) |
| `credential` | `str` | Yes | Token, certificate, or attestation |
| `attestation` | `str \| None` | No | Optional hardware or software attestation |
| `timestamp` | `datetime` | Auto | UTC timestamp of origin declaration |
| `nonce` | `str \| None` | No | Optional nonce for replay protection |

**Verification:**

```python
def verify(self, action: Action) -> TierVerdict:
    if not self.identity:
        return TierVerdict("origin", False, "missing_identity")
    if not self.credential:
        return TierVerdict("origin", False, "missing_credential")
    return TierVerdict("origin", True, "ok", evidence={...})
```

Failure modes:

· missing_identity
· missing_credential

---

2.2 Semantic Tier

The semantic tier establishes intent, scope, constraints, and preconditions.

Fields:

Field Type Required Description
intent str Yes Intent label (e.g., read_file)
scope list[str] Yes Allowed targets (or *)
constraints dict No Numeric or string constraints
preconditions list[str] No Logical preconditions

Verification:

```python
def verify(self, action: Action) -> TierVerdict:
    if not self.intent:
        return TierVerdict("semantic", False, "missing_intent")
    if not self.scope:
        return TierVerdict("semantic", False, "missing_scope")
    if action.target not in self.scope and "*" not in self.scope:
        return TierVerdict("semantic", False, "target_out_of_scope", ...)
    return TierVerdict("semantic", True, "ok", evidence={...})
```

Failure modes:

· missing_intent
· missing_scope
· target_out_of_scope

---

2.3 Consequence Tier

The consequence tier establishes effects, side effects, reversibility, and audit footprint.

Fields:

Field Type Required Description
effects list[str] Yes Effects produced (e.g., file:read)
side_effects list[str] No Secondary effects (e.g., log:write)
reversibility str Yes reversible, irreversible, or conditional
audit_footprint dict No Audit metadata

Verification:

```python
def verify(self, action: Action) -> TierVerdict:
    if not self.effects:
        return TierVerdict("consequence", False, "missing_effects")
    if self.reversibility not in (REVERSIBLE, IRREVERSIBLE, CONDITIONAL):
        return TierVerdict("consequence", False, "invalid_reversibility")
    return TierVerdict("consequence", True, "ok", evidence={...})
```

Failure modes:

· missing_effects
· invalid_reversibility

---

3. Decision Engine

The decision engine aggregates the three tier verdicts into a single decision.

Decision outcomes:

Outcome Condition
AUTHORIZED All three tiers pass
DENIED At least one tier fails
ESCALATED At least one failed tier requests escalation

Code:

```python
class DecisionEngine:
    def decide(self, action, origin_verdict, semantic_verdict,
               consequence_verdict, trace_id=""):
        verdicts = (origin_verdict, semantic_verdict, consequence_verdict)
        failed = [v for v in verdicts if not v.passed]
        if not failed:
            decision = Decision.AUTHORIZED
        elif any("escalate" in v.reason.lower() for v in failed):
            decision = Decision.ESCALATED
        else:
            decision = Decision.DENIED
        return Authorization(decision=decision, tiers=verdicts, trace_id=trace_id)
```

---

4. Execution Gateway

The execution gateway executes an action if and only if it is authorized.

Atomicity guarantee: the gateway does not re-evaluate the tiers. It trusts the authorization decision.

Code:

```python
class ExecutionGateway:
    def execute(self, action, authorization):
        if not authorization.authorized:
            return ExecutionResult(
                executed=False,
                reason=f"Not authorized: {authorization.decision.value}",
            )
        try:
            output = self._executor(action)
            return ExecutionResult(executed=True, output=output, reason="ok")
        except Exception as e:
            return ExecutionResult(executed=False, reason=f"Execution error: {e}")
```

---

5. Action Binding

Every authorized action is cryptographically bound to its authorization.

Binding fields:

Field Description
action_fingerprint SHA-256 of the action (verb, target, parameters)
authorization_hash SHA-256 of (decision, trace_id)
binding_hash SHA-256 of (action_fingerprint, authorization_hash)

Code:

```python
class ActionBinding:
    @classmethod
    def create(cls, action, authorization):
        action_fp = action.fingerprint()
        auth_hash = sha256(f"{authorization.decision.value}:{authorization.trace_id}")
        binding_hash = sha256(f"{action_fp}:{auth_hash}")
        return cls(action_fp, auth_hash, binding_hash)

    def verify(self, action, authorization):
        return ActionBinding.create(action, authorization).binding_hash == self.binding_hash
```

---

6. Replay Protection

Nonces are tracked to reject replays.

```python
class ReplayProtection:
    def check_and_record(self, nonce: str) -> bool:
        if nonce in self._seen:
            return False
        self._seen.add(nonce)
        return True
```

---

7. Invariants

OSCA enforces the following invariants:

1. Independence — each tier is evaluated without trusting the others.
2. Non-override — no tier can silently override another.
3. Atomicity — all three tiers must pass, or the action is denied/escalated.
4. Traceability — every authorized action carries a traceable decision.
5. Binding — every executed action is cryptographically bound to its authorization.
6. Replay resistance — nonces prevent replay attacks.

---

8. Example

```python
from core.action import Action
from authority.origin import Origin
from authority.semantic import Semantic
from authority.consequence import Consequence, Reversibility
from core.decision_engine import DecisionEngine
from core.execution_gateway import ExecutionGateway
from security.action_binding import ActionBinding

action = Action(verb="read", target="/data/file.txt")

origin = Origin(identity="agent:123", credential="token_abc")
semantic = Semantic(intent="read_file", scope=["/data/file.txt"])
consequence = Consequence(effects=["file:read"], reversibility=Reversibility.REVERSIBLE)

engine = DecisionEngine()
auth = engine.decide(
    action,
    origin.verify(action),
    semantic.verify(action),
    consequence.verify(action),
    trace_id="t-full",
)

assert auth.authorized

gateway = ExecutionGateway(lambda a: f"read:{a.target}")
result = gateway.execute(action, auth)
assert result.executed
assert result.output == "read:/data/file.txt"

binding = ActionBinding.create(action, auth)
assert binding.verify(action, auth)
```

