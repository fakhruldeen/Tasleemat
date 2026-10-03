#!/usr/bin/env python3
"""Generate the official root datapackage.json conforming to the
Open Knowledge Foundation (OKF) Frictionless Data Package Standard
using native JSON Schemas for all 204 project management artifacts.
"""

import os
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_DIR = ROOT / "forms"
DATAPACKAGE_PATH = ROOT / "datapackage.json"

JSON_SCHEMA_DEF = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "form_name": {
            "type": "string",
            "description": "The official standard name of the PMO deliverable."
        },
        "document_reference": {
            "type": "string",
            "description": "Standardized PMO governance code (e.g. PMO-03.01)."
        },
        "_llm_instructions": {
            "type": "string",
            "description": "System prompt and execution instructions for AI LLM generation."
        },
        "project_title": {
            "type": "string",
            "description": "Name or title of the project."
        },
        "date_prepared": {
            "type": "string",
            "description": "ISO date of deliverable preparation."
        },
        "fields": {
            "type": "object",
            "description": "Dictionary of standardized deliverable sections, labels, guidance, and values.",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "section": {"type": "string"},
                    "label": {"type": "string"},
                    "guidance": {"type": "string"},
                    "value": {"type": "string"}
                },
                "required": ["section", "label", "guidance"]
            }
        }
    },
    "required": ["form_name", "document_reference", "fields"]
}

def build_datapackage():
    print("=== Generating Open Knowledge Foundation (OKF) JSON Data Package Manifest ===")

    resources = []
    
    # 1. English JSON Schemas (forms/en/**/*.json)
    for json_file in sorted(FORMS_DIR.glob("en/**/*.json")):
        rel_path = json_file.relative_to(ROOT).as_posix()
        slug = re.sub(r'[^a-zA-Z0-9_-]', '-', json_file.stem).lower()
        resource_name = f"en-{slug}"
        
        # Read file to extract title and document ref
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                content = json.load(f)
                title = content.get("form_name", json_file.stem.replace('_', ' '))
                doc_ref = content.get("document_reference", "")
        except Exception:
            title = json_file.stem.replace('_', ' ')
            doc_ref = ""
        
        resources.append({
            "name": resource_name,
            "title": title,
            "reference": doc_ref,
            "path": rel_path,
            "format": "json",
            "mediatype": "application/json",
            "encoding": "utf-8",
            "language": "en",
            "direction": "ltr",
            "schema": JSON_SCHEMA_DEF
        })

    # 2. Arabic JSON Schemas (forms/ar/**/*.json)
    for json_file in sorted(FORMS_DIR.glob("ar/**/*.json")):
        rel_path = json_file.relative_to(ROOT).as_posix()
        slug = re.sub(r'[^a-zA-Z0-9_\u0600-\u06FF-]', '-', json_file.stem).lower()
        resource_name = f"ar-{slug}"
        
        try:
            with open(json_file, "r", encoding="utf-8") as f:
                content = json.load(f)
                title = content.get("form_name", json_file.stem.replace('_', ' '))
                doc_ref = content.get("document_reference", "")
        except Exception:
            title = json_file.stem.replace('_', ' ')
            doc_ref = ""
        
        resources.append({
            "name": resource_name,
            "title": title,
            "reference": doc_ref,
            "path": rel_path,
            "format": "json",
            "mediatype": "application/json",
            "encoding": "utf-8",
            "language": "ar-SA",
            "direction": "rtl",
            "schema": JSON_SCHEMA_DEF
        })

    datapackage = {
        "profile": "data-package",
        "name": "tasleemat-pmo-framework",
        "title": "Tasleemat: Enterprise Bilingual (English & Arabic) Project Management Framework",
        "description": "Complete open, machine-readable Project Management Office (PMO) artifact library with 102 bilingual deliverable JSON schemas conforming to PMI PMBOK® 6th, 7th & 8th Edition standards and the Open Knowledge Foundation (OKF) Frictionless Data specification.",
        "version": "2.0.0",
        "homepage": "https://github.com/fakhruldeen/Tasleemat",
        "licenses": [
            {
                "name": "MIT",
                "path": "https://opensource.org/licenses/MIT",
                "title": "MIT License"
            }
        ],
        "keywords": [
            "project-management",
            "pmo",
            "pmbok",
            "open-knowledge",
            "frictionless-data",
            "json-schema",
            "arabic",
            "bilingual",
            "ai-governance",
            "agile",
            "esg"
        ],
        "contributors": [
            {
                "title": "Tasleemat Contributors",
                "role": "author"
            }
        ],
        "resources": resources
    }

    with open(DATAPACKAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(datapackage, f, ensure_ascii=False, indent=2)

    print(f"✅ Created datapackage.json with {len(resources)} JSON Schema Resources ({len(resources)//2} EN + {len(resources)//2} AR).")

if __name__ == "__main__":
    build_datapackage()
