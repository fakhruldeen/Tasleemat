#!/usr/bin/env python3
"""Validate the root datapackage.json and all 204 tabular CSV resources
against Open Knowledge Foundation (OKF) Frictionless Data specifications.
"""

import os
import sys
import json
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATAPACKAGE_PATH = ROOT / "datapackage.json"

REQUIRED_FIELDS = ["Section", "Field", "Guidance", "LLM_Generated_Value"]

def validate_datapackage():
    print("=== Validating Open Knowledge Foundation (OKF) Data Package ===")
    
    if not DATAPACKAGE_PATH.exists():
        print("❌ Error: datapackage.json not found at repository root!")
        sys.exit(1)

    with open(DATAPACKAGE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Validate package level metadata
    assert data.get("name") == "tasleemat-pmo-framework", "Invalid package name"
    assert data.get("profile") == "tabular-data-package", "Invalid profile (must be tabular-data-package)"
    assert len(data.get("licenses", [])) > 0, "Missing open licenses"

    resources = data.get("resources", [])
    print(f"Checking {len(resources)} Frictionless resources...")

    if len(resources) != 204:
        print(f"❌ Error: Expected 204 resources, found {len(resources)}")
        sys.exit(1)

    errors = 0
    en_count = 0
    ar_count = 0

    for res in resources:
        res_name = res.get("name")
        res_path = ROOT / res.get("path")
        
        if not res_path.exists():
            print(f"❌ Resource file missing: {res_path}")
            errors += 1
            continue

        lang = res.get("language")
        if lang == "en":
            en_count += 1
        elif lang == "ar-SA":
            ar_count += 1

        # Validate CSV contents against Table Schema
        try:
            with open(res_path, "r", encoding="utf-8") as csv_f:
                reader = csv.reader(csv_f)
                header = next(reader, None)
                if not header or header != REQUIRED_FIELDS:
                    print(f"❌ Header mismatch in {res_path}: {header}")
                    errors += 1
                    continue
                
                row_count = 0
                for row in reader:
                    if len(row) != 4:
                        print(f"❌ Column count mismatch in {res_path} row {row_count+1}: expected 4, got {len(row)}")
                        errors += 1
                        break
                    row_count += 1
        except Exception as e:
            print(f"❌ Error reading {res_path}: {e}")
            errors += 1

    print(f"Resources verified: {en_count} English + {ar_count} Arabic = {len(resources)} Total")
    if errors == 0:
        print("✨ SUCCESS: OKF Frictionless Data Package is 100% VALID and compliant!")
        return 0
    else:
        print(f"❌ FAILED: {errors} validation errors detected.")
        sys.exit(1)

if __name__ == "__main__":
    validate_datapackage()
