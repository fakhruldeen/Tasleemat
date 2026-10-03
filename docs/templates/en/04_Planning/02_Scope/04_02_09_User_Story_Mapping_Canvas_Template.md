<div class="lang-switch-bar">
  <span>🌐 Dual Language / ثنائي اللغة:</span>
  <a class="lang-switch-btn" href="../../../ar/04_التخطيط/02_النطاق/04_02_09_نموذج_تخطيط_قصص_المستخدم_قالب.md">🇸🇦 الانتقال للقالب بالعربية (Arabic Template)</a>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-04.02.09</span>
    <span class="badge badge-phase">04. Planning</span>
    <span class="badge badge-standard">PMI PMBOK® 6/7/8 • ISO 21500</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill active" href="#">📋 Blank Template</a>
    <a class="nav-pill" href="../../../../guides/en/04_Planning/02_Scope/04_02_09_User_Story_Mapping_Canvas_Guide.md">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../../examples/en/04_Planning/02_Scope/04_02_09_User_Story_Mapping_Canvas_Example.md">💡 Completed Example</a>
    <a class="nav-pill lang-pill" href="../../../ar/04_التخطيط/02_النطاق/04_02_09_نموذج_تخطيط_قصص_المستخدم_قالب.md">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

<!--
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Section Instructions:

**1. Persona and Problem**
*   **Primary Persona:** The specific person, described so that a team can tell whether a proposed story serves them. A persona written as a role title rather than a person is the reason two teams build different products from the same map and discover the difference at launch.
*   **What They Are Trying to Do:** What the person is trying to accomplish, in their own framing, and what they do today instead. The workaround is the baseline: a proposal that cannot say what it replaces cannot say what it improves, and every estimate is then a guess.
*   **Frequency and Stakes:** How often the person does this, and what it costs them when it goes wrong. Frequency is what orders the backbone, and stakes are what separate a task worth automating from one worth automating carefully.
*   **Organisations and Roles Affected:** Other roles the change touches, including the people who approve, review, or are affected by a decision made from the output. A map that names only the operator will produce a system whose other users are discovered after release.

**2. The Backbone**
*   **Activities in Order:** The high-level activities the persona performs, left to right in the order performed. The order is a claim about how the work actually happens, and it is the part of the map most often arranged by system architecture instead, which hides the sequence the person actually experiences.
*   **Backbone Source:** How the sequence was established: observation, interview, existing process document, or assumption. A backbone derived from a process diagram describes how the organisation says the work happens, which is not always how anyone does it.
*   **Activities Deferred:** Activities the person does that are deliberately not on the map, and why. A map that lists everything is a list of activities; the argument is in what has been left off and what that defers.
*   **Optional and Variable Paths:** Where the sequence branches, and which branches are common and which are rare. A backbone drawn as a single line forces rare paths into the main flow, which is where most of the wasted work in a release comes from.

**3. The Slices**
*   **Tasks Under Each Activity:** One row per activity, with the specific steps of that activity. A step that serves no single activity is a horizontal layer, and a horizontal layer cannot be released on its own because no user can do anything useful with it.
*   **Slices as Vertical Columns:** Each column must be a usable increment: every activity in the backbone has something in it, and a user can complete the whole journey with only that column. This is the defining discipline of the method, and a map that fails it has produced a technical layering dressed as a story map.
*   **Walking Skeleton:** The thinnest possible column, end to end, with the crudest workable implementation of every activity. Its purpose is to prove the integration rather than the features, and it is normally thrown away, which is the reason teams hesitate to build it.
*   **Slice Sizing Evidence:** What shows each slice is small enough to deliver, such as a timeboxed trial or a measured manual run. An estimate is a claim about a slice nobody has tried, and the first slice is where the estimate is usually wrong.

**4. Release Slicing**
*   **MVP Boundary:** Which columns are in the first release and which are not, and the single outcome that release delivers. The boundary is drawn by whether a persona can achieve something they came for, not by what is most valuable or most nearly finished, and a release assembled from the easiest columns delivers nothing anyone wanted.
*   **Outcome of the First Release:** What the persona is able to do after it that they could not do before, stated as a capability and not as a list of features. A release described by its features has no test for whether it succeeded, so its success is decided afterwards by whoever feels strongly about it.
*   **Validation Plan:** How the first release will be judged, against what, and by whom. Recorded before the release because a validation designed afterwards is a description of whatever was found.
*   **Slices Deferred Beyond MVP:** The columns not in the first release, with the reason for each. "Later" is not a reason; the reason is usually a dependency, a missing decision, or a risk too large for a first release.

**5. Beyond the First Release**
*   **Later Release Candidates:** Columns considered for subsequent releases, with their dependencies named. A candidate with an unnamed dependency is a wish, and a wish placed on a map is read as a commitment by whoever reads the map next.
*   **Emergent Work Anticipated:** Work the map does not contain because it has not been discovered yet, and how new items will be added. A map that claims to be complete invites the work to go somewhere unrecorded instead, which is where it is found later at the worst possible moment.
*   **Explicitly Out of Scope:** What this product will not do, stated so it can be said out loud. This is the section that makes the map safe to publish, because an unstated exclusion is discovered by a user rather than by the team.

**6. Map Quality and Maintenance**
*   **Assumptions and Unvalidated Beliefs:** What the map takes on trust, and what would have to be true for it to hold. Every map rests on beliefs nobody has tested, and listing them is the only way to know which one to test first.
*   **Risks to the Map:** What would force the map to be redrawn, such as a change in regulation, a competitor's launch, or a finding that the real sequence differs. Recorded as triggers rather than as concerns, because a concern has no date and a trigger does.
*   **Update Cadence and Owners:** How often the map is revisited, when a change triggers a redraw, and who owns it. A map with no owner and no cadence is a picture of what was understood once, and it is still being shown to people as if it were current.
*   **Traceability to Backlog and Release:** How a story on this map reaches the backlog, and what happens when a backlog item contradicts the map. The two are kept in step by a rule and a person, or they diverge quietly and the map stops describing the product.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Project_Name}} - {{Project_ID}}</h2>
<h1 dir="ltr" align="center">USER STORY MAPPING CANVAS</h1>

| **Date Prepared:** {{Current_Date}} | **Project Manager:** {{Project_Manager_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |
---

## 1. Persona and Problem
<!-- Who this is for, what they are trying to do, how often they do it, what it costs them, and who else the change touches. -->

**Primary Persona:** [ Add details... ]

**What They Are Trying to Do:** [ Add details... ]

**Frequency and Stakes:** [ Add details... ]

**Organisations and Roles Affected:** [ Add details... ]

---

## 2. The Backbone
<!-- The high-level activities in the order they are performed, where that order came from, what is deliberately not on the map, and where the sequence branches. -->

**Activities in Order:**

| # | Activity | Purpose for the Persona | Source of Evidence |
| :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

**Backbone Source:** [ Add details... ]

**Activities Deferred:** [ Add details... ]

**Optional and Variable Paths:** [ Add details... ]

---

## 3. The Slices
<!-- The steps under each activity, one row per activity, so that each column is a usable increment rather than a horizontal layer. -->

**Tasks Under Each Activity:**

| Activity | Step 1 | Step 2 | Step 3 | Vertical Slice Complete |
| :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

**Slices as Vertical Columns:** [ Add details... ]

**Walking Skeleton:** [ Add details... ]

**Slice Sizing Evidence:** [ Add details... ]

---

## 4. Release Slicing
<!-- Where the first-release line falls, what the persona can then do, how that will be judged, and which columns were left out and why. -->

**MVP Boundary:** [ Add details... ]

**Outcome of the First Release:** [ Add details... ]

**Validation Plan:** [ Add details... ]

**Slices Deferred Beyond MVP:** [ Add details... ]

---

## 5. Beyond the First Release
<!-- Columns considered later with their dependencies, work the map does not yet contain, and what this product will not do. -->

**Later Release Candidates:** [ Add details... ]

**Emergent Work Anticipated:** [ Add details... ]

**Explicitly Out of Scope:** [ Add details... ]

---

## 6. Map Quality and Maintenance
<!-- What the map takes on trust, what would force it to be redrawn, who owns it and how often it is revisited, and how it reaches the backlog. -->

**Assumptions and Unvalidated Beliefs:** [ Add details... ]

**Risks to the Map:** [ Add details... ]

**Update Cadence and Owners:** [ Add details... ]

**Traceability to Backlog and Release:** [ Add details... ]

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :--- | :--- |
| **Product Owner** | {{Product_Owner_Name}} | _______________________ | [ .... - .... - .... ] |
| **UX / BA Lead** | {{UX_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **Development Team Lead** | {{Dev_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;">
  <strong>Template:</strong> USER STORY MAPPING CANVAS | <strong>Ref:</strong> PMO-04.02.09 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
