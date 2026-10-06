---
type: Form
lang: en
layout: default
title: Definition of Ready and Done Standard
nav_order: 7
token_pointer: /_tokens/forms/en/04_Planning/05_Quality/03_Definition_of_Ready_and_Done/04_05_03_Definition_of_Ready_and_Done_Guide.npy
token_count: 1212
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.991592+00:00'
---

## Tasleemat Forms Guide
# Project Artifact: Definition of Ready and Done Standard

**Document Reference:** `PMO-04.05.03`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Definition of Ready and Done Standard** in alignment with the
Tasleemat framework.

---

### 1. What?
Two lists rather than a table, because each item is meaningful only as part of a set: a team that meets six of eight ready criteria has not met a reduced standard, it has not met it. The ready list states what work must satisfy before the team will pick it up, and the done list states what must be true before work is called finished, each item written so somebody other than its author could check it.

---

### 2. Why?
Because the alternative is worse and quieter. A team with no ready standard discovers halfway through a sprint that a requirement was ambiguous, and a team with no done standard discovers at acceptance that half the work was never tested. Both failures are found late, which is exactly when they are expensive, and both are avoided by writing down in advance what would have caught them.

---

### 3. When?
Once, at the start of the team's work, and then revised only when the team can say which criterion stopped being useful. It is not a per-sprint document and it is not filled in per item. A revision is itself an event worth recording, because a standard that changes quietly is a standard nobody knows they are being measured against, and the first sign of that is a story shipped against the previous version.

---

### 4. Who?
Agreed by the team, which is the only arrangement that produces something they will actually apply to each other, and signed by the product owner and the team lead because the two of them are the people who feel its cost most: the product owner when ready criteria are used to hold up the backlog, the team lead when done criteria are enforced on a Friday afternoon. The quality manager's signature is there because the done criteria are mostly about testing, and someone with no authority over the work should be the one confirming that the testing actually happened.

---

### Tailoring Tips
*   Keep the ready standard short. It is the only reason the team can refuse work, and a standard that cannot be met is a standard that gets waived.
*   Write the done standard once and apply it without renegotiation. A justified exception belongs in an exception log, because a definition quietly rewritten is one nobody can hold anybody to.
*   Make every item checkable by somebody other than its author. Both definitions are about evidence, and the moment an item can only be confirmed by the person who wrote it, it is a statement of confidence rather than a criterion.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Project Scope Statement (PMO-04.02.05)
    *   Requirements Documentation (PMO-04.02.03)
*   **Optional / Contextual:**
    *   Tailoring Plan (PMO-02.01)
    *   AI Governance Plan (PMO-02.02)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Quality Audits (PMO-05.05)
    *   Product Acceptance Form (PMO-06.08)
    *   UAT Sign-off Form (PMO-06.10)
*   **Optional / Contextual:**
    *   Definition of Ready & Done (PMO-04.05.03)
    *   Vendor Scorecard (PMO-06.09)

---

### 5. How?
To accurately complete the Definition of Ready and Done Standard, populate the following sections based on
the project context (ensuring reference to `parameters.md` for the general
project variables):

*   **Definition of Ready (DoR):** What a piece of work must satisfy before the team will pick it up. The test for every item is that a second person can check it without asking the author: the acceptance criteria are written and are unambiguous, the dependency is named, the estimate exists. "The team believes it is understood" is not ready; "the acceptance criteria are in the ticket and no two readers would build different things from them" is.
*   **Definition of Done (DoD):** What must be true before a piece of work is called finished, stated so that somebody other than the author could confirm each one: the change is reviewed, the tests exist and pass, the documentation follows the change, and the acceptance criteria are met. This is the definition that decays, because every story shipped with an exception weakens it for the next one and nothing stops that becoming the rule. It is written once and applied without renegotiation; a justified exception is logged, not folded back into the definition.

---

### Associated Templates
* [📄 Printable Template (Markdown)](04_05_03_Definition_of_Ready_and_Done_Template.md)
* [🤖 Smart Generation Prompt](04_05_03_Definition_of_Ready_and_Done.md)
* [📊 Data Structure (JSON)](04_05_03_Definition_of_Ready_and_Done.json)
* [📈 Tabular Data (CSV)](04_05_03_Definition_of_Ready_and_Done.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [04_05_03_Definition_of_Ready_and_Done_Example.md](../../../../../examples/en/04_Planning/05_Quality/03_Definition_of_Ready_and_Done/04_05_03_Definition_of_Ready_and_Done_Example.md)
