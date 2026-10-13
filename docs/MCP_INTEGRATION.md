---
type: Guide
---

# 🔌 Tasleemat Model Context Protocol (MCP) Integration Guide

This guide describes how to connect the **Tasleemat MCP Server** (`tasleemat-mcp`) to **Claude Desktop**, **Cursor**, **OpenCode**, and any standard Model Context Protocol client.

---

## 🌟 Overview

The Tasleemat MCP server enables AI assistants to directly interact with:
- **114 Standardized Bilingual PMO Deliverables** across 8 lifecycle phases (`00` to `07`).
- **Templates, Practitioner Guides & LLM Prompts** in English and Arabic.
- **Bilingual PMO Lexicon** conforming to PMI PMBOK® and Saudi Digital Government Authority (DGA) standards.
- **Structural Data Validation** in strict mode (for stage-gates) and draft mode (for agent drafting loops).
- **Offline HTML Document Rendering** with responsive styling and Arabic RTL support.

---

## 🛠️ Exposed MCP Tools

| Tool Name | Description | Key Arguments |
| :--- | :--- | :--- |
| `tasleemat_list_artifacts` | List deliverables filtered by phase or tailoring tier | `phase?: string`, `tier?: string` |
| `tasleemat_get_artifact` | Get metadata and authoritative SHA-256 fingerprint for a deliverable | `artifact_id: string` (e.g. `PMO-03.01`) |
| `tasleemat_get_asset` | Retrieve template, practitioner guide, prompt, schema, or example | `artifact_id: string`, `role: string`, `lang?: string` |
| `tasleemat_get_lexicon` | Search bilingual PMI & DGA PMO terminology | `category?: string`, `query?: string` |
| `tasleemat_validate_data` | Validate structured data against JSON companion schema (structural check only) | `artifact_id: string`, `data: object`, `definition_version?: string`, `mode?: "strict" \| "draft"` |
| `tasleemat_render_artifact` | Render deliverable to styled, print-ready HTML | `artifact_id: string`, `lang?: string`, `data?: object` |

---

## 🚀 Client Setup Configurations

### 1. Claude Desktop Setup

Add the server to your `claude_desktop_config.json`:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "python3",
      "args": ["-m", "tasleemat.mcp"]
    }
  }
}
```

Or using `uvx` directly from PyPI without pre-installing:

```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "uvx",
      "args": ["tasleemat", "mcp"]
    }
  }
}
```

---

### 2. Cursor IDE Setup

In Cursor, go to **Settings** $\rightarrow$ **Features** $\rightarrow$ **MCP** $\rightarrow$ **Add New MCP Server**:
- **Name:** `tasleemat`
- **Type:** `command`
- **Command:** `tasleemat-mcp`

Or configure via `.cursor/mcp.json` in your workspace root:

```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

---

### 3. OpenCode Setup

In your OpenCode MCP settings or workspace configuration:

```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

---

### 4. Windsurf (Codeium) Setup

In Windsurf, configure `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

---

### 5. Cline / Roo Code (VS Code Extension) Setup

In VS Code with Cline or Roo Code installed, edit `cline_mcp_settings.json`:

```json
{
  "mcpServers": {
    "tasleemat": {
      "command": "tasleemat-mcp"
    }
  }
}
```

---

## 🐍 Multi-Agent Frameworks (CrewAI, LangChain, LlamaIndex)

Because `tasleemat` is a first-class Python package (`pip install tasleemat`), it can be integrated directly into autonomous multi-agent pipelines:

### 1. CrewAI Custom Tools

Equip CrewAI agents with PMO document retrieval and structural validation capabilities:

```python
from crewai.tools import tool
import tasleemat
import json

@tool("PMO Deliverable Retriever")
def get_pmo_deliverable(artifact_id: str, role: str = "template", lang: str = "en") -> str:
    """Fetches standardized PMO deliverable templates and guides (e.g. PMO-03.01)."""
    return tasleemat.get_artifact_asset(artifact_id, role, lang)

@tool("PMO Structural Validator")
def validate_pmo_data(artifact_id: str, payload_json_str: str) -> str:
    """Validates structured project data against formal JSON schema contracts."""
    data = json.loads(payload_json_str)
    report = tasleemat.validate_artifact_data(artifact_id, data, mode="draft")
    return f"Valid: {report.valid}, Errors: {len(report.errors)}, Warnings: {len(report.warnings)}"
```

### 2. LangChain Custom BaseTool

Expose Tasleemat deliverable lookups to LangGraph and LangChain agents:

```python
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
import tasleemat

class PMOFetchInput(BaseModel):
    artifact_id: str = Field(description="Unique PMO artifact ID, e.g., 'PMO-03.01'")
    role: str = Field(default="template", description="Role: 'template', 'guide', 'prompt', 'schema'")
    lang: str = Field(default="en", description="Language: 'en' or 'ar'")

class PMOFetchTool(BaseTool):
    name: str = "pmo_fetch_asset"
    description: str = "Retrieve standardized PMBOK-compliant PMO templates, guides, or prompts in English or Arabic."
    args_schema: type[BaseModel] = PMOFetchInput

    def _run(self, artifact_id: str, role: str = "template", lang: str = "en") -> str:
        return tasleemat.get_artifact_asset(artifact_id, role=role, lang=lang)
```

### 3. LlamaIndex Tool Integration

Integrate Tasleemat into LlamaIndex query engines or RAG workflows:

```python
from llama_index.core.tools import FunctionTool
import tasleemat

def fetch_pmo_template(artifact_id: str, lang: str = "en") -> str:
    """Retrieve an authoritative bilingual PMO template by ID."""
    return tasleemat.get_artifact_asset(artifact_id, role="template", lang=lang)

pmo_tool = FunctionTool.from_defaults(
    fn=fetch_pmo_template,
    name="tasleemat_pmo_template",
    description="Provides access to 114 standardized bilingual PMO deliverable templates."
)
```

---

## 🧪 Testing the Server Directly via stdio

You can test the server directly from the terminal using JSON-RPC 2.0 messages:

```bash
# 1. Initialize Handshake
echo '{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}, "clientInfo": {"name": "cli", "version": "1.0"}}}' | python3 -m tasleemat.mcp

# 2. List Available Tools
echo '{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}' | python3 -m tasleemat.mcp

# 3. Retrieve Project Charter Template (Arabic)
echo '{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "tasleemat_get_asset", "arguments": {"artifact_id": "PMO-03.01", "role": "template", "lang": "ar"}}}' | python3 -m tasleemat.mcp
```

---

## 📋 JSON-RPC 2.0 Protocol Conformance & Request ID Rules

The Tasleemat MCP server strictly conforms to the JSON-RPC 2.0 specification:

### 1. Request ID Validation Rules
| ID Type | Example | Server Behavior |
| :--- | :--- | :--- |
| **String** | `"req-101"`, `""` | ✅ Accepted; mirrored exactly in response `id`. |
| **Integer** | `1`, `0`, `-5` | ✅ Accepted; mirrored exactly in response `id`. |
| **Integral Float** | `1.0`, `42.0` | ✅ Normalized to integer `1`, `42` in response `id`. |
| **Null** | `null` | ✅ Accepted; mirrored as `null` in response `id`. |
| **Fractional Float** | `1.5`, `3.14159` | ❌ Rejected with `-32600` (`Invalid Request`). |
| **Non-finite Float** | `NaN`, `Infinity` | ❌ Rejected with `-32600` (`Invalid Request`). |
| **Boolean** | `true`, `false` | ❌ Rejected with `-32600` (`Invalid Request`). |
| **Container** | `[]`, `{"id": 1}` | ❌ Rejected with `-32600` (`Invalid Request`). |

### 2. Standard JSON-RPC Error Taxonomy
| Code | Constant | Meaning in Tasleemat MCP Server |
| :---: | :--- | :--- |
| `-32700` | Parse error | Received payload is not well-formed JSON. |
| `-32600` | Invalid Request | Missing `"jsonrpc": "2.0"`, invalid method type, or disallowed request ID format. |
| `-32601` | Method not found | Method does not exist (supported: `initialize`, `ping`, `tools/list`, `tools/call`, `resources/list`, `prompts/list`). |
| `-32602` | Invalid params | Positional array parameters passed instead of named object, or missing required tool arguments. |
| `-32603` | Internal error | Unhandled runtime exception within tool execution. |

---

## 🔧 Troubleshooting & Common Questions

#### 1. Why does Cursor or Claude report "Server disconnected"?
Ensure your Python environment has `tasleemat` installed in the exact Python interpreter configured:
```bash
# Verify CLI runs cleanly from the environment
python3 -m tasleemat.mcp --help
```
If using a virtualenv, specify the full path to `python3` in your configuration (e.g. `/home/user/venv/bin/python3`).

#### 2. Stdio Buffering in Shell Scripts
When communicating with the server over pipes, ensure unbuffered output or explicit newlines:
```bash
python3 -u -m tasleemat.mcp
```

#### 3. Re-validating AI Drafts in Strict vs. Draft Mode
Use `mode="draft"` when generating incomplete sections during agent drafting loops. Use `mode="strict"` only prior to formal stage-gate submission to ensure 100% required field presence and baseline completeness.
