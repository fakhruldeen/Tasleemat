"""
tasleemat.tui.screens.explorer
Split-pane Deliverables Catalog Explorer (114 forms) with Live Markdown preview and schema tabs.
"""

from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Tree, MarkdownViewer, Button, Tabs, Tab
from textual.widgets.tree import TreeNode
from tasleemat.tui.i18n import t
from tasleemat.catalog import list_artifacts, get_artifact_definition, get_artifact_asset

PHASES = [
    ("00", "00 Portfolio & Program (المحفظة والبرامج)"),
    ("01", "01 Business & Value (الأعمال والقيمة)"),
    ("02", "02 Approach & Tailoring (المنهجية والتكييف)"),
    ("03", "03 Initiating (البدء والتفويض)"),
    ("04", "04 Planning (التخطيط المتكامل)"),
    ("05", "05 Executing (التنفيذ والتسليم)"),
    ("06", "06 Monitoring & Controlling (المتابعة والتحكم)"),
    ("07", "07 Closing (الإغلاق والتقييم)"),
]

class DeliverablesExplorerScreen(Vertical):
    """Split-pane Explorer for 114 PMO Deliverables."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.current_artifact_id = "PMO-03.01"
        self.current_role = "template"
        self.all_artifacts = list_artifacts()

    def compose(self) -> ComposeResult:
        with Horizontal():
            # Left pane: Tree & Search
            with Vertical(id="split_left"):
                yield Static(f"### {t('tab_catalog', self.lang)}", classes="card-title")
                yield Input(placeholder="🔍 Search ID or name...", id="inp_search_forms")
                yield Tree("📦 PMO Lifecycle Phases", id="tree_phases")

            # Right pane: Artifact Header, Tabs, Markdown Viewer
            with Vertical(id="split_right"):
                yield Static("", id="artifact_header", classes="card")
                yield Tabs(
                    Tab("📄 Template (القالب)", id="tab_role_template"),
                    Tab("📖 Guide (الدليل)", id="tab_role_guide"),
                    Tab("🤖 Prompt (موجه الذكاء)", id="tab_role_prompt"),
                    Tab("🗄️ Schema (المخطط)", id="tab_role_schema"),
                    id="tabs_roles"
                )
                yield MarkdownViewer("", show_table_of_contents=False, id="md_viewer")

    def on_mount(self) -> None:
        self.populate_tree()
        self.load_artifact("PMO-03.01")

    def populate_tree(self, filter_query: str = "") -> None:
        tree = self.query_one("#tree_phases", Tree)
        tree.clear()
        tree.root.expand()

        filter_q = filter_query.lower().strip()

        for phase_code, phase_title in PHASES:
            phase_artifacts = [
                a for a in self.all_artifacts 
                if a.phase_code == phase_code and (
                    not filter_q or 
                    filter_q in a.artifact_id.lower() or 
                    filter_q in a.name_en.lower() or 
                    filter_q in a.name_ar.lower()
                )
            ]
            if phase_artifacts or not filter_q:
                node = tree.root.add(f"{phase_code} - {phase_title}", expand=bool(filter_q or phase_code == "03"))
                for art in phase_artifacts:
                    node.add_leaf(f"{art.artifact_id}: {art.name_en}", data=art.artifact_id)

    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "inp_search_forms":
            self.populate_tree(event.value)

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        if event.node.data:
            self.load_artifact(event.node.data)

    def on_tabs_tab_activated(self, event: Tabs.TabActivated) -> None:
        role_map = {
            "tab_role_template": "template",
            "tab_role_guide": "guide",
            "tab_role_prompt": "prompt",
            "tab_role_schema": "schema",
        }
        tab_id = getattr(event.tab, "id", None)
        if tab_id in role_map:
            self.current_role = role_map[tab_id]
            self.update_content()

    def load_artifact(self, artifact_id: str) -> None:
        self.current_artifact_id = artifact_id
        try:
            defn = get_artifact_definition(artifact_id)
            name_en = defn.get("name_en", "")
            name_ar = defn.get("name_ar", "")
            phase_en = defn.get("phase_name_en", "")
            tiers = ", ".join(defn.get("tiers", []))
            gate = defn.get("stage_gate", "N/A")

            header_widget = self.query_one("#artifact_header", Static)
            header_widget.update(
                f"[b cyan]{artifact_id}: {name_en}[/b cyan] | [b yellow]{name_ar}[/b yellow]\n"
                f"[dim]Phase:[/dim] {phase_en} | [dim]Governance Tiers:[/dim] [green]{tiers}[/green] | [dim]Gate:[/dim] [magenta]{gate}[/magenta]"
            )
        except Exception:
            pass

        self.update_content()

    def update_content(self) -> None:
        viewer = self.query_one("#md_viewer", MarkdownViewer)
        try:
            content = get_artifact_asset(self.current_artifact_id, role=self.current_role, lang=self.lang)
            if not content:
                # Fallback to English if Arabic asset is not directly loaded
                content = get_artifact_asset(self.current_artifact_id, role=self.current_role, lang="en")
            
            if self.current_role == "schema":
                viewer.document.update(f"```json\n{content}\n```")
            else:
                viewer.document.update(content or "*No content available for this asset.*")
        except Exception as e:
            viewer.document.update(f"⚠️ Error loading asset for `{self.current_artifact_id}` ({self.current_role}): {e}")
