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
| `tasleemat_get_artifact` | Get metadata and SHA-256 fingerprint for a deliverable | `artifact_id: string` (e.g. `PMO-03.01`) |
| `tasleemat_get_asset` | Retrieve template, guide, prompt, schema, or example | `artifact_id: string`, `role: string`, `lang?: string` |
| `tasleemat_get_lexicon` | Search bilingual PMI & DGA PMO terminology | `category?: string`, `query?: string` |
| `tasleemat_validate_data` | Validate structured artifact data against JSON schema | `artifact_id: string`, `data: object`, `mode?: "strict" \| "draft"` |
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
- **Command:** `python3 -m tasleemat.mcp`

Or configure via `.cursor/mcp.json` in your workspace root:

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

---

### 3. OpenCode & Agentic IDEs

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
