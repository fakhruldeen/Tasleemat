"""
tasleemat.tui.app
Main Textual Application for the Tasleemat Bilingual PMO Operating System.
"""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, Horizontal
from textual.widgets import Header, Footer, Static, Tabs, Tab, ContentSwitcher
from tasleemat.tui.theme import TUI_CSS
from tasleemat.tui.i18n import t
from tasleemat.tui.screens.wizard import ScaffolderWizardScreen
from tasleemat.tui.screens.explorer import DeliverablesExplorerScreen
from tasleemat.tui.screens.gates import StageGatesScreen
from tasleemat.tui.screens.lexicon import LexiconScreen
from tasleemat.tui.screens.ai_studio import AIStudioScreen
from tasleemat.tui.screens.llm_config import LLMConfigScreen
from tasleemat.tui.screens.agent_hub import AgentHubScreen
from tasleemat.tui.screens.auditor import AuditorScreen

class TasleematApp(App):
    """Tasleemat PMO Operating System TUI Application."""

    CSS = TUI_CSS
    TITLE = "Tasleemat (تسليمات)"
    SUB_TITLE = "Enterprise Bilingual PMO & AI Toolkit"

    BINDINGS = [
        Binding("f1", "app_help", "Help", show=True),
        Binding("f2", "toggle_lang", "EN / العربية", show=True),
        Binding("f10", "quit", "Quit", show=True),
        Binding("ctrl+q", "quit", "Quit", show=False),
    ]

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang

    def compose(self) -> ComposeResult:
        with Vertical(id="header_container"):
            with Horizontal():
                yield Static(f"🚀 {t('app_title', self.lang)}", id="header_title")
                yield Static(f"[b]Mode:[/b] [{self.lang.upper()}] | [b]F2:[/b] Switch Language", id="header_meta")

        yield Tabs(
            Tab(t("tab_scaffolder", self.lang), id="tab_scaffolder"),
            Tab(t("tab_catalog", self.lang), id="tab_catalog"),
            Tab(t("tab_gates", self.lang), id="tab_gates"),
            Tab(t("tab_lexicon", self.lang), id="tab_lexicon"),
            Tab(t("tab_ai_studio", self.lang), id="tab_ai_studio"),
            Tab(t("tab_llm_config", self.lang), id="tab_llm_config"),
            Tab(t("tab_agents", self.lang), id="tab_agents"),
            Tab(t("tab_auditor", self.lang), id="tab_auditor"),
            id="main_nav_tabs"
        )

        with ContentSwitcher(initial="tab_scaffolder", id="main_content_switcher"):
            yield ScaffolderWizardScreen(lang=self.lang, id="screen_scaffolder")
            yield DeliverablesExplorerScreen(lang=self.lang, id="screen_catalog")
            yield StageGatesScreen(lang=self.lang, id="screen_gates")
            yield LexiconScreen(lang=self.lang, id="screen_lexicon")
            yield AIStudioScreen(lang=self.lang, id="screen_ai_studio")
            yield LLMConfigScreen(lang=self.lang, id="screen_llm_config")
            yield AgentHubScreen(lang=self.lang, id="screen_agents")
            yield AuditorScreen(lang=self.lang, id="screen_auditor")

        yield Footer()

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        switcher = self.query_one("#main_content_switcher", ContentSwitcher)
        tab_id = getattr(event.tab, "id", None)
        mapping = {
            "tab_scaffolder": "screen_scaffolder",
            "tab_catalog": "screen_catalog",
            "tab_gates": "screen_gates",
            "tab_lexicon": "screen_lexicon",
            "tab_ai_studio": "screen_ai_studio",
            "tab_llm_config": "screen_llm_config",
            "tab_agents": "screen_agents",
            "tab_auditor": "screen_auditor",
        }
        if tab_id in mapping:
            switcher.current = mapping[tab_id]

    def action_toggle_lang(self) -> None:
        self.lang = "ar" if self.lang == "en" else "en"
        meta = self.query_one("#header_meta", Static)
        meta.update(f"[b]Mode:[/b] [{self.lang.upper()}] | [b]F2:[/b] Switch Language")
        title = self.query_one("#header_title", Static)
        title.update(f"🚀 {t('app_title', self.lang)}")
        self.notify(f"Interface language set to: {self.lang.upper()}", title="Language Switched")

    def action_app_help(self) -> None:
        self.notify(
            "Tasleemat TUI Navigation:\n"
            "• [F2] Toggle English / Arabic\n"
            "• [Tabs] Switch between Scaffolder, Catalog, Gates, Lexicon, AI Studio, LLM API, and Agents\n"
            "• [F10 / Ctrl+Q] Exit to terminal",
            title="Help Reference",
            timeout=8
        )

def run_tui(lang: str = "en"):
    """Entrypoint function to run the Textual application."""
    app = TasleematApp(lang=lang)
    app.run()

if __name__ == "__main__":
    run_tui()
