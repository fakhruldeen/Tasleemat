"""
tasleemat.tui.screens.auditor
Interactive Project Governance Auditor & Verification Screen.
Features live progress bars, KPIs (governance score, deliverable completion, schema integrity),
Stage-Gate readiness table, and detailed pass/fail deliverable findings with 1-click remediation.
"""

import os
import pathlib
from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal, ScrollableContainer
from textual.widgets import Static, Input, Button, Label, ProgressBar, DataTable
from tasleemat.tui.i18n import t
from tasleemat.tui.bidi import shape_text
from tasleemat.audit import audit_project, ProjectAuditReport


class AuditorScreen(ScrollableContainer):
    """Interactive Project Auditor & Governance Dashboard."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.current_report: ProjectAuditReport | None = None

    def compose(self) -> ComposeResult:
        with Vertical(classes="panel-container"):
            title = "🛡️ Project Governance Auditor & Verification" if self.lang == "en" else shape_text("🛡️ أداة تدقيق حوكمة المشاريع والتحقق الهيكلي")
            desc = (
                "Audit any scaffolded project workspace against its required PMO Tier & Methodology Pack. "
                "Calculates overall governance KPIs, completion percentages, Stage-Gate status, and JSON schema integrity."
                if self.lang == "en"
                else shape_text("تدقيق أي بيئة عمل مشروع ومطابقتها مع متطلبات الحوكمة ومنهجية التسليم، مع حساب مؤشرات الأداء والنسب المئوية وجاهزية بوابات المرحلة ومخططات البيانات.")
            )

            yield Static(f"[b]{title}[/b]", classes="card-title")
            yield Static(desc, classes="card-subtitle")

            # Workspace path selector
            with Vertical(classes="card"):
                path_lbl = "Project Workspace Directory:" if self.lang == "en" else shape_text("مسار مجلد بيئة عمل المشروع:")
                yield Label(f"[b]{path_lbl}[/b]", classes="form-label")
                with Horizontal():
                    yield Input(value=os.getcwd(), id="inp_audit_path", placeholder="/path/to/project_workspace")
                    yield Button(t("btn_run_audit", self.lang), id="btn_trigger_audit", classes="-accent")

            # KPI Summary Row
            with Horizontal(id="kpi_summary_container", classes="kpi-row"):
                with Vertical(classes="kpi-box", id="kpi_completion_box"):
                    lbl1 = "Deliverable Completion" if self.lang == "en" else shape_text("اكتمال المخرجات")
                    yield Static(lbl1, classes="kpi-label")
                    yield Static("-- %", id="val_kpi_completion", classes="kpi-value")
                    yield ProgressBar(total=100, show_eta=False, id="prog_completion")

                with Vertical(classes="kpi-box", id="kpi_governance_box"):
                    lbl2 = "Governance Score" if self.lang == "en" else shape_text("درجة الحوكمة")
                    yield Static(lbl2, classes="kpi-label")
                    yield Static("-- %", id="val_kpi_governance", classes="kpi-value")
                    yield ProgressBar(total=100, show_eta=False, id="prog_governance")

                with Vertical(classes="kpi-box", id="kpi_schema_box"):
                    lbl3 = "Schema Integrity" if self.lang == "en" else shape_text("سلامة المخططات")
                    yield Static(lbl3, classes="kpi-label")
                    yield Static("-- %", id="val_kpi_schema", classes="kpi-value")
                    yield ProgressBar(total=100, show_eta=False, id="prog_schema")

            # Project Metadata Status Card
            with Vertical(classes="card", id="audit_meta_card"):
                meta_header = "Project Context & Audit Scope" if self.lang == "en" else shape_text("سياق المشروع ونطاق التدقيق")
                yield Static(f"[b]{meta_header}[/b]", classes="card-title")
                yield Static("Enter project path above and click [Run Project Governance Audit] to begin.", id="audit_meta_text")

            # Stage-Gate Readiness Matrix Table
            with Vertical(classes="card"):
                gate_title = "🚪 Stage-Gate Governance Readiness (Gates 0 - 5)" if self.lang == "en" else shape_text("🚪 جاهزية بوابات حوكمة المرحلة (البوابات 0 إلى 5)")
                yield Static(f"[b]{gate_title}[/b]", classes="card-title")
                yield DataTable(id="table_gate_readiness")

            # Detailed Deliverable Findings Table
            with Vertical(classes="card"):
                findings_title = "📋 Deliverables Verification Breakdown" if self.lang == "en" else shape_text("📋 تفاصيل التحقق من مخرجات المشروع")
                yield Static(f"[b]{findings_title}[/b]", classes="card-title")
                yield DataTable(id="table_audit_findings")

    def on_mount(self) -> None:
        """Initialize tables on mount."""
        self._init_gate_table()
        self._init_findings_table()

    def _init_gate_table(self) -> None:
        table = self.query_one("#table_gate_readiness", DataTable)
        table.clear(columns=True)
        if self.lang == "en":
            table.add_columns("Gate ID", "Gate / Lifecycle Phase", "Progress", "Deliverables", "Status")
        else:
            table.add_columns(
                shape_text("رمز البوابة"),
                shape_text("المرحلة الحوكمية"),
                shape_text("النسبة المئوية"),
                shape_text("المخرجات"),
                shape_text("الحالة")
            )

    def _init_findings_table(self) -> None:
        table = self.query_one("#table_audit_findings", DataTable)
        table.clear(columns=True)
        if self.lang == "en":
            table.add_columns("ID", "Deliverable Name", "Status", "Files Found", "Findings / Errors")
        else:
            table.add_columns(
                shape_text("المعرف"),
                shape_text("اسم المخرج"),
                shape_text("الحالة"),
                shape_text("الملفات"),
                shape_text("الملاحظات / الأخطاء")
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn_trigger_audit":
            self.run_audit()

    def run_audit(self) -> None:
        """Execute audit on entered path and update UI."""
        path_inp = self.query_one("#inp_audit_path", Input)
        meta_txt = self.query_one("#audit_meta_text", Static)
        target = pathlib.Path(path_inp.value.strip() or os.getcwd()).resolve()

        if not target.exists():
            meta_txt.update(f"[red]❌ Directory not found: {target}[/red]")
            return

        try:
            report = audit_project(target, strict_schema=True)
            self.current_report = report
        except Exception as e:
            meta_txt.update(f"[red]❌ Error running audit: {e}[/red]")
            return

        # 1. Update KPIs and Progress Bars
        val_comp = self.query_one("#val_kpi_completion", Static)
        val_gov = self.query_one("#val_kpi_governance", Static)
        val_sch = self.query_one("#val_kpi_schema", Static)

        prog_comp = self.query_one("#prog_completion", ProgressBar)
        prog_gov = self.query_one("#prog_governance", ProgressBar)
        prog_sch = self.query_one("#prog_schema", ProgressBar)

        val_comp.update(f"{report.overall_progress_pct:.1f}%")
        val_gov.update(f"{report.governance_score_pct:.1f}%")
        val_sch.update(f"{report.schema_compliance_pct:.1f}%")

        prog_comp.progress = report.overall_progress_pct
        prog_gov.progress = report.governance_score_pct
        prog_sch.progress = report.schema_compliance_pct

        # 2. Update Metadata Card
        status_color = "green" if report.is_compliant else "yellow"
        res_str = "PASS (100% Compliant)" if report.is_compliant else f"NOTICE ({report.total_missing} missing, {report.total_schema_errors} schema errors)"
        agents_str = ", ".join(report.agent_integrations_found) if report.agent_integrations_found else "None detected"

        meta_msg = (
            f"[b]Project:[/b] {report.project_name} (`{report.project_code}`) | [b]Tier:[/b] Tier {report.tier} | [b]Pack:[/b] {report.pack.upper()}\n"
            f"[b]Languages:[/b] {', '.join(report.detected_langs).upper()} | [b]AI Agents:[/b] {agents_str}\n"
            f"[b]Audit Result:[/b] [{status_color}]{res_str}[/{status_color}]"
        )
        meta_txt.update(meta_msg)

        # 3. Populate Gate Readiness Table
        gate_table = self.query_one("#table_gate_readiness", DataTable)
        gate_table.clear()
        for g in report.gate_readiness:
            st_color = "green" if g.status == "PASS" else ("yellow" if g.status == "WARN" else "red")
            name = g.gate_name_en if self.lang == "en" else shape_text(g.gate_name_ar)
            bar_text = f"{g.percentage:5.1f}%"
            counts = f"{g.completed_count} / {g.required_count}"
            gate_table.add_row(g.gate_id, name, bar_text, counts, f"[{st_color}][{g.status}][/{st_color}]")

        # 4. Populate Deliverables Findings Table
        find_table = self.query_one("#table_audit_findings", DataTable)
        find_table.clear()
        for f in report.findings:
            if f.status == "valid":
                st_badge = "[green]✓ VALID[/green]"
            elif f.status == "incomplete":
                st_badge = "[yellow]⚠ INCOMPLETE[/yellow]"
            elif f.status == "schema_error":
                st_badge = "[red]✖ SCHEMA ERR[/red]"
            else:
                st_badge = "[red]✗ MISSING[/red]"

            name = f.name_en if self.lang == "en" else shape_text(f.name_ar)
            files_count = str(len(f.found_files))
            notes = "; ".join(f.messages) if f.messages else ("Clean" if self.lang == "en" else shape_text("سليم"))
            find_table.add_row(f.artifact_id, name, st_badge, files_count, notes)
