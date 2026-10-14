"""
tasleemat.tui.integrations.agy
Configures Antigravity (AGY) with the Tasleemat MCP server, PMO governance skill, and rules.
"""

import json
import pathlib
import shutil

SKILL_CONTENT = """---
type: Skill
name: pmo-governance
description: Bilingual PMO artifact scaffolding, deliverable retrieval, and structural data validation using Tasleemat.
---

# PMO Governance Skill

This skill equips agents with standard operating procedures for retrieving deliverables and structurally validating completed data payloads using the Tasleemat library.

## Workflow
1. Identify the required deliverable ID using `tasleemat_list_artifacts` or `tasleemat_get_artifact`.
2. Retrieve the official template and practitioner guide using `tasleemat_get_asset`.
3. Populate the deliverable adhering to Document Control headers and metadata conventions.
4. Validate structured payloads across all 114 PMO deliverables using `tasleemat_validate_data` (strict or draft mode).
5. Note: Structural schema validation confirms field types and constraints only; it does not replace human PMO approval, business viability evaluation, or PMI/DGA certification.
"""

def configure_agy(workspace_path: pathlib.Path, install_global_skill: bool = True) -> list[str]:
    """
    Configures Antigravity (AGY):
    1. Writes .gemini/settings.json in workspace or mcp config.
    2. Installs pmo-governance skill into ~/.gemini/config/skills/pmo-governance/SKILL.md if global.
    3. Writes AGENT_INSTRUCTIONS.md or .antigravityrules in workspace.
    Returns list of modified/created file paths.
    """
    actions = []
    
    # 1. Workspace rule
    agy_rule = workspace_path / ".antigravityrules"
    rule_content = """# Tasleemat PMO Governance & Standards for Antigravity (AGY)

When drafting deliverables, analyzing governance, or reviewing project status:
1. Always reference canonical Tasleemat form codes (e.g. PMO-03.01 for Project Charter, PMO-04.08.02 for Risk Register).
2. Adhere to 1:1 bilingual parity (Arabic & English).
3. Validate data payloads against official JSON schemas via `tasleemat_validate_data`.
4. Ensure compliance with PMI PMBOK® 7th/8th edition standards and Saudi DGA governance mandates.
"""
    agy_rule.write_text(rule_content, encoding="utf-8")
    actions.append(str(agy_rule))

    # 2. Workspace skills directory
    ws_skill_dir = workspace_path / "skills" / "pmo-governance"
    ws_skill_dir.mkdir(parents=True, exist_ok=True)
    ws_skill_file = ws_skill_dir / "SKILL.md"
    ws_skill_file.write_text(SKILL_CONTENT, encoding="utf-8")
    actions.append(str(ws_skill_file))

    # 3. Global skill if user directory exists
    if install_global_skill:
        home = pathlib.Path.home()
        global_skill_dir = home / ".gemini" / "config" / "skills" / "pmo-governance"
        try:
            global_skill_dir.mkdir(parents=True, exist_ok=True)
            global_skill_file = global_skill_dir / "SKILL.md"
            global_skill_file.write_text(SKILL_CONTENT, encoding="utf-8")
            actions.append(str(global_skill_file))
        except Exception:
            pass

    return actions
