"""
tasleemat.tui.integrations.manager
Unified manager for detecting and applying agent integrations across workspaces.
"""

import pathlib
from tasleemat.tui.integrations.cursor import configure_cursor
from tasleemat.tui.integrations.agy import configure_agy
from tasleemat.tui.integrations.claude import configure_claude
from tasleemat.tui.integrations.vscode import configure_vscode
from tasleemat.tui.integrations.opencode import configure_opencode
from tasleemat.tui.integrations.cline import configure_cline
from tasleemat.tui.integrations.windsurf import configure_windsurf
from tasleemat.tui.integrations.openai_cli import configure_openai_cli

SUPPORTED_AGENTS = {
    "cursor": {
        "id": "cursor",
        "name": "Cursor IDE",
        "desc": "Configures .cursor/mcp.json and installs PMO governance rules",
        "fn": configure_cursor
    },
    "agy": {
        "id": "agy",
        "name": "Antigravity (AGY)",
        "desc": "Configures AGY MCP server and installs pmo-governance skill",
        "fn": configure_agy
    },
    "claude": {
        "id": "claude",
        "name": "Claude Desktop",
        "desc": "Appends tasleemat-mcp to system claude_desktop_config.json",
        "fn": configure_claude
    },
    "vscode": {
        "id": "vscode",
        "name": "VS Code (Standard)",
        "desc": "Configures .vscode/mcp.json and copies AGENT_GUIDE.md",
        "fn": configure_vscode
    },
    "opencode": {
        "id": "opencode",
        "name": "OpenCode",
        "desc": "Configures .opencode/mcp.json and OPENCODE.md guidelines",
        "fn": configure_opencode
    },
    "cline": {
        "id": "cline",
        "name": "Cline / Roo Code",
        "desc": "Configures .cline/mcp.json and writes .clinerules in workspace",
        "fn": configure_cline
    },
    "windsurf": {
        "id": "windsurf",
        "name": "Windsurf (Codeium)",
        "desc": "Configures .windsurf/mcp.json and writes .windsurfrules in workspace",
        "fn": configure_windsurf
    },
    "openai_cli": {
        "id": "openai_cli",
        "name": "OpenAI CLI Replica",
        "desc": "Generates .openai/ tools schema and interactive agent_runner.py",
        "fn": configure_openai_cli
    }
}

def detect_existing_integrations(workspace_path: pathlib.Path) -> dict[str, bool]:
    """Detect which agent integrations are already configured in the workspace."""
    results = {}
    results["cursor"] = (workspace_path / ".cursor" / "mcp.json").exists()
    results["agy"] = (workspace_path / ".antigravityrules").exists() or (workspace_path / "skills" / "pmo-governance").exists()
    results["claude"] = (workspace_path / "CLAUDE.md").exists()
    results["vscode"] = (workspace_path / ".vscode" / "mcp.json").exists()
    results["opencode"] = (workspace_path / ".opencode" / "mcp.json").exists() or (workspace_path / "OPENCODE.md").exists()
    results["cline"] = (workspace_path / ".cline" / "mcp.json").exists() or (workspace_path / ".clinerules").exists()
    results["windsurf"] = (workspace_path / ".windsurf" / "mcp.json").exists() or (workspace_path / ".windsurfrules").exists()
    results["openai_cli"] = (workspace_path / ".openai" / "agent_runner.py").exists() or (workspace_path / ".openai" / "tools.json").exists()
    return results

def apply_selected_integrations(workspace_path: pathlib.Path, selected_agents: list[str]) -> dict[str, list[str]]:
    """
    Applies the selected agent integrations to the workspace.
    Returns mapping of agent_id -> list of created/modified file paths.
    """
    workspace_path = pathlib.Path(workspace_path).resolve()
    workspace_path.mkdir(parents=True, exist_ok=True)
    report = {}

    for agent_id in selected_agents:
        if agent_id in SUPPORTED_AGENTS:
            handler = SUPPORTED_AGENTS[agent_id]["fn"]
            try:
                modified = handler(workspace_path)
                report[agent_id] = modified
            except Exception as e:
                report[agent_id] = [f"Error: {e}"]

    return report
