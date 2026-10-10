#!/usr/bin/env python3
"""Tests for JSON Schemas and Field Data Integrity across all 228 form bundles.
"""

import unittest
import pathlib
import json
import csv
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_EN = ROOT / "forms" / "en"
FORMS_AR = ROOT / "forms" / "ar"

class TestSchemas(unittest.TestCase):

    def test_json_parse_and_top_level_keys(self):
        """Verify all 228 JSON files parse cleanly and have required top-level keys."""
        all_jsons = list(FORMS_EN.rglob("*.json")) + list(FORMS_AR.rglob("*.json"))
        self.assertEqual(len(all_jsons), 228, f"Expected 228 JSON files, found {len(all_jsons)}")

        for jf in all_jsons:
            try:
                with open(jf, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception as e:
                self.fail(f"Failed to parse JSON file {jf}: {e}")

            self.assertIn("form_name", data, f"Missing form_name in {jf}")
            self.assertIn("document_reference", data, f"Missing document_reference in {jf}")
            self.assertIn("_llm_instructions", data, f"Missing _llm_instructions in {jf}")
            self.assertIn("fields", data, f"Missing fields in {jf}")

            doc_ref = data["document_reference"]
            self.assertTrue(
                bool(re.match(r"^PMO-\d{2}(?:\.\d{2})+$", doc_ref)),
                f"Invalid document_reference format '{doc_ref}' in {jf}"
            )

    def test_field_definitions_and_guidance_depth(self):
        """Verify every field has valid section, label, and rich guidance."""
        all_jsons = list(FORMS_EN.rglob("*.json")) + list(FORMS_AR.rglob("*.json"))

        for jf in all_jsons:
            with open(jf, "r", encoding="utf-8") as f:
                data = json.load(f)

            fields = data["fields"]
            self.assertIsInstance(fields, dict, f"'fields' must be a dict in {jf}")
            self.assertGreater(len(fields), 0, f"No fields defined in {jf}")

            for field_key, field_obj in fields.items():
                self.assertIsInstance(field_obj, dict, f"Field {field_key} must be an object in {jf}")
                self.assertIn("section", field_obj, f"Missing 'section' in {field_key} in {jf}")
                self.assertIn("label", field_obj, f"Missing 'label' in {field_key} in {jf}")
                self.assertIn("guidance", field_obj, f"Missing 'guidance' in {field_key} in {jf}")
                
                guidance = field_obj["guidance"].strip()
                self.assertGreaterEqual(
                    len(guidance), 10,
                    f"Guidance too short ({len(guidance)} chars) in field '{field_key}' in {jf}"
                )

    def test_json_csv_field_count_alignment(self):
        """Verify that JSON field count matches CSV row count for each form."""
        all_jsons = list(FORMS_EN.rglob("*.json")) + list(FORMS_AR.rglob("*.json"))

        for jf in all_jsons:
            csv_file = jf.with_suffix('.csv')
            self.assertTrue(csv_file.exists(), f"Matching CSV file not found for {jf}")

            with open(jf, "r", encoding="utf-8") as f:
                json_data = json.load(f)
            json_field_count = len(json_data.get("fields", {}))

            with open(csv_file, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                header = next(reader, None)
                csv_rows = list(reader)

            self.assertEqual(
                json_field_count, len(csv_rows),
                f"Field count mismatch between JSON ({json_field_count}) and CSV ({len(csv_rows)}) in {jf.name}"
            )

if __name__ == "__main__":
    unittest.main()
