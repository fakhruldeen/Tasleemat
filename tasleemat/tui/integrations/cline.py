"""
tasleemat.tui.integrations.cline
Configures Cline & Roo Code with the Tasleemat MCP server and .clinerules.
"""

import os
import sys
import json
import pathlib

def get_cline_global_settings_path() -> pathlib.Path:
    """Determine OS-specific path for Cline VS Code extension MCP settings."""
    home = pathlib.Path.home()
    if sys.platform == "darwin":
        return home / "Library" / "Application Support" / "Code" / "User" / "globalStorage" / "saoudrizwan.claude-dev" / "settings" / "cline_mcp_settings.json"
    elif sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        base = pathlib.Path(appdata) if appdata else (home / "AppData" / "Roaming")
        return base / "Code" / "User" / "globalStorage" / "saoudrizwan.claude-dev" / "settings" / "cline_mcp_settings.json"
    else:
        return home / ".config" / "Code" / "User" / "globalStorage" / "saoudrizwan.claude-dev" / "settings" / "cline_mcp_settings.json"

def configure_cline(workspace_path: pathlib.Path, configure_global: bool = True) -> list[str]:
    """
    Configures Cline:
    1. Creates .cline/mcp.json in workspace.
    2. Writes .clinerules in workspace root.
    3. Safely updates global cline_mcp_settings.json if available.
    Returns list of modified/created file paths.
    """
    actions = []
    cline_dir = workspace_path / ".cline"
    cline_dir.mkdir(parents=True, exist_ok=True)

    # 1. .cline/mcp.json
    mcp_file = cline_dir / "mcp.json"
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

    # 2. .clinerules in workspace root
    rules_file = workspace_path / ".clinerules"
    rules_content = """# Cline & Roo Code PMO Operating System Instructions

When assisting with this repository:
1. Deliverable Identification: All deliverables use standard Tasleemat codes (e.g., `PMO-03.01` for Project Charter, `PMO-04.08.02` for Risk Register).
2. Bilingual Parity: Deliverables exist as symmetric English (`en/`) and Arabic (`ar/`) pairs. Ensure changes preserve parity.
3. MCP Server: Use `tasleemat-mcp` tools (`tasleemat_get_asset`, `tasleemat_validate_data`, `tasleemat_render_artifact`) to fetch templates and validate structured project data.
4. Schema Conformance: Complete deliverables must conform to their companion JSON schema.
"""
    rules_file.write_text(rules_content, encoding="utf-8")
    actions.append(str(rules_file))

    # 3. Global Cline settings
    if configure_global:
        try:
            global_path = get_cline_global_settings_path()
            if global_path.parent.exists():
                g_data = {"mcpServers": {}}
                if global_path.exists():
                    try:
                        with open(global_path, "r", encoding="utf-8") as f:
                            g_data = json.load(f)
                    except Exception:
                        g_data = {"mcpServers": {}}
                if "mcpServers" not in g_data:
                    g_data["mcpServers"] = {}
                g_data["mcpServers"]["tasleemat"] = {
                    "command": "tasleemat-mcp"
                }
                with open(global_path, "w", encoding="utf-8") as f:
                    json.dump(g_data, f, indent=2, ensure_ascii=False)
                actions.append(str(global_path))
        except Exception:
            pass

    return actions
