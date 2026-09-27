---
lang: en
layout: default
title: Network Diagram
nav_order: 5
---

<div dir="ltr" style="font-family: Arial, sans-serif; line-height: 1.6;">

## Tasleemat Forms Guide
# Project Artifact: Network Diagram

**Document Reference:** `PMO-04.03.05`

This document provides a comprehensive reference to understand the purpose and usage of the **Network Diagram**.

---

### 1. What?
A visual display of the logical relationships (dependencies) between project schedule activities.

---

### 2. Why?
It visually depicts the flow of work, highlighting critical paths and showing exactly how activities are logically linked. It allows project managers to see which tasks can be done in parallel and which are strictly sequential.

---

### 3. When?
Prepared during the **PLANNING Process Group** (Process 6.3 Sequence Activities). 

---

### 4. Who?
**Responsibilities:** Developed by the Project Manager with input from the project team.

---

### 5. How?
To accurately and professionally complete the **NETWORK DIAGRAM**, the responsible party must populate the dependencies table and generate the visual chart:
*   **Predecessor:** The preceding schedule element.
*   **Relationship & Lead/Lag:** Indicate one of four types: Finish-to-start (FS), Start-to-start (SS), Finish-to-finish (FF), Start-to-finish (SF). Add Lags (delays, e.g., FS+3d) or Leads (accelerations, e.g., FS-3d).
*   **Successor:** The succeeding schedule element.
*   **Visualization:** Render these relationships graphically. Tasleemat recommends using Markdown-native **Mermaid** syntax (`graph LR`) for seamless documentation rendering.

---

### Tailoring Tips
• For some projects you will enter the type of relationship directly into the schedule tool rather than draw it out.
• The network diagram can be produced at the activity level, the deliverable level, or the milestone level.

### Alignment
The network diagram should be aligned and consistent with the following documents:
• Project schedule
• Project roadmap
• Milestone list

---

### 📥 Associated Templates
* [📄 Printable Template (Markdown)](04_03_05_Network_Diagram_Template.md)
* [🤖 LLM Generation Prompt](04_03_05_Network_Diagram.md)
* [📊 Data Schema (JSON)](04_03_05_Network_Diagram.json)
* [📈 Tabular Data (CSV)](04_03_05_Network_Diagram.csv)

</div>
