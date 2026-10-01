# Resuming work on Tasleemat

Written before a reboot. Everything needed to continue is in this directory;
nothing important lives only in `/tmp`.

## Where things are

| what | where | survives reboot |
| --- | --- | --- |
| Completed forms | `forms/` and `forms/ar/`, committed and pushed | yes |
| `progress.md` — the checklist | repo root, **gitignored** (`.gitignore:27`) | yes, but never pushed |
| `plan.md` — backlog notes | repo root, committed | yes |
| Pipeline generators | `.staging/` | yes, untracked |
| Shared library copies | `.staging/lib/` | yes, untracked |

The generators used to live in `/tmp/fast/`, which a reboot clears. They are
now under `.staging/`, so after a reboot copy them back:

```
cd /home/mohamed/Desktop/PMOSKILL/Tasleemat
rm -rf /tmp/fast/lib /tmp/fast/forms
cp -r .staging/lib /tmp/fast/lib
mkdir -p /tmp/fast/forms
for d in .staging/forms/*/; do cp -r "$d" /tmp/fast/forms/; done
```

Each `forms/<dir>/` is one form's working directory. `tr_ar.py` and
`guidance_ar.py` are the two files that must be read and re-checked before
generating anything; everything else is a thin generator.

## State at the time of writing

88 forms done, 5 open. HEAD is `a09bb3c`, pushed, working tree clean apart
from `plan.md` and `.gitignore`.

Open, in the order `progress.md` lists them:

1. `04_09_04` Statement Of Work (SOW)
2. `04_09_05` Request For Proposal (RFP)
3. `04_11_01` OCM Strategy And Plan
4. `04_11_02` Training Plan And Log
5. `07_04` Transition To Operations Checklist

The most recent completed form is `04_05_03`; its staging directory is
`.staging/forms/dor/` and is the best template for a two-section prose form.
`07_04` is the next one that has a **table** rather than prose sections, so
`06_09` (`.staging/forms/vps/`) is the closer model for it.

## The pipeline, and the order it must run in

```
tr_ar.check()  ->  guidance_ar.check()  ->  gen_en.py  ->  gen_en_md.py
  ->  en_install.py  ->  gen_ar_tpl.py  ->  gen_ar_all.py  ->  install_verify.py
```

Running out of order produces a misleading "no guidance for" error, because
`gen_ar_all` reads labels from the generated English JSON.

`install_verify.py` runs audit_forms (EN and AR), check_rendering, and local
GFM parity, and installs the five Arabic files. It is the single command that
verifies a form.

## What is not optional

**Read the generated Arabic by eye.** On every form this session, every gate was
green and the documents still contained defects that no check reports:
agreement errors, a doubled clause, a plural subject with a singular predicate,
a footer separator swallowed by a regex. Reading is the only gate that finds
those. It has never once been wasted.

The tools, in the order they earn their place:

- `scan.py` — CJK/Kana/Hangul, U+FFFD, Latin splices, doubled spaces
- `trcheck.py` — every Arabic word must be attested in the committed tree
- `build.check_rows` — a table row wrapped across two source lines is invisible
  to every other gate
- `parity_local.py` — structural comparison between the two languages
- `build.check_braces` — a single-brace placeholder is a token nothing fills

## Traps that have already cost time

Each of these has been paid for at least once. They are in
`/memories/repo/` in more detail.

1. **Never type Arabic by character into a file and check afterwards.** Six
   foreign splices reached one form's staging directory: Chinese, Russian,
   Japanese, Korean, two English. Two of them would have shipped undetected,
   because a CJK or Cyrillic character renders as a plausible-looking block of
   script and defeats any check that only inspects Arabic.

2. **Write a prose block whole, once, then read it.** Patching sentence by
   sentence left duplicate lines and deleted content four times on one form.
   Line-index edits are for a single genuinely targeted line.

3. **Verify the check before changing the file.** A throwaway regex I wrote to
   verify four guide links reported them truncated, using the same faulty
   pattern I was hunting for. The files were correct; the check was wrong.

4. **The tree has no dual number, and no nouns for several ordinary things**
   (length, words, milestone, ticket, device). Rebuild the sentence on what
   exists and accept that it says slightly less.

5. **`و` attaches only to words attested affixed.** `وثمن` fails while `ثمن`
   is attested bare. Measure the affixed string, not the stem.

6. **Never wrap a table row across two source lines** in a `TEMPLATE` literal.
   A 150-character line is the right trade.

## Not done, deliberately

Deferred by earlier instruction, and not to be picked up without asking:

- the dependency-mapping proposal in `plan.md`
- the six `progress.md` entries that do not match `mapping.md`
- the seven prompts that name a different form than their own JSON
- the stray `02_02_AI_Governance_Plan_Template.md`

PMBOK content across this repository is **reconstructed from practice, not
transcribed**, and every commit message says so.