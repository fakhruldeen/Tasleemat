---
type: Form
lang: en
Form: Duration Estimating Worksheet (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/03_Schedule/07_Duration_Estimating_Worksheet/04_03_07_Duration_Estimating_Worksheet.npy
token_count: 660
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.971559+00:00'
---

# Duration Estimating Worksheet - Generation Prompt

<!--
System Instructions: This document contains instructions for generating the
«Duration Estimating Worksheet». When asked to fill this template, follow the section-by-section
instructions below. Refer to `parameters.md` for project variables.
-->

> **Context and Definition:**
> A detailed analytical worksheet used to derive activity duration estimates using parametric, analogous, and three-point (PERT) methodologies.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Work Breakdown Structure / WBS (PMO-04.02.06), Scope Statement (PMO-04.02.05)
>   * *Optional:* Resource Requirements (PMO-04.06.02), Risk Register (PMO-04.08.02)
> * **Downstream Dependents:**
>   * *Mandatory:* Project Schedule Baseline (PMO-04.03.08), Earned Value Analysis / EVA (PMO-06.05)
>   * *Optional:* Release Plan (PMO-04.03.09), Lookahead Planning Log (PMO-04.03.10)

---

## Parametric Estimates

### Parametric Activity and Unit Metric
**Instruction:** The activity name and specific unit metric rate used for parametric calculation (e.g., hours per unit).

**Generated Value:** [ Add details... ]

### Quantity and Resource Factor
**Instruction:** Total quantity of work units and resource efficiency factor applied.

**Generated Value:** [ Add details... ]

### Parametric Duration Result
**Instruction:** Calculated duration derived from the mathematical parametric formula.

**Generated Value:** [ Add details... ]

## Analogous Estimates

### Historical Reference Activity
**Instruction:** Past project activity used as a baseline benchmark for historical comparison.

**Generated Value:** [ Add details... ]

### Historical Duration and Complexity Scaling
**Instruction:** Duration of past activity and scaling factor applied for project scope differences.

**Generated Value:** [ Add details... ]

### Analogous Duration Result
**Instruction:** Final duration outcome determined through analogous comparison.

**Generated Value:** [ Add details... ]

## Three-Point Estimates (Beta Distribution)

### Optimistic, Most Likely, and Pessimistic Durations
**Instruction:** The recorded optimistic (tO), most likely (tM), and pessimistic (tP) estimates.

**Generated Value:** [ Add details... ]

### Beta Calculated Expected Duration (tE)
**Instruction:** Calculated expected duration using the PERT beta distribution formula (tO + 4tM + tP) / 6.

**Generated Value:** [ Add details... ]

### Standard Deviation and Variance
**Instruction:** Calculated standard deviation (tP - tO) / 6 assessing estimating risk and variance.

**Generated Value:** [ Add details... ]

## Aggregated Schedule Reserves

### Total Calculated Schedule Buffer
**Instruction:** Consolidated sum of duration contingency buffers across all estimated activities.

**Generated Value:** [ Add details... ]

### Worksheet Reconciliation and Approval
**Instruction:** Formal review confirming no duplicate activity estimations across methods.

**Generated Value:** [ Add details... ]

---
