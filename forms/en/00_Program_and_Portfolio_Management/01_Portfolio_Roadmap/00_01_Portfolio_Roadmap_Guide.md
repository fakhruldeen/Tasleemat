---
lang: en
layout: default
title: Portfolio Roadmap
nav_order: 1
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: Portfolio Roadmap

**Document Reference:** `PMO-00.01`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Portfolio Roadmap** in alignment with
the Tasleemat framework.

---

### 1. What?
A formal Tasleemat-aligned project document known as the **Portfolio Roadmap**, a
time-phased, visual representation of the programs, projects, and operations in
a portfolio, showing their sequence, expected outcomes, and the dependencies
between them.

It records the basis on which the portfolio is planned, the initiatives
themselves with their type, strategic objective, dates, budget and status, the
dependencies between them, whether the funding and capacity behind the plan is
actually available, the assumptions and constraints the plan rests on, and what
changed between this version of the roadmap and the last.

---

### 2. Why?
Because a roadmap listing only initiatives and dates is a calendar rather than a
plan. It looks complete while telling the reader nothing about what will happen
if one initiative runs late, and the funding and capacity section is where that
becomes visible. Without a version and a change log, two roadmaps differing by a
few initiatives cannot be read as a change of direction rather than as two views
of the same portfolio.

---

### 3. When?
This artifact is prepared at the **PROGRAM AND PORTFOLIO MANAGEMENT** Process
Group, and refreshed on the planning cycle recorded in the context section,
typically at the start of each financial period or ahead of each investment
review.

---

### 4. Who?
**Responsibilities:** Owned by the Portfolio Manager and prepared with the
portfolio's initiative owners. Approved by the governance forum that holds the
funding, typically the investment board, and signed by the sponsor and the
finance business partner who can confirm the funding rows are real.

---

### Tailoring Tips
*   A programme-level portfolio roadmap may aggregate to programmes only, and the
    initiative rows may be several levels down where a division plans its own
    portfolio.
*   The roadmap may be presented graphically rather than as a table. The
    sections below carry the same content in either form, and the form should
    say which presentation is expected.
*   Add or remove rows as needed. If an initiative carries more detail than the
    roadmap can hold, link to its charter or business case rather than
    compressing it here.
*   Where the organisation runs a fixed planning cycle, record the cycle in the
    context section and reuse it, so that successive roadmaps are comparable.
*   The funding section may be omitted where the roadmap is purely
    sequencing-focused, but the form should say so explicitly rather than
    leaving the reader to assume funding was considered.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Enterprise Strategic Plan
    *   Portfolio Capital Budget & Allocations
*   **Optional / Contextual:**
    *   Program Charters (PMO-00.02)
    *   Interdependency Register (PMO-00.03)
    *   Resource Capacity Matrix (PMO-00.04)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Program Charters (PMO-00.02)
    *   Project Charters (PMO-03.01)
    *   Portfolio Capacity Allocations
*   **Optional / Contextual:**
    *   Business Cases (PMO-01.01)
    *   AI Readiness Assessment (PMO-02.03)

---

### 5. How?
To accurately and professionally complete the **PORTFOLIO ROADMAP**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Portfolio Purpose and Scope:** What this portfolio covers and what it deliberately excludes, in the terms the strategy uses. A roadmap that does not state its boundaries cannot be read against a strategy that is wider than the portfolio, and the gap is mistaken for missing initiatives.
*   **Planning Period:** The period the roadmap plans for, and whether it is a financial year, a rolling three years, or a fixed cycle agreed elsewhere. Successive roadmaps are only comparable if this is the same each time.
*   **Roadmap Horizon:** How far ahead the roadmap looks. Record the horizon even where it equals the planning period, because the two are frequently confused and the confusion shows up later as a gap between what was planned and what was expected.
*   **Portfolio Owner:** The single role accountable for the portfolio as a whole, which is usually not the owner of any one initiative in it. Where this is left blank, the roadmap has an author but no owner, and reprioritisation becomes nobody's decision.
*   **Planning Cycle:** How often the roadmap is refreshed and by what governance forum, such as a quarterly investment board. The cycle is what makes two versions of the roadmap comparable, and a roadmap refreshed on no cycle is a document nobody can diff.
*   **Roadmap Version and Status:** Which planning cycle this represents, its version number, and whether it is draft or approved. Without a version, two roadmaps differing by a few initiatives cannot be read as a change of direction rather than as two views of the same portfolio.
*   **ID:** The stable identifier for the initiative, used by every later cycle of this roadmap and by the dependency and funding sections. A roadmap reviewed across several cycles is unreadable if an initiative is named differently each time, because the reader cannot tell whether two rows are one initiative or two.
*   **Initiative Name:** The name of the program, project, or operation, taken from its charter so the same initiative is not tracked under two names. Where a name has changed, record the former name rather than replacing it, or the history becomes impossible to follow.
*   **Type:** Whether the row is a Program, Project, or Operation. The type determines what governance applies, so an initiative recorded without one has no defined approval path, and the roadmap cannot answer what kind of decision is needed about it.
*   **Strategic Objective:** The specific objective this initiative serves, named from the strategy rather than from the initiative's own charter. An initiative that maps to no objective is a candidate for removal, and the roadmap is the only place that becomes visible; where the mapping is genuinely absent, say so in the cell rather than leaving it blank.
*   **Start:** When the initiative is expected to start, at the precision this table uses throughout. Mixed precision within one table is the thing to avoid, because the reader compares the rows against each other and a month beside a quarter invites a wrong conclusion.
*   **End:** When the initiative is expected to deliver its outcomes, which is not the same as when its budget is spent. An initiative that delivers early and closes its accounts later is normal, and recording the accounts date as the end date moves every dependent initiative on the roadmap.
*   **Budget:** The funding envelope allocated to the initiative for the planning period, not a spend forecast. The roadmap answers whether the money is available in the period, not whether it is being spent, and the two are routinely confused when the figure is taken from a finance system.
*   **Status:** Where the initiative currently stands against the fixed set agreed for this roadmap, such as Proposed, Funded, In Progress, On Hold, or Complete. A free-text status cannot be sorted or filtered, and a roadmap that cannot be filtered is a picture rather than a plan.
*   **ID:** The identifier of the initiative whose dependency is being recorded, matching the ID used in the initiatives section so the row can be joined to it.
*   **Dependent Initiative:** The initiative that cannot proceed, or cannot proceed on its own dates, without the predecessor. Name it rather than describing it, because a dependency stated in terms of a category rather than a named initiative cannot be actioned when it is threatened.
*   **Dependency Type:** Whether the dependency is Finish to Start, Start to Start, Finish to Finish, or Start to Finish. The type determines how much float the successor has, so an untyped dependency cannot be planned; Finish to Start is the common case and the others arise where two initiatives must move together.
*   **Predecessor:** The initiative on which this one depends, named and identified. A dependency recorded only in prose is a dependency nobody can query, and it is therefore a dependency that will not be checked before the predecessor slips.
*   **Required By:** The date by which the dependency must be satisfied for the dependent initiative to hold its own dates. Where the required date is later than the predecessor's planned finish, the gap is the risk and should be visible here rather than discovered later.
*   **Impact if Late:** What happens to the dependent initiative if the predecessor does not deliver in time, in money, schedule, or scope terms. A dependency with no stated impact is not actionable when the predecessor slips, because nobody knows whether to escalate, re-sequence, or absorb the delay.
*   **Period:** The planning period the row covers, using the same periods as the planning basis section so the two can be read together. Where a quarter appears in one table and a month in another, the reader has to reconcile them before drawing any conclusion.
*   **Planned Funding:** The money available in the period across the whole portfolio, from the approved budget rather than from requests. The roadmap's purpose is to test the plan against what is actually available, so a figure taken from requests tests nothing.
*   **Planned Capacity:** The resource capacity available in the period, in the unit the organisation uses, whether that is person-days, FTEs, or machine hours. The unit matters because a capacity row expressed in a different unit from the rest of the roadmap cannot be added up with anything else.
*   **Committed Load:** The capacity already committed to initiatives in the period, including work that will not finish inside it. Excluding the part that spills into the next period is the most common way a capacity table overstates what is free.
*   **Available:** The difference between planned and committed. This is the column that tells the reader whether the plan is feasible; a roadmap where this figure is negative in some period is a roadmap that will break in that period, and the shortfall is visible here or nowhere.
*   **Notes:** Anything that changes how the row should be read, such as a known shortage, a hiring assumption the row depends on, or a funding decision not yet taken. A capacity row without its assumptions reads as a commitment, and the reader treats it as one.
*   **ID:** The identifier for the assumption or constraint, so it can be referred to from the change log and from the initiative rows that depend on it.
*   **Type:** Whether the row is an Assumption or a Constraint. An assumption may prove false and be replaced; a constraint may not be replaced at all, only planned around, and recording both under one heading loses that distinction exactly where it matters.
*   **Description:** What is being assumed, or what is limiting the portfolio. State it as a testable statement rather than a sentiment, since an assumption phrased as a hope cannot be shown to have failed.
*   **Impact on Roadmap:** The effect on the roadmap if this proves false, or proves tighter than stated. An assumption recorded without its impact cannot be prioritised for testing, because nothing distinguishes the consequential ones from the trivial.
*   **Owner:** Who is responsible for confirming or managing it. An assumption with no owner is not being watched, and the roadmap carries it forward indefinitely after the conditions that made it true have gone.
*   **Review Date:** When the assumption will next be checked. This is what separates an assumption from a fact in practice: an assumption nobody revisits is indistinguishable from a fact, and it stops being questioned precisely when it should be.
*   **Change ID:** The identifier for the change, used to link it to the decision record and to the meeting that authorised it.
*   **Description:** What changed in the roadmap, stated concretely enough to be diffed against the previous version. A change described only as a realignment cannot be checked to see whether it actually happened.
*   **Reason:** Why it changed. A reader comparing two roadmaps needs the reason as much as the change itself, because the reason is what tells them whether the same reasoning applies to the next change or whether the reasoning has been overtaken.
*   **Affected Initiatives:** The initiatives the change touches, by identifier where possible. This is what allows the reader to see whether a change described as minor has in fact moved a committed date.
*   **Approved By:** Who authorised the change. A roadmap altered without an approver is a roadmap nobody owns, and the next alteration is as likely to be an error as a decision.
*   **Date:** When the change was approved, which fixes the version of the roadmap in which it took effect and lets the change log be read in order.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](00_01_Portfolio_Roadmap_Template.md)
* [🤖 LLM Generation Prompt](00_01_Portfolio_Roadmap.md)
* [📊 Data Structure (JSON)](00_01_Portfolio_Roadmap.json)
* [📈 Tabular Data (CSV)](00_01_Portfolio_Roadmap.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [00_01_Portfolio_Roadmap_Example.md](../../../../examples/en/00_Program_and_Portfolio_Management/01_Portfolio_Roadmap/00_01_Portfolio_Roadmap_Example.md)

</div>
