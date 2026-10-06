---
type: Form
lang: en
Form: Activity List (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/03_Schedule/02_Activity_List/04_03_02_Activity_List.npy
token_count: 483
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.976958+00:00'
form_id: PMO-04.03.02
status: approved
---

# Activity List - Generation Prompt

<!--
System Instructions: This document contains instructions for generating the
«Activity List». When asked to fill this template, follow the section-by-section
instructions below. Refer to `parameters.md` for project variables.
-->

> **Context and Definition:**
> A comprehensive table listing all scheduled activities required on the project to decompose WBS work packages into manageable execution units.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Work Breakdown Structure / WBS (PMO-04.02.06), Scope Statement (PMO-04.02.05)
>   * *Optional:* Resource Requirements (PMO-04.06.02), Risk Register (PMO-04.08.02)
> * **Downstream Dependents:**
>   * *Mandatory:* Project Schedule Baseline (PMO-04.03.08), Earned Value Analysis / EVA (PMO-06.05)
>   * *Optional:* Release Plan (PMO-04.03.09), Lookahead Planning Log (PMO-04.03.10)

---

## Schedule Activity Inventory

### Activity Identifier and Name
**Instruction:** Unique activity code and concise action-oriented title for each schedule activity.

**Generated Value:** [ Add details... ]

### Activity Scope of Work
**Instruction:** Specific narrative detailing the discrete scope of work to be performed in this activity.

**Generated Value:** [ Add details... ]

### Planned Iteration or Release
**Instruction:** The target delivery sprint, wave, or milestone window assigned to this activity.

**Generated Value:** [ Add details... ]

## Activity Details and Descriptions

### Activity Execution Method
**Instruction:** Technical or managerial execution approach applied to perform the work.

**Generated Value:** [ Add details... ]

### Estimated Effort and Duration Units
**Instruction:** Estimated working effort in person-hours and planned calendar duration.

**Generated Value:** [ Add details... ]

## Associated WBS Work Packages

### Parent WBS Work Package Mapping
**Instruction:** The parent WBS work package identifier and deliverable directly decomposed by this activity.

**Generated Value:** [ Add details... ]

### Activity Completion Deliverable
**Instruction:** The tangible or verified intermediate output produced upon activity completion.

**Generated Value:** [ Add details... ]

---
