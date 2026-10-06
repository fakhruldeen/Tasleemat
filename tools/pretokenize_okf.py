#!/usr/bin/env python3
import os
import re
import datetime
import tiktoken
import numpy as np

def main():
    tokenizer = tiktoken.get_encoding("o200k_base")
    model_id = "tiktoken/o200k_base"
    
    tokens_dir = "_tokens"
    os.makedirs(tokens_dir, exist_ok=True)
    
    for root_dir, _, files in os.walk('.'):
        skip = False
        for part in root_dir.split(os.sep):
            if part != '.' and part.startswith('.'):
                skip = True
            if part in ['scratch', '_tokens']:
                skip = True
        if skip:
            continue
            
        for file in files:
            if not file.endswith('.md') or file == 'log.md':
                continue
                
            filepath = os.path.join(root_dir, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            if not content.startswith('---'):
                continue
                
            end_idx = content.find('\n---', 3)
            if end_idx == -1:
                continue
                
            frontmatter = content[3:end_idx]
            body = content[end_idx+4:]
            
            # Tokenize body
            tokens = tokenizer.encode(body)
            tokens_array = np.array(tokens, dtype=np.int32)
            
            # Save to .npy
            rel_path = os.path.relpath(filepath, '.')
            npy_rel_path = os.path.splitext(rel_path)[0] + '.npy'
            npy_abs_path = os.path.join(tokens_dir, npy_rel_path)
            
            os.makedirs(os.path.dirname(npy_abs_path), exist_ok=True)
            np.save(npy_abs_path, tokens_array)
            
            # Update frontmatter
            if 'token_pointer:' in frontmatter:
                # Remove existing token metadata to replace it
                frontmatter = re.sub(r'\ntoken_pointer:.*', '', frontmatter)
                frontmatter = re.sub(r'\ntoken_count:.*', '', frontmatter)
                frontmatter = re.sub(r'\ntokenizer_model_id:.*', '', frontmatter)
                frontmatter = re.sub(r'\ncreated_at:.*', '', frontmatter)
                
            timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
            pointer = f"/{tokens_dir}/{npy_rel_path}"
            
            # Add to frontmatter
            new_meta = f"\ntoken_pointer: {pointer}\ntoken_count: {len(tokens)}\ntokenizer_model_id: {model_id}\ncreated_at: '{timestamp}'"
            new_content = f"---{frontmatter}{new_meta}\n---{body}"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
    print(f"Pre-tokenization complete. Saved tokens to {tokens_dir}/")

if __name__ == '__main__':
    main()
