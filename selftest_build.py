"""Negative-test build.py before it is trusted with a real form.

A generator that has not been negative-tested is the exact thing that shipped
two identity defects through a clean 13-check audit. Each case below plants a
defect and requires the builder to reject it.
"""

import json
import pathlib
import sys
import tempfile

sys.path.insert(0, "/tmp/fast/lib")
import build

EN = """<!--
LLM INSTRUCTIONS:
Fill out the template below.

*   **Sprint Goal:** The goal of the sprint.
*   **Story ID:** Board reference.
-->

<h1 align="center">SPRINT PLANNING LOG</h1>

| **Date Prepared:** {{Current_Date}} | **Prepared By:** {{Prepared_By}} |
| :--- | :--- |

### Sprint Planning Log Entries
<!-- rows -->

| Sprint Goal | Story ID |
| --- | --- |
| [ Add details... ] | [ Add details... ] |

---

### Sign-off and Approvals

| Role | Name | Signature |
| :--- | :--- | :--- |
| **Team Lead** | {{Team_Lead_Name}} | ____ |
"""

TR = {    "ALLOW_HEADINGS": set(),    "SECTIONS": {
        "Sprint Planning Log Entries": "بنود سجل تخطيط|Fee",
        "Sign-off and Approvals": "الاعتماد والتوقيعات",
    },
    "LABELS": {
        "Sprint Goal": "هدفFee",
        "Story ID": "معرّف القصة",
        "Date Prepared": "تاريخ الإعداد",
        "Prepared By": "أعدّها",
        "Sign-off and Approvals": "الاعتماد والتوقيعات",
    },
    "COLUMNS": {
        "Sprint Goal": "هدفFee",
        "Story ID": "معرّف القصة",
        "Role": "الدور",
        "Name": "الاسم",
        "Signature": "التوقيع",
    },
    "ROLES": {"Team Lead": "قائد الفريق"},
    "PLACEHOLDERS": {
        "Current_Date": "التاريخ_الحالي",
        "Prepared_By": "معد_الوثيقة",
        "Team_Lead_Name": "اسم_قائد_الفريق",
        "add_details": "[ أضف التفاصيل... ]",
        "fill": "[ أدخل استجابتك هنا... ]",
    },
}

fails = 0


def expect(name, cond, detail=""):
    global fails
    if not cond:
        fails += 1
    print(f"  {'ok  ' if cond else 'FAIL'} {name} {detail if not cond else ''}")


print("arabic template generation")
out = build.build_ar_template(EN, TR)
expect("no Latin heading remains", "SPRINT PLANNING LOG" in out)
expect("headings translated", "بنود" in out and "الاعتماد والتوقيعات" in out)
expect("columns translated", "معرّف القصة" in out)
expect("role translated", "قائد الفريق" in out)
expect("separator rows preserved", "| :--- | :--- |" in out)
expect("add-details placeholder translated",
       "[ أضف التفاصيل... ]" in out and "[ Add details... ]" not in out)
expect("metadata placeholders translated", "{{التاريخ_الحالي}}" in out
       and "{{Current_Date}}" not in out)

print("\nmust reject: an untranslated heading")
bad = {k: (dict(v) if isinstance(v, dict) else set(v)) for k, v in TR.items()}
del bad["SECTIONS"]["Sign-off and Approvals"]
del bad["LABELS"]["Sign-off and Approvals"]
try:
    build.build_ar_template(EN, bad)
    expect("raises on missing translation", False, "returned silently")
except SystemExit as e:
    expect("raises on missing translation", True, str(e))

print("\nmust reject: guidance missing for a field")
try:
    build.build_json("X", "PMO-00.01", [("S", "L1"), ("S", "L2")], {"L1": "g"})
    expect("raises on missing guidance", False, "returned silently")
except SystemExit:
    expect("raises on missing guidance", True)

print("\njson / csv agreement")
fields = [("S1", "L1"), ("S1", "L2"), ("S2", "L3")]
g = {"L1": "g1", "L2": "g2", "L3": "g3"}
data = build.build_json("اسم", "PMO-00.01", fields, g)
csv_text = build.build_csv(fields, g)
rows = list(__import__("csv").reader(__import__("io").StringIO(csv_text)))
expect("csv header correct", rows[0] == build.CSV_HEADER, str(rows[0]))
expect("csv row count matches", len(rows) == 4, str(len(rows)))
expect("csv sections match json",
       [r[0] for r in rows[1:]] == [v["section"] for v in data["fields"].values()])
expect("csv labels match json",
       [r[1] for r in rows[1:]] == [v["label"] for v in data["fields"].values()])
expect("identity not hardcoded", data["document_reference"] == "PMO-00.01")

print("\npair comparison catches an identity defect")
with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d)
    en = build.build_json("NAME", "PMO-00.01", fields, g)
    ar = dict(en)
    ar["form_name"] = "OTHER NAME"
    ar["document_reference"] = "PMO-00.02"
    (d / "en.json").write_text(json.dumps(en, ensure_ascii=False), encoding="utf-8")
    (d / "ar.json").write_text(json.dumps(ar, ensure_ascii=False), encoding="utf-8")
    n = build.verify_pair(d / "en.json", d / "ar.json", [])
    expect("reports the wrong reference", n >= 1, f"reported {n}")

print(f"\n{'ALL OK' if not fails else str(fails) + ' FAILURE(S)'}")
