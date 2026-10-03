<h3 dir="ltr" align="right">Saudi Enterprise Telecommunications (SET)</h3>
<h2 dir="ltr" align="right">PRJ-2026-AI-004 - AI Customer Service Platform</h2>
<h1 dir="ltr" align="center">RISK REGISTER</h1>

| **Date Prepared:** 2026-03-01 | **Project Manager:** Sarah Al-Mansoor, PMP | **Prepared By:** Risk Specialist |
| :--- | :--- | :--- |

---

## Risk Log Entries

| Risk ID | Category | Risk Description | Probability (1-5) | Impact (1-5) | Score (P×I) | Response Strategy | Mitigation Action Plan | Risk Owner | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- | :--- | :--- | :---: |
| **RSK-AI-01** | Technical / Quality | LLM produces factually inaccurate billing advice (Hallucination). | 3 | 5 | **15** | Mitigate | Implement strict RAG grounding with $<0.88$ confidence routing to human agents. | ML Lead | Active |
| **RSK-AI-02** | Regulatory | PII data leakage through conversational logs breaching Saudi PDPL. | 2 | 5 | **10** | Avoid | Integrate real-time on-premise PII tokenization and masking proxy. | Security Lead | Closed |
| **RSK-AI-03** | Performance | High inference latency during peak hours ($>1500\text{ms}$). | 4 | 3 | **12** | Mitigate | Deploy local TensorRT-LLM quantization and vLLM multi-GPU inference cluster. | Infrastructure Lead | Active |
| **RSK-AI-04** | Operational | Human call center agents resist AI adoption fearing redundancy. | 3 | 4 | **12** | Mitigate | Roll out OCM upskilling program transitioning agents to Tier-2 specialized advisors. | HR Lead | Active |
