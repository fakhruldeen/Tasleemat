---
lang: en
Form: REQUIREMENTS TRACEABILITY MATRIX (Instructions)
---

# REQUIREMENTS TRACEABILITY MATRIX - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `REQUIREMENTS TRACEABILITY MATRIX`. When asked to populate this form, use the guidance provided for each section below to accurately generate the required content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> A requirements traceability matrix is used to track the various attributes of requirements throughout the project life cycle. It uses information from the requirements documentation and traces how those requirements are addressed through other aspects of the project. An inter-requirements traceability matrix can be used to trace the relationship between categories of requirements (e.g., Business vs Technical). The requirements traceability matrix is an output from the process 5.2 Collect Requirements in the PMBOK® Guide – Sixth Edition.
> 
> **Alignment:**
> The requirements traceability matrix should be aligned and consistent with the following documents:
• Development approach
• Requirements management plan
• Requirements documentation
• Release and iteration plan

---

### Requirements Traceability Matrix
**Instruction:** Generate a Markdown table containing exactly the columns specified below. Generate at least 5 representative requirements tracing entries based on the project context.

**Table Columns & Generation Rules:**
*   **ID:** Enter a unique requirement identifier.
*   **Requirement:** Document the condition or capability that must be met by the project.
*   **Source:** The stakeholder that identified the requirement.
*   **Priority:** Prioritize the requirement category (e.g., Level 1, Level 2, must have).
*   **Category:** Categorize the requirement (e.g., functional, nonfunctional, security).
*   **Business objective:** List the business objective as identified in the charter or business case that is met by fulfilling the requirement.
*   **Deliverable:** Identify the deliverable that is associated with the requirement.
*   **Verification:** Describe the metric that is used to measure the satisfaction of the requirement.
*   **Validation:** Describe the technique that will be used to validate that the requirement meets the stakeholder needs.

---

### Inter-Requirements Traceability Matrix
**Instruction:** Generate a Markdown table containing exactly the columns specified below. Generate at least 3 representative inter-requirement relationships based on the project context.

**Table Columns & Generation Rules:**
*   **Business Req ID:** Enter a unique business requirement identifier.
*   **Business Requirement:** Document the condition or capability that must be met to satisfy business needs.
*   **Business Priority:** Prioritize the business requirement.
*   **Business Source:** Document the stakeholder who identified the business requirement.
*   **Technical Req ID:** Enter a unique technical requirement identifier.
*   **Technical Requirement:** Document the technical performance that must be met by the deliverable to satisfy a need.
*   **Technical Priority:** Prioritize the technical requirement.
*   **Technical Source:** Document the stakeholder who identified the technical requirement.
