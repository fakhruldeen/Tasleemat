---
type: Form
lang: en
Form: Earned Value Analysis (Instructions)
token_pointer: /_tokens/forms/en/06_Monitoring_and_Controlling/05_Earned_Value_Analysis/06_05_Earned_Value_Analysis.npy
token_count: 1963
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.057757+00:00'
form_id: PMO-06.05
status: approved
---

# Earned Value Analysis - Generation Prompt

<!--
System Instructions: This document contains instructions for generating the
«Earned Value Analysis». When asked to fill this template, follow the section-by-section
instructions below. Refer to `parameters.md` for project variables.
-->

> **Context and Definition:**
> A rigorous performance measurement methodology that integrates project scope, schedule, and cost metrics to assess health and forecast final outcomes.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Approved Project Baselines (PMO-04.01.01), Work Performance Data & Logs (PMO-05.01 - 05.12)
>   * *Optional:* Risk Register (PMO-04.08.02), Vendor Agreements (PMO-04.09.04)
> * **Downstream Dependents:**
>   * *Mandatory:* Change Requests (PMO-05.03), Project / Phase Closeout (PMO-07.03), Lessons Learned Summary (PMO-07.01)
>   * *Optional:* Transition to Operations Checklist (PMO-07.04), Value Realization Register (PMO-01.03)

---

## Basic Earned Value Metrics

### Budget at Completion (BAC)
**Instruction:** The total approved baseline budget allocated for the complete project scope.

**Generated Value:** [ Add details... ]

### Planned Value (PV) / Current Reporting Period
**Instruction:** The authorized budget assigned to scheduled work for the current reporting period.

**Generated Value:** [ Add details... ]

### Planned Value (PV) / Current Period Cumulative
**Instruction:** The cumulative authorized budget planned from project start through current period.

**Generated Value:** [ Add details... ]

### Planned Value (PV) / Past Period Cumulative
**Instruction:** The cumulative planned value calculated at the close of the previous reporting period.

**Generated Value:** [ Add details... ]

### Earned Value (EV) / Current Reporting Period
**Instruction:** The budgeted amount for the work actually completed during the current period.

**Generated Value:** [ Add details... ]

### Earned Value (EV) / Current Period Cumulative
**Instruction:** The cumulative budgeted amount for all work accomplished from project start to date.

**Generated Value:** [ Add details... ]

### Earned Value (EV) / Past Period Cumulative
**Instruction:** The cumulative earned value achieved as of the previous reporting period.

**Generated Value:** [ Add details... ]

### Actual Cost (AC) / Current Reporting Period
**Instruction:** The actual expenditures incurred for work performed during the current period.

**Generated Value:** [ Add details... ]

### Actual Cost (AC) / Current Period Cumulative
**Instruction:** The cumulative total actual costs incurred from project start through current period.

**Generated Value:** [ Add details... ]

### Actual Cost (AC) / Past Period Cumulative
**Instruction:** The cumulative actual costs recorded as of the previous reporting period.

**Generated Value:** [ Add details... ]

## Variances and Indices

### Schedule Variance (SV) / Current Reporting Period
**Instruction:** The schedule performance in financial terms (EV - PV) for the current period.

**Generated Value:** [ Add details... ]

### Schedule Variance (SV) / Current Period Cumulative
**Instruction:** The cumulative schedule variance (Cumulative EV - Cumulative PV) to date.

**Generated Value:** [ Add details... ]

### Schedule Variance (SV) / Past Period Cumulative
**Instruction:** The cumulative schedule variance as of the prior reporting period.

**Generated Value:** [ Add details... ]

### Cost Variance (CV) / Current Reporting Period
**Instruction:** The financial budget variance (EV - AC) for the current reporting period.

**Generated Value:** [ Add details... ]

### Cost Variance (CV) / Current Period Cumulative
**Instruction:** The cumulative cost variance (Cumulative EV - Cumulative AC) to date.

**Generated Value:** [ Add details... ]

### Cost Variance (CV) / Past Period Cumulative
**Instruction:** The cumulative cost variance as of the prior reporting period.

**Generated Value:** [ Add details... ]

### Schedule Performance Index (SPI) / Current Reporting Period
**Instruction:** The schedule efficiency ratio (EV / PV) for the current period.

**Generated Value:** [ Add details... ]

### Schedule Performance Index (SPI) / Current Period Cumulative
**Instruction:** The cumulative schedule efficiency ratio (Cumulative EV / Cumulative PV).

**Generated Value:** [ Add details... ]

### Schedule Performance Index (SPI) / Past Period Cumulative
**Instruction:** The cumulative schedule efficiency index from the previous reporting period.

**Generated Value:** [ Add details... ]

### Cost Performance Index (CPI) / Current Reporting Period
**Instruction:** The cost efficiency ratio (EV / AC) for the current period.

**Generated Value:** [ Add details... ]

### Cost Performance Index (CPI) / Current Period Cumulative
**Instruction:** The cumulative cost efficiency ratio (Cumulative EV / Cumulative AC).

**Generated Value:** [ Add details... ]

### Cost Performance Index (CPI) / Past Period Cumulative
**Instruction:** The cumulative cost efficiency index from the previous reporting period.

**Generated Value:** [ Add details... ]

## Percentages

### Percent Planned / Current Reporting Period
**Instruction:** Planned Value divided by BAC for the current reporting period.

**Generated Value:** [ Add details... ]

### Percent Planned / Current Period Cumulative
**Instruction:** Cumulative Planned Value divided by BAC to measure scheduled completion percentage.

**Generated Value:** [ Add details... ]

### Percent Planned / Past Period Cumulative
**Instruction:** Cumulative Planned Value divided by BAC as of the prior reporting period.

**Generated Value:** [ Add details... ]

### Percent Earned / Current Reporting Period
**Instruction:** Earned Value divided by BAC for the current reporting period.

**Generated Value:** [ Add details... ]

### Percent Earned / Current Period Cumulative
**Instruction:** Cumulative Earned Value divided by BAC representing actual project percent complete.

**Generated Value:** [ Add details... ]

### Percent Earned / Past Period Cumulative
**Instruction:** Cumulative Earned Value divided by BAC as of the prior reporting period.

**Generated Value:** [ Add details... ]

### Percent Spent / Current Reporting Period
**Instruction:** Actual Cost divided by BAC for the current reporting period.

**Generated Value:** [ Add details... ]

### Percent Spent / Current Period Cumulative
**Instruction:** Cumulative Actual Cost divided by BAC representing total project budget spent to date.

**Generated Value:** [ Add details... ]

### Percent Spent / Past Period Cumulative
**Instruction:** Cumulative Actual Cost divided by BAC as of the prior reporting period.

**Generated Value:** [ Add details... ]

## Forecasting (Estimates)

### EAC w/CPI / Current Reporting Period
**Instruction:** Estimate at Completion assuming future work performed at current period CPI (BAC / CPI).

**Generated Value:** [ Add details... ]

### EAC w/CPI / Current Period Cumulative
**Instruction:** Estimate at Completion assuming future work performed at cumulative CPI.

**Generated Value:** [ Add details... ]

### EAC w/CPI / Past Period Cumulative
**Instruction:** Estimate at Completion based on past period cumulative CPI.

**Generated Value:** [ Add details... ]

### EAC w/CPI × SPI / Current Reporting Period
**Instruction:** Estimate at Completion factoring both cost and schedule indices for current period.

**Generated Value:** [ Add details... ]

### EAC w/CPI × SPI / Current Period Cumulative
**Instruction:** Estimate at Completion factoring cumulative cost and schedule performance indices.

**Generated Value:** [ Add details... ]

### EAC w/CPI × SPI / Past Period Cumulative
**Instruction:** Estimate at Completion factoring past period cumulative cost and schedule indices.

**Generated Value:** [ Add details... ]

### To Complete Performance Index (TCPI) / Current Reporting Period
**Instruction:** Cost efficiency required to complete the remaining work within BAC for current period.

**Generated Value:** [ Add details... ]

### To Complete Performance Index (TCPI) / Current Period Cumulative
**Instruction:** Cost efficiency required to complete the remaining work within BAC cumulatively.

**Generated Value:** [ Add details... ]

### To Complete Performance Index (TCPI) / Past Period Cumulative
**Instruction:** TCPI calculated at the close of the prior reporting period.

**Generated Value:** [ Add details... ]

### Selected EAC - Justification and Explanation
**Instruction:** Detailed justification of the selected EAC forecasting formula and expected final budget outcome.

**Generated Value:** [ Add details... ]

## Root Cause and Impacts Analysis

### Root cause of schedule variance
**Instruction:** Underlying drivers and operational causes for schedule efficiency or delay.

**Generated Value:** [ Add details... ]

### Schedule impact (incl. implications of continued variance)
**Instruction:** Projected delivery delays and critical path impacts if schedule trends continue.

**Generated Value:** [ Add details... ]

### Root cause of cost variance
**Instruction:** Operational factors, rate fluctuations, or scope drivers causing cost variances.

**Generated Value:** [ Add details... ]

### Budget impact (incl. intended actions/reserves)
**Instruction:** Financial exposure and reserve utilization strategies to maintain fiscal control.

**Generated Value:** [ Add details... ]

## Comments

### Comments
**Instruction:** Additional contextual observations or recommendations from the EVM analyst.

**Generated Value:** [ Add details... ]

---
