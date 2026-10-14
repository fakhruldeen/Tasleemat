"""
tasleemat.audit
Enterprise Project Governance Auditor & Verification Engine.
Performs deterministic structural audits on scaffolded PMO project workspaces.
Computes KPIs, progress metrics, stage-gate readiness, and JSON schema compliance.
"""

from __future__ import annotations

import json
import pathlib
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from tasleemat.catalog import (
    VALID_TIERS,
    VALID_PACKS,
    get_artifact_definition,
    get_tailoring_profile,
    list_artifacts,
)
from tasleemat.validation import validate_artifact_data, ValidationReport

# 8 canonical project lifecycle phases
PHASES_ORDER = [
    ("00", "Program & Portfolio Management", "إدارة البرامج والمحافظ"),
    ("01", "Business & Value Delivery", "الأعمال وتسليم القيمة"),
    ("02", "Project Approach & Tailoring", "منهجية المشروع والتخصيص"),
    ("03", "Initiating", "البدء والترخيص"),
    ("04", "Planning", "التخطيط المتكامل"),
    ("05", "Executing", "التنفيذ والتوجيه"),
    ("06", "Monitoring & Controlling", "المراقبة والتحكم"),
    ("07", "Closing", "الإغلاق والتسليم النهائي"),
]


@dataclass
class ArtifactAuditFinding:
    artifact_id: str
    name_en: str
    name_ar: str
    phase_code: str
    required: bool
    status: str  # "valid", "incomplete", "missing", "schema_error"
    present_langs: List[str] = field(default_factory=list)
    found_files: List[str] = field(default_factory=list)
    schema_report: Optional[ValidationReport] = None
    messages: List[str] = field(default_factory=list)


@dataclass
class GateReadinessKPI:
    gate_id: str
    gate_name_en: str
    gate_name_ar: str
    required_count: int
    completed_count: int
    percentage: float
    status: str  # "PASS", "WARN", "FAIL"


@dataclass
class ProjectAuditReport:
    project_path: str
    project_name: str
    project_code: str
    tier: str
    pack: str
    detected_langs: List[str]
    total_required: int
    total_present: int
    total_valid: int
    total_missing: int
    total_schema_errors: int
    
    # KPIs
    overall_progress_pct: float
    governance_score_pct: float
    schema_compliance_pct: float
    
    findings: List[ArtifactAuditFinding] = field(default_factory=list)
    gate_readiness: List[GateReadinessKPI] = field(default_factory=list)
    agent_integrations_found: List[str] = field(default_factory=list)
    is_compliant: bool = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "project_path": self.project_path,
            "project_name": self.project_name,
            "project_code": self.project_code,
            "tier": self.tier,
            "pack": self.pack,
            "detected_langs": self.detected_langs,
            "summary": {
                "total_required": self.total_required,
                "total_present": self.total_present,
                "total_valid": self.total_valid,
                "total_missing": self.total_missing,
                "total_schema_errors": self.total_schema_errors,
                "overall_progress_pct": round(self.overall_progress_pct, 1),
                "governance_score_pct": round(self.governance_score_pct, 1),
                "schema_compliance_pct": round(self.schema_compliance_pct, 1),
                "is_compliant": self.is_compliant,
            },
            "gate_readiness": [
                {
                    "gate_id": g.gate_id,
                    "name_en": g.gate_name_en,
                    "name_ar": g.gate_name_ar,
                    "required": g.required_count,
                    "completed": g.completed_count,
                    "percentage": round(g.percentage, 1),
                    "status": g.status,
                }
                for g in self.gate_readiness
            ],
            "agent_integrations": self.agent_integrations_found,
            "findings": [
                {
                    "artifact_id": f.artifact_id,
                    "name_en": f.name_en,
                    "name_ar": f.name_ar,
                    "phase_code": f.phase_code,
                    "required": f.required,
                    "status": f.status,
                    "present_langs": f.present_langs,
                    "found_files": f.found_files,
                    "messages": f.messages,
                }
                for f in self.findings
            ],
        }


def detect_project_metadata(root_path: pathlib.Path) -> Tuple[str, str, str, str]:
    """Extract (name, code, tier, pack) from PROJECT_README.md, config.json, or defaults."""
    name = root_path.name
    code = "PRJ-UNKNOWN"
    tier = "2"
    pack = "general"

    # 1. Check PROJECT_README.md
    readme = root_path / "PROJECT_README.md"
    if not readme.exists():
        readme = root_path / "README.md"

    if readme.exists():
        try:
            content = readme.read_text(encoding="utf-8")
            # Code from header
            m_code = re.search(r'\(`([A-Za-z0-9_\-]+)`\)', content)
            if m_code:
                code = m_code.group(1)
            # Tier
            m_tier = re.search(r'Governance Tier:\*\* Tier (\d)', content)
            if m_tier:
                tier = m_tier.group(1)
            # Pack
            m_pack = re.search(r'Methodology Pack:\*\* ([A-Za-z]+)', content)
            if m_pack:
                pack = m_pack.group(1).lower()
            # Name
            m_name = re.search(r'^# [^\w]*([A-Za-z0-9_\u0600-\u06FF\s\-]+?)\s*(?:\(|—)', content, re.MULTILINE)
            if m_name:
                cand_name = m_name.group(1).strip()
                if cand_name and len(cand_name) > 2:
                    name = cand_name
        except Exception:
            pass

    return name, code, tier, pack


def audit_project(
    project_path: str | pathlib.Path,
    tier: Optional[str] = None,
    pack: Optional[str] = None,
    strict_schema: bool = True,
) -> ProjectAuditReport:
    """
    Perform a complete structural audit on a project workspace.
    
    Parameters:
        project_path: Directory path of the scaffolded project.
        tier: Optional explicit tier ("1", "2", "3"). If None, auto-detected.
        pack: Optional methodology pack ("general", "agile", "ai", "predictive", "hybrid"). If None, auto-detected.
        strict_schema: If True, executes full JSON Schema Draft 2020-12 checks on completed data files.
    """
    root = pathlib.Path(project_path).resolve()
    if not root.exists() or not root.is_dir():
        raise FileNotFoundError(f"Project directory does not exist or is not a directory: {root}")

    det_name, det_code, det_tier, det_pack = detect_project_metadata(root)
    eff_tier = str(tier).strip() if tier else det_tier
    eff_pack = pack.lower().strip() if pack else det_pack

    if eff_tier not in VALID_TIERS:
        eff_tier = "2"
    if eff_pack not in VALID_PACKS:
        eff_pack = "general"

    required_ids = set(get_tailoring_profile(eff_tier, eff_pack))
    all_defs = {a.artifact_id: a for a in list_artifacts()}

    # Detect installed agent configurations
    agents_found = []
    if (root / ".cursor" / "mcp.json").exists() or (root / ".cursorrules").exists():
        agents_found.append("Cursor")
    if (root / ".antigravityrules").exists() or (root / "skills" / "pmo-governance").exists():
        agents_found.append("Antigravity")
    if (root / "CLAUDE.md").exists():
        agents_found.append("Claude Desktop")
    if (root / ".vscode" / "mcp.json").exists():
        agents_found.append("VS Code")
    if (root / ".opencode" / "mcp.json").exists() or (root / "OPENCODE.md").exists():
        agents_found.append("OpenCode")
    if (root / ".cline" / "mcp.json").exists() or (root / ".clinerules").exists():
        agents_found.append("Cline")
    if (root / ".windsurf" / "mcp.json").exists() or (root / ".windsurfrules").exists():
        agents_found.append("Windsurf")
    if (root / ".openai" / "agent_runner.py").exists():
        agents_found.append("OpenAI CLI")

    # Detect languages present in directory
    detected_langs = []
    if (root / "en").is_dir():
        detected_langs.append("en")
    if (root / "ar").is_dir():
        detected_langs.append("ar")
    if not detected_langs:
        # Check if root contains flat files
        detected_langs.append("root")

    # Search project workspace for artifact files
    # Pattern matching for artifacts e.g. PMO-03.01, PMO_03_01, 03_01, or 04_02_01
    file_map: Dict[str, List[pathlib.Path]] = {}
    for p in root.rglob("*"):
        if p.is_file():
            # Check filename first, then parent folder for PMO identifier
            m = re.search(r'(?:PMO[-_])?(\d{2})[._](\d{2})(?:[._](\d{2}))?', p.name, re.IGNORECASE)
            if not m:
                m = re.search(r'(?:PMO[-_])?(\d{2})[._](\d{2})(?:[._](\d{2}))?', p.parent.name, re.IGNORECASE)
            if m:
                part1, part2, part3 = m.group(1), m.group(2), m.group(3)
                art_id = f"PMO-{part1}.{part2}" + (f".{part3}" if part3 else "")
                file_map.setdefault(art_id, []).append(p)

    findings: List[ArtifactAuditFinding] = []
    total_present = 0
    total_valid = 0
    total_missing = 0
    total_schema_errors = 0

    # Gate breakdown counters (Gate 0 to 5)
    # Mapping Phase -> Gate
    # Gate 0: Phase 00, 01, 02 (Strategic Alignment & Tailoring)
    # Gate 1: Phase 03 (Initiating)
    # Gate 2: Phase 04 (Planning Baselines)
    # Gate 3: Phase 05 (Executing & Directing)
    # Gate 4: Phase 06 (Monitoring & Verification)
    # Gate 5: Phase 07 (Closeout)
    gate_phase_map = {
        "Gate 0": ["00", "01", "02"],
        "Gate 1": ["03"],
        "Gate 2": ["04"],
        "Gate 3": ["05"],
        "Gate 4": ["06"],
        "Gate 5": ["07"],
    }
    gate_counts = {
        g: {"required": 0, "completed": 0} for g in gate_phase_map
    }

    # Evaluate all required deliverables
    for art_id in sorted(list(required_ids)):
        defn = all_defs.get(art_id)
        if not defn:
            continue

        phase_code = defn.phase_code
        # Find which gate this belongs to
        target_gate = None
        for g_name, phases in gate_phase_map.items():
            if phase_code in phases:
                target_gate = g_name
                break
        if target_gate:
            gate_counts[target_gate]["required"] += 1

        matched_files = file_map.get(art_id, [])
        found_names = [f.name for f in matched_files]

        # Determine present languages
        present_langs = []
        for mf in matched_files:
            rel = str(mf.relative_to(root))
            if rel.startswith("en/") or "/en/" in rel:
                if "en" not in present_langs:
                    present_langs.append("en")
            elif rel.startswith("ar/") or "/ar/" in rel:
                if "ar" not in present_langs:
                    present_langs.append("ar")
        if not present_langs and matched_files:
            present_langs.append("default")

        # Status evaluation
        status = "missing"
        schema_rep: Optional[ValidationReport] = None
        messages: List[str] = []

        if not matched_files:
            status = "missing"
            messages.append("Mandatory deliverable file not found in workspace.")
            total_missing += 1
        else:
            total_present += 1
            # Check content completeness
            has_substance = False
            for mf in matched_files:
                if mf.suffix.lower() in [".md", ".json", ".csv"]:
                    try:
                        text = mf.read_text(encoding="utf-8")
                        # Check that it's not empty or just title
                        if len(text.strip()) > 100:
                            has_substance = True
                    except Exception:
                        pass

            if not has_substance:
                status = "incomplete"
                messages.append("Deliverable file exists but contains insufficient content (<100 characters).")
            else:
                status = "valid"

            # Check JSON companion payload if present
            # A completed-data JSON payload contains 'artifact_id' and 'metadata', whereas scaffold templates contain 'form_name' and 'guidance'
            json_payload_files = [f for f in matched_files if f.suffix.lower() == ".json" and "schema" not in f.name.lower()]
            if json_payload_files and strict_schema:
                for jf in json_payload_files:
                    try:
                        payload = json.loads(jf.read_text(encoding="utf-8"))
                        if isinstance(payload, dict) and "artifact_id" in payload and ("metadata" in payload or "fields" in payload):
                            rep = validate_artifact_data(art_id, payload)
                            schema_rep = rep
                            if not rep.valid:
                                status = "schema_error"
                                total_schema_errors += 1
                                for err in rep.errors[:3]:
                                    messages.append(f"Schema Error [{err.field_path}]: {err.message}")
                                break
                    except Exception as e:
                        status = "schema_error"
                        total_schema_errors += 1
                        messages.append(f"JSON Parse Error: {str(e)}")
                        break

            if status == "valid":
                total_valid += 1
                if target_gate:
                    gate_counts[target_gate]["completed"] += 1

        finding = ArtifactAuditFinding(
            artifact_id=art_id,
            name_en=defn.name_en,
            name_ar=defn.name_ar,
            phase_code=phase_code,
            required=True,
            status=status,
            present_langs=present_langs,
            found_files=found_names,
            schema_report=schema_rep,
            messages=messages,
        )
        findings.append(finding)

    total_req = len(required_ids)
    overall_progress = (total_present / total_req * 100.0) if total_req > 0 else 0.0
    governance_score = (total_valid / total_req * 100.0) if total_req > 0 else 0.0
    schema_compliance = (
        ((total_valid / (total_present or 1)) * 100.0)
        if total_schema_errors == 0
        else max(0.0, (1.0 - (total_schema_errors / (total_present or 1))) * 100.0)
    )

    # Compute Gate readiness objects
    gate_readiness_list: List[GateReadinessKPI] = []
    gate_meta = [
        ("Gate 0", "Gate 0: Strategic Alignment & Architecture", "البوابة 0: المواءمة الاستراتيجية والمعمارية"),
        ("Gate 1", "Gate 1: Project Initiation & Charter Authorization", "البوابة 1: بدء المشروع واعتماد الميثاق"),
        ("Gate 2", "Gate 2: Integrated Baseline Approval", "البوابة 2: اعتماد الخطط المرجعية المتكاملة"),
        ("Gate 3", "Gate 3: Execution Readiness & Directing", "البوابة 3: جاهزية التنفيذ والتوجيه"),
        ("Gate 4", "Gate 4: Testing & Verification Gate", "البوابة 4: الاختبارات والتحقق والمراقبة"),
        ("Gate 5", "Gate 5: Operational Transition & Closeout", "البوابة 5: الانتقال التشغيلي والإغلاق"),
    ]

    for g_id, g_en, g_ar in gate_meta:
        c_data = gate_counts[g_id]
        req = c_data["required"]
        comp = c_data["completed"]
        pct = (comp / req * 100.0) if req > 0 else 100.0
        if pct == 100.0:
            st = "PASS"
        elif pct >= 60.0:
            st = "WARN"
        else:
            st = "FAIL"

        gate_readiness_list.append(
            GateReadinessKPI(
                gate_id=g_id,
                gate_name_en=g_en,
                gate_name_ar=g_ar,
                required_count=req,
                completed_count=comp,
                percentage=pct,
                status=st,
            )
        )

    is_compliant = (total_missing == 0 and total_schema_errors == 0 and total_req > 0)

    return ProjectAuditReport(
        project_path=str(root),
        project_name=det_name,
        project_code=det_code,
        tier=eff_tier,
        pack=eff_pack,
        detected_langs=detected_langs,
        total_required=total_req,
        total_present=total_present,
        total_valid=total_valid,
        total_missing=total_missing,
        total_schema_errors=total_schema_errors,
        overall_progress_pct=overall_progress,
        governance_score_pct=governance_score,
        schema_compliance_pct=schema_compliance,
        findings=findings,
        gate_readiness=gate_readiness_list,
        agent_integrations_found=agents_found,
        is_compliant=is_compliant,
    )
