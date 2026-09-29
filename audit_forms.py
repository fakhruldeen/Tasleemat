#!/usr/bin/env python3
"""Offline structural audit for the bilingual form set in forms/ and forms/ar/.

Complements check_rendering.py, which only guards against the GitHub
invisible-header bug. This script checks the project conventions that keep a
form's five files synchronised with each other and satisfying the language
rules.

Design rule, learned the hard way this session: a clean run from a newly
written checker is not evidence until the checker has been negative-tested
against a known-bad input. Run --selftest to do that.

Usage:
    python3 audit_forms.py            # audit every form
    python3 audit_forms.py 05_08      # audit only forms matching a substring
    python3 audit_forms.py --selftest # prove each check fires on bad input
    python3 audit_forms.py --report   # print findings but always exit 0
"""

from __future__ import annotations

import csv
import io
import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent
FORMS = ROOT / "forms"

CSV_HEADER = ["Section", "Field", "Guidance", "LLM_Generated_Value"]
JSON_PROPS = ("section", "label", "guidance", "value")
# Shortest guidance considered real content. The reference form's thinnest
# guidance is "The date the retrospective was held." at 35 characters, which is
# a complete and adequate sentence for a Date column, so the floor sits below it.
MIN_GUIDANCE = 25

# Latin tokens that legitimately appear inside Arabic files: real acronyms,
# the project and document-reference vocabulary, and words that are proper
# nouns in context rather than untranslated prose.
ACRONYMS = {
    "FLAP", "AI", "SWOT", "RACI", "RBS", "WBS", "EVA", "PID", "SOW", "RFP",
    "UAT", "KPI", "MOU", "SLA", "SMART", "PDCA", "OHS", "PMP", "ML", "API",
    "SaaS", "PRINCE2", "TPS", "MoSCoW", "PII", "GDPR", "LLM", "NLP",
    "PMBOK", "PMO", "Tasleemat", "Arial", "HTML", "PDF", "CSV", "JSON",
    "md", "csv", "json", "ar", "en", "lang", "default", "true", "false",
    "Fill", "Field", "Section", "Guidance", "Value", "Generated", "Reference",
    "and", "based", "align", "datetime", "iso", "utf",
}
# Filename components such as (Product_Backlog) are carried across verbatim.
FILENAME_COMPONENT = re.compile(r"\(([A-Za-z0-9_.\- ]+)\)")
# A Latin token that is part of a filename or a path, e.g. parameters.md.
PATH_LIKE = re.compile(r"[A-Za-z0-9_.\-]*\.(?:md|csv|json|pdf|html)\b")
# An identifier such as TR-114 or PO-0097: a code, not prose. Coded references
# are quoted inside an example sentence and stay in their original form.
CODE_TOKEN = re.compile(r"\b[A-Z]{2,}[-_/]?\d{2,}\b")
# The house style glosses a translated term with its English original in
# parentheses, e.g. مرحلة المراقبة والتحكم (Monitoring & Controlling Process
# Group) and **Generated value:**. The gloss is deliberate, not untranslated.
PAREN_GLOSS = re.compile(r"\([^()]*\)")
BOLD_LABEL = re.compile(r"\*\*[^*]*:\*\*")

CJK = re.compile(
    "[\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\u3400-\u4dbf"
    "\u4e00-\u9fff\uf900-\ufaff\uff00-\uffef]"
)
ARABIC = re.compile(r"[\u0600-\u06ff\ufb50-\ufdff\ufe70-\ufeff]")
LATIN_LETTER = re.compile(r"[A-Za-z]")
COMMENT_OPEN = re.compile(r"<!--")
COMMENT_CLOSE = re.compile(r"-->")
# Markdown link target, tolerant of one level of balanced parentheses so that
# filenames like (Issue_Log.md) are not truncated.
MD_LINK = re.compile(r"\]\(((?:[^()]|\([^()]*\))+)\)")


def is_rtl(name: str) -> bool:
    return ARABIC.search(name) is not None


# --------------------------------------------------------------------------
# loading
# --------------------------------------------------------------------------

def load_form(folder: pathlib.Path) -> dict:
    files = sorted(p.name for p in folder.iterdir() if p.is_file())
    guide = next((f for f in files
                  if f.endswith("_Guide.md") or f.endswith("_دليل.md")), None)
    template = next((f for f in files
                     if f.endswith("_Template.md") or f.endswith("_قالب.md")),
                    None)
    kind = {
        "template": template,
        "prompt": next((f for f in files
                        if f.endswith(".md")
                        and f != template
                        and f != guide), None),
        "guide": guide,
        "json": next((f for f in files if f.endswith(".json")), None),
        "csv": next((f for f in files if f.endswith(".csv")), None),
    }
    form = {"dir": folder, "rtl": is_rtl(folder.name), "kind": kind}
    for role, name in kind.items():
        if name:
            form[role + "_text"] = (folder / name).read_text(encoding="utf-8")
    return form


def is_form_dir(folder: pathlib.Path) -> bool:
    """A form folder holds at least one recognised artifact file.

    Group landing pages and intermediate sub-group folders hold only index.md,
    or nothing at all, and are not forms.
    """
    for p in folder.iterdir():
        if p.is_file() and p.suffix in (".json", ".csv"):
            return True
        if p.is_file() and p.suffix == ".md" and p.name != "index.md":
            return True
    return False


def load_all_forms() -> list[dict]:
    """Every per-form directory in forms/ and forms/ar/.

    The walk is recursive because planning sub-groups nest form folders one
    level deeper, e.g. forms/04_Planning/02_Scope/08_Product_Backlog. The
    Arabic tree is reached only through its own base, so it is not visited
    twice as a group of the English tree.
    """
    forms = []
    for base in (FORMS, FORMS / "ar"):
        if not base.is_dir():
            continue
        for group in sorted(base.iterdir()):
            if not group.is_dir() or (base is FORMS and group.name == "ar"):
                continue
            for folder in sorted(p for p in group.rglob("*") if p.is_dir()):
                if is_form_dir(folder):
                    forms.append(load_form(folder))
    return forms


def rel(form: dict) -> str:
    return str(form["dir"].relative_to(ROOT))


# --------------------------------------------------------------------------
# text helpers
# --------------------------------------------------------------------------

def strip_comments(text: str) -> str:
    return COMMENT_OPEN.sub("", COMMENT_CLOSE.sub("", text))


def heading_titles(text: str) -> list[str]:
    """Titles of level-1 and level-2 headings, in document order."""
    titles = []
    in_fence = False
    for line in strip_comments(text).splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = re.match(r"^(#{1,2})\s+(.*?)\s*$", line)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            if title:
                titles.append(title)
    return titles


def normalise(text: str) -> str:
    """Fold case, strip bidi marks and collapse whitespace for comparison."""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"[\u200e\u200f\u202a-\u202e\u2066-\u2069]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def strip_front_matter(text: str) -> str:
    """Remove a leading Jekyll YAML front-matter block."""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end != -1 else text


def strip_code_fences(text: str) -> str:
    """Remove fenced code blocks, whose content is often copied verbatim."""
    out, in_fence = [], False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def latin_tokens(text: str) -> list[str]:
    """Latin words in text that indicate untranslated prose.

    Front matter, fenced code, filename components, paths, coded identifiers,
    parenthetical English glosses and bold field labels are removed first, then
    known acronyms and schema vocabulary are dropped. Jekyll front matter carries
    fixed configuration keys (lang, layout, nav_order) that are never translated,
    a reference such as TR-114 is an identifier rather than prose, and the house
    style deliberately glosses a translated term with its English original.
    """
    cleaned = strip_front_matter(text)
    cleaned = strip_code_fences(cleaned)
    cleaned = FILENAME_COMPONENT.sub(" ", cleaned)
    cleaned = PATH_LIKE.sub(" ", cleaned)
    cleaned = CODE_TOKEN.sub(" ", cleaned)
    cleaned = PAREN_GLOSS.sub(" ", cleaned)
    cleaned = BOLD_LABEL.sub(" ", cleaned)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    return [t for t in re.findall(r"[A-Za-z]{2,}", cleaned)
            if t.upper() not in ACRONYMS]


# --------------------------------------------------------------------------
# checks
# --------------------------------------------------------------------------

def check_files(form: dict, bad: list) -> None:
    missing = [r for r, n in form["kind"].items() if not n]
    if missing:
        bad.append(f"missing file(s): {', '.join(missing)}")


def check_json(form: dict, bad: list) -> None:
    if not form["kind"]["json"]:
        return
    try:
        data = json.loads(form["json_text"])
    except json.JSONDecodeError as exc:
        bad.append(f"JSON does not parse: {exc}")
        return
    fields = data.get("fields")
    if not isinstance(fields, dict) or not fields:
        bad.append("JSON has no non-empty 'fields' object")
        return
    for key, spec in fields.items():
        if not isinstance(spec, dict):
            bad.append(f"JSON field {key} is not an object")
            continue
        for prop in JSON_PROPS:
            if prop not in spec:
                bad.append(f"JSON field {key} missing '{prop}'")
        for prop in ("label", "guidance", "value"):
            val = spec.get(prop)
            if isinstance(val, list):
                bad.append(
                    f"JSON field {key}.{prop} uses the list-value anti-pattern")
        guidance = spec.get("guidance")
        if isinstance(guidance, str) and len(guidance.strip()) < MIN_GUIDANCE:
            bad.append(f"JSON field {key}.guidance is too thin "
                       f"(<{MIN_GUIDANCE} chars)")


def check_csv(form: dict, bad: list) -> None:
    if not form["kind"]["csv"]:
        return
    rows = list(csv.reader(io.StringIO(form["csv_text"])))
    if not rows:
        bad.append("CSV is empty")
        return
    if rows[0] != CSV_HEADER:
        bad.append(f"CSV header is {rows[0]}, expected {CSV_HEADER}")
    for n, row in enumerate(rows[1:], start=2):
        if len(row) != 4:
            bad.append(f"CSV line {n} has {len(row)} columns, expected 4")
        elif len(row[2].strip()) < MIN_GUIDANCE:
            bad.append(f"CSV line {n} guidance is too thin "
                       f"(<{MIN_GUIDANCE} chars)")


def json_pairs(form: dict):
    if not form["kind"]["json"]:
        return None
    try:
        data = json.loads(form["json_text"])
    except json.JSONDecodeError:
        return None
    fields = data.get("fields")
    if not isinstance(fields, dict):
        return None
    return [(s.get("section", ""), s.get("label", ""))
            for s in fields.values() if isinstance(s, dict)]


def csv_pairs(form: dict):
    if not form["kind"]["csv"]:
        return None
    rows = list(csv.reader(io.StringIO(form["csv_text"])))
    if not rows or rows[0] != CSV_HEADER or len(rows) < 2:
        return None
    return [(r[0], r[1]) for r in rows[1:] if len(r) >= 2]


def check_agreement(form: dict, bad: list) -> None:
    """JSON and CSV must list the same (section, field) pairs, in the same order."""
    jp, cp = json_pairs(form), csv_pairs(form)
    if jp is None or cp is None:
        return  # schema error already reported by check_json / check_csv
    if jp == cp:
        return
    only_json = [f"{s}/{l}" for s, l in jp if (s, l) not in cp]
    only_csv = [f"{s}/{l}" for s, l in cp if (s, l) not in jp]
    detail = []
    if only_json:
        detail.append(f"only in JSON: {only_json[:3]}")
    if only_csv:
        detail.append(f"only in CSV: {only_csv[:3]}")
    if not detail:
        detail.append("same pairs, different order")
    bad.append(f"JSON/CSV disagree ({'; '.join(detail)})")


def check_sections_in_template(form: dict, bad: list) -> None:
    """Every JSON section must correspond to a real heading in the template."""
    jp = json_pairs(form)
    if jp is None or not form["kind"]["template"]:
        return
    titles = normalise(" | ".join(heading_titles(form["template_text"])))
    for section in dict.fromkeys(s for s, _ in jp):
        if not section:
            continue
        core = re.sub(r"^\d+[.)]\s*", "", section).strip()
        if normalise(core) and normalise(core) in titles:
            continue
        bad.append(f"JSON section {section!r} has no matching template heading")


def check_labels_present(form: dict, bad: list) -> None:
    """Every JSON field label must appear in both the template and the prompt.

    A matrix row is addressed by a composite label such as "Scope / Objectives",
    which names a row heading and a column heading that appear separately in
    the template. Each part is therefore checked on its own.
    """
    jp = json_pairs(form)
    if jp is None:
        return
    blob_t = normalise(form.get("template_text", ""))
    blob_p = normalise(form.get("prompt_text", ""))
    for _, label in jp:
        if not label:
            continue
        parts = [p for p in re.split(r"\s+/\s+", label) if p.strip()]
        for part in parts:
            n = normalise(re.sub(r"<[^>]+>", "", part))
            if not n:
                continue
            if n not in blob_t:
                bad.append(f"label {part.strip()!r} not found in template")
            if n not in blob_p:
                bad.append(f"label {part.strip()!r} not found in LLM prompt")


def check_comments_balanced(form: dict, bad: list) -> None:
    for role in ("template", "prompt", "guide"):
        if not form["kind"][role]:
            continue
        text = form[role + "_text"]
        if len(COMMENT_OPEN.findall(text)) != len(COMMENT_CLOSE.findall(text)):
            bad.append(f"unbalanced HTML comments in {form['kind'][role]}")


def check_no_visible_instructions(form: dict, bad: list) -> None:
    """Instructional blockquotes must not be visible in a printable template.

    One exception is deliberate and pre-existing: the Team Performance
    Assessment carries a "Rating Legend" that decodes the [X]/[M]/[N] codes
    used in the form body. A decoding key the form cannot be read without is
    content, not an instruction, and is documented in that form's JSON and
    prompt. Anything else beginning with > is an instruction and must move
    into an HTML comment.
    """
    if not form["kind"]["template"]:
        return
    in_fence = False
    legend_allowed = "Rating Legend" in form["template_text"] or \
        "مفتاح التقييم" in form["template_text"]
    for n, line in enumerate(form["template_text"].splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not re.match(r"^\s*>\s", line):
            continue
        if legend_allowed and re.search(
                r"Rating Legend|مفتاح التقييم|Exceeds Expectations|"
                r"Needs Improvement|يتجاوز التوقعات|بحاجة إلى تحسين",
                line):
            continue
        bad.append(f"visible blockquote instruction at template line {n}")


def check_table_split(form: dict, bad: list) -> None:
    """A blank line between a table's separator row and its data rows splits it.

    This produced a table with a single rowgroup that every structural count
    still accepted; it was only visible in the rendered Arabic.

    The row above the separator must itself be a table row, otherwise the
    separator is a stray horizontal rule. And the next non-blank line must be
    a table row too, otherwise the table simply ends and the blank line that
    follows it is correct.
    """
    for role in ("template", "guide", "prompt"):
        if not form["kind"][role]:
            continue
        lines = form[role + "_text"].splitlines()
        for n, sep in enumerate(lines):
            sep = sep.strip()
            if not (sep.startswith("|")
                    and re.fullmatch(r"\|?[\s:\-|]+\|[\s:\-|]*", sep)):
                continue
            if n == 0 or not lines[n - 1].strip().startswith("|"):
                continue  # not a table separator
            nxt = next((ln.strip() for ln in lines[n + 1:]
                        if ln.strip()), "")
            if nxt == "":
                continue  # table ends here; a blank line is correct
            if not nxt.startswith("|"):
                continue  # followed by prose, not a stranded data row
            if lines[n + 1].strip() == "":
                bad.append(f"blank line between table separator and its data "
                           f"rows in {form['kind'][role]} line {n + 1}")


def check_cjk(form: dict, bad: list) -> None:
    for role in ("template", "prompt", "guide", "json", "csv"):
        if not form["kind"][role]:
            continue
        text = form[role + "_text"]
        hit = CJK.search(text)
        if hit:
            line = text[:hit.start()].count("\n") + 1
            bad.append(f"CJK character {hit.group()!r} in {form['kind'][role]} "
                       f"line {line}")


def check_script_purity(form: dict, bad: list) -> None:
    """No Arabic in an English file; no stray Latin in an Arabic file.

    The Latin scan covers only the prose a reader sees: template, prompt and
    guide. JSON and CSV carry fixed English schema keys, the literal
    parameters.md, and document references, so a Latin word there is expected
    and says nothing about translation quality.
    """
    for role in ("template", "prompt", "guide", "json", "csv"):
        if not form["kind"][role]:
            continue
        name = form["kind"][role]
        text = form[role + "_text"]
        if form["rtl"]:
            if role in ("json", "csv"):
                continue
            offenders = latin_tokens(strip_comments(text))
            if offenders:
                bad.append(f"untranslated Latin "
                           f"{sorted(set(offenders))[:5]} in {name}")
        else:
            body = strip_comments(text)
            hit = ARABIC.search(body)
            if hit:
                line = body[:hit.start()].count("\n") + 1
                bad.append(f"Arabic text in English file {name} line {line}")


def check_guide_links(form: dict, bad: list) -> None:
    if not form["kind"]["guide"]:
        return
    base = form["dir"]
    for n, line in enumerate(form["guide_text"].splitlines(), start=1):
        for target in MD_LINK.findall(line):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path_part = target.split("#", 1)[0]
            if path_part and not (base / path_part).exists():
                bad.append(f"broken guide link {target!r} (guide line {n})")


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------

def check_missing_word(form: dict, bad: list) -> None:
    """Two spaces between Arabic letters, on one line, with no indentation.

    A single word lost during Arabic generation leaves the two spaces that
    marked its place behind, so the sentence still parses as Arabic and no
    other check sees it. This happened twice: "بعد سنوات  شخص" in the Program
    Charter and "بديل  لنفس" in the Product Vision.

    Wrapped list items and continuation lines are indented, so a run of
    spaces that reaches the start of a line is layout rather than a gap.
    """
    run = re.compile(r"[؀-ۿ][ \t]{2,}[؀-ۿ]")
    for role in ("template", "prompt", "guide", "json", "csv"):
        if not form["kind"][role]:
            continue
        name = form["kind"][role]
        for n, line in enumerate(form[role + "_text"].splitlines(), start=1):
            if line[:1] in (" ", "\t") or line.lstrip() != line:
                continue  # an indented continuation or list item
            for m in run.finditer(line):
                frag = line[max(0, m.start() - 30):m.end() + 30]
                bad.append(f"possible missing word in {name} line {n}: "
                           f"...{frag.strip()}...")


CHECKS = (
    check_files,
    check_json,
    check_csv,
    check_agreement,
    check_sections_in_template,
    check_labels_present,
    check_comments_balanced,
    check_no_visible_instructions,
    check_table_split,
    check_cjk,
    check_script_purity,
    check_guide_links,
    check_missing_word,
)


def audit(form: dict) -> list[str]:
    bad: list[str] = []
    for fn in CHECKS:
        fn(form, bad)
    return bad


# --------------------------------------------------------------------------
# self-test: every check must fire on a known-bad input
# --------------------------------------------------------------------------

REFERENCE = ("forms", "05_Executing", "08_Retrospective")


def _probe(which: str, mutate) -> bool:
    """Load the healthy reference form, apply a mutation, expect one check.

    The checks report by appending to a list and returning None, so the list
    has to be kept and inspected rather than testing the return value.
    """
    form = load_form(ROOT.joinpath(*REFERENCE))
    mutate(form)
    found: list[str] = []
    globals()[which](form, found)
    return bool(found)


def selftest() -> int:
    def list_value(form):
        form["json_text"] = json.dumps({"fields": {"f01": {
            "section": "S", "label": "L", "guidance": "g" * 60,
            "value": ["a", "b"]}}})

    def bare_csv(form):
        form["csv_text"] = "Col1,Col2\nx,y\n"

    def thin_guidance(form):
        form["json_text"] = json.dumps({"fields": {"f01": {
            "section": "S", "label": "L", "guidance": "short", "value": ""}}})

    def split_table(form):
        form["template_text"] = "| A | B |\n| --- | --- |\n\n| x | y |\n"

    def cjk(form):
        form["template_text"] += "\n\n文書\n"

    def arabic_in_english(form):
        form["template_text"] += "\n\nهذا نص عربي\n"

    def latin_in_arabic(form):
        form["rtl"] = True
        form["template_text"] += "\n\nThis is untranslated English prose.\n"

    def visible_quote(form):
        form["template_text"] += "\n\n> [ Add details... ]\n"

    def broken_link(form):
        form["guide_text"] += "\n\n[x](does_not_exist.md)\n"

    def unbalanced_comment(form):
        form["template_text"] += "\n\n<!-- never closed\n"

    def disagree(form):
        form["csv_text"] = ",".join(CSV_HEADER) + "\n" + \
            'Session,Other,"' + "g" * 60 + '",\n'

    def missing_file(form):
        form["kind"]["json"] = None

    cases = [
        ("check_files", missing_file),
        ("check_json", list_value),
        ("check_json", thin_guidance),
        ("check_csv", bare_csv),
        ("check_agreement", disagree),
        ("check_cjk", cjk),
        ("check_script_purity", arabic_in_english),
        ("check_script_purity", latin_in_arabic),
        ("check_no_visible_instructions", visible_quote),
        ("check_table_split", split_table),
        ("check_guide_links", broken_link),
        ("check_comments_balanced", unbalanced_comment),
    ]

    failures = 0
    for which, mutate in cases:
        try:
            fired = _probe(which, mutate)
        except Exception as exc:  # noqa: BLE001
            print(f"  ERROR  {which}: probe raised {exc!r}")
            failures += 1
            continue
        if fired:
            print(f"  ok     {which} fires on its known-bad input")
        else:
            print(f"  FAIL   {which} did NOT fire on its known-bad input")
            failures += 1

    baseline = audit(load_form(ROOT.joinpath(*REFERENCE)))
    if baseline:
        print(f"  note   reference form reports: {baseline}")
    else:
        print("  ok     reference form is clean (no false positives)")

    # Front matter is fixed configuration and must not read as untranslated
    # prose, while genuine prose in the same file still must.
    AR_CONFIG = ("---\nlang: ar\nlayout: default\nnav_order: 1\n"
                 "---\n\n<div dir=\"rtl\"></div>\n")

    form = load_form(ROOT.joinpath(*REFERENCE))
    form["rtl"] = True
    form["template_text"] = AR_CONFIG
    form["prompt_text"] = ""
    form["guide_text"] = ""
    form["json_text"] = ""
    form["csv_text"] = ""
    found: list[str] = []
    check_script_purity(form, found)
    if found:
        print(f"  FAIL   front matter treated as untranslated: {found}")
        failures += 1
    else:
        print("  ok     Jekyll front matter is not flagged as untranslated")

    # ...and the same file must still be flagged when real prose is present.
    form["template_text"] += "\n\nThis is untranslated English prose.\n"
    found = []
    check_script_purity(form, found)
    if found:
        print("  ok     untranslated prose beside front matter is still flagged")
    else:
        print("  FAIL   untranslated prose beside front matter went unnoticed")
        failures += 1

    # A coded reference such as TR-114 is an identifier, not untranslated prose.
    form = load_form(ROOT.joinpath(*REFERENCE))
    form["rtl"] = True
    form["template_text"] = ("<div dir=\"rtl\">\n"
                             "وثيقة اختبار TR-114 وسجل طلب الشراء PO-0097.\n"
                             "</div>\n")
    form["prompt_text"] = ""
    form["guide_text"] = ""
    form["json_text"] = ""
    form["csv_text"] = ""
    found = []
    check_script_purity(form, found)
    if found:
        print(f"  FAIL   coded reference treated as untranslated: {found}")
        failures += 1
    else:
        print("  ok     coded references are not flagged as untranslated")

    # Prose that merely contains digits must still be flagged.
    form["template_text"] += "\nThis sentence has 114 items to record.\n"
    found = []
    check_script_purity(form, found)
    if found:
        print("  ok     English prose with digits is still flagged")
    else:
        print("  FAIL   English prose with digits went unnoticed")
        failures += 1

    # A parenthetical English gloss is house style, but prose outside the
    # parentheses must still be flagged.
    form = load_form(ROOT.joinpath(*REFERENCE))
    form["rtl"] = True
    form["template_text"] = (
        "<div dir=\"rtl\">\n"
        "يتم إعداد هذا المخرج خلال **مرحلة المراقبة والتحكم "
        "(Monitoring & Controlling Process Group)** من الدورة.\n"
        "</div>\n")
    form["prompt_text"] = ""
    form["guide_text"] = ""
    form["json_text"] = ""
    form["csv_text"] = ""
    found = []
    check_script_purity(form, found)
    if found:
        print(f"  FAIL   gloss treated as untranslated: {found}")
        failures += 1
    else:
        print("  ok     parenthetical English gloss is not flagged")

    form["template_text"] += "\nThis whole sentence is English.\n"
    found = []
    check_script_purity(form, found)
    if found:
        print("  ok     prose outside the gloss is still flagged")
    else:
        print("  FAIL   prose outside the gloss went unnoticed")
        failures += 1

    # A word lost mid-sentence leaves two spaces behind and no other check
    # sees it, because the sentence still parses as Arabic.
    form = load_form(ROOT.joinpath(*REFERENCE))
    form["rtl"] = True
    form["template_text"] = (
        "<div dir=\"rtl\">\n"
        "هذا هو الاختبار الذي يُقاس عليه كل ميثاق في النهاية، عادةً بعد سنوات  "
        "شخص لم يكن حاضرًا عند كتابته.\n"
        "</div>\n")
    form["prompt_text"] = ""
    form["guide_text"] = ""
    form["json_text"] = ""
    form["csv_text"] = ""
    found = []
    check_missing_word(form, found)
    if found:
        print("  ok     a word lost mid-sentence is flagged")
    else:
        print("  FAIL   a word lost mid-sentence went unnoticed")
        failures += 1

    # ...and an indented continuation line is layout, not a gap.
    form["template_text"] = (
        "<div dir=\"rtl\">\n"
        "سطر مستمر مع مسافة بادئة\n"
        "   _followed by four spaces of indentation here.\n"
        "</div>\n")
    found = []
    check_missing_word(form, found)
    if found:
        print(f"  FAIL   indentation treated as a missing word: {found}")
        failures += 1
    else:
        print("  ok     indented continuation lines are not flagged")
    return failures


def main() -> int:
    args = sys.argv[1:]
    if "--selftest" in args:
        print("Self-test: each check must fire on its known-bad input.\n")
        return 1 if selftest() else 0

    forms = load_all_forms()
    needles = [a for a in args if not a.startswith("--")]
    if needles:
        forms = [f for f in forms if any(n in str(f["dir"]) for n in needles)]
    if not forms:
        print("No forms matched.")
        return 0

    total = 0
    clean = 0
    for form in forms:
        bad = audit(form)
        if bad:
            total += len(bad)
            print(f"\n{rel(form)}")
            for b in bad:
                print(f"  - {b}")
        else:
            clean += 1

    print(f"\n{clean}/{len(forms)} forms clean, {total} problem(s) found.")
    if total and "--report" in args:
        return 0
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
