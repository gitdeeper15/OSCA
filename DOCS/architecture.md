# OSCA — Architecture

**OSCA — Origin, Semantic, and Consequence Authority**

---

## 1. Overview

OSCA is organized into six layers:

1. **Core** — action, authorization, decision engine, execution gateway.
2. **Authority** — the three tiers: origin, semantic, consequence.
3. **Governance** — policy, delegation, escalation, audit.
4. **Security** — action binding, provenance, replay protection.
5. **Simulation** — scenarios, agents, attacks, results.
6. **Tests** — unit and adversarial tests.

Each layer depends only on the layers below it. The authority layer depends on core; governance depends on authority; security depends on core; simulation depends on everything.

---

## 2. Module Tree

```

OSCA/
├── core/
│   ├── action.py              # Action (verb, target, params)
│   ├── authorization.py       # Authorization, Decision, TierVerdict
│   ├── decision_engine.py     # DecisionEngine
│   └── execution_gateway.py   # ExecutionGateway, ExecutionResult
│
├── authority/
│   ├── origin.py              # Origin tier
│   ├── semantic.py            # Semantic tier
│   └── consequence.py         # Consequence tier
│
├── governance/
│   ├── policy.py              # Policy
│   ├── delegation.py          # Delegation
│   ├── escalation.py          # Escalation
│   └── audit.py               # AuditLog, AuditRecord
│
├── security/
│   ├── action_binding.py      # ActionBinding
│   ├── provenance.py          # Provenance
│   └── replay_protection.py   # ReplayProtection
│
├── simulation/
│   ├── __init__.py
│   ├── runner.py              # Scenario runner + summary
│   ├── __main__.py            # CLI entry point
│   ├── scenarios/
│   │   ├── __init__.py
│   │   ├── happy_path.py      # Authorized action executes
│   │   ├── scope_escalation.py # Out-of-scope action denied
│   │   └── tier_collusion.py  # Two-tier collusion blocked
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── honest_agent.py    # Proposes in-scope actions
│   │   └── malicious_agent.py # Proposes out-of-scope actions
│   ├── attacks/
│   │   ├── __init__.py
│   │   ├── replay_attack.py   # Nonce replay rejected
│   │   └── tamper_attack.py   # Binding detects tampering
│   └── results/               # Simulation outputs
│
├── tests/
│   ├── test_origin.py
│   ├── test_semantic.py
│   ├── test_consequence.py
│   ├── test_authorization.py
│   ├── test_escalation.py
│   ├── test_execution_binding.py
│   └── test_adversarial.py
│
├── DOCS/
│   ├── authorization_model.md
│   ├── architecture.md
│   └── threat_model.md
│
├── RESEARCH_PAPER/
│   └── OSCA_Research_Paper.pdf
│
├── CHANGELOG.md
├── README.md
└── VERSION

```

---

## 3. Data Flow

A single authorized execution traverses the architecture as follows:

```

```

---

## 4. Dependencies

### 4.1 Core → no internal dependencies (except `dataclasses`, `enum`, `hashlib`).

### 4.2 Authority → depends on `core.action` and `core.authorization`.

### 4.3 Governance → depends on `core.action`, `core.authorization`.

### 4.4 Security → depends on `core.action`, `core.authorization`.

### 4.5 Simulation → depends on all of the above.

### 4.6 Tests → depend on all of the above.

**No circular dependencies.** The dependency graph is a DAG.

---

## 5. Invariants Enforced by the Architecture

### 5.1 Independence

Each tier (`Origin`, `Semantic`, `Consequence`) receives only the `Action` and produces only a `TierVerdict`. No tier receives the verdict of another tier. This ensures the three evaluations are independent.

### 5.2 Non-Override

The `DecisionEngine` aggregates verdicts without allowing any single tier to override the others. If any tier fails, the decision is not `AUTHORIZED`.

### 5.3 Atomicity

The `ExecutionGateway` executes the action only if the decision is `AUTHORIZED`. There is no partial execution.

### 5.4 Traceability

Every `Authorization` carries a `trace_id`. Every `TierVerdict` carries `evidence`. Every `ExecutionResult` carries `reason`. The chain from agent → tier → decision → execution is reconstructible.

### 5.5 Binding

The `ActionBinding` cryptographically binds the executed action to its authorization. A tampered action or authorization fails verification.

### 5.6 Replay Resistance

The `ReplayProtection` tracks nonces and rejects duplicates. Combined with `ActionBinding`, this prevents replay attacks.

---

## 6. Extension Points

The architecture is designed to be extended without modifying the core:

- **New tiers:** add a new `TierVerdict` producer and extend the `DecisionEngine` (but preserve the non-override invariant).
- **New governance rules:** add new `Policy` objects and consult them before `DecisionEngine`.
- **New security bindings:** add new hash schemes in `security/` without modifying `ActionBinding`.
- **New simulation scenarios:** add new files in `simulation/scenarios/` without modifying the core.

---

## 7. Testing Strategy

OSCA's test suite is organized by module:

- `test_origin.py` — origin tier: valid, missing identity, missing credential, evidence, timestamp, nonce, attestation.
- `test_semantic.py` — semantic tier: valid, missing intent, missing scope, out-of-scope, wildcard.
- `test_consequence.py` — consequence tier: valid, missing effects, reversibility, side effects, audit.
- `test_authorization.py` — decision engine: all pass, one fail, escalated, multiple fails.
- `test_escalation.py` — escalation record: immutability, equality, repr.
- `test_execution_binding.py` — execution gateway + binding: authorized, denied, exception, tampered.
- `test_adversarial.py` — hostile conditions: compromised origin, semantic drift, consequence escalation, non-override, atomicity, replay, tampered binding, full pipeline.

**Total: 51 tests. Status: 51/51 passing.**

---

## 8. Non-Goals

OSCA does not:

- Replace cryptographic identity systems (it consumes them).
- Guarantee semantic correctness of the agent's intent (it verifies declared intent against declared scope).
- Provide isolation between agents (it authorizes individual actions).
- Offer formal verification (it uses structural invariants and adversarial tests).
- Extend beyond the six listed research domains at this stage.
