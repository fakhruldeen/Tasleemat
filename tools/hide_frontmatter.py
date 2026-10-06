#!/usr/bin/env python3
import os

def hide_frontmatter():
    processed = 0
    
    for root_dir, dirs, files in os.walk('forms'):
        for file in files:
            if not file.endswith('.md'):
                continue
                
            # Target _Template.md, _قالب.md, and README.md
            if not ('_Template' in file or '_قالب' in file or file == 'README.md'):
                continue
                
            filepath = os.path.join(root_dir, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if content.startswith('<!--\n---'):
                continue
                
            if not content.startswith('---'):
                continue
                
            end_idx = content.find('\n---', 3)
            if end_idx == -1:
                continue
                
            frontmatter_block = content[0:end_idx+4]
            body = content[end_idx+4:]
            
            new_content = f"<!--\n{frontmatter_block}\n-->{body}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            processed += 1
            
    print(f"Hid frontmatter in {processed} files.")

if __name__ == '__main__':
    hide_frontmatter()
