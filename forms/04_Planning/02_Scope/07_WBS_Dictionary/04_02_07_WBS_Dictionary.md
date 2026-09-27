---
lang: en
Form: WBS DICTIONARY (Instructions)
---

# WBS DICTIONARY - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `WBS DICTIONARY`. When asked to populate this form, generate multiple dictionary entries (one for each work package).

> **Context & Definition:**
> The WBS dictionary supports the work breakdown structure (WBS) by providing detail about the control accounts and work packages it contains. The dictionary provides detailed information about each work package.
> 
> **Alignment:**
> The WBS dictionary should be aligned and consistent with the following documents:
• Project charter
• Requirements documentation
• Project scope statement
• WBS
• Activity list

---

### Work Package Entries
**Instruction:** Repeat the following block for EVERY Work Package defined in the WBS.

*   **Work Package Name:** Enter the name of the work package.
*   **Code of Accounts:** Enter the WBS ID / code of account.
*   **Due Dates:** List the overarching due dates.
*   **Description of Work:** Brief description of the deliverable.
*   **Assumptions and Constraints:** List assumptions and constraints related to this work package.
*   **Milestones:** Provide a numbered list of milestones formatted as a single markdown string containing list items.
*   **Activities & Costs:** Generate a Markdown table (Columns: ID, Activity, Team resource, Labor hours, Labor rate, Labor total, Material units, Material cost, Material total, Total cost).
*   **Quality Requirements:** Document any quality metrics.
*   **Acceptance Criteria:** Describe how the deliverable will be accepted.
*   **Technical Information:** Reference technical requirements.
*   **Agreement Information:** Reference any contracts or agreements.
