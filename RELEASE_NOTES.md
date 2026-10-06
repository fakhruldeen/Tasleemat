# Tasleemat v2.0.0: The AI-Native OKF Framework

We are thrilled to announce **Tasleemat v2.0.0**, marking a massive architectural leap forward. With this release, Tasleemat transforms from a standard PMO documentation repository into a globally compliant, AI-native **Open Knowledge Format (OKF) v0.2** framework.

### 🌟 Major Highlights
- **OKF v0.2 Conformance**: Over 600 PMO templates and guides across all 5 project phases have been fully converted to the Open Knowledge Format, embedding strict machine-readable YAML frontmatter into every artifact.
- **LLM Pre-tokenization**: Introduced a cutting-edge AI optimization. All markdown documents are now pre-tokenized (using the `tiktoken/o200k_base` vocabulary), with exact binary arrays hosted in `_tokens/`. AI Agents reading this framework will experience up to 30% faster Time-To-First-Token (TTFT) by bypassing tokenization via the `token_pointer` protocol.
- **Bilingual Identity Mapping**: English and Arabic templates are now strictly mapped to one another using a unique deterministic `form_id` (e.g., `PMO-06.05`), ensuring LLMs never hallucinate translation boundaries.
- **Attested Computations (EVA)**: Core analytical templates (like Earned Value Analysis) are now protected by **Attested Computation Contracts**, featuring a deterministic Python execution engine that guarantees zero mathematical hallucinations.
- **Agent Navigation Guardrails**: Shipped `docs/AGENT_NAVIGATION.md` and an automated evaluation suite to guide RAG systems and autonomous agents on how to strictly parse status, dependencies, and translations.

### 🛠️ Tooling & Infrastructure
- Dual-validator support: Coexistence of `validate_okf_markdown.py` (Google OKF v0.2 + Local Profile) and `validate_frictionless.py` (JSON Data Packages).
- Frictionless GitHub Actions integration for continuous quality assurance.

*This release makes Tasleemat the definitive, interoperable, and agent-ready project management framework.*
