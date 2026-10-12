"""
Tasleemat Artifact Rendering Engine
Converts Markdown templates and artifacts into styled, print-ready HTML documents.
Guarantees rendered files are never written into forms/.
"""

from __future__ import annotations

import datetime
import pathlib
import re
from typing import Any, Dict, Optional

from tasleemat.catalog import get_artifact_assets

PACKAGE_DIR = pathlib.Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_DIR.parent
FORMS_DIR = (REPO_ROOT / "forms").resolve()

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


def _render_table(table_lines: list[str]) -> str:
    if not table_lines:
        return ""
    rows = []
    for line in table_lines:
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return ""
    header_row = rows[0]
    is_sep = all(re.match(r"^:?-+:?$", c) for c in rows[1])
    data_rows = rows[2:] if is_sep else rows[1:]

    html = "<table>\n<thead>\n<tr>\n"
    for c in header_row:
        html += f"  <th>{c}</th>\n"
    html += "</tr>\n</thead>\n<tbody>\n"
    for r in data_rows:
        html += "<tr>\n"
        for c in r:
            html += f"  <td>{c}</td>\n"
        html += "</tr>\n"
    html += "</tbody>\n</table>"
    return html


def markdown_to_html(md_text: str) -> str:
    """Robust Markdown to HTML converter supporting tables, headers, and RTL text."""
    # Strip comments
    md_text = re.sub(r"<!--[\s\S]*?-->", "", md_text)

    lines = md_text.split("\n")
    in_table = False
    table_lines: list[str] = []
    output_lines: list[str] = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|"):
            in_table = True
            table_lines.append(stripped)
        else:
            if in_table:
                output_lines.append(_render_table(table_lines))
                table_lines = []
                in_table = False
            output_lines.append(line)

    if in_table:
        output_lines.append(_render_table(table_lines))

    html = "\n".join(output_lines)

    html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", html, flags=re.M)
    html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", html, flags=re.M)
    html = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", html, flags=re.M)
    html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", html)
    html = re.sub(r"\*(.*?)\*", r"<em>\1</em>", html)
    html = re.sub(r"^> (.*?)$", r"<blockquote>\1</blockquote>", html, flags=re.M)
    html = re.sub(r"^---$", r"<hr/>", html, flags=re.M)

    paragraphs = []
    for block in html.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        if any(block.startswith(t) for t in ("<h", "<table", "<blockquote", "<hr", "<div")):
            paragraphs.append(block)
        else:
            block_with_br = block.replace("\n", "<br/>")
            paragraphs.append(f"<p>{block_with_br}</p>")

    return "\n".join(paragraphs)


def render_artifact(
    artifact_id: str,
    lang: str = "en",
    data: Optional[Dict[str, Any]] = None,
    out_path: Optional[str | pathlib.Path] = None,
) -> str:
    """
    Render an artifact template to styled HTML.

    Parameters:
        artifact_id: PMO code (e.g. "PMO-03.01")
        lang: "en" or "ar"
        data: Optional parameter substitution dictionary
        out_path: Optional target file path (MUST be outside forms/)

    Returns:
        Rendered HTML string.
    """
    norm_lang = lang.lower().strip()
    is_ar = norm_lang == "ar"
    assets = get_artifact_assets(artifact_id, lang=norm_lang)
    raw_md = assets.get_template_content()

    if data:
        for k, v in data.items():
            raw_md = raw_md.replace(f"{{{{{k}}}}}", str(v))
            raw_md = raw_md.replace(f"[{k}]", str(v))

    body_html = markdown_to_html(raw_md)

    full_html = HTML_TEMPLATE.format(
        title=f"{artifact_id} - {lang.upper()}",
        lang=norm_lang,
        direction="rtl" if is_ar else "ltr",
        font_family="'Cairo', sans-serif" if is_ar else "'Inter', sans-serif",
        align="right" if is_ar else "left",
        border_side="right" if is_ar else "left",
        content=body_html,
        date=datetime.date.today().isoformat(),
    )

    if out_path:
        target = pathlib.Path(out_path).resolve()
        # Strictly verify that out_path is NOT within forms/ or package directory
        prohibited_dirs = [FORMS_DIR, PACKAGE_DIR]
        for pdir in prohibited_dirs:
            if pdir.exists() and (target == pdir or pdir in target.parents):
                raise ValueError(
                    f"Prohibited output path: '{target}' is inside protected directory '{pdir.name}'. "
                    f"Rendered outputs must be written outside package sources and forms/."
                )
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(full_html, encoding="utf-8")

    return full_html
