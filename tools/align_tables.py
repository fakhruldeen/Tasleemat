#!/usr/bin/env python3
"""align_tables.py
Sanitizes and formats Markdown table alignments across English (and Arabic) templates,
examples, guides, and documentation.
Aligns columns semantically based on content and visual design:
  - IDs, Codes, Status, Priority, Dates, Version, Sprints, Signatures -> Centered (:---:)
  - Financial, Costs, Budgets, Story Points, Quantities, Variances, Scores -> Right-aligned (---:)
  - Text, Descriptions, Names, Roles, Actions, Deliverables, Notes -> Left-aligned (:---)
"""

import os
import glob
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

def determine_alignment_en(col_name: str) -> str:
    clean = col_name.strip()
    clean = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', clean)
    clean = re.sub(r'[*_`]', '', clean).strip()
    low = clean.lower()

    if not low:
        return ':---'

    # 1. Numeric / Financial / Quantitative -> Right-aligned (---:)
    numeric_exact = {
        'budget', 'costs', 'cost', 'planned funding', 'price', 'npv', 'net present value', 
        'roi', 'rate', 'contingency amount', 'baseline value', 'target value', 
        'actual value', 'variance', 'gap', 'total available', 'allocated', 'remaining', 
        'committed load', 'available', 'required capacity', 'hours', 'story points', 
        'target score', 'actual score', 'weight', 'points', '%', 'amount', 'net value',
        'funding', 'planned capacity', 'estimate', 'estimated cost', 'actual cost',
        'cost variance', 'schedule variance', 'cpi', 'spi', 'ev', 'pv', 'ac', 'bac', 'eac', 'etc',
        'planned budget', 'actual budget', 'variance ($)', 'variance (%)', 'actual cost ($)',
        'estimated cost ($)', 'total cost', 'unit cost', 'hourly rate', 'daily rate'
    }
    if low in numeric_exact:
        return '---:'
    if any(low.endswith(sfx) for sfx in [' ($)', ' (%)', ' (hrs)', ' (hours)', ' (days)', ' (points)', ' (sar)', ' (usd)', ' (eur)', ' (gbp)']):
        return '---:'
    if any(k in low for k in ['budget', 'planned funding', 'net present value', 'contingency amount', 'total available', 'allocated', 'remaining', 'committed load']):
        return '---:'

    # 2. Identifiers, Codes, Status, Priority, Dates, Version, Sprints, Signatures -> Centered (:---:)
    center_exact = {
        'id', 'doc id', 'change id', 'component id', 'benefit id', 'dependency id', 
        'req id', 'requirement id', 'risk id', 'issue id', 'action id', 'defect id',
        'item #', 'ref #', 'step #', 'no.', '#', 'code', 'guide #', 'template #', 'example #',
        'status', 'sprint status', 'sign-off status', 'status at closure', 'approval status',
        'priority', 'severity', 'rag', 'tier', 'level', 'phase', 'sprint', 'release', 
        'iteration', 'version', 'signature', 'by when', 'date', 'dates', 'start date', 
        'end date', 'target date', 'review date', 'agreed date', 'resolution date', 
        'realization date', 'handover date', 'date approved', 'date resolved', 'start', 'end',
        'period', 'frequency', 'criticality', 'probability', 'impact score', 'raci',
        'language', 'target sprint or release'
    }
    if low in center_exact:
        return ':---:'
    if low.endswith(' id') or low.startswith('id ') or low.endswith(' status') or low.endswith(' date') or low.startswith('date '):
        return ':---:'
    if low in ['start', 'end'] and ('start date' in low or 'end date' in low or low == 'start' or low == 'end'):
        return ':---:'

    # 3. Default text / descriptions / narrative -> Left-aligned (:---)
    return ':---'

def align_table_in_text(text: str, is_arabic: bool = False) -> str:
    lines = text.splitlines(keepends=True)
    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        line_s = line.strip()
        
        # Check if this line is a table separator line
        if line_s.startswith('|') and ('---' in line_s) and i > 0:
            prev_line = lines[i-1].strip()
            # Verify previous line is table header
            if prev_line.startswith('|') and not ('---' in prev_line and prev_line.count('|') == line_s.count('|')):
                # Check if it is a metadata table like | **Date:** ... |
                if '{{' in prev_line or 'Date Prepared:' in prev_line or 'تاريخ الإعداد:' in prev_line:
                    new_lines.append(line)
                    i += 1
                    continue
                
                # Split header columns
                header_cols = [c.strip() for c in prev_line.strip('|').split('|')]
                sep_cols = [c.strip() for c in line_s.strip('|').split('|')]
                
                if len(header_cols) == len(sep_cols) and len(header_cols) > 0:
                    if is_arabic:
                        # In Arabic, default is right-aligned text, but numbers/dates/IDs can be centered
                        # We preserve or ensure proper RTL format
                        new_lines.append(line)
                        i += 1
                        continue
                    else:
                        new_alignments = [determine_alignment_en(col) for col in header_cols]
                        new_sep = '| ' + ' | '.join(new_alignments) + ' |\n'
                        indent = len(line) - len(line.lstrip())
                        new_lines.append(' ' * indent + new_sep)
                        i += 1
                        continue

        new_lines.append(line)
        i += 1
        
    return ''.join(new_lines)

def process_directory(dir_path: pathlib.Path, is_arabic: bool = False):
    count = 0
    for md_file in dir_path.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        updated = align_table_in_text(content, is_arabic=is_arabic)
        if updated != content:
            md_file.write_text(updated, encoding="utf-8")
            count += 1
    return count

def main():
    print("Aligning tables in English forms, examples, guides, and documentation...")
    en_forms = process_directory(ROOT / "forms" / "en")
    en_examples = process_directory(ROOT / "examples" / "en")
    en_guides = process_directory(ROOT / "guides" / "en") if (ROOT / "guides" / "en").exists() else 0
    docs_en = process_directory(ROOT / "docs" / "forms" / "en")
    docs_ex_en = process_directory(ROOT / "docs" / "examples" / "en")
    docs_guides_en = process_directory(ROOT / "docs" / "guides" / "en")
    
    print(f"Updated tables in:")
    print(f"  - forms/en: {en_forms} files")
    print(f"  - examples/en: {en_examples} files")
    print(f"  - docs/forms/en: {docs_en} files")
    print(f"  - docs/examples/en: {docs_ex_en} files")
    print(f"  - docs/guides/en: {docs_guides_en} files")

if __name__ == "__main__":
    main()
