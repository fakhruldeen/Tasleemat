#!/usr/bin/env python3
"""
Deterministic Catalog Generator for Tasleemat
Generates tasleemat/data/catalog.json from existing repository assets,
datapackage.json, and TIER_PACKS definitions without modifying forms/.
"""

import os
import sys
import json
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
FORMS_EN = ROOT / "forms" / "en"
FORMS_AR = ROOT / "forms" / "ar"
EXAMPLES_EN = ROOT / "examples" / "en"
EXAMPLES_AR = ROOT / "examples" / "ar"
DATAPACKAGE_PATH = ROOT / "datapackage.json"
OUTPUT_CATALOG = ROOT / "tasleemat" / "data" / "catalog.json"

# Import TIER_PACKS from tasleemat_cli
sys.path.insert(0, str(ROOT))
from tools.tasleemat_cli import TIER_PACKS

PHASE_NAMES = {
    "00": {"en": "Program and Portfolio Management", "ar": "إدارة البرامج والمحافظ"},
    "01": {"en": "Business and Value Delivery", "ar": "الأعمال وتسليم القيمة"},
    "02": {"en": "Project Approach and Tailoring", "ar": "منهجية المشروع وتخصيصه"},
    "03": {"en": "Initiating", "ar": "البدء"},
    "04": {"en": "Planning", "ar": "التخطيط"},
    "05": {"en": "Executing", "ar": "التنفيذ"},
    "06": {"en": "Monitoring and Controlling", "ar": "المراقبة والتحكم"},
    "07": {"en": "Closing", "ar": "الإغلاق"},
}

COMPANION_SCHEMAS = {
    "PMO-03.01": "schemas/completed/PMO-03.01.schema.json",
    "PMO-04.08.02": "schemas/completed/PMO-04.08.02.schema.json",
    "PMO-06.01": "schemas/completed/PMO-06.01.schema.json",
}

def compute_file_sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def find_asset_bundles():
    """Discover all 114 artifact bundles in EN and match with AR."""
    en_templates = sorted(FORMS_EN.rglob("*_Template.md"))
    artifacts = []

    for t_en in en_templates:
        folder_en = t_en.parent
        match = re.match(r"^(\d{2}(?:_\d{2})+)", t_en.name)
        if not match:
            continue
        prefix = match.group(1)
        phase_code = prefix.split("_")[0]

        # Read JSON in EN folder
        json_en_list = list(folder_en.glob("*.json"))
        if not json_en_list:
            continue
        json_en_path = json_en_list[0]
        with open(json_en_path, "r", encoding="utf-8") as f:
            data_en = json.load(f)

        doc_ref = data_en.get("document_reference", f"PMO-{prefix.replace('_', '.')}")
        title_en = data_en.get("form_name", "")

        # Find other EN files
        guide_en = list(folder_en.glob("*_Guide.md"))[0]
        prompt_en = [p for p in folder_en.glob("*.md") if not p.name.endswith(("_Template.md", "_Guide.md"))][0]
        csv_en = list(folder_en.glob("*.csv"))[0]

        # Find EN example
        example_en_pattern = f"**/{prefix}*_Example.md"
        example_en_matches = list(EXAMPLES_EN.glob(example_en_pattern))
        example_en_path = example_en_matches[0] if example_en_matches else None

        # Find matching AR folder
        ar_templates = list(FORMS_AR.rglob(f"{prefix}*_قالب.md"))
        if not ar_templates:
            raise RuntimeError(f"Missing Arabic template for prefix {prefix}")
        t_ar = ar_templates[0]
        folder_ar = t_ar.parent

        json_ar_list = list(folder_ar.glob("*.json"))
        json_ar_path = json_ar_list[0]
        with open(json_ar_path, "r", encoding="utf-8") as f:
            data_ar = json.load(f)
        title_ar = data_ar.get("form_name", "")

        guide_ar = list(folder_ar.glob("*_دليل.md"))[0]
        prompt_ar = [p for p in folder_ar.glob("*.md") if not p.name.endswith(("_قالب.md", "_دليل.md"))][0]
        csv_ar = list(folder_ar.glob("*.csv"))[0]

        # Find AR example
        example_ar_pattern = f"**/{prefix}*_مثال.md"
        example_ar_matches = list(EXAMPLES_AR.glob(example_ar_pattern))
        example_ar_path = example_ar_matches[0] if example_ar_matches else None

        # Tailoring mappings from TIER_PACKS
        applicable_tiers = []
        applicable_packs = {}
        for tier_num, tier_info in TIER_PACKS.items():
            matched_packs = []
            for pack_name, pack_items in tier_info.items():
                if pack_name == "name":
                    continue
                # Match doc_ref or prefix
                clean_ref = doc_ref.replace("PMO-", "").replace(".", "_")
                for item in pack_items:
                    item_clean = item.replace("PMO-", "").replace(".", "_")
                    if item_clean == clean_ref or clean_ref.startswith(item_clean):
                        matched_packs.append(pack_name)
                        break
            if matched_packs:
                applicable_tiers.append(tier_num)
                applicable_packs[tier_num] = sorted(list(set(matched_packs)))

        # Relative paths
        rel = lambda p: str(p.relative_to(ROOT)) if p else None

        entry = {
            "artifact_id": doc_ref,
            "prefix": prefix,
            "phase_code": phase_code,
            "phase_name_en": PHASE_NAMES.get(phase_code, {}).get("en", ""),
            "phase_name_ar": PHASE_NAMES.get(phase_code, {}).get("ar", ""),
            "name_en": title_en,
            "name_ar": title_ar,
            "fingerprint": compute_file_sha256(t_en),
            "assets": {
                "en": {
                    "template": rel(t_en),
                    "guide": rel(guide_en),
                    "prompt": rel(prompt_en),
                    "schema": rel(json_en_path),
                    "dictionary": rel(csv_en),
                    "example": rel(example_en_path),
                },
                "ar": {
                    "template": rel(t_ar),
                    "guide": rel(guide_ar),
                    "prompt": rel(prompt_ar),
                    "schema": rel(json_ar_path),
                    "dictionary": rel(csv_ar),
                    "example": rel(example_ar_path),
                }
            },
            "tailoring": {
                "tiers": sorted(applicable_tiers),
                "packs_by_tier": applicable_packs,
            },
            "companion_data_schema": COMPANION_SCHEMAS.get(doc_ref),
        }
        artifacts.append(entry)

    # Sort deterministically by artifact_id
    artifacts.sort(key=lambda x: x["artifact_id"])
    return artifacts

def build_catalog():
    print("Generating canonical Tasleemat artifact catalog...")
    artifacts = find_asset_bundles()
    print(f"Discovered {len(artifacts)} unique artifact definitions.")

    catalog_data = {
        "version": "2.4.1",
        "description": "Canonical Tasleemat PMO Artifact Registry",
        "generated_from": "datapackage.json & forms/ baseline",
        "total_artifacts": len(artifacts),
        "artifacts": artifacts,
    }

    OUTPUT_CATALOG.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CATALOG, "w", encoding="utf-8") as f:
        json.dump(catalog_data, f, indent=2, ensure_ascii=False)
    print(f"Catalog successfully written to: {OUTPUT_CATALOG.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    sys.exit(build_catalog())
