---
lang: en
Form: AI GOVERNANCE PLAN (Instructions)
---

# AI GOVERNANCE PLAN - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the
> `AI GOVERNANCE PLAN`. When asked to populate this form, use the guidance
> provided for each section below to accurately generate the required
> content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> A model card is the document that answers the question a person asks when they have been handed a model and told to use it: what is this, what was it built from, what does it do well, what does it fail at, and what am I not allowed to do with it. That question arrives from engineering, from legal, from the data protection officer and from the person who will be affected by the output, and they need different halves of the same answer. The card is what stops four documents being written separately and disagreeing.

The six sections follow the order those questions arrive. Identification records the model at a version rather than a name, because a card that names a model describes whichever build is deployed when it is read, and the answer is rarely the one that was assessed; it also records licence and where the artefacts live, since a card with no locations is a description that cannot be checked against anything. Intended use separates the endorsed use from the tolerated one and from the refused one, records the operating conditions under which the evaluation in section 4 holds, and names the points at which a human must review an output. Training data records each dataset by name and owner, whom and where it represents, the period it covers, the basis on which it may be used, and what preprocessing did to it, since filtering is where a dataset acquires the shape of the population the model will later fail on. Evaluation records the disjointness of the test set first, because its absence invalidates every figure in the section, then each metric with its sample size, the same figure by subgroup, the baseline, and the threshold in force, since a model is a set of trade-offs rather than a single system. Ethical and safety considerations name the affected groups and the specific way the model is unfair to them, stated so that they could be false. Limitations and change control record what the model cannot do, what is watched after deployment, what triggers action, when it is retrained, what changed in this version, and how it will be retired.

The card's value is entirely in the fields that are inconvenient. A model card with no out-of-scope use, no known limitations, no subgroup figures and no change record describes a model that has not been used, because every one of those fields is filled in by something that happened. So the fields to insist on are the ones with no good answer available: the subgroup figure with its sample size, the threshold and what the alternatives would cost, the known dataset limitations, the out-of-distribution behaviour, and the decommissioning plan. Where a value genuinely is not known, record that it is not known and who must resolve it, which is more useful than a plausible figure, because a plausible figure will be relied on and a declared gap will be closed.

> **Alignment:**
> This AI governance plan must be consistent with: AI use case canvas, AI governance plan, data privacy and ethics assessment, risk management plan.

---

## Model Identification and Provenance

### Model Name and Version
**Instruction:** The model at a specific version, with the date that version was produced. A card that names a model rather than a version describes whichever build happens to be deployed when it is read, and the answer is rarely the one that was assessed.

**Generated value:** [ Add details... ]

### Developer and Provenance
**Instruction:** Who built it, whether it was trained in-house, fine-tuned, or acquired, and from what base model. Provenance determines which of the sections that follow can be answered at all, and it is usually the section that is missing when a question is asked.

**Generated value:** [ Add details... ]

### Architecture and Configuration
**Instruction:** The architecture family, the parameter count, and the settings that affect behaviour. The settings are the part that matters, because the same architecture with different decoding parameters is a different system.

**Generated value:** [ Add details... ]

### Training Method and Compute
**Instruction:** How it was trained, over what period, and at what cost. Compute is recorded because it bounds reproducibility: a result that needed a compute allocation nobody can obtain again is not a result that can be re-derived.

**Generated value:** [ Add details... ]

### Licence and Usage Terms
**Instruction:** The licence, who may use it, and under what restrictions. A model used outside its licence is a legal exposure that no technical section of this card addresses.

**Generated value:** [ Add details... ]

### Related Artefacts
**Instruction:** The model, the code, the weights and the data, each with where it lives. A card that lists no locations is a description, and a description cannot be checked against anything.

**Generated value:** [ Add details... ]

## Intended Use and Out-of-Scope Use

### Primary Use
**Instruction:** The task the model is for, stated as an input and an output. An input and an output can be tested; a purpose cannot.

**Generated value:** [ Add details... ]

### Secondary Use
**Instruction:** What else it may legitimately be used for, if anything. Recorded separately because a use that is merely tolerated and one that is endorsed need different controls, and a card that lists only the endorsed one hides the tolerated ones.

**Generated value:** [ Add details... ]

### Out-of-Scope Use
**Instruction:** The uses it must not be used for, with the reason for each. This section is the one that makes the card usable by someone deciding whether to deploy it, and a card without it can only say what the model is for.

**Generated value:** [ Add details... ]

### User and Audience
**Instruction:** Who operates it, and who is subject to its output. The two are routinely treated as one, and the conflation is how a system that scores applicants comes to be described as a tool that helps recruiters write better.

**Generated value:** [ Add details... ]

### Operating Conditions
**Instruction:** The inputs it expects, the conditions it was tested under, and the conditions under which it should not be used. These are the boundaries of the evaluation in section 4, and a metric read outside them is not a weaker claim, it is a wrong one.

**Generated value:** [ Add details... ]

### Human Oversight Requirement
**Instruction:** Where a person must review an output before it is acted on. Oversight specified as a general principle rather than as points in a workflow does not survive contact with a deadline.

**Generated value:** [ Add details... ]

## Training Data

### Datasets
**Instruction:** Each dataset by name, with its owner and the date it was collected. A dataset named only by type cannot be checked for permission, and permission is what blocks first.

**Generated value:** [ Add details... ]

### Provenance and Collection Method
**Instruction:** Where each dataset came from and how it was gathered. Collected data carries the practices of the period and place it came from, whether or not those were examined.

**Generated value:** [ Add details... ]

### Demographic and Geographic Coverage
**Instruction:** Who and where the data represents, and who and where it does not. A dataset that represents a population accurately says so; the field matters because its absence is what allows a model to be applied to a population nobody measured.

**Generated value:** [ Add details... ]

### Time Period Covered
**Instruction:** The span the data covers, and what happened during it. A model trained on a period of stable conditions inherits the assumption that conditions will remain stable, and the card is where that assumption is written down.

**Generated value:** [ Add details... ]

### Licence and Consent Basis
**Instruction:** The basis on which each dataset may be used, and whether consent was obtained where it was required. Where consent was not obtained, that is the fact to record, not an absence to leave blank.

**Generated value:** [ Add details... ]

### Preprocessing and Filtering
**Instruction:** What was removed, resampled or imputed, and on what basis. Filtering is where a dataset acquires the shape of the population the model will then fail on, and it is rarely the step examined.

**Generated value:** [ Add details... ]

### Known Dataset Limitations
**Instruction:** What the dataset cannot represent. This is the field that prevents a metric from being read as a general claim, and it is almost always empty.

**Generated value:** [ Add details... ]

## Evaluation and Performance

### Evaluation Data
**Instruction:** The data the evaluation was run on, and whether it is disjoint from the training data. Disjointness is the first thing to check in any evaluation, and its absence invalidates every number in the section.

**Generated value:** [ Add details... ]

### Metrics
**Instruction:** Each metric, its value, and the confidence interval or sample size behind it. A single figure with no interval is a point presented as a range, and decisions get made on it.

**Generated value:** [ Add details... ]

### Performance by Subgroup
**Instruction:** The same metrics for each group the model affects, with the sample size for each. A subgroup figure from a small sample is not a measurement, and the sample size is what distinguishes the two.

**Generated value:** [ Add details... ]

### Baseline Comparison
**Instruction:** What the model is compared against, and by how much. A model compared only with a trivial baseline can be both better than it and useless.

**Generated value:** [ Add details... ]

### Threshold and Operating Point
**Instruction:** The threshold in force, and what the alternatives would cost. A model is a set of trade-offs rather than a single system, and the trade-off is only visible once a threshold is fixed.

**Generated value:** [ Add details... ]

### Evaluation Method and Limitations
**Instruction:** How the evaluation was conducted, by whom, and what it does not establish. An evaluation conducted by the team that built the model is legitimate, and it is a fact that belongs on the card.

**Generated value:** [ Add details... ]

### Robustness and Failure Modes
**Instruction:** How the model behaves under input it was not tested on, and the known ways it fails. Known failure modes are more useful than a robustness score, because a reader can act on them and cannot act on a score.

**Generated value:** [ Add details... ]

## Ethical, Fairness and Safety Considerations

### Affected Groups
**Instruction:** The groups whose outcomes the model determines, named. Groups described in aggregate on the basis of a test are not the same as the group that performs worst on it.

**Generated value:** [ Add details... ]

### Known Bias
**Instruction:** The specific ways this model is unfair to this group, stated so that they could be false. A field titled "bias" that says the model may be biased is a heading; "the model scores this group lower on historic completion rates" is a claim that can be measured and can turn out to be wrong.

**Generated value:** [ Add details... ]

### Safety Risks
**Instruction:** The ways the model could cause harm, by severity, with the conditions under which each arises. Severity is what determines the control, and a risk listed without severity is a list of possibilities.

**Generated value:** [ Add details... ]

### Dual-Use and Misuse Potential
**Instruction:** How the model could be used to cause harm, and what has been done about it. Relevant to a model that generates as well as one that classifies, and usually unstated.

**Generated value:** [ Add details... ]

### Environmental and Resource Impact
**Instruction:** The energy and compute consumed, and by whom bears it. Recorded because it is a real cost that appears in no other section, and because it is usually the only figure an external party can verify.

**Generated value:** [ Add details... ]

### Data Privacy Impact
**Instruction:** What the model can reveal about individuals in its training data, and whether it has been tested for it. Extraction and memorisation are testable, and the test is the only thing that distinguishes a considered answer from an assumption.

**Generated value:** [ Add details... ]

## Limitations, Monitoring and Change Control

### Known Limitations
**Instruction:** What the model cannot do, stated plainly. This is the section a reader consults after an incident, and a card that is optimistic in it is a card that will not be consulted a second time.

**Generated value:** [ Add details... ]

### Out-of-Distribution Behaviour
**Instruction:** How the model behaves on inputs unlike its training data, and whether that has been measured. A model given a population it never saw does not fail loudly, which is what makes this worth recording.

**Generated value:** [ Add details... ]

### Production Monitoring
**Instruction:** What is watched after deployment, against what baseline, and how often. Drift is a property of the relationship between the model and the world, not of the model, so a launch measurement is the first of a series.

**Generated value:** [ Add details... ]

### Monitoring Thresholds
**Instruction:** What result triggers action, written before the result is known. A threshold set after seeing a number is a description of that number.

**Generated value:** [ Add details... ]

### Retraining and Update Policy
**Instruction:** When the model will be retrained, what triggers it, and who approves. Without this the model is updated whenever someone has time, and the change is then invisible to everything above it in this card.

**Generated value:** [ Add details... ]

### Version Change Record
**Instruction:** What changed between this version and the last, and why. Models change often and silently, and a card with no change record cannot answer what was in force when an incident occurred.

**Generated value:** [ Add details... ]

### Decommissioning Plan
**Instruction:** How and when the model will be retired, and what happens to the data it holds. A model in production with no retirement plan is a system whose cost grows and whose obligations are never discharged.

**Generated value:** [ Add details... ]

---
