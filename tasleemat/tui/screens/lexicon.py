"""
tasleemat.tui.screens.lexicon
Bilingual Lexicon & Terminology Explorer with instant fuzzy search and BiDi display.
"""

from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Tree, MarkdownViewer
from tasleemat.tui.i18n import t
from tasleemat.tui.bidi import shape_text
from tasleemat.catalog import get_lexicon

class LexiconScreen(Vertical):
    """Bilingual Lexicon Search & Lookup Screen."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.terms = get_lexicon()
        self.selected_term = self.terms[0] if self.terms else None

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="split_left"):
                yield Static(f"### {t('tab_lexicon', self.lang)}", classes="card-title")
                yield Input(placeholder="🔍 Search term (e.g. Risk, ميثاق, Charter)...", id="inp_search_lex")
                yield Tree("📖 Bilingual Terminology (114)", id="tree_lexicon")

            with Vertical(id="split_right"):
                yield MarkdownViewer("", show_table_of_contents=False, id="lex_md_viewer")

    def on_mount(self) -> None:
        self.populate_tree()
        if self.terms:
            self.load_term(self.terms[0]["code"])

    def populate_tree(self, filter_query: str = "") -> None:
        tree = self.query_one("#tree_lexicon", Tree)
        tree.clear()
        tree.root.expand()

        fq = filter_query.lower().strip()
        filtered = []
        for t in self.terms:
            code = t.get("code", "")
            en = t.get("english_name") or t.get("en_name") or ""
            ar = t.get("arabic_name") or t.get("ar_name") or ""
            grp = t.get("group", "")
            if not fq or fq in code.lower() or fq in en.lower() or fq in ar.lower() or fq in grp.lower():
                filtered.append(t)

        # Group terms by group
        groups = {}
        for item in filtered:
            grp = item.get("group", "General")
            groups.setdefault(grp, []).append(item)

        for grp_name, items in sorted(groups.items()):
            grp_node = tree.root.add(f"📂 {grp_name} ({len(items)})", expand=bool(fq or "Initiating" in grp_name))
            for item in items:
                en = item.get("english_name") or item.get("en_name") or ""
                display_label = f"{item['code']}: {en}"
                grp_node.add_leaf(display_label, data=item["code"])

    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "inp_search_lex":
            self.populate_tree(event.value)

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        if event.node.data:
            self.load_term(event.node.data)

    def load_term(self, code: str) -> None:
        match = next((x for x in self.terms if x.get("code") == code), None)
        if not match:
            return

        self.selected_term = match
        viewer = self.query_one("#lex_md_viewer", MarkdownViewer)

        en_title = match.get("english_name") or match.get("en_name") or ""
        ar_title = match.get("arabic_name") or match.get("ar_name") or ""
        shaped_ar = shape_text(ar_title)

        md = f"# 📖 `{match.get('code', code)}` — {en_title}\n"
        md += f"## {shaped_ar}\n\n"
        md += f"**📂 Category / Phase:** `{match.get('group', 'N/A')}`  \n"
        if match.get("subgroup"):
            md += f"**📑 Subgroup:** `{match.get('subgroup')}`  \n"
        if match.get("pmi_standard_term"):
            md += f"**Standard PMI Term:** `{match.get('pmi_standard_term')}`  \n"

        en_dir = match.get("en_dir") or match.get("en_path") or ""
        ar_dir = match.get("ar_dir") or match.get("ar_path") or ""

        md += "\n---\n\n### 🗂️ Canonical Bilingual File Paths\n"
        md += f"- **English Bundle:** `{en_dir}`\n"
        md += f"- **Arabic Bundle:** `{ar_dir}`\n\n"

        md += "---\n\n### 💡 Standard Alignment\n"
        md += "This deliverable is fully aligned with **PMI PMBOK® (6th, 7th & 8th Edition Ready)**, **ISO 21500 / 21502**, and the **Saudi Digital Government Authority (DGA)** standard project lifecycle governance."

        viewer.document.update(md)
