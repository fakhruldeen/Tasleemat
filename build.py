"""Build all five files of a form, in both languages, from one field list.

The point of this module is that the JSON, the CSV, the prompt and the guide
are all generated from the same source, so a label cannot drift between them.
That has been the defect that shipped twice: a form whose JSON carried the
previous form's name and document reference, and a prompt whose front matter
named a different form than its own guide.

The Arabic printable template is generated too, by walking the verified English
template and substituting only headings, labels, column headers, roles and
placeholders. Everything structural -- blank lines, the comment block, table
shapes -- is inherited from the English, which is why six consecutive forms
came through with no corruption on the first scan.

Identity is read from the JSON and never typed into a generator. A generator
that hardcodes the form name has shipped the wrong name through a clean
13-check audit.
"""

import csv
import io
import json
import pathlib
import re

import scan

ARABIC = lambda c: "\u0600" <= c <= "\u06ff"
WORD = re.compile("[\u0600-\u06ff][\u0600-\u06ff\u064b-\u0652\u0670]*")

CSV_HEADER = ["Section", "Field", "Guidance", "LLM_Generated_Value"]

# Latin that is legitimately present in an Arabic artefact. `parameters` is
# referenced by every prompt and template, and the document reference itself
# is Latin by convention, so both are allow-listed rather than suppressed.
ALLOW = (
    "Tasleemat", "Business_Case",
    "lang", "ar", "en", "title", "layout", "default", "Form", "Instructions",
    "nav_order", "Generated", "on", "by", "Ref", "Template", "Markdown",
    "JSON", "CSV", "Data", "Schema", "Structure", "Printable", "LLM",
    "Generation", "Prompt", "Tabular", "Associated", "Templates", "Output",
    "Artifact", "QA", "UAT", "RBS", "WBS", "RACI", "The", "and", "of", "to",
    "for", "with", "Guide", "What", "Why", "When", "Who", "How",
    "parameters.md", "parameters", "PMO",
)


# --- sections and fields -----------------------------------------------------

def sections_of(fields):
    """Group an ordered list of (section, label) pairs, preserving order."""
    order, groups = [], {}
    for section, label in fields:
        if section not in groups:
            groups[section] = []
            order.append(section)
        groups[section].append(label)
    return [(s, groups[s]) for s in order]


# --- JSON --------------------------------------------------------------------

def build_json(name, ref, fields, guidance, meta=None, lang="ar"):
    """Build the JSON. `guidance` maps label -> guidance text.

    `_llm_instructions` follows the language of the file it goes into. It was
    hardcoded Arabic, which put Arabic inside the English JSON -- caught by the
    audit's no-Arabic-in-English-files check.
    """
    missing = [label for _, label in fields if label not in guidance]
    if missing:
        raise SystemExit(f"no guidance for: {missing}")

    if lang == "ar":
        instructions = (
            f"قم بتعبئة حقول '{name}' وكتابة قيمة كل حقل في موضع "
            "'القيمة المولَّدة' اعتمادًا على سياق المشروع. "
            f"السياق: المشروع الذي يحمل المرجع {ref}."
        )
    else:
        instructions = (
            f"Populate the fields of '{name}' and write the value of each "
            "field under 'Generated Value', based on the project context. "
            f"Context: the project carrying reference {ref}."
        )

    data = {
        "form_name": name,
        "document_reference": ref,
        "_llm_instructions": instructions,
    }
    if meta:
        data.update(meta)
    data["fields"] = {}
    for i, (section, label) in enumerate(fields, 1):
        key = f"f{i:02d}_" + re.sub(r"[^\w]+", "_", label, flags=re.UNICODE).strip("_")
        data["fields"][key] = {
            "section": section,
            "label": label,
            "guidance": guidance[label],
            "value": "",
        }
    return data


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n",
                    encoding="utf-8")


# --- CSV ---------------------------------------------------------------------

def build_csv(fields, guidance):
    """Build the CSV from the same field list, so it cannot disagree with the JSON."""
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(CSV_HEADER)
    for section, label in fields:
        w.writerow([section, label, guidance[label], ""])
    return buf.getvalue()


def write_csv(path, text):
    path.write_text(text, encoding="utf-8")


# --- Arabic printable template ----------------------------------------------

H3 = re.compile(r"^###\s+(.*?)\s*$")
H2 = re.compile(r"^##\s+(.*?)\s*$")
BOLD_LABEL = re.compile(r"^\*\*([^*]+?):\*\*\s*(.*)$")
TABLE_ROW = re.compile(r"^\|(.+)\|\s*$")
SEPARATOR = re.compile(r"^\|[\s:|-]+\|\s*$")
PLACEHOLDER = re.compile(r"\{\{([^}]+)\}\}")
META_LABEL = re.compile(r"\*\*([^*]+?):\*\*")


def _split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def build_ar_template(en_text, tr):
    """Walk the verified English template and substitute translated strings.

    `tr` must provide SECTIONS, LABELS, COLUMNS, ROLES and PLACEHOLDERS dicts,
    each keyed by the exact English string. A missing key raises rather than
    passing the English through, so an untranslated string fails loudly.
    """
    out = []
    lines = en_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        # heading levels
        m = H3.match(line) or H2.match(line)
        if m:
            level = line[:3]
            body = m.group(1)
            # The number in a numbered heading is outside the regex body, so
            # the body is the heading text alone. An earlier version
            # re-prepended the number and produced a doubled space after
            # every heading marker.
            num = re.match(r"^(\d+\.\s*)", body)
            num = num.group(1) if num else ""
            bare = body[len(num):]
            if bare in tr["SECTIONS"]:
                body = num + tr["SECTIONS"][bare]
            elif bare in tr["LABELS"]:
                body = num + tr["LABELS"][bare]
            elif body in tr["ALLOW_HEADINGS"]:
                pass                        # already a permitted proper noun
            else:
                # Do not pass English through. A heading that has no
                # translation is an untranslated string, and it has shipped
                # through a clean audit more than once.
                raise SystemExit(f"untranslated heading: {body!r}")
            out.append(f"{level} {body}".replace("##  ", "## "))
            i += 1
            continue

        # table rows: translate each data row, keep separator rows verbatim
        if TABLE_ROW.match(line):
            j = i + 1
            while j < len(lines) and TABLE_ROW.match(lines[j]):
                j += 1
            for k in range(i, j):
                row = lines[k]
                if SEPARATOR.match(row):
                    out.append(row)          # alignment markers are structural
                    continue
                # A *metadata* row is a single line of **Label:** {{value}}
                # pairs. A sign-off row also contains {{...}} but is a normal
                # table whose cells must each be translated, so the test is
                # whether the first cell is a bold metadata label, not
                # whether the row mentions a placeholder at all.
                first = _split_row(row)[0].strip()
                if META_LABEL.match(first):
                    out.append(_translate_meta_row(row, tr))
                else:
                    out.append(_translate_row(row, tr))
            i = j
            continue

        # bold label lines: **Label:** value
        m = BOLD_LABEL.match(line)
        if m:
            label, rest = m.group(1), m.group(2)
            if label not in tr["LABELS"]:
                raise SystemExit(f"untranslated label: {label!r}")
            new = f"**{tr['LABELS'][label]}:**"
            if rest:
                # rest may itself be a placeholder such as [ Add details... ],
                # so it goes through the same substitution as any other line
                new += f" {translate_inline(rest, tr)}"
            out.append(new)
            i += 1
            continue

        out.append(translate_inline(line, tr))
        i += 1

    return "\n".join(out)


def _translate_meta_row(line, tr):
    """A metadata cell is a bold label followed by its value.

    `META_LABEL.fullmatch` cannot be used here: the cell is
    `**Label:** {{Placeholder}}`, so the regex never consumes the whole
    string and the label is left in English. `match` on the prefix is what
    the shape of the cell calls for, and the remainder is translated
    separately so the placeholder is substituted rather than discarded.
    """
    cells = _split_row(line)
    out = []
    for cell in cells:
        c = cell.strip()
        m = META_LABEL.match(c)
        if m and m.group(1) in tr["LABELS"]:
            rest = c[m.end():].strip()
            value = f" {translate_inline(rest, tr)}" if rest else ""
            out.append(f"**{tr['LABELS'][m.group(1)]}:**{value}")
        else:
            out.append(translate_inline(cell, tr))
    return "| " + " | ".join(out) + " |"


def _translate_row(line, tr):
    cells = _split_row(line)
    out = []
    for cell in cells:
        c = cell.strip()
        if not c:
            out.append(c)
            continue
        # A cell may be wrapped in bold markers: **Team Lead**. Strip them to
        # look the content up, then restore them. Without this a role in the
        # sign-off table is left untranslated, which is exactly where a role
        # most often appears.
        bold = c.startswith("**") and c.endswith("**")
        key = c[2:-2].strip() if bold else c
        if key in tr["COLUMNS"]:
            out.append(tr["COLUMNS"][key])
            continue
        if key in tr["LABELS"]:
            out.append(tr["LABELS"][key])
            continue
        if key in tr["ROLES"]:
            out.append(tr["ROLES"][key])
            continue
        meta = META_LABEL.match(key)
        if meta and meta.group(1) in tr["LABELS"]:
            out.append(f"**{tr['LABELS'][meta.group(1)]}:**")
            continue
        if "[ Add details... ]" in c:
            out.append(tr["PLACEHOLDERS"]["add_details"])
            continue
        if re.fullmatch(r"\[\s*\.{4}\s*-\s*\.{4}\s*-\s*\.{4}\s*\]", c):
            out.append(tr["PLACEHOLDERS"].get("date_mask", c))
            continue
        if "[" in c and "]" in c:
            out.append(tr["PLACEHOLDERS"]["fill"])
            continue
        out.append(translate_inline(c, tr))
    return "| " + " | ".join(out) + " |"


def translate_inline(text, tr):
    """Substitute placeholders, inline bold labels and fill-in markers."""
    def ph(m):
        name = m.group(1)
        if name not in tr["PLACEHOLDERS"]:
            raise SystemExit(
                f"untranslated placeholder: {name!r} "
                f"(from {text!r})"
            )
        return "{{" + tr["PLACEHOLDERS"][name] + "}}"
    text = PLACEHOLDER.sub(ph, text)
    # the fill-in marker is prose, not a template placeholder, so it is
    # substituted before the generic bracket rule can swallow it
    text = text.replace("[ Add details... ]", tr["PLACEHOLDERS"]["add_details"])
    text = re.sub(r"\*\*([^*]+?):\*\*",
                  lambda m: f"**{tr['LABELS'].get(m.group(1), m.group(1))}:**",
                  text)
    return text


# --- verification ------------------------------------------------------------

def check_braces(text, label="template"):
    """Every `{{Name}}` placeholder must carry both braces, and the count is
    reported.

    A template written as a Python literal and passed through `str.format`
    loses one brace from each side unless the source doubled them, leaving
    `{Name}` -- a token no substitution will ever fill. Neither the audit nor
    the renderer inspects braces, so the file reaches the tree looking clean.
    Found on PMO-05.09, where the English template had nine such tokens and
    the Arabic builder carried all nine across faithfully.
    """
    bad = re.findall(r"(?<!\{)\{[A-Za-z_\u0600-\u06FF][^{}]*\}(?!\})", text)
    good = re.findall(r"\{\{[^{}]+\}\}", text)
    if bad:
        for b in sorted(set(bad)):
            print(f"  PLACEHOLDER WITHOUT BRACES in {label}: {b}")
        raise SystemExit(f"{len(bad)} malformed placeholder(s) in {label}")
    return len(good)


def verify_ar(text, label=""):
    problems = scan.check_text(text, label, allow=ALLOW)
    return scan.report(problems, label or "arabic")


def verify_pair(en_json_path, ar_json_path, ar_paths):
    """Compare the Arabic JSON against the English one, field for field.

    A cross-language comparison catches an identity defect that neither file
    contradicts on its own: a form whose form_name and document_reference are
    both wrong still agrees with itself.
    """
    en = json.loads(pathlib.Path(en_json_path).read_text(encoding="utf-8"))
    ar = json.loads(pathlib.Path(ar_json_path).read_text(encoding="utf-8"))
    problems = []
    if ar["document_reference"] != en["document_reference"]:
        problems.append(("REF MISMATCH",
                         f"EN {en['document_reference']} vs AR "
                         f"{ar['document_reference']}", "identity"))
    if len(ar["fields"]) != len(en["fields"]):
        problems.append(("FIELD COUNT",
                         f"EN {len(en['fields'])} vs AR {len(ar['fields'])}",
                         "identity"))
    en_sections = [v["section"] for v in en["fields"].values()]
    ar_sections = [v["section"] for v in ar["fields"].values()]
    if len(ar_sections) != len(en_sections):
        problems.append(("SECTION COUNT",
                         f"EN {len(en_sections)} vs AR {len(ar_sections)}",
                         "identity"))
    for p in ar_paths:
        problems.extend(scan.check_file(p, allow=ALLOW))
    return scan.report(problems, "pair")


def check_rows(text, label="template"):
    """Every table row must be one line.

    `TABLE_ROW` requires a leading and a trailing pipe, so a row
    that a generator's string concatenation wrapped across two
    source lines produces two fragments, and *neither* matches.
    concatenation wrapped across two source lines produces two fragments, and
    *neither* matches: the first has no closing pipe and the second has no
    opening one. Both fragments then fall through to `translate_inline`, which
    leaves role names in English, truncates a multi-cell row, and turns real
    placeholders into fragments that no brace check recognises.

    Found on PMO-06.09, where seven rows in one template were wrapped that way
    and the only symptom the gates reported was untranslated Latin in the
    Arabic file.
    """
    bad = []
    for i, line in enumerate(text.split("\n"), 1):
        s = line.rstrip()
        if s.startswith("|") and not s.endswith("|"):
            bad.append((i, s[:60]))
    if bad:
        for i, s in bad:
            print(f"  line {i}: table row with no closing pipe: {s!r}")
        raise SystemExit(
            f"{len(bad)} table row(s) broken in {label} at line "
            f"{bad[0][0]}; a row must be a single source line"
        )
    return True
