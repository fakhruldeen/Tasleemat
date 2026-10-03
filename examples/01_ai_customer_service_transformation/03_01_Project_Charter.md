# PROJECT CHARTER
**Document Reference:** `PMO-03.01`  
**Project Name:** Omnichannel Enterprise AI Customer Service Platform  
**Project ID:** PRJ-2026-AI-004  
**Classification:** Tier 2 Enterprise (Hybrid Delivery)  

---

<h3 dir="ltr" align="right">Saudi Enterprise Telecommunications (SET)</h3>
<h2 dir="ltr" align="right">PRJ-2026-AI-004 - AI Customer Service Platform</h2>
<h1 dir="ltr" align="center">PROJECT CHARTER</h1>

| **Date Prepared:** 2026-02-15 | **Project Manager:** Sarah Al-Mansoor, PMP | **Prepared By:** Lead Solution Architect |
| :--- | :--- | :--- |

---

## 1. Project Purpose and Justification
This project implements an enterprise-grade, omnichannel AI Conversational Agent leveraging localized Arabic LLMs and Retrieval-Augmented Generation (RAG) to automate Tier-1 customer inquiries, reduce contact center call volume by 45%, and achieve a sub-second response latency across Mobile App, Web Portal, and WhatsApp channels.

* **Business Justification:** Customer call center operating costs currently exceed 28M SAR annually with an average wait time of 4.2 minutes. The AI platform will reduce annual operating expenditure by 9.2M SAR starting Year 1.
* **Strategic Alignment:** Directly supports Enterprise Strategic Pillar 2 (Digital-First Customer Experience) and Vision 2030 National AI Adoption metrics.

---

## 2. Scope Baseline & Key Deliverables
* **In-Scope:**
  1. Fine-tuned Arabic Natural Language Understanding (NLU) model with Saudi dialect coverage.
  2. Enterprise RAG pipeline integrating with CRM, Billing, and Knowledge Base APIs.
  3. Omnichannel connectors (iOS/Android App, Web Widget, WhatsApp Business API).
  4. Human-in-the-loop agent handover desktop integration.
  5. Security & Data Privacy sandbox compliant with Saudi PDPL regulations.
* **Out-of-Scope:**
  1. Replacement of core CRM billing engine.
  2. Physical voice IVR replacement (deferred to Phase 2).

---

## 3. Milestone Schedule & Budget Envelope

| Milestone | Target Completion Date | Success Criteria |
| :--- | :---: | :--- |
| **M1: Architecture & Data Pipeline Sign-off** | 2026-03-31 | Data privacy audit passed; RAG architecture approved |
| **M2: Model Fine-Tuning & Alpha Benchmark** | 2026-05-15 | Intent accuracy $\ge 94\%$ on 5,000 test utterances |
| **M3: End-to-End System Integration** | 2026-07-01 | Latency $< 850	ext{ms}$ under 500 concurrent sessions |
| **M4: User Acceptance Testing (UAT)** | 2026-08-15 | Zero Sev-1/Sev-2 bugs; CSAT pilot score $\ge 4.5/5.0$ |
| **M5: Operational Go-Live & Handover** | 2026-09-30 | 100% agent handover operational; PIR signed |

* **Total Approved Budget:** **4,500,000 SAR** (CAPEX: 3.2M SAR, OPEX/Training: 1.3M SAR).
* **Contingency Reserve:** 450,000 SAR (10% allocated against quantitative risk exposure).

---

## 4. Key Governance Roles & Sign-off

| Governance Role | Name | Signature | Approval Date |
| :--- | :--- | :--- | :---: |
| **Project Sponsor** | Khalid Al-Harbi (VP Customer Care) | *[Signed]* | 2026-02-18 |
| **PMO Director** | Tariq Al-Otaibi, PfMP | *[Signed]* | 2026-02-18 |
| **Chief AI & Data Officer** | Dr. Reem Al-Fahad | *[Signed]* | 2026-02-19 |
| **Project Manager** | Sarah Al-Mansoor, PMP | *[Signed]* | 2026-02-19 |
