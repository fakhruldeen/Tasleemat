"""
tasleemat.tui.integrations.vscode
Configures VS Code, Windsurf, Cline, and Roo Code with the Tasleemat MCP server.
"""

import json
import pathlib

def configure_vscode(workspace_path: pathlib.Path) -> list[str]:
    """
    Configures VS Code / Windsurf / Cline:
    1. Creates .vscode/mcp.json.
    2. Writes AGENT_GUIDE.md.
    Returns list of modified/created file paths.
    """
    actions = []
    vscode_dir = workspace_path / ".vscode"
    vscode_dir.mkdir(parents=True, exist_ok=True)

    # 1. .vscode/mcp.json
    mcp_file = vscode_dir / "mcp.json"
    mcp_data = {"servers": {}}
    if mcp_file.exists():
        try:
            with open(mcp_file, "r", encoding="utf-8") as f:
                mcp_data = json.load(f)
        except Exception:
            mcp_data = {"servers": {}}

    if "servers" not in mcp_data:
        mcp_data["servers"] = {}

    mcp_data["servers"]["tasleemat"] = {
        "command": "tasleemat-mcp",
        "type": "stdio"
    }

    with open(mcp_file, "w", encoding="utf-8") as f:
        json.dump(mcp_data, f, indent=2, ensure_ascii=False)
    actions.append(str(mcp_file))

    # 2. AGENT_GUIDE.md
    guide_file = workspace_path / "AGENT_GUIDE.md"
    guide_content = """# 🤖 Agent PMO Instruction Guide

This project workspace was generated using the **Tasleemat PMO Operating System**.

### Primary Instructions for Coding & PM Agents:
- **Deliverable Templates:** All project deliverables follow standard PMO codes (e.g., `PMO-03.01`, `PMO-04.08.02`).
- **Bilingual Symmetry:** English (`en/`) and Arabic (`ar/`) templates correspond 1:1. Never delete either language without explicit instruction.
- **MCP Tool Usage:** Use `tasleemat_get_asset` to retrieve blank templates or AI prompts, and use `tasleemat_validate_data` to ensure JSON data fields meet structural schema requirements.
- **Stage-Gate Integrity:** Do not remove Document Control tables or Stage-Gate sign-off sections.
"""
    guide_file.write_text(guide_content, encoding="utf-8")
    actions.append(str(guide_file))

    return actions
