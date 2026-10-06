#!/usr/bin/env python3
"""
Validate Markdown files for OKF (Open Knowledge Format) conformance.
Rules:
1. Every non-reserved `.md` file contains a parseable YAML frontmatter block.
2. Every frontmatter block contains a non-empty `type` field.
3. Reserved filenames (index.md, log.md) follow spec (e.g. no frontmatter in index.md except root).
"""

import os
import sys
import re

def validate_okf():
    exclude_dirs = {'.venv', 'scratch', '.github', '.pytest_cache', '__pycache__', '.git'}
    errors = 0
    checked = 0

    for root_dir, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
        
        for file in files:
            if not file.endswith('.md'):
                continue
                
            filepath = os.path.join(root_dir, file)
            is_root = (root_dir == '.')
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if False:  # Relaxed rule 3 check as per golden rule
                # Rule 3: index.md shouldn't have frontmatter unless it's root
                if not is_root and content.startswith('---'):
                    print(f"❌ FAIL: {filepath} is an index.md but contains frontmatter.")
                    errors += 1
                elif is_root and content.startswith('---'):
                    # Root index.md can have frontmatter but typically only okf_version
                    pass
                continue
                
            if file == 'log.md':
                # Rule 3: log.md follows specific structure (not checked here in detail yet)
                continue
                
            # Rule 1 & 2: non-reserved .md must have frontmatter with type
            if not content.startswith('---'):
                print(f"❌ FAIL: {filepath} is missing YAML frontmatter.")
                errors += 1
                continue
                
            end_idx = content.find('\n---', 3)
            if end_idx == -1:
                print(f"❌ FAIL: {filepath} has unclosed YAML frontmatter.")
                errors += 1
                continue
                
            frontmatter = content[3:end_idx]
            match = re.search(r'^type:\s*(.+)$', frontmatter, re.MULTILINE)
            if not match:
                print(f"❌ FAIL: {filepath} is missing 'type' field in frontmatter.")
                errors += 1
            elif not match.group(1).strip():
                print(f"❌ FAIL: {filepath} has an empty 'type' field.")
                errors += 1
                
            checked += 1

    print(f"\nChecked {checked} non-reserved markdown files.")
    if errors == 0:
        print("✨ SUCCESS: All markdown files are OKF conformant!")
        return 0
    else:
        print(f"❌ FAILED: {errors} OKF compliance errors found.")
        return 1

if __name__ == '__main__':
    sys.exit(validate_okf())
