---
type: Guide
token_pointer: /_tokens/docs/guides/en/06_Monitoring_and_Controlling/06_05_Earned_Value_Analysis_Guide.npy
token_count: 2326
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.394197+00:00'
---

<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/06_Monitoring_and_Controlling/05_Earned_Value_Analysis/06_05_Earned_Value_Analysis_Guide.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../ar/06_المراقبة_والتحكم/06_05_تحليل_القيمة_المكتسبة_(EVA)_دليل.html">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-06.05</span>
    <span class="badge badge-phase">06. Monitoring & Controlling</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../forms/en/06_Monitoring_and_Controlling/06_05_Earned_Value_Analysis_Template.html">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/06_Monitoring_and_Controlling/06_05_Earned_Value_Analysis_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/06_Monitoring_and_Controlling/05_Earned_Value_Analysis/06_05_Earned_Value_Analysis_Guide.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../ar/06_المراقبة_والتحكم/06_05_تحليل_القيمة_المكتسبة_(EVA)_دليل.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
lang: en
layout: default
title: Earned Value Analysis
nav_order: 5
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;" markdown="1">

## Tasleemat Forms Guide
# Project Artifact: Earned Value Analysis

**Document Reference:** `PMO-06.05`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Earned Value Analysis** in alignment with the
Tasleemat framework.

---

### 1. What?
A quantitative management artifact calculating PV, EV, AC, variances (SV, CV), indices (SPI, CPI), and estimates at completion (EAC, TCPI).

---

### 2. Why?
Provides objective mathematical forecasting of final project cost and completion dates, avoiding optimistic bias.

---

### 3. When?
Calculated at regular reporting intervals throughout project execution and controlling.

---

### 4. Who?
Produced by Project Controller or Project Manager and reviewed by PMO and Executive Sponsors.

---

### Tailoring Tips
*   Select the appropriate EAC forecasting formula based on whether past variances are considered typical or atypical.
*   Calculate EVM at control account level for complex multi-vendor programs.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Approved Project Baselines (PMO-04.01.01)
    *   Work Performance Data & Logs (PMO-05.01 - 05.12)
*   **Optional / Contextual:**
    *   Risk Register (PMO-04.08.02)
    *   Vendor Agreements (PMO-04.09.04)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Change Requests (PMO-05.03)
    *   Project / Phase Closeout (PMO-07.03)
    *   Lessons Learned Summary (PMO-07.01)
*   **Optional / Contextual:**
    *   Transition to Operations Checklist (PMO-07.04)
    *   Value Realization Register (PMO-01.03)

---

### 5. How?
To accurately and professionally complete the **Earned Value Analysis**, the responsible party
must populate the following critical sections based on the project context (ensure `parameters.md` is referenced for global project variables):

*   **Budget at Completion (BAC):** The total approved baseline budget allocated for the complete project scope.
*   **Planned Value (PV) / Current Reporting Period:** The authorized budget assigned to scheduled work for the current reporting period.
*   **Planned Value (PV) / Current Period Cumulative:** The cumulative authorized budget planned from project start through current period.
*   **Planned Value (PV) / Past Period Cumulative:** The cumulative planned value calculated at the close of the previous reporting period.
*   **Earned Value (EV) / Current Reporting Period:** The budgeted amount for the work actually completed during the current period.
*   **Earned Value (EV) / Current Period Cumulative:** The cumulative budgeted amount for all work accomplished from project start to date.
*   **Earned Value (EV) / Past Period Cumulative:** The cumulative earned value achieved as of the previous reporting period.
*   **Actual Cost (AC) / Current Reporting Period:** The actual expenditures incurred for work performed during the current period.
*   **Actual Cost (AC) / Current Period Cumulative:** The cumulative total actual costs incurred from project start through current period.
*   **Actual Cost (AC) / Past Period Cumulative:** The cumulative actual costs recorded as of the previous reporting period.
*   **Schedule Variance (SV) / Current Reporting Period:** The schedule performance in financial terms (EV - PV) for the current period.
*   **Schedule Variance (SV) / Current Period Cumulative:** The cumulative schedule variance (Cumulative EV - Cumulative PV) to date.
*   **Schedule Variance (SV) / Past Period Cumulative:** The cumulative schedule variance as of the prior reporting period.
*   **Cost Variance (CV) / Current Reporting Period:** The financial budget variance (EV - AC) for the current reporting period.
*   **Cost Variance (CV) / Current Period Cumulative:** The cumulative cost variance (Cumulative EV - Cumulative AC) to date.
*   **Cost Variance (CV) / Past Period Cumulative:** The cumulative cost variance as of the prior reporting period.
*   **Schedule Performance Index (SPI) / Current Reporting Period:** The schedule efficiency ratio (EV / PV) for the current period.
*   **Schedule Performance Index (SPI) / Current Period Cumulative:** The cumulative schedule efficiency ratio (Cumulative EV / Cumulative PV).
*   **Schedule Performance Index (SPI) / Past Period Cumulative:** The cumulative schedule efficiency index from the previous reporting period.
*   **Cost Performance Index (CPI) / Current Reporting Period:** The cost efficiency ratio (EV / AC) for the current period.
*   **Cost Performance Index (CPI) / Current Period Cumulative:** The cumulative cost efficiency ratio (Cumulative EV / Cumulative AC).
*   **Cost Performance Index (CPI) / Past Period Cumulative:** The cumulative cost efficiency index from the previous reporting period.
*   **Percent Planned / Current Reporting Period:** Planned Value divided by BAC for the current reporting period.
*   **Percent Planned / Current Period Cumulative:** Cumulative Planned Value divided by BAC to measure scheduled completion percentage.
*   **Percent Planned / Past Period Cumulative:** Cumulative Planned Value divided by BAC as of the prior reporting period.
*   **Percent Earned / Current Reporting Period:** Earned Value divided by BAC for the current reporting period.
*   **Percent Earned / Current Period Cumulative:** Cumulative Earned Value divided by BAC representing actual project percent complete.
*   **Percent Earned / Past Period Cumulative:** Cumulative Earned Value divided by BAC as of the prior reporting period.
*   **Percent Spent / Current Reporting Period:** Actual Cost divided by BAC for the current reporting period.
*   **Percent Spent / Current Period Cumulative:** Cumulative Actual Cost divided by BAC representing total project budget spent to date.
*   **Percent Spent / Past Period Cumulative:** Cumulative Actual Cost divided by BAC as of the prior reporting period.
*   **EAC w/CPI / Current Reporting Period:** Estimate at Completion assuming future work performed at current period CPI (BAC / CPI).
*   **EAC w/CPI / Current Period Cumulative:** Estimate at Completion assuming future work performed at cumulative CPI.
*   **EAC w/CPI / Past Period Cumulative:** Estimate at Completion based on past period cumulative CPI.
*   **EAC w/CPI × SPI / Current Reporting Period:** Estimate at Completion factoring both cost and schedule indices for current period.
*   **EAC w/CPI × SPI / Current Period Cumulative:** Estimate at Completion factoring cumulative cost and schedule performance indices.
*   **EAC w/CPI × SPI / Past Period Cumulative:** Estimate at Completion factoring past period cumulative cost and schedule indices.
*   **To Complete Performance Index (TCPI) / Current Reporting Period:** Cost efficiency required to complete the remaining work within BAC for current period.
*   **To Complete Performance Index (TCPI) / Current Period Cumulative:** Cost efficiency required to complete the remaining work within BAC cumulatively.
*   **To Complete Performance Index (TCPI) / Past Period Cumulative:** TCPI calculated at the close of the prior reporting period.
*   **Selected EAC - Justification and Explanation:** Detailed justification of the selected EAC forecasting formula and expected final budget outcome.
*   **Root cause of schedule variance:** Underlying drivers and operational causes for schedule efficiency or delay.
*   **Schedule impact (incl. implications of continued variance):** Projected delivery delays and critical path impacts if schedule trends continue.
*   **Root cause of cost variance:** Operational factors, rate fluctuations, or scope drivers causing cost variances.
*   **Budget impact (incl. intended actions/reserves):** Financial exposure and reserve utilization strategies to maintain fiscal control.
*   **Comments:** Additional contextual observations or recommendations from the EVM analyst.

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [06_05_Earned_Value_Analysis_Example.md](../../../examples/en/06_Monitoring_and_Controlling/06_05_Earned_Value_Analysis_Example.md)

</div>
