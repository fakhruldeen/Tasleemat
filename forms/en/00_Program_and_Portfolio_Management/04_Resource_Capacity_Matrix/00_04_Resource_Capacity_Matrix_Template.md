---
type: Form
---

<!--  
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

The resource capacity matrix shows whether the plan is feasible in terms of the
people available to carry it out. It compares what the programme or project
needs against what exists, and the difference is the thing worth reading: a
plan that requires more capacity than is available is not a plan that needs
more effort, it is a plan that cannot be executed as written.

The intent behind separating demand from supply is that they are gathered from
different places and are therefore rarely reconciled by accident. Demand comes
from the schedule and the scope, supply comes from the resourcing plan and the
organisation's actual shape, and nobody reconciles the two until a matrix like
this makes the gap visible. The Gap column is therefore the one the reader
cares about, and a matrix that records only the totals has omitted the only
figure that matters.

Alignment: the resource capacity matrix should be aligned and consistent with
the following documents: Portfolio roadmap, Program charter, Project management
plan, Resource breakdown structure, Procurement plan.

Writing guidance:

*   State the unit of capacity once and use it throughout, whether that is
    person-days, full-time equivalents, or hours per period. A matrix whose
    rows use different units cannot be added up, and the total at the bottom
    is then arithmetically meaningless rather than merely approximate.

*   Record capacity per period, not in total. A resource with a thousand
    person-days available who is fully committed in the month the work is
    needed has no capacity at all, and a total figure hides exactly that.

*   Record the demand from the plan, not from what the team currently is. The
    demand column is what the schedule and scope require; the supply column is
    what exists. Recording the same number in both columns is the single most
    common way a capacity matrix comes to be wrong, because it makes the
    matrix agree with the plan rather than with reality.

*   Record named constraints as consequences, not as adjectives. "Test
    automation is a single point of failure because one person holds it" is
    actionable; "test automation is a risk" is not.

*   Where a gap is covered by a contractor or a shared resource, record the
    contract or agreement that covers it. A gap filled on the understanding
    that someone will help is not covered, and the difference shows up the week
    the help is needed elsewhere.

Tailoring Notes:

*   The matrix may be maintained at portfolio level across all initiatives, or
    at program level across the components, or for a single project. The form
    should say which, because a portfolio matrix is used to decide between
    initiatives and a project matrix is used to decide whether one plan is
    credible.

*   Where the organisation runs a resourcing tool, the matrix may be an
    extract rather than the source of truth. Record that, so a reader does not
    treat a stale extract as current.

*   Add or remove rows as needed. Where a role is filled by more than one
    person, record the role once and note the split in the notes column, since
    a row per person hides the total capacity of the role.

*   The matrix may be maintained by a resourcing or workforce planning
    function, in which case cross-reference it rather than duplicating the
    supply side.

Column guidance, by column:

Capacity by resource:

*   **ID:** The identifier for the resource role, used in the demand and the
    gap sections so the two can be compared row against row.

*   **Resource Role or Team:** The role or team, named as the work requires it
    rather than as the organisation chart draws it. A matrix organised by
    existing departments cannot show a gap, because it only ever lists what is
    already there.

*   **Period:** The period the row covers, using the same periods throughout
    the matrix and matching those of the schedule it is compared against.

*   **Total Available:** The capacity that exists in the period, before any
    allocation, stated in the unit declared for the matrix.

*   **Allocated:** The capacity already committed elsewhere in the portfolio.
    This is the column most often left out, and without it the available
    figure is the total, which is not what the project can use.

*   **Remaining:** What is left after allocation, which is the figure the
    planner actually has.

*   **Constraints or Single Points of Failure:** What limits this resource, such
    as a location, a qualification held by one person, a licence, or a tool
    only one person can operate. Record the consequence rather than the
    adjective.

*   **Notes:** Anything that changes how the row should be read, such as a
    known vacancy, a planned leave, or a commitment shared with another
    portfolio.

Demand rows:

*   **ID:** The resource role the demand is for, matching the ID used above.

*   **Required Capacity:** What the scope and schedule require in the period.
    Record the figure the plan was built on rather than the figure currently
    being achieved, since the second is a consequence of the first being wrong.

*   **Source of Demand:** Which part of the plan generates it, such as a
    specific deliverable or work package. A demand that cannot be traced to
    something in the plan cannot be challenged, and demands that cannot be
    challenged only ever grow.

*   **Period:** The period the demand falls in.

*   **Priority:** Whether the demand is essential, or could be deferred or
    descoped. Without a priority a gap has no remedy, because the only
    available responses are to add capacity, move the work, or reduce it, and
    the matrix does not say which is acceptable.

Gap analysis rows:

*   **Resource Role:** The role the gap applies to.

*   **Gap:** The difference between required and remaining, stated as a number
    and signed so a surplus is not read as a shortfall.

*   **Period:** The period the gap falls in.

*   **Resolution Planned:** How the gap will be closed, whether by recruitment,
    by a contractor, by moving work between periods, or by reducing scope.

*   **Resolution Owner:** Who is accountable for closing it. A gap with a
    planned resolution and no owner is a gap that is being wished away, and it
    is the most common way a capacity matrix comes to be relied upon.

*   **Resolution Date:** By when the resolution is expected to be in place,
    which is what tells the reader whether the plan is still feasible.

Contingency rows:

*   **Resource Role:** The role the contingency applies to.

*   **Contingency Type:** Whether the buffer is in capacity, in time, or in
    scope. The three are not interchangeable: time contingency can be spent
    once, capacity contingency can be spent on anything, and scope
    contingency reduces the deliverable.

*   **Contingency Amount:** The size of the buffer, in the declared unit.

*   **How It Would Be Used:** What it protects, so that a buffer cannot be
    quietly consumed on something it was not held for.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Organization_Unit}} - {{Planning_Period}}</h2>
<h1 dir="ltr" align="center">RESOURCE CAPACITY MATRIX</h1>

| **Date Prepared:** {{Current_Date}} | **Program Manager:** {{Program_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |  

---

## 1. Matrix Basis
<!-- What this matrix covers, in what unit, and over which periods. Record the
 unit once and use it throughout: a matrix whose rows use different units
 cannot be added up, and a total is then arithmetically meaningless rather than
 merely approximate. Record the level the matrix is maintained at, because a
 portfolio matrix is used to decide between initiatives while a project matrix
 is used to decide whether a single plan is credible. And record whether this
 is the source of truth or an extract from a resourcing tool, so a reader does
 not treat a stale extract as current. -->

**Matrix Scope and Level:** [ Add details... ]

**Capacity Unit of Measure:** [ Add details... ]

**Periods Covered:** [ Add details... ]

**Source of Truth or Extract:** [ Add details... ]

**Matrix Owner:** [ Add details... ]

**Last Updated:** [ Add details... ]

---

## 2. Capacity by Resource
<!-- What exists, in what unit, in which period. The Allocated column is the one
 most often left out, and without it the available figure is the total, which
 is not what the project can use. Record capacity per period rather than in
 total: a resource with a thousand person-days available who is fully
 committed in the month the work is needed has no capacity at all, and a total
 figure hides exactly that. Record constraints as consequences, not as
 adjectives; "test automation is a single point of failure because one person
 holds it" can be acted on, and "test automation is a risk" cannot. Where a
 role is filled by more than one person, record the role once and note the
 split, since a row per person hides the total capacity of the role. Add or
 remove rows as needed. -->

| ID | Resource Role or Team | Period | Total Available | Allocated | Remaining | Constraints or Single Points of Failure | Notes |
| :---: | :--- | :---: | ---: | ---: | ---: | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 3. Demand by Resource
<!-- What the plan requires, which is a different number from what is
 currently being achieved. Record the figure the plan was built on rather than
 the figure being achieved, since the second is a consequence of the first
 being wrong. Record the source of the demand so it can be traced to a
 deliverable or a work package; a demand that cannot be traced to something in
 the plan cannot be challenged, and demands that cannot be challenged only ever
 grow. Record a priority, because without one a gap has no remedy, since the
 available responses are to add capacity, move the work, or reduce it, and
 nothing in the matrix says which is acceptable here. Add or remove rows as
 needed. -->

| ID | Resource Role | Period | Required Capacity | Source of Demand | Priority |
| :---: | :--- | :---: | ---: | :--- | :---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. Gap Analysis
<!-- The difference between what is required and what is remaining, which is
 the only figure in the matrix the reader is looking for. State it as a signed
 number so a surplus is not read as a shortfall. Record a planned resolution
 and, separately, an owner for it: a gap with a resolution and no owner is a
 gap being wished away, and it is the most common way a capacity matrix comes
 to be relied upon after it has already been superseded. The resolution date is
 what tells the reader whether the plan is still feasible, so record it rather
 than leaving the row open. Add or remove rows as needed. -->

| Resource Role | Gap | Period | Resolution Planned | Resolution Owner | Resolution Date |
| :--- | ---: | :---: | :--- | :--- | :---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 5. Contingency
<!-- What the plan holds in reserve, and what that reserve protects. The three
 kinds of contingency are not interchangeable: time contingency can be spent
 once, capacity contingency can be spent on anything, and scope contingency
 reduces the deliverable. Record which kind each buffer is, because a plan that
 holds no scope contingency and states only that it has float is a plan whose
 contingency is the work being cut. Record what each buffer protects so that it
 cannot be quietly consumed on something it was not held for. Add or remove
 rows as needed. -->

| Resource Role | Contingency Type | Contingency Amount | How It Would Be Used |
| :--- | :--- | ---: | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 6. Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Resource Planning Lead** | {{Resource_Planning_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **Program Manager** | {{Program_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **PMO Director** | {{PMO_Director_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> Resource Capacity Matrix | <strong>Ref:</strong> PMO-00.04 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
