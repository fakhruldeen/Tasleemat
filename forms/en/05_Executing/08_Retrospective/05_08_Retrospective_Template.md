---
type: Form
token_pointer: /_tokens/forms/en/05_Executing/08_Retrospective/05_08_Retrospective_Template.npy
token_count: 1792
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.063365+00:00'
---

<!--  LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

The retrospective is an activity that is performed at the end of every sprint. The information is usually recorded on sticky notes or recorded in software. A common retrospective approach is called a "starfish," which collects Start, Stop, Keep, More, and Less.

The intent of a retrospective is to improve the performance of the team and make them more efficient in each subsequent sprint. That intent is why this form carries action items and an outcome column and not only the five observation columns: a retrospective that records what happened without recording what will change is a meeting, not a feedback loop.

Alignment: the retrospective should be aligned and consistent with the following documents: Lessons learned summary, Project closeout.

Writing guidance:

*   Write one item per row and keep it to a single sentence. An item that needs explaining is two items, or it is not yet understood well enough to act on.

*   The five columns are not interchangeable. Stop means cease, not reduce; Less means too much of something, not something to stop altogether. Putting the same item in two columns to hedge is how a retrospective stops being honest.

*   Only record in Start and Stop what the team is genuinely willing to begin and cease. A list of good intentions nobody intends to act on teaches the team that the exercise is theatre.

*   Carry every action into the next retrospective with its outcome filled in. An action reviewed only once is an action nobody checked.

*   Colour coding is optional but useful: technical, process, people, environment. It makes a pattern visible that a list of sentences hides.

Tailoring Notes:

*   Instead of a starfish approach you can use "FLAP," which stands for Future Considerations, Lessons, Accomplishments, and Problems. Use one or the other, not both: two parallel forms each get half-filled and neither is trusted.

*   You can colour code information to indicate a category, such as technical, process, people, environment, etc.

*   Add or remove rows as needed. Some teams run the retrospective per sprint, others per release, and the template should say which.

Column guidance, by column:
- **Start:** Actions and behaviors the team will begin to implement. Be specific: "hold a joint review with QA twice a week" can be started, "communicate better" cannot.
- **Stop:** Actions or behaviors the team will cease doing. If the team is not willing to actually stop it, recording it here only builds a list the team learns to distrust.
- **Keep:** Practices the team should continue with. Note why, because the reason is what a future team will need when the person who introduced the practice has moved on.
- **More:** Practices that were not done consistently and should be done more often. Inconsistent usually means the practice exists but nothing enforces it, so record what would enforce it.
- **Less:** Practices that were done too much or should be reduced. Watch for process that exists to fix a problem which no longer occurs; that is the usual source of ceremony the team has stopped noticing.
- **Action:** The specific change being made, taken from the Start, Stop, More, and Less columns rather than invented separately.
- **Owner:** The one person accountable for making it happen. A team cannot own an action, because a team is never available.
- **By When:** The date it should be done, and where it will be reviewed. An action with no review date is an action that will be carried into the next retrospective as a note about doing it better.
- **Outcome:** What happened when it was tried, filled in at the next retrospective. Without this column the team repeats the same actions and the retrospective becomes a ritual rather than a feedback loop.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 dir="ltr" align="center">RETROSPECTIVE</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |  

---

## 1. Session
<!-- A retrospective that does not say which sprint it covers cannot be compared with the previous one, and someone who was not in the room cannot act on what was agreed. -->

| Sprint or Iteration | Team Members Present | Date |
| :--- | :--- | :---: |
| [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 2. Starfish
<!-- One item per row, one sentence each. The columns are not interchangeable: Stop means cease and Less means too much of something, so putting the same item in both to hedge is how a retrospective stops being honest. Add or remove rows as needed. -->

| Start | Stop | Keep | More | Less |
| :---: | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 3. Action Items
<!-- Every action taken from the Start, Stop, More, and Less columns, with one named owner and a review date. Carry each row into the next retrospective and fill in the outcome: an action reviewed only once is an action nobody checked, and a retrospective without an outcome column becomes a ritual rather than a feedback loop. -->

| Action | Owner | By When | Outcome |
| :--- | :--- | :---: | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. FLAP Alternative
<!-- The FLAP alternative to the starfish. If the team prefers FLAP, replace the five starfish columns with Accomplishments, Problems, Lessons, and Future Considerations rather than recording both, since two parallel forms get half-filled and neither is trusted. Delete this section if the team uses the starfish above; do not keep both. -->


---

| Accomplishments | Problems | Lessons | Future Considerations |
| :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

## 5. Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Scrum Master / Facilitator** | {{Scrum_Master_Name}} | _______________________ | [ .... - .... - .... ] |
| **Product Owner** | {{Product_Owner_Name}} | _______________________ | [ .... - .... - .... ] |
| **Team Representative** | {{Team_Representative_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> RETROSPECTIVE | <strong>Ref:</strong> PMO-05.08 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
