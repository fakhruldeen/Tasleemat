"""
tasleemat.tui.integrations.claude
Configures Claude Desktop and Claude Code with the Tasleemat MCP server.
"""

import os
import sys
import json
import pathlib

def get_claude_desktop_config_path() -> pathlib.Path:
    """Determine OS-specific path for claude_desktop_config.json."""
    home = pathlib.Path.home()
    if sys.platform == "darwin":
        return home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        base = pathlib.Path(appdata) if appdata else (home / "AppData" / "Roaming")
        return base / "Claude" / "claude_desktop_config.json"
    else:
        # Linux / Unix
        return home / ".config" / "Claude" / "claude_desktop_config.json"

def configure_claude(workspace_path: pathlib.Path, configure_desktop: bool = True) -> list[str]:
    """
    Configures Claude:
    1. Writes CLAUDE.md inside the target workspace.
    2. Safely updates claude_desktop_config.json with the tasleemat MCP server.
    Returns list of modified/created file paths.
    """
    actions = []

    # 1. CLAUDE.md in workspace
    claude_md = workspace_path / "CLAUDE.md"
    claude_md_content = """# Tasleemat PMO Governance Guide for Claude

This project uses the **Tasleemat PMO Operating System**.
When generating, updating, or reviewing project management deliverables:
- Use official Form IDs (e.g., `PMO-03.01` for Project Charter, `PMO-04.08.02` for Risk Register).
- Support English and Arabic 1:1 bilingual symmetry.
- Ensure all deliverables follow the 5-file bundle standard (Template, Guide, Prompt, Schema, Dictionary).
- Use `tasleemat-mcp` tools when available to retrieve canonical definitions and validate schemas.
"""
    claude_md.write_text(claude_md_content, encoding="utf-8")
    actions.append(str(claude_md))

    # 2. Claude Desktop system config
    if configure_desktop:
        try:
            cfg_path = get_claude_desktop_config_path()
            cfg_path.parent.mkdir(parents=True, exist_ok=True)
            cfg_data = {}
            if cfg_path.exists():
                try:
                    with open(cfg_path, "r", encoding="utf-8") as f:
                        cfg_data = json.load(f)
                except Exception:
                    cfg_data = {}
            
            if "mcpServers" not in cfg_data:
                cfg_data["mcpServers"] = {}

            cfg_data["mcpServers"]["tasleemat"] = {
                "command": "tasleemat-mcp"
            }

            with open(cfg_path, "w", encoding="utf-8") as f:
                json.dump(cfg_data, f, indent=2, ensure_ascii=False)
            actions.append(str(cfg_path))
        except Exception:
            pass

    return actions
