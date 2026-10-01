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

### Alignment
the test plan, because the signoff is against the cases the plan defines; the product acceptance form, which records the same decision at deliverable level; and the transition to operations checklist, which cannot start until this is signed

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
* [📄 Printable Template (Markdown)](06_10_User_Acceptance_Testing_Signoff_Template.md)
* [🤖 Smart Generation Prompt](06_10_User_Acceptance_Testing_Signoff.md)
* [📊 Data Structure (JSON)](06_10_User_Acceptance_Testing_Signoff.json)
* [📈 Tabular Data (CSV)](06_10_User_Acceptance_Testing_Signoff.csv)
