<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/05_Executing/08_Retrospective/05_08_Retrospective_Guide.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../ar/05_التنفيذ/05_08_مراجعة_المرحلة_(Retrospective)_دليل.html">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-05.08</span>
    <span class="badge badge-phase">05. Executing</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../forms/en/05_Executing/05_08_Retrospective_Template.html">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/05_Executing/05_08_Retrospective_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/05_Executing/08_Retrospective/05_08_Retrospective_Guide.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../ar/05_التنفيذ/05_08_مراجعة_المرحلة_(Retrospective)_دليل.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
type: Form
lang: en
layout: default
title: Retrospective
nav_order: 1
token_pointer: /_tokens/forms/en/05_Executing/08_Retrospective/05_08_Retrospective_Guide.npy
token_count: 1476
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.063985+00:00'
form_id: PMO-05.08
status: approved
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;" markdown="1">

## Tasleemat Forms Guide
# Project Artifact: Retrospective

**Document Reference:** `PMO-05.08`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Retrospective** in alignment with the
Tasleemat framework.

---

### 1. What?
A formal Tasleemat-aligned project document known as the **Retrospective**, an
activity performed at the end of every sprint. The information is usually
recorded on sticky notes or in software. A common approach is called a
starfish and collects Start, Stop, Keep, More, and Less. The intent is to
improve the performance of the team and make them more efficient in each
subsequent sprint.

It records the session context, the five starfish observations, the action
items taken from them with an owner and a review date, and the outcome of
those actions at the next retrospective. The FLAP alternative is carried as
a removable section.

---

### 2. Why?
Because a retrospective that records what happened without recording what will
change is a meeting rather than a feedback loop. The outcome column is what
turns a list of good intentions into a change in how the team works, and
without it the same actions are carried forward sprint after sprint.

---

### 3. When?
This artifact is prepared at the **EXECUTING** Process Group, at the end of
every sprint, or at whatever interval the team has agreed, which the form
records explicitly.

---

### 4. Who?
**Responsibilities:** Facilitated by the Team Lead with the whole team
present, including anyone who will be affected by the actions. Outcomes are
reviewed by the Project Manager at the following retrospective.

---

### Tailoring Tips
*   Instead of a starfish approach you can use "FLAP," which stands for
    Future Considerations, Lessons, Accomplishments, and Problems. Use one or
    the other, not both: two parallel forms each get half-filled and neither
    is trusted.
*   You can colour code information to indicate a category, such as
    technical, process, people, environment, etc. This makes a pattern
    visible that a list of sentences hides.
*   Add or remove rows as needed. Some teams run the retrospective per sprint,
    others per release, and the template should say which.
*   Keep one item per row and to a single sentence. An item that needs
    explaining is two items, or it is not yet understood well enough to act on.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Project Management Plan (PMO-04.01.01)
    *   Approved Baselines (Scope/Schedule/Cost)
*   **Optional / Contextual:**
    *   Risk Register (PMO-04.08.02)
    *   Stakeholder Engagement Plan (PMO-04.10.01)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Project Status Reports (PMO-06.01)
    *   Change Log (PMO-05.04)
    *   Lessons Learned Summary (PMO-07.01)
*   **Optional / Contextual:**
    *   Variance Analysis (PMO-06.04)
    *   Decision Log (PMO-05.02)

---

### 5. How?
To accurately and professionally complete the **RETROSPECTIVE**, the responsible party
must populate the following sections based on the project context (ensure
`parameters.md` is referenced for global project variables):

*   **Sprint or Iteration:** The sprint or iteration this retrospective covers. A retrospective that does not say which sprint it belongs to cannot be compared with the previous one, and an uncountable sequence of retrospectives is the same as none.
*   **Team Members Present:** Who took part. Someone who is not in the room cannot act on what was agreed, so name the absent members and how the outcome will reach them.
*   **Date:** The date the retrospective was held. Record it against the sprint number on the same line, because a retrospective carrying only a date cannot be matched to the one before it, and the set becomes a list of dates with no context.
*   **Start:** Actions and behaviors the team will begin to implement. Be specific: "hold a joint review with QA twice a week" can be started, "communicate better" cannot.
*   **Stop:** Actions or behaviors the team will cease doing. If the team is not willing to actually stop it, recording it here only builds a list the team learns to distrust.
*   **Keep:** Practices the team should continue with. Note why, because the reason is what a future team will need when the person who introduced the practice has moved on.
*   **More:** Practices that were not done consistently and should be done more often. Inconsistent usually means the practice exists but nothing enforces it, so record what would enforce it.
*   **Less:** Practices that were done too much or should be reduced. Watch for process that exists to fix a problem which no longer occurs; that is the usual source of ceremony the team has stopped noticing.
*   **Action:** The specific change being made, taken from the Start, Stop, More, and Less columns rather than invented separately.
*   **Owner:** The one person accountable for making it happen. A team cannot own an action, because a team is never available.
*   **By When:** The date it should be done, and where it will be reviewed. An action with no review date is an action that will be carried into the next retrospective as a note about doing it better.
*   **Outcome:** What happened when it was tried, filled in at the next retrospective. Without this column the team repeats the same actions and the retrospective becomes a ritual rather than a feedback loop.
*   **Future Considerations:** The FLAP alternative to the starfish. If the team prefers FLAP, replace the five starfish columns with Accomplishments, Problems, Lessons, and Future Considerations rather than recording both, since two parallel forms get half-filled and neither is trusted.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](../../../forms/en/05_Executing/05_08_Retrospective_Template.md)
* [🤖 LLM Generation Prompt](https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/05_Executing/08_Retrospective/05_08_Retrospective.md)
* [📊 Data Structure (JSON)](https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/05_Executing/08_Retrospective/05_08_Retrospective.json)
* [📈 Tabular Data (CSV)](https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/05_Executing/08_Retrospective/05_08_Retrospective.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [05_08_Retrospective_Example.md](../../../examples/en/05_Executing/05_08_Retrospective_Example.md)

</div>
