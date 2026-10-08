<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/04_Planning/03_Schedule/07_Duration_Estimating_Worksheet/04_03_07_Duration_Estimating_Worksheet_Guide.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../../ar/04_التخطيط/03_الجدول_الزمني/04_03_07_ورقة_عمل_تقدير_المدة_دليل.html">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-04.03.07</span>
    <span class="badge badge-phase">04. Planning</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../../forms/en/04_Planning/03_Schedule/04_03_07_Duration_Estimating_Worksheet_Template.html">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../../examples/en/04_Planning/03_Schedule/04_03_07_Duration_Estimating_Worksheet_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/04_Planning/03_Schedule/07_Duration_Estimating_Worksheet/04_03_07_Duration_Estimating_Worksheet_Guide.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../../ar/04_التخطيط/03_الجدول_الزمني/04_03_07_ورقة_عمل_تقدير_المدة_دليل.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
type: Form
lang: en
layout: default
title: Duration Estimating Worksheet
nav_order: 7
token_pointer: /_tokens/forms/en/04_Planning/03_Schedule/07_Duration_Estimating_Worksheet/04_03_07_Duration_Estimating_Worksheet_Guide.npy
token_count: 819
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.972535+00:00'
form_id: PMO-04.03.07
status: approved
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;" markdown="1">

## Tasleemat Forms Guide
# Project Artifact: Duration Estimating Worksheet

**Document Reference:** `PMO-04.03.07`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Duration Estimating Worksheet** in alignment with the
Tasleemat framework.

---

### 1. What?
A structured computational artifact documenting formulas, inputs, assumptions, and statistical variance for schedule durations.

---

### 2. Why?
Ensures estimating rigor, documents mathematical basis of estimates, and quantifies duration uncertainty.

---

### 3. When?
Utilized during schedule planning when calculating detailed duration models.

---

### 4. Who?
Authored by Project Scheduler and Technical Leads, audited by Project Manager.

---

### Tailoring Tips
*   Focus on statistical three-point distributions for novel software research components.
*   Emphasize unit-rate parametric tables for repetitive engineering and construction installations.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Work Breakdown Structure / WBS (PMO-04.02.06)
    *   Scope Statement (PMO-04.02.05)
*   **Optional / Contextual:**
    *   Resource Requirements (PMO-04.06.02)
    *   Risk Register (PMO-04.08.02)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Project Schedule Baseline (PMO-04.03.08)
    *   Earned Value Analysis / EVA (PMO-06.05)
*   **Optional / Contextual:**
    *   Release Plan (PMO-04.03.09)
    *   Lookahead Planning Log (PMO-04.03.10)

---

### 5. How?
To accurately and professionally complete the **Duration Estimating Worksheet**, the responsible party
must populate the following critical sections based on the project context (ensure `parameters.md` is referenced for global project variables):

*   **Parametric Activity and Unit Metric:** The activity name and specific unit metric rate used for parametric calculation (e.g., hours per unit).
*   **Quantity and Resource Factor:** Total quantity of work units and resource efficiency factor applied.
*   **Parametric Duration Result:** Calculated duration derived from the mathematical parametric formula.
*   **Historical Reference Activity:** Past project activity used as a baseline benchmark for historical comparison.
*   **Historical Duration and Complexity Scaling:** Duration of past activity and scaling factor applied for project scope differences.
*   **Analogous Duration Result:** Final duration outcome determined through analogous comparison.
*   **Optimistic, Most Likely, and Pessimistic Durations:** The recorded optimistic (tO), most likely (tM), and pessimistic (tP) estimates.
*   **Beta Calculated Expected Duration (tE):** Calculated expected duration using the PERT beta distribution formula (tO + 4tM + tP) / 6.
*   **Standard Deviation and Variance:** Calculated standard deviation (tP - tO) / 6 assessing estimating risk and variance.
*   **Total Calculated Schedule Buffer:** Consolidated sum of duration contingency buffers across all estimated activities.
*   **Worksheet Reconciliation and Approval:** Formal review confirming no duplicate activity estimations across methods.

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [04_03_07_Duration_Estimating_Worksheet_Example.md](../../../../examples/en/04_Planning/03_Schedule/04_03_07_Duration_Estimating_Worksheet_Example.md)

</div>
