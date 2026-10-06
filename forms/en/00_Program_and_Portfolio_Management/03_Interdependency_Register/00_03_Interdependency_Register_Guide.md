---
type: Form
lang: en
layout: default
title: Interdependency Register
nav_order: 1
token_pointer: /_tokens/forms/en/00_Program_and_Portfolio_Management/03_Interdependency_Register/00_03_Interdependency_Register_Guide.npy
token_count: 2502
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.038703+00:00'
form_id: PMO-00.03
status: approved
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: Interdependency Register

**Document Reference:** `PMO-00.03`

This document provides a comprehensive, professional reference to understand the
purpose and effective usage of the **Interdependency Register** in alignment with
the Tasleemat framework.

---

### 1. What?
A formal Tasleemat-aligned project document known as the **Interdependency
Register**, recording the relationships between the components of a program,
portfolio, or project, in the specific sense that one cannot proceed, or cannot
proceed on its own dates, until another delivers something.

It records the basis on which the register is maintained, the internal
dependencies with their required and agreed dates side by side, the external
dependencies with the contractual basis on which each rests, and what has been
escalated about the dependencies that are not holding.

---

### 2. Why?
Because a dependency recorded as a project name rather than a deliverable
cannot be chased when that project slips: nobody knows what to ask for. And
because a register that mixes internal and external dependencies invites the
reader to treat an external commitment as though it were a request to a
colleague. The contractual basis column is what tells the two apart.

---

### 3. When?
This artifact is prepared at the **PROGRAM AND PORTFOLIO MANAGEMENT** Process
Group, and maintained on the review cycle recorded in its basis section. It is
a living record rather than a document produced once, because a dependency
register describes a plan that is still being made.

---

### 4. Who?
**Responsibilities:** Owned by the Program Manager or Portfolio Manager, with
each row's content supplied by the owner of the successor, since that is the
person who knows what they are waiting for. External dependency rows are owned
by whoever holds the relationship with the external party, which is usually not
the person who needs the deliverable.

---

### Tailoring Tips
*   The register may be maintained at portfolio level, covering all
    interdependencies between initiatives, or at program level covering only
    those between components. The form should say which, because the two answer
    different questions.
*   Where the organisation runs a dependency log in a planning tool, the
    register may be an extract rather than the source of truth. If so, record
    that, so a reader does not treat the extract as authoritative.
*   Add or remove rows as needed. Where two projects have a reciprocal
    dependency, record both directions rather than one row with both names, so
    each direction can be tracked and agreed separately.
*   The external dependency section may be maintained separately by a
    procurement or vendor governance function, in which case cross-reference it
    rather than duplicating it.
*   A register with many rows benefits from a status filter, which is the
    reason for insisting on a fixed status set rather than free text.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Program Charter (PMO-00.02) or Portfolio Roadmap (PMO-00.01)
    *   Project Schedules (PMO-04.03.08)
*   **Optional / Contextual:**
    *   Milestone Lists (PMO-04.03.04)
    *   Procurement Plans (PMO-04.09.01)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Project Schedules (PMO-04.03.08)
    *   Program Status Reports (PMO-06.01)
    *   Risk Registers (PMO-04.08.02)
*   **Optional / Contextual:**
    *   Lookahead Planning Log (PMO-04.03.10)
    *   Change Requests (PMO-05.03)

---

### 5. How?
To accurately and professionally complete the **INTERDEPENDENCY REGISTER**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Register Scope and Level:** What this register covers and at what level it is maintained, whether portfolio-wide, program-level, or project-level. The level decides which plan the register is compared against, and a portfolio register read against a project schedule produces conclusions that are true of neither.
*   **Programs or Projects Covered:** The programs, projects, or components whose mutual dependencies are recorded, by name and identifier so the list can be joined to the portfolio roadmap. A register that names no components cannot be checked for completeness, and an incomplete register reads as a complete one.
*   **Source of Truth or Extract:** Whether this register is the authoritative record or an extract from a planning tool. Record which, because a reader who treats an extract as authoritative will act on a date that has since moved, and the error is invisible until the dependency is missed.
*   **Review Cycle:** How often the register is reviewed and by which forum. The cycle is what makes two versions comparable, and a register refreshed on no cycle describes the portfolio as it once was rather than as it is.
*   **Register Owner:** The single role accountable for the register as a whole, which is normally not the owner of any one dependency in it. Where this is left blank, the register has contributors but no one who notices that a row has gone stale.
*   **Last Updated:** The date the register was last reviewed, and against which version of the portfolio roadmap. Without it, a reader has no way to tell a current register from an abandoned one, and the two look identical on the page.
*   **ID:** The identifier for the dependency, used in the escalation section and in reporting so a threatened dependency can be referred to without ambiguity.
*   **Predecessor:** The project or component that must deliver first, named and identified so the row can be joined to the portfolio roadmap. "Project B" is not a predecessor; the component's own identifier is, because that is what survives it being renamed.
*   **Successor:** The project or component that is waiting. Where the same predecessor is needed by several successors, record a row for each rather than listing them together, because the required dates and the impacts differ and one date cannot serve all of them.
*   **Deliverable or Condition:** What specifically is being waited on, stated so that it can be confirmed as delivered or not. "Waiting for Project B" cannot be chased when Project B slips, because nobody knows what to ask for; "waiting for the signed data migration specification from Project B" can be chased, and can be closed.
*   **Dependency Type:** Whether the relationship is Finish to Start, Start to Start, Finish to Finish, or Start to Finish. The type determines how much float the successor has, and Finish to Start is the only one needing no explanation; the others arise where two projects must move together and cannot be read from the names alone.
*   **Required By:** The date by which the successor needs the deliverable. This is the successor's requirement, and recording the predecessor's forecast here instead hides the gap between what is needed and what has been promised, which is the only figure worth watching.
*   **Agreed Date:** The date the predecessor has committed to. Kept beside the required date so the gap between the two is visible in the register itself; where the agreed date is later than the required date, that gap is the dependency's risk, and it is usually found out by being overrun rather than by being read.
*   **Status:** Where the dependency currently stands against the fixed set agreed for this register, such as On Track, At Risk, Breached, or Agreed. A free-text status cannot be filtered, and a register of forty dependencies that cannot be filtered is a document nobody consults when they need to answer a question about one of them.
*   **Impact if Late:** What happens to the successor if the predecessor misses the required date, in schedule, cost, or scope terms. A dependency with no stated impact cannot be escalated, because nobody can say what is at stake, and an escalation that cannot state the stake is usually declined.
*   **ID:** The identifier for the external dependency, so it can be referred to in reporting and joined to any contract or correspondence that covers it.
*   **External Party:** The organisation outside the program through which the dependency runs, named by the role it plays rather than by the individual, so the row survives a change of contact and remains readable to someone who has not met them.
*   **Dependency Description:** What the external party is expected to provide, approve, or decide, and by when. State it as something that can be confirmed as done, since a dependency described as ongoing support cannot be closed and will therefore never show as satisfied.
*   **Contractual Basis:** Whether the dependency is covered by a contract, a memorandum of understanding, a formal letter, or nothing in writing. This column decides whether the dependency can be enforced, and a commitment taken in correspondence and one written into a contract look identical in every other column while being entirely different in practice.
*   **Required By:** The date the program needs this, which for an external dependency is usually a hard commercial or regulatory date rather than a date the program chose. Record where the date comes from, because an external date the program did not set is a date it cannot move.
*   **Status:** Where the dependency stands against the fixed set. For external dependencies record separately whether the external party has confirmed it, since the program can know its own position accurately and the other party's only by asking.
*   **Owner:** Who is accountable for the relationship with the external party, which is normally not the person who needs the deliverable. Separating the two is what stops the urgency of a need being communicated through whoever happens to have the contact.
*   **Dependency ID:** The dependency the escalation concerns, so the row can be joined back to the register. An escalation recorded without this reference cannot be traced to the thing it was about, and the next cycle repeats it.
*   **Trigger:** What caused the escalation: a missed agreed date, an explicit refusal, a change on the predecessor's side, or a commercial dispute. The remedy differs in each case, and an escalation that does not distinguish them tends to produce a general escalation that resolves nothing.
*   **Escalated To:** Who it was escalated to, named rather than described, so the reader knows whether the person holds the authority to decide. An escalation to somebody who cannot decide records the disagreement without recording a resolution.
*   **Action Agreed:** What was decided or agreed, which is what stops the same question being escalated again next cycle with the same outcome. Where nothing was agreed, record that explicitly, because a blank action and an unresolved escalation look identical once the register has been read a few times.
*   **Date:** When the escalation happened, and where relevant when it will next be reviewed. An escalation without a date has no position in the sequence, and the register becomes a list of grievances rather than a record of decisions.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](00_03_Interdependency_Register_Template.md)
* [🤖 LLM Generation Prompt](00_03_Interdependency_Register.md)
* [📊 Data Structure (JSON)](00_03_Interdependency_Register.json)
* [📈 Tabular Data (CSV)](00_03_Interdependency_Register.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [00_03_Interdependency_Register_Example.md](../../../../examples/en/00_Program_and_Portfolio_Management/03_Interdependency_Register/00_03_Interdependency_Register_Example.md)

</div>
