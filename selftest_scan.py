"""Negative-test scan.py: every check must fire on a planted defect and stay
silent on clean text. A checker that has not been negative-tested is not
evidence, and an earlier round shipped a real defect past a checker built on
that assumption.
"""

import sys

sys.path.insert(0, "/tmp/fast/lib")
import scan

PLANTED = [
    ("CJK",        "\u0627\u0644\u0623\u0646\u0634\u0637\u0629 \u548c \u0627\u0644\u0623\u0646\u0634\u0637\u0629"),
    ("KANA",       "\u0645\u0648\u062f\u064a\u0648\u064b\u0644 Exclusion \u0627\u0644\u062d\u062a"),
    ("HANGUL",     "\u0644\u0627 \u0634\u064a\u0621 \u6280\uac00\uac00 \u0645\u062a\u0633\u062a\u0642\u0628\u0644"),
    ("U+FFFD",     "\u0627\u0644\u0645\u0646\u0635\u0629\ufffd \u0627\u0644\u062b\u0627\u0646\u064a\u0629"),
    ("LATIN",      "\u0627\u0644\u062a\u0631\u0627\u0643\u0645 \u0639\u0646 \u0642\u0627\u0626\u0645\u0629 backlog"),
    ("DIGIT",      "\u062c\u062f\u0631 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a 27\u0644\u0633\u062c\u0644"),
    ("LOST_WORD",  "\u0647\u0630\u0627 \u0645\u0627 \u064a\u0641\u0635\u0644\u0647\u0627  \u0639\u0646 \u0627\u0644\u0642\u0627\u0626\u0645\u0629"),
    ("TAGLIKE",    "\u0645\u0646 \u0627\u0644\u062e\u0631\u064a\u0637\u0629 <\u0627\u0644\u0625\u0635\u062f\u0627\u0631> \u0627\u0644\u0623\u0648\u0644"),
]

ALWAYS_OK = ("lang", "ar", "en", "title", "layout", "default", "Form",
             "Instructions", "nav_order", "Generated", "on", "by", "Ref",
             "Template", "Markdown", "JSON", "CSV", "Data", "Schema",
             "Structure", "Printable", "LLM", "Generation", "Prompt",
             "Tabular", "Associated", "Templates", "Output", "Artifact",
             "Tasleemat", "The", "and", "of", "to", "for", "with", "Business_Case")

CLEAN = [
    ("front matter", "---\nlang: ar\nlayout: default\ntitle: نموذج تخطيط\nnav_order: 1\n---\n"),
    ("tags",         '<div dir="rtl">محضر الاجتماع</div>'),
    ("comment",      '<!-- تعليمات للنموذج الذكي:\n  قم بملء النموذج أدناه. -->\nمحضر'),
    ("block quote",  "> أضف التفاصيل... "),
    ("arabic-indic", "الخطوة ١ من الخطوات"),
    ("filename",     "القالب (Business_Case) مرجع"),
    ("footer link",  'by <a href="https://github.com/fakhruldeen/Tasleemat/">تسليمات</a>'),
    ("guide links",  "* [القالب القابل للطباعة](04_01_نموذج_قالب.md)\n"
                     "* [موجّه التوليد الذكي](04_01_نموذج.md)"),
    ("table",        "| الدور | الاسم | التوقيع |\n| ---: | ---: | ---: |\n| مدير المشروع | {{الاسم}} | ____ |"),
    ("wrapped item", "*   قطعة أولى تامة\n    وتتمة السطر الذي يعتمد عليها."),
]

# A guide links to files whose stems contain both scripts, so the scanner has to
# treat a link target as an identifier rather than as Latin prose.
GUIDE_LINK = "* [القالب](04_02_09_نموذج_تخطيط_قصص_المستخدم_قالب.md)\n" \
             "* [الدليل](04_02_09_Risk_Mitigation_Action_Plan_Guide.md)"

print("planted defects -- each must be caught")
fails = 0
for name, text in PLANTED:
    probs = scan.check_text(text, name, allow=ALWAYS_OK)
    ok = bool(probs)
    if not ok:
        fails += 1
    kinds = sorted({p[0] for p in probs})
    print(f"  {'FIRED ' if ok else 'MISSED'} {name:<12} {kinds}")

print("\nclean text -- none may be flagged")
for name, text in CLEAN:
    probs = scan.check_text(text, name, allow=ALWAYS_OK)
    if probs:
        fails += 1
        print(f"  FALSE+ {name:<12} {probs}")
    else:
        print(f"  ok     {name:<12}")

probs = scan.check_text(GUIDE_LINK, "guide link", allow=ALWAYS_OK)
if probs:
    fails += 1
    print(f"  FALSE+ {'guide link':<12} {probs}")
else:
    print(f"  ok     {'guide link':<12}")

print("\nallow-list honoured")
text = "Business_Case و lang و default مرجع"
probs = scan.check_text(text, "allow-test", allow=ALWAYS_OK)
print(f"  {'ok' if not probs else 'FALSE+ ' + str(probs)}")
probs = scan.check_text("zzqq مرجع", "not-allowed", allow=ALWAYS_OK)
print(f"  {'ok' if probs else 'MISSED'} unlisted Latin still caught")
if not probs:
    fails += 1

print(f"\n{'ALL OK' if not fails else str(fails) + ' FAILURE(S)'}")
