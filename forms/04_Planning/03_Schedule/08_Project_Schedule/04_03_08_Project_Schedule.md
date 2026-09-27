---
lang: en
Form: PROJECT SCHEDULE (Instructions)
---

# PROJECT SCHEDULE - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `PROJECT SCHEDULE`. When asked to populate this form, generate an array of objects representing the schedule tabular data, and output a Mermaid Gantt chart for the markdown visualization.

> **Context & Definition:**
> The project schedule combines the information from the activity list, network diagram, resource requirements, and duration estimates to determine the start and finish dates for project activities. A common way of showing a schedule is via a Gantt chart. It is an output from the process 6.5 Develop Schedule in the PMBOK® Guide.
> 
> **Alignment:**
> The project schedule should be aligned and consistent with the following documents:
• Project charter
• Assumption log
• Schedule management plan
• Project roadmap
• Scope baseline
• Activity list
• Network diagram
• Duration estimates
• Project team assignments
• Project calendars

---

### Data: Project Schedule
**Instruction:** Generate a comprehensive list of activities with their start and finish dates.

**Columns Definition:**
*   **WBS Identifier:** The unique WBS code linking the activity to the work package.
*   **Activity Name:** A brief description of the work.
*   **Start Date:** The planned start date (YYYY-MM-DD).
*   **Finish Date:** The planned finish date (YYYY-MM-DD).
*   **Resource Name:** The person or role assigned to the activity.
