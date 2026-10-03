#!/usr/bin/env python3
"""Tests for Open Knowledge Foundation (OKF) Frictionless Data Package compliance.
"""

import unittest
import pathlib
import json

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATAPACKAGE_PATH = ROOT / "datapackage.json"

class TestOKFDataPackage(unittest.TestCase):

    def setUp(self):
        self.assertTrue(DATAPACKAGE_PATH.exists(), "datapackage.json not found at repository root")
        with open(DATAPACKAGE_PATH, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def test_package_metadata(self):
        """Verify package-level metadata compliance."""
        self.assertEqual(self.data.get("name"), "tasleemat-pmo-framework")
        self.assertEqual(self.data.get("profile"), "data-package")
        self.assertIn("version", self.data)
        self.assertIn("licenses", self.data)
        self.assertGreater(len(self.data["licenses"]), 0)
        self.assertEqual(self.data["licenses"][0]["name"], "MIT")

    def test_resource_count_and_uniqueness(self):
        """Verify exactly 204 unique resources exist in datapackage.json."""
        resources = self.data.get("resources", [])
        self.assertEqual(len(resources), 204, f"Expected 204 resources, got {len(resources)}")

        names = [r["name"] for r in resources]
        self.assertEqual(len(names), len(set(names)), "Duplicate resource names found in datapackage.json")

    def test_resource_paths_and_properties(self):
        """Verify all resource paths point to real files with correct metadata."""
        resources = self.data.get("resources", [])
        en_count = 0
        ar_count = 0

        for r in resources:
            path_str = r.get("path")
            self.assertIsNotNone(path_str, f"Resource {r.get('name')} has no path")
            
            file_path = ROOT / path_str
            self.assertTrue(file_path.exists(), f"Resource file missing on disk: {path_str}")
            
            self.assertEqual(r.get("format"), "json")
            self.assertEqual(r.get("mediatype"), "application/json")
            self.assertEqual(r.get("encoding"), "utf-8")

            lang = r.get("language")
            direction = r.get("direction")
            if "en/" in path_str:
                self.assertEqual(lang, "en")
                self.assertEqual(direction, "ltr")
                en_count += 1
            elif "ar/" in path_str:
                self.assertEqual(lang, "ar-SA")
                self.assertEqual(direction, "rtl")
                ar_count += 1

            # Validate reference format
            ref = r.get("reference")
            self.assertTrue(ref.startswith("PMO-"), f"Invalid reference '{ref}' in {r.get('name')}")

        self.assertEqual(en_count, 102)
        self.assertEqual(ar_count, 102)

if __name__ == "__main__":
    unittest.main()
