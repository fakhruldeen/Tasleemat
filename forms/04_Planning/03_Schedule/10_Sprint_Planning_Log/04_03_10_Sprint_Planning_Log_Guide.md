---
lang: en
layout: default
title: Sprint Planning Log
nav_order: 1
---

## Tasleemat Forms Guide
# Project Artifact: Sprint Planning Log

**Document Reference:** `PMO-04.03.10`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **Sprint Planning Log** in alignment with
Tasleemat framework.

---

### 1. What?
A record of one sprint: its goal and window, the stories committed with their estimates and acceptance criteria, who is carrying what, and what could stop it. It is the point at which a sprint becomes a commitment that can be checked rather than an intention.

---

### 2. Why?
Because a sprint is agreed in a meeting and reviewed weeks later by people who were not there. Without a record the review becomes an argument about memory, and the numbers that disagree are the ones nobody can reconstruct. The log also makes scope added mid-sprint visible, which is the single largest cause of a sprint finishing over.

---

### 3. When?
Prepared at the start of each sprint and completed at its review. Read again whenever the next sprint is planned, because the carry-over and the actual capacity are the two figures that the next estimate depends on.

---

### 4. Who?
The team lead records it and owns the estimate, the product owner owns the priority and confirms the goal, and the project manager confirms the sprint fits the release plan. A sign-off with only one of the first two is an agreement about half of what was planned.

---

### Tailoring Tips
*   A sprint of one story is fine and should be recorded as such; the log is not the place to argue for a smaller number.
*   Keep the identifiers exactly as the board shows them. A log that paraphrases them cannot be reconciled with the board later.
*   Where a story carries over, re-estimate it rather than repeating the old number, and say which of the two was done.
*   An agile team using this form may record only the committed scope and the risks; the remaining sections are there when a release needs defending.
*   Where the sprint is fixed by a release date rather than by capacity, record the date in the window field so the constraint is visible to whoever reviews the outcome.

---

### Alignment
The sprint plan should be consistent with the product backlog, the release plan, the project schedule, and the resource capacity matrix.

---

### 5. How?
To accurately complete the Sprint Planning Log, populate the following sections
based on the project context (ensuring reference to `parameters.md` for the
general project variables):

*   **Sprint Goal:** The one outcome the sprint is for, stated as a capability the team can demonstrate rather than as a list of stories. A goal written as a list of stories cannot be used to reject anything, and a sprint that cannot reject anything has no goal.
*   **Sprint Window:** The start and end dates, and the length of the sprint. The window is a constraint rather than a preference, because a sprint length that drifts produces a velocity figure that means nothing.
*   **Capacity Basis:** How much the team believes it can take on, and what that belief is based on. Capacity stated without its basis is a wish, and the first sprint is where a capacity figure is usually found to be wrong.
*   **Carry-over From the Previous Sprint:** What was not finished, and whether it has been re-estimated or carried as-is. Work carried without a new estimate is work whose estimate has never been tested.
*   **Story ID:** The identifier from the board, so the story can be traced when the sprint ends and the question is asked afterwards. A story with no identifier cannot be found again once it leaves the room.
*   **Story Title:** A short name for the story, in the language the team uses for it. A title that restates the acceptance criteria instead of naming the story makes the log harder to scan than the board it came from.
*   **Story Points:** The estimate for each story, and the scale used. Points are a relative comparison rather than a duration, so a scale changed between sprints makes two velocities incomparable.
*   **Priority:** Order relative to the other stories in this sprint, and why this story sits where it does. Priority stated as high or medium without a reason is a label rather than an ordering.
*   **Status:** Where the story stands at the end of the sprint, against what was committed. A status recorded only at review is too late to be useful to anyone planning the next sprint.
*   **Acceptance Criteria:** What will be true when the story is done, written so that a person who was not in the planning meeting can tell. Criteria agreed after the work is built describe whatever was built.
*   **Verified By:** Who checks the criteria and when. A criterion with no named verifier is a statement of intent, and the review becomes the first time anyone looks at it.
*   **Reason Added:** Why the story entered a sprint that had already been planned. The reason is the part worth recording, because it distinguishes a genuine discovery from a preference.
*   **Requested By:** Who asked for the addition, so the trade-off can be discussed with the person who wanted it. Scope added mid-sprint is how a sprint stops being a commitment.
*   **Effect on Sprint:** What the addition displaces, or which committed story now carries the risk of not finishing. An addition recorded without an effect reads as free, and it is not.
*   **Team Member:** The person, named rather than as a role, so the assignment can be checked against the person's actual availability.
*   **Role:** The role this person holds on the sprint, which is not the same as their title outside it. The role decides who settles an argument about scope during the sprint.
*   **Assigned Stories:** The stories this person is carrying in this sprint. The list is the thing to read for over-allocation: a person on every story in the log is a plan that has not been made yet.
*   **Available Capacity:** How much of this person's time the sprint actually has, after other commitments. Capacity at full for every story in the log is a statement of hope rather than of plan.
*   **Skill and Capacity Gaps:** What the committed scope needs that the team does not have. A gap named at planning is a risk to be managed; the same gap found at the end of the sprint is a surprise.
*   **Dependencies Outside the Team:** What must arrive from another team, and by when. A dependency with no date is an assumption, and it is usually discovered on the last day of the sprint.
*   **Risk:** What could stop the sprint, described as the event rather than as a feeling. A risk written as a concern cannot be managed, because there is nothing to watch for.
*   **Trigger:** The observable signal that the risk is happening. This is what makes a risk trackable: without a trigger the item is reviewed at the end of the sprint and found to have happened.
*   **Likelihood:** How likely the risk is, and what that judgement rests on. A bare high or low records no basis, so the next person cannot tell whether the estimate improved or the mood changed.
*   **Impact:** What the sprint loses if the risk occurs, measured in the same units as the commitment. Impact stated as severe is not comparable to a story estimate.
*   **Response:** What will be done about the risk while the sprint is running. A risk with no response is recorded in order to be mentioned later.
*   **Contingency:** What will be dropped or deferred if the risk occurs. A sprint with no contingency is a sprint where the decision gets made under pressure by whoever is most available at the time.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](04_03_10_Sprint_Planning_Log_Template.md)
* [🤖 LLM Generation Prompt](04_03_10_Sprint_Planning_Log.md)
* [📊 Data Structure (JSON)](04_03_10_Sprint_Planning_Log.json)
* [📈 Tabular Data (CSV)](04_03_10_Sprint_Planning_Log.csv)
