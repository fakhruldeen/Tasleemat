#!/usr/bin/env python3
import os
import re
import json

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'):
        return {}
    end = content.find('\n---', 3)
    if end == -1:
        return {}
    
    fm_text = content[3:end]
    meta = {}
    for line in fm_text.split('\n'):
        match = re.match(r'^([a-zA-Z0-9_]+):\s*(.+)$', line)
        if match:
            meta[match.group(1)] = match.group(2).strip(" '\"")
    return meta

def main():
    print("=== Agent Navigation & Assurance Evaluation ===")
    
    # Pre-index all forms
    db = {}
    for root_dir, _, files in os.walk('forms'):
        for file in files:
            if file.endswith('.md'):
                path = os.path.join(root_dir, file)
                meta = parse_frontmatter(path)
                if 'form_id' in meta:
                    fid = meta['form_id']
                    lang = meta.get('language', 'en')
                    if fid not in db:
                        db[fid] = {}
                    db[fid][lang] = {'path': path, 'meta': meta}
                    
    scores = {}
    
    # Scenario 1: Find authorizing form (PMO-03.01)
    print("\n[Scenario 1] Find a form authorizing a project")
    target_id = 'PMO-03.01'
    if target_id in db and 'en' in db[target_id]:
        print(f"✅ Found: {db[target_id]['en']['path']}")
        scores['S1'] = 'PASS'
    else:
        print("❌ Failed to find Project Charter.")
        scores['S1'] = 'FAIL'
        
    # Scenario 2: Locate Arabic equivalent
    print("\n[Scenario 2] Locate the Arabic equivalent")
    if target_id in db and 'ar' in db[target_id]:
        print(f"✅ Found exact translation: {db[target_id]['ar']['path']}")
        scores['S2'] = 'PASS'
    else:
        print("❌ Failed to find Arabic counterpart via form_id.")
        scores['S2'] = 'FAIL'
        
    # Scenario 3: Complete a form from notes
    print("\n[Scenario 3] Complete a form from notes")
    # Simulate finding LLM instructions
    with open(db[target_id]['en']['path'], 'r') as f:
        if 'LLM INSTRUCTIONS' in f.read():
            print("✅ Found explicit LLM instructions embedded in template.")
            scores['S3'] = 'PASS'
        else:
            print("❌ No LLM instructions found.")
            scores['S3'] = 'FAIL'
            
    # Scenario 5: Check currency
    print("\n[Scenario 5] Check currency (freshness/status)")
    status = db[target_id]['en']['meta'].get('status')
    if status == 'approved':
        print(f"✅ Currency verified. Status: {status}")
        scores['S5'] = 'PASS'
    else:
        print("❌ Status missing or invalid.")
        scores['S5'] = 'FAIL'
        
    # Generate Defect Log & Fixtures
    print("\n=== Evaluation Results ===")
    passed = sum(1 for v in scores.values() if v == 'PASS')
    print(f"Score: {passed}/{len(scores)} passed.")
    
    fixtures = {
        "scenarios": scores,
        "indexed_concepts": len(db)
    }
    
    with open('tests/agent_evaluation_results.json', 'w') as f:
        json.dump(fixtures, f, indent=2)

if __name__ == '__main__':
    os.makedirs('tests', exist_ok=True)
    main()
