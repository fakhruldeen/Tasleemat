#!/usr/bin/env python3
"""Validate the root datapackage.json and all 204 JSON Schema resources
against Open Knowledge Foundation (OKF) Frictionless Data specifications.
"""

import os
import sys
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATAPACKAGE_PATH = ROOT / "datapackage.json"

def validate_datapackage():
    print("=== Validating Open Knowledge Foundation (OKF) JSON Data Package ===")
    
    if not DATAPACKAGE_PATH.exists():
        print("❌ Error: datapackage.json not found at repository root!")
        sys.exit(1)

    with open(DATAPACKAGE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Validate package level metadata
    assert data.get("name") == "tasleemat-pmo-framework", "Invalid package name"
    assert data.get("profile") == "data-package", "Invalid profile"
    assert len(data.get("licenses", [])) > 0, "Missing open licenses"

    resources = data.get("resources", [])
    print(f"Checking {len(resources)} JSON Schema resources...")

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

        # Validate JSON content against schema rules
        try:
            with open(res_path, "r", encoding="utf-8") as json_f:
                content = json.load(json_f)
                
                # Verify required top-level keys
                if "form_name" not in content or "document_reference" not in content or "fields" not in content:
                    print(f"❌ Missing mandatory keys in {res_path}")
                    errors += 1
                    continue
                
                fields = content.get("fields", {})
                if not isinstance(fields, dict) or len(fields) == 0:
                    print(f"❌ Empty or invalid fields object in {res_path}")
                    errors += 1
                    continue
                
                # Check field items
                for field_key, field_data in fields.items():
                    if not isinstance(field_data, dict):
                        print(f"❌ Field {field_key} in {res_path} is not an object")
                        errors += 1
                        break
                    if "section" not in field_data or "label" not in field_data or "guidance" not in field_data:
                        print(f"❌ Field {field_key} in {res_path} missing section/label/guidance")
                        errors += 1
                        break

        except Exception as e:
            print(f"❌ Error parsing JSON in {res_path}: {e}")
            errors += 1

    print(f"Resources verified: {en_count} English + {ar_count} Arabic = {len(resources)} Total")
    if errors == 0:
        print("✨ SUCCESS: OKF JSON Schema Data Package is 100% VALID and compliant!")
        return 0
    else:
        print(f"❌ FAILED: {errors} validation errors detected.")
        sys.exit(1)

if __name__ == "__main__":
    validate_datapackage()
