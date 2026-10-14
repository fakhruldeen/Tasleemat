"""
tasleemat.tui.screens.wizard
Interactive 5-step Scaffolding Wizard with Tier Tailoring, Methodology Packs, and Agent Integrations.
"""

import os
import re
import datetime
import hashlib
import pathlib
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.widgets import Static, Input, Select, Button, Label, Checkbox
from tasleemat.tui.i18n import t
from tasleemat.tui.integrations.manager import apply_selected_integrations

TIER_PACKS = {
    "1": {
        "name": "Enterprise (Tier 1)",
        "general": ["PMO-00.01", "PMO-00.02", "PMO-00.03", "PMO-00.04", "PMO-00.05", "PMO-00.06",
                    "PMO-01.01", "PMO-01.02", "PMO-01.03", "PMO-01.04", "PMO-02.01", "PMO-02.02",
                    "PMO-03.01", "PMO-03.02", "PMO-03.03", "PMO-03.04", "PMO-03.05",
                    "PMO-04.01.01", "PMO-04.01.02", "PMO-04.02.01", "PMO-04.02.02", "PMO-04.03.01",
                    "PMO-04.03.02", "PMO-04.04.01", "PMO-04.04.02", "PMO-04.05.01", "PMO-04.06.01",
                    "PMO-04.07.01", "PMO-04.08.01", "PMO-04.08.02", "PMO-04.09.01", "PMO-04.10.01",
                    "PMO-04.11.01", "PMO-04.12.01", "PMO-05.01", "PMO-05.02", "PMO-05.03", "PMO-05.04",
                    "PMO-06.01", "PMO-06.02", "PMO-06.03", "PMO-06.04", "PMO-06.05", "PMO-06.11",
                    "PMO-07.01", "PMO-07.02", "PMO-07.03", "PMO-07.04", "PMO-07.05"],
        "agile": ["PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.02", "PMO-04.02.01", "PMO-04.03.01",
                  "PMO-04.08.02", "PMO-05.01", "PMO-05.04", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"],
        "ai": ["PMO-01.01", "PMO-02.01", "PMO-02.02", "PMO-02.03", "PMO-02.04", "PMO-02.05", "PMO-02.06",
               "PMO-03.01", "PMO-04.01.01", "PMO-04.08.02", "PMO-05.01", "PMO-05.09", "PMO-06.01", "PMO-07.01"],
        "predictive": ["PMO-00.01", "PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.04", "PMO-04.01.01",
                       "PMO-04.02.01", "PMO-04.03.01", "PMO-04.04.01", "PMO-04.05.01", "PMO-04.08.02",
                       "PMO-05.01", "PMO-05.03", "PMO-06.01", "PMO-06.05", "PMO-07.03"],
        "hybrid": ["PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.04", "PMO-04.01.01", "PMO-04.02.01",
                   "PMO-04.03.01", "PMO-04.08.02", "PMO-05.01", "PMO-05.04", "PMO-05.10", "PMO-06.01",
                   "PMO-06.05", "PMO-06.12", "PMO-07.01", "PMO-07.03"]
    },
    "2": {
        "name": "Standard (Tier 2)",
        "general": ["PMO-01.01", "PMO-02.01", "PMO-03.01", "PMO-03.04", "PMO-04.01.01", "PMO-04.02.01",
                    "PMO-04.03.01", "PMO-04.04.01", "PMO-04.08.02", "PMO-05.01", "PMO-05.03",
                    "PMO-06.01", "PMO-07.01", "PMO-07.03"],
        "agile": ["PMO-01.01", "PMO-03.01", "PMO-03.02", "PMO-04.02.01", "PMO-04.08.02", "PMO-05.01",
                  "PMO-05.04", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"],
        "ai": ["PMO-01.01", "PMO-02.02", "PMO-02.03", "PMO-02.05", "PMO-03.01", "PMO-04.08.02",
               "PMO-05.01", "PMO-06.01", "PMO-07.01"],
        "predictive": ["PMO-01.01", "PMO-03.01", "PMO-04.01.01", "PMO-04.02.01", "PMO-04.03.01",
                       "PMO-04.04.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.03"],
        "hybrid": ["PMO-01.01", "PMO-03.01", "PMO-04.01.01", "PMO-04.02.01", "PMO-04.08.02",
                   "PMO-05.01", "PMO-05.10", "PMO-06.01", "PMO-06.12", "PMO-07.01"]
    },
    "3": {
        "name": "Lean / Fast-Track (Tier 3)",
        "general": ["PMO-01.01", "PMO-03.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.03"],
        "agile": ["PMO-03.01", "PMO-03.02", "PMO-04.02.01", "PMO-05.01", "PMO-05.10", "PMO-06.01", "PMO-07.01"],
        "ai": ["PMO-02.03", "PMO-02.05", "PMO-03.01", "PMO-05.01", "PMO-06.01"],
        "predictive": ["PMO-01.01", "PMO-03.01", "PMO-04.02.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.03"],
        "hybrid": ["PMO-03.01", "PMO-04.02.01", "PMO-04.08.02", "PMO-05.01", "PMO-06.01", "PMO-07.01"]
    }
}

def locate_forms_root() -> pathlib.Path:
    """Find the forms directory in repo root or installed package."""
    # Try relative to repo
    curr = pathlib.Path(__file__).resolve()
    for p in curr.parents:
        if (p / "forms").exists():
            return p / "forms"
    # Package data fallback
    import tasleemat
    pkg_dir = pathlib.Path(tasleemat.__file__).parent / "forms"
    if pkg_dir.exists():
        return pkg_dir
    return pathlib.Path.cwd() / "forms"

def find_available_forms(forms_dir: pathlib.Path, lang: str = "en") -> dict[str, pathlib.Path]:
    base_dir = forms_dir / lang
    forms_map = {}
    if not base_dir.exists():
        return forms_map
    pattern = "*_Template.md" if lang == "en" else "*_قالب.md"
    for p in base_dir.rglob(pattern):
        prefix_match = re.match(r"^(\d{2}(?:_\d{2})+)", p.name)
        if prefix_match:
            forms_map[prefix_match.group(1)] = p.parent
    return forms_map

class ScaffolderWizardScreen(ScrollableContainer):
    """Interactive 5-step Scaffolding Wizard."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.forms_dir = locate_forms_root()

    def compose(self) -> ComposeResult:
        with Vertical(classes="panel-container"):
            yield Static(f"### {t('tab_scaffolder', self.lang)}", classes="card-title")
            yield Static("Scaffold a complete, tailored project workspace populated with 5-file deliverable bundles and AI Agent integrations.", classes="card-subtitle")

            # Step 1: Project Identity
            with Vertical(classes="card"):
                yield Static("[b]Step 1: Project Identity & Metadata[/b]", classes="card-title")
                with Horizontal():
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_project_name", self.lang), classes="form-label")
                        yield Input(value="Digital Transformation Platform", id="inp_prj_name")
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_project_code", self.lang), classes="form-label")
                        yield Input(value="PRJ-2026-001", id="inp_prj_code")
                with Horizontal():
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_pm_name", self.lang), classes="form-label")
                        yield Input(value="Lead PM", id="inp_pm_name")
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_sponsor_name", self.lang), classes="form-label")
                        yield Input(value="Executive Sponsor", id="inp_sponsor_name")

            # Step 2 & 3: Governance & Methodology
            with Vertical(classes="card"):
                yield Static("[b]Step 2 & 3: Governance Tailoring & Methodology Pack[/b]", classes="card-title")
                with Horizontal():
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_tier", self.lang), classes="form-label")
                        yield Select(
                            [
                                ("Tier 2: Standard Enterprise (18–25 forms)", "2"),
                                ("Tier 1: Enterprise / Strategic (35–50 forms)", "1"),
                                ("Tier 3: Lean / Fast-Track (7–9 forms)", "3"),
                            ],
                            value="2",
                            id="sel_tier"
                        )
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_pack", self.lang), classes="form-label")
                        yield Select(
                            [
                                (t("pack_general", self.lang), "general"),
                                (t("pack_agile", self.lang), "agile"),
                                (t("pack_ai", self.lang), "ai"),
                                (t("pack_predictive", self.lang), "predictive"),
                                (t("pack_hybrid", self.lang), "hybrid"),
                            ],
                            value="general",
                            id="sel_pack"
                        )

            # Step 4: Language & Output Directory
            with Vertical(classes="card"):
                yield Static("[b]Step 4: Language & Target Workspace[/b]", classes="card-title")
                with Horizontal():
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_lang", self.lang), classes="form-label")
                        yield Select(
                            [
                                (t("lang_both", self.lang), "both"),
                                (t("lang_en", self.lang), "en"),
                                (t("lang_ar", self.lang), "ar"),
                            ],
                            value="both",
                            id="sel_lang"
                        )
                    with Vertical(classes="half-col"):
                        yield Label(t("lbl_out_dir", self.lang), classes="form-label")
                        default_out = str(pathlib.Path.cwd() / "PRJ-2026-001_Workspace")
                        yield Input(value=default_out, id="inp_out_dir")

            # Step 5: Agent Integrations
            with Vertical(classes="card"):
                yield Static("[b]Step 5: Preferred AI Agent Integrations[/b]", classes="card-title")
                yield Static("Configure AI agent MCP connections & governance rules into this workspace upon creation:", classes="card-subtitle")
                with Horizontal():
                    yield Checkbox("Cursor IDE", value=True, id="wiz_chk_cursor")
                    yield Checkbox("Antigravity (AGY)", value=True, id="wiz_chk_agy")
                    yield Checkbox("Claude Desktop", value=False, id="wiz_chk_claude")
                    yield Checkbox("VS Code", value=True, id="wiz_chk_vscode")
                with Horizontal():
                    yield Checkbox("OpenCode", value=True, id="wiz_chk_opencode")
                    yield Checkbox("Cline / Roo", value=True, id="wiz_chk_cline")
                    yield Checkbox("Windsurf", value=True, id="wiz_chk_windsurf")
                    yield Checkbox("OpenAI CLI", value=True, id="wiz_chk_openai_cli")

            # Action & Status
            with Vertical(classes="card"):
                yield Button(t("btn_scaffold", self.lang), id="btn_run_scaffold", variant="primary")
                yield Static("", id="wizard_status")

    def on_input_changed(self, event: Input.Changed) -> None:
        if event.input.id == "inp_prj_code":
            code = event.value.strip() or "PRJ-2026-001"
            out_inp = self.query_one("#inp_out_dir", Input)
            out_inp.value = str(pathlib.Path.cwd() / f"{code}_Workspace")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_run_scaffold":
            self.execute_scaffold()

    def execute_scaffold(self) -> None:
        status = self.query_one("#wizard_status", Static)
        name = self.query_one("#inp_prj_name", Input).value.strip() or "New Initiative"
        code = self.query_one("#inp_prj_code", Input).value.strip() or "PRJ-2026-001"
        pm = self.query_one("#inp_pm_name", Input).value.strip() or "Lead PM"
        sponsor = self.query_one("#inp_sponsor_name", Input).value.strip() or "Executive Sponsor"
        tier = str(self.query_one("#sel_tier", Select).value)
        pack = str(self.query_one("#sel_pack", Select).value)
        lang_sel = str(self.query_one("#sel_lang", Select).value)
        out_str = self.query_one("#inp_out_dir", Input).value.strip()
        out_dir = pathlib.Path(out_str).resolve()
        date_str = datetime.date.today().isoformat()

        selected_ids = TIER_PACKS.get(tier, {}).get(pack, TIER_PACKS["2"]["general"])
        target_langs = ["en", "ar"] if lang_sel == "both" else [lang_sel]

        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            scaffolded_count = 0

            for l in target_langs:
                lang_dir = out_dir / l
                lang_dir.mkdir(parents=True, exist_ok=True)
                forms_map = find_available_forms(self.forms_dir, l)

                for item_id in selected_ids:
                    clean_id = item_id.replace("PMO-", "").replace(".", "_")
                    matched_folder = None
                    for k, folder in forms_map.items():
                        if k == clean_id or k.endswith(clean_id) or clean_id.endswith(k):
                            matched_folder = folder
                            break

                    if matched_folder and matched_folder.exists():
                        dest_folder = lang_dir / matched_folder.relative_to(self.forms_dir / l)
                        dest_folder.mkdir(parents=True, exist_ok=True)

                        for item in matched_folder.iterdir():
                            if item.is_file():
                                content = item.read_text(encoding="utf-8")
                                content = content.replace("{{اسم_المشروع}}", name).replace("{{Project_Name}}", name)
                                content = content.replace("{{معرف_المشروع}}", code).replace("{{Project_ID}}", code).replace("{{Project_Code}}", code)
                                content = content.replace("{{اسم_مدير_المشروع}}", pm).replace("{{Project_Manager}}", pm)
                                content = content.replace("{{اسم_راعي_المشروع}}", sponsor).replace("{{Sponsor_Name}}", sponsor)
                                content = content.replace("{{التاريخ_الحالي}}", date_str).replace("{{Current_Date}}", date_str)
                                content = content.replace("{{اسم_الشركة}}", "حلول القمة المؤسسية (Apex Solutions)").replace("{{Company_Name}}", "Apex Enterprise Solutions")

                                content_for_hash = content.replace("{{رمز_تجزئة_التدقيق_SHA256}}", "").replace("{{Audit_Trail_SHA256_Hash}}", "")
                                audit_hash = hashlib.sha256(content_for_hash.encode("utf-8")).hexdigest()
                                content = content.replace("{{رمز_تجزئة_التدقيق_SHA256}}", audit_hash).replace("{{Audit_Trail_SHA256_Hash}}", audit_hash)

                                content = re.sub(r'(\*\*اسم المشروع:\*\*|\*\*Project Name:\*\*)\s*\[.*?\]', rf'\1 {name}', content)
                                content = re.sub(r'(\*\*رمز المشروع:\*\*|\*\*Project ID:\*\*|\*\*Project Code:\*\*)\s*\[.*?\]', rf'\1 {code}', content)
                                content = re.sub(r'(\*\*مدير المشروع:\*\*|\*\*Project Manager:\*\*)\s*\[.*?\]', rf'\1 {pm}', content)
                                content = re.sub(r'(\*\*راعي المشروع:\*\*|\*\*Project Sponsor:\*\*)\s*\[.*?\]', rf'\1 {sponsor}', content)
                                content = re.sub(r'(\*\*تاريخ الوثيقة:\*\*|\*\*Date:\*\*)\s*\[.*?\]', rf'\1 {date_str}', content)

                                (dest_folder / item.name).write_text(content, encoding="utf-8")
                        scaffolded_count += 1

            # Build PROJECT_README.md
            readme = f"# 📋 {name} (`{code}`) — Project Management Workspace\n"
            readme += f"**Governance Tier:** Tier {tier} | **Methodology Pack:** {pack.upper()} | **Date:** {date_str}  \n"
            readme += f"**Project Manager:** {pm} | **Project Sponsor:** {sponsor}  \n\n---\n\n## 🎯 Deliverables & Stage-Gate Checklist\n"
            for l in target_langs:
                readme += f"\n### 📂 Deliverables ({'Arabic' if l == 'ar' else 'English'})\n"
                for fid in sorted(selected_ids):
                    readme += f"- [ ] **`{fid}`** — `[{l.upper()}]` [Open Deliverable Folder]({l}/)\n"
            (out_dir / "PROJECT_README.md").write_text(readme, encoding="utf-8")

            # Apply Agent Integrations
            def _is_checked(selector: str) -> bool:
                try:
                    w = self.query_one(selector, Checkbox)
                    return bool(getattr(w, "value", False))
                except Exception:
                    return False

            agents_to_apply = []
            if _is_checked("#wiz_chk_cursor"):
                agents_to_apply.append("cursor")
            if _is_checked("#wiz_chk_agy"):
                agents_to_apply.append("agy")
            if _is_checked("#wiz_chk_claude"):
                agents_to_apply.append("claude")
            if _is_checked("#wiz_chk_vscode"):
                agents_to_apply.append("vscode")
            if _is_checked("#wiz_chk_opencode"):
                agents_to_apply.append("opencode")
            if _is_checked("#wiz_chk_cline"):
                agents_to_apply.append("cline")
            if _is_checked("#wiz_chk_windsurf"):
                agents_to_apply.append("windsurf")
            if _is_checked("#wiz_chk_openai_cli"):
                agents_to_apply.append("openai_cli")

            agent_report = apply_selected_integrations(out_dir, agents_to_apply)

            status.update(
                f"✅ [b]Successfully scaffolded project workspace![/b]\n"
                f"📁 Destination: [cyan]{out_dir}[/cyan]\n"
                f"📦 Bundles: [green]{scaffolded_count}[/green] deliverables ({lang_sel.upper()})\n"
                f"🤖 Configured Agents: [magenta]{', '.join(agent_report.keys())}[/magenta]"
            )
        except Exception as e:
            status.update(f"❌ Error during scaffolding: {e}")
