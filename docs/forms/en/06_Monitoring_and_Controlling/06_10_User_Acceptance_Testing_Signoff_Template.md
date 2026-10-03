<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/06_Monitoring_and_Controlling/10_User_Acceptance_Testing_Signoff/06_10_User_Acceptance_Testing_Signoff_Template.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../ar/06_المراقبة_والتحكم/06_10_نموذج_اعتماد_اختبار_قبول_المستخدم_(UAT)_قالب.html">🇸🇦 الانتقال للنسخة العربية (Arabic Template) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-06.10</span>
    <span class="badge badge-phase">06. Monitoring & Controlling</span>
    <span class="badge badge-standard">PMI PMBOK® 6/7/8 • ISO 21500</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill active" href="#">📋 Blank Template</a>
    <a class="nav-pill" href="../../../guides/en/06_Monitoring_and_Controlling/06_10_User_Acceptance_Testing_Signoff_Guide.html">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/06_Monitoring_and_Controlling/06_10_User_Acceptance_Testing_Signoff_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/06_Monitoring_and_Controlling/10_User_Acceptance_Testing_Signoff/06_10_User_Acceptance_Testing_Signoff_Template.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../ar/06_المراقبة_والتحكم/06_10_نموذج_اعتماد_اختبار_قبول_المستخدم_(UAT)_قالب.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

<!-- LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Context and Definition:
A user acceptance testing signoff records a decision rather than a test
report. The testing was performed and written up elsewhere; what this
document holds is the business's agreement that the thing tested is the
thing they asked for.

It is the only artifact in this set that cannot be taken back quietly.
Development testing continues past a failure, and a failed unit test is
ordinary. Acceptance means the business has signed, and once that happens
the project moves to the next phase and the outstanding findings stop being
worked on.

The two sections that carry the form are the criteria and the known
defects. The criteria have to exist before the testing, or the result
describes an outcome rather than confirming a decision. The defects are
recorded rather than resolved because that is the deliberate trade: a
critical defect blocks acceptance, and a non-critical one is accepted
knowingly, by somebody who has the authority to accept it and who will
still be there after go-live.

It can receive information from:
*   The test plan and the test cases executed against it
*   The defect log, which is where anything found is already recorded
*   The requirements or acceptance criteria the build was measured against

It provides information to:
*   Product acceptance form, which records the same decision for the deliverable
*   Project closure or phase closure, which needs the acceptance date
*   Transition to operations checklist, which is gated on this signature

Tailoring Tips:
*   Agree the criteria before the testing starts. Criteria written afterwards
    describe what happened rather than deciding whether it was acceptable.
*   Record what was accepted, not only what passed. An empty defects section
    tells the reader the testing found nothing, and a reader who suspects that
    has no way to check it.
*   Say which build and which environment. A pass somewhere other than where
    the business will work is not a pass, and the signature does not carry that
    distinction.

Alignment:
The user acceptance testing signoff should be aligned and consistent with:
*   The test plan, because the signoff is against the cases the plan defines
*   Product acceptance form, which records the same decision at deliverable level
*   Transition to operations checklist, which cannot start until this is signed

Section Instructions:
*   Test Summary: what was tested, named specifically enough that the criteria
    below can be read against something.
*   Testing Environment: where the testing ran and against which build.
*   Pass/Fail Criteria: what was decided before the testing began.
*   Known Defects: what was found and accepted rather than fixed, with severity
    and who accepted it.
*   Business Owner Sign-off: the decision in the business's own terms, covering
    what is accepted, with what, and what happens if it does not work.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 dir="ltr" align="center">USER ACCEPTANCE TESTING SIGNOFF</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- | :--- |

---

## Acceptance Record

### Test Summary

[ Add details... ]

---

### Testing Environment

[ Add details... ]

---

### Pass/Fail Criteria

[ Add details... ]

---

### Known Defects

[ Add details... ]

---

### Business Owner Sign-off

[ Add details... ]

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Quality Assurance (QA) Manager** | {{QA_Manager_Name}} | _______________________ | [ .... - .... - .... ] |
| **Product Owner** | {{Product_Owner_Name}} | _______________________ | [ .... - .... - .... ] |
| **Client Representative / Business Owner** | {{Client_Representative_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;" markdown="1">
  <strong>Template:</strong> USER ACCEPTANCE TESTING SIGNOFF | <strong>Ref:</strong> PMO-06.10 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
