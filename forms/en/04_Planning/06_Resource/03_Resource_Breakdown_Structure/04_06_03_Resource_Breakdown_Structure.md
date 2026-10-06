---
type: Form
lang: en
Form: RESOURCE BREAKDOWN STRUCTURE (Instructions)
token_pointer: /_tokens/forms/en/04_Planning/06_Resource/03_Resource_Breakdown_Structure/04_06_03_Resource_Breakdown_Structure.npy
token_count: 575
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:29.000464+00:00'
form_id: PMO-04.06.03
status: approved
---

# RESOURCE BREAKDOWN STRUCTURE - LLM Generation Prompt

<!--
SYSTEM INSTRUCTIONS: This document is the detailed instruction set for
generating the RESOURCE BREAKDOWN STRUCTURE. When asked to populate the template, follow the
guidance for each section below to produce the requested content. Refer to
`parameters.md` for the general project variables.
-->

> **Context and Definition:**
> A hierarchical view of the project's resources, organised by type and category. It is an output of Estimate Activity Resources, and its job is to make the resource picture legible at a glance rather than to restate it line by line.

> **Alignment & Dependencies:**
> * **Pre-requisites (Inputs):**
>   * *Mandatory:* Work Breakdown Structure / WBS (PMO-04.02.06), Project Schedule (PMO-04.03.08)
>   * *Optional:* Resource Capacity Matrix (PMO-00.04), Cost Management Plan (PMO-04.04.01)
> * **Downstream Dependents:**
>   * *Mandatory:* Responsibility Assignment Matrix / RAM (PMO-04.06.04), Team Charter (PMO-04.06.05), Team Performance Assessment (PMO-05.06)
>   * *Optional:* Team Onboarding Checklist (PMO-05.12), Training Plan & Log (PMO-04.11.02)

---

## Resource Breakdown Structure (Outline)

### RBS Code
**Instructions:** The position of the node in the hierarchy, written as 1, 1.1, 1.1.1 so a reader can reconstruct the tree from the text alone. A node numbered 1.2.1 with no 1.2 above it means a level was skipped.

**Generated Value:** [ Add details... ]

### Resource Node
**Instructions:** What the node names. A first-level node is the project, a second-level node is a resource category such as people or equipment, and a third-level node is an individual resource carrying its quantity. A category node with nothing beneath it leaves the branch empty.

**Generated Value:** [ Add details... ]

## Resource Breakdown Structure (Hierarchical Chart)

### Chart Form
**Instructions:** Which view the chart takes: a mindmap for a single hierarchy, or a flowchart where the nodes carry relationships rather than only parentage. Stated so a reader knows what the diagram is meant to show.

**Generated Value:** [ Add details... ]

### Node Labels
**Instructions:** The node labels, one per line, in the same order as the outline. The chart and the outline must agree: a branch present in one and absent from the other is the defect this section exists to prevent.

**Generated Value:** [ Add details... ]

---
