---
type: Form
lang: en
Form: USER STORY MAPPING CANVAS (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/04_02_09_User_Story_Mapping_Canvas.npy
token_count: 2845
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.945408+00:00'
---

# USER STORY MAPPING CANVAS - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `USER STORY MAPPING CANVAS`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> A story map is a picture of how one person gets something done, and its whole purpose is to make an argument that can be wrong in a visible way. That is what separates it from a backlog, a requirements list or a release plan, all of which record decisions already taken. A map records the reasoning, so a team can disagree with the reasoning before anyone spends a sprint on it. The disagreement is the point: it is much cheaper to move a column on a whiteboard than to unpick a release.

The six sections follow the order the argument is made. Persona establishes who this is for, what they are trying to accomplish in their own framing, what they do today instead, how often, and what it costs them when it goes wrong. The workaround matters more than it looks: a proposal that cannot say what it replaces cannot say what it improves, and every estimate downstream becomes a guess. Frequency is what orders the backbone, because a task done twice a year and a task done twenty times a day do not earn the same place in the sequence, and the map that ignores this orders the work by how interesting it is to build rather than by how much it is needed.

The backbone is the high-level activities in the order the person performs them, and the order is a claim about how the work actually happens. It is the part of the map most often arranged by system architecture instead, which produces a map that describes the software rather than the day, and the difference surfaces as a release nobody wanted. So the map records where the sequence came from: observation, interview, an existing process document, or assumption. A backbone drawn from a process diagram describes how the organisation says the work happens, which is frequently not how anybody does it. The section also records what has been deliberately left off, because a map listing everything is a list of activities and the argument is in the omissions, and where the sequence branches, since a backbone drawn as a single line forces rare paths into the main flow and that is where most of the wasted work in a release comes from.

The slices are where the method either holds or becomes decoration. A column of the map must be a usable increment: every activity in the backbone has something in it, and a user can complete the whole journey using only that column. A step that serves no single activity is a horizontal layer, and a horizontal layer cannot be released on its own because no user can do anything useful with it alone. Teams that get this wrong produce a map that looks like a story map and is in fact a technical layering with the labels changed, and the tell is that no column can be pointed at and described as a thing a person would use. The walking skeleton is the first column built for that reason: the crudest workable version of every activity, end to end, proving the integration rather than the features. It is normally thrown away once it has done its job, which is the reason teams hesitate to build it, and the map says so in advance rather than letting the throwaway look like wasted effort.

Release slicing is where most maps quietly fail. The boundary of the first release is drawn by whether the persona can achieve something they came for, not by what is most valuable, most nearly finished, or easiest to estimate. A release assembled from the easiest columns delivers a set of features and no outcome, and its success is then decided afterwards by whoever feels strongly about it, because a release described by its features has no test. So the map states the outcome as a capability, and records the validation plan before the release, since a validation designed afterwards is a description of whatever was found. Everything deferred gets a reason: later is not a reason, and the real reasons are a dependency, a missing decision, or a risk too large for a first release.

The last two sections keep the map honest. Work the map does not contain is anticipated, because a map that claims completeness sends the work somewhere unrecorded, where it is found later at the worst possible moment. What the product will not do is stated so that it can be said out loud, which is what makes the map safe to publish. The assumptions are listed, because every map rests on beliefs nobody has tested and listing them is the only way to know which to test first. The risks are recorded as triggers rather than as concerns, since a concern has no date and a trigger does. And the map has an owner and a cadence, because a map with neither is a picture of what was understood once, and it is still being shown to people as though it were current.

The value of the form is in the fields that are inconvenient. A map with no stated workaround, no recorded source for the backbone, no deferred slices with reasons, no outcome and no validation plan describes a product nobody has agreed on, because each of those is filled in by something that happened rather than by something that was decided. So the fields to insist on are the ones with no good answer available: what the person does today, where the sequence came from, which slices are out of the first release and why, and what the map assumes. Where a value genuinely is not known, record that it is not known and who must resolve it, which is more useful than a plausible answer, because a plausible answer will be relied on and a declared gap will be closed.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Project Charter (PMO-03.01), Stakeholder Requirements
>   * *Optional:* Product Vision (PMO-03.02), Assumption Log (PMO-03.03)
> * **Downstream Dependents:**
>   * *Mandatory:* Work Breakdown Structure / WBS (PMO-04.02.06), Project Schedule (PMO-04.03.08), Cost Estimates (PMO-04.04.02)
>   * *Optional:* Product Backlog (PMO-04.02.08), Quality Metrics (PMO-04.05.02)

---

## Persona and Problem

### Primary Persona
**Instruction:** The specific person, described so that a team can tell whether a proposed story serves them. A persona written as a role title rather than a person is the reason two teams build different products from the same map and discover the difference at launch.

**Generated value:** [ Add details... ]

### What They Are Trying to Do
**Instruction:** What the person is trying to accomplish, in their own framing, and what they do today instead. The workaround is the baseline: a proposal that cannot say what it replaces cannot say what it improves, and every estimate is then a guess.

**Generated value:** [ Add details... ]

### Frequency and Stakes
**Instruction:** How often the person does this, and what it costs them when it goes wrong. Frequency is what orders the backbone, and stakes are what separate a task worth automating from one worth automating carefully.

**Generated value:** [ Add details... ]

### Organisations and Roles Affected
**Instruction:** Other roles the change touches, including the people who approve, review, or are affected by a decision made from the output. A map that names only the operator will produce a system whose other users are discovered after release.

**Generated value:** [ Add details... ]

## The Backbone

### Activities in Order
**Instruction:** The high-level activities the persona performs, left to right in the order performed. The order is a claim about how the work actually happens, and it is the part of the map most often arranged by system architecture instead, which hides the sequence the person actually experiences.

**Generated value:** [ Add details... ]

### Backbone Source
**Instruction:** How the sequence was established: observation, interview, existing process document, or assumption. A backbone derived from a process diagram describes how the organisation says the work happens, which is not always how anyone does it.

**Generated value:** [ Add details... ]

### Activities Deferred
**Instruction:** Activities the person does that are deliberately not on the map, and why. A map that lists everything is a list of activities; the argument is in what has been left off and what that defers.

**Generated value:** [ Add details... ]

### Optional and Variable Paths
**Instruction:** Where the sequence branches, and which branches are common and which are rare. A backbone drawn as a single line forces rare paths into the main flow, which is where most of the wasted work in a release comes from.

**Generated value:** [ Add details... ]

## The Slices

### Tasks Under Each Activity
**Instruction:** One row per activity, with the specific steps of that activity. A step that serves no single activity is a horizontal layer, and a horizontal layer cannot be released on its own because no user can do anything useful with it.

**Generated value:** [ Add details... ]

### Slices as Vertical Columns
**Instruction:** Each column must be a usable increment: every activity in the backbone has something in it, and a user can complete the whole journey with only that column. This is the defining discipline of the method, and a map that fails it has produced a technical layering dressed as a story map.

**Generated value:** [ Add details... ]

### Walking Skeleton
**Instruction:** The thinnest possible column, end to end, with the crudest workable implementation of every activity. Its purpose is to prove the integration rather than the features, and it is normally thrown away, which is the reason teams hesitate to build it.

**Generated value:** [ Add details... ]

### Slice Sizing Evidence
**Instruction:** What shows each slice is small enough to deliver, such as a timeboxed trial or a measured manual run. An estimate is a claim about a slice nobody has tried, and the first slice is where the estimate is usually wrong.

**Generated value:** [ Add details... ]

## Release Slicing

### MVP Boundary
**Instruction:** Which columns are in the first release and which are not, and the single outcome that release delivers. The boundary is drawn by whether a persona can achieve something they came for, not by what is most valuable or most nearly finished, and a release assembled from the easiest columns delivers nothing anyone wanted.

**Generated value:** [ Add details... ]

### Outcome of the First Release
**Instruction:** What the persona is able to do after it that they could not do before, stated as a capability and not as a list of features. A release described by its features has no test for whether it succeeded, so its success is decided afterwards by whoever feels strongly about it.

**Generated value:** [ Add details... ]

### Validation Plan
**Instruction:** How the first release will be judged, against what, and by whom. Recorded before the release because a validation designed afterwards is a description of whatever was found.

**Generated value:** [ Add details... ]

### Slices Deferred Beyond MVP
**Instruction:** The columns not in the first release, with the reason for each. "Later" is not a reason; the reason is usually a dependency, a missing decision, or a risk too large for a first release.

**Generated value:** [ Add details... ]

## Beyond the First Release

### Later Release Candidates
**Instruction:** Columns considered for subsequent releases, with their dependencies named. A candidate with an unnamed dependency is a wish, and a wish placed on a map is read as a commitment by whoever reads the map next.

**Generated value:** [ Add details... ]

### Emergent Work Anticipated
**Instruction:** Work the map does not contain because it has not been discovered yet, and how new items will be added. A map that claims to be complete invites the work to go somewhere unrecorded instead, which is where it is found later at the worst possible moment.

**Generated value:** [ Add details... ]

### Explicitly Out of Scope
**Instruction:** What this product will not do, stated so it can be said out loud. This is the section that makes the map safe to publish, because an unstated exclusion is discovered by a user rather than by the team.

**Generated value:** [ Add details... ]

## Map Quality and Maintenance

### Assumptions and Unvalidated Beliefs
**Instruction:** What the map takes on trust, and what would have to be true for it to hold. Every map rests on beliefs nobody has tested, and listing them is the only way to know which one to test first.

**Generated value:** [ Add details... ]

### Risks to the Map
**Instruction:** What would force the map to be redrawn, such as a change in regulation, a competitor's launch, or a finding that the real sequence differs. Recorded as triggers rather than as concerns, because a concern has no date and a trigger does.

**Generated value:** [ Add details... ]

### Update Cadence and Owners
**Instruction:** How often the map is revisited, when a change triggers a redraw, and who owns it. A map with no owner and no cadence is a picture of what was understood once, and it is still being shown to people as if it were current.

**Generated value:** [ Add details... ]

### Traceability to Backlog and Release
**Instruction:** How a story on this map reaches the backlog, and what happens when a backlog item contradicts the map. The two are kept in step by a rule and a person, or they diverge quietly and the map stops describing the product.

**Generated value:** [ Add details... ]

---
