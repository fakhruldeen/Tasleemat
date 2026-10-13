---
type: Specification
target_runtime: LLM / Autonomous Agent / Multi-Agent Swarm
specification_version: 2.5.0
---

# 🤖 Tasleemat Autonomous AI Agent Navigation Protocol
**Protocol Identifier:** `TASLEEMAT-SPEC-AGENT-NAVIGATION`  
**Compliance Standards:** Model Context Protocol (MCP) JSON-RPC 2.0, Open Knowledge Format (OKF) v0.2, JSON Schema Draft 2020-12  

---

## 🎯 Protocol Overview & Machine Directives

This specification provides unambiguous, machine-readable instructions for Large Language Models (LLMs), autonomous agents, and multi-agent coordination orchestrators interacting with the Tasleemat repository.

### Core Machine Invariants
1. **Source Immutability**: The `forms/` directory is **100% read-only**. Never attempt to mutate, write, or delete files under `forms/`.
2. **Canonical Identification (`artifact_id`)**: Every deliverable is indexed by a canonical dot-delimited code (`PMO-XX.YY` or `PMO-XX.YY.ZZ`). Never invent or reference legacy codes (`FORM-XX-YY`).
3. **Draft 2020-12 Validation Rule**: Never persist deliverable payloads into project workspaces without verifying `tasleemat.validate_artifact_data(artifact_id, data, strict=True)`.

---

## 🗺️ 1. Directed Acyclic Graph (DAG) Traversal Protocol

Autonomous agents must respect upstream-to-downstream dependencies. Upstream deliverables provide the mandatory grounding context for downstream deliverables:

```
[PMO-01.01 Business Case]
         │
         ▼
[PMO-03.01 Project Charter] ──────┐
         │                        │
         ▼                        ▼
[PMO-04.02.05 Scope Statement]   [PMO-03.04 Stakeholder Register]
         │
         ▼
[PMO-04.02.06 WBS & Dictionary]
         │
         ├────────────────────────┐
         ▼                        ▼
[PMO-04.03.08 Schedule Baseline] [PMO-04.04.04 Cost Budget]
         │                        │
         └───────────┬────────────┘
                     ▼
       [PMO-04.08.02 Risk Register]
                     │
                     ▼
       [PMO-06.05 Earned Value EVA]
```

### Machine Traversal Logic
1. When asked to generate a downstream artifact (e.g., `PMO-04.08.02`), query whether its upstream inputs (`PMO-04.02.05`, `PMO-04.03.08`, `PMO-04.04.04`) exist in the current workspace.
2. If upstream inputs are missing, inform the orchestrator or generate upstream prerequisites first.
3. Consult `docs/en/07_document_dependencies.md` (or `docs/ar/07_document_dependencies.md`) for full 114-deliverable dependency graphs.

---

## 🔌 2. JSON-RPC 2.0 Tool-Calling Contract (Model Context Protocol)

When interacting via the Tasleemat MCP server (`tasleemat mcp`), agents must construct valid JSON-RPC 2.0 messages:

### A. Discovering Artifacts (`tasleemat_list_artifacts`)
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "tasleemat_list_artifacts",
    "arguments": {
      "category": "04_Planning",
      "tier": "2"
    }
  }
}
```

### B. Extracting Deliverable Assets (`tasleemat_get_asset`)
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "tasleemat_get_asset",
    "arguments": {
      "artifact_id": "PMO-03.01",
      "role": "schema",
      "lang": "en"
    }
  }
}
```
*Valid `role` values:* `"template"`, `"prompt"`, `"guide"`, `"schema"`, `"dictionary"`, `"example"`.

### C. Validating Structured Data (`tasleemat_validate_data`)
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "tasleemat_validate_data",
    "arguments": {
      "artifact_id": "PMO-03.01",
      "data": {
        "project_code": "PRJ-2026-CLOUD",
        "project_name": "Enterprise Cloud Migration",
        "start_date": "2026-11-01",
        "sponsor_name": "Executive Sponsor",
        "estimated_budget": 2500000.00
      },
      "mode": "strict"
    }
  }
}
```

### D. Offline HTML Rendering (`tasleemat_render_artifact`)
```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "tasleemat_render_artifact",
    "arguments": {
      "artifact_id": "PMO-03.01",
      "data": { "project_name": "Cloud Transformation" },
      "lang": "ar"
    }
  }
}
```

---

## ⚡ 3. Token-Optimized Fast Traversal (`token_pointer`)

Every markdown document in `docs/` and `forms/` contains a pre-computed tokenization pointer in its frontmatter:
```yaml
token_pointer: /_tokens/forms/en/03_Initiating/01_Project_Charter/03_01_Project_Charter.npy
tokenizer_model_id: tiktoken/o200k_base
```
If your agent runtime supports direct NumPy array loading, load the `.npy` array directly into KV-cache to bypass tokenization overhead, reducing Time-To-First-Token (TTFT) by approximately $30\%$.

---

## 🛑 4. Strict Hallucination & Evidence Rules

1. **Missing Data Placeholder**:
   - If user context lacks required information, insert `[ Requires Human Input: <Attribute> ]`. Never fabricate metrics.
2. **Cryptographic Integrity Preservation**:
   - Always preserve `{{Audit_Trail_SHA256_Hash}}` placeholders in generated document control blocks.
3. **Bilingual Parity Preservation**:
   - Never generate hybrid English-Arabic text in a single field. English templates must use standard PMBOK English; Arabic templates must use official Saudi DGA / SDAIA Arabic terminology.
