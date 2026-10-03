# AI CANVAS & USE CASE CARD
**Document Reference:** `PMO-02.04`  
**Solution Name:** GenAI Bilingual Customer Care Assistant  
**Governance Scope:** Enterprise AI Solution Lifecycle  

---

<h3 dir="ltr" align="right">Saudi Enterprise Telecommunications (SET)</h3>
<h2 dir="ltr" align="right">AI-CARE-2026 - GenAI Assistant Use Case Card</h2>
<h1 dir="ltr" align="center">AI CANVAS & USE CASE CARD</h1>

| **Date Prepared:** 2026-02-10 | **AI Product Owner:** Faisal Al-Ghamdi | **Prepared By:** Lead ML Engineer |
| :--- | :--- | :--- |

---

## 1. Problem Statement & Value Hypothesis
* **Problem Statement:** 65% of customer support volume consists of repetitive transactional requests (SIM activation, roaming packages, invoice inquiries) causing agent burnout and high customer churn.
* **Value Hypothesis:** A grounded RAG model capable of understanding formal Arabic and Saudi dialect variations will resolve 45% of Tier-1 inquiries autonomously with zero human intervention.

---

## 2. Technical Architecture & Data Landscape
* **Foundation Model:** Localized Llama-3-70B Arabic Fine-Tuned + Embedding-Large-v3.
* **Vector Database:** Enterprise Milvus with hybrid sparse/dense vector search.
* **Data Sources:** 12,000 curated support articles, real-time CRM GraphQL APIs, billing history database.
* **Latency SLA:** $\le 850	ext{ms}$ Time-to-First-Token (TTFT).

---

## 3. Ethical Guardrails & Risk Controls
* **Hallucination Control:** Strict RAG retrieval threshold; response confidence score $< 0.88$ triggers immediate graceful transfer to a human specialist.
* **PII Redaction:** Real-time Presidio PII masking on National ID, phone numbers, and credit card credentials before prompt submission.
* **Fairness & Toxicity:** Automated NeMo Guardrails blocking discriminatory, harmful, or out-of-domain conversational attempts.
