"""
tasleemat.tui.integrations.windsurf
Configures Windsurf (Codeium) with the Tasleemat MCP server and .windsurfrules.
"""

import os
import json
import pathlib

def configure_windsurf(workspace_path: pathlib.Path, configure_global: bool = True) -> list[str]:
    """
    Configures Windsurf:
    1. Creates .windsurf/mcp.json in workspace.
    2. Writes .windsurfrules in workspace root.
    3. Safely updates global ~/.codeium/windsurf/mcp_config.json if available.
    Returns list of modified/created file paths.
    """
    actions = []
    windsurf_dir = workspace_path / ".windsurf"
    windsurf_dir.mkdir(parents=True, exist_ok=True)

    # 1. .windsurf/mcp.json
    mcp_file = windsurf_dir / "mcp.json"
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

    # 2. .windsurfrules in workspace root
    rules_file = workspace_path / ".windsurfrules"
    rules_content = """# Windsurf Cascade PMO Governance Rules

When generating or editing project management artifacts:
- Follow official Tasleemat deliverable prefixes (e.g. `PMO-03.01` for Project Charter, `PMO-04.08.02` for Risk Register).
- Ensure English and Arabic deliverables are maintained in 1:1 symmetry.
- Preserve all Document Control tables and Stage-Gate sign-off headers.
- Utilize the `tasleemat-mcp` tools for artifact asset retrieval and structural schema validation.
"""
    rules_file.write_text(rules_content, encoding="utf-8")
    actions.append(str(rules_file))

    # 3. Global Windsurf config
    if configure_global:
        try:
            home = pathlib.Path.home()
            global_cfg = home / ".codeium" / "windsurf" / "mcp_config.json"
            global_cfg.parent.mkdir(parents=True, exist_ok=True)
            g_data = {"mcpServers": {}}
            if global_cfg.exists():
                try:
                    with open(global_cfg, "r", encoding="utf-8") as f:
                        g_data = json.load(f)
                except Exception:
                    g_data = {"mcpServers": {}}
            if "mcpServers" not in g_data:
                g_data["mcpServers"] = {}
            g_data["mcpServers"]["tasleemat"] = {
                "command": "tasleemat-mcp"
            }
            with open(global_cfg, "w", encoding="utf-8") as f:
                json.dump(g_data, f, indent=2, ensure_ascii=False)
            actions.append(str(global_cfg))
        except Exception:
            pass

    return actions
