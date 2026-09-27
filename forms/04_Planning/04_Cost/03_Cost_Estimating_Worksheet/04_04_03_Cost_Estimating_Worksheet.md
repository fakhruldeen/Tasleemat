---
lang: en
Form: COST ESTIMATING WORKSHEET (Instructions)
---

# COST ESTIMATING WORKSHEET - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `COST ESTIMATING WORKSHEET`. When asked to populate this form, generate arrays for the tables based on the quantitative methods appropriate for the project.

> **Context & Definition:**
> A cost estimating worksheet helps develop cost estimates when quantitative methods (Parametric, Analogous, Three-point) or a bottom-up estimate are developed. Bottom-up estimates are detailed estimates done at the work package level.
> 
> **Alignment:**
> The cost estimating worksheet should be aligned and consistent with the following documents:
• Cost management plan
• Scope baseline
• Project schedule
• Quality management plan
• Resource requirements
• Risk register
• Lessons learned register

---

### Section Generation Instructions
**1. Parametric Estimates:** Use for activities driven by a quantifiable measure.
*   **ID:** Unique identifier, such as the WBS ID or activity ID.
*   **Cost Variable:** Enter the cost estimating driver, such as hours, square feet, gallons, or some other quantifiable measure.
*   **Cost Per Unit:** Record the cost per unit.
*   **Number of Units:** Enter the number of units.
*   **Cost Estimate:** Multiply the number of units times the cost per unit to calculate the estimate.

**2. Analogous Estimates:** Use for activities compared to previous similar work.
*   **ID:** Unique identifier.
*   **Previous Activity:** Enter a description of the previous activity.
*   **Previous Cost:** Document the cost of the previous activity.
*   **Current Activity:** Describe how the current activity is different.
*   **Multiplier:** Divide the current activity by the previous activity to get a multiplier.
*   **Cost Estimate:** Multiply the cost for the previous activity by the multiplier to calculate the Cost Estimate.

**3. Three-Point Estimates:** Use to account for uncertainty using beta distribution.
*   **ID:** Unique identifier.
*   **Optimistic Cost:** Estimate assuming all costs were identified and there won't be any cost increases.
*   **Most Likely Cost:** Estimate assuming some cost fluctuations but nothing out of the ordinary.
*   **Pessimistic Cost:** Estimate assuming significant risks will materialize and cause cost overruns.
*   **Weighting Equation:** Weight the three estimates. The most common method is the beta distribution: cE = (cO + 4cM + cP) / 6.
*   **Expected Cost:** Enter the expected cost based on the beta distribution.
