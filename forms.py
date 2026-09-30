"""The settled per-form pipeline, extracted from the two forms that now pass
every gate.

Two forms were built with their own scripts and the scripts drifted apart: the
RBS's stem derivation added a separator and produced a doubled underscore on
three separate files, and the guidance was taken from the English JSON so five
English words reached the Arabic files. Both were fixed by hand in the RBS.
Consolidating here means the next six forms get the fixes for free.

The order is mandatory: `gen_ar_all` reads labels from the generated Arabic
template, and the prompt and guide read from the JSON that `gen_ar_all`
writes.

  1. tr_lookup.check()   every English string the template contains has a
                         translation, so an untranslated string fails here
  2. guidance_ar.check() every Arabic label has guidance, no splice, and no
                         English word in the prose
  3. gen_en.py           the English JSON and CSV
  4. gen_en_md.py        the English prompt and guide
  5. gen_ar_tpl.py       the Arabic template
  6. gen_ar_all.py       the Arabic JSON and CSV
  7. gen_ar_md.py        the Arabic prompt and guide
  8. install             copy all ten into the tree
  9. verify              audit both languages, render parity, read the Arabic
"""

import pathlib
import sys

HERE = pathlib.Path(__file__).parent


def stem_from(repo, prefix, ext=".json"):
    """The Arabic stem, taken from a file that carries no suffix.

    Never slice a suffix off the template's name and never add a separator:
    the template's suffix is joined directly to a stem that ends in the
    closing parenthesis of an acronym, so both operations go wrong. Every
    filename in this pipeline is built from a file that has no suffix.
    """
    for q in (repo / "forms" / "ar").rglob(f"{prefix}*{ext}"):
        return q.name[: -len(ext)]
    raise SystemExit(f"no Arabic {ext} found for {prefix}")


def ar_dir_from(repo, prefix, ext=".json"):
    for q in (repo / "forms" / "ar").rglob(f"{prefix}*{ext}"):
        return q.parent
    raise SystemExit(f"no Arabic {ext} found for {prefix}")


def en_dir_from(repo, stem):
    return next((repo / "forms").rglob(f"{stem}_Template.md")).parent


def suffixes():
    """The Arabic filename suffixes, assembled from code points copied out of
    committed filenames rather than typed."""
    qalb = "".join(chr(c) for c in (0x642, 0x627, 0x644, 0x628))
    dalil = "".join(chr(c) for c in (0x62F, 0x644, 0x64A, 0x644))
    return {"template": f"_{qalb}.md",
            "prompt": ".md",
            "guide": f"_{dalil}.md",
            "json": ".json",
            "csv": ".csv"}


def install_all(repo, src, stem_ar, files):
    """Copy the five files of one language into the tree."""
    import shutil
    dest = ar_dir_from(repo, stem_ar.split("_")[0] + "_" + stem_ar.split("_")[1])
    for key, name in files.items():
        s = src / name
        if not s.exists():
            raise SystemExit(f"missing {s}")
        shutil.copy2(s, dest / s.name)
        print("installed", s.name)
    return dest


if __name__ == "__main__":
    # negative-test the stem helper, since a wrong stem has been the single
    # most common defect in these two forms
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / "forms" / "ar" / "x").mkdir(parents=True)
        name = "04_06_03_hekl_tajzia_(RBS)"
        (root / "forms" / "ar" / "x" / f"{name}.json").write_text("{}")
        got = stem_from(root, "04_06_03")
        assert got == name, got
        print("stem_from ok:", got)

        suf = suffixes()
        assert "قالب" in suf["template"], suf["template"]
        assert "دليل" in suf["guide"], suf["guide"]
        print("suffixes ok:", suf["template"], suf["guide"])
    print("ALL OK")
