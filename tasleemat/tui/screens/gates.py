"""
tasleemat.tui.screens.gates
Interactive Stage-Gate Governance Navigator (Gates 0 to 5) with checklists, RACI, and required deliverables.
"""

from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Tree, MarkdownViewer
from tasleemat.tui.i18n import t

GATES_DATA = {
    "Gate 0": {
        "title": "Gate 0: Concept & Strategic Justification (دراسة الفكرة والجدوى)",
        "governing_body": "Executive Strategy Committee / Investment Review Board / CFO",
        "entry_criteria": "Business opportunity or strategic mandate identified; initial sponsorship established.",
        "deliverables": ["PMO-00.06 OKR Alignment Matrix", "PMO-01.01 Business Case", "PMO-01.02 Benefits Management Plan", "PMO-01.04 Gap Analysis Report", "PMO-02.04 AI Canvas & Use Case Card"],
        "checklist": [
            "Does the initiative directly support corporate strategic objectives?",
            "Is the cost of inaction clearly quantified against the investment envelope?",
            "Are strategic risks within organizational tolerance?"
        ],
        "exit_criteria": "Formal approval of the Business Case and inclusion in the Portfolio Roadmap (PMO-00.01)."
    },
    "Gate 1": {
        "title": "Gate 1: Initiation & Charter Authorization (تفويض ميثاق المشروع)",
        "governing_body": "Project Sponsor / PMO Director",
        "entry_criteria": "Approved Business Case from Gate 0; designated Project Manager.",
        "deliverables": ["PMO-03.01 Project Charter", "PMO-03.02 Stakeholder Register", "PMO-03.04 Assumptions & Constraints Log", "PMO-02.01 Methodology & Tailoring Strategy"],
        "checklist": [
            "Is the Project Charter formally signed by the executive sponsor?",
            "Are key stakeholders identified with defined engagement strategies?",
            "Has the governance tier (Tier 1-3) been formally determined?"
        ],
        "exit_criteria": "Authorized Project Charter empowering the Project Manager to apply organizational resources."
    },
    "Gate 2": {
        "title": "Gate 2: Integrated Baseline Approval (اعتماد خط الأساس المتكامل)",
        "governing_body": "Steering Committee / PMO Director / Lead Architect",
        "entry_criteria": "Completed subsidiary project management plans and baselines.",
        "deliverables": ["PMO-04.01.01 Project Management Plan", "PMO-04.02.01 Scope Baseline & WBS", "PMO-04.03.01 Schedule Baseline", "PMO-04.04.01 Cost Baseline & Budget", "PMO-04.08.02 Risk Register"],
        "checklist": [
            "Are Scope, Schedule, and Cost baselines fully reconciled?",
            "Are critical path dependencies agreed upon across functional teams?",
            "Is the Risk Response budget allocated in the cost baseline?"
        ],
        "exit_criteria": "Formal baseline freeze and authorization to mobilize full delivery teams."
    },
    "Gate 3": {
        "title": "Gate 3: Execution Control & Phase Verification (التحكم في التنفيذ والتحقق)",
        "governing_body": "Project Manager / Technical Lead / QA Director",
        "entry_criteria": "Execution progress milestones achieved; deliverable deliverables submitted for review.",
        "deliverables": ["PMO-06.01 Project Status Report (EV/SPI/CPI)", "PMO-05.01 Deliverable Acceptance Form", "PMO-05.03 Quality Inspection Log", "PMO-06.02 Change Request Log"],
        "checklist": [
            "Are SPI and CPI metrics within approved threshold boundaries (0.9 - 1.1)?",
            "Have all major change requests been evaluated by the Change Control Board?",
            "Are quality inspection defects resolved or mitigated?"
        ],
        "exit_criteria": "Validation of phase deliverables and authorization to continue development."
    },
    "Gate 4": {
        "title": "Gate 4: Operational Handover & UAT Acceptance (التسليم التشغيلي وقبول الفحص)",
        "governing_body": "Operations Owner / Product Sponsor / Head of IT Operations",
        "entry_criteria": "Successful User Acceptance Testing (UAT); operational documentation completed.",
        "deliverables": ["PMO-05.04 UAT Test Plan & Sign-off", "PMO-05.07 Operational Handover Checklist", "PMO-05.08 Training & Knowledge Transfer Plan", "PMO-05.09 AI Model Card & Audit Fact Sheet"],
        "checklist": [
            "Is UAT formally signed off with zero Severity 1 open defects?",
            "Are operations and support teams fully trained?",
            "Is the rollback/contingency plan documented and verified?"
        ],
        "exit_criteria": "Operational handover agreement signed; production release cutover approved."
    },
    "Gate 5": {
        "title": "Gate 5: Closeout & Benefits Realization Sign-off (الإغلاق النهائي وتحقق المنافع)",
        "governing_body": "Executive Sponsor / PMO Director / Financial Controller",
        "entry_criteria": "Production handover complete; final financial reconciliations prepared.",
        "deliverables": ["PMO-07.01 Project Closeout Report", "PMO-07.03 Lessons Learned Register", "PMO-07.04 Financial Closure & Audit Reconciliation", "PMO-07.05 Post-Implementation Review"],
        "checklist": [
            "Are all contract procurements and vendor invoices settled?",
            "Are lessons learned cataloged in the institutional PMO knowledge base?",
            "Is the benefits realization tracking schedule transitioned to business operations?"
        ],
        "exit_criteria": "Formal release of project resources, financial closeout, and organizational archiving."
    }
}

class StageGatesScreen(Vertical):
    """Interactive Stage-Gate Governance Navigator."""

    def __init__(self, lang: str = "en", **kwargs):
        super().__init__(**kwargs)
        self.lang = lang
        self.current_gate = "Gate 1"

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="split_left"):
                yield Static(f"### {t('tab_gates', self.lang)}", classes="card-title")
                yield Tree("🚪 6 Governance Stage-Gates", id="tree_gates")

            with Vertical(id="split_right"):
                yield MarkdownViewer("", show_table_of_contents=False, id="gate_md_viewer")

    def on_mount(self) -> None:
        tree = self.query_one("#tree_gates", Tree)
        tree.clear()
        tree.root.expand()
        for gate_key in sorted(GATES_DATA.keys()):
            data = GATES_DATA[gate_key]
            tree.root.add_leaf(data["title"], data=gate_key)
        self.load_gate("Gate 1")

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        if event.node.data:
            self.load_gate(event.node.data)

    def load_gate(self, gate_key: str) -> None:
        self.current_gate = gate_key
        data = GATES_DATA.get(gate_key, {})
        viewer = self.query_one("#gate_md_viewer", MarkdownViewer)

        md = f"# 🚪 {data.get('title', gate_key)}\n\n"
        md += f"**🏛️ Governing Body:** `{data.get('governing_body', '')}`  \n"
        md += f"**📥 Entry Criteria:** {data.get('entry_criteria', '')}  \n"
        md += f"**📤 Exit Criteria:** {data.get('exit_criteria', '')}  \n\n"
        md += "---\n\n### 📦 Required Deliverables Kit\n"
        for d in data.get("deliverables", []):
            md += f"- **`{d}`**\n"

        md += "\n### 📋 Stage-Gate Review Checklist\n"
        for item in data.get("checklist", []):
            md += f"- [ ] {item}\n"

        viewer.document.update(md)
