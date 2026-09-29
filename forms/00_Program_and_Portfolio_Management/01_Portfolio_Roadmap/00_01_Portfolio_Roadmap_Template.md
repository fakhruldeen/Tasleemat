<!--  
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

A portfolio roadmap is a time-phased, visual representation of the programs,
projects, and operations in a portfolio, showing their sequence, expected
outcomes, and the dependencies between them. Its purpose is to communicate
strategy and to let decision-makers see the consequence of a change before the
change is made, rather than discovering it a quarter later when funding has
already been committed.

The intent behind carrying dependencies, funding, and capacity as separate
sections is that a roadmap listing only initiatives and dates is a calendar, not
a plan. It looks complete while telling the reader nothing about what will
happen if one initiative runs late.

Alignment: the portfolio roadmap should be aligned and consistent with the
following documents: Program charter, Business case, Portfolio management plan,
Resource capacity matrix.

Writing guidance:

*   Give every initiative a stable identifier. A roadmap reviewed over several
    cycles is unreadable if an initiative is referred to by a different name
    each time it appears, and the reader cannot tell whether two rows are the
    same initiative or two of them.

*   Write dates at the precision the decision actually needs. An annual
    portfolio may legitimately be planned by quarter; a release with a fixed
    commercial date may not. Mixed precision in one table is the thing to
    avoid, because the reader compares the rows against each other.

*   Record the status as a value from a fixed set such as Proposed, Funded,
    In Progress, On Hold, or Complete. A free-text status cannot be sorted or
    filtered, and a roadmap that cannot be filtered is a picture.

*   Record funding as a planned envelope rather than a spend forecast. The
    roadmap answers whether the money is available in the period, not whether it
    is being spent, and the two are routinely confused.

*   Where an initiative is dependent on another, name the predecessor in the
    dependency section rather than in a free-text note. A dependency recorded
    only in prose is a dependency nobody can query.

Tailoring Notes:

*   A programme-level portfolio roadmap may aggregate to programmes only, and
    the initiative rows may be several levels down where a division plans its
    own portfolio.

*   The roadmap may be presented graphically rather than as a table. The
    sections below carry the same content in either form, and the form should
    say which presentation is expected.

*   Add or remove rows as needed. If an initiative carries more detail than the
    roadmap can hold, link to its charter or business case rather than
    compressing it here.

*   Where the organisation runs a fixed planning cycle, record the cycle in the
    context section and reuse it, so that successive roadmaps are comparable.

Column guidance, by column:

Initiative rows:

*   **ID:** The stable identifier for the initiative, used by every later cycle
    of this roadmap and by the dependency and funding sections.

*   **Initiative Name:** The name of the program, project, or operation. Use the
    name from its charter so the same initiative is not tracked under two.

*   **Type:** Whether the row is a Program, Project, or Operation. The type
    determines what governance applies, so an initiative recorded without one
    has no defined approval path.

*   **Strategic Objective:** The specific objective this initiative serves, named
    from the strategy rather than from the initiative's own charter. An
    initiative that maps to no objective is a candidate for removal, and the
    roadmap is where that is visible.

*   **Start:** When the initiative is expected to start.

*   **End:** When the initiative is expected to deliver its outcomes, which is
    not the same as when its budget is spent.

*   **Budget:** The funding envelope allocated to the initiative for the
    planning period.

*   **Status:** Where the initiative currently stands against the fixed set
    used in this roadmap.

Dependency rows:

*   **ID:** The identifier of the initiative whose dependency is being recorded.

*   **Dependent Initiative:** The initiative that cannot proceed without the
    predecessor.

*   **Dependency Type:** Whether the dependency is Finish to Start, Start to
    Start, Finish to Finish, or Start to Finish. The type determines the amount
    of float the successor has, so an untyped dependency cannot be planned.

*   **Predecessor:** The initiative on which this one depends.

*   **Required By:** The date by which the dependency must be satisfied for the
    dependent initiative to hold its own date.

*   **Impact if Late:** What happens to the dependent initiative if the
    predecessor does not deliver in time.

Funding and capacity rows:

*   **Period:** The planning period the row covers.

*   **Planned Funding:** The money available in the period across the portfolio.

*   **Planned Capacity:** The resource capacity available in the period, in the
    unit the organisation uses.

*   **Committed Load:** The capacity already committed to initiatives in the
    period.

*   **Available:** The difference between planned and committed, which is the
    figure that tells the reader whether the plan is feasible.

*   **Notes:** Anything that changes the interpretation of the row, such as a
    known shortage or a hiring assumption the row depends on.

Assumption and constraint rows:

*   **ID:** The identifier for the assumption or constraint.

*   **Type:** Whether the row is an Assumption or a Constraint.

*   **Description:** What is being assumed or constrained.

*   **Impact on Roadmap:** The effect on the roadmap if this proves false or
    proves tighter than stated.

*   **Owner:** Who is responsible for confirming or managing it.

*   **Review Date:** When it will next be checked, because an assumption nobody
    revisits is indistinguishable from a fact.

Roadmap change rows:

*   **Change ID:** The identifier for the change.

*   **Description:** What changed in the roadmap.

*   **Reason:** Why it changed, which is what the next reader needs in order to
    judge whether the same reasoning applies again.

*   **Affected Initiatives:** The initiatives the change touches.

*   **Approved By:** Who authorised the change.

*   **Date:** When the change was approved, which fixes the version of the
    roadmap in which it took effect.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 dir="ltr" align="center">PORTFOLIO ROADMAP</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |  

---

## 1. Portfolio Context and Planning Basis
<!-- What this portfolio covers, over what period, and how often the roadmap is
 refreshed. Record the planning cycle here rather than in a note, because
 successive roadmaps are only comparable if they were built on the same basis.
 Record the roadmap status as a version statement: which planning cycle this
 represents and which meeting approved it. Without that, two roadmaps differing
 by a few initiatives cannot be read as a change of direction rather than as two
 views of the same portfolio. -->

**Portfolio Purpose and Scope:** [ Add details... ]

**Planning Period:** [ Add details... ]

**Roadmap Horizon:** [ Add details... ]

**Portfolio Owner:** [ Add details... ]

**Planning Cycle:** [ Add details... ]

**Roadmap Version and Status:** [ Add details... ]

---

## 2. Roadmap Initiatives
<!-- One row per program, project, or operation, ordered by start date. Use the
 names from each initiative's charter so the same initiative is not tracked
 under two names across cycles. Record the status from the fixed set agreed for
 this roadmap, because a free-text status cannot be filtered, and a roadmap that
 cannot be filtered is a picture rather than a plan. Where an initiative serves
 no strategic objective, leave that cell saying so explicitly rather than
 leaving it blank, since the blank is indistinguishable from an oversight. Add
 or remove rows as needed. -->

| ID | Initiative Name | Type | Strategic Objective | Start | End | Budget | Status |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 3. Dependencies and Sequencing
<!-- Where one initiative cannot proceed until another delivers, record it here
 with a typed dependency rather than in a free-text note, because a dependency
 recorded only in prose is a dependency nobody can query. Finish to Start is
 the common case; Start to Start and Finish to Finish arise where two
 initiatives must move together. State the impact of a late predecessor in
 money, schedule, or both, since a dependency with no stated impact is not
 actionable when the predecessor slips. -->

| ID | Dependent Initiative | Dependency Type | Predecessor | Required By | Impact if Late |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. Funding and Capacity by Period
<!-- Whether the plan is feasible, not merely what is planned. The Available
 column is the one that matters: it is planned funding or capacity less what is
 already committed, and a roadmap where that figure is negative in some period
 is a roadmap that will be broken in that period. Record assumptions the row
 depends on, such as a hiring date or a funding decision that has not yet been
 taken, because a capacity row without them reads as a commitment. Add or remove
 rows as needed. -->

| Period | Planned Funding | Planned Capacity | Committed Load | Available | Notes |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 5. Assumptions and Constraints
<!-- What the roadmap takes for granted, and what limits it. An assumption
 without an owner and a review date is indistinguishable from a fact, and the
 roadmap then carries it forward indefinitely after the conditions that made it
 true have gone. Record constraints with the same seriousness, since a
 constraint recorded without its impact cannot be traded off against anything.
 Add or remove rows as needed. -->

| ID | Type | Description | Impact on Roadmap | Owner | Review Date |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 6. Roadmap Changes
<!-- What changed between this version of the roadmap and the last, and why. A
 reader comparing two roadmaps needs the reason as much as the change, because
 the reason is what tells them whether the same reasoning applies to the next
 change. Record the approver, since a roadmap altered without one is a roadmap
 nobody owns. Add or remove rows as needed. -->

| Change ID | Description | Reason | Affected Initiatives | Approved By | Date |
| ---: | ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 7. Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Portfolio Manager** | {{Portfolio_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **PMO Lead** | {{PMO_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **Program Sponsor** | {{Program_Sponsor_Name}} | _______________________ | [ .... - .... - .... ] |
| **Finance Business Partner** | {{Finance_Business_Partner_Name}} | _______________________ | [ .... - .... - .... ] |

---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> Portfolio Roadmap | <strong>Ref:</strong> PMO-00.01 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
