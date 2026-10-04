#!/usr/bin/env python3
"""strip_redundant_dir_rtl.py
Removes redundant dir="rtl" and dir='rtl' attributes from HTML elements inside
Arabic Markdown templates, examples, guides, and documentation since the parent
<html> tag already sets dir="rtl".
"""

import os
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

def clean_file_content(text: str) -> str:
    # 1. Remove dir="rtl" or dir='rtl' from tags like <h1 dir="rtl">, <div dir="rtl">, etc.
    # e.g. <h3 dir="rtl" align="left"> -> <h3 align="left">
    # e.g. <h1 dir="rtl" align="center"> -> <h1 align="center">
    # e.g. <div dir="rtl"> -> <div>
    
    # Remove dir="rtl" attribute with surrounding spaces
    cleaned = re.sub(r'\s+dir=[\"\']rtl[\"\']', '', text)
    cleaned = re.sub(r'dir=[\"\']rtl[\"\']\s+', '', cleaned)
    cleaned = re.sub(r'dir=[\"\']rtl[\"\']', '', cleaned)
    
    # If there are standalone <div> tags right before <h3 align="left"> with a trailing </div> at EOF
    # Let's clean standalone empty <div> or </div> at the top/bottom if redundant
    cleaned = re.sub(r'\n<div>\s*\n\n<h3', '\n\n<h3', cleaned)
    cleaned = re.sub(r'\n<div>\s*\n<h3', '\n<h3', cleaned)
    
    return cleaned

def process_directory(dir_path: pathlib.Path):
    count = 0
    for md_file in dir_path.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        updated = clean_file_content(content)
        if updated != content:
            md_file.write_text(updated, encoding="utf-8")
            count += 1
    return count

def main():
    print("Stripping redundant dir=rtl attributes across Arabic files...")
    ar_forms = process_directory(ROOT / "forms" / "ar")
    ar_examples = process_directory(ROOT / "examples" / "ar")
    ar_guides = process_directory(ROOT / "guides" / "ar") if (ROOT / "guides" / "ar").exists() else 0
    docs_ar = process_directory(ROOT / "docs" / "forms" / "ar")
    docs_ex_ar = process_directory(ROOT / "docs" / "examples" / "ar")
    docs_guides_ar = process_directory(ROOT / "docs" / "guides" / "ar")
    docs_manuals_ar = process_directory(ROOT / "docs" / "ar")
    
    print(f"Cleaned:")
    print(f"  - forms/ar: {ar_forms} files")
    print(f"  - examples/ar: {ar_examples} files")
    print(f"  - docs/forms/ar: {docs_ar} files")
    print(f"  - docs/examples/ar: {docs_ex_ar} files")
    print(f"  - docs/guides/ar: {docs_guides_ar} files")
    print(f"  - docs/ar: {docs_manuals_ar} files")

if __name__ == "__main__":
    main()
