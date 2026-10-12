#!/usr/bin/env python3
"""
Generate completed-data companion schemas and test fixtures for all deliverables.
Preserves existing manual companion schemas without overwriting.
"""

import json
import re
from pathlib import Path
from collections import defaultdict
import jsonschema

from tasleemat.validation import preflight_schema

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "tasleemat" / "data" / "catalog.json"
SCHEMAS_DIR = ROOT / "tasleemat" / "schemas" / "completed"
FIXTURES_DIR = ROOT / "tests" / "fixtures"

def to_slug(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "_", text).strip("_").lower()
    return re.sub(r"_+", "_", s)

def generate_schema_for_artifact(art: dict) -> dict:
    aid = art["artifact_id"]
    title_en = art["name_en"]
    schema_path = ROOT / art["assets"]["en"]["schema"]
    
    with open(schema_path, "r", encoding="utf-8") as f:
        form_data = json.load(f)
        
    sections = defaultdict(dict)
    for raw_k, fld in form_data.get("fields", {}).items():
        sec_name = fld.get("section", "General Information")
        sec_slug = to_slug(sec_name)
        
        lbl = fld.get("label", raw_k)
        fld_slug = to_slug(lbl)
        if aid == "PMO-00.02" and raw_k == "f31_Escalation_Path":
            fld_slug = "decision_escalation_path"
            
        sections[sec_slug][fld_slug] = {
            "type": "string",
            "minLength": 1,
            "description": fld.get("guidance", lbl)
        }
        
    properties = {
        "artifact_id": {
            "type": "string",
            "const": aid
        },
        "metadata": {
            "type": "object",
            "properties": {
                "project_name": {"type": "string", "minLength": 1},
                "project_code": {"type": "string"},
                "date_prepared": {"type": "string", "format": "date"},
                "project_manager": {"type": "string", "minLength": 1},
                "prepared_by": {"type": "string", "minLength": 1},
                "version": {"type": "string"},
                "status": {
                    "type": "string",
                    "enum": ["draft", "baselined", "in_review", "approved"]
                }
            },
            "required": ["project_name", "date_prepared", "project_manager", "prepared_by"]
        }
    }
    
    req_sections = ["artifact_id", "metadata"]
    for sec_slug, flds in sections.items():
        properties[sec_slug] = {
            "type": "object",
            "properties": flds,
            "required": list(flds.keys())
        }
        req_sections.append(sec_slug)
        
    companion = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"https://tasleemat.pmo/schemas/completed/{aid}.schema.json",
        "title": f"Completed {title_en} Data Contract",
        "description": f"Additive structural schema validating completed {title_en} artifact data payloads ({aid}).",
        "type": "object",
        "properties": properties,
        "required": req_sections
    }
    return companion


def generate_fixtures_for_schema(aid: str, schema: dict):
    # 1. Valid fixture
    valid_payload = {
        "artifact_id": aid,
        "metadata": {
            "project_name": "Digital Transformation Core",
            "project_code": f"PRJ-2026-{aid.replace('.', '-').replace('PMO-', '')}",
            "date_prepared": "2026-10-12",
            "project_manager": "Sarah Jenkins",
            "prepared_by": "PMO Governance Directorate",
            "version": "1.0",
            "status": "approved"
        }
    }
    
    # 2. Invalid fixture (bad date, bad status, empty strings)
    invalid_payload = {
        "artifact_id": aid,
        "metadata": {
            "project_name": "Digital Transformation Core",
            "project_code": f"PRJ-2026-{aid.replace('.', '-').replace('PMO-', '')}",
            "date_prepared": "2026-02-29",  # Invalid calendar date
            "project_manager": "Sarah Jenkins",
            "prepared_by": "PMO Governance Directorate",
            "version": "1.0",
            "status": "not_an_enum"
        }
    }
    
    # 3. Draft fixture (incomplete sections, valid metadata)
    draft_payload = {
        "artifact_id": aid,
        "metadata": {
            "project_name": "Digital Transformation Core",
            "project_code": f"PRJ-2026-{aid.replace('.', '-').replace('PMO-', '')}",
            "date_prepared": "2026-10-12",
            "project_manager": "Sarah Jenkins",
            "prepared_by": "PMO Governance Directorate",
            "version": "0.1",
            "status": "draft"
        }
    }
    
    props = schema.get("properties", {})
    for sec_name, sec_obj in props.items():
        if sec_name in ("artifact_id", "metadata"):
            continue
        valid_payload[sec_name] = {}
        invalid_payload[sec_name] = {}
        draft_payload[sec_name] = {}
        
        flds = sec_obj.get("properties", {})
        for idx, (f_name, f_obj) in enumerate(flds.items()):
            label_text = f_name.replace("_", " ").title()
            valid_payload[sec_name][f_name] = f"Substantive completed details for {label_text}."
            invalid_payload[sec_name][f_name] = ""  # Violates minLength: 1
            if idx == 0:
                draft_payload[sec_name][f_name] = f"Draft notes for {label_text}."
                
    return valid_payload, invalid_payload, draft_payload


def main():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        cat = json.load(f)
        
    created_schemas = 0
    created_fixtures = 0
    
    for art in cat["artifacts"]:
        aid = art["artifact_id"]
        schema_file = SCHEMAS_DIR / f"{aid}.schema.json"
        
        # Only generate if schema does not already exist
        if not schema_file.exists():
            schema = generate_schema_for_artifact(art)
            
            # Verify validity
            jsonschema.Draft202012Validator.check_schema(schema)
            errs = preflight_schema(schema)
            if errs:
                raise ValueError(f"Preflight error in {aid}: {errs}")
                
            with open(schema_file, "w", encoding="utf-8") as f:
                json.dump(schema, f, indent=2, ensure_ascii=False)
            created_schemas += 1
        else:
            with open(schema_file, "r", encoding="utf-8") as f:
                schema = json.load(f)
                
        # Fixtures check / generation
        valid_file = FIXTURES_DIR / "valid" / f"{aid}_valid.json"
        invalid_file = FIXTURES_DIR / "invalid" / f"{aid}_invalid.json"
        draft_file = FIXTURES_DIR / "draft" / f"{aid}_draft.json"
        
        # Check if alternative invalid fixtures exist (e.g. _missing_required, _invalid_types)
        existing_invalids = list((FIXTURES_DIR / "invalid").glob(f"{aid}_*.json"))
        
        if not valid_file.exists() or not existing_invalids or not draft_file.exists():
            v_p, inv_p, dr_p = generate_fixtures_for_schema(aid, schema)
            if not valid_file.exists():
                with open(valid_file, "w", encoding="utf-8") as f:
                    json.dump(v_p, f, indent=2, ensure_ascii=False)
                created_fixtures += 1
            if not existing_invalids:
                with open(invalid_file, "w", encoding="utf-8") as f:
                    json.dump(inv_p, f, indent=2, ensure_ascii=False)
                created_fixtures += 1
            if not draft_file.exists():
                with open(draft_file, "w", encoding="utf-8") as f:
                    json.dump(dr_p, f, indent=2, ensure_ascii=False)
                created_fixtures += 1

    print(f"Schema generation complete: created {created_schemas} new companion schemas, {created_fixtures} fixtures.")


if __name__ == "__main__":
    main()
