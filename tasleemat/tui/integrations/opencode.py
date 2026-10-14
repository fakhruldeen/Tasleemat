"""
tasleemat.tui.integrations.opencode
Configures OpenCode with the Tasleemat MCP server and governance guidelines.
"""

import json
import pathlib

def configure_opencode(workspace_path: pathlib.Path) -> list[str]:
    """
    Configures OpenCode:
    1. Creates .opencode/mcp.json.
    2. Writes OPENCODE.md in workspace.
    Returns list of modified/created file paths.
    """
    actions = []
    opencode_dir = workspace_path / ".opencode"
    opencode_dir.mkdir(parents=True, exist_ok=True)

    # 1. .opencode/mcp.json
    mcp_file = opencode_dir / "mcp.json"
    mcp_data = {"mcpServers": {}}
    if mcp_file.exists():
        try:
            with open(mcp_file, "r", encoding="utf-8") as f:
                mcp_data = json.load(f)
        except Exception:
            mcp_data = {"mcpServers": {}}

    if "mcpServers" not in mcp_data:
        mcp_data["mcpServers"] = {}

    mcp_data["mcpServers"]["tasleemat"] = {
        "command": "tasleemat-mcp"
    }

    with open(mcp_file, "w", encoding="utf-8") as f:
        json.dump(mcp_data, f, indent=2, ensure_ascii=False)
    actions.append(str(mcp_file))

    # 2. OPENCODE.md in workspace
    guide_file = workspace_path / "OPENCODE.md"
    guide_content = """# 🚀 OpenCode PMO Governance Integration

This repository follows the **Tasleemat PMO Operating System**.

### OpenCode Guidelines:
- **Canonical Deliverables:** Use official Form IDs (e.g. `PMO-03.01` for Project Charter, `PMO-04.08.02` for Risk Register).
- **Bilingual Standard:** Maintain 1:1 symmetry between English (`en/`) and Arabic (`ar/`) templates.
- **MCP Tool Protocol:** Use `tasleemat_get_asset` to retrieve blank templates or AI prompts, and use `tasleemat_validate_data` to ensure JSON data fields meet structural schema requirements.
- **Stage-Gate Integrity:** Do not delete Document Control tables or Stage-Gate sign-off sections.
"""
    guide_file.write_text(guide_content, encoding="utf-8")
    actions.append(str(guide_file))

    return actions
