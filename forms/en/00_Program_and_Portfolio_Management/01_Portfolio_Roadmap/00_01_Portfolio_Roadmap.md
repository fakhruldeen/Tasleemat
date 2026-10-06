---
type: Form
lang: en
Form: PORTFOLIO ROADMAP (Instructions)
---

# PORTFOLIO ROADMAP - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `PORTFOLIO ROADMAP`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required content.
> Reference `parameters.md` for global project variables.

> **Context & Definition:**
> A portfolio roadmap is a time-phased, visual representation of the programs,
> projects, and operations in a portfolio, showing their sequence, expected
> outcomes, and the dependencies between them. Its purpose is to communicate
> strategy and to let decision-makers see the consequence of a change before the
> change is made, rather than discovering it a quarter later when funding has
> already been committed.

> **Alignment:**
> This portfolio roadmap must be consistent with: Program charter, Business case,
> Portfolio management plan, Resource capacity matrix.


## Portfolio Context and Planning Basis


### Portfolio Purpose and Scope


**Instruction:** What this portfolio covers and what it deliberately excludes, in the terms the strategy uses. A roadmap that does not state its boundaries cannot be read against a strategy that is wider than the portfolio, and the gap is mistaken for missing initiatives.


**Generated value:** [ Add details... ]


### Planning Period


**Instruction:** The period the roadmap plans for, and whether it is a financial year, a rolling three years, or a fixed cycle agreed elsewhere. Successive roadmaps are only comparable if this is the same each time.


**Generated value:** [ Add details... ]


### Roadmap Horizon


**Instruction:** How far ahead the roadmap looks. Record the horizon even where it equals the planning period, because the two are frequently confused and the confusion shows up later as a gap between what was planned and what was expected.


**Generated value:** [ Add details... ]


### Portfolio Owner


**Instruction:** The single role accountable for the portfolio as a whole, which is usually not the owner of any one initiative in it. Where this is left blank, the roadmap has an author but no owner, and reprioritisation becomes nobody's decision.


**Generated value:** [ Add details... ]


### Planning Cycle


**Instruction:** How often the roadmap is refreshed and by what governance forum, such as a quarterly investment board. The cycle is what makes two versions of the roadmap comparable, and a roadmap refreshed on no cycle is a document nobody can diff.


**Generated value:** [ Add details... ]


### Roadmap Version and Status


**Instruction:** Which planning cycle this represents, its version number, and whether it is draft or approved. Without a version, two roadmaps differing by a few initiatives cannot be read as a change of direction rather than as two views of the same portfolio.


**Generated value:** [ Add details... ]


## Roadmap Initiatives


### ID


**Instruction:** The stable identifier for the initiative, used by every later cycle of this roadmap and by the dependency and funding sections. A roadmap reviewed across several cycles is unreadable if an initiative is named differently each time, because the reader cannot tell whether two rows are one initiative or two.


**Generated value:** [ Add details... ]


### Initiative Name


**Instruction:** The name of the program, project, or operation, taken from its charter so the same initiative is not tracked under two names. Where a name has changed, record the former name rather than replacing it, or the history becomes impossible to follow.


**Generated value:** [ Add details... ]


### Type


**Instruction:** Whether the row is a Program, Project, or Operation. The type determines what governance applies, so an initiative recorded without one has no defined approval path, and the roadmap cannot answer what kind of decision is needed about it.


**Generated value:** [ Add details... ]


### Strategic Objective


**Instruction:** The specific objective this initiative serves, named from the strategy rather than from the initiative's own charter. An initiative that maps to no objective is a candidate for removal, and the roadmap is the only place that becomes visible; where the mapping is genuinely absent, say so in the cell rather than leaving it blank.


**Generated value:** [ Add details... ]


### Start


**Instruction:** When the initiative is expected to start, at the precision this table uses throughout. Mixed precision within one table is the thing to avoid, because the reader compares the rows against each other and a month beside a quarter invites a wrong conclusion.


**Generated value:** [ Add details... ]


### End


**Instruction:** When the initiative is expected to deliver its outcomes, which is not the same as when its budget is spent. An initiative that delivers early and closes its accounts later is normal, and recording the accounts date as the end date moves every dependent initiative on the roadmap.


**Generated value:** [ Add details... ]


### Budget


**Instruction:** The funding envelope allocated to the initiative for the planning period, not a spend forecast. The roadmap answers whether the money is available in the period, not whether it is being spent, and the two are routinely confused when the figure is taken from a finance system.


**Generated value:** [ Add details... ]


### Status


**Instruction:** Where the initiative currently stands against the fixed set agreed for this roadmap, such as Proposed, Funded, In Progress, On Hold, or Complete. A free-text status cannot be sorted or filtered, and a roadmap that cannot be filtered is a picture rather than a plan.


**Generated value:** [ Add details... ]


## Dependencies and Sequencing


### ID


**Instruction:** The identifier of the initiative whose dependency is being recorded, matching the ID used in the initiatives section so the row can be joined to it.


**Generated value:** [ Add details... ]


### Dependent Initiative


**Instruction:** The initiative that cannot proceed, or cannot proceed on its own dates, without the predecessor. Name it rather than describing it, because a dependency stated in terms of a category rather than a named initiative cannot be actioned when it is threatened.


**Generated value:** [ Add details... ]


### Dependency Type


**Instruction:** Whether the dependency is Finish to Start, Start to Start, Finish to Finish, or Start to Finish. The type determines how much float the successor has, so an untyped dependency cannot be planned; Finish to Start is the common case and the others arise where two initiatives must move together.


**Generated value:** [ Add details... ]


### Predecessor


**Instruction:** The initiative on which this one depends, named and identified. A dependency recorded only in prose is a dependency nobody can query, and it is therefore a dependency that will not be checked before the predecessor slips.


**Generated value:** [ Add details... ]


### Required By


**Instruction:** The date by which the dependency must be satisfied for the dependent initiative to hold its own dates. Where the required date is later than the predecessor's planned finish, the gap is the risk and should be visible here rather than discovered later.


**Generated value:** [ Add details... ]


### Impact if Late


**Instruction:** What happens to the dependent initiative if the predecessor does not deliver in time, in money, schedule, or scope terms. A dependency with no stated impact is not actionable when the predecessor slips, because nobody knows whether to escalate, re-sequence, or absorb the delay.


**Generated value:** [ Add details... ]


## Funding and Capacity by Period


### Period


**Instruction:** The planning period the row covers, using the same periods as the planning basis section so the two can be read together. Where a quarter appears in one table and a month in another, the reader has to reconcile them before drawing any conclusion.


**Generated value:** [ Add details... ]


### Planned Funding


**Instruction:** The money available in the period across the whole portfolio, from the approved budget rather than from requests. The roadmap's purpose is to test the plan against what is actually available, so a figure taken from requests tests nothing.


**Generated value:** [ Add details... ]


### Planned Capacity


**Instruction:** The resource capacity available in the period, in the unit the organisation uses, whether that is person-days, FTEs, or machine hours. The unit matters because a capacity row expressed in a different unit from the rest of the roadmap cannot be added up with anything else.


**Generated value:** [ Add details... ]


### Committed Load


**Instruction:** The capacity already committed to initiatives in the period, including work that will not finish inside it. Excluding the part that spills into the next period is the most common way a capacity table overstates what is free.


**Generated value:** [ Add details... ]


### Available


**Instruction:** The difference between planned and committed. This is the column that tells the reader whether the plan is feasible; a roadmap where this figure is negative in some period is a roadmap that will break in that period, and the shortfall is visible here or nowhere.


**Generated value:** [ Add details... ]


### Notes


**Instruction:** Anything that changes how the row should be read, such as a known shortage, a hiring assumption the row depends on, or a funding decision not yet taken. A capacity row without its assumptions reads as a commitment, and the reader treats it as one.


**Generated value:** [ Add details... ]


## Assumptions and Constraints


### ID


**Instruction:** The identifier for the assumption or constraint, so it can be referred to from the change log and from the initiative rows that depend on it.


**Generated value:** [ Add details... ]


### Type


**Instruction:** Whether the row is an Assumption or a Constraint. An assumption may prove false and be replaced; a constraint may not be replaced at all, only planned around, and recording both under one heading loses that distinction exactly where it matters.


**Generated value:** [ Add details... ]


### Description


**Instruction:** What is being assumed, or what is limiting the portfolio. State it as a testable statement rather than a sentiment, since an assumption phrased as a hope cannot be shown to have failed.


**Generated value:** [ Add details... ]


### Impact on Roadmap


**Instruction:** The effect on the roadmap if this proves false, or proves tighter than stated. An assumption recorded without its impact cannot be prioritised for testing, because nothing distinguishes the consequential ones from the trivial.


**Generated value:** [ Add details... ]


### Owner


**Instruction:** Who is responsible for confirming or managing it. An assumption with no owner is not being watched, and the roadmap carries it forward indefinitely after the conditions that made it true have gone.


**Generated value:** [ Add details... ]


### Review Date


**Instruction:** When the assumption will next be checked. This is what separates an assumption from a fact in practice: an assumption nobody revisits is indistinguishable from a fact, and it stops being questioned precisely when it should be.


**Generated value:** [ Add details... ]


## Roadmap Changes


### Change ID


**Instruction:** The identifier for the change, used to link it to the decision record and to the meeting that authorised it.


**Generated value:** [ Add details... ]


### Description


**Instruction:** What changed in the roadmap, stated concretely enough to be diffed against the previous version. A change described only as a realignment cannot be checked to see whether it actually happened.


**Generated value:** [ Add details... ]


### Reason


**Instruction:** Why it changed. A reader comparing two roadmaps needs the reason as much as the change itself, because the reason is what tells them whether the same reasoning applies to the next change or whether the reasoning has been overtaken.


**Generated value:** [ Add details... ]


### Affected Initiatives


**Instruction:** The initiatives the change touches, by identifier where possible. This is what allows the reader to see whether a change described as minor has in fact moved a committed date.


**Generated value:** [ Add details... ]


### Approved By


**Instruction:** Who authorised the change. A roadmap altered without an approver is a roadmap nobody owns, and the next alteration is as likely to be an error as a decision.


**Generated value:** [ Add details... ]


### Date


**Instruction:** When the change was approved, which fixes the version of the roadmap in which it took effect and lets the change log be read in order.


**Generated value:** [ Add details... ]

