---
type: Form
lang: en
layout: default
title: AI Model Card and Fact Sheet
nav_order: 1
token_pointer: /_tokens/forms/en/02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet/02_05_AI_Model_Card_and_Fact_Sheet_Guide.npy
token_count: 3199
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.016567+00:00'
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: AI Model Card and Fact Sheet

**Document Reference:** `PMO-02.05`

This document provides a comprehensive, professional reference to understand
the purpose and effective usage of the **AI Model Card and Fact Sheet** in alignment
with the Tasleemat framework.

---

### 1. What?
A record of one model at one version: what it is, who built it and from what, the settings that affect its behaviour, the licence it may be used under, the tasks it is for and the tasks it must not be used for, each training dataset with its provenance, coverage, licence basis and preprocessing, each evaluation metric with its sample size, subgroup figure, baseline and threshold, the affected groups and the specific ways the model is unfair to them, what it cannot do, what is watched in production, when it is retrained, what changed in this version, and how it will be retired.

---

### 2. Why?
Because a model arrives with no instructions. A weights file, an API endpoint or a vendor's marketing page says what the model can do and nothing about what it cannot, and the people who need the second half are not the people who built the first. Without a card the questions are answered from memory and from documentation written for a different version, and the answers are inconsistent between the engineer, the lawyer and the person the model scores.

The card is also the only artefact that describes the model after the team that built it has moved on. A deployment without a card cannot answer what was in force when an incident occurred, because nothing recorded the version, the threshold or the changes. And the fields that appear empty are the evidence: a card with no known limitations, no subgroup figures and no change record describes a model that has not yet been used, since each of those is filled in by something that happened rather than by something that was decided.

---

### 3. When?
This artifact is primarily prepared, utilized, and updated during the **PROJECT APPROACH AND TAILORING Process Group** of the project lifecycle. It is drafted when the model is built, baselined at the point of release, and revised on every version change, every retraining, and every change to the intended use, since each of those changes what the card should say. It is read at procurement, at approval, at incident review, and by anyone deciding whether to rely on an output.

---

### 4. Who?
**Responsibilities:** Prepared by the AI or ML Lead, who is accountable for the evaluation section and for stating which part of the feasibility was unproven. Reviewed by the Data Protection Officer, who is accountable for the privacy impact and the dataset licence basis, and by legal where the licence terms or the training provenance raise a question the organisation cannot answer alone. Approved by the Project Sponsor. Where the model was acquired rather than built, the sections that cannot be answered are to be marked as unavailable with the supplier asked for them, rather than left blank.

---

### Tailoring Tips
*   A card for a model with no training data of its own, such as a purely prompted configuration, may compress the training-data section, provided the base model, its version and its own card are identified, since the questions then transfer to the base.
*   Where a model is a third-party component embedded in a larger system, the card may be the supplier's, but the deployment record must state the configuration used, because the same model at different settings is a different system.
*   Evaluation figures may be carried forward from a previous version where the training data is unchanged, provided the change to the model is stated, since an unretrained model with a new prompt is not an unretrained model.
*   It is worth recording which sections are unavailable and why, as this is what distinguishes a card describing a model the organisation does not understand from one that has not been filled in.
*   Superseded cards should be retained rather than overwritten, since the question an incident generates is almost always about what was in force at the time.
*   A card may be shorter for an internal low-risk model, but the out-of-scope use, the known limitations and the decommissioning plan should survive any abbreviation, since those three are what a reader needs when deciding whether to rely on an output.

---

### Alignment & Dependencies

#### 1. Pre-requisites & Inputs (Upstream Dependencies)
*   **Mandatory:**
    *   AI Governance Plan (PMO-02.02)
    *   Model Training & Validation Benchmarks
*   **Optional / Contextual:**
    *   Data Privacy & Ethics Assessment (PMO-02.06)
    *   AI Use Case Canvas (PMO-02.04)

#### 2. Downstream Dependents
*   **Mandatory:**
    *   Product Acceptance Form (PMO-06.08)
    *   UAT Sign-off Form (PMO-06.10)
    *   Transition to Operations Checklist (PMO-07.04)
*   **Optional / Contextual:**
    *   Prompt Library Register (PMO-05.09)
    *   Lessons Learned Register (PMO-05.07)

---

### 5. How?
To accurately and professionally complete the **AI MODEL CARD AND FACT SHEET**, the
responsible party must populate the following sections based on the project
context (ensure `parameters.md` is referenced for global project variables):

*   **Model Name and Version:** The model at a specific version, with the date that version was produced. A card that names a model rather than a version describes whichever build happens to be deployed when it is read, and the answer is rarely the one that was assessed.
*   **Developer and Provenance:** Who built it, whether it was trained in-house, fine-tuned, or acquired, and from what base model. Provenance determines which of the sections that follow can be answered at all, and it is usually the section that is missing when a question is asked.
*   **Architecture and Configuration:** The architecture family, the parameter count, and the settings that affect behaviour. The settings are the part that matters, because the same architecture with different decoding parameters is a different system.
*   **Training Method and Compute:** How it was trained, over what period, and at what cost. Compute is recorded because it bounds reproducibility: a result that needed a compute allocation nobody can obtain again is not a result that can be re-derived.
*   **Licence and Usage Terms:** The licence, who may use it, and under what restrictions. A model used outside its licence is a legal exposure that no technical section of this card addresses.
*   **Related Artefacts:** The model, the code, the weights and the data, each with where it lives. A card that lists no locations is a description, and a description cannot be checked against anything.
*   **Primary Use:** The task the model is for, stated as an input and an output. An input and an output can be tested; a purpose cannot.
*   **Secondary Use:** What else it may legitimately be used for, if anything. Recorded separately because a use that is merely tolerated and one that is endorsed need different controls, and a card that lists only the endorsed one hides the tolerated ones.
*   **Out-of-Scope Use:** The uses it must not be used for, with the reason for each. This section is the one that makes the card usable by someone deciding whether to deploy it, and a card without it can only say what the model is for.
*   **User and Audience:** Who operates it, and who is subject to its output. The two are routinely treated as one, and the conflation is how a system that scores applicants comes to be described as a tool that helps recruiters write better.
*   **Operating Conditions:** The inputs it expects, the conditions it was tested under, and the conditions under which it should not be used. These are the boundaries of the evaluation in section 4, and a metric read outside them is not a weaker claim, it is a wrong one.
*   **Human Oversight Requirement:** Where a person must review an output before it is acted on. Oversight specified as a general principle rather than as points in a workflow does not survive contact with a deadline.
*   **Datasets:** Each dataset by name, with its owner and the date it was collected. A dataset named only by type cannot be checked for permission, and permission is what blocks first.
*   **Provenance and Collection Method:** Where each dataset came from and how it was gathered. Collected data carries the practices of the period and place it came from, whether or not those were examined.
*   **Demographic and Geographic Coverage:** Who and where the data represents, and who and where it does not. A dataset that represents a population accurately says so; the field matters because its absence is what allows a model to be applied to a population nobody measured.
*   **Time Period Covered:** The span the data covers, and what happened during it. A model trained on a period of stable conditions inherits the assumption that conditions will remain stable, and the card is where that assumption is written down.
*   **Licence and Consent Basis:** The basis on which each dataset may be used, and whether consent was obtained where it was required. Where consent was not obtained, that is the fact to record, not an absence to leave blank.
*   **Preprocessing and Filtering:** What was removed, resampled or imputed, and on what basis. Filtering is where a dataset acquires the shape of the population the model will then fail on, and it is rarely the step examined.
*   **Known Dataset Limitations:** What the dataset cannot represent. This is the field that prevents a metric from being read as a general claim, and it is almost always empty.
*   **Evaluation Data:** The data the evaluation was run on, and whether it is disjoint from the training data. Disjointness is the first thing to check in any evaluation, and its absence invalidates every number in the section.
*   **Metrics:** Each metric, its value, and the confidence interval or sample size behind it. A single figure with no interval is a point presented as a range, and decisions get made on it.
*   **Performance by Subgroup:** The same metrics for each group the model affects, with the sample size for each. A subgroup figure from a small sample is not a measurement, and the sample size is what distinguishes the two.
*   **Baseline Comparison:** What the model is compared against, and by how much. A model compared only with a trivial baseline can be both better than it and useless.
*   **Threshold and Operating Point:** The threshold in force, and what the alternatives would cost. A model is a set of trade-offs rather than a single system, and the trade-off is only visible once a threshold is fixed.
*   **Evaluation Method and Limitations:** How the evaluation was conducted, by whom, and what it does not establish. An evaluation conducted by the team that built the model is legitimate, and it is a fact that belongs on the card.
*   **Robustness and Failure Modes:** How the model behaves under input it was not tested on, and the known ways it fails. Known failure modes are more useful than a robustness score, because a reader can act on them and cannot act on a score.
*   **Affected Groups:** The groups whose outcomes the model determines, named. Groups described in aggregate on the basis of a test are not the same as the group that performs worst on it.
*   **Known Bias:** The specific ways this model is unfair to this group, stated so that they could be false. A field titled "bias" that says the model may be biased is a heading; "the model scores this group lower on historic completion rates" is a claim that can be measured and can turn out to be wrong.
*   **Safety Risks:** The ways the model could cause harm, by severity, with the conditions under which each arises. Severity is what determines the control, and a risk listed without severity is a list of possibilities.
*   **Dual-Use and Misuse Potential:** How the model could be used to cause harm, and what has been done about it. Relevant to a model that generates as well as one that classifies, and usually unstated.
*   **Environmental and Resource Impact:** The energy and compute consumed, and by whom bears it. Recorded because it is a real cost that appears in no other section, and because it is usually the only figure an external party can verify.
*   **Data Privacy Impact:** What the model can reveal about individuals in its training data, and whether it has been tested for it. Extraction and memorisation are testable, and the test is the only thing that distinguishes a considered answer from an assumption.
*   **Known Limitations:** What the model cannot do, stated plainly. This is the section a reader consults after an incident, and a card that is optimistic in it is a card that will not be consulted a second time.
*   **Out-of-Distribution Behaviour:** How the model behaves on inputs unlike its training data, and whether that has been measured. A model given a population it never saw does not fail loudly, which is what makes this worth recording.
*   **Production Monitoring:** What is watched after deployment, against what baseline, and how often. Drift is a property of the relationship between the model and the world, not of the model, so a launch measurement is the first of a series.
*   **Monitoring Thresholds:** What result triggers action, written before the result is known. A threshold set after seeing a number is a description of that number.
*   **Retraining and Update Policy:** When the model will be retrained, what triggers it, and who approves. Without this the model is updated whenever someone has time, and the change is then invisible to everything above it in this card.
*   **Version Change Record:** What changed between this version and the last, and why. Models change often and silently, and a card with no change record cannot answer what was in force when an incident occurred.
*   **Decommissioning Plan:** How and when the model will be retired, and what happens to the data it holds. A model in production with no retirement plan is a system whose cost grows and whose obligations are never discharged.

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](02_05_AI_Model_Card_and_Fact_Sheet_Template.md)
* [🤖 LLM Generation Prompt](02_05_AI_Model_Card_and_Fact_Sheet.md)
* [📊 Data Structure (JSON)](02_05_AI_Model_Card_and_Fact_Sheet.json)
* [📈 Tabular Data (CSV)](02_05_AI_Model_Card_and_Fact_Sheet.csv)

---

### 6. Reference Example
A fully completed, gold-standard reference example illustrating this artifact in practice is available:
> 📖 **Completed Example:** [02_05_AI_Model_Card_and_Fact_Sheet_Example.md](../../../../examples/en/02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet/02_05_AI_Model_Card_and_Fact_Sheet_Example.md)

</div>
