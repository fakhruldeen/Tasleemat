<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>Language:</strong> English Manual</span>
  <a class="lang-switch-btn" href="../ar/09_agile_hybrid_integration.html">🇸🇦 الانتقال للنسخة العربية (Arabic Manual) →</a>
</div>

<p align="center">
  <img src="../img/logo.png" alt="Tasleemat Logo" width="320" />
</p>

---

# ⚡ Agile, Scrum, Kanban & Hybrid Integration Guide
**Document ID:** `TASLEEMAT-GUIDE-09-AGILE-HYBRID`  
**Version:** 2.0  
**Target Audience:** Scrum Masters, Agile Coaches, Product Owners, Hybrid Project Managers  

---

## 🎯 The Pragmatic Hybrid Model

Modern enterprises rarely operate in 100% pure waterfall or 100% pure agile. Strategic alignment, procurement, budgeting, and regulatory signoffs require predictable governance, while feature discovery, development, and user testing demand agile speed.

**Tasleemat provides the ultimate bridge:** a lightweight governance wrapper for executive oversight paired with high-velocity agile toolkits for product delivery teams.

```mermaid
flowchart TD
    subgraph "Executive & Governance Wrapper (Lightweight Waterfall)"
        G1["PMO-03.01 Project Charter"] --> G2["PMO-04.01.03 Project Roadmap"]
        G2 --> G3["PMO-04.05.03 Definition of Ready & Done"]
    end

    subgraph "Agile Delivery Loop (Scrum / Kanban)"
        G3 --> A1["PMO-04.02.09 User Story Mapping"]
        A1 --> A2["PMO-04.02.08 Product Backlog"]
        A2 --> A3["PMO-04.03.10 Sprint Planning Log"]
        A3 --> A4["PMO-06.12 Flow Metrics & Value Stream"]
        A4 --> A5["PMO-05.08 Retrospective"]
        A5 --> A3
    end

    subgraph "Milestone & Value Governance"
        A4 --> M1["PMO-04.03.09 Release Plan"]
        M1 --> M2["PMO-06.01 Status Report"]
    end
```

---

## 🛠️ Mapping Tasleemat Deliverables to Agile Ceremonies

| Agile Ceremony / Activity | Tasleemat Deliverable | Role Responsible | Frequency |
| :--- | :--- | :--- | :--- |
| **Discovery & Inception** | [`PMO-04.02.09 User Story Mapping Canvas`](../../forms/en/04_Planning/02_Scope/09_User_Story_Mapping_Canvas/) | Product Owner | Project Start / Major Releases |
| **Quality Criteria Agreement** | [`PMO-04.05.03 Definition of Ready & Done`](../../forms/en/04_Planning/05_Quality/03_Definition_of_Ready_and_Done/) | Team & Scrum Master | Inception & Sprint 0 |
| **Backlog Refinement** | [`PMO-04.02.08 Product Backlog`](../../forms/en/04_Planning/02_Scope/08_Product_Backlog/) | Product Owner | Weekly / Continuous |
| **Sprint Planning** | [`PMO-04.03.10 Sprint Planning Log`](../../forms/en/04_Planning/03_Schedule/10_Sprint_Planning_Log/) | Scrum Master & Dev Team | Start of Sprint (Bi-weekly) |
| **Release Coordination** | [`PMO-04.03.09 Release Plan`](../../forms/en/04_Planning/03_Schedule/09_Release_Plan/) | Product Owner / Release Mgr | Quarterly / Per Release |
| **Flow & WIP Monitoring** | [`PMO-06.12 Flow Metrics & Value Stream`](../../forms/en/06_Monitoring_and_Controlling/12_Flow_Metrics_and_Value_Stream/) | Agile Coach / PMO | Continuous / Sprint Review |
| **Sprint Retrospective** | [`PMO-05.08 Retrospective`](../../forms/en/05_Executing/08_Retrospective/) | Team & Scrum Master | End of Sprint |
| **Team Psychological Safety** | [`PMO-04.06.06 Psychological Safety Index`](../../forms/en/04_Planning/06_Resource/06_Team_Psychological_Safety_and_Wellbeing_Index/) | Agile Coach / HR Partner | Monthly / Quarterly |

---

## 📊 Agile Flow Metrics & Governance KPIs

Rather than tracking task hours, high-performing agile teams measure value throughput using [`PMO-06.12`](../../forms/en/06_Monitoring_and_Controlling/12_Flow_Metrics_and_Value_Stream/):

1. **Cycle Time:** The elapsed calendar time from when work starts on a user story to when it is delivered to production.
2. **Throughput:** The number of completed user stories or story points delivered per sprint.
3. **Work In Progress (WIP):** The total active items in the system. Enforcing strict WIP limits prevents multi-tasking bottlenecks.
4. **Flow Efficiency:** $	ext{Flow Efficiency} = rac{	ext{Active Working Time}}{	ext{Total Lead Time}} 	imes 100\%$. Target $\ge 40\%$.
