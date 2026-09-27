---
lang: en
Form: WORK BREAKDOWN STRUCTURE (Instructions)
---

# WORK BREAKDOWN STRUCTURE - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `WORK BREAKDOWN STRUCTURE`. When asked to populate this form, use the guidance provided for each section below to accurately generate the required content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> The work breakdown structure (WBS) is used to decompose all the work of the project. It begins at the project level and is successively broken down into finer levels of detail. The lowest level, a work package, represents a discrete deliverable that can be decomposed into activities to produce the deliverable. The WBS is an output from the process 5.4 Create WBS in the PMBOK® Guide – Sixth Edition.
> 
> **Alignment:**
> The WBS should be aligned and consistent with the following documents:
• Project charter
• Requirements documentation
• Project scope statement
• WBS dictionary
• Activity list

---

### Work Breakdown Structure
**Instruction:** Generate a Markdown table containing exactly the columns specified below. Build a realistic multi-level hierarchy (e.g., Level 1 -> Control Accounts -> Work Packages) containing at least 8 to 12 rows based on the project scope.

**Table Columns & Generation Rules:**
*   **WBS ID:** Provide a hierarchical numeric structure (e.g., 1.0, 1.1, 1.1.1) to clearly indicate outline level.
*   **Element Name:** The concise name of the deliverable or component.
*   **Element Type:** Categorize the element (e.g., 'Project Phase', 'Major Deliverable', 'Control Account', 'Work Package'). Ensure you include Control Accounts and Work Packages.
*   **Description:** A very brief description of the element's scope.
