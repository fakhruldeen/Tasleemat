---
type: Form
lang: en
Form: Cost Baseline (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/04_Cost/04_Cost_Baseline/04_04_04_Cost_Baseline.npy
token_count: 525
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.955066+00:00'
form_id: PMO-04.04.04
status: approved
---

# Cost Baseline - Generation Prompt

<!--
System Instructions: This document contains instructions for generating the
«Cost Baseline». When asked to fill this template, follow the section-by-section
instructions below. Refer to `parameters.md` for project variables.
-->

> **Context and Definition:**
> The approved version of the time-phased project budget, excluding any management reserves, which can be changed only through formal change control.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Work Breakdown Structure / WBS (PMO-04.02.06), Project Schedule (PMO-04.03.08), Resource Requirements (PMO-04.06.02)
>   * *Optional:* Risk Register (PMO-04.08.02), Procurement Strategy (PMO-04.09.02)
> * **Downstream Dependents:**
>   * *Mandatory:* Cost Baseline (PMO-04.04.04), Earned Value Analysis / EVA (PMO-06.05), Variance Analysis (PMO-06.04)
>   * *Optional:* Cost Estimating Worksheet (PMO-04.04.03), Procurement Budget Plan (PMO-04.09.01)

---

## Time-Phased Cost Baseline (S-Curve)

### Reporting Period and Planned Expenditures
**Instruction:** Periodic time-phased planned expenditures across months or fiscal quarters.

**Generated Value:** [ Add details... ]

### Cumulative Planned Value (S-Curve PV)
**Instruction:** The authorized cumulative planned budget curve from project start to completion.

**Generated Value:** [ Add details... ]

### Budget at Completion (BAC) Total
**Instruction:** The total authorized baseline budget excluding management reserves.

**Generated Value:** [ Add details... ]

## Work Package Budget Allocations

### Control Account and Work Package Allocations
**Instruction:** Approved baseline budget figures mapped to specific WBS control accounts.

**Generated Value:** [ Add details... ]

### Contingency Reserve Distribution
**Instruction:** Distribution of project contingency reserves assigned across control accounts.

**Generated Value:** [ Add details... ]

## Project Funding Requirements and Limits

### Periodic Funding Requirements
**Instruction:** Total cash outlay required per period, incorporating funding step increments.

**Generated Value:** [ Add details... ]

### Management Reserve and Total Project Budget
**Instruction:** Executive management reserve amount and the total authorized project budget (BAC + Management Reserve).

**Generated Value:** [ Add details... ]

---
