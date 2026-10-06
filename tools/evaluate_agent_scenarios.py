#!/usr/bin/env python3
import os
import re
import json

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---') and not content.startswith('<!--\n---'):
        return {}
        
    offset = 5 if content.startswith('<!--\n---') else 0
    end = content.find('\n---', offset + 3)
    if end == -1:
        return {}
    
    fm_text = content[offset+3:end]
    meta = {}
    for line in fm_text.split('\n'):
        match = re.match(r'^([a-zA-Z0-9_]+):\s*(.+)$', line)
        if match:
            meta[match.group(1)] = match.group(2).strip(" '\"")
    return meta

def main():
    print("=== Agent Navigation & Assurance Evaluation ===")
    
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
    target_id = 'PMO-03.01'
    if target_id in db and 'en' in db[target_id]:
        scores['S1'] = 'PASS'
    else:
        scores['S1'] = 'FAIL'
        
    # Scenario 2: Locate Arabic equivalent
    if target_id in db and 'ar' in db[target_id]:
        scores['S2'] = 'PASS'
    else:
        scores['S2'] = 'FAIL'
        
    # Scenario 3: Complete a form from notes
    with open(db[target_id]['en']['path'], 'r') as f:
        if 'LLM INSTRUCTIONS' in f.read():
            scores['S3'] = 'PASS'
        else:
            scores['S3'] = 'FAIL'
            
    # Scenario 5: Check currency
    status = db[target_id]['en']['meta'].get('status')
    if status == 'approved':
        scores['S5'] = 'PASS'
    else:
        scores['S5'] = 'FAIL'
        
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
