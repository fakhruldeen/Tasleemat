#!/usr/bin/env python3
"""Generate the official root datapackage.json conforming to the
Open Knowledge Foundation (OKF) Frictionless Data Package Standard.
"""

import os
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_DIR = ROOT / "forms"
DATAPACKAGE_PATH = ROOT / "datapackage.json"

TABLE_SCHEMA = {
    "fields": [
        {
            "name": "Section",
            "type": "string",
            "title": "Document Section",
            "description": "Lifecycle section, domain grouping, or table category within the PMO artifact.",
            "constraints": {
                "required": True
            }
        },
        {
            "name": "Field",
            "type": "string",
            "title": "Field Label",
            "description": "Standardized field name, parameter label, or table column header.",
            "constraints": {
                "required": True
            }
        },
        {
            "name": "Guidance",
            "type": "string",
            "title": "Practitioner Guidance",
            "description": "Instruction and contextual prompt guidelines for populating this field.",
            "constraints": {
                "required": True
            }
        },
        {
            "name": "LLM_Generated_Value",
            "type": "string",
            "title": "Target / Generated Value",
            "description": "Generated or placeholder value populated by the user or AI agent.",
            "constraints": {
                "required": False
            }
        }
    ],
    "primaryKey": ["Section", "Field"],
    "missingValues": [""]
}

def build_datapackage():
    print("=== Generating Open Knowledge Foundation (OKF) Data Package Manifest ===")

    resources = []
    
    # 1. English Resources (forms/en/**/*.csv)
    for csv_file in sorted(FORMS_DIR.glob("en/**/*.csv")):
        rel_path = csv_file.relative_to(ROOT).as_posix()
        # Clean slug name e.g. en-03-01-project-charter
        slug = re.sub(r'[^a-zA-Z0-9_-]', '-', csv_file.stem).lower()
        resource_name = f"en-{slug}"
        
        resources.append({
            "name": resource_name,
            "title": csv_file.stem.replace('_', ' '),
            "path": rel_path,
            "format": "csv",
            "mediatype": "text/csv",
            "encoding": "utf-8",
            "language": "en",
            "direction": "ltr",
            "schema": TABLE_SCHEMA
        })

    # 2. Arabic Resources (forms/ar/**/*.csv)
    for csv_file in sorted(FORMS_DIR.glob("ar/**/*.csv")):
        rel_path = csv_file.relative_to(ROOT).as_posix()
        # Clean slug name e.g. ar-03-01-project-charter
        slug = re.sub(r'[^a-zA-Z0-9_\u0600-\u06FF-]', '-', csv_file.stem).lower()
        resource_name = f"ar-{slug}"
        
        resources.append({
            "name": resource_name,
            "title": csv_file.stem.replace('_', ' '),
            "path": rel_path,
            "format": "csv",
            "mediatype": "text/csv",
            "encoding": "utf-8",
            "language": "ar-SA",
            "direction": "rtl",
            "schema": TABLE_SCHEMA
        })

    datapackage = {
        "profile": "tabular-data-package",
        "name": "tasleemat-pmo-framework",
        "title": "Tasleemat: Enterprise Bilingual (English & Arabic) Project Management Framework",
        "description": "Complete open, machine-readable Project Management Office (PMO) artifact library with 102 bilingual deliverable pairs conforming to PMI PMBOK® 6th, 7th & 8th Edition standards and the Open Knowledge Foundation (OKF) Frictionless Data specification.",
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

    print(f"✅ Created datapackage.json with {len(resources)} Frictionless Tabular Resources ({len(resources)//2} EN + {len(resources)//2} AR).")

if __name__ == "__main__":
    build_datapackage()
