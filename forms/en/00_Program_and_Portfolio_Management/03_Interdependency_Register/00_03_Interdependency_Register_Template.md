<!--  
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

The interdependency register records the relationships between the components
of a program, portfolio, or project, in the specific sense that one cannot
proceed, or cannot proceed on its own dates, until another delivers
something. It is a forward-looking record: it is what tells the reader what
will have to be true before the plan works.

The intent behind separating internal dependencies from external ones is that
they behave differently and are governed by different people. An internal
dependency can usually be renegotiated by asking; an external one often
cannot, and a register that mixes them invites the reader to treat an external
commitment as though it were a request to a colleague.

Alignment: the interdependency register should be aligned and consistent with
the following documents: Portfolio roadmap, Program charter, Project management
plan, Schedule management plan.

Writing guidance:

*   Name the specific deliverable or condition being waited on, not the other
    project. "Waiting for Project B" cannot be actioned when Project B is
    delayed, because nobody knows what to chase; "waiting for the signed data
    migration specification from Project B" can.

*   Record the date the dependency must be satisfied by, which is the
    successor's requirement, rather than the date the predecessor expects to
    deliver. Where the two differ, the gap between them is the risk, and it
    belongs in the register rather than in somebody's memory.

*   Record the dependency type. Finish to Start is the common case, and it is
    the only one that needs no explanation; the other types arise where two
    projects must move together, and without the type a reader cannot tell a
    hard sequencing constraint from a preference.

*   Record who agreed the dependency, and when. A dependency that was assumed
    rather than agreed is the one that will be disputed at the moment it
    becomes inconvenient.

*   Record the status as a value from a fixed set. A free-text status cannot be
    filtered, and a register of forty dependencies that cannot be filtered is
    a document nobody reads when they need to answer a question about one of
    them.

Tailoring Notes:

*   The register may be maintained at portfolio level, covering all
    interdependencies between initiatives, or at program level covering only
    those between components. The form should say which, because the two
    answer different questions.

*   Where the organisation runs a dependency log in a planning tool, the
    register may be an extract rather than the source of truth. If so, record
    that, so a reader does not treat the extract as authoritative.

*   Add or remove rows as needed. Where two projects have a reciprocal
    dependency, record both directions rather than one row with both names, so
    each direction can be tracked and agreed separately.

*   The external dependency section may be maintained separately by a
    procurement or vendor governance function, in which case cross-reference
    it rather than duplicating it.

Column guidance, by column:

Internal dependency rows:

*   **ID:** The identifier for the dependency, used in the change log and in
    reporting so a threatened dependency can be referred to unambiguously.

*   **Predecessor:** The project or component that must deliver first, named
    and identified so the row can be joined to the portfolio roadmap.

*   **Successor:** The project or component that is waiting. Where the same
    predecessor is needed by several successors, record a row for each, because
    the required dates and the impacts differ.

*   **Deliverable or Condition:** What specifically is being waited on, stated
    so that it can be confirmed as delivered or not. A dependency stated as a
    general state of readiness cannot be closed, because no one can say when
    it has been reached.

*   **Dependency Type:** Whether the relationship is Finish to Start, Start to
    Start, Finish to Finish, or Start to Finish.

*   **Required By:** The date by which the successor needs the deliverable.
    This is the successor's requirement, and recording the predecessor's
    forecast here instead hides the gap between the two.

*   **Agreed Date:** The date the predecessor has committed to, so the gap
    against the required date is visible in the register itself.

*   **Status:** Where the dependency currently stands against the fixed set
    used in this register.

*   **Impact if Late:** What happens to the successor if the predecessor misses
    the required date, in schedule, cost, or scope terms. A dependency with no
    stated impact cannot be escalated, because nobody can say what is at risk.

External dependency rows:

*   **ID:** The identifier for the external dependency.

*   **External Party:** The organisation outside the program the dependency
    runs through, named with the role it plays rather than the individual, so
    the row survives a change of contact.

*   **Dependency Description:** What the external party is expected to provide
    or approve, and by when.

*   **Contractual Basis:** Whether the dependency is covered by a contract, a
    memorandum of understanding, or nothing in writing. This is the column
    that decides whether the dependency can be enforced, and a register that
    omits it cannot tell a reader which rows are at risk.

*   **Required By:** The date the program needs it.

*   **Status:** Where the dependency stands against the fixed set.

*   **Owner:** Who is accountable for the relationship with the external party,
    which is normally not the person who needs the deliverable.

Escalation rows:

*   **Dependency ID:** The dependency the escalation concerns, so it can be
    joined back to the register.

*   **Trigger:** What caused the escalation, whether a missed date, a stated
    refusal, or a change on the predecessor's side.

*   **Escalated To:** Who it was escalated to, named rather than described.

*   **Action Agreed:** What was decided, which is what stops the same question
    being escalated again next cycle with no progress.

*   **Date:** When the escalation happened, and when it will next be reviewed.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 dir="ltr" align="center">INTERDEPENDENCY REGISTER</h1>

| **Date Prepared:** {{Current_Date}} | **Program Manager:** {{Program_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |  

---

## 1. Register Basis
<!-- What this register covers and how current it is meant to be. Record the
 level at which it is maintained, because a portfolio-level register and a
 program-level one answer different questions and are compared against
 different plans. Record the review cycle, because a register nobody refreshes
 is a register that describes a portfolio as it once was. And record whether
 this is the source of truth or an extract from a planning tool, so a reader
 does not treat an extract as authoritative and act on a stale date. -->

**Register Scope and Level:** [ Add details... ]

**Programs or Projects Covered:** [ Add details... ]

**Source of Truth or Extract:** [ Add details... ]

**Review Cycle:** [ Add details... ]

**Register Owner:** [ Add details... ]

**Last Updated:** [ Add details... ]

---

## 2. Internal Interdependencies
<!-- Between projects and components the program controls. Name the specific
 deliverable or condition being waited on, not the other project: "waiting for
 Project B" cannot be chased when Project B slips, because nobody knows what to
 ask for, whereas "waiting for the signed data migration specification from
 Project B" can. Record the required date, which is the successor's
 requirement, alongside the agreed date, so the gap between what is needed and
 what has been promised is visible in the register rather than discovered
 later. Where the same predecessor serves several successors, record a row for
 each, because the required dates and the impacts differ. Add or remove rows as
 needed. -->

| ID | Predecessor | Successor | Deliverable or Condition | Dependency Type | Required By | Agreed Date | Status | Impact if Late |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 3. External Interdependencies
<!-- On organisations outside the program, which behave differently and are
 governed by different people. The column that matters most here is
 Contractual Basis, because it decides whether the dependency can be enforced:
 a commitment taken in correspondence and a commitment written into a contract
 look identical in every other column and are not remotely the same. Name the
 external party by role rather than by individual, so the row survives a change
 of contact, and record who is accountable for the relationship separately from
 the person who needs the deliverable. Add or remove rows as needed. -->

| ID | External Party | Dependency Description | Contractual Basis | Required By | Status | Owner |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. Escalations and Agreements
<!-- What has been done about the dependencies that are not holding. Record the
 trigger, so a reader can tell an escalation caused by a missed date from one
 caused by a refusal, because the remedy differs. Record what was agreed,
 since an escalation that concludes nothing is repeated the following cycle
 with the same result. Add or remove rows as needed. -->

| Dependency ID | Trigger | Escalated To | Action Agreed | Date |
| ---: | ---: | ---: | ---: | ---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 5. Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Program / Portfolio Manager** | {{Program_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **Delivery / Component Lead** | {{Delivery_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **PMO Lead** | {{PMO_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> Interdependency Register | <strong>Ref:</strong> PMO-00.03 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
