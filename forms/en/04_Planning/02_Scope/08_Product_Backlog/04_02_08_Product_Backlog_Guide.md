---
lang: en
layout: default
title: Product Backlog
nav_order: 1
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: Product Backlog

**Document Reference:** `PMO-04.02.08`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Product Backlog** in alignment with
the Tasleemat framework.

---

### 1. What?
A formal Tasleemat-aligned project document known as the **Product Backlog**,
used to document and prioritize the requirements, features, functions, and
user stories for releases or sprints. It is developed at the very beginning of
a project, often in conjunction with the product vision, and it keeps track of
all the requirements along with their priority and the release they will be
incorporated into.

It records five elements: the identifier, a summary description, the priority,
the user story, and the status. It also carries the four optional columns the
tailoring guidance calls for: story points, target sprint or release, user
type, and category.

---

### 2. Why?
To keep every requirement, its priority, and its target release in one place
that is visible to the whole team, so that what is being built next is a
matter of record rather than of memory or of who asked most recently.

---

### 3. When?
This artifact is prepared at the **PLANNING** Process Group, under Scope. It
is developed at the very beginning of the project and is updated throughout
it.

---

### 4. Who?
**Responsibilities:** Maintained by the Product Owner, who is accountable for
the ordering and for its accuracy. Estimated, reviewed, and updated by the
team.

---

### Tailoring Tips
*   You can add estimating information such as story points.
*   To provide more detail you can indicate which sprint a feature or function
    will be incorporated into.
*   You may want to indicate the user type that will benefit from the
    requirement, such as customer, administrator, manager, etc.
*   For large projects it helps to categorize requirements, so having a column
    that indicates the category can be useful.
*   The Story Points, Target Sprint or Release, User Type, and Category columns
    are optional. Remove any of them the project does not use, rather than
    leaving them empty down every row.
*   Add or remove rows as needed. On a large project the backlog will outgrow
    any single sheet, and a backlog that is split without a stated rule will
    drift into two backlogs.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Project Charter (PMO-03.01)
    *   Stakeholder Requirements
*   **Optional / Contextual:**
    *   Product Vision (PMO-03.02)
    *   Assumption Log (PMO-03.03)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Work Breakdown Structure / WBS (PMO-04.02.06)
    *   Project Schedule (PMO-04.03.08)
    *   Cost Estimates (PMO-04.04.02)
*   **Optional / Contextual:**
    *   Product Backlog (PMO-04.02.08)
    *   Quality Metrics (PMO-04.05.02)

---

### 5. How?
To accurately and professionally complete the **PRODUCT BACKLOG**, the responsible party
must populate the following sections based on the project context (ensure
`parameters.md` is referenced for global project variables):

*   **ID:** A unique identifier. Keep it short, stable, and never reused, because the same ID appears in the trace from vision to release and a reassigned ID breaks that trace without anyone noticing.
*   **Summary Description:** A brief description of the requirement or need, in no more than one or two sentences. If it needs a paragraph, the item is probably two items, or it belongs in the vision rather than the backlog.
*   **Priority:** A way of ranking the requirements. Either summary groups such as high, medium, and low, or a numbered rank. State which scheme is in use, because a backlog that mixes the two cannot be sorted.
*   **Story:** A prioritised user story, or the name of a user story recorded elsewhere. Where the story lives elsewhere, reference it rather than copying it, so the two do not diverge.
*   **Status:** Whether the requirement is not started, in progress, or complete. Use the same set of values for every row, since a status column with mixed vocabularies cannot be filtered.
*   **Story Points:** Estimating information such as story points. An estimate is a prediction made to compare against actuals, so record it even when it is a rough guess, and do not revise it silently.
*   **Target Sprint or Release:** Which sprint or release the item will be incorporated into. Treat this as a forecast: an item that keeps moving between releases is telling you something, and the churn is worth seeing.
*   **User Type:** The user type that will benefit, such as customer, administrator, or manager. This is what shows which parts of the organisation the release actually serves.
*   **Category:** A category, which helps on large projects where the backlog is too big to hold in one view. Categories should reflect how the work is actually sequenced, not how the team happens to be divided.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](04_02_08_Product_Backlog_Template.md)
* [🤖 LLM Generation Prompt](04_02_08_Product_Backlog.md)
* [📊 Data Structure (JSON)](04_02_08_Product_Backlog.json)
* [📈 Tabular Data (CSV)](04_02_08_Product_Backlog.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [04_02_08_Product_Backlog_Example.md](../../../../../examples/en/04_Planning/02_Scope/08_Product_Backlog/04_02_08_Product_Backlog_Example.md)

</div>
