---
type: Form
lang: en
Form: RESOURCE CAPACITY MATRIX (Instructions)
token_pointer: /_tokens/forms/en/00_Program_and_Portfolio_Management/04_Resource_Capacity_Matrix/00_04_Resource_Capacity_Matrix.npy
token_count: 2240
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.029217+00:00'
form_id: PMO-00.04
status: approved
---

# RESOURCE CAPACITY MATRIX - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `RESOURCE CAPACITY MATRIX`. When asked to populate this form, use the
> guidance provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> The resource capacity matrix shows whether the plan is feasible in terms of
> the people available to carry it out. It compares what the programme or
> project needs against what exists, and the difference is the thing worth
> reading: a plan that requires more capacity than is available is not a plan
> that needs more effort, it is a plan that cannot be executed as written.

> **Alignment:**
> This resource capacity matrix must be consistent with: Portfolio roadmap,
> Program charter, Project management plan, Resource breakdown structure,
> Procurement plan.

### Matrix Scope and Level

**Instruction:** What this matrix covers and at what level it is maintained, whether portfolio-wide across initiatives, program-wide across components, or for a single project. The level decides what the matrix is used to decide: a portfolio matrix decides between initiatives, a project matrix decides whether one plan is credible, and reading either as the other produces a confident wrong answer.

**Generated value:** [ Add details... ]

### Capacity Unit of Measure

**Instruction:** The unit used for every figure in the matrix, whether person-days, full-time equivalents, or hours per period. State it once and use it throughout: a matrix whose rows use different units cannot be added up, and the total at the foot of it is then arithmetically meaningless rather than merely approximate.

**Generated value:** [ Add details... ]

### Periods Covered

**Instruction:** The periods the matrix covers, matching those of the schedule it is compared against. Where the matrix is annual and the schedule is weekly, the comparison has to be done by hand every time and is therefore not done, which is how a quarterly shortfall survives to become a delivery failure.

**Generated value:** [ Add details... ]

### Source of Truth or Extract

**Instruction:** Whether this matrix is the authoritative record or an extract from a resourcing tool. Record which, because a reader who treats a stale extract as current will plan against capacity that was reallocated weeks ago, and the error surfaces only when the work cannot be staffed.

**Generated value:** [ Add details... ]

### Matrix Owner

**Instruction:** The single role accountable for the matrix as a whole, which is normally not the owner of any one resource in it. Where this is blank, the matrix has contributors but nobody who notices that a row has not been updated since the reorganisation.

**Generated value:** [ Add details... ]

### Last Updated

**Instruction:** The date the matrix was last reconciled against the plan, and against which version of the schedule. Without it a reader cannot tell a current matrix from an abandoned one, and the two are indistinguishable on the page.

**Generated value:** [ Add details... ]

### ID

**Instruction:** The identifier for the resource role, used in the demand and gap sections so the three can be compared row against row. Without a shared identifier the comparison is done by eye, and two similarly named roles are the ones most often confused.

**Generated value:** [ Add details... ]

### Resource Role or Team

**Instruction:** The role or team, named as the work requires it rather than as the organisation chart draws it. A matrix organised by existing departments can never show a gap, because it only ever lists what is already there, and the absence of a needed capability reads as its absence from the plan rather than from the organisation.

**Generated value:** [ Add details... ]

### Period

**Instruction:** The period the row covers, using the same periods throughout the matrix. Capacity recorded per period rather than in total is what makes the matrix usable, because a resource with a thousand person-days available who is fully committed in the month the work is needed has no capacity at all.

**Generated value:** [ Add details... ]

### Total Available

**Instruction:** The capacity that exists in the period, before any allocation, in the unit declared for the matrix. This is a figure about the organisation rather than about the project, and recording it here is what allows the reader to see how much of it is actually available.

**Generated value:** [ Add details... ]

### Allocated

**Instruction:** The capacity already committed elsewhere in the portfolio. This is the column most often left out, and without it the available figure is the total, which is not what the project can use. It is also the column that reveals a resource being shared between initiatives without either owner knowing.

**Generated value:** [ Add details... ]

### Remaining

**Instruction:** What is left after allocation, which is the figure the planner actually has. Where this is negative, the matrix has found a real problem; where it is silently recorded as zero because nobody wanted to write a negative number, the problem has been hidden instead of solved.

**Generated value:** [ Add details... ]

### Constraints or Single Points of Failure

**Instruction:** What limits this resource: a location, a qualification held by one person, a licence, a tool only one person can operate, or a notice period. Record the consequence rather than the adjective, because "test automation is a single point of failure because one person holds it" can be acted on, while "test automation is a risk" cannot.

**Generated value:** [ Add details... ]

### Notes

**Instruction:** Anything that changes how the row should be read, such as a known vacancy, planned leave, or a resource shared with another portfolio. Where a role is filled by more than one person, record the role once and note the split here, since a row per person hides the total capacity of the role.

**Generated value:** [ Add details... ]

### ID

**Instruction:** The resource role the demand is for, matching the ID used in the capacity section so the two can be set against each other.

**Generated value:** [ Add details... ]

### Resource Role

**Instruction:** The role the demand falls on, using the same naming as the capacity section. The two must be the same list, or the comparison in the gap section silently excludes roles that appear in only one of them, which are usually the ones in trouble.

**Generated value:** [ Add details... ]

### Period

**Instruction:** The period the demand falls in. A demand recorded with no period cannot be compared with a capacity figure that has one, and is therefore dropped from the comparison without anyone deciding to drop it.

**Generated value:** [ Add details... ]

### Required Capacity

**Instruction:** What the scope and schedule require in the period. Record the figure the plan was built on rather than the figure currently being achieved, since the second is a consequence of the first being wrong and reporting it back as the requirement makes the shortfall disappear from the plan.

**Generated value:** [ Add details... ]

### Source of Demand

**Instruction:** Which part of the plan generates it, such as a named deliverable, work package, or activity. A demand that cannot be traced to something in the plan cannot be challenged, and demands that cannot be challenged only ever grow.

**Generated value:** [ Add details... ]

### Priority

**Instruction:** Whether the demand is essential, or could be deferred or descoped. Without a priority a gap has no remedy, because the available responses are to add capacity, move the work, or reduce it, and nothing in the matrix says which of those the programme would accept.

**Generated value:** [ Add details... ]

### Resource Role

**Instruction:** The role the gap applies to, using the same naming as the sections above. Where a role appears in the demand but not the capacity, the gap is the whole requirement rather than a shortfall, and that case is worth distinguishing because it is a different problem.

**Generated value:** [ Add details... ]

### Gap

**Instruction:** The difference between required and remaining, stated as a signed number so that a surplus is not read as a shortfall. This is the figure the whole matrix exists to produce, and a matrix that records only the totals has omitted the only number anyone reads.

**Generated value:** [ Add details... ]

### Period

**Instruction:** The period the gap falls in. A gap in a period with no demand in it is a different problem from a gap in a period the work needs, and reporting both as "a gap" sends the reader looking for the wrong remedy.

**Generated value:** [ Add details... ]

### Resolution Planned

**Instruction:** How the gap will be closed: recruitment, a contractor, moving work between periods, reducing scope, or accepting the risk. Where the gap is covered by a contractor or a shared resource, record the contract or agreement that covers it, because a gap filled on the understanding that someone will help is not covered at all.

**Generated value:** [ Add details... ]

### Resolution Owner

**Instruction:** Who is accountable for closing the gap. A gap with a planned resolution and no owner is a gap being wished away, and it is the most common way a capacity matrix comes to be relied upon long after it was last true.

**Generated value:** [ Add details... ]

### Resolution Date

**Instruction:** By when the resolution is expected to be in place. This is what tells the reader whether the plan is still feasible, so record it rather than leaving the row open, and where the date has passed without resolution, escalate rather than moving the date.

**Generated value:** [ Add details... ]

### Resource Role

**Instruction:** The role the contingency applies to, or "plan" where the buffer is held across all roles rather than against one.

**Generated value:** [ Add details... ]

### Contingency Type

**Instruction:** Whether the buffer is in capacity, in time, or in scope. The three are not interchangeable: time contingency can be spent once, capacity contingency can be spent on anything, and scope contingency reduces the deliverable. A plan that holds no scope contingency and states only that it has float is a plan whose contingency is the work being cut.

**Generated value:** [ Add details... ]

### Contingency Amount

**Instruction:** The size of the buffer, in the declared unit. Record it as a figure rather than a percentage, because a percentage of a demand that was never reconciled produces a number that looks precise and is not.

**Generated value:** [ Add details... ]

### How It Would Be Used

**Instruction:** What the buffer protects, recorded so it cannot be quietly consumed on something it was not held for. A contingency with no stated use is the first thing cut in a difficult month, which is precisely the month it was held for.

**Generated value:** [ Add details... ]
