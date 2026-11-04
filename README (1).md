# 📚 Research II — The Production and Control of Representations in Artificial Intelligence

### A Conceptual Architecture, Authority Structure, Representation Lifecycle, and Research Protocol

---

<!-- Core -->
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23940837.svg)](https://doi.org/10.5281/zenodo.23940837)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-a6ce39)](https://orcid.org/0009-0003-8903-0029)

<!-- PyPI -->
[![PyPI version](https://img.shields.io/pypi/v/pcr-ai?color=gold&label=PyPI)](https://pypi.org/project/pcr-ai/)
[![PyPI downloads](https://img.shields.io/pypi/dm/pcr-ai?color=gold&label=Downloads)](https://pypi.org/project/pcr-ai/)
[![PyPI status](https://img.shields.io/pypi/status/pcr-ai?color=gold)](https://pypi.org/project/pcr-ai/)

<!-- OSF Preregistration -->
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://osf.io/vmx2u)
[![OSF Project](https://img.shields.io/badge/OSF-Project-blue?logo=osf&logoColor=white)](https://osf.io/vmx2u)
[![Registration DOI](https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/8NZV2-blue)](https://doi.org/10.17605/OSF.IO/8NZV2)
[![Internet Archive](https://img.shields.io/badge/Internet%20Archive-Preserved-darkgreen?logo=internetarchive)](https://archive.org/details/osf-registrations-XXXXX-v1)
[![License: CC BY 4.0](https://img.shields.io/badge/Registration%20License-CC%20BY%204.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

<!-- Stack -->
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.4%2B-orange.svg)](https://pytorch.org)
[![Official Site](https://img.shields.io/badge/Official%20Site-pcr--ai.netlify.app-gold.svg)](https://pcr-ai.netlify.app)

<!-- Publication -->
[![Journal](https://img.shields.io/badge/Journal-Under%20Review-red)](https://journal.example.com)
[![Paper ID](https://img.shields.io/badge/Paper%20ID-PAPER--2026--001-blue)](https://journal.example.com)
[![ISSN](https://img.shields.io/badge/ISSN-XXXX--XXXX-green)](https://journal.example.com)

---

> *"The program's commitments are reported as specified, not as established: this repository presents an architecture and a research protocol, not findings."*
>
> — Research II, Abstract

> *"No empirical work has been performed under this protocol."*

---

## Table of Contents

- [Overview](#overview)
- [The Central Question](#the-central-question)
- [Foundational Documents](#foundational-documents)
- [Conceptual Architecture](#conceptual-architecture)
- [Authority Structure](#authority-structure)
- [Representation Lifecycle](#representation-lifecycle)
- [Research Questions](#research-questions)
- [Document Governance](#document-governance)
- [Relation to Research I](#relation-to-research-i)
- [Platforms & Mirrors](#platforms--mirrors)
- [Project Structure](#project-structure)
- [OSF Preregistration](#osf-preregistration)
- [Version History](#version-history)
- [Citation](#citation)
- [Author](#author)
- [License](#license)

---

## Overview

**Research II** examines the structural relations through which representations are constituted before they reach a recipient, treating representation itself as the central analytical object rather than treating the model, the platform, or the user in isolation.

The program is specified through **four foundational documents**, developed in sequence and adopted individually. This repository consolidates them into a single research protocol. It does not add new architectural commitments beyond what the four source documents specify, and it does not report empirical findings.

---

## The Central Question

> **Who produces the representations a recipient encounters through AI systems, who controls their formation, availability, and appearance, and who consumes them?**

This question is **structural**, not accusatory or normative. It does not presuppose that production, control, and consumption are each located in a single entity, that any one party necessarily dominates the chain, or that current arrangements are illegitimate. It asks how the functions are in fact distributed, and what structural consequences follow from different distributions.

---

## Foundational Documents

| # | Document | Version | Status |
|---|---|---|---|
| 1 | **Conceptual Architecture** | 0.2 | ✅ Adopted |
| 2 | **Authority Structure** | 0.2 | ✅ Adopted |
| 3 | **Representation Lifecycle** | 0.2 | ✅ Adopted |
| 4 | **Research Questions** | 0.2 | ✅ Adopted |

Development is strictly sequential: no further architectural work, no system selection, and no methodological commitments proceed from a given document until it is adopted.

---

## Conceptual Architecture

*Status: Adopted, version 0.2.*

The architecture distinguishes **five functional units**, defined by function rather than by institutional identity, ownership, or technical component:

| # | Functional Unit | Function |
|---|---|---|
| 1 | **Producer** | Originates or supplies the material from which the representation is constituted. |
| 2 | **Model / Generative System** | Transforms inputs into a representation. |
| 3 | **Platform / Controller** | Governs the conditions of production, presentation, and availability. |
| 4 | **Distribution Interface** | Determines how the representation reaches and appears to the recipient. |
| 5 | **Recipient / Consumer** | Receives the representation and engages with it. |

**Foundational assumption (negative):** Research II does not assume that each function has a distinct owner, nor that any one function subsumes the others.

### Five Foundational Distinctions

```

Production    ≠ Control
Control       ≠ Distribution
Distribution  ≠ Reception
Function      ≠ Owner
Governance    ≠ Execution

```

### Five Provisional Configuration Patterns

- **Concentrated Configuration** — multiple functions performed by a single entity
- **Partially Integrated Configuration** — some functions combined, others distributed
- **Functionally Separated Configuration** — each function performed by a distinct entity
- **Distributed Authority** — a single function jointly exercised by multiple entities
- **Hybrid Distribution** — different functions exhibit different degrees of concentration

---

## Authority Structure

*Status: Version 0.2, adopted 2026-11-04. Depends on the Conceptual Architecture (adopted, v0.2).*

The Authority Structure distinguishes **five authority types** and establishes that authority is analytically distinct from function — a function is what is done; an authority is the right to do it.

| Authority | Object | Central Question |
|---|---|---|
| **Production Authority** | The representation as originated | Who has the authority to originate this representation? |
| **Transformation Authority** | The representation as modified | Who has the authority to modify or reshape this representation? |
| **Selection Authority** | The representation as presented | Who has the authority to decide what is shown and what is not? |
| **Distribution Authority** | The representation as available | Who has the authority to determine access, reach, and retention? |
| **Interpretive Authority** | The representation as interpreted | Who has the authority to present a particular interpretation as the accepted one? |

### Five Pairwise Distinctions

```

Production     ⊥ Transformation
Transformation ⊥ Selection
Selection      ⊥ Distribution
Distribution   ⊥ Interpretation
Production     ⊥ Interpretation

```

Each pair is analytically separable even where it is empirically joined in a specific system.

---

## Representation Lifecycle

*Status: Version 0.2, adopted 2026-11-04. Depends on the Conceptual Architecture and the Authority Structure.*

The lifecycle traces the path of a representation through **six structural stages**:

| Stage | Description |
|---|---|
| 1. **Origination** | The representation is constituted from material. |
| 2. **Transformation** | The representation is modified, reshaped, or regenerated. |
| 3. **Selection** | The representation is included in or excluded from the presented set. |
| 4. **Distribution** | The representation is made available (or restricted). |
| 5. **Reception** | The representation reaches the recipient. |
| 6. **Re-origination** | The recipient may produce a new representation, entering the lifecycle again. |

### The Canonical Path

```

Origination → Transformation → Selection → Distribution → Reception → [Re-origination → …]

```

> The canonical path is **analytically clean, empirically rare, and useful as a baseline for comparison**. It is a reference point, not a norm.

### Five Structurally Distinct Alternative Paths

| Path | Structure |
|---|---|
| **Merged Path** | [Origination + Transformation + Selection + Distribution] → Reception → [Re-origination → …] |
| **Skipped Transformation** | Origination → Selection → Distribution → Reception |
| **Skipped Selection** | Origination → Transformation → Distribution → Reception |
| **Distributed Origination** | [Producer₁ + Producer₂ + … + Producerₙ] → Transformation → … |
| **Iterative Re-origination** | Origination → … → Reception → Re-origination → Transformation → … → Reception → … |

These five alternative paths are not exhaustive; they are structurally distinct reference points.

---

## Research Questions

*Status: Version 0.2, adopted 2026-11-04. 20 questions across 4 families.*

### Family A — Conceptual (Priority: First)

- **RQ-A1.** Are the five functional units analytically distinct in actual systems, or do they routinely merge?
- **RQ-A2.** Are the five authority types exercised by distinct entities, or do specific configurations of concentration appear systematically?
- **RQ-A3.** What structural conditions determine whether functions and authorities coincide or diverge?

### Family B — Authority (Priority: Second)

- **RQ-B1.** How is Production Authority distributed across entities in AI-mediated representational systems?
- **RQ-B2.** How is Transformation Authority distributed, and under what conditions does it diverge from Production Authority?
- **RQ-B3.** How is Selection Authority distributed, and what criteria govern the selection of representations for presentation?
- **RQ-B4.** How is Distribution Authority distributed, and what conditions constrain access, reach, and retention?
- **RQ-B5.** How is Interpretive Authority distributed, and whose interpretations are presented as authoritative?
- **RQ-B6.** What patterns of authority distribution recur across different systems, and what structural factors explain these patterns?

### Family C — Lifecycle (Priority: Third)

- **RQ-C1.** Which lifecycle paths appear in practice, and with what frequency?
- **RQ-C2.** What structural factors determine which path a representation takes?
- **RQ-C3.** Where do structural interruptions occur, and what do they reveal about the exercise of authority?
- **RQ-C4.** How do re-origination cycles interact with the lifecycle's earlier stages, and what structural transformations occur across cycles?
- **RQ-C5.** How does the Recipient's interpretive authority operate on representations that have passed through different lifecycle paths?

### Family D — Boundary (Priority: Later)

- **RQ-D1 (Boundary with Research I).** How does the structural distribution of authority over representations affect the recipient's epistemic standards, as examined in Research I?
- **RQ-D2 (Methodological Scope).** What methodological approaches are adequate for examining the questions in families A–C: analytical, empirical, or both?

### Priority and Sequencing

| Priority | Questions | Rationale |
|---|---|---|
| **First** | RQ-A1, RQ-A2, RQ-A3 | Test the architecture's own categories. |
| **Second** | RQ-B1 – RQ-B6 | Operationalize authority distribution. |
| **Third** | RQ-C1 – RQ-C5 | Operationalize the lifecycle. |
| **Later** | RQ-D1, RQ-D2 | Boundary and methodological questions. |

---

## Document Governance

The program's four foundational documents are developed and adopted **sequentially**, each depending on the documents before it:

1. **Conceptual Architecture** — depends on nothing prior; establishes the functional vocabulary.
2. **Authority Structure** — depends on the Conceptual Architecture; establishes the authority vocabulary.
3. **Representation Lifecycle** — depends on both prior documents; establishes the stages and paths.
4. **Research Questions** — depends on all three prior documents; formulates the questions these documents make askable.

**Current document status:**

| Document | Version | Status |
|---|---|---|
| Conceptual Architecture | 0.2 | ✅ Adopted |
| Authority Structure | 0.2 | ✅ Adopted |
| Representation Lifecycle | 0.2 | ✅ Adopted |
| Research Questions | 0.2 | ✅ Adopted |

After adoption of all four documents, the program will determine its methodological scope (RQ-D2) and proceed accordingly.

---

## Relation to Research I

**Research I** — *Epistemic Discipline in the Age of Artificial Intelligence: A Three-Study Research Protocol* (Baladi, 2026; DOI [10.5281/zenodo.23876902](https://doi.org/10.5281/zenodo.23876902)) — examines whether repeated interaction with an AI system can change a recipient's standards for interpreting system behavior and accepting its outputs. Its unit of analysis is the recipient's evolving interpretive standards across repeated interactions with a single system.

**Research II** examines the structural distribution of production, transformation, selection, distribution, and interpretive authority over representations across the broader chain of functions, independent of any single recipient's history of interaction.

The two programs are **methodologically independent**. RQ-D1 is retained as a question about their possible intersection, not as an integration of them. At the time of this manuscript, neither program has produced empirical findings; RQ-D1 is recorded as a later-priority question and is not pursued further here.

---

## Platforms & Mirrors

| Platform | URL | Role |
|---|---|---|
| **GitHub (Primary)** | [github.com/gitdeeper/pcr-ai](https://github.com/gitdeeper/pcr-ai) | Source code, issues, PRs |
| **GitLab** | [gitlab.com/gitdeeper/pcr-ai](https://gitlab.com/gitdeeper/pcr-ai) | Mirror repository |
| **Codeberg** | [codeberg.org/gitdeeper/pcr-ai](https://codeberg.org/gitdeeper/pcr-ai) | Mirror repository |
| **Bitbucket** | [bitbucket.org/gitdeeper/pcr-ai](https://bitbucket.org/gitdeeper/pcr-ai) | Mirror repository |
| **PyPI** | [pypi.org/project/pcr-ai](https://pypi.org/project/pcr-ai/) | Python package distribution |
| **Zenodo** | [doi.org/10.5281/zenodo.23940837](https://doi.org/10.5281/zenodo.23940837) | Citable DOI, paper archive |
| **Figshare** | [10.6084/m9.figshare.34908597](https://doi.org/10.6084/m9.figshare.34908597) | Secondary archive (figures, data) |
| **Website** | [pcr-ai.netlify.app](https://pcr-ai.netlify.app) | Live documentation |
| **OSF** | [osf.io/vmx2u](https://osf.io/vmx2u) | Preregistration |
| **Internet Archive** | [archive.org/details/osf-registrations-XXXXX-v1](https://archive.org/details/osf-registrations-XXXXX-v1) | Permanent preservation |
| **ORCID** | [orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) | Author identity |

---

## Project Structure

```

PCR_AI/
├── docs/
│   ├── 01_conceptual_architecture/    # v0.2 — Adopted
│   ├── 02_authority_structure/        # v0.2 — Adopted
│   ├── 03_representation_lifecycle/   # v0.2 — Adopted
│   ├── 04_research_questions/         # v0.2 — Adopted
│   ├── ITERATION_LOG.md
│   └── comprehensive_audit_report.json
├── protocol/
│   └── methodology_scope.md           # v0.2 — Adopted (Mixed Methods)
├── literature/
│   ├── review_status.md              # Stage 1 completed
│   ├── review_matrix.csv              # 16 categories × 5 traditions
│   ├── review_stage_1.md             # Stage 1 narrative report
│   ├── references_stage_2.md          # Stage 2 — 56 proposed references
│   ├── review_stage_2b.md             # Stage 2b — Distinct verification
│   └── synthesis_draft.md            # Section 2 draft (~1,400 words)
├── figures/                            # Diagrams (Figures 1–4)
├── ANALYSIS/
│   ├── ANALYSIS_REPORT.md
│   └── analysis_insights.json
├── DATA/
│   └── raw/
│       └── input.json
├── EXTERNAL_REVIEW/
│   ├── review_PCR_AI_2026-11-04.md
│   ├── review_coordinator.json
├── PUBLICATION/
│   ├── Netlify/                        # Official project website
│   │   ├── netlify.toml
│   │   ├── project.json
│   │   └── public/
│   ├── dist/
│   │   ├── pcr-ai-1.0.0-py3-none-any.whl
│   │   └── pcr-ai-1.0.0.tar.gz
│   └── Production_Control_Representations_In_Artificial_Intelligence.pdf
├── REPORTS/                            # Audit, compliance, and consistency reports
├── VALIDATION/
│   └── .lock/
│       └── language_lock_report.json
├── AUTHORS.md
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── FINAL_REPORT.json
├── INVENTORY.md
├── LICENSE
├── OSF_REGISTRATION.md
├── PROJECT_SUMMARY.txt
├── README.md
├── VERSION
├── manifest.json
├── scientific_state.json
├── requirements.txt
├── setup.cfg
└── setup.py

```

**Note on layout:** The four foundational documents are consolidated in this README (Sections 3–6) and mirrored as directory stubs under `docs/` to enforce sequential adoption (Section 8.1). The operational directories (`ANALYSIS/`, `DATA/`, `EXTERNAL_REVIEW/`, `PUBLICATION/`, `REPORTS/`, `VALIDATION/`) are research-infrastructure artifacts, not architectural commitments of the protocol.

---

## OSF Preregistration

[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://osf.io/vmx2u)
[![Registration DOI](https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/8NZV2-blue)](https://doi.org/10.17605/OSF.IO/8NZV2)

**Registration DOI:** `10.17605/OSF.IO/8NZV2`
**Project:** [osf.io/vmx2u](https://osf.io/vmx2u)
**Archive:** [Internet Archive](https://archive.org/details/osf-registrations-XXXXX-v1)
**License:** CC-By Attribution 4.0 International

---

## Version History

| Version | Release | Focus | Status |
|---|---|---|---|
| **v0.2** | 2026-11 | Conceptual Architecture adopted | ✅ Adopted |
| **v0.1** | 2026-11 | Authority Structure, Lifecycle, Questions specified | ⏳ Pending |
| **v0.1** | 2026-11 | Initial Program Manuscript — Architecture Specification Stage | Research |

> **Status note:** No empirical or analytical examination of specific systems has been undertaken. The five functional units, five authorities, six lifecycle stages, and five alternative paths are **analytical proposals, not empirically validated categories**.

---

## Citation

### Primary Manuscript (Research II)

```bibtex
@techreport{baladi2026research2,
  author       = {Baladi, Samir},
  title        = {The Production and Control of Representations in Artificial Intelligence --- Research II: A Conceptual Architecture, Authority Structure, Representation Lifecycle, and Research Protocol},
  institution  = {Ronin Institute / Rite of Renaissance},
  type         = {Research Protocol},
  year         = {2026},
  month        = {November},
  version      = {0.1},
  doi          = {10.5281/zenodo.23940837},
  url          = {https://doi.org/10.5281/zenodo.23940837},
  note         = {Initial Program Manuscript --- Architecture Specification Stage.
                  All four foundational documents adopted (v0.2): Conceptual Architecture, Authority Structure, Representation Lifecycle, and Research Questions.}
}
```

Software Archive (Zenodo)

https://zenodo.org/badge/DOI/10.5281/zenodo.23940837.svg

```bibtex
@software{baladi2026pcr-ai,
  author       = {Baladi, Samir},
  title        = {{PCR\_AI} v1.0.0: Reference Implementation for Research II --- The Production and Control of Representations in Artificial Intelligence},
  year         = {2026},
  month        = {November},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23940837},
  url          = {https://doi.org/10.5281/zenodo.23940837},
  note         = {GITDEEPER LAB ZERO V6 Series.
                  Ronin Institute / Rite of Renaissance.
                  PyPI: pip install pcr-ai}
}
```

OSF Preregistration

https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/8NZV2-blue

```bibtex
@misc{baladi2026pcr-ai_osf,
  author       = {Baladi, Samir},
  title        = {{PCR\_AI}: Preregistration --- Research II Protocol},
  year         = {2026},
  month        = {November},
  publisher    = {OSF Registries},
  doi          = {10.17605/OSF.IO/8NZV2},
  url          = {https://doi.org/10.17605/OSF.IO/8NZV2},
  note         = {OSF Preregistration. Associated project: https://osf.io/vmx2u.
                  Archived: https://archive.org/details/osf-registrations-XXXXX-v1.
                  License: CC-By Attribution 4.0 International.}
}
```

PyPI Package

https://img.shields.io/pypi/v/pcr-ai?color=gold&label=PyPI%20pcr-ai

```bibtex
@misc{baladi2026pcr-ai_pypi,
  author       = {Baladi, Samir},
  title        = {{pcr-ai}: Python Package for Research II Protocol Implementation},
  year         = {2026},
  month        = {November},
  howpublished = {Python Package Index (PyPI)},
  url          = {https://pypi.org/project/pcr-ai/},
  note         = {Install: \texttt{pip install pcr-ai}.
                  Ronin Institute / Rite of Renaissance. MIT License.}
}
```

Journal Submission

https://img.shields.io/badge/Journal-Under%20Review-red
https://img.shields.io/badge/Paper%20ID-PAPER--2026--001-blue

```bibtex
@article{baladi2026research2_journal,
  author       = {Baladi, Samir},
  title        = {The Production and Control of Representations in Artificial Intelligence --- Research II: A Conceptual Architecture, Authority Structure, Representation Lifecycle, and Research Protocol},
  journal      = {Journal of Educational Quality Assurance},
  volume       = {1},
  number       = {1},
  year         = {2026},
  month        = {November},
  issn         = {XXXX-XXXX},
  paperid      = {PAPER-2026-001},
  url          = {https://journal.example.com},
  note         = {Under review. Open access journal.}
}
```

---

Author

Samir Baladi
Interdisciplinary AI Researcher — Ronin Institute / Rite of Renaissance

· Research Area: Science and Technology Studies, Media and Platform Studies, Human-AI Interaction
· Research Domain: Structural Analysis of Representational Authority in AI-Mediated Systems
· Research Type: Prospective Structural Research Protocol — Conceptual, Authority, and Lifecycle Architecture
· 📧 gitdeeper@gmail.com
· 🔗 ORCID: 0009-0003-8903-0029
· 🌐 Official Site
· 🐙 GitHub
· 🦊 GitLab
· 🟦 Codeberg
· 🪣 Bitbucket
· 🐝 pcr-ai on PyPI

---

License

```
MIT License
Copyright © 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

Research II — Initial Program Manuscript v0.1
© 2026 Samir Baladi — Ronin Institute / Rite of Renaissance — MIT License
Zenodo: 10.5281/zenodo.23940837 | Official Site: pcr-ai.netlify.app | PyPI: pcr-ai
