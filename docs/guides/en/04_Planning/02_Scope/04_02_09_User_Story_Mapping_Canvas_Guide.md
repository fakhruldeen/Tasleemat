<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/04_02_09_User_Story_Mapping_Canvas_Guide.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../../ar/04_التخطيط/02_النطاق/04_02_09_نموذج_تخطيط_قصص_المستخدم_دليل.html">🇸🇦 الانتقال للدليل بالعربية (Arabic Guide) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-04.02.09</span>
    <span class="badge badge-phase">04. Planning</span>
    <span class="badge badge-type">Authoring & Governance Guide</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill" href="../../../../forms/en/04_Planning/02_Scope/04_02_09_User_Story_Mapping_Canvas_Template.html">📋 Blank Template</a>
    <a class="nav-pill active" href="#">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../../examples/en/04_Planning/02_Scope/04_02_09_User_Story_Mapping_Canvas_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/04_02_09_User_Story_Mapping_Canvas_Guide.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../../ar/04_التخطيط/02_النطاق/04_02_09_نموذج_تخطيط_قصص_المستخدم_دليل.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

---
type: Form
lang: en
layout: default
title: User Story Mapping Canvas
nav_order: 1
token_pointer: /_tokens/forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/04_02_09_User_Story_Mapping_Canvas_Guide.npy
token_count: 2861
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.944551+00:00'
form_id: PMO-04.02.09
status: approved
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;" markdown="1">

## Tasleemat Forms Guide
# Project Artifact: User Story Mapping Canvas

**Document Reference:** `PMO-04.02.09`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **User Story Mapping Canvas** in alignment
with the Tasleemat framework.

---

### 1. What?
A picture of how one person gets something done, and the reasoning behind
it: who that person is, what they are trying to accomplish, what they do
today instead, how often they do it and what it costs them, and which other
roles the change touches. Then the high-level activities in the order they
are performed, where that order came from, what has been deliberately left
off, and where the sequence branches. Then the steps under each activity, one
row per activity so that every column of the map is a usable increment rather
than a horizontal layer, the walking skeleton that proves the integration, and
what shows each slice is small enough to deliver. Then where the first-release
line falls, what the person can then do, how that will be judged, and which
slices were deferred and why. Then the later candidates with their
dependencies, the work the map does not yet contain, what the product will
not do, what the map assumes, what would force it to be redrawn, and who owns
it.

---

### 2. Why?
Because a backlog records decisions already taken and a map records the
reasoning, which is the part that can still be argued with. The disagreement
is the point: it is much cheaper to move a column on a whiteboard than to
unpick a release. The map is also the artefact that makes a wrong assumption
visible while it is still cheap, which a requirements list cannot do, because
by the time a requirement is written the assumption has been built into it.

The fields that appear empty are the evidence. A map with no stated
workaround, no recorded source for the backbone, no deferred slices with
reasons, no outcome and no validation plan describes a product nobody has
agreed on, since each of those is filled in by something that happened
rather than by something that was decided. A backbone drawn from an existing
process diagram describes how the organisation says the work happens, which
is frequently not how anybody does it, and a map ordered by system
architecture describes the software rather than the day. A release boundary
drawn by what is easiest to estimate delivers a set of features and no
outcome, and a release described by its features has no test for whether it
succeeded, so its success is decided afterwards by whoever feels strongly
about it.

---

### 3. When?
This artifact is primarily prepared, utilized, and updated during the
**PLANNING Process Group** of the project lifecycle. It is drafted before
the backlog is committed to, revised whenever the persona, the workaround or
the sequence changes, whenever a release boundary is drawn or moved, and
whenever new work arrives that the map does not contain. It is read at
backlog refinement, at release planning, and by anyone proposing a story,
who needs to know which column it would sit in and whether that column is
already scheduled.

---

### 4. Who?
**Responsibilities:** Prepared by the Product Owner, who is accountable for
the persona and for the first-release boundary, since the boundary is a
decision about what the product is for. Reviewed by the Business Analyst,
who is accountable for the backbone sequence and for where its evidence came
from, and by the UX practitioner who observed the workaround. Approved by the
Business Owner, who confirms the persona is the one whose problem is worth
solving. Where a column has no stated dependency or a deferred slice has no
reason, record that rather than leaving the cell empty, since an empty cell
on a map is read as a decision by whoever reads the map next.

---

### Tailoring Tips
*   A map for a single well-understood persona may omit the persona section
    beyond a sentence, but the workaround and the frequency should survive,
    since they are what order the backbone and what justify building
    anything.
*   Where a team already maintains a mature backlog, the map may be used
    retrospectively to test whether the backlog is vertical, provided the
    test is applied honestly; a backlog that turns out to be horizontal is a
    finding, and the map is the only artefact that will show it.
*   The walking skeleton may be run against real data in a trial, provided
    the trial is bounded and the data handled accordingly, since the point
    is to prove the integration and a real trial proves more.
*   Slices may be split across releases where a single column is too large,
    provided each part remains usable on its own; a column cut in half across
    two releases has reintroduced the horizontal layer.
*   It is worth recording which activities were considered and left off the
    backbone, as this is what distinguishes a considered map from an
    incomplete one.
*   A map for an internal tool with one user may be a single row, but it
    should still state what that person does today, since a tool with no
    stated workaround is usually solving a problem nobody has.
*   Superseded maps should be retained rather than overwritten, since the
    question a team argues about later is almost always what was believed at
    the time.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   Project Charter (PMO-03.01)
    *   Stakeholder Requirements
*   **Optional / Contextual:**
    *   Product Vision (PMO-03.02)
    *   Assumption Log (PMO-03.03)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Work Breakdown Structure / WBS (PMO-04.02.06)
    *   Project Schedule (PMO-04.03.08)
    *   Cost Estimates (PMO-04.04.02)
*   **Optional / Contextual:**
    *   Product Backlog (PMO-04.02.08)
    *   Quality Metrics (PMO-04.05.02)

---

### 5. How?
To accurately and professionally complete the **USER STORY MAPPING CANVAS**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Primary Persona:** The specific person, described so that a team can tell whether a proposed story serves them. A persona written as a role title rather than a person is the reason two teams build different products from the same map and discover the difference at launch.
*   **What They Are Trying to Do:** What the person is trying to accomplish, in their own framing, and what they do today instead. The workaround is the baseline: a proposal that cannot say what it replaces cannot say what it improves, and every estimate is then a guess.
*   **Frequency and Stakes:** How often the person does this, and what it costs them when it goes wrong. Frequency is what orders the backbone, and stakes are what separate a task worth automating from one worth automating carefully.
*   **Organisations and Roles Affected:** Other roles the change touches, including the people who approve, review, or are affected by a decision made from the output. A map that names only the operator will produce a system whose other users are discovered after release.
*   **Activities in Order:** The high-level activities the persona performs, left to right in the order performed. The order is a claim about how the work actually happens, and it is the part of the map most often arranged by system architecture instead, which hides the sequence the person actually experiences.
*   **Backbone Source:** How the sequence was established: observation, interview, existing process document, or assumption. A backbone derived from a process diagram describes how the organisation says the work happens, which is not always how anyone does it.
*   **Activities Deferred:** Activities the person does that are deliberately not on the map, and why. A map that lists everything is a list of activities; the argument is in what has been left off and what that defers.
*   **Optional and Variable Paths:** Where the sequence branches, and which branches are common and which are rare. A backbone drawn as a single line forces rare paths into the main flow, which is where most of the wasted work in a release comes from.
*   **Tasks Under Each Activity:** One row per activity, with the specific steps of that activity. A step that serves no single activity is a horizontal layer, and a horizontal layer cannot be released on its own because no user can do anything useful with it.
*   **Slices as Vertical Columns:** Each column must be a usable increment: every activity in the backbone has something in it, and a user can complete the whole journey with only that column. This is the defining discipline of the method, and a map that fails it has produced a technical layering dressed as a story map.
*   **Walking Skeleton:** The thinnest possible column, end to end, with the crudest workable implementation of every activity. Its purpose is to prove the integration rather than the features, and it is normally thrown away, which is the reason teams hesitate to build it.
*   **Slice Sizing Evidence:** What shows each slice is small enough to deliver, such as a timeboxed trial or a measured manual run. An estimate is a claim about a slice nobody has tried, and the first slice is where the estimate is usually wrong.
*   **MVP Boundary:** Which columns are in the first release and which are not, and the single outcome that release delivers. The boundary is drawn by whether a persona can achieve something they came for, not by what is most valuable or most nearly finished, and a release assembled from the easiest columns delivers nothing anyone wanted.
*   **Outcome of the First Release:** What the persona is able to do after it that they could not do before, stated as a capability and not as a list of features. A release described by its features has no test for whether it succeeded, so its success is decided afterwards by whoever feels strongly about it.
*   **Validation Plan:** How the first release will be judged, against what, and by whom. Recorded before the release because a validation designed afterwards is a description of whatever was found.
*   **Slices Deferred Beyond MVP:** The columns not in the first release, with the reason for each. "Later" is not a reason; the reason is usually a dependency, a missing decision, or a risk too large for a first release.
*   **Later Release Candidates:** Columns considered for subsequent releases, with their dependencies named. A candidate with an unnamed dependency is a wish, and a wish placed on a map is read as a commitment by whoever reads the map next.
*   **Emergent Work Anticipated:** Work the map does not contain because it has not been discovered yet, and how new items will be added. A map that claims to be complete invites the work to go somewhere unrecorded instead, which is where it is found later at the worst possible moment.
*   **Explicitly Out of Scope:** What this product will not do, stated so it can be said out loud. This is the section that makes the map safe to publish, because an unstated exclusion is discovered by a user rather than by the team.
*   **Assumptions and Unvalidated Beliefs:** What the map takes on trust, and what would have to be true for it to hold. Every map rests on beliefs nobody has tested, and listing them is the only way to know which one to test first.
*   **Risks to the Map:** What would force the map to be redrawn, such as a change in regulation, a competitor's launch, or a finding that the real sequence differs. Recorded as triggers rather than as concerns, because a concern has no date and a trigger does.
*   **Update Cadence and Owners:** How often the map is revisited, when a change triggers a redraw, and who owns it. A map with no owner and no cadence is a picture of what was understood once, and it is still being shown to people as if it were current.
*   **Traceability to Backlog and Release:** How a story on this map reaches the backlog, and what happens when a backlog item contradicts the map. The two are kept in step by a rule and a person, or they diverge quietly and the map stops describing the product.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](../../../../forms/en/04_Planning/02_Scope/04_02_09_User_Story_Mapping_Canvas_Template.md)
* [🤖 LLM Generation Prompt](https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/04_02_09_User_Story_Mapping_Canvas.md)
* [📊 Data Structure (JSON)](https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/04_02_09_User_Story_Mapping_Canvas.json)
* [📈 Tabular Data (CSV)](https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/04_02_09_User_Story_Mapping_Canvas.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [04_02_09_User_Story_Mapping_Canvas_Example.md](../../../../examples/en/04_Planning/02_Scope/04_02_09_User_Story_Mapping_Canvas_Example.md)

</div>
