<div align="center">

# OSCA

### Origin, Semantic, and Consequence Authority

*A Multi-Tier Authorization Architecture for Autonomous AI Agents*

*Authority Separation · Structural Invariants · Execution Binding · Decision Traceability*

---

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23851837-1B4F72?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.23851837)
[![Figshare](https://img.shields.io/badge/Figshare-Archived-1B4F72?logo=figshare&logoColor=white)](https://doi.org/10.6084/m9.figshare.34884411)
[![PyPI](https://img.shields.io/badge/PyPI-osca--engine-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/osca-engine)
[![GitHub](https://img.shields.io/badge/GitHub-OSCA-181717?logo=github&logoColor=white)](https://github.com/gitdeeper15/OSCA)
[![Site](https://img.shields.io/badge/site-osca--ai.netlify.app-00c7b7)](https://osca-ai.netlify.app)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![Python](https://img.shields.io/badge/python-3.x-3776ab?logo=python&logoColor=white)](https://python.org)
[![Tests](https://img.shields.io/badge/tests-51%2F51%20passing-27ae60)]()
[![Status](https://img.shields.io/badge/status-Phase%20I%20implemented-blue)]()
[![License: MIT](https://img.shields.io/badge/license-MIT-27ae60)](LICENSE)

---

**`3 Authority Layers`** · **`4 Decision States`** · **`9 Architectural Invariants`** · **`8 Threat Categories`** · **`10 Evaluation Scenarios`** · **`51 Tests`** · **`5 Simulation Scenarios`**

---

[Research Paper](RESEARCH_PAPER/) · [Architecture](#-architectural-model) · [Quick Start](#-quick-start) · [Formal Model](#-formal-authorization-model) · [Threat Model](#-threat-model) · [Evaluation](#-experimental-methodology) · [Citation](#-citation)

</div>

---

## 📌 Overview

**OSCA** (Origin, Semantic, and Consequence Authority) is a multi-tier authorization architecture for autonomous, tool-using AI agents, together with a Phase I reference implementation.

The starting observation is that *the ability to generate an action does not imply the authority to execute it.* An agent can interpret instructions, call tools, modify resources, and trigger operations whose consequences reach beyond its immediate environment. Conventional permission models usually collapse three different questions into one decision. OSCA separates them:

| Authority | Authorization Object | Primary Question |
|-----------|----------------------|------------------|
| **Origin** | Request source | Who has authority to initiate this action? |
| **Semantic** | Proposed action | What is authorized to be performed? |
| **Consequence** | Expected effects | Which consequences are authorized? |

> *"The authority to initiate an action, the authority to define its permissible meaning, and the authority to approve its consequences are distinct responsibilities and must remain independently verifiable."*

### Core Principle

```
Execution(A) ⇔ Origin(A) ∧ Semantic(A) ∧ Consequence(A)

Subject to:  ActionExecuted = ActionAuthorized
```

OSCA is **not** an empirically validated security mechanism. The architecture is specified and a Phase I implementation passes its own test suite and simulation scenarios, but empirical and adversarial evaluation have not yet been performed. OSCA is designed to complement, not replace, existing identity, access-control, and fine-grained authorization technologies.

---

## 🗂️ Table of Contents

- [Overview](#-overview)
- [What's In This Release](#-whats-in-this-release)
- [Key Features](#-key-features)
- [Architectural Model](#-architectural-model)
- [Action Representation](#-action-representation)
- [Formal Authorization Model](#-formal-authorization-model)
- [Architectural Invariants](#-architectural-invariants)
- [Execution Pipeline](#-execution-pipeline)
- [Atomic Authorization Binding](#-atomic-authorization-binding)
- [Threat Model](#-threat-model)
- [Implementation Status](#-implementation-status)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Experimental Methodology](#-experimental-methodology)
- [Research Status](#-research-status)
- [Limitations](#-limitations)
- [Future Research](#-future-research)
- [Research Paper](#-research-paper)
- [Platforms & Mirrors](#-platforms--mirrors)
- [Citation](#-citation)
- [License](#-license)
- [Author](#-author)

---

## ✨ What's In This Release

> **Status:** Research manuscript + Phase I reference implementation
> **Version:** `0.1.0-research-draft`
> **Scope:** Architectural research, formal system design, and executable prototype

This release provides:

- A **three-tier authority model** separating source legitimacy, semantic scope, and consequence approval.
- A **formal authorization model** with four decision states and explicit precedence rules.
- A set of **architectural invariants** (O1–O2, S1–S2, C1–C2, G1–G3).
- A **threat model** of eight threat categories (T1–T8).
- A **Phase I implementation** of the three authority tiers, decision engine, execution gateway, governance layer, and security primitives.
- A **test suite** (51 tests) and **simulation suite** (5 scenarios, including attack scenarios).
- A **comparative experimental protocol** with three configurations, ten scenarios, and seven metrics.

**What is *not* yet demonstrated:**

- No empirical evaluation against the proposed baselines (Configurations A and B)
- No adversarial evaluation against established agent-security benchmarks
- No claim of resistance to real-world attacks
- No formal verification or model-checking of the stated properties

---

## 🔑 Key Features

| Feature | Description |
|---------|-------------|
| **Authority Separation** | Origin, Semantic, and Consequence are evaluated as independent responsibilities |
| **No Implicit Inheritance** | Approval at one layer never substitutes for approval at another |
| **Structured Actions** | Requests are converted to an explicit object before authorization, never evaluated as free text |
| **Four Decision States** | PASS · DENY · ESCALATE · INDETERMINATE |
| **Fail-Closed Handling** | Uncertainty is never silently interpreted as permission |
| **Human Escalation** | Formal path to human or institutional approval, itself authenticated and bound to the action |
| **Execution Binding** | Authorization tied to a cryptographic digest of the exact evaluated action |
| **Replay Protection** | Nonce tracking and replay rejection |
| **TOCTOU Protection** | Short-lived decisions and revalidation of environmental state before execution |
| **Decision Traceability** | Every decision linked to its action, evidence, policy version, and timestamp |

---

## 🏛️ Architectural Model

Each layer evaluates a different dimension of an action request.

```
┌──────────────────────────────────────────────────────────────────┐
│  Action Request                                                  │
│        ↓                                                         │
│  1. ORIGIN AUTHORITY       Who initiated it? Is the chain valid? │
│        ↓                                                         │
│  2. SEMANTIC AUTHORITY     What does it mean? Is it in scope?    │
│        ↓                                                         │
│  3. CONSEQUENCE AUTHORITY  What effects? Is approval required?   │
│        ↓                                                         │
│  Authorization Decision  ──→  Escalation (if required)           │
│        ↓                                                         │
│  Authorized Action Execution                                     │
│                                                                  │
│  Audit & Traceability: decisions · evidence · path · timestamps  │
└──────────────────────────────────────────────────────────────────┘
```

A rejection at any tier blocks the action. Escalation routes the decision to additional human or institutional authorization.

### 1. Origin Authority

Determines whether the **source** of a request has legitimate authority to initiate it.

- Authenticates the requesting entity and verifies the initiating agent
- Validates the delegation chain
- Checks whether the source may request this action category
- Checks whether authority has been revoked or has expired

**Outcomes:** `PASS` · `DENY` · `ESCALATE`

A `PASS` establishes only that the request came from a legitimate source. It does **not** authorize execution.

### 2. Semantic Authority

Evaluates the **meaning and scope** of the proposed action.

- Interprets the action type and intended operation
- Verifies the target resource and validates parameters
- Compares the action against the authorized task scope
- Identifies semantic inconsistencies and unauthorized expansions

**Outcomes:** `PASS` · `DENY` · `ESCALATE`

An authenticated agent may legitimately request access to a resource while proposing an operation that exceeds the permissions of its task. Origin passes, Semantic denies.

### 3. Consequence Authority

Evaluates the **potential effects** of an otherwise legitimate and semantically permitted action.

- Identifies direct and relevant indirect consequences
- Evaluates impact scope
- Identifies irreversible or difficult-to-reverse effects
- Determines whether additional approval is required and sets execution constraints

**Outcomes:** `APPROVE` · `DENY` · `ESCALATE` · `INDETERMINATE`

An agent may correctly interpret a request to modify a database yet propose a modification whose consequences exceed the permitted operational scope. Origin and Semantic pass, Consequence denies.

> **Design Note.** Consequence Authority must be implemented as a genuinely independent authority in both design and execution, not as an additional risk assessment embedded within Semantic Authority. This is the most important architectural distinction that the paper and any implementation must preserve.

### Authority Separation ≠ Permission Duplication

The three layers do not perform identical checks. Origin does not redefine semantic scope, Semantic does not authenticate the requester, and Consequence does not silently replace the decisions of the other layers. Formally: `OA(A) ≠ SA(A) ≠ CA(A)`, distinct authorization functions, not necessarily different numerical values.

---

## 🧾 Action Representation

Every proposed action is converted into a structured object before authorization:

```
A = (id, s, d, a, p, t, c, e)
```

| Field | Meaning |
|-------|---------|
| `id` | Unique action identifier |
| `s` | Requesting subject or agent |
| `d` | Delegation and provenance information |
| `a` | Action type |
| `p` | Action parameters |
| `t` | Target resource or environment |
| `c` | Execution context |
| `e` | Declared expected effects |

An action request must never be interpreted as an unrestricted textual instruction.

---

## 📐 Formal Authorization Model

### Decision Domain

```
D_i(A) ∈ { PASS, DENY, ESCALATE, INDETERMINATE },   i ∈ { O, S, C }
```

### Conditions (default strict policy)

```
Authorize(A)      =  PASS_O(A) ∧ PASS_S(A) ∧ PASS_C(A)
Execute(A)        ⇔  Authorize(A)

Deny(A)           =  DENY_O(A) ∨ DENY_S(A) ∨ DENY_C(A)
Escalate(A)       =  ¬Deny(A) ∧ (ESC_O(A) ∨ ESC_S(A) ∨ ESC_C(A))
Indeterminate(A)  ⇒  ¬Execute(A)
```

A denial can never be overridden by a PASS from another layer. Escalation suspends execution until the required authorization is obtained. An implementation may convert INDETERMINATE into escalation, but must not treat uncertainty as permission.

### Decision Precedence

```
1. DENY  >  2. ESCALATE  >  3. INDETERMINATE  >  4. PASS
```

### Core Decision Table

| Origin | Semantic | Consequence | Final Decision |
|--------|----------|-------------|----------------|
| PASS | PASS | PASS | **AUTHORIZE** |
| DENY | Any | Any | **DENY** |
| PASS | DENY | Any | **DENY** |
| PASS | PASS | DENY | **DENY** |
| ESCALATE | Any | Any | **ESCALATE** |
| PASS | ESCALATE | Any | **ESCALATE** |
| PASS | PASS | ESCALATE | **ESCALATE** |
| INDETERMINATE | Any | Any | **SUSPEND** |
| PASS | INDETERMINATE | Any | **SUSPEND** |
| PASS | PASS | INDETERMINATE | **SUSPEND** |

---

## 🛡️ Architectural Invariants

| ID | Invariant | Statement |
|----|-----------|-----------|
| **O1** | Origin Verification | `Execute(A) ⇒ OA(A) = PASS` |
| **O2** | Delegation Integrity | `Authority(Agent) ⊆ Authority(Delegator)` |
| **S1** | Semantic Scope Preservation | `Scope(A) ⊆ AuthorizedScope` |
| **S2** | Action Representation Integrity | The action evaluated by Semantic Authority must match the action received from Origin Authority; material changes require re-evaluation |
| **C1** | Consequence Authorization | `Execute(A) ⇒ Impact(A) ⊆ AuthorizedImpact` |
| **C2** | Consequence Escalation | Actions needing human or institutional approval remain suspended until it is obtained |
| **G1** | Non-Inheritance of Authority | Approval by one layer never implies approval by another |
| **G2** | Decision Traceability | Every decision is tied to an identifiable request and its evaluation evidence |
| **G3** | Execution Binding | The executed action must be the authorized action; material modification invalidates approval |

---

## 🔁 Execution Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│  1. Submit       →  Agent submits an action request         │
│  2. Structure    →  Action Gateway builds structured action │
│  3. Origin       →  Origin Authority evaluates the source   │
│  4. Semantic     →  Semantic Authority evaluates the action │
│  5. Consequence  →  Consequence Authority evaluates effects │
│  6. Decide       →  Decision Engine combines the results    │
│  7. Escalate     →  Escalation Manager (if required)        │
│  8. Execute      →  Execution Gateway runs the exact action │
│  9. Audit        →  Audit Engine records the decision path  │
└─────────────────────────────────────────────────────────────┘
```

### Components

| Component | Responsibility |
|-----------|----------------|
| **Action Gateway** | Receives agent actions and converts them to structured requests |
| **Origin Authority Engine** | Validates identity, provenance, and delegation |
| **Semantic Authority Engine** | Evaluates meaning, parameters, target, and permitted scope |
| **Consequence Authority Engine** | Evaluates impact and whether additional approval is necessary |
| **Authorization Decision Engine** | Combines independent decisions under the authorization policy |
| **Escalation Manager** | Routes actions to an appropriate human or institutional authority |
| **Execution Gateway** | Executes only the exact action tied to a valid authorization decision |
| **Audit and Traceability Engine** | Records request, decisions, policy versions, evidence, and execution status |

### Default Strict Policy (pseudocode)

```python
def authorize(action):
    origin = origin_authority.evaluate(action)
    if origin.status == "DENY":
        return deny(action, origin)
    if origin.status != "PASS":
        return suspend_or_escalate(action, origin)

    semantic = semantic_authority.evaluate(action)
    if semantic.status == "DENY":
        return deny(action, semantic)
    if semantic.status != "PASS":
        return suspend_or_escalate(action, semantic)

    consequence = consequence_authority.evaluate(action)
    if consequence.status == "DENY":
        return deny(action, consequence)
    if consequence.status != "PASS":
        return suspend_or_escalate(action, consequence)

    return authorize_execution(action)
```

The execution gateway must independently verify the authorization record and action binding before executing.

---

## 🔐 Atomic Authorization Binding

Authorization is bound to the exact action that was evaluated, using a digest over a canonical representation:

```
h_A = H(Canonicalize(A))
```

The authorization record stores the digest together with the action identifier, authority decisions, policy version, context version, timestamp, approval identity, and expiration or validity conditions. Before execution, the gateway verifies that the digest still matches.

### Time-of-Check to Time-of-Use (TOCTOU)

The environment may change between authorization and execution (for example, a resource's owner or state). OSCA proposes:

- Binding authorization to the evaluated action
- Recording relevant environmental state
- Using short-lived authorization decisions where appropriate
- Revalidating critical environmental attributes immediately before execution
- Requiring reauthorization when relevant conditions change

---

## ⚠️ Threat Model

| ID | Threat | Relevant Controls |
|----|--------|-------------------|
| **T1** | Unauthorized request origin | Origin Authority |
| **T2** | Delegation abuse | Origin Authority, delegation integrity |
| **T3** | Semantic scope expansion | Semantic Authority |
| **T4** | Indirect prompt injection | Origin provenance, semantic scope evaluation, consequence authorization |
| **T5** | Consequence escalation | Consequence Authority |
| **T6** | Authorization replay | Action identifiers, expiration, context binding, execution validation |
| **T7** | Post-authorization modification | Execution binding, digest verification |
| **T8** | Audit manipulation | Protected audit storage, integrity verification, restricted permissions |

### Security Assumptions

1. Identity credentials and cryptographic verification are appropriately managed.
2. Authority policies are maintained by trusted administrative processes.
3. The execution gateway cannot be bypassed by the agent.
4. Authority evaluation components have sufficiently isolated responsibilities.
5. Audit records are protected against unauthorized modification.
6. Human escalation channels follow explicit approval procedures.

### Out of Scope

OSCA does not claim to eliminate: all model hallucinations, all prompt-injection attacks, compromise of the operating system or execution gateway, malicious behavior by fully compromised trusted authorities, incorrect organizational policies, or undetectable and unforeseeable consequences.

> **OSCA is an authorization architecture, not a complete security solution.**

---

## 📊 Implementation Status

| Layer | Modules | Status | Tests |
|-------|---------|--------|-------|
| Origin tier | `authority/origin.py` | ✅ Phase I | 8 |
| Semantic tier | `authority/semantic.py` | ✅ Phase I | 8 |
| Consequence tier | `authority/consequence.py` | ✅ Phase I | 7 |
| Authorization / decision engine | `core/authorization.py`, `core/decision_engine.py` | ✅ Phase I | 8 |
| Escalation | `governance/escalation.py` | ✅ Phase I | 5 |
| Execution binding | `core/execution_gateway.py`, `security/action_binding.py` | ✅ Phase I | 7 |
| Adversarial | replay and tamper scenarios | ✅ Phase I | 8 |
| **Total** | | **51/51 passing** | **51** |

**Simulation:** 5/5 scenarios, namely `happy_path`, `scope_escalation`, `tier_collusion`, `replay_attack`, `tamper_attack`.

> Passing tests establish that the implementation matches its specification. They do not establish resistance to real-world adversarial attacks.

**Current VERSION:** `0.1.0-research-draft`

---

## 📁 Project Structure

```
OSCA/
│
├── core/                           # Core authorization logic
│   ├── action.py                   # Action structure
│   ├── authorization.py            # Decision, TierVerdict, Authorization
│   ├── decision_engine.py          # Combining tier verdicts
│   └── execution_gateway.py        # Atomic execution + binding
│
├── authority/                      # Three independent tiers
│   ├── origin.py                   # Origin tier (identity, credential)
│   ├── semantic.py                 # Semantic tier (intent, scope)
│   └── consequence.py              # Consequence tier (effects, reversibility)
│
├── governance/                     # Governance layer
│   ├── policy.py                   # Policy definitions
│   ├── delegation.py               # Authority delegation
│   ├── escalation.py               # Escalation records
│   └── audit.py                    # Audit trail
│
├── security/                       # Security primitives
│   ├── action_binding.py           # Cryptographic action-to-auth binding
│   ├── provenance.py               # Action provenance tracking
│   └── replay_protection.py        # Nonce tracking, replay rejection
│
├── simulation/                     # End-to-end scenarios
│   ├── __main__.py                 # CLI entry point (python3 -m simulation)
│   ├── runner.py                   # Scenario runner
│   ├── scenarios/                  # happy_path, scope_escalation, tier_collusion
│   ├── agents/                     # honest_agent, malicious_agent
│   ├── attacks/                    # replay_attack, tamper_attack
│   └── results/
│
├── tests/                          # Test suite (51/51 passing)
│   ├── test_origin.py              # 8 tests
│   ├── test_semantic.py            # 8 tests
│   ├── test_consequence.py         # 7 tests
│   ├── test_authorization.py       # 8 tests
│   ├── test_escalation.py          # 5 tests
│   ├── test_execution_binding.py   # 7 tests
│   └── test_adversarial.py         # 8 tests
│
├── DOCS/                           # authorization_model.md, architecture.md, threat_model.md
├── RESEARCH_PAPER/                 # OSCA_Research_Paper.pdf (32 pages)
├── PUBLICATION/Netlify/            # Static site (index, dashboard, results, documentation)
│
├── README.md · CHANGELOG.md · VERSION · LICENSE · AUTHORS.md
├── CONTRIBUTING.md · CITATION.cff · MANIFEST.in · Makefile
├── pyproject.toml · setup.py · setup.cfg · requirements.txt
└── upload_osca.py                  # PyPI uploader
```

### Design Principles

1. Independent authority interfaces
2. Explicit input and output schemas
3. Deterministic policy evaluation wherever possible
4. Fail-closed handling of uncertainty
5. Immutable authorization records
6. No implicit permission inheritance
7. Execution through a controlled gateway

### Authority Interface (conceptual)

```python
class AuthorityDecision:
    status: str
    reason: str
    evidence: dict

class OriginAuthority:
    def evaluate(self, action): ...

class SemanticAuthority:
    def evaluate(self, action): ...

class ConsequenceAuthority:
    def evaluate(self, action): ...
```

The decision engine must not replace the internal evaluation logic of any authority layer. It only combines the resulting decisions according to the policy.

---

## 🚀 Quick Start

```bash
# Install the package from PyPI
pip install osca-engine

# Or work from source
git clone https://github.com/gitdeeper15/OSCA.git
cd OSCA
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run the test suite
python -m pytest -v

# Run the simulation scenarios
python3 -m simulation
```

---

## 🔬 Experimental Methodology

The proposed evaluation tests whether authority separation improves authorization accuracy, traceability, and resistance to unauthorized actions without unacceptable overhead. Architectural correctness and empirical security performance are kept distinct: a passing software test does not establish resistance to real-world attacks.

### Configurations

| Config | Model |
|--------|-------|
| **A** | Conventional authorization (unified permission evaluation) |
| **B** | Two-dimensional authorization (source verification + action-scope verification) |
| **C** | OSCA (Origin + Semantic + Consequence) |

### Scenarios

| ID | Description | Expected OSCA Behavior |
|----|-------------|------------------------|
| E1 | Legitimate origin and action | Authorized |
| E2 | Unauthorized source | Origin denial |
| E3 | Valid source, invalid action scope | Semantic denial |
| E4 | Valid source and scope, excessive impact | Consequence denial |
| E5 | Valid request requiring human approval | Escalation |
| E6 | Indirect prompt injection | Unauthorized action blocked |
| E7 | Modified action after approval | Reauthorization required |
| E8 | Replayed authorization request | Replay rejected |
| E9 | Conflicting authority decisions | No unauthorized execution |
| E10 | Missing authorization evidence | Fail-closed or escalation |

### Adversarial Evaluation

Identity impersonation · delegation-chain manipulation · semantic scope expansion · hidden instructions in retrieved content · parameter substitution · target substitution · consequence underestimation · authorization replay · post-authorization modification · attempts to bypass the execution gateway. Where possible, established agent-security environments such as [AgentDojo](https://doi.org/10.52202/079017-2636) are to be used.

### Metrics

| Metric | Definition |
|--------|------------|
| **UAPR** | Unauthorized Action Prevention Rate = Blocked / Total Unauthorized × 100 |
| **LAAR** | Legitimate Action Acceptance Rate = Authorized Legitimate / Total Legitimate × 100 |
| **FRR** | False Rejection Rate = Legitimate Denied / Total Legitimate × 100 |
| **ER** | Escalation Rate = Escalated / Total Requests × 100 |
| **L_A** | Authorization Latency = t_decision − t_request |
| **DTR** | Decision Traceability Rate = Complete Records / Total Decisions × 100 |
| **EBI** | Execution-Binding Integrity = Executions Matching Authorized Action / Total Executions × 100 |

### Hypotheses

| ID | Hypothesis |
|----|------------|
| **H1** | Separating Origin from Semantic Authority improves identification of actions from legitimate sources that exceed their authorized scope |
| **H2** | Adding Consequence Authority improves detection of actions whose effects exceed the permitted impact boundary |
| **H3** | Independent authority decisions improve traceability of authorization outcomes |
| **H4** | OSCA adds authorization latency compared with a unified baseline |
| **H5** | OSCA can reduce unauthorized execution while maintaining an acceptable legitimate-action acceptance rate |

> No hypothesis is considered confirmed until supported by experimental evidence.

### Experimental Controls

Identical agent configurations across models · same action corpus and scenarios · documented policy differences · separated benign and adversarial cases · every decision recorded · repeated stochastic trials · security **and** utility reported · failed and incomplete executions preserved · per-layer operational cost reported.

---

## 📈 Research Status

| Dimension | Status |
|-----------|--------|
| Architectural model | ✅ Defined (paper §3) |
| Formal authorization model | ✅ Defined (paper §4) |
| Architectural invariants | ✅ Defined (paper §5) |
| Threat model | ✅ Defined (paper §7) |
| Experimental protocol | ✅ Specified (paper §9) |
| Executable prototype | ✅ Phase I (`core/`, `authority/`, `governance/`, `security/`) |
| Unit and integration tests | ✅ 51/51 passing |
| Simulation scenarios | ✅ 5/5 |
| Preregistration (OSF) | ✅ Registered (10.17605/OSF.IO/5EQC9) |
| Empirical evaluation | ❌ Not yet performed |
| Adversarial evaluation | ❌ Not yet performed |
| Formal verification | ❌ Future work |

**Next stage:** empirical validation of the Phase I implementation and adversarial evaluation against established agent-security benchmarks.

---

## 🧱 Limitations

1. The Phase I implementation has not yet been validated through complete empirical evaluation and adversarial benchmarking.
2. Semantic interpretation is uncertain, especially for actions generated from natural language. The architecture requires structured action representations and policy-grounded evaluation rather than relying on model-generated explanations.
3. Consequence evaluation cannot guarantee identification of every downstream effect; complex systems may produce indirect or emergent consequences.
4. Effectiveness depends on the integrity of identity, policy, execution, and audit infrastructure.
5. The three layers may need domain-specific definitions; a financial transaction, a database modification, and a physical robotic action do not share the same consequence boundaries.
6. Additional operational overhead must be measured under realistic conditions, along with possible false rejections or unnecessary escalations from poorly calibrated policies.

---

## 🔭 Future Research

| Direction | Focus |
|-----------|-------|
| Formal verification | Model-checking of authority separation, decision precedence, delegation integrity, execution binding |
| Empirical evaluation | Benchmarks against AgentDojo, InjecAgent, and other agent-security suites |
| Domain-specific authorization | Finance, enterprise software, autonomous research agents, safety-critical systems |
| Dynamic consequence evaluation | Updating assessments when conditions change during execution |
| Distributed authority | Multiple agents, institutions, authorization services, independently governed environments |
| Authority and execution | One-time decision versus continuously maintained condition over an action's lifecycle |

---

## 📄 Research Paper

**Title:** OSCA: A Multi-Tier Authorization Architecture for Autonomous AI Agents — Origin, Semantic, and Consequence Authority

**Status:** Initial Research Manuscript — Proposed Architecture
**Record ID:** OSCA-ARCH-01
**Version:** 0.1.0-research-draft
**DOI:** [10.5281/zenodo.23851837](https://doi.org/10.5281/zenodo.23851837)

See [`RESEARCH_PAPER/`](RESEARCH_PAPER/) for the full manuscript (32 pages).

**Keywords:** OSCA · Autonomous AI Agents · Multi-Tier Authorization · Origin Authority · Semantic Authority · Consequence Authority · Authority Separation · AI Governance · Action Authorization · Agentic AI Safety · Runtime Authorization · Consequence-Aware Execution

### Key References

1. Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*, ICLR 2023.
2. Hu et al., *Guide to Attribute Based Access Control (ABAC)*, NIST SP 800-162, 2019.
3. Lodderstedt, Richer, Campbell, *OAuth 2.0 Rich Authorization Requests*, RFC 9396, 2023.
4. Saltzer and Schroeder, *The Protection of Information in Computer Systems*, Proc. IEEE, 1975.
5. Debenedetti et al., *AgentDojo*, NeurIPS 2024.
6. OWASP, *Top 10 for Large Language Model Applications 2025*.
7. Tabassi, *AI Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, 2023.

---

## 🌐 Platforms & Mirrors

| Platform | URL | Role |
|----------|-----|------|
| GitHub (Primary) | [github.com/gitdeeper15/OSCA](https://github.com/gitdeeper15/OSCA) | Source code, issues, PRs |
| GitLab | [gitlab.com/gitdeeper15/OSCA](https://gitlab.com/gitdeeper15/OSCA) | Mirror |
| Codeberg | [codeberg.org/gitdeeper15/OSCA](https://codeberg.org/gitdeeper15/OSCA) | Mirror |
| Bitbucket | [bitbucket.org/gitdeeper15/OSCA](https://bitbucket.org/gitdeeper15/OSCA) | Mirror |
| PyPI | [pypi.org/project/osca-engine](https://pypi.org/project/osca-engine) | Python package |
| Zenodo | [doi.org/10.5281/zenodo.23851837](https://doi.org/10.5281/zenodo.23851837) | Citable DOI, manuscript archive |
| Figshare | [doi.org/10.6084/m9.figshare.34884411](https://doi.org/10.6084/m9.figshare.34884411) | Secondary citable archive |
| Website | [osca-ai.netlify.app](https://osca-ai.netlify.app) | Live documentation |
| ORCID | [orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) | Researcher identity |

*OSF preregistration: [10.17605/OSF.IO/5EQC9](https://doi.org/10.17605/OSF.IO/5EQC9).*

---

## 📖 Citation

If this work contributes to your research, please cite it as follows.

### Zenodo Archive (Primary)

```bibtex
@article{baladi2026osca,
  author       = {Baladi, Samir},
  title        = {{OSCA}: A Multi-Tier Authorization Architecture for
                  Autonomous {AI} Agents --- Origin, Semantic, and
                  Consequence Authority},
  year         = {2026},
  month        = nov,
  version      = {0.1.0-research-draft},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23851837},
  url          = {https://doi.org/10.5281/zenodo.23851837},
  note         = {Ronin Institute / Rite of Renaissance}
}
```

### Figshare Archive

```bibtex
@misc{baladi2026osca_figshare,
  author       = {Baladi, Samir},
  title        = {{OSCA}: Origin, Semantic, and Consequence Authority},
  year         = {2026},
  publisher    = {figshare},
  doi          = {10.6084/m9.figshare.34884411},
  url          = {https://doi.org/10.6084/m9.figshare.34884411},
  note         = {Ronin Institute / Rite of Renaissance}
}
```

### OSF Preregistration

```bibtex
@misc{baladi2026osca_osf,
  author       = {Baladi, Samir},
  title        = {{OSCA}: Pre-Registered Study Protocol for Multi-Tier
                  Authorization of Autonomous AI Agents},
  year         = {2026},
  publisher    = {Open Science Framework},
  doi          = {10.17605/OSF.IO/5EQC9},
  url          = {https://doi.org/10.17605/OSF.IO/5EQC9},
  note         = {OSF Preregistration}
}
```

### PyPI Package

```bibtex
@software{baladi2026osca_pypi,
  author       = {Baladi, Samir},
  title        = {{osca-engine}: Multi-Tier Authorization Architecture for
                  Autonomous AI Agents},
  year         = {2026},
  publisher    = {Python Package Index},
  url          = {https://pypi.org/project/osca-engine},
  note         = {Python package, MIT License}
}
```

### APA (inline)

> Baladi, S. (2026). *OSCA: A multi-tier authorization architecture for autonomous AI agents — Origin, Semantic, and Consequence Authority* (Version 0.1.0-research-draft). Zenodo. https://doi.org/10.5281/zenodo.23851837

---

## 📜 License

- **Code:** MIT License (see [`LICENSE`](LICENSE))
- **Manuscript and documentation:** CC-BY-4.0

```
MIT License

Copyright (c) 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

---

## 👤 Author

**Samir Baladi**
Interdisciplinary AI Researcher
Ronin Institute / Rite of Renaissance

| Contact | Link |
|---------|------|
| Email | gitdeeper@gmail.com |
| ORCID | [https://orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) |
| GitHub | [https://github.com/gitdeeper15](https://github.com/gitdeeper15) |
| PyPI | [https://pypi.org/project/osca-engine](https://pypi.org/project/osca-engine) |
| Zenodo | [https://doi.org/10.5281/zenodo.23851837](https://doi.org/10.5281/zenodo.23851837) |
| Figshare | [https://doi.org/10.6084/m9.figshare.34884411](https://doi.org/10.6084/m9.figshare.34884411) |
| Website | [https://osca-ai.netlify.app](https://osca-ai.netlify.app) |

---

<div align="center">

**OSCA · v0.1.0-research-draft · November 2026**

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23851837-1B4F72?logo=zenodo&logoColor=white)](https://doi.org/10.5281/zenodo.23851837)
[![PyPI](https://img.shields.io/badge/PyPI-osca--engine-3775A9?logo=pypi&logoColor=white)](https://pypi.org/project/osca-engine)
[![License: MIT](https://img.shields.io/badge/license-MIT-27ae60)](LICENSE)

*Phase I Implemented · Empirical Validation Pending*

</div>
