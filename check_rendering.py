"""Offline structural check for the GitHub "invisible header" bug.

Why this exists
---------------
GitHub's markdown API reproduced the reported bug exactly: for a template
whose first line opens a raw <div> and whose last line closes it, GitHub
emitted no company header, no <h1> title and no "1. Audit Information" --
the markdown inside that span was swallowed as one opaque HTML block.

A locally built cmark-gfm 0.29.0.gfm.11 does NOT reproduce this, so a local
parser cannot be trusted as an oracle for this bug. This script checks the
structural invariant that makes the bug possible, which is version
independent and needs no network:

    If a file's first line opens a raw HTML element that is not closed on
    that same line, the element spans the document. GitHub can treat the
    whole span as a single HTML block and discard the markdown inside it.

A standalone single-line element (e.g. <h1 ...>Title</h1>) closes on its
own line and is always safe.

Usage:  python3 check_rendering.py [forms_dir]
Exit code 1 if any at-risk template is found.
"""
import io
import os
import re
import sys

OPEN_TAG = re.compile(r"^<([a-zA-Z][a-zA-Z0-9-]*)(\s|>|/)")


def spanning_tag_of_text(text):
    """Return the tag name if the text opens an element it does not also close."""
    lines = text.split("\n")
    if not lines:
        return None
    first = lines[0].strip()
    if first.startswith("<!--") or not first.startswith("<"):
        return None
    m = OPEN_TAG.match(first)
    if not m:
        return None
    tag = m.group(1)
    if re.search(r"</%s>\s*$" % re.escape(tag), first):
        return None
    if first.rstrip().endswith("/>"):
        return None
    return tag


def spanning_tag(path):
    """Return the tag name if line 1 opens an element it does not also close."""
    return spanning_tag_of_text(io.open(path, encoding="utf-8").read())


def main(root):
    files = []
    for dirpath, _, names in os.walk(root):
        for n in names:
            if n.endswith("_Template.md") or n.endswith("_قالب.md"):
                files.append(os.path.join(dirpath, n))

    bad = []
    for p in sorted(files):
        tag = spanning_tag(p)
        if tag:
            bad.append((p, tag))

    ar = [b for b in bad if os.sep + "ar" + os.sep in b[0]]
    en = [b for b in bad if b not in ar]
    print("templates scanned : %d" % len(files))
    print("AT RISK           : %d  (EN %d / AR %d)"
          % (len(bad), len(en), len(ar)))
    for p, tag in bad[:15]:
        print("   <%s> spans file   %s" % (tag, os.path.relpath(p, root)))
    if len(bad) > 15:
        print("   ... and %d more" % (len(bad) - 15))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "forms"))
