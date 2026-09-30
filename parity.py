"""Compare the GitHub render of a form's English and Arabic files, and print
the rendered Arabic so it can be read.

Structural parity between the two languages is the check that has caught
defects every other check passed: a table that rendered as zero rows, a heading
level that vanished, a column count that differed by four. Reading the rendered
Arabic is what caught a missing preposition in English-equivalent guidance.
"""

import collections
import json
import pathlib
import re
import sys
import urllib.request


def render(path):
    body = json.dumps({
        "text": pathlib.Path(path).read_text(encoding="utf-8"),
        "mode": "gfm",
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.github.com/markdown",
        data=body,
        headers={"Content-Type": "application/json",
                 "Accept": "application/vnd.github+json"})
    return urllib.request.urlopen(req).read().decode("utf-8", "replace")


def counts(html):
    return collections.Counter(re.findall(r"<(h1|h2|h3|table|tr|th|td)\b", html))


def plain(html):
    t = re.sub(r"<[^>]+>", " ", html)
    t = re.sub(r"[ \t]+", " ", t)
    return t


def main():
    en_dir, ar_dir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    pairs = sys.argv[3:]

    bad = 0
    for name_en, name_ar in zip(pairs[::2], pairs[1::2]):
        ce = counts(render(en_dir / name_en))
        ca = counts(render(ar_dir / name_ar))
        label = name_en.split("_", 3)[-1]
        print(f"\n=== {label}")
        for k in ("h1", "h2", "h3", "table", "tr", "th", "td"):
            ok = ce[k] == ca[k]
            bad += 0 if ok else 1
            print(f"  {'ok  ' if ok else 'DIFF'} {k:>5}: EN {ce[k]:>3}  AR {ca[k]:>3}")

    print(f"\n{'PARITY OK' if not bad else str(bad) + ' DIFFERENCE(S)'}")

    if "--read" in sys.argv:
        for name in pairs[1::2]:
            if name.endswith("Guide.md"):
                continue
            print("\n" + "=" * 70)
            print("RENDERED ARABIC:", name)
            print("=" * 70)
            for line in plain(render(ar_dir / name)).split("\n"):
                line = line.strip()
                if line:
                    print(line[:300])


if __name__ == "__main__":
    main()
