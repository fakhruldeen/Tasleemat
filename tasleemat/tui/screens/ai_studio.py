"""
tasleemat.tui.screens.ai_studio
AI Deliverable Drafting Studio for auto-filling PMO templates using configured LLM providers.
"""

import pathlib
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.widgets import Static, Input, Select, Button, Label, MarkdownViewer, TextArea
from tasleemat.tui.i18n import t
from tasleemat.catalog import list_artifacts, get_artifact_asset
from tasleemat.ai import AIClient, load_config

class AIStudioScreen(ScrollableContainer):
    """AI Studio for drafting deliverables with LLMs."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.artifacts = list_artifacts()
        self.generated_content = ""

    def compose(self) -> ComposeResult:
        with Vertical(classes="panel-container"):
            yield Static(f"### {t('tab_ai_studio', self.lang)}", classes="card-title")
            yield Static("Draft production-ready PMO deliverables using your configured LLM provider and official Tasleemat prompt schemas.", classes="card-subtitle")

            with Vertical(classes="card"):
                yield Label("Select Deliverable to Generate:", classes="form-label")
                art_options = [
                    (f"{a.artifact_id}: {a.name_en}", a.artifact_id)
                    for a in self.artifacts
                ]
                yield Select(art_options, value="PMO-03.01", id="sel_studio_art")

                yield Label("Output Language:", classes="form-label")
                yield Select(
                    [("English (en)", "en"), ("Arabic (العربية)", "ar")],
                    value=self.lang,
                    id="sel_studio_lang"
                )

                yield Label("Project Notes & Meeting Context:", classes="form-label")
                yield TextArea(
                    "Project Goal: Build a secure, high-throughput digital payments gateway for enterprise clients.\nBudget: $1.8M USD. Target Timeline: 9 months.\nKey Stakeholders: Head of Digital Banking, Enterprise Security Director.\nKey Risks: Regulatory compliance sign-off delay, legacy core banking integration.",
                    id="txt_studio_notes",
                    language="markdown"
                )

                with Horizontal():
                    yield Button(t("btn_generate", self.lang), id="btn_studio_generate", variant="primary")
                    yield Button("Mock Offline Test", id="btn_studio_mock", classes="-secondary")

                yield Static("", id="studio_status")

            with Vertical(classes="card"):
                yield Static("[b]Generated Deliverable Preview:[/b]", classes="card-title")
                yield MarkdownViewer("*Output will appear here after generation...*", id="studio_md_preview")
                with Horizontal():
                    yield Label("Export File Path:", classes="form-label")
                    yield Input(value=str(pathlib.Path.cwd() / "Generated_Deliverable.md"), id="inp_studio_export")
                    yield Button(t("btn_export", self.lang), id="btn_studio_export", variant="success")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        status = self.query_one("#studio_status", Static)
        art_select = self.query_one("#sel_studio_art", Select)
        lang_select = self.query_one("#sel_studio_lang", Select)
        notes_area = self.query_one("#txt_studio_notes", TextArea)

        artifact_id = str(art_select.value)
        out_lang = str(lang_select.value)
        notes = notes_area.text.strip()

        if event.button.id in ["btn_studio_generate", "btn_studio_mock"]:
            is_mock = (event.button.id == "btn_studio_mock")
            cfg = load_config()
            provider = "mock" if is_mock else cfg.get("provider", "gemini")
            model = cfg.get("model", "default")

            status.update(f"⏳ Generating `{artifact_id}` deliverable via {provider} ({model})...")
            self.app.call_later(self._run_generation, artifact_id, out_lang, notes, is_mock)

        elif event.button.id == "btn_studio_export":
            export_path_inp = self.query_one("#inp_studio_export", Input)
            target = pathlib.Path(export_path_inp.value.strip()).resolve()
            if not self.generated_content:
                status.update("⚠️ No generated content to export. Click Generate first.")
                return
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(self.generated_content, encoding="utf-8")
                status.update(f"✅ Successfully exported deliverable to: [b]{target}[/b]")
            except Exception as e:
                status.update(f"❌ Failed to export file: {e}")

    def _run_generation(self, artifact_id: str, out_lang: str, notes: str, is_mock: bool):
        status = self.query_one("#studio_status", Static)
        preview = self.query_one("#studio_md_preview", MarkdownViewer)

        try:
            template = get_artifact_asset(artifact_id, role="template", lang=out_lang) or ""
            prompt_guide = get_artifact_asset(artifact_id, role="prompt", lang=out_lang) or ""

            sys_instruction = "You are an expert PMO Director. Auto-fill the project deliverable template strictly according to PMI and Saudi DGA governance rules."
            full_prompt = (
                f"PROJECT CONTEXT & NOTES:\n{notes}\n\n"
                f"DELIVERABLE PROMPT GUIDANCE:\n{prompt_guide}\n\n"
                f"BLANK TEMPLATE TO COMPLETE:\n{template}"
            )

            client = AIClient()
            output = client.generate(full_prompt, system_instruction=sys_instruction, mock=is_mock)
            self.generated_content = output
            preview.document.update(output)
            status.update(f"✅ Successfully generated `{artifact_id}` deliverable ({len(output)} chars)!")
        except Exception as e:
            status.update(f"🔴 AI Generation error: {e}")
