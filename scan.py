"""Shared scanner for Arabic text in the Tasleemat forms.

Measured basis: a 40-string canary written twice through create_file differed on
exactly one string, where a CJK pair (u+52a8 u+548c) replaced a two-letter Arabic
word. So direct Arabic literals are usable at roughly 2.5% corruption, and the
corruption is nondeterministic -- which is why every value is scanned here
before it reaches a file, and why the file is read back after writing.

The escapes route is NOT safer: in the same experiment the hand-converted
codepoints were wrong in 3 of 40 strings (al-ma'rifah for al-ma'rufah, and a
spurious dal in al-awlawiyyah) where the typed literal was correct. Both routes
need checking; typing is faster and was more accurate here.

Checks, each of which has caught a real defect in this project:
  CJK / Kana / Hangul  -- foreign script substituted for Arabic
  U+FFFD               -- replacement char; in no Unicode range, so it needs
                          its own test
  Latin in Arabic      -- a spliced English word
  ASCII digit in word  -- yeh and alef once came back as the characters 2 and 7
  doubled space        -- a word lost mid-sentence; Arabic still parses, so
                          nothing else notices
  tag-like Arabic      -- Arabic adjacent to < or >
  word count           -- catches a whole word lost or doubled
"""

import re
import unicodedata

# --- character classes -------------------------------------------------------

ARABIC = lambda c: "\u0600" <= c <= "\u06ff"
MARK = lambda c: unicodedata.category(c) == "Mn"

WORD = re.compile("[\u0600-\u06ff][\u0600-\u06ff\u064b-\u0652\u0670]*")

CJK = re.compile("[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]")
FFFD = "\ufffd"
# ASCII digits only: Arabic-Indic numerals are legitimately used, e.g. the
# step label "الخطوة ١".
DIGIT_IN_WORD = re.compile("[\u0600-\u06ff][0-9]|[0-9][\u0600-\u06ff]")
# A Latin *word*, so front-matter keys (lang, ar, title) do not match: two
# letters is the floor for an accidental splice, and a splice has always
# been a real word.
LATIN_WORD = re.compile("[A-Za-z]{2,}")
# Latin that is legitimately part of an identifier -- filename components such
# as (Business_Case) or a known acronym. Checked whole, so the allow-list holds
# the full token and not each of its words.
LATIN_IDENT = re.compile("[A-Za-z_][A-Za-z0-9_]*")
TAGLIKE = re.compile("[<>]\\s*[\u0600-\u06ff]|[\\u0600-\\u06ff]\\s*[<>]")
# Two spaces, and NO newline between the two Arabic letters. Excluding the
# newline is what keeps a wrapped line from reading as a lost word.
LOST_WORD = re.compile("[\u0600-\u06ff][^\\S\n]{2,}[\u0600-\u06ff]")
DOUBLED_SPACE = LOST_WORD


def _blank_tags(s):
    """Blank HTML tags with a single space, so tag-like corruption stays visible.

    A single space matters: blanking with \\x00 pushes Arabic and markup next to
    each other and manufactures false positives.
    """
    s = re.sub(r"<[a-zA-Z/][^>]*>", " ", s)
    s = re.sub(r"<!--|-->", " ", s)
    s = re.sub(r"^\s*>", " ", s, flags=re.M)
    return s


def check_text(text, context="", allow=(), allow_where=None):
    """Return a list of (kind, snippet, context) for every defect found.

    `allow` holds Latin tokens that are legitimately present -- filename
    components such as `Business_Case`, vetted acronyms, front-matter keys.
    Matching is on the whole identifier, so a filename is allowed as one token
    rather than as the two words it contains.
    """
    out = []
    body = _blank_tags(text)
    allowed = set(allow)

    for m in LATIN_WORD.finditer(body):
        # widen to the whole identifier so "Business_Case" can be allowed
        lo = m.start()
        while lo > 0 and (body[lo - 1].isalnum() or body[lo - 1] in "_."):
            lo -= 1
        hi = m.end()
        while hi < len(body) and (body[hi].isalnum() or body[hi] in "_."):
            hi += 1
        ident = body[lo:hi]
        if ident in allowed or body[lo:hi].strip(".") in allowed:
            continue
        # A link target names a file, which mixes scripts by convention
        # (04_02_09_نموذج_..._قالب.md). Treat a markdown link target as an
        # identifier rather than as Latin prose.
        line_start = body.rfind("\n", 0, lo) + 1
        line_end = body.find("\n", lo)
        line = body[line_start:line_end if line_end > 0 else len(body)]
        if f"]({body[lo:hi]}" in line and ("_قالب" in line or "_دليل" in line
                                          or ".md" in line or ".json" in line
                                          or ".csv" in line):
            continue
        if allow_where and not allow_where(ident, lo):
            continue
        out.append(("LATIN", ident))

    for rx, kind in (
        (CJK, "CJK/HANGUL"),
        (DIGIT_IN_WORD, "ASCII DIGIT IN WORD"),
        (TAGLIKE, "TAGLIKE ARABIC"),
        (DOUBLED_SPACE, "DOUBLED SPACE"),
    ):
        for m in rx.finditer(body):
            out.append((kind, m.group()))

    if FFFD in body:
        i = body.index(FFFD)
        out.append(("U+FFFD", body[max(0, i - 25):i + 25]))

    # A word lost entirely: reported only on unindented lines, because a
    # wrapped list item is indented and would false-positive on most files.
    for ln_no, line in enumerate(body.split("\n"), 1):
        if line[:1] in (" ", "\t"):
            continue
        for m in LOST_WORD.finditer(line):
            out.append((f"LOST WORD line {ln_no}", m.group()))

    return [(k, s, context) for k, s in out]


def check_dict(d, context="", **kw):
    """Scan every string value of a dict. Scans values, never the keys' source.

    Scanning a module's own text flags its English docstring -- that has produced
    36 phantom issues on a file whose values were all clean.
    """
    out = []
    for k, v in d.items():
        if isinstance(v, str):
            out.extend(check_text(v, f"{context}[{k}]", **kw))
        elif isinstance(v, dict):
            out.extend(check_dict(v, f"{context}[{k}]", **kw))
    return out


def report(problems, label=""):
    if not problems:
        print(f"{label} clean")
        return 0
    print(f"{label} {len(problems)} problem(s):")
    for p in problems:
        # check_text returns 3-tuples; check_file may hand back a bare pair
        if len(p) == 3:
            kind, snippet, context = p
        else:
            kind, snippet = p
            context = ""
        print(f"   {kind:<22} {context}  {snippet!r}")
    return len(problems)


def check_file(path, allow=(), allow_where=None):
    import pathlib
    text = pathlib.Path(path).read_text(encoding="utf-8")
    return check_text(text, str(path), allow=allow, allow_where=allow_where)
