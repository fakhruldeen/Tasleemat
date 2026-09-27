---
lang: en
Form: NETWORK DIAGRAM (Instructions)
---

# NETWORK DIAGRAM - LLM GENERATION GUIDE

> **System Prompt / Instructions:**
> This document serves as the detailed instruction set for generating the `NETWORK DIAGRAM`. When asked to populate this form, generate the tabular dependencies list and a valid Mermaid graph visualization.

> **Context & Definition:**
> The network diagram is a visual display of the relationship between schedule elements. The purpose is to visually depict the types of relationships (FS, SS, FF, SF) and any modifications such as leads or lags between components. It is an output from process 6.3 Sequence Activities in the PMBOK® Guide – Sixth Edition.
> 
> **Alignment:**
> The network diagram should be aligned and consistent with the following documents:
• Project schedule
• Project roadmap
• Milestone list

---

### 1. Network Diagram Dependencies
**Instruction:** Generate a table listing the connections between activities/milestones.

**Columns Definition:**
*   **Predecessor:** The activity or milestone that comes first.
*   **Relationship & Lead/Lag:** The relationship type (FS, SS, FF, SF) and any applied lead (-days) or lag (+days).
*   **Successor:** The activity or milestone that follows.

### 2. Network Diagram Visualization
**Instruction:** Generate a valid `mermaid` block (using `graph LR` or `graph TD`) that visually represents the dependencies listed in the table above. Ensure node names are concise or utilize node IDs with labels (e.g., `A[Activity A] -->|FS| B[Activity B]`).
