#!/usr/bin/env python3
import os
import sys
import re

def migrate():
    processed = 0
    errors = 0
    
    for root_dir, dirs, files in os.walk('forms'):
        for file in files:
            if not file.endswith('.md'):
                continue
                
            filepath = os.path.join(root_dir, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not (content.startswith('---') or content.startswith('<!--
---')):
                continue
                
            offset = 5 if content.startswith('<!--
---') else 0
            end_idx = content.find('
---', offset + 3)
            if end_idx == -1:
                continue
                
            frontmatter = content[offset+3:end_idx]
            body = content[end_idx+4:]
            if content.startswith('<!--
---') and body.startswith('
-->'):
                body = body[4:]
            
            # Identify if it's a template or guide
            is_template = 'Template' in file or 'قالب' in file or 'نموذج' in file or file == 'index.md' or file == 'README.md'
            # Actually, the profile says "Template" needs form_id. 
            # We will apply form_id to any file that has an ID prefix like XX_XX_XX
            id_match = re.match(r'^(\d+_\d+(?:_\d+)?).*', file)
            form_id = f"PMO-{id_match.group(1).replace('_', '.')}" if id_match else None
            
            # Language
            lang = "en" if "/en/" in filepath else ("ar" if "/ar/" in filepath else None)
            
            changed = False
            
            # We must be idempotent.
            if form_id and "form_id:" not in frontmatter:
                # Some files might have missing form_id, wait, the profile says Templates and Forms need form_id.
                type_match = re.search(r'^type:\s*(.+)$', frontmatter, re.MULTILINE)
                type_val = type_match.group(1).strip() if type_match else ""
                
                if 'Template' in type_val or 'Form' in type_val or 'قالب' in type_val or 'نموذج' in type_val:
                    frontmatter += f"\nform_id: {form_id}"
                    changed = True
                elif 'Guide' in type_val or 'دليل' in type_val:
                    # Guides also share the same form_id
                    frontmatter += f"\nform_id: {form_id}"
                    changed = True
                    
            if lang and "language:" not in frontmatter and "lang:" not in frontmatter:
                frontmatter += f"\nlanguage: {lang}"
                changed = True
                
            if "status:" not in frontmatter and file != 'index.md' and file != 'README.md':
                frontmatter += f"\nstatus: approved"
                changed = True
                
            if changed:
                # Clean up double newlines
                frontmatter = re.sub(r'\n\n+', '\n', frontmatter)
                new_content = f"<!--
---{frontmatter}
---
-->{body}" if content.startswith('<!--
---') else f"---{frontmatter}
---{body}" 
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                processed += 1

    print(f"Migration completed. Processed/Updated {processed} files.")

if __name__ == '__main__':
    migrate()
