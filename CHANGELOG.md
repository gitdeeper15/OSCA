# OSCA — Changelog

All notable changes to this research project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

**Versioning scheme.**

- **Research-draft versions** (`0.x.y-research-draft`): changes to the formal model, authorization model, architecture, or experimental protocol.
- **Implementation versions** (`0.x.y-implementation`): changes to the code (tiers, invariants, execution binding, traceability).
- **Pilot versions** (`0.x.y-pilot`): changes following pilot experiments.
- **Stable versions** (`x.y.z`): after multi-tier validation.

At the current stage, no empirical data has been collected.

---

## [0.1.0-research-draft] — 2026-11-01

### Initial Research Manuscript and Implementation Specification

This release establishes the complete initial research manuscript for
**OSCA — Origin, Semantic, and Consequence Authority: A Multi-Tier
Authorization Architecture for Autonomous AI Agents** and the first
specification of the implementation.

No empirical data is included. No pilot has been executed.

### Added — Research Framework

#### Formal Authorization Model
- Three-tier authority separation:
  - **Origin** — who authorized the action.
  - **Semantic** — what the action means in context.
  - **Consequence** — what the action produces in the world.
- Structural invariants linking tiers.
- Execution binding: actions can proceed only when all three tiers agree.
- Decision traceability: every authorized action carries an auditable trace.

#### Architectural Invariants
- Each tier is independently verifiable.
- No tier can override another.
- Execution binding is atomic.

#### Threat Model
- Compromised origin (identity spoofing).
- Semantic drift (misinterpreted intent).
- Consequence escalation (unauthorized side effects).
- Cross-tier collusion.

### Added — Implementation Specification

#### Core Modules (specified)
- `core/origin.py` — origin tier implementation.
- `core/semantic.py` — semantic tier implementation.
- `core/consequence.py` — consequence tier implementation.
- `core/execution_binding.py` — atomic binding of the three tiers.
- `core/traceability.py` — decision trace logging.

#### Package Structure
- `core/` — tier modules.
- `invariants/` — architectural invariants.
- `sandbox/` — isolation and differential testing.
- `tests/` — Python test suite.

### Added — Documentation

- `README.md` — project overview, architecture, six research domains.
- `AUTHORS.md` — Principal Investigator: Samir Baladi (ORCID 0009-0003-8903-0029).
- `CONTRIBUTING.md` — scope, standards, contact.
- `LICENSE` — MIT for code, CC-BY-4.0 for documentation.
- `CITATION.cff` — citation metadata with author block.
- `RESEARCH_PAPER/OSCA_Research_Paper.pdf` — 32-page manuscript.

### Added — Project Infrastructure

- `pyproject.toml` — package metadata.
- `setup.py` / `setup.cfg` — legacy compatibility.
- `requirements.txt` — runtime + dev dependencies.
- `Makefile` — common targets.
- `.gitignore`, `.coveragerc`, `.gitlab-ci.yml`, `.pre-commit-config.yaml`, `.readthedocs.yaml`.

### Not Included

- Empirical results (no pilot executed).
- Implementation of the tier modules (specified only).
- Package distribution on PyPI.

### Status

| Dimension | Status |
|-----------|--------|
| Formal model | Defined |
| Architecture | Specified |
| Authorization model | Specified |
| Threat model | Specified |
| Implementation | Specified only |
| Pilot data | Not yet collected |
| Empirical results | Not yet available |

---

## Roadmap

### 0.1.1-implementation (next)
- Implement `core/origin.py`, `core/semantic.py`, `core/consequence.py`.
- Implement `core/execution_binding.py` (atomic binding).
- Implement `core/traceability.py` (decision trace).
- Add unit tests for each tier.

### 0.2.0-implementation
- Complete implementation of all six tiers.
- Add integration tests.
- Prepare for pilot.

### 0.3.0-pilot
- Execute pilot study.
- Collect baseline metrics.
- Determine transition criteria outcomes.

---

## Notes on the Changelog

- Substantive changes only.
- Any change to the authorization model or architectural invariants after the pilot begins
  is recorded as a protocol amendment with explicit rationale.
- Baseline numeric thresholds are set **after** pilot calibration, not before.

---

**Last Updated:** 2026-11-01
**Current Version:** 0.1.0-research-draft
