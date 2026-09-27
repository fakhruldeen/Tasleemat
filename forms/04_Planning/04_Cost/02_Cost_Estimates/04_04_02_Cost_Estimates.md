---
lang: en
Form: COST ESTIMATES (Instructions)
---

# COST ESTIMATES - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `COST ESTIMATES`. When asked to populate this form, generate an array of objects representing the cost estimate tabular data.

> **Context & Definition:**
> Cost estimates provide information on the cost of resources necessary to complete project work, including labor, equipment, supplies, services, facilities, and material. Estimates can be determined by developing an approximation for each work package using expert judgment or by using quantitative methods. It is an output from the process 7.2 Estimate Costs in the PMBOK® Guide.
> 
> **Alignment:**
> The cost estimates should be aligned and consistent with the following documents:
• Assumption log
• Activity attributes
• Project schedule
• Resource requirements
• Project team assignments

---

### Table: Activity Cost Estimates
**Instruction:** Generate a comprehensive tabular list of activity cost estimates incorporating labor, physical resources, and reserves.

**Columns Definition:**
*   **ID:** Unique identifier, such as the WBS ID or activity ID.
*   **Resource:** The resource (person, equipment, material) needed for the deliverable.
*   **Labor Costs:** The costs associated with team or outsourced resources.
*   **Physical Costs:** Costs associated with material, equipment, supplies, or other physical resources.
*   **Reserve:** Document contingency reserve amounts, if any.
*   **Estimate:** The sum of the cost of labor, physical resources, and reserve costs.
*   **Basis of Estimates:** Information such as cost per pound, duration of the work, square feet, etc.
*   **Method:** The method used to estimate the cost (analogous, parametric, three-point, bottom-up).
*   **Assumptions/Constraints:** Assumptions used to estimate the cost (e.g. resource duration).
*   **Range:** The range of the estimate (e.g. +/- 10%).
*   **Confidence Level:** The degree of confidence in the estimate (e.g. 90%).
