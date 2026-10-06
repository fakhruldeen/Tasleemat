---
type: Form
lang: en
layout: default
title: Prompt Library Log
nav_order: 7
---

## Tasleemat Forms Guide
# Project Artifact: Prompt Library Log

**Document Reference:** `PMO-05.09`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Prompt Library Log** in alignment with the
Tasleemat framework.

---

### 1. What?
A table of the prompts in use, one row each: an identifier, the use case, the text as it is actually sent, what a good response looks like, and the version and status it currently holds. The text column is the one that decides whether the log is usable: a prompt filed as a description has to be rewritten before it can be sent.

---

### 2. Why?
Because prompts are written repeatedly and rarely remembered, and the cost of a badly written prompt is paid in the review of whatever it produced. A library converts that cost into a lookup. It also converts an individual judgement into a shared one: a prompt that two people use gets better in a way that one person's habit does not, and the expected output column is what lets a team say the improvement happened.

---

### 3. When?
Written when a prompt has been used and found worth keeping, and revised whenever the prompt itself is revised. The version belongs in the first entry rather than being added later, because a prompt revised without a version number leaves every earlier result attached to a text that no longer exists.

---

### 4. Who?
Kept by whoever uses the prompts, which on an AI-enabled project is the team rather than a single owner. The AI or ML lead signs because that role is where prompts are drawn from and where the ones that do not work get noticed. The data protection officer signs because a prompt is where personal data most often enters a model without being noticed.

---

### Tailoring Tips
*   File the prompt, not its history. The library is read under time pressure, and an entry written with a paragraph of reasoning attached to it is an entry nobody opens.
*   Write the expected output before the prompt is used. Deciding what a good answer looks like after seeing the answer is not a standard, it is a description.
*   Retire what does not work. An entry that was used and did not help is the most valuable line in the log, provided it is marked as one rather than deleted.

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
To accurately complete the Prompt Library Log, populate the following sections based on
the project context (ensuring reference to `parameters.md` for the general
project variables):

*   **Prompt ID:** A short identifier, so a prompt can be referred to in a meeting without its text being read out. A number is enough if it is the only one in use.
*   **Use Case:** What the prompt is for, in one line: the task it was written to do and the situation it was written in. A prompt filed without its use case cannot be told apart from another one that reads almost the same.
*   **Prompt Text:** The prompt as it is actually sent, not a description of it. What is filed here has to be usable by pasting it, because a paraphrase is a different prompt and will behave differently.
*   **Expected Output:** What a good answer looks like, specifically enough to be checked. This is the column that makes the library auditable: without it there is nothing to compare a later response against.
*   **Status/Version:** Where the prompt stands, and which version this is. A prompt that has been revised without the version moving leaves every earlier result attached to a text that no longer exists.

---

### Associated Templates
* [📄 Printable Template (Markdown)](05_09_Prompt_Library_Log_Template.md)
* [🤖 Smart Generation Prompt](05_09_Prompt_Library_Log.md)
* [📊 Data Structure (JSON)](05_09_Prompt_Library_Log.json)
* [📈 Tabular Data (CSV)](05_09_Prompt_Library_Log.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [05_09_Prompt_Library_Log_Example.md](../../../../examples/en/05_Executing/09_Prompt_Library_Log/05_09_Prompt_Library_Log_Example.md)
