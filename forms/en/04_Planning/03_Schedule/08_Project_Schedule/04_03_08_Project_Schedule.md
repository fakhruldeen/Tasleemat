---
type: Form
lang: en
Form: Project Schedule (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/03_Schedule/08_Project_Schedule/04_03_08_Project_Schedule.npy
token_count: 566
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.974975+00:00'
form_id: PMO-04.03.08
status: approved
---

# Project Schedule - Generation Prompt

<!--
System Instructions: This document contains instructions for generating the
«Project Schedule». When asked to fill this template, follow the section-by-section
instructions below. Refer to `parameters.md` for project variables.
-->

> **Context and Definition:**
> The primary schedule output that presents linked activities with planned dates, durations, milestones, and resource allocations.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Work Breakdown Structure / WBS (PMO-04.02.06), Scope Statement (PMO-04.02.05)
>   * *Optional:* Resource Requirements (PMO-04.06.02), Risk Register (PMO-04.08.02)
> * **Downstream Dependents:**
>   * *Mandatory:* Project Schedule Baseline (PMO-04.03.08), Earned Value Analysis / EVA (PMO-06.05)
>   * *Optional:* Release Plan (PMO-04.03.09), Lookahead Planning Log (PMO-04.03.10)

---

## Baseline Schedule Summary

### Project Start and Target Finish Dates
**Instruction:** The authorized baseline start date and targeted project completion date.

**Generated Value:** [ Add details... ]

### Schedule Data Version and Baseline Status
**Instruction:** The formal schedule model version number and baseline authorization state.

**Generated Value:** [ Add details... ]

### Total Critical Path Length and Major Phases
**Instruction:** Total working days on the critical path and scheduled durations for each major project phase.

**Generated Value:** [ Add details... ]

## Detailed Schedule Data

### WBS Code and Activity Schedule Mapping
**Instruction:** Consolidated schedule line items linking WBS code, activity title, and work package.

**Generated Value:** [ Add details... ]

### Planned Start and Finish Dates
**Instruction:** Approved baseline start date and baseline completion date for each scheduled activity.

**Generated Value:** [ Add details... ]

### Assigned Resources and Effort Allocation
**Instruction:** Designated resource leads, team members, and allocated effort hours per activity.

**Generated Value:** [ Add details... ]

## Critical Path and Float Analysis

### Critical Path Flag and Dependencies
**Instruction:** Clear indicator (Yes/No) identifying critical path activities and predecessor linkages.

**Generated Value:** [ Add details... ]

### Total Float and Free Float Values
**Instruction:** Calculated total float and free float values in working days for each schedule activity.

**Generated Value:** [ Add details... ]

### Schedule Risk and Recovery Considerations
**Instruction:** Identification of high-risk scheduling bottlenecks and contingency deployment rules.

**Generated Value:** [ Add details... ]

---
