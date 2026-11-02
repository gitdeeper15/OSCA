# OSCA — Origin, Semantic, and Consequence Authority: Pre-registered Protocol

---

**Registration DOI:** [10.17605/OSF.IO/5EQC9](https://doi.org/10.17605/OSF.IO/5EQC9)
**Registration Type:** OSF Preregistration
**Registry:** OSF Registries
**Date Created:** Nov 2, 2026, 8:16 AM
**Date Registered:** Nov 2, 2026, 8:16 AM
**Associated Project:** [https://osf.io/wp2se](https://osf.io/wp2se)
**Internet Archive:** [https://archive.org/details/osf-registrations-5eqc9-v1](https://archive.org/details/osf-registrations-5eqc9-v1)
**License:** CC-By Attribution 4.0 International
**Contributor:** Samir Baladi

---

## Data / Analytic Code / Materials / Papers / Supplements

The following files were attached to this registration:

- `README.md`
- `OSCA_Research_Paper.pdf`
- `threat_model.md`
- `architecture.md`
- `authorization_model.md`

---

## Overview

### Research questions or hypotheses

RQ1: Under what conditions can a multi-tier authorization architecture preserve the independence of Origin, Semantic, and Consequence authority during runtime action evaluation?

RQ2: To what extent can independent authority separation reduce the rate of unauthorized actions executed by autonomous AI agents compared with unified permission models?

RQ3: How effectively does execution binding (cryptographic digest of the evaluated action) prevent post-authorization modification and authorization replay attacks?

RQ4: What operational overhead is introduced by the proposed three-tier authorization architecture compared with conventional and two-dimensional authorization models?

RQ5: Can consequence-tier evaluation detect actions whose downstream effects exceed the permitted impact boundary even when origin and semantic tiers pass?

RQ6: Which experimentally measurable conditions justify extending the architecture from simulation-based evaluation to real-world agent deployments?

H1 (Separation Hypothesis): Separating Origin from Semantic Authority improves identification of actions from legitimate sources that exceed their authorized scope compared with unified permission evaluation.

H2 (Consequence Hypothesis): Adding an independent Consequence Authority improves detection of actions whose effects exceed the permitted impact boundary compared with two-dimensional authorization.

H3 (Traceability Hypothesis): Independent authority decisions improve the traceability of authorization outcomes, measured as the Decision Traceability Rate (DTR).

H4 (Overhead Hypothesis): OSCA introduces measurable authorization latency compared with a unified baseline, measured as the Authorization Latency (L_A).

H5 (Security-Utility Hypothesis): OSCA can reduce unauthorized execution (measured by UAPR) while maintaining an acceptable legitimate-action acceptance rate (measured by LAAR).

### Foreknowledge of data or evidence

Data does not yet exist. No part of the data that will be used for this analysis plan exists, and no part will be generated until after this plan is registered.

### Explanation of foreknowledge and managing unintended influences

No empirical data exists at the time of registration. All evaluation data will be generated after registration using synthetic scenarios and established agent-security benchmarks (e.g., AgentDojo).

To reduce risk of unintended influence:

1. The experimental protocol (three configurations, ten scenarios, seven metrics) is specified in the research paper (§9) and frozen before registration.
2. The five hypotheses (H1–H5) and their associated metrics (UAPR, LAAR, FRR, ER, L_A, DTR, EBI) are pre-specified.
3. The architectural invariants (O1–O2, S1–S2, C1–C2, G1–G3) and threat model (T1–T8) are defined before any evaluation runs.
4. The Phase I implementation (51/51 tests, 5/5 simulation scenarios) is complete but does not include empirical or adversarial benchmarking; no pilot data has been collected.
5. Any change to the protocol after registration will be documented as a protocol amendment with explicit rationale.

The pre-registration separates architectural correctness (already established via structural tests) from empirical security performance (not yet measured).

---

## Research Design

### Study type

Simulation study: Using existing or synthetic data to assess performance of a model, mimic operation of an existing or proposed system, or predict possible outcomes in a controlled context. This may include demonstration of methods, many varieties of modeling, prediction of policy impacts, simulating behavior or outcomes in a population, and other designs.

### Intention for causal interpretation

No causal relationship inferred: This study is not intended to inform a causal relationship.

### Blinding of experimental treatments

No blinding is involved.

### Additional blinding during research or analysis

No blinding is required. The study uses deterministic architectural evaluation and simulation-based scenarios. There are no human subjects, no experimental manipulation of human behavior, and no subjective coding or interpretation. All authorization decisions are produced by the architectural components (Origin, Semantic, Consequence, Decision Engine, Execution Gateway), and all metrics are computed programmatically.

### Study design

Simulation-based comparative evaluation of three authorization architectures, executed against a fixed corpus of agent actions and attack scenarios.

Design type: Between-configuration comparison (three independent configurations), repeated within-scenario.

Configurations:

- A: Conventional authorization (unified permission evaluation).
- B: Two-dimensional authorization (source verification + action-scope verification).
- C: OSCA (Origin + Semantic + Consequence).

Scenarios (10):

- E1: Legitimate origin and action.
- E2: Unauthorized source.
- E3: Valid source, invalid action scope.
- E4: Valid source and scope, excessive impact.
- E5: Valid request requiring human approval.
- E6: Indirect prompt injection.
- E7: Modified action after approval.
- E8: Replayed authorization request.
- E9: Conflicting authority decisions.
- E10: Missing authorization evidence.

Metrics (7):

- UAPR: Unauthorized Action Prevention Rate.
- LAAR: Legitimate Action Acceptance Rate.
- FRR: False Rejection Rate.
- ER: Escalation Rate.
- L_A: Authorization Latency.
- DTR: Decision Traceability Rate.
- EBI: Execution-Binding Integrity.

Structure: Fully crossed evaluation. Each configuration (A, B, C) is evaluated against each of the 10 scenarios, producing 30 configuration-scenario cells. Each cell is run with N repeated trials (N ≥ 30) using the same action corpus and attack generators to estimate variance.

Between-subject vs. within-subject: All comparisons are between-configuration. The action corpus and attack scenarios are identical across configurations (paired comparison at the level of individual actions).

Assessment: All metrics are computed programmatically from the architectural components' decisions and execution records. No human coding is involved.

Counterbalancing: Not required. Execution order across configurations and scenarios is randomized per trial to control for order effects, but no counterbalancing of treatment assignment is needed because the configurations are deterministic.

Adversarial evaluation: Attack scenarios include identity impersonation, delegation-chain manipulation, semantic scope expansion, hidden instructions in retrieved content, parameter substitution, target substitution, consequence underestimation, authorization replay, post-authorization modification, and attempts to bypass the execution gateway. Established benchmarks such as AgentDojo are used where applicable.

### Randomization

No subject randomization. Configurations and scenarios are fixed in advance and identical across trials.

Randomization is used only for:

1. Execution order across the 30 configuration-scenario cells (to control for order effects).
2. Generation of synthetic action instances within each scenario, using a fixed random seed (42) so that the same corpus is evaluated across configurations.
3. Attack instance selection where the attack generator has stochastic elements, also with a fixed seed.

No random assignment of treatments to subjects is required, because this is a simulation-based comparison of architectures, not a human-subjects experiment.

---

## Sampling

### Data collection procedures

This study does not involve human subjects. All data is generated programmatically through simulation-based evaluation of three authorization architectures against a fixed corpus of agent actions and attack scenarios.

Data source: Local execution environment. No external datasets, no geographic regions, no recruiting.

Action corpus:

- Synthetic actions generated programmatically, covering the ten evaluation scenarios (E1–E10).
- Each action is a structured object A = (id, s, d, a, p, t, c, e), instantiated from templates.
- Attack instances (prompt injection, delegation abuse, scope expansion, replay, tampering) are generated programmatically.

Configurations:

- A: Conventional authorization (unified permission evaluation).
- B: Two-dimensional authorization (source verification + action-scope verification).
- C: OSCA (Origin + Semantic + Consequence).

Evaluation process:

1. For each configuration (A, B, C) and each scenario (E1–E10), generate N action instances from the fixed corpus (same seed across configurations).
2. Run each instance through the configuration's authorization pipeline.
3. Record the decision (PASS / DENY / ESCALATE / INDETERMINATE / AUTHORIZE / SUSPEND), the latency, and the trace.
4. If authorized, run the execution gateway and record whether execution occurred, and whether the executed action matches the authorized action.
5. Compute the seven metrics per configuration-scenario cell.
6. Repeat N times to estimate variance.

Inclusion criteria: All generated action instances from the fixed corpus. No exclusion based on outcome.

Exclusion criteria: None. Failed or incomplete executions are preserved and reported.

Expected duration: Not applicable. All data is generated in a single automated run (seconds to minutes per configuration-scenario cell).

### Sample size

Unit of analysis: action instance.

Planned sample sizes (per configuration-scenario cell):

- N = 100 action instances per scenario (E1–E10), per configuration (A, B, C).
- Total action instances: 3 configurations × 10 scenarios × 100 instances = 3,000.
- For attack scenarios, 100 attack instances per attack category.

Balanced design: Every configuration is evaluated against every scenario with the same N (100).

No nesting or multi-level structure. The design is fully crossed at the configuration × scenario level.

Repetition: Each configuration-scenario cell is run in R = 5 independent repetitions with different random seeds to estimate measurement variance (not to increase effective sample size).

### Sample size rationale

The sample size is determined by two considerations:

1. Precision of rate estimates. With N = 100 per cell, the 95% confidence interval for a proportion is approximately ±10 percentage points at p = 0.5, and ±4 percentage points at p = 0.9. This is sufficient for comparative evaluation across configurations, but not for fine-grained effect-size estimation.
2. Repeatability. R = 5 independent repetitions per cell allow estimation of measurement variance without making the study dependent on a single random seed.

No formal power analysis is conducted, because the primary goal is feasibility demonstration and comparative evaluation, not confirmatory hypothesis testing. A confirmatory study with larger N per cell is planned as a follow-up.

### Starting and stopping rules

Starting rule: Data collection begins after this registration is submitted. No evaluation data has been generated, observed, or analyzed before registration.

Stopping rule (per action instance): Each action instance terminates when:

- The authorization pipeline returns a decision (PASS, DENY, ESCALATE, INDETERMINATE, AUTHORIZE, or SUSPEND), OR
- The timeout is reached (classified as INDETERMINATE / SUSPEND, never AUTHORIZE).

Stopping rule (per configuration-scenario cell): Each cell terminates when N = 100 action instances have been evaluated and R = 5 independent repetitions are complete. No additional instances are collected.

Stopping rule (overall study): The study terminates after all 3 configurations × 10 scenarios × 5 repetitions are complete. No early stopping is planned. No data-dependent termination rules are used.

Post-collection analysis: After all data is collected, the seven metrics (UAPR, LAAR, FRR, ER, L_A, DTR, EBI) are computed per configuration-scenario cell and aggregated. Hypotheses H1–H5 are evaluated against the pre-specified metrics. Deviations from the protocol are reported as amendments.

---

## Variables

### Manipulated variables

Configuration (3 levels):

- A: Conventional authorization (unified permission evaluation).
- B: Two-dimensional authorization (source verification + action-scope verification).
- C: OSCA (Origin + Semantic + Consequence).

Scenario (10 levels, fixed not manipulated):

- E1: Legitimate origin and action.
- E2: Unauthorized source.
- E3: Valid source, invalid action scope.
- E4: Valid source and scope, excessive impact.
- E5: Valid request requiring human approval.
- E6: Indirect prompt injection.
- E7: Modified action after approval.
- E8: Replayed authorization request.
- E9: Conflicting authority decisions.
- E10: Missing authorization evidence.

The configuration is the only manipulated variable. Scenarios are fixed conditions used to elicit different authorization outcomes.

No randomization of participants. The assignment of actions to configurations is deterministic (every action is evaluated by every configuration).

### Measured variables

Outcome measures (per action instance, per configuration):

1. Authorization decision (categorical): AUTHORIZE, DENY, ESCALATE, SUSPEND (or INDETERMINATE). Recorded per action.
2. Execution outcome (binary): Executed / Not executed. Whether the execution gateway ran the action.
3. Authorization latency (continuous, ms): L_A = t_decision − t_request. Measured with time.perf_counter.
4. Execution-binding integrity (binary, per authorized execution): EBI_flag = 1 if executed action matches authorized action; 0 otherwise.
5. Decision trace completeness (binary, per decision): DTR_flag = 1 if a complete trace record exists (action id, decision, evidence, policy version, timestamp); 0 otherwise.
6. Layer verdicts (categorical, for configuration C only):
   - Origin verdict: PASS / DENY / ESCALATE.
   - Semantic verdict: PASS / DENY / ESCALATE.
   - Consequence verdict: PASS / DENY / ESCALATE / INDETERMINATE.
   - Recorded separately for diagnostic analysis.
7. Escalation event (binary): Escalated / Not escalated. Escalation target recorded if escalated.
8. Attack success (binary, attack scenarios only): Unauthorized action executed (1) / Blocked (0).

Predictors (for subsetting and diagnostic analysis, not for adjustment):

9. Scenario ID (E1–E10).
10. Configuration ID (A, B, C).
11. Attack category (for attack scenarios): impersonation, delegation, scope expansion, injection, substitution, underestimation, replay, tampering, bypass.

Covariates (not used for causal adjustment):

12. Action complexity (number of parameters).
13. Action verb type (read, write, execute, send, delete).

Variables used for subsetting:

- Scenario ID (to analyze per-scenario metrics).
- Configuration ID (to compare configurations).
- Attack category (to analyze per-attack detection).

No variables are used for exclusion. All generated action instances are analyzed.

### Indices

1. UAPR — Unauthorized Action Prevention Rate
   Formula: UAPR = (Blocked Unauthorized Actions) / (Total Unauthorized Actions) × 100
   Computed per configuration, per attack category, and overall.
   Measured in attack scenarios only (E2, E3, E4, E6, E7, E8, E9, E10).

2. LAAR — Legitimate Action Acceptance Rate
   Formula: LAAR = (Authorized Legitimate Actions) / (Total Legitimate Actions) × 100
   Computed per configuration.
   Measured in legitimate scenarios (E1, E5).

3. FRR — False Rejection Rate
   Formula: FRR = (Legitimate Denied) / (Total Legitimate) × 100
   Computed per configuration.
   Complement of LAAR for legitimate actions.

4. ER — Escalation Rate
   Formula: ER = (Escalated Actions) / (Total Actions) × 100
   Computed per configuration, per scenario.

5. L_A — Authorization Latency
   Formula: L_A = t_decision − t_request
   Reported as median, IQR, and 95th percentile per configuration.

6. DTR — Decision Traceability Rate
   Formula: DTR = (Complete Trace Records) / (Total Decisions) × 100
   Computed per configuration.
   A trace is complete if it includes action ID, decision, tier evidence, policy version, and timestamp.

7. EBI — Execution-Binding Integrity
   Formula: EBI = (Executions Matching Authorized Action) / (Total Executions) × 100
   Computed per configuration.
   An execution matches if the executed action's fingerprint equals the authorized action's fingerprint.

Aggregation:

- Per-action metrics are computed first.
- Then aggregated per configuration-scenario cell (mean or proportion).
- Then aggregated per configuration (mean across scenarios).
- Final comparisons use per-configuration aggregates.

No composite scores. Each index is reported separately. No weighting scheme is applied.

Derived comparisons (not indices themselves):

- ΔUAPR = UAPR_C − UAPR_A (C vs. A)
- ΔLAAR = LAAR_C − LAAR_A (C vs. A)
- ΔL_A = median(L_A_C) − median(L_A_A) (C vs. A)

These are reported as differences with 95% confidence intervals, not as single indices.

---

## Analysis Plan

### Statistical models

H1 (Separation improves identification of out-of-scope actions):
Test: Two-proportion z-test on UAPR (E3, E9) comparing Configuration C vs. Configuration A.
Outcome: Blocked / Total unauthorized (binary per action).
Model: Proportion difference ΔUAPR = UAPR_C − UAPR_A.
Inference: One-sided z-test (H1: ΔUAPR > 0), α = 0.05.
Effect size: Cohen's h with 95% CI.
Assumption: Independent action instances; adequate cell size (n ≥ 30 per configuration). If cell sizes < 30, use Fisher's exact test instead.

H2 (Consequence tier detects excessive-impact actions):
Test: Two-proportion z-test on UAPR restricted to E4 (excessive impact), comparing Configuration C vs. Configuration B.
Outcome: Blocked / Total (E4 only).
Inference: One-sided z-test (H2: ΔUAPR > 0), α = 0.05.
Effect size: Cohen's h with 95% CI.

H3 (Independent authority decisions improve traceability):
Test: Two-proportion z-test on DTR comparing Configuration C vs. Configuration A.
Outcome: Complete trace (binary per decision).
Inference: One-sided z-test (H3: ΔDTR > 0), α = 0.05.
Effect size: Cohen's h with 95% CI.

H4 (OSCA adds authorization latency):
Test: Mann-Whitney U test on L_A comparing Configuration C vs. Configuration A.
Outcome: L_A (continuous, ms, per action).
Inference: Two-sided test (H4: ΔL_A ≠ 0), α = 0.05.
Effect size: Rank-biserial correlation with 95% CI.
Assumption: Continuous latency, independent observations; Mann-Whitney is non-parametric and does not require normality. If sample size per configuration < 20, report descriptive statistics only.

H5 (OSCA reduces unauthorized execution without unacceptable legitimate-action rejection):
Test: Two co-primary comparisons, each one-sided:
(a) ΔUAPR (C vs. A) > 0 on unauthorized scenarios.
(b) ΔLAAR (C vs. A) ≥ −10 percentage points (non-inferiority margin).
Inference: Both must be satisfied for H5 to be supported.
Effect size: Cohen's h for each.

Positive control: E1 (legitimate origin and action) — expected AUTHORIZE across all configurations. If any configuration fails E1 systematically, the evaluation pipeline is invalid and is reported as a deviation.

Negative control: E6 (indirect prompt injection) and E7 (post-authorization modification) — expected DENY or SUSPEND in Configuration C. If C authorizes them, the architecture is reported as failing the corresponding invariant.

Manipulation check: None. Configurations are deterministic and instantiated programmatically.

Convergence criteria: Not applicable (no iterative estimation).

Model assumption checks:

- Proportions: independence (guaranteed by generation), adequate cell size (n ≥ 30); if not, use Fisher's exact test.
- Latency: non-parametric tests used; no normality assumption.
- No follow-up tests from omnibus tests (all comparisons are pre-specified pairwise).

No subgroup analyses beyond the pre-specified scenario-level analyses. No complex contrasts beyond the pairwise comparisons listed above.

### Transformations

Categorical coding (for tables, not for modeling):

- Configuration: A, B, C (nominal).
- Scenario: E1–E10 (nominal).
- Attack category: impersonation, delegation, scope expansion, injection, substitution, underestimation, replay, tampering, bypass (nominal).
- Authorization decision: AUTHORIZE, DENY, ESCALATE, SUSPEND (nominal).

Continuous variables:

- L_A (ms): reported as raw values (median, IQR, percentiles). No log transformation applied to inference tests (Mann-Whitney uses ranks).
- Counts (Blocked, Total): used directly in proportion tests.

Centering: Not applied. No regression model requires centering.

Recoding: None. Categorical variables remain nominal.

No transformations are performed on the data before inference tests.

### Inference criteria

Tests:

- H1, H2, H3: one-sided two-proportion z-test (α = 0.05).
- H4: two-sided Mann-Whitney U test (α = 0.05).
- H5: one-sided test for (a) and non-inferiority test for (b), each at α = 0.05.

P-values: Reported as exact two-sided or one-sided as specified. α = 0.05.

Multiple comparisons: Five pre-specified hypotheses. Apply Benjamini-Hochberg correction with FDR = 0.05 across the five tests. Report both raw and adjusted p-values. Conclusions use adjusted p-values.

Effect sizes: Cohen's h for proportions; rank-biserial correlation for Mann-Whitney. Reported with 95% CIs regardless of significance.

Confidence intervals: 95% CIs for all proportions and effect sizes.

Transition/decision rules:

- H1 supported if ΔUAPR > 0 and adjusted p < 0.05.
- H2 supported if ΔUAPR (E4) > 0 and adjusted p < 0.05.
- H3 supported if ΔDTR > 0 and adjusted p < 0.05.
- H4 supported if ΔL_A ≠ 0 and adjusted p < 0.05 (reported as "OSCA adds latency" if median L_A_C > median L_A_A).
- H5 supported if (a) and (b) both hold.

Bayes factors: Not used.

Model fit indices: Not applicable (no regression, SEM, or mixed-effects models).

Assumption checks:

- Adequate cell sizes: n ≥ 30 per proportion cell. If not met, Fisher's exact test replaces z-test.
- Latency: Mann-Whitney is non-parametric.
- No transformation of L_A is applied.

### Data inclusion and exclusion

Inclusion criteria:

- All generated action instances from the fixed corpus.
- All scenarios (E1–E10).
- All configurations (A, B, C).

Exclusion criteria:

- None based on outcome.
- No outlier removal. Latency outliers (e.g., from OS scheduling noise) are retained. Non-parametric tests are used precisely because they are robust to outliers.
- Failed or incomplete executions are preserved and reported; they are not dropped.
- SUSPEND / INDETERMINATE outcomes are included in UAPR and DTR (classified as "not executed" for EBI, and as "not authorized" for LAAR).

No data is excluded from the primary analysis.

### Missing data

No missing data is expected. All action instances are generated programmatically and evaluated in a single automated pass. Each instance produces a decision, a latency measurement, and a trace record.

If an instance fails due to environment error (e.g., process crash), it is recorded with status "Environment Error" and reported in a supplementary table. It is excluded from UAPR/LAAR/FRR calculations but retained in the total N for reporting.

No imputation is performed.

If a configuration fails to produce output for an entire scenario, this is reported as a protocol deviation and the affected cells are marked as not analyzable.

### Other planned analysis

Exploratory analyses (not used for hypothesis testing):

1. Per-layer verdict distribution in Configuration C: frequency of PASS / DENY / ESCALATE / INDETERMINATE per tier, per scenario. Diagnostic only.
2. Latency decomposition: L_A split into per-tier evaluation time (Origin, Semantic, Consequence) and decision-engine overhead. Reported per configuration.
3. Attack category breakdown: UAPR per attack category (impersonation, delegation, scope expansion, injection, substitution, underestimation, replay, tampering, bypass). Reported for Configuration C only.
4. Per-scenario heatmap: configurations × scenarios, colored by decision outcome distribution.
5. Sensitivity analysis: repeat metric computation with a stricter definition of "blocked" (only DENY and SUSPEND, excluding ESCALATE). Report whether conclusions change.
6. Error analysis: catalogue of false positives and false negatives in Configuration C, with case-level descriptions.

These analyses are exploratory, reported as supplementary material, and do not affect the pre-registered hypothesis tests.

---

## Other

### Context and additional information

This registration pre-registers the empirical evaluation protocol for OSCA (Origin, Semantic, and Consequence Authority), a multi-tier authorization architecture for autonomous AI agents.

Status at registration:

- Phase I (architectural specification and reference implementation) is complete.
- The implementation comprises:
  - Core: action representation, authorization, decision engine, execution gateway.
  - Authority: origin, semantic, and consequence tiers.
  - Governance: policy, delegation, escalation, audit.
  - Security: action binding, provenance, replay protection.
  - Simulation: five end-to-end scenarios.
  - Tests: 51 automated tests, all passing.
- No empirical or adversarial evaluation has been conducted yet. No pilot data has been collected. No results are reported.

What this registration pre-registers:

- The five hypotheses (H1–H5).
- The seven metrics (UAPR, LAAR, FRR, ER, L_A, DTR, EBI).
- The ten evaluation scenarios (E1–E10).
- The three configurations (A, B, C).
- The statistical tests for each hypothesis.
- The multiple-comparison correction (Benjamini-Hochberg, FDR = 0.05).

What this registration does not include:

- Human-subjects research.
- Empirical data collected before registration.
- Adversarial benchmark results.

Relation to other artifacts:

- Research paper: DOI 10.5281/zenodo.23851837.
- Figshare archive: DOI 10.6084/m9.figshare.34884411.
- Source repository: github.com/gitdeeper15/OSCA.
- Live documentation: osca-ai.netlify.app.

Scope of the claims:

- OSCA is an architectural proposal, not an empirically validated security mechanism.
- The Phase I implementation demonstrates that the architecture can be realized and tested; it does not demonstrate resistance to real-world adversarial agents.
- The evaluation protocol registered here is the first empirical test of the architecture and is designed to be falsifiable.

Protocol integrity:

- The protocol is frozen at registration.
- Any change after registration (to hypotheses, metrics, scenarios, or statistical tests) will be documented as a protocol amendment with explicit rationale and reported in the final evaluation report.
- Any deviation observed during evaluation will be documented as a deviation and reported alongside the primary results.

Ethics:

- This study does not involve human subjects.
- No IRB approval is required.
- No personal data is collected or processed.
- All action instances and attack scenarios are synthetic.

Data availability:

- All generated data, code, and analysis scripts will be made publicly available at the source repository upon completion.
- The evaluation pipeline is deterministic given a fixed random seed.

---

## Metadata

### Contributors
Samir Baladi

### Resource type
No resource type

### Description

Pre-registration of the OSCA architecture and empirical evaluation protocol.

OSCA is a multi-tier authorization architecture for autonomous AI agents. It separates authority into three independently verifiable tiers — Origin, Semantic, and Consequence — and binds them atomically at execution time. Every authorized action carries an auditable decision trace from origin through consequence.

This project pre-registers:

- The three-tier authority model.
- The formal authorization model (four decision states, precedence rules).
- Nine architectural invariants (O1–O2, S1–S2, C1–C2, G1–G3).
- Eight threat categories (T1–T8).
- A comparative experimental protocol with three configurations, ten scenarios, and seven metrics.

Related resources:

- Research paper DOI: 10.5281/zenodo.23851837
- Figshare archive: 10.6084/m9.figshare.34884411
- Code: github.com/gitdeeper15/OSCA
- Live documentation: osca-ai.netlify.app

### Registration Type
OSF Preregistration

### Registry
OSF Registries

### Associated project
https://osf.io/wp2se

### Date Created
Nov 2, 2026, 8:16 AM

### Date registered
Nov 2, 2026, 8:16 AM

### Subjects
- Databases and Information Systems
- Engineering
- Artificial Intelligence and Robotics
- Computer Sciences
- Computer Engineering
- Information Security
- Computer and Systems Architecture
- Physical Sciences and Mathematics

### Tags
- action authorization
- agentic AI safety
- AI governance
- authority separation
- autonomous AI agents
- consequence authority
- consequence-aware execution
- decision traceability
- execution binding
- multi-tier authorization
- origin authority
- OSCA
- runtime authorization
- semantic authority

### Affiliated Institutions
No affiliated institutions

### Funder Names
No information

### Language
No language

### Associated project
https://osf.io/wp2se

### Internet Archive link
https://archive.org/details/osf-registrations-5eqc9-v1

### License
CC-By Attribution 4.0 International

### Registration DOI
10.17605/OSF.IO/5EQC9

---

## Citations

### APA
Baladi, S. (2026, November 2). OSCA — Origin, Semantic, and Consequence Authority: Pre-registered Protocol. https://doi.org/10.17605/OSF.IO/5EQC9

### MLA
Baladi, Samir. "OSCA — Origin, Semantic, and Consequence Authority: Pre-registered Protocol." OSF, 2 Nov. 2026. Web.

### Chicago
Baladi, Samir. 2026. "OSCA — Origin, Semantic, and Consequence Authority: Pre-registered Protocol." OSF. November 2. doi:10.17605/OSF.IO/5EQC9.

### BibTeX

```bibtex
@misc{baladi2026osca_osf,
  author       = {Baladi, Samir},
  title        = {{OSCA} --- Origin, Semantic, and Consequence Authority:
                  Pre-registered Protocol},
  year         = {2026},
  month        = nov,
  day          = {2},
  publisher    = {OSF},
  doi          = {10.17605/OSF.IO/5EQC9},
  url          = {https://doi.org/10.17605/OSF.IO/5EQC9},
  note         = {OSF Preregistration}
}
```

---

Source: Center for Open Science · OSF Registries
Retrieved: 2026-11-02
