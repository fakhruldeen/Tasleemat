"""
tasleemat.tui.integrations.cursor
Configures Cursor IDE with the Tasleemat MCP server and governance rules.
"""

import json
import pathlib

def configure_cursor(workspace_path: pathlib.Path) -> list[str]:
    """
    Configures Cursor in the target workspace:
    1. Creates/updates .cursor/mcp.json pointing to tasleemat-mcp.
    2. Writes .cursor/rules/tasleemat-pmo.mdc containing PMO governance rules.
    Returns list of modified/created file paths.
    """
    actions = []
    cursor_dir = workspace_path / ".cursor"
    rules_dir = cursor_dir / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)

    # 1. .cursor/mcp.json
    mcp_file = cursor_dir / "mcp.json"
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

    # 2. .cursor/rules/tasleemat-pmo.mdc
    rule_file = rules_dir / "tasleemat-pmo.mdc"
    rule_content = """---
description: Enterprise Bilingual (EN/AR) PMO Operating System rules and artifact generation
globs: *
alwaysApply: false
---

# Tasleemat PMO Governance & Deliverables Rule

When assisting with project management, creating project plans, or drafting deliverables:
- Use official Tasleemat Form IDs (e.g. `PMO-03.01` for Project Charter, `PMO-04.08.02` for Risk Register, `PMO-06.01` for Status Report).
- Maintain 1:1 bilingual symmetry between English and Arabic.
- Preserve Document Control and Sign-off metadata blocks for practitioner review.
- Reference standard project management practices and terminology.
- Use `tasleemat-mcp` tools (`tasleemat_get_asset`, `tasleemat_validate_data`, `tasleemat_render_artifact`) to fetch templates and validate structured project data.
- Note: Structural data validation confirms schema compliance only; it does not replace independent stakeholder review, formal stage-gate approval, or organizational sign-off.
"""
    rule_file.write_text(rule_content, encoding="utf-8")
    actions.append(str(rule_file))

    return actions
