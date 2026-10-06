#!/usr/bin/env python3
"""
Validate Markdown files for OKF (Open Knowledge Format) conformance.
Rules:
1. Every non-reserved `.md` file contains a parseable YAML frontmatter block.
2. Every frontmatter block contains a non-empty `type` field.
3. If LLM pre-tokenization is used, token_pointer, token_count, and tokenizer_model_id must be valid.
"""

import os
import sys
import re

def validate_okf():
    exclude_dirs = {'.venv', 'scratch', '.github', '.pytest_cache', '__pycache__', '.git', '_tokens'}
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
                
            if file == 'log.md':
                continue
                
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
                
            # LLM Pre-tokenization check
            token_pointer_match = re.search(r'^token_pointer:\s*(.+)$', frontmatter, re.MULTILINE)
            if token_pointer_match:
                pointer = token_pointer_match.group(1).strip()
                # Remove leading slash for local path check
                if pointer.startswith('/'):
                    pointer = pointer[1:]
                    
                if not os.path.exists(pointer):
                    print(f"❌ FAIL: {filepath} token_pointer '{pointer}' does not exist.")
                    errors += 1
                    
                if not re.search(r'^token_count:\s*\d+$', frontmatter, re.MULTILINE):
                    print(f"❌ FAIL: {filepath} has token_pointer but missing valid token_count.")
                    errors += 1
                    
                if not re.search(r'^tokenizer_model_id:\s*.+$', frontmatter, re.MULTILINE):
                    print(f"❌ FAIL: {filepath} has token_pointer but missing tokenizer_model_id.")
                    errors += 1
                    
            checked += 1

    print(f"\nChecked {checked} markdown files.")
    if errors == 0:
        print("✨ SUCCESS: All markdown files are OKF conformant (including token pointers)!")
        return 0
    else:
        print(f"❌ FAILED: {errors} OKF compliance errors found.")
        return 1

if __name__ == '__main__':
    sys.exit(validate_okf())
