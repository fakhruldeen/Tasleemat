<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Documentation</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet/02_05_AI_Model_Card_and_Fact_Sheet_Template.md" target="_blank" rel="noopener noreferrer">🐙 View on GitHub ↗</a>
    <a class="lang-switch-btn" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_05_بطاقة_نموذج_الذكاء_الاصطناعي_قالب.html">🇸🇦 الانتقال للنسخة العربية (Arabic Template) →</a>
  </div>
</div>

<div class="deliverable-header-card">
  <div class="deliverable-badge-row">
    <span class="badge badge-code">PMO-02.05</span>
    <span class="badge badge-phase">02. Project Approach & Tailoring</span>
    <span class="badge badge-standard">PMI PMBOK® 6/7/8 • ISO 21500</span>
  </div>
  <div class="deliverable-nav-pills">
    <a class="nav-pill active" href="#">📋 Blank Template</a>
    <a class="nav-pill" href="../../../guides/en/02_Project_Approach_and_Tailoring/02_05_AI_Model_Card_and_Fact_Sheet_Guide.html">📖 Authoring Guide</a>
    <a class="nav-pill" href="../../../examples/en/02_Project_Approach_and_Tailoring/02_05_AI_Model_Card_and_Fact_Sheet_Example.html">💡 Completed Example</a>
    <a class="nav-pill github-pill" href="https://github.com/fakhruldeen/Tasleemat/blob/main/forms/en/02_Project_Approach_and_Tailoring/05_AI_Model_Card_and_Fact_Sheet/02_05_AI_Model_Card_and_Fact_Sheet_Template.md" target="_blank" rel="noopener noreferrer">🐙 GitHub Source ↗</a>
    <a class="nav-pill lang-pill" href="../../ar/02_منهجية_المشروع_وتخصيصه/02_05_بطاقة_نموذج_الذكاء_الاصطناعي_قالب.html">🇸🇦 النسخة العربية</a>
  </div>
</div>

---

<!--
LLM INSTRUCTIONS: Fill in the [ Add details... ] placeholders based on project context.

Section Instructions:

**1. Model Identification and Provenance**
*   **Model Name and Version:** The model at a specific version, with the date that version was produced. A card that names a model rather than a version describes whichever build happens to be deployed when it is read, and the answer is rarely the one that was assessed.
*   **Developer and Provenance:** Who built it, whether it was trained in-house, fine-tuned, or acquired, and from what base model. Provenance determines which of the sections that follow can be answered at all, and it is usually the section that is missing when a question is asked.
*   **Architecture and Configuration:** The architecture family, the parameter count, and the settings that affect behaviour. The settings are the part that matters, because the same architecture with different decoding parameters is a different system.
*   **Training Method and Compute:** How it was trained, over what period, and at what cost. Compute is recorded because it bounds reproducibility: a result that needed a compute allocation nobody can obtain again is not a result that can be re-derived.
*   **Licence and Usage Terms:** The licence, who may use it, and under what restrictions. A model used outside its licence is a legal exposure that no technical section of this card addresses.
*   **Related Artefacts:** The model, the code, the weights and the data, each with where it lives. A card that lists no locations is a description, and a description cannot be checked against anything.

**2. Intended Use and Out-of-Scope Use**
*   **Primary Use:** The task the model is for, stated as an input and an output. An input and an output can be tested; a purpose cannot.
*   **Secondary Use:** What else it may legitimately be used for, if anything. Recorded separately because a use that is merely tolerated and one that is endorsed need different controls, and a card that lists only the endorsed one hides the tolerated ones.
*   **Out-of-Scope Use:** The uses it must not be used for, with the reason for each. This section is the one that makes the card usable by someone deciding whether to deploy it, and a card without it can only say what the model is for.
*   **User and Audience:** Who operates it, and who is subject to its output. The two are routinely treated as one, and the conflation is how a system that scores applicants comes to be described as a tool that helps recruiters write better.
*   **Operating Conditions:** The inputs it expects, the conditions it was tested under, and the conditions under which it should not be used. These are the boundaries of the evaluation in section 4, and a metric read outside them is not a weaker claim, it is a wrong one.
*   **Human Oversight Requirement:** Where a person must review an output before it is acted on. Oversight specified as a general principle rather than as points in a workflow does not survive contact with a deadline.

**3. Training Data**
*   **Datasets:** Each dataset by name, with its owner and the date it was collected. A dataset named only by type cannot be checked for permission, and permission is what blocks first.
*   **Provenance and Collection Method:** Where each dataset came from and how it was gathered. Collected data carries the practices of the period and place it came from, whether or not those were examined.
*   **Demographic and Geographic Coverage:** Who and where the data represents, and who and where it does not. A dataset that represents a population accurately says so; the field matters because its absence is what allows a model to be applied to a population nobody measured.
*   **Time Period Covered:** The span the data covers, and what happened during it. A model trained on a period of stable conditions inherits the assumption that conditions will remain stable, and the card is where that assumption is written down.
*   **Licence and Consent Basis:** The basis on which each dataset may be used, and whether consent was obtained where it was required. Where consent was not obtained, that is the fact to record, not an absence to leave blank.
*   **Preprocessing and Filtering:** What was removed, resampled or imputed, and on what basis. Filtering is where a dataset acquires the shape of the population the model will then fail on, and it is rarely the step examined.
*   **Known Dataset Limitations:** What the dataset cannot represent. This is the field that prevents a metric from being read as a general claim, and it is almost always empty.

**4. Evaluation and Performance**
*   **Evaluation Data:** The data the evaluation was run on, and whether it is disjoint from the training data. Disjointness is the first thing to check in any evaluation, and its absence invalidates every number in the section.
*   **Metrics:** Each metric, its value, and the confidence interval or sample size behind it. A single figure with no interval is a point presented as a range, and decisions get made on it.
*   **Performance by Subgroup:** The same metrics for each group the model affects, with the sample size for each. A subgroup figure from a small sample is not a measurement, and the sample size is what distinguishes the two.
*   **Baseline Comparison:** What the model is compared against, and by how much. A model compared only with a trivial baseline can be both better than it and useless.
*   **Threshold and Operating Point:** The threshold in force, and what the alternatives would cost. A model is a set of trade-offs rather than a single system, and the trade-off is only visible once a threshold is fixed.
*   **Evaluation Method and Limitations:** How the evaluation was conducted, by whom, and what it does not establish. An evaluation conducted by the team that built the model is legitimate, and it is a fact that belongs on the card.
*   **Robustness and Failure Modes:** How the model behaves under input it was not tested on, and the known ways it fails. Known failure modes are more useful than a robustness score, because a reader can act on them and cannot act on a score.

**5. Ethical, Fairness and Safety Considerations**
*   **Affected Groups:** The groups whose outcomes the model determines, named. Groups described in aggregate on the basis of a test are not the same as the group that performs worst on it.
*   **Known Bias:** The specific ways this model is unfair to this group, stated so that they could be false. A field titled "bias" that says the model may be biased is a heading; "the model scores this group lower on historic completion rates" is a claim that can be measured and can turn out to be wrong.
*   **Safety Risks:** The ways the model could cause harm, by severity, with the conditions under which each arises. Severity is what determines the control, and a risk listed without severity is a list of possibilities.
*   **Dual-Use and Misuse Potential:** How the model could be used to cause harm, and what has been done about it. Relevant to a model that generates as well as one that classifies, and usually unstated.
*   **Environmental and Resource Impact:** The energy and compute consumed, and by whom bears it. Recorded because it is a real cost that appears in no other section, and because it is usually the only figure an external party can verify.
*   **Data Privacy Impact:** What the model can reveal about individuals in its training data, and whether it has been tested for it. Extraction and memorisation are testable, and the test is the only thing that distinguishes a considered answer from an assumption.

**6. Limitations, Monitoring and Change Control**
*   **Known Limitations:** What the model cannot do, stated plainly. This is the section a reader consults after an incident, and a card that is optimistic in it is a card that will not be consulted a second time.
*   **Out-of-Distribution Behaviour:** How the model behaves on inputs unlike its training data, and whether that has been measured. A model given a population it never saw does not fail loudly, which is what makes this worth recording.
*   **Production Monitoring:** What is watched after deployment, against what baseline, and how often. Drift is a property of the relationship between the model and the world, not of the model, so a launch measurement is the first of a series.
*   **Monitoring Thresholds:** What result triggers action, written before the result is known. A threshold set after seeing a number is a description of that number.
*   **Retraining and Update Policy:** When the model will be retrained, what triggers it, and who approves. Without this the model is updated whenever someone has time, and the change is then invisible to everything above it in this card.
*   **Version Change Record:** What changed between this version and the last, and why. Models change often and silently, and a card with no change record cannot answer what was in force when an incident occurred.
*   **Decommissioning Plan:** How and when the model will be retired, and what happens to the data it holds. A model in production with no retirement plan is a system whose cost grows and whose obligations are never discharged.
-->

<h3 dir="ltr" align="right">{{Company_Name}}</h3>
<h2 dir="ltr" align="right">{{Governance_Scope}} - {{Framework_ID}}</h2>
<h1 dir="ltr" align="center">AI MODEL CARD AND FACT SHEET</h1>

| **Date Prepared:** {{Current_Date}} | **Compliance Officer:** {{Compliance_Officer_Name}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- | :--- |

---

## 1. Model Identification and Provenance
<!-- What the model is at a specific version, who built it and from what, the settings that affect its behaviour, what it may be used under, and where the artefacts live. -->

**Model Name and Version:** [ Add details... ]

**Developer and Provenance:** [ Add details... ]

**Architecture and Configuration:** [ Add details... ]

**Training Method and Compute:** [ Add details... ]

**Licence and Usage Terms:** [ Add details... ]

**Related Artefacts:** [ Add details... ]

---

## 2. Intended Use and Out-of-Scope Use
<!-- The task as an input and an output, what else it may be used for, what it must not be used for, who operates it and who it acts upon, and the conditions under which its metrics hold. -->

**Primary Use:** [ Add details... ]

**Secondary Use:** [ Add details... ]

**Out-of-Scope Use:** [ Add details... ]

**User and Audience:** [ Add details... ]

**Operating Conditions:** [ Add details... ]

**Human Oversight Requirement:** [ Add details... ]

---

## 3. Training Data
<!-- One row per dataset: what it is and who owns it, where it came from, whom and where it represents, when it covers, on what basis it may be used, what was done to it, and what it cannot represent. -->

| Dataset | Provenance and Collection | Demographic and Geographic Coverage | Time Period Covered | Licence and Consent Basis | Preprocessing and Filtering | Known Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 4. Evaluation and Performance
<!-- One row per metric: what it is measured on, its value with the sample size behind it, the same figure for each affected group, the baseline it beats, the threshold in force, and what the method does not establish. -->

| Metric | Evaluation Data and Disjointness | Value and Sample Size | Performance by Subgroup | Baseline Comparison | Threshold in Force | Method Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 5. Ethical, Fairness and Safety Considerations
<!-- One row per consideration: which group is affected, the specific way this model is unfair, the harm it could cause and its severity, how it could be misused, what it can reveal, and its resource cost. -->

| Consideration | Groups Affected | Specific Finding | Severity | What Was Done |
| :--- | :--- | :--- | :---: | :--- |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |
| [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] | [ Add details... ] |

---

## 6. Limitations, Monitoring and Change Control
<!-- What the model cannot do, how it behaves off-distribution, what is watched in production, what triggers action, when it is retrained, what changed in this version, and how it will be retired. -->

**Known Limitations:** [ Add details... ]

**Out-of-Distribution Behaviour:** [ Add details... ]

**Production Monitoring:** [ Add details... ]

**Monitoring Thresholds:** [ Add details... ]

**Retraining and Update Policy:** [ Add details... ]

**Version Change Record:** [ Add details... ]

**Decommissioning Plan:** [ Add details... ]

---

### Sign-off and Approvals

| Role | Name | Signature | Date |
| :--- | :--- | :---: | :---: |
| **Model Developer / ML Lead** | {{ML_Lead_Name}} | _______________________ | [ .... - .... - .... ] |
| **AI Ethics / QA Reviewer** | {{QA_Reviewer_Name}} | _______________________ | [ .... - .... - .... ] |
| **Product Owner** | {{Product_Owner_Name}} | _______________________ | [ .... - .... - .... ] |
---

<div dir="ltr" align="right" style="margin-top: 20px; font-size: 12px; color: #7f8c8d;" markdown="1">
  <strong>Template:</strong> AI MODEL CARD AND FACT SHEET | <strong>Ref:</strong> PMO-02.05 <br>
  <i>Generated on: {{Current_Timestamp}}, by <a href="https://github.com/fakhruldeen/Tasleemat/" style="color: #7f8c8d;">Tasleemat</a></i>
</div>
