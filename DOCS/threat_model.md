# OSCA — Threat Model

**OSCA — Origin, Semantic, and Consequence Authority**

---

## 1. Scope

This document specifies the threats OSCA is designed to detect or prevent, the assumptions it makes, and the threats it explicitly does not address.

OSCA is an authorization architecture for autonomous AI agents. It does not replace cryptographic identity systems, network security, or operating-system isolation. It assumes the caller can establish identity and the underlying platform can execute code.

---

## 2. Assets

OSCA protects:

1. **Integrity of the authorization decision** — the decision (authorized / denied / escalated) cannot be forged or silently altered.
2. **Integrity of the executed action** — the action that runs is the action that was authorized.
3. **Auditability** — every authorized action leaves a verifiable trace.
4. **Non-repudiation** — an agent cannot deny having proposed an action.
5. **Replay resistance** — an authorized action cannot be re-executed without re-authorization.

---

## 3. Adversary Model

OSCA considers three classes of adversaries:

### 3.1 Compromised Agent

The agent itself is malicious or subverted. It attempts to:
- execute actions outside its declared scope,
- produce effects not declared in its consequence tier,
- replay previously authorized actions,
- escalate its own privileges.

### 3.2 Compromised Tier

One of the three tiers (origin, semantic, consequence) is compromised. It attempts to:
- approve actions it should deny,
- forge evidence to bypass other tiers,
- collude with another tier to bypass the third.

### 3.3 External Attacker

An external party attempts to:
- forge an authorization decision,
- tamper with an action after authorization,
- intercept and replay an authorized action,
- tamper with the audit log.

---

## 4. Threat Catalogue

### T1 — Identity Spoofing

**Scenario:** An agent claims an identity it does not own (e.g., `agent:admin`).

**Asset affected:** integrity of the authorization decision.

**OSCA defense:** the origin tier checks `identity` and `credential`. If either is missing or invalid, the tier fails. The verification of credentials is delegated to the underlying identity system (e.g., OAuth, SPIFFE, X.509); OSCA does not implement cryptography itself.

**Residual risk:** if the underlying credential system is compromised, OSCA cannot detect it.

---

### T2 — Scope Escalation

**Scenario:** An agent authorized to read `/data/file.txt` attempts to read `/etc/passwd`.

**Asset affected:** integrity of the executed action.

**OSCA defense:** the semantic tier checks that `action.target` is in `scope`. If it is not, the tier fails with `target_out_of_scope`. The decision engine denies the action.

**Residual risk:** if `scope` is declared as `["*"]`, the semantic tier does not constrain the target. The system designer must decide when wildcards are acceptable.

---

### T3 — Consequence Concealment

**Scenario:** An agent declares `effects=["file:read"]` but actually performs `file:write`.

**Asset affected:** integrity of the executed action.

**OSCA defense:** the consequence tier requires `effects` to be declared. The execution gateway executes the action only if the decision is `AUTHORIZED`, which requires all three tiers to pass. The `ActionBinding` binds the executed action to the authorization; any modification of the action after authorization invalidates the binding.

**Residual risk:** OSCA verifies **declared** effects, not **actual** effects. If the executor performs effects it did not declare, OSCA cannot detect it at the authorization layer. Detecting undeclared effects requires runtime monitoring (out of scope for Phase I).

---

### T4 — Tier Collusion

**Scenario:** Two tiers collude to bypass the third. For example, origin and semantic both pass even though the consequence tier should fail.

**Asset affected:** integrity of the authorization decision.

**OSCA defense:** the decision engine requires all three tiers to pass. Even if two tiers are compromised, the third tier's failure still triggers `DENIED`. The non-override invariant guarantees that no tier can silently overrule another.

**Residual risk:** if all three tiers are compromised simultaneously, OSCA cannot prevent the decision. This is outside the threat model — OSCA assumes at most two tiers are compromised at any time.

---

### T5 — Replay

**Scenario:** An attacker captures an authorized action and re-executes it later.

**Asset affected:** replay resistance.

**OSCA defense:** the origin tier accepts an optional `nonce`. The `ReplayProtection` component tracks seen nonces and rejects duplicates. The `ActionBinding` binds the action to its authorization; a replayed action with the original authorization will be rejected if the nonce has been consumed.

**Residual risk:** if the origin does not provide a nonce, replay resistance is disabled. Nonces are recommended for all production deployments.

---

### T6 — Authorization Tampering

**Scenario:** An attacker modifies the authorization decision from `DENIED` to `AUTHORIZED` before passing it to the execution gateway.

**Asset affected:** integrity of the authorization decision.

**OSCA defense:** the `ActionBinding` cryptographically binds the decision to the action. The binding hash covers the decision value and the trace id. Any tampering of the decision invalidates the binding.

**Residual risk:** if the attacker can also recompute the binding hash, they can forge the pair. Preventing this requires a secret key (out of scope for Phase I; the binding assumes a trusted environment).

---

### T7 — Escalation Abuse

**Scenario:** An agent repeatedly requests escalation to overload the human reviewer or to force approval under time pressure.

**Asset affected:** governance integrity.

**OSCA defense:** escalation is a distinct decision (`Decision.ESCALATED`), not an automatic approval. The governance layer records escalations in the audit log. Rate limits on escalation requests are a policy decision, not a structural invariant.

**Residual risk:** OSCA does not itself limit the rate of escalations. Rate limiting is delegated to the governance policy.

---

### T8 — Audit Log Tampering

**Scenario:** An attacker modifies the audit log to erase evidence of an unauthorized action.

**Asset affected:** auditability.

**OSCA defense:** the audit log is append-only. It does not by itself provide tamper-evidence. A hash chain or a Merkle tree can be added at the deployment layer (out of scope for Phase I).

**Residual risk:** in Phase I, audit logs are append-only but not tamper-evident.

---

## 5. Out-of-Scope Threats

OSCA does not address:

- **Operating-system compromise.** If the OS is compromised, all bets are off.
- **Network-level attacks.** OSCA assumes a trusted transport or delegates to TLS.
- **Side-channel attacks.** OSCA does not attempt to detect timing or power side channels.
- **Supply-chain attacks.** OSCA does not verify the provenance of its own dependencies.
- **Semantic correctness of intent.** OSCA verifies that declared intent matches declared scope; it does not verify that the declared intent reflects the agent's actual goals.
- **Undeclared effects.** OSCA verifies declared effects, not actual runtime effects.
- **Formal semantic equivalence.** OSCA does not prove that the executed action is semantically equivalent to the authorized action; it binds them structurally.

---

## 6. Assumptions

OSCA assumes:

1. **At most two tiers are compromised at any time.** If all three tiers are compromised, OSCA cannot protect the integrity of the decision.
2. **The credential system is trusted.** OSCA consumes credentials; it does not issue them.
3. **The execution environment is trusted at the point of execution.** The gateway trusts its `executor` callable.
4. **Nonces are unique per action.** Replay protection depends on this.
5. **The action fingerprint captures all relevant fields.** If an action has hidden state (e.g., references to mutable objects), the fingerprint may not capture it.

---

## 7. Security Goals

Under the assumptions above, OSCA achieves:

| Goal | Mechanism |
|------|-----------|
| Integrity of the authorization decision | Three independent tiers + non-override invariant |
| Integrity of the executed action | Atomic execution gateway + action binding |
| Auditability | Decision trace + audit log |
| Non-repudiation | Action fingerprint + binding |
| Replay resistance | Nonce tracking + binding |

---

## 8. Testing the Threat Model

The following adversarial tests are implemented in `tests/test_adversarial.py`:

| Test | Threat addressed |
|------|------------------|
| `test_compromised_origin_missing_credential` | T1 |
| `test_semantic_drift_scope_escalation` | T2 |
| `test_consequence_escalation_missing_effects` | T3 |
| `test_non_override_all_tiers_required` | T4 |
| `test_atomicity_gateway_does_not_run_when_denied` | T3, T4 |
| `test_replay_protection_rejects_second_use` | T5 |
| `test_action_binding_detects_tampered_authorization` | T6 |
| `test_full_pipeline_happy_path` | baseline |

Threats not yet covered by tests:

- T7 (escalation abuse) — governance policy.
- T8 (audit log tampering) — deployment layer.

---

## 9. Limitations and Future Work

- **Formal verification** of the non-override invariant is future work.
- **Runtime monitoring** of declared vs. actual effects is future work.
- **Hash-chained audit logs** are a deployment-layer improvement, not part of Phase I.
- **Rate limiting** of escalations is a governance policy, not a structural invariant.

---

## 10. Summary

OSCA's threat model is **explicit, bounded, and testable**. It names what it defends against, what it assumes, and what it does not cover. This is a necessary condition for any authorization architecture claiming to govern autonomous agents.
