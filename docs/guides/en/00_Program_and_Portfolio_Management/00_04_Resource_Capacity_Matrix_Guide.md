<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <a class="lang-switch-btn" href="../../ar/00_إدارة_البرامج_والمحافظ/00_04_مصفوفة_سعة_الموارد_دليل.html">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-00.04</span>
    <span class="badge badge-phase">00. Program & Portfolio Management</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../forms/en/00_Program_and_Portfolio_Management/00_04_Resource_Capacity_Matrix_Template.html">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/00_Program_and_Portfolio_Management/00_04_Resource_Capacity_Matrix_Example.html">💡 Completed Example</a>
    <a class="nav-pill lang-pill" href="../../ar/00_إدارة_البرامج_والمحافظ/00_04_مصفوفة_سعة_الموارد_دليل.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
lang: en
layout: default
title: Resource Capacity Matrix
nav_order: 1
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;" markdown="1">

## Tasleemat Forms Guide
# Project Artifact: Resource Capacity Matrix

**Document Reference:** `PMO-00.04`

This document provides a comprehensive, professional reference to understand the
purpose and effective usage of the **Resource Capacity Matrix** in alignment with
the Tasleemat framework.

---

### 1. What?
A formal Tasleemat-aligned project document known as the **Resource Capacity
Matrix**, showing whether the plan is feasible in terms of the people available
to carry it out.

It records the basis of the matrix and its unit of measure, the capacity that
exists by role and period with what is already allocated elsewhere, the demand
the scope and schedule create with the source and priority of each, the gap
between the two with how each gap will be closed and by whom, and the
contingency the plan holds and what that contingency protects.

---

### 2. Why?
Because demand and supply are gathered from different places and are therefore
never reconciled by accident. Demand comes from the schedule and the scope,
supply comes from the resourcing plan and the organisation's actual shape, and
nobody sets the two against each other until a matrix like this makes the gap
visible. The Gap column is the one the reader is looking for, so a matrix that
records only totals has omitted the only figure that matters.

---

### 3. When?
This artifact is prepared at the **PROGRAM AND PORTFOLIO MANAGEMENT** Process
Group, and re-reconciled whenever the schedule changes materially or the
organisation is restructured. It is a recurring reconciliation rather than a
document produced once, because capacity is reallocated continuously and a
matrix that is not refreshed describes an organisation that no longer exists.

---

### 4. Who?
**Responsibilities:** Owned by the Program Manager and reconciled with the
resource or workforce planning function that holds the supply side. Signed by
the PMO and by the finance business partner, since a gap closed by a contractor
is a cost change and should not be agreed without someone who can see the cost.

---

### Tailoring Tips
*   The matrix may be maintained at portfolio level across all initiatives, or
    at program level across the components, or for a single project. The form
    should say which, because a portfolio matrix is used to decide between
    initiatives and a project matrix is used to decide whether one plan is
    credible.
*   Where the organisation runs a resourcing tool, the matrix may be an extract
    rather than the source of truth. Record that, so a reader does not treat a
    stale extract as current.
*   Add or remove rows as needed. Where a role is filled by more than one
    person, record the role once and note the split in the notes column, since a
    row per person hides the total capacity of the role.
*   The matrix may be maintained by a resourcing or workforce planning function,
    in which case cross-reference it rather than duplicating the supply side.
*   The contingency section may be omitted where the organisation holds
    contingency centrally, but the form should say so explicitly rather than
    leaving a reader to assume the plan holds none.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Portfolio Roadmap (PMO-00.01)
    *   Program Charter (PMO-00.02)
    *   Organizational Staffing Budgets
*   **Optional / Contextual:**
    *   Resource Management Plans (PMO-04.06.01)
    *   Resource Requirements (PMO-04.06.02)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Project Resource Management Plans (PMO-04.06.01)
    *   Project Schedules (PMO-04.03.08)
*   **Optional / Contextual:**
    *   Responsibility Assignment Matrix / RAM (PMO-04.06.04)
    *   Procurement Strategy (PMO-04.09.02)

---

### 5. How?
To accurately and professionally complete the **RESOURCE CAPACITY MATRIX**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Matrix Scope and Level:** What this matrix covers and at what level it is maintained, whether portfolio-wide across initiatives, program-wide across components, or for a single project. The level decides what the matrix is used to decide: a portfolio matrix decides between initiatives, a project matrix decides whether one plan is credible, and reading either as the other produces a confident wrong answer.
*   **Capacity Unit of Measure:** The unit used for every figure in the matrix, whether person-days, full-time equivalents, or hours per period. State it once and use it throughout: a matrix whose rows use different units cannot be added up, and the total at the foot of it is then arithmetically meaningless rather than merely approximate.
*   **Periods Covered:** The periods the matrix covers, matching those of the schedule it is compared against. Where the matrix is annual and the schedule is weekly, the comparison has to be done by hand every time and is therefore not done, which is how a quarterly shortfall survives to become a delivery failure.
*   **Source of Truth or Extract:** Whether this matrix is the authoritative record or an extract from a resourcing tool. Record which, because a reader who treats a stale extract as current will plan against capacity that was reallocated weeks ago, and the error surfaces only when the work cannot be staffed.
*   **Matrix Owner:** The single role accountable for the matrix as a whole, which is normally not the owner of any one resource in it. Where this is blank, the matrix has contributors but nobody who notices that a row has not been updated since the reorganisation.
*   **Last Updated:** The date the matrix was last reconciled against the plan, and against which version of the schedule. Without it a reader cannot tell a current matrix from an abandoned one, and the two are indistinguishable on the page.
*   **ID:** The identifier for the resource role, used in the demand and gap sections so the three can be compared row against row. Without a shared identifier the comparison is done by eye, and two similarly named roles are the ones most often confused.
*   **Resource Role or Team:** The role or team, named as the work requires it rather than as the organisation chart draws it. A matrix organised by existing departments can never show a gap, because it only ever lists what is already there, and the absence of a needed capability reads as its absence from the plan rather than from the organisation.
*   **Period:** The period the row covers, using the same periods throughout the matrix. Capacity recorded per period rather than in total is what makes the matrix usable, because a resource with a thousand person-days available who is fully committed in the month the work is needed has no capacity at all.
*   **Total Available:** The capacity that exists in the period, before any allocation, in the unit declared for the matrix. This is a figure about the organisation rather than about the project, and recording it here is what allows the reader to see how much of it is actually available.
*   **Allocated:** The capacity already committed elsewhere in the portfolio. This is the column most often left out, and without it the available figure is the total, which is not what the project can use. It is also the column that reveals a resource being shared between initiatives without either owner knowing.
*   **Remaining:** What is left after allocation, which is the figure the planner actually has. Where this is negative, the matrix has found a real problem; where it is silently recorded as zero because nobody wanted to write a negative number, the problem has been hidden instead of solved.
*   **Constraints or Single Points of Failure:** What limits this resource: a location, a qualification held by one person, a licence, a tool only one person can operate, or a notice period. Record the consequence rather than the adjective, because "test automation is a single point of failure because one person holds it" can be acted on, while "test automation is a risk" cannot.
*   **Notes:** Anything that changes how the row should be read, such as a known vacancy, planned leave, or a resource shared with another portfolio. Where a role is filled by more than one person, record the role once and note the split here, since a row per person hides the total capacity of the role.
*   **ID:** The resource role the demand is for, matching the ID used in the capacity section so the two can be set against each other.
*   **Resource Role:** The role the demand falls on, using the same naming as the capacity section. The two must be the same list, or the comparison in the gap section silently excludes roles that appear in only one of them, which are usually the ones in trouble.
*   **Period:** The period the demand falls in. A demand recorded with no period cannot be compared with a capacity figure that has one, and is therefore dropped from the comparison without anyone deciding to drop it.
*   **Required Capacity:** What the scope and schedule require in the period. Record the figure the plan was built on rather than the figure currently being achieved, since the second is a consequence of the first being wrong and reporting it back as the requirement makes the shortfall disappear from the plan.
*   **Source of Demand:** Which part of the plan generates it, such as a named deliverable, work package, or activity. A demand that cannot be traced to something in the plan cannot be challenged, and demands that cannot be challenged only ever grow.
*   **Priority:** Whether the demand is essential, or could be deferred or descoped. Without a priority a gap has no remedy, because the available responses are to add capacity, move the work, or reduce it, and nothing in the matrix says which of those the programme would accept.
*   **Resource Role:** The role the gap applies to, using the same naming as the sections above. Where a role appears in the demand but not the capacity, the gap is the whole requirement rather than a shortfall, and that case is worth distinguishing because it is a different problem.
*   **Gap:** The difference between required and remaining, stated as a signed number so that a surplus is not read as a shortfall. This is the figure the whole matrix exists to produce, and a matrix that records only the totals has omitted the only number anyone reads.
*   **Period:** The period the gap falls in. A gap in a period with no demand in it is a different problem from a gap in a period the work needs, and reporting both as "a gap" sends the reader looking for the wrong remedy.
*   **Resolution Planned:** How the gap will be closed: recruitment, a contractor, moving work between periods, reducing scope, or accepting the risk. Where the gap is covered by a contractor or a shared resource, record the contract or agreement that covers it, because a gap filled on the understanding that someone will help is not covered at all.
*   **Resolution Owner:** Who is accountable for closing the gap. A gap with a planned resolution and no owner is a gap being wished away, and it is the most common way a capacity matrix comes to be relied upon long after it was last true.
*   **Resolution Date:** By when the resolution is expected to be in place. This is what tells the reader whether the plan is still feasible, so record it rather than leaving the row open, and where the date has passed without resolution, escalate rather than moving the date.
*   **Resource Role:** The role the contingency applies to, or "plan" where the buffer is held across all roles rather than against one.
*   **Contingency Type:** Whether the buffer is in capacity, in time, or in scope. The three are not interchangeable: time contingency can be spent once, capacity contingency can be spent on anything, and scope contingency reduces the deliverable. A plan that holds no scope contingency and states only that it has float is a plan whose contingency is the work being cut.
*   **Contingency Amount:** The size of the buffer, in the declared unit. Record it as a figure rather than a percentage, because a percentage of a demand that was never reconciled produces a number that looks precise and is not.
*   **How It Would Be Used:** What the buffer protects, recorded so it cannot be quietly consumed on something it was not held for. A contingency with no stated use is the first thing cut in a difficult month, which is precisely the month it was held for.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](../../../forms/en/00_Program_and_Portfolio_Management/00_04_Resource_Capacity_Matrix_Template.md)
* **🤖 LLM Generation Prompt**
* **📊 Data Structure (JSON)**
* **📈 Tabular Data (CSV)**

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [00_04_Resource_Capacity_Matrix_Example.md](../../../examples/en/00_Program_and_Portfolio_Management/00_04_Resource_Capacity_Matrix_Example.md)

</div>
