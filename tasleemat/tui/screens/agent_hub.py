"""
tasleemat.tui.screens.agent_hub
Screen for 1-click configuration of AI coding agents (Cursor, AGY, Claude, VS Code).
"""

import os
import pathlib
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.widgets import Static, Input, Button, Label, Checkbox
from tasleemat.tui.i18n import t
from tasleemat.tui.integrations.manager import (
    SUPPORTED_AGENTS,
    apply_selected_integrations,
    detect_existing_integrations,
)

class AgentHubScreen(ScrollableContainer):
    """Screen for connecting workspaces to AI coding agents."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang

    def compose(self) -> ComposeResult:
        with Vertical(classes="panel-container"):
            yield Static(f"### {t('tab_agents', self.lang)}", classes="card-title")
            yield Static("Connect your project workspaces directly to Cursor, Antigravity (AGY), Claude Desktop, and VS Code with 1-click MCP and governance rules.", classes="card-subtitle")

            with Vertical(classes="card"):
                yield Label("Target Project Workspace Path:", classes="form-label")
                default_path = str(pathlib.Path.cwd())
                yield Input(value=default_path, placeholder="Path to workspace root...", id="inp_ws_path")

                yield Label("Select Agents to Connect:", classes="form-label")
                
                with Vertical():
                    yield Checkbox(
                        f"[b]{t('agent_cursor_title', self.lang)}[/b] — {t('agent_cursor_desc', self.lang)}",
                        value=True,
                        id="chk_cursor"
                    )
                    yield Checkbox(
                        f"[b]{t('agent_agy_title', self.lang)}[/b] — {t('agent_agy_desc', self.lang)}",
                        value=True,
                        id="chk_agy"
                    )
                    yield Checkbox(
                        f"[b]{t('agent_claude_title', self.lang)}[/b] — {t('agent_claude_desc', self.lang)}",
                        value=False,
                        id="chk_claude"
                    )
                    yield Checkbox(
                        f"[b]{t('agent_vscode_title', self.lang)}[/b] — {t('agent_vscode_desc', self.lang)}",
                        value=True,
                        id="chk_vscode"
                    )
                    yield Checkbox(
                        f"[b]{t('agent_opencode_title', self.lang)}[/b] — {t('agent_opencode_desc', self.lang)}",
                        value=True,
                        id="chk_opencode"
                    )
                    yield Checkbox(
                        f"[b]{t('agent_cline_title', self.lang)}[/b] — {t('agent_cline_desc', self.lang)}",
                        value=True,
                        id="chk_cline"
                    )
                    yield Checkbox(
                        f"[b]{t('agent_windsurf_title', self.lang)}[/b] — {t('agent_windsurf_desc', self.lang)}",
                        value=True,
                        id="chk_windsurf"
                    )
                    yield Checkbox(
                        f"[b]{t('agent_openai_cli_title', self.lang)}[/b] — {t('agent_openai_cli_desc', self.lang)}",
                        value=True,
                        id="chk_openai_cli"
                    )

                with Horizontal():
                    yield Button(t("btn_apply_agents", self.lang), id="btn_apply_agents", variant="primary")
                    yield Button("🔍 Check Workspace", id="btn_detect_agents", classes="-secondary")

                yield Static("", id="agent_status_message")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        status = self.query_one("#agent_status_message", Static)
        ws_input = self.query_one("#inp_ws_path", Input)
        ws_path = pathlib.Path(ws_input.value.strip()).resolve()

        if event.button.id == "btn_detect_agents":
            if not ws_path.exists():
                status.update(f"⚠️ Directory {ws_path} does not exist yet.")
                return
            detected = detect_existing_integrations(ws_path)
            summary = []
            for k, active in detected.items():
                name = SUPPORTED_AGENTS[k]["name"]
                icon = "✅" if active else "⭕"
                summary.append(f"{icon} {name}")
            status.update(f"Detection results for [b]{ws_path.name}[/b]:\n" + "  •  ".join(summary))

        elif event.button.id == "btn_apply_agents":
            selected = []
            if self.query_one("#chk_cursor", Checkbox).value:
                selected.append("cursor")
            if self.query_one("#chk_agy", Checkbox).value:
                selected.append("agy")
            if self.query_one("#chk_claude", Checkbox).value:
                selected.append("claude")
            if self.query_one("#chk_vscode", Checkbox).value:
                selected.append("vscode")
            if self.query_one("#chk_opencode", Checkbox).value:
                selected.append("opencode")
            if self.query_one("#chk_cline", Checkbox).value:
                selected.append("cline")
            if self.query_one("#chk_windsurf", Checkbox).value:
                selected.append("windsurf")
            if self.query_one("#chk_openai_cli", Checkbox).value:
                selected.append("openai_cli")

            if not selected:
                status.update("⚠️ Please select at least one agent to configure.")
                return

            try:
                report = apply_selected_integrations(ws_path, selected)
                lines = [f"✅ Successfully configured {len(report)} agent integrations in [b]{ws_path}[/b]:"]
                for agent_id, files in report.items():
                    name = SUPPORTED_AGENTS[agent_id]["name"]
                    lines.append(f"  • [b]{name}[/b]:")
                    for f in files:
                        lines.append(f"     └─ {f}")
                status.update("\n".join(lines))
            except Exception as e:
                status.update(f"❌ Failed to install agent integrations: {e}")
