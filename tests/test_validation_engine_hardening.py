#!/usr/bin/env python3
"""
tests/test_validation_engine_hardening.py
Verification suite for Tasleemat Validation & Interface Hardening:
- Task A: Pattern enforcement, ISO date format, maxLength, maxItems, and bool-type traps.
- Task B: Strict version compatibility contract whitelist.
- Task C: ValidationReport metadata, definition_fingerprint, schema_id, schema_dialect.
- Task D: Catalog defensive copy, strict tailoring profile validation, path traversal defense.
- Task G: Rendering path traversal and directory containment protection.
- Task H: Mock output prominent unvalidated disclaimer.
"""

import copy
import json
import pathlib
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import tasleemat
from tasleemat.catalog import (
    get_artifact_assets,
    get_artifact_definition,
    get_tailoring_profile,
    list_artifacts,
)
from tasleemat.rendering import render_artifact
from tasleemat.validation import (
    ValidationError,
    ValidationReport,
    validate_artifact_data,
    preflight_schema,
)
from tasleemat.ai import AIClient


class TestValidationEngineHardening(unittest.TestCase):

    def setUp(self):
        self.charter_base = {
            "artifact_id": "PMO-03.01",
            "metadata": {
                "project_name": "Cloud Transformation",
                "project_code": "PRJ-999",
                "date_prepared": "2026-03-15",
                "prepared_by": "Dr. Sarah",
                "sponsor": "Executive VP",
                "version": "1.0",
                "status": "approved",
            },
            "fields": {
                "project_purpose": "Detailed objective for the enterprise cloud modernization.",
                "high_level_project_description": "Migrating on-premise compute nodes to hybrid cloud architecture.",
                "key_deliverables": ["Cloud Architecture Plan", "Security Framework"],
                "project_objectives_and_related_success_criteria": [
                    {"objective": "Zero downtime", "success_criteria": "99.99% SLA"}
                ],
                "summary_milestone_schedule": [
                    {"milestone": "Phase 1 Gate", "target_date": "2026-06-30"}
                ],
            },
        }

    # ==================== TASK A: CONSTRAINT VALIDATION ====================

    def test_pattern_constraint_enforcement(self):
        """Verify that regex pattern constraint is enforced on project_code."""
        payload = copy.deepcopy(self.charter_base)
        # Invalid characters in project_code according to ^[A-Z0-9_-]+$
        payload["metadata"]["project_code"] = "PRJ 999 with spaces!"
        report = validate_artifact_data("PMO-03.01", payload)
        self.assertFalse(report.valid)
        error_codes = [e.code for e in report.errors]
        self.assertIn("PATTERN_VIOLATION", error_codes)

    def test_date_format_constraint_enforcement(self):
        """Verify that date format is enforced as valid ISO YYYY-MM-DD."""
        payload = copy.deepcopy(self.charter_base)
        # Invalid date format
        payload["metadata"]["date_prepared"] = "15/03/2026"
        report = validate_artifact_data("PMO-03.01", payload)
        self.assertFalse(report.valid)
        error_codes = [e.code for e in report.errors]
        self.assertIn("FORMAT_VIOLATION", error_codes)

        # Invalid date value
        payload["metadata"]["date_prepared"] = "2026-02-31"
        report2 = validate_artifact_data("PMO-03.01", payload)
        self.assertFalse(report2.valid)
        self.assertIn("FORMAT_VIOLATION", [e.code for e in report2.errors])

    def test_python_boolean_type_trap(self):
        """Verify that Python bool (True/False) is rejected for integer and number types."""
        risk_payload = {
            "artifact_id": "PMO-04.08.02",
            "metadata": {
                "project_name": "Test Project",
                "project_code": "PRJ-01",
                "last_updated": "2026-03-15",
            },
            "risks": [
                {
                    "risk_id": "RSK-001",
                    "category": "Technical",
                    "event_narrative": "Latency issue during cloud sync",
                    "probability_score": True,  # Boolean passed where integer is expected
                    "impact_score": 4,
                    "response_strategy": "Mitigate",
                    "owner": "Network Lead",
                    "status": "Identified",
                }
            ],
        }
        report = validate_artifact_data("PMO-04.08.02", risk_payload)
        self.assertFalse(report.valid)
        error_codes = [e.code for e in report.errors]
        self.assertIn("TYPE_MISMATCH", error_codes)

    # ==================== TASK B: VERSION CONTRACT ====================

    def test_version_compatibility_strict_whitelist(self):
        """Verify version compatibility strictly accepts valid references and rejects unmapped/dialect URIs."""
        defn = get_artifact_definition("PMO-03.01")
        real_fp = defn["fingerprint"]
        schema_fp = defn["completed_data_validation"]["schema_fingerprint"]
        schema_id = defn["completed_data_validation"]["schema_id"]

        # Valid supported references
        for v in ["2.5.0", "v2.5.0", real_fp, schema_fp, schema_id]:
            rep = validate_artifact_data("PMO-03.01", self.charter_base, definition_version=v)
            self.assertTrue(rep.valid, f"Expected {v} to be supported")

        # Invalid arbitrary strings, older unmapped versions, or dialect URIs must be rejected
        for bad_v in [
            "https://json-schema.org/draft/2020-12/schema",
            "custom_PMO-03.01",
            "2.4.2",
            "2.4.0",
            "3.0.0",
            "invalid_version",
        ]:
            rep_bad = validate_artifact_data("PMO-03.01", self.charter_base, definition_version=bad_v)
            self.assertFalse(rep_bad.valid, f"Expected {bad_v} to be rejected")
            self.assertIn("UNSUPPORTED_VERSION", [e.code for e in rep_bad.errors])

    # ==================== TASK C: TRACEABILITY METADATA ====================

    def test_validation_report_traceability_metadata(self):
        """Verify report returns real SHA-256 fingerprint, schema_id, and schema_dialect."""
        rep = validate_artifact_data("PMO-03.01", self.charter_base)
        self.assertTrue(rep.valid)
        # Definition fingerprint must be a 64-char SHA-256 hash matching catalog
        defn = get_artifact_definition("PMO-03.01")
        self.assertEqual(rep.definition_fingerprint, defn["fingerprint"])
        self.assertEqual(len(rep.definition_fingerprint), 64)
        self.assertEqual(rep.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-03.01.schema.json")
        self.assertEqual(rep.schema_dialect, "https://json-schema.org/draft/2020-12/schema")

        d = rep.to_dict()
        self.assertIn("definition_fingerprint", d)
        self.assertIn("schema_id", d)
        self.assertIn("schema_dialect", d)

    # ==================== TASK D: CATALOG & PROFILE HARDENING ====================

    def test_get_artifact_definition_defensive_deepcopy(self):
        """Verify mutating returned definition does not mutate catalog cache."""
        defn1 = get_artifact_definition("PMO-03.01")
        defn1["name_en"] = "MUTATED NAME"
        defn2 = get_artifact_definition("PMO-03.01")
        self.assertEqual(defn2["name_en"], "PROJECT CHARTER")

    def test_tailoring_profile_validation_errors(self):
        """Verify get_tailoring_profile raises ValueError on invalid tier or pack."""
        with self.assertRaises(ValueError):
            get_tailoring_profile(tier="99")

        with self.assertRaises(ValueError):
            get_tailoring_profile(tier="2", pack="unknown_pack")

        # Valid calls
        t1 = get_tailoring_profile(tier="1", pack="general")
        self.assertGreater(len(t1), 0)

    def test_asset_path_traversal_containment(self):
        """Verify ArtifactAssets._resolve rejects paths escaping repository/package root."""
        assets = get_artifact_assets("PMO-03.01", lang="en")
        with self.assertRaises(ValueError):
            assets._resolve("../../etc/passwd")

    # ==================== TASK G: RENDERING IMMUTABILITY ====================

    def test_rendering_protected_directories(self):
        """Verify render_artifact blocks writing to forms/ and package directory."""
        with self.assertRaises(ValueError):
            render_artifact("PMO-03.01", lang="en", out_path=ROOT / "forms" / "illegal.html")

        with self.assertRaises(ValueError):
            render_artifact("PMO-03.01", lang="en", out_path=ROOT / "tasleemat" / "illegal.html")

    # ==================== TASK H: MOCK DISCLAIMER ====================

    def test_mock_generation_unvalidated_notice(self):
        """Verify mock AI generation emits prominent unvalidated test output disclaimer."""
        client = AIClient(provider="mock")
        res = client.generate("Draft Project Charter for testing", mock=True)
        self.assertIn("UNVALIDATED TEST OUTPUT: NOT SUITABLE FOR PRODUCTION USE", res)
        self.assertIn("MOCK AI GENERATION", res)
        self.assertIn("[MOCK TEST ONLY]", res)

    # ==================== STAGE B TESTS ====================

    def test_unsupported_schema_keyword_detection(self):
        """Verify pure-Python validator flags unsupported JSON schema assertions."""
        schema_with_unsupported = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "name": {"type": "string", "unsupportedAssertion": True}
            }
        }
        from tasleemat.validation import _validate_with_builtin
        errors, warnings = _validate_with_builtin({"name": "test"}, schema_with_unsupported, "strict")
        self.assertTrue(any(e.code == "UNSUPPORTED_SCHEMA_ASSERTION" for e in errors))

    def test_unsupported_artifact_explicit_status(self):
        """Verify validation of deliverable without companion schema returns status='unavailable'."""
        with patch("tasleemat.validation._load_schema", side_effect=KeyError("Schema unavailable")):
            report = validate_artifact_data("PMO-00.01", {"some": "data"})
            self.assertFalse(report.valid)
            self.assertEqual(report.status, "unavailable")
            self.assertFalse(report.is_available)
            self.assertEqual(len(report.errors), 1)
            self.assertEqual(report.errors[0].code, "SCHEMA_UNAVAILABLE")

    def test_artifact_summary_and_lexicon_cache_isolation(self):
        """Verify mutating ArtifactSummary.tiers or get_lexicon() does not pollute cache."""
        from tasleemat.catalog import get_lexicon
        arts1 = list_artifacts()
        arts1[0].tiers.append("DIRTY_TIER")
        arts2 = list_artifacts()
        self.assertNotIn("DIRTY_TIER", arts2[0].tiers)

        lex1 = get_lexicon()
        lex1[0]["dirty_key"] = "DIRTY_VALUE"
        lex2 = get_lexicon()
        self.assertNotIn("dirty_key", lex2[0])

    def test_combined_tier_and_pack_filter_intersection(self):
        """Verify list_artifacts with tier and pack enforces strict intersection."""
        # PMO-02.01 has agile under tier 1, but NOT under tier 2
        arts = list_artifacts(tier="2", pack="agile")
        ids = [a.artifact_id for a in arts]
        self.assertNotIn("PMO-02.01", ids)

    def test_batch_1_pmo_01_01_business_case_validation(self):
        """Verify PMO-01.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-01.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-01.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-01.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-01.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-01.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-01.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_1_pmo_07_03_closeout_validation(self):
        """Verify PMO-07.03 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-07.03_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-07.03_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-07.03_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-07.03", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-07.03", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-07.03", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    # ==================== BATCH 2 COMPANION SCHEMAS ====================

    def test_batch_2_pmo_04_01_01_project_management_plan_validation(self):
        """Verify PMO-04.01.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.01.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.01.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.01.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.01.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.01.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.01.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.01.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_2_pmo_04_02_05_scope_statement_validation(self):
        """Verify PMO-04.02.05 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.02.05_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.02.05_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.02.05_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.02.05", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.02.05", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.02.05", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_2_pmo_04_04_01_cost_management_plan_validation(self):
        """Verify PMO-04.04.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.04.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.04.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.04.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.04.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.04.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.04.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    # ==================== BATCH 3 COMPANION SCHEMAS ====================

    def test_batch_3_pmo_04_03_01_schedule_management_plan_validation(self):
        """Verify PMO-04.03.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.03.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.03.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.03.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.03.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.03.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.03.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.03.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_3_pmo_04_10_01_stakeholder_engagement_plan_validation(self):
        """Verify PMO-04.10.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.10.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.10.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.10.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.10.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.10.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.10.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_3_pmo_05_01_issue_log_validation(self):
        """Verify PMO-05.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-05.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-05.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-05.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-05.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-05.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-05.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    # ==================== BATCH 4 COMPANION SCHEMAS ====================

    def test_batch_4_pmo_04_05_01_quality_management_plan_validation(self):
        """Verify PMO-04.05.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.05.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.05.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.05.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.05.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.05.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.05.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.05.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_4_pmo_04_06_01_resource_management_plan_validation(self):
        """Verify PMO-04.06.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.06.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.06.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.06.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.06.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.06.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.06.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.06.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_4_pmo_04_07_01_communications_management_plan_validation(self):
        """Verify PMO-04.07.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.07.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.07.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.07.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.07.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.07.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.07.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.07.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    # ==================== BATCH 5 COMPANION SCHEMAS ====================

    def test_batch_5_pmo_04_02_01_scope_management_plan_validation(self):
        """Verify PMO-04.02.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.02.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.02.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.02.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.02.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.02.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.02.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.02.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_5_pmo_04_08_01_risk_management_plan_validation(self):
        """Verify PMO-04.08.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.08.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.08.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.08.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.08.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.08.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.08.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.08.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    def test_batch_5_pmo_04_09_01_procurement_management_plan_validation(self):
        """Verify PMO-04.09.01 valid, invalid, and draft fixture validation."""
        fixtures_dir = ROOT / "tests" / "fixtures"
        valid_path = fixtures_dir / "valid" / "PMO-04.09.01_valid.json"
        invalid_path = fixtures_dir / "invalid" / "PMO-04.09.01_invalid.json"
        draft_path = fixtures_dir / "draft" / "PMO-04.09.01_draft.json"

        with open(valid_path, "r", encoding="utf-8") as f:
            v_data = json.load(f)
        rep_v = validate_artifact_data("PMO-04.09.01", v_data)
        self.assertTrue(rep_v.valid)
        self.assertEqual(rep_v.status, "supported")
        self.assertTrue(rep_v.is_available)
        self.assertEqual(rep_v.schema_id, "https://tasleemat.pmo/schemas/completed/PMO-04.09.01.schema.json")

        with open(invalid_path, "r", encoding="utf-8") as f:
            inv_data = json.load(f)
        rep_inv = validate_artifact_data("PMO-04.09.01", inv_data)
        self.assertFalse(rep_inv.valid)
        self.assertGreater(len(rep_inv.errors), 0)

        with open(draft_path, "r", encoding="utf-8") as f:
            dr_data = json.load(f)
        rep_dr = validate_artifact_data("PMO-04.09.01", dr_data, mode="draft")
        self.assertTrue(rep_dr.valid)

    # ==================== ALL 114 DELIVERABLES VALIDATION MATRIX ====================

    def test_all_114_companion_schemas_and_fixtures_matrix(self):
        """Verify that all 114 companion schemas in the catalog validate their fixture sets."""
        schema_dir = ROOT / "tasleemat" / "schemas" / "completed"
        schemas = sorted(schema_dir.glob("*.json"))
        self.assertEqual(len(schemas), 114, "Expected exactly 114 companion schemas")

        for sf in schemas:
            with open(sf, "r", encoding="utf-8") as f:
                s = json.load(f)
            aid = s.get("properties", {}).get("artifact_id", {}).get("const")
            self.assertIsNotNone(aid, f"Schema {sf.name} missing artifact_id const")

            # Preflight
            p_errs = preflight_schema(s)
            self.assertEqual(len(p_errs), 0, f"{aid} preflight errors: {p_errs}")

            # Valid fixture
            v_path = ROOT / "tests" / "fixtures" / "valid" / f"{aid}_valid.json"
            self.assertTrue(v_path.exists(), f"Missing valid fixture for {aid}")
            with open(v_path, "r", encoding="utf-8") as f:
                v_data = json.load(f)
            rep_v = validate_artifact_data(aid, v_data)
            self.assertTrue(rep_v.valid, f"{aid} valid failed: {rep_v.errors}")
            self.assertEqual(rep_v.status, "supported")

            # Invalid fixture
            inv_candidates = list((ROOT / "tests" / "fixtures" / "invalid").glob(f"{aid}_*.json"))
            self.assertGreater(len(inv_candidates), 0, f"Missing invalid fixture for {aid}")
            with open(inv_candidates[0], "r", encoding="utf-8") as f:
                inv_data = json.load(f)
            rep_inv = validate_artifact_data(aid, inv_data)
            self.assertFalse(rep_inv.valid, f"{aid} invalid fixture unexpectedly valid")
            self.assertGreater(len(rep_inv.errors), 0)

            # Draft fixture
            dr_path = ROOT / "tests" / "fixtures" / "draft" / f"{aid}_draft.json"
            self.assertTrue(dr_path.exists(), f"Missing draft fixture for {aid}")
            with open(dr_path, "r", encoding="utf-8") as f:
                dr_data = json.load(f)
            rep_dr = validate_artifact_data(aid, dr_data, mode="draft")
            self.assertTrue(rep_dr.valid, f"{aid} draft failed: {rep_dr.errors}")

    # ==================== ADVANCED PREFLIGHT & CONTRACT TESTS ====================

    def test_definition_reference_contract(self):
        """Verify definition reference supports fingerprint, schema ID, package version and rejects invalid."""
        defn = get_artifact_definition("PMO-03.01")
        real_fp = defn["fingerprint"]
        schema_id = "https://tasleemat.pmo/schemas/completed/PMO-03.01.schema.json"

        # 1. Exact catalog fingerprint
        rep_fp = validate_artifact_data("PMO-03.01", self.charter_base, definition_version=real_fp)
        self.assertTrue(rep_fp.valid)

        # 2. Exact schema ID
        rep_sid = validate_artifact_data("PMO-03.01", self.charter_base, definition_version=schema_id)
        self.assertTrue(rep_sid.valid)

        # 3. Exact package version
        rep_ver = validate_artifact_data("PMO-03.01", self.charter_base, definition_version="2.5.0")
        self.assertTrue(rep_ver.valid)

        # 4. Mismatched fingerprint
        wrong_fp = "0000000000000000000000000000000000000000000000000000000000000000"
        rep_wrong_fp = validate_artifact_data("PMO-03.01", self.charter_base, definition_version=wrong_fp)
        self.assertFalse(rep_wrong_fp.valid)
        self.assertEqual(rep_wrong_fp.errors[0].code, "UNSUPPORTED_VERSION")

        # 5. Schema dialect URI rejected
        rep_dialect = validate_artifact_data("PMO-03.01", self.charter_base, definition_version="https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(rep_dialect.valid)
        self.assertEqual(rep_dialect.errors[0].code, "UNSUPPORTED_VERSION")

        # 6. Arbitrary artifact ID suffix rejected
        rep_suffix = validate_artifact_data("PMO-03.01", self.charter_base, definition_version="release_PMO-03.01")
        self.assertFalse(rep_suffix.valid)
        self.assertEqual(rep_suffix.errors[0].code, "UNSUPPORTED_VERSION")

    def test_schema_preflight_independent_of_payload(self):
        """Verify schema preflight detects unsupported keywords, types, and invalid patterns in unexercised branches."""
        from tasleemat.validation import preflight_schema, _validate_with_builtin

        # 1. Unsupported assertion on absent optional property
        schema_opt_bad = {
            "type": "object",
            "properties": {
                "present_field": {"type": "string"},
                "absent_field": {"type": "string", "unsupportedAssertion": True}
            }
        }
        errs_preflight = preflight_schema(schema_opt_bad)
        self.assertTrue(any(e.code == "UNSUPPORTED_SCHEMA_ASSERTION" for e in errs_preflight))
        
        # When validating payload that omits absent_field, it still fails due to schema preflight
        errs_val, _ = _validate_with_builtin({"present_field": "hello"}, schema_opt_bad, "strict")
        self.assertTrue(any(e.code == "UNSUPPORTED_SCHEMA_ASSERTION" for e in errs_val))

        # 2. Unsupported item-schema assertion on empty array
        schema_empty_arr = {
            "type": "object",
            "properties": {
                "items_list": {
                    "type": "array",
                    "items": {"type": "string", "unsupportedKeyword": 123}
                }
            }
        }
        errs_arr, _ = _validate_with_builtin({"items_list": []}, schema_empty_arr, "strict")
        self.assertTrue(any(e.code == "UNSUPPORTED_SCHEMA_ASSERTION" for e in errs_arr))

        # 3. Unsupported declared type
        schema_bad_type = {"type": "object", "properties": {"x": {"type": "unknown_primitive_type"}}}
        errs_type = preflight_schema(schema_bad_type)
        self.assertTrue(any(e.code == "UNSUPPORTED_TYPE_DECLARATION" for e in errs_type))

        # 4. Invalid pattern syntax
        schema_bad_regex = {"type": "object", "properties": {"x": {"type": "string", "pattern": "[unclosed-regex"}}}
        errs_regex = preflight_schema(schema_bad_regex)
        self.assertTrue(any(e.code == "INVALID_PATTERN_SYNTAX" for e in errs_regex))

        # 5. Malformed keyword values
        schema_bad_num = {"type": "object", "properties": {"x": {"type": "number", "minimum": "not_a_number"}}}
        errs_num = preflight_schema(schema_bad_num)
        self.assertTrue(any(e.code == "MALFORMED_SCHEMA_KEYWORD" for e in errs_num))

    def test_universal_keywords_and_input_immutability(self):
        """Verify enum and const apply across numbers/booleans and payload is not mutated."""
        from tasleemat.validation import _validate_with_builtin
        import copy

        # Numeric enum & const
        schema_num = {
            "type": "object",
            "properties": {
                "rate": {"type": "number", "enum": [1.5, 2.0, 2.5]},
                "fixed_code": {"type": "integer", "const": 42}
            }
        }
        payload = {"rate": 2.0, "fixed_code": 42}
        payload_copy = copy.deepcopy(payload)

        errs_ok, _ = _validate_with_builtin(payload, schema_num, "strict")
        self.assertEqual(len(errs_ok), 0)
        self.assertEqual(payload, payload_copy)  # Immutability check

        # Enum violation on number
        errs_bad_enum, _ = _validate_with_builtin({"rate": 3.0, "fixed_code": 42}, schema_num, "strict")
        self.assertTrue(any(e.code == "ENUM_VIOLATION" for e in errs_bad_enum))

        # Const violation on integer
        errs_bad_const, _ = _validate_with_builtin({"rate": 2.0, "fixed_code": 99}, schema_num, "strict")
        self.assertTrue(any(e.code == "CONST_VIOLATION" for e in errs_bad_const))

    def test_availability_and_unknown_artifact_distinction(self):
        """Verify unknown artifacts, missing schemas, and malformed payloads are accurately categorized."""
        # 1. Unknown artifact ID
        rep_unknown = validate_artifact_data("UNKNOWN-99.99", {"some": "data"})
        self.assertFalse(rep_unknown.valid)
        self.assertEqual(rep_unknown.status, "unknown_artifact")
        self.assertFalse(rep_unknown.is_available)
        self.assertEqual(rep_unknown.errors[0].code, "UNKNOWN_ARTIFACT")

        # 2. Known artifact without companion schema (simulated via patch)
        with patch("tasleemat.validation._load_schema", side_effect=KeyError("Schema unavailable")):
            rep_no_schema = validate_artifact_data("PMO-00.01", {"some": "data"})
            self.assertFalse(rep_no_schema.valid)
            self.assertEqual(rep_no_schema.status, "unavailable")
            self.assertFalse(rep_no_schema.is_available)
            self.assertEqual(rep_no_schema.errors[0].code, "SCHEMA_UNAVAILABLE")

        # 3. Known artifact with supported schema but non-dict payload
        rep_bad_payload = validate_artifact_data("PMO-03.01", ["not", "a", "dict"])
        self.assertFalse(rep_bad_payload.valid)
        self.assertEqual(rep_bad_payload.status, "supported")
        self.assertTrue(rep_bad_payload.is_available)
        self.assertEqual(rep_bad_payload.errors[0].code, "INVALID_PAYLOAD")

    def test_preflight_rejects_type_union_and_tuple_items(self):
        """Verify preflight rejects type unions and tuple item lists instead of silently skipping them."""
        # Type union
        schema_union = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "field": {"type": ["string", "null"]}
            }
        }
        errs_union = preflight_schema(schema_union)
        self.assertTrue(any(e.code == "UNSUPPORTED_TYPE_DECLARATION" for e in errs_union))

        # Tuple item array
        schema_tuple = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "coords": {"type": "array", "items": [{"type": "number"}, {"type": "number"}]}
            }
        }
        errs_tuple = preflight_schema(schema_tuple)
        self.assertTrue(any(e.code == "UNSUPPORTED_SCHEMA_ASSERTION" for e in errs_tuple))

        # Non-finite schema bounds
        import math
        schema_nan = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": "object",
            "properties": {
                "score": {"type": "number", "minimum": float("nan")}
            }
        }
        errs_nan = preflight_schema(schema_nan)
        self.assertTrue(any(e.code == "MALFORMED_SCHEMA_KEYWORD" for e in errs_nan))

    def test_strict_json_equality_for_boolean_vs_number(self):
        """Verify Python True/False does not match JSON numbers in const and enum assertions."""
        from tasleemat.validation import _validate_with_builtin

        # Const assertion: number 1 vs boolean True
        schema_const_num = {"type": "object", "properties": {"val": {"const": 1}}}
        errs_c1, _ = _validate_with_builtin({"val": True}, schema_const_num, "strict")
        self.assertEqual(len(errs_c1), 1)
        self.assertEqual(errs_c1[0].code, "CONST_VIOLATION")

        # Const assertion: boolean True vs number 1
        schema_const_bool = {"type": "object", "properties": {"val": {"const": True}}}
        errs_c2, _ = _validate_with_builtin({"val": 1}, schema_const_bool, "strict")
        self.assertEqual(len(errs_c2), 1)
        self.assertEqual(errs_c2[0].code, "CONST_VIOLATION")

        # Enum assertion: boolean True vs number in enum [1, 2, 3]
        schema_enum_num = {"type": "object", "properties": {"val": {"enum": [1, 2, 3]}}}
        errs_e1, _ = _validate_with_builtin({"val": True}, schema_enum_num, "strict")
        self.assertEqual(len(errs_e1), 1)
        self.assertEqual(errs_e1[0].code, "ENUM_VIOLATION")

        # Enum assertion: number 1 vs boolean in enum [True, "other"]
        schema_enum_bool = {"type": "object", "properties": {"val": {"enum": [True, "other"]}}}
        errs_e2, _ = _validate_with_builtin({"val": 1}, schema_enum_bool, "strict")
        self.assertEqual(len(errs_e2), 1)
        self.assertEqual(errs_e2[0].code, "ENUM_VIOLATION")

    def test_rejection_of_nan_and_infinity_in_payload(self):
        """Verify non-finite float values (NaN, Infinity) in payloads are rejected."""
        import math
        from tasleemat.validation import _validate_with_builtin

        schema = {"type": "object", "properties": {"rate": {"type": "number"}, "count": {"type": "integer"}}}

        # NaN
        errs_nan, _ = _validate_with_builtin({"rate": float("nan")}, schema, "strict")
        self.assertEqual(len(errs_nan), 1)
        self.assertEqual(errs_nan[0].code, "TYPE_MISMATCH")

        # +Infinity
        errs_inf, _ = _validate_with_builtin({"rate": float("inf")}, schema, "strict")
        self.assertEqual(len(errs_inf), 1)
        self.assertEqual(errs_inf[0].code, "TYPE_MISMATCH")

        # -Infinity on integer
        errs_ninf, _ = _validate_with_builtin({"count": float("-inf")}, schema, "strict")
        self.assertEqual(len(errs_ninf), 1)
        self.assertEqual(errs_ninf[0].code, "TYPE_MISMATCH")


if __name__ == "__main__":
    unittest.main()
