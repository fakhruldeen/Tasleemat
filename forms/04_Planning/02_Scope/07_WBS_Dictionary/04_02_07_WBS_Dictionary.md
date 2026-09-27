---
lang: en
Form: WBS DICTIONARY (Instructions)
---

# WBS DICTIONARY - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `WBS DICTIONARY`. When asked to populate this form, use the guidance provided for each section below to accurately generate the required content. Reference `parameters.md` for global project variables.

> **Context & Definition:**
> The WBS dictionary supports the work breakdown structure (WBS) by providing detail about the control accounts and work packages it contains. The dictionary can provide detailed information about each work package or summary information at the control account level. The WBS dictionary is progressively elaborated throughout the project.
> 
> **Alignment:**
> The WBS dictionary should be aligned and consistent with the following documents:
• Project charter
• Requirements documentation
• Project scope statement
• WBS
• Activity list

---

### Work Package Details
*   **Code of account:** Enter the code of account from the WBS.
*   **Work package name:** Enter the name of the work package.

### Description of Work
**Instruction:** Enter a brief description of the work package deliverable from the WBS.

### Quality Requirements
**Instruction:** Document any quality requirements or metrics associated with the work package.

### Acceptance Criteria
**Instruction:** Describe the acceptance criteria for the deliverable, usually from the scope statement.

### Technical Information
**Instruction:** Describe or reference any technical requirements or documentation needed to complete the work package.

### Agreement Information
**Instruction:** Reference any contracts or other agreements that impact the work package.

### Milestones
**Instruction:** Generate a Markdown table containing the columns below. List any milestones associated with the work package.
*   **Milestone:** Name of the milestone.
*   **Due Date:** Due date for the milestone.

### Activities & Costs
**Instruction:** Generate a Markdown table containing the columns below.
*   **ID:** Unique activity identifier—usually an extension of the WBS code of accounts.
*   **Activity:** Describe the activity from the activity list or the schedule.
*   **Team resource:** Identify the resources.
*   **Labor hours:** Total effort required.
*   **Labor rate:** Labor rate.
*   **Labor total:** Effort hours times labor rate.
*   **Material units:** Amount of material required.
*   **Material cost:** Material cost.
*   **Material total:** Material units times material cost.
*   **Total cost:** Sum the labor, materials, and any other costs.
