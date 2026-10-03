<div class="lang-switch-bar">
  <span>🌐 Dual Language / ثنائي اللغة:</span>
  <a class="lang-switch-btn" href="../../ar/06_المراقبة_والتحكم/06_10_نموذج_اعتماد_اختبار_قبول_المستخدم_(UAT)_دليل.md">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide)</a>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-06.10</span>
    <span class="badge badge-phase">06. Monitoring & Controlling</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../templates/en/06_Monitoring_and_Controlling/06_10_User_Acceptance_Testing_Signoff_Template.md">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/06_Monitoring_and_Controlling/06_10_User_Acceptance_Testing_Signoff_Example.md">💡 Completed Example</a>
    <a class="nav-pill lang-pill" href="../../ar/06_المراقبة_والتحكم/06_10_نموذج_اعتماد_اختبار_قبول_المستخدم_(UAT)_دليل.md">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
lang: en
layout: default
title: User Acceptance Testing Signoff
nav_order: 7
---

## Tasleemat Forms Guide
# Project Artifact: User Acceptance Testing Signoff

**Document Reference:** `PMO-06.10`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **User Acceptance Testing Signoff** in alignment with the
Tasleemat framework.

---

### 1. What?
Five statements rather than a table, because their lengths are not comparable and a table would pretend they are: what was tested, where it was tested and against what was decided beforehand as the standard for passing, what was found and accepted rather than fixed, and the business's decision in its own terms.

---

### 2. Why?
Because acceptance is the point at which the work stops being the project's and becomes the business's. A test report can be reopened; a signature cannot be withdrawn by the team that asked for it. That is what makes the record worth keeping carefully, and it is also why the criteria and the defects matter more than they would in a test report: the criteria establish what was actually agreed, and the defects are what the business knew about when it agreed.

---

### 3. When?
Once per release or per acceptance milestone, after the testing has been executed and before the project moves to the next phase or to operations. Not drafted in advance and not revised afterwards: a signoff edited after a problem is found is a signoff that cannot be relied on, because the reader has no way to tell what was agreed from what was accepted later.

---

### 4. Who?
Signed by the business owner or client representative, who is the party accepting the risk and is the only one with the authority to accept it, with the quality manager accountable for the testing having been done against the plan and the project manager for the schedule consequence of the date. The client signature is the one that matters and the one most often missing, which is how a project reaches go-live with nobody having agreed to anything.

---

### Tailoring Tips
*   Agree the criteria before the testing starts. Criteria written afterwards describe what happened rather than deciding whether it was acceptable, and a reader cannot tell the two apart.
*   Record what was accepted, not only what passed. An empty defects section asserts that the testing found nothing, which is almost never what happened, and a reader who suspects that has no way to check it.
*   Say which build and which environment. A pass somewhere other than where the business will work is not a pass, and the signature does not carry that distinction.

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
To accurately complete the User Acceptance Testing Signoff, populate the following sections based on
the project context (ensuring reference to `parameters.md` for the general
project variables):

*   **Test Summary:** What was tested, stated so that a reader can tell whether this was the whole release or a slice of it, and so that the criteria below can be read against something. "The system" is not a test summary; "the three checkout flows plus the refund path" is.
*   **Testing Environment:** Where the testing took place and against what. The environment and the build are part of what was accepted: a pass on a developer's machine is not a pass on the environment the business will use, and a signature that does not record which one was tested cannot be relied on at go-live.
*   **Pass/Fail Criteria:** What was decided before the testing began, not what was concluded after it. The criteria are what make the result mean anything: "the system works" cannot fail, because every system works on the day it is demonstrated, and a criterion written afterwards describes the outcome.
*   **Known Defects:** What was found and accepted rather than fixed, with the severity and who agreed to carry it. This section is what makes the signature honest: an empty defects section says the testing found nothing, which is almost never what happened, and a reader who knows that stops trusting the signature. Anything still open at go-live is discovered by somebody with no authority left to stop it.
*   **Business Owner Sign-off:** The decision, stated in the business's own terms rather than as a signature alone. What is being accepted, what is being accepted with, and what happens if something turns out not to work. This is the line that is read later when the question is whether the business agreed to this.

---

### Associated Templates
* [📄 Printable Template (Markdown)](../../../templates/en/06_Monitoring_and_Controlling/06_10_User_Acceptance_Testing_Signoff_Template.md)
* **🤖 Smart Generation Prompt**
* **📊 Data Structure (JSON)**
* **📈 Tabular Data (CSV)**

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [06_10_User_Acceptance_Testing_Signoff_Example.md](../../../examples/en/06_Monitoring_and_Controlling/06_10_User_Acceptance_Testing_Signoff_Example.md)
