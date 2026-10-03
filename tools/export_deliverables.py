#!/usr/bin/env python3
"""Tasleemat Batch Deliverable Exporter
Converts Markdown deliverables and full project workspaces into
print-ready, styled HTML / PDF-ready documents with full Arabic RTL support.
"""

import os
import sys
import pathlib
import argparse
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang}" dir="{direction}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary-color: #0b2545;
      --accent-color: #134074;
      --border-color: #cbd5e1;
      --bg-header: #f8fafc;
      --text-main: #1e293b;
      --text-muted: #64748b;
    }}
    
    body {{
      font-family: {font_family};
      color: var(--text-main);
      line-height: 1.6;
      margin: 0;
      padding: 40px;
      background-color: #ffffff;
    }}

    @page {{
      size: A4;
      margin: 20mm;
    }}

    .container {{
      max-width: 900px;
      margin: 0 auto;
    }}

    .doc-header {{
      border-bottom: 2px solid var(--accent-color);
      padding-bottom: 20px;
      margin-bottom: 30px;
    }}

    h1, h2, h3, h4 {{
      color: var(--primary-color);
      font-weight: 700;
    }}

    h1 {{
      font-size: 26px;
      margin-top: 0;
      text-align: center;
    }}

    h2 {{
      font-size: 19px;
      margin-top: 30px;
      border-bottom: 1px solid var(--border-color);
      padding-bottom: 6px;
    }}

    h3 {{
      font-size: 15px;
      margin-top: 20px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
      font-size: 13px;
    }}

    th, td {{
      border: 1px solid var(--border-color);
      padding: 9px 12px;
      text-align: {align};
    }}

    th {{
      background-color: var(--bg-header);
      font-weight: 600;
      color: var(--primary-color);
    }}

    blockquote {{
      background-color: #f1f5f9;
      border-{border_side}: 4px solid var(--accent-color);
      margin: 15px 0;
      padding: 12px 18px;
      border-radius: 4px;
      font-size: 14px;
    }}

    hr {{
      border: 0;
      border-top: 1px solid var(--border-color);
      margin: 30px 0;
    }}

    .print-footer {{
      margin-top: 50px;
      text-align: center;
      font-size: 11px;
      color: var(--text-muted);
      border-top: 1px solid var(--border-color);
      padding-top: 15px;
    }}

    @media print {{
      body {{
        padding: 0;
      }}
      .no-print {{
        display: none;
      }}
    }}
  </style>
</head>
<body>
  <div class="container">
    {content}
    <div class="print-footer">
      Tasleemat PMO Operating System • Generated on {date} • Standard PMI PMBOK® Alignment
    </div>
  </div>
</body>
</html>
"""

def simple_markdown_to_html(md_text):
    """Clean, robust Markdown to HTML parser for tables, headers, and text."""
    # Remove LLM instruction comments
    md_text = re.sub(r'<!--[\s\S]*?-->', '', md_text)
    
    # Process tables
    lines = md_text.split('\n')
    in_table = False
    table_lines = []
    output_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('|') and stripped.endswith('|'):
            in_table = True
            table_lines.append(stripped)
        else:
            if in_table:
                # Render table
                output_lines.append(render_table(table_lines))
                table_lines = []
                in_table = False
            output_lines.append(line)
            
    if in_table:
        output_lines.append(render_table(table_lines))
        
    html = '\n'.join(output_lines)
    
    # Headers
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.M)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.M)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.M)
    
    # Bold / Italic
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # Blockquotes
    html = re.sub(r'^> (.*?)$', r'<blockquote>\1</blockquote>', html, flags=re.M)
    
    # Horizontal Rule
    html = re.sub(r'^---$', r'<hr/>', html, flags=re.M)
    
    # Paragraphs (simple)
    paragraphs = []
    for block in html.split('\n\n'):
        block = block.strip()
        if not block:
            continue
        if block.startswith('<h') or block.startswith('<table') or block.startswith('<blockquote') or block.startswith('<hr') or block.startswith('<div'):
            paragraphs.append(block)
        else:
            # line breaks
            block_with_br = block.replace('\n', '<br/>')
            paragraphs.append(f'<p>{block_with_br}</p>')
            
    return '\n'.join(paragraphs)

def render_table(table_lines):
    if not table_lines:
        return ""
    
    rows = []
    for l in table_lines:
        cells = [c.strip() for c in l.strip('|').split('|')]
        rows.append(cells)
        
    if len(rows) < 2:
        return ""
        
    header_row = rows[0]
    # Check if row 1 is separator
    is_sep = all(re.match(r'^:?-+:?$', c) for c in rows[1])
    data_rows = rows[2:] if is_sep else rows[1:]
    
    html = '<table>\n<thead>\n<tr>\n'
    for c in header_row:
        html += f'  <th>{c}</th>\n'
    html += '</tr>\n</thead>\n<tbody>\n'
    
    for r in data_rows:
        html += '<tr>\n'
        for c in r:
            html += f'  <td>{c}</td>\n'
        html += '</tr>\n'
    html += '</tbody>\n</table>'
    return html

def export_file(file_path, out_path=None):
    p = pathlib.Path(file_path).resolve()
    if not p.exists():
        print(f"Error: File not found: {p}")
        return
        
    is_ar = "_ar" in p.name.lower() or "ar/" in str(p) or "arabic" in str(p).lower()
    lang = "ar" if is_ar else "en"
    direction = "rtl" if is_ar else "ltr"
    align = "right" if is_ar else "left"
    border_side = "right" if is_ar else "left"
    font_family = "'Cairo', sans-serif" if is_ar else "'Inter', sans-serif"
    
    raw_md = p.read_text(encoding="utf-8")
    body_html = simple_markdown_to_html(raw_md)
    
    import datetime
    full_html = HTML_TEMPLATE.format(
        title=p.stem,
        lang=lang,
        direction=direction,
        font_family=font_family,
        align=align,
        border_side=border_side,
        content=body_html,
        date=datetime.date.today().isoformat()
    )
    
    if out_path is None:
        out_path = p.with_suffix('.html')
    else:
        out_path = pathlib.Path(out_path).resolve()
        
    out_path.write_text(full_html, encoding="utf-8")
    print(f"✅ Exported: {p.name} -> {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Tasleemat Deliverable Batch Exporter")
    parser.add_argument("input", help="Path to markdown file or directory to export")
    parser.add_argument("-o", "--output", help="Output file or directory")
    args = parser.parse_args()
    
    in_path = pathlib.Path(args.input).resolve()
    if in_path.is_file():
        export_file(in_path, args.output)
    elif in_path.is_dir():
        for md_file in in_path.rglob("*.md"):
            export_file(md_file)

if __name__ == "__main__":
    main()
