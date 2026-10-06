#!/usr/bin/env python3
"""
Validate Markdown files for OKF (Open Knowledge Format) conformance and Tasleemat Local Profile.
"""

import os
import sys
import re

def validate_okf():
    exclude_dirs = {'.venv', 'scratch', '.github', '.pytest_cache', '__pycache__', '.git', '_tokens'}
    
    okf_errors = 0
    profile_errors = 0
    checked = 0

    print("=== Pass 1: OKF v0.2 Structural Conformance ===")
    for root_dir, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
        
        for file in files:
            if not file.endswith('.md'):
                continue
                
            filepath = os.path.join(root_dir, file)
            is_root = (root_dir == '.')
            in_forms = 'forms' in root_dir.split(os.sep)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if file == 'log.md':
                continue
                
            # OKF Conformance
            if not content.startswith('---'):
                print(f"❌ OKF FAIL: {filepath} is missing YAML frontmatter.")
                okf_errors += 1
                continue
                
            end_idx = content.find('\n---', 3)
            if end_idx == -1:
                print(f"❌ OKF FAIL: {filepath} has unclosed YAML frontmatter.")
                okf_errors += 1
                continue
                
            frontmatter = content[3:end_idx]
            match = re.search(r'^type:\s*(.+)$', frontmatter, re.MULTILINE)
            if not match or not match.group(1).strip():
                print(f"❌ OKF FAIL: {filepath} is missing a valid 'type' field.")
                okf_errors += 1
                
            # Pre-tokenization check
            token_pointer_match = re.search(r'^token_pointer:\s*(.+)$', frontmatter, re.MULTILINE)
            if token_pointer_match:
                pointer = token_pointer_match.group(1).strip()
                if pointer.startswith('/'):
                    pointer = pointer[1:]
                if not os.path.exists(pointer):
                    print(f"❌ OKF FAIL: {filepath} token_pointer '{pointer}' does not exist.")
                    okf_errors += 1
                    
            # Tasleemat Profile Conformance (Only inside forms/)
            if in_forms and file != 'index.md' and file != 'README.md':
                # Check for language
                lang_match = re.search(r'^language:\s*(en|ar)$', frontmatter, re.MULTILINE)
                lang_alt_match = re.search(r'^lang:\s*(en|ar)$', frontmatter, re.MULTILINE)
                if not lang_match and not lang_alt_match:
                    # In Tasleemat, path often contains /en/ or /ar/
                    if '/en/' not in filepath and '/ar/' not in filepath:
                        print(f"⚠️ PROFILE WARN: {filepath} lacks explicit language frontmatter.")
                        profile_errors += 1
                
                # Check for status
                status_match = re.search(r'^status:\s*(draft|review|approved)$', frontmatter, re.MULTILINE)
                if not status_match:
                    pass # We will warn about this later if it's a template
                    
                # If it's a template, it should have a form_id
                type_val = match.group(1).strip() if match else ""
                if 'Template' in type_val or 'Form' in type_val:
                    form_id_match = re.search(r'^form_id:\s*(.+)$', frontmatter, re.MULTILINE)
                    if not form_id_match:
                        print(f"⚠️ PROFILE FAIL: {filepath} is a template but missing 'form_id'.")
                        profile_errors += 1
                        
            checked += 1

    print(f"\nChecked {checked} markdown files.")
    print(f"OKF Conformance Errors: {okf_errors}")
    print(f"Tasleemat Profile Warnings/Errors: {profile_errors}")
    
    if okf_errors > 0:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(validate_okf())
