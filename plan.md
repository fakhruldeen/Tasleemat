
### Future Enhancement: Document Dependency Mapping (Inputs/Outputs)
**Objective:** Add explicit Predecessor and Successor document dependencies to the form instructions (LLM & Guide) without modifying the actual document templates. This ensures users and AI agents know exactly which forms must be completed prior, and which downstream forms depend on the current one.

**Proposed Architectural Solution:**
1. **LLM Generation Prompts (`.md`):** 
   Update the `> **Alignment:**` section to explicitly categorize dependencies into:
   * `Predecessor Documents (Inputs):` The forms the AI must read/process *before* generating this artifact.
   * `Successor Documents (Outputs):` The downstream forms that will rely on the data generated here.
   * *If the document is independent, explicitly state: "Independent Document (No Predecessors)".*

2. **User Guides (`_Guide.md`):**
   Inject a new dedicated section, `### 6. Document Dependencies`, outlining the exact input/output flow. This will guide human users through the PMBOK sequence (e.g., "You must complete the WBS before generating the Activity List").

3. **Implementation Plan:**
   * Do not touch `_Template.md`, `_Template.csv`, or `.json` schemas.
   * We will leverage the exact PMBOK data ("receives information from..." / "provides information to...") to build accurate lists for each artifact.
   * We will write a Python script to perform a sweeping update across all currently completed artifacts (both English and Arabic) to inject these dependency maps simultaneously.

---

## Backlog: `PMO-templates/` Gap Analysis (assessed 2026-09-30, revised after field-level comparison)

Source: `PMO-templates/` — 28 binary files (13 `.docx`, 13 `.xlsx`, 2 `.pptx`),
all Open PMO (openpmo.org) business/project documents. The repository is
Markdown-first: 297 English `.md` forms plus an Arabic mirror tree, with per-form
`.json`/`.csv` companions. Nothing is copied in as-is; each file is assessed for
**information worth carrying across**.

### Method

First pass judged by filename and concluded "12 already covered". That was
**wrong** — comparing the actual table columns showed most of those forms are
*thinner* than the Open PMO source. Revised verdict:

| Verdict | Files | Meaning |
| --- | --- | --- |
| **Enrich existing form** | 9 | A form exists and is the right home, but is missing specific columns/sections the source has |
| **New form needed** | 10 | Genuine coverage gap, no adequate home |
| **Skip** | 6 | Source adds nothing the repo does not already have |
| **Merge, do not add** | 3 | Would create a third overlapping artefact |

> Principle: prefer **enriching** an existing form over adding a near-duplicate.
> The repo's forms are already deeply integrated (sign-off blocks, placeholder
> variables, PMO doc IDs, Arabic mirrors); a duplicate form doubles the
> translation and audit surface for no gain.

---

### A. Enrich an existing form (9 files) — highest value, lowest risk

| Source | Enrich into | What the source has that the repo form lacks |
| --- | --- | --- |
| `12-project-health-check.docx` + `.xlsx` | `PMO-06.01 Project Status Report` | **Biggest single gap found.** The repo status report has no RAG table at all. Source gives 7 scored dimensions (Governance & Sponsorship, Planning & Control, Risk & Issue, Budget, Stakeholder & Comms, Team & Resources, Benefits) each scored /5 with R/A/G, plus ~18 explicit assessment *criteria questions* per area, plus an overall roll-up. |
| `04-meeting-minutes.docx` | `PMO-05.11 Meeting Minutes` | Repo form has no meeting **metadata** (meeting number, location, chair, minute taker), no **present/apologies** per attendee, no **agenda with a presenter + discussion + decision row per item**, and no **next-meeting scheduling**. |
| `ba-13-requirements-traceability-matrix.xlsx` | `PMO-04.02.04 Requirements Traceability Matrix` | Repo stops at Verification/Validation. Source adds **Design Reference, Test Case ID, Test Status, Implementation Status, Delivery Version, Signed Off** — the design→test→delivery chain. |
| `ba-11-user-story-backlog.xlsx` | `PMO-04.02.08 Product Backlog` | Repo has `Story` as one blob. Source splits **As a / I want to / So that**, and adds **Acceptance Criteria**, **Linked Requirement**, **Tester**. |
| `15-benefits-tracker.xlsx` | `PMO-01.03 Value Realization Register` | Repo has actual + variance but no **trend** and no **period-actuals history** feeding the latest actual (a quarterly actuals tab). |
| `ba-09-stakeholder-analysis-matrix.xlsx` | `PMO-03.05 Stakeholder Analysis` | Repo form is only 5 columns (ID, Name, Interest, Influence, Attitude). Source adds **Current Sentiment, Stakeholder Type** (Champion/Supporter/Sceptic/Blocker), **Engagement Strategy** (power/interest quadrant), **Key Messages, Owner, Next Action, Status** — plus a power/interest **grid guide**. |
| `05-raid-log.xlsx` | `PMO-04.08.02` / `03.03` / `05.01` / `00.03` | All four log tabs are covered. Only the **Dashboard** roll-up (open/high counts across all four categories) is missing. Low value — consider a summary block on the portfolio roadmap instead. |
| `14-capacity-resource-plan.xlsx` | `PMO-00.04 Resource Capacity Matrix` | Repo aggregates by *role or team* per period. Source is **per named individual × 12 months**, with capacity in days/month and an auto **Over / Full / Under** utilisation status. |
| `ba-05-user-story-template.docx` | `PMO-04.02.08 Product Backlog` | A single-story card rather than a backlog. The As-a/I-want/So-that + AC columns are the same enrichment as above; **do not create a separate form.** |

---

### B. New forms needed (10)

| # | Proposed form | Source | Why it is a real gap |
| --- | --- | --- | --- |
| 1 | **Business Requirements Document** | `ba-01-business-requirements-document.docx` | Repo has a requirements *plan* (`04.02.02`) and a requirements *list* (`04.02.03`), but no BRD artefact. Missing concepts: executive summary, business context, stakeholder summary, **in/out of scope**, and the **functional vs non-functional split** (NFRs appear nowhere in the repo). |
| 2 | **Use Case Specification** | `ba-02-use-case-template.docx` | The only use-case form is `PMO-02.04 AI Use Case Canvas`, which is AI-specific. No general use case: actor definitions, primary/secondary flows, pre/post conditions, triggers, summary table. |
| 3 | **Gap Analysis** | `ba-03-gap-analysis.docx` + `ba-10-gap-analysis.xlsx` | No equivalent. Current vs target capability scored 1–5, auto gap, priority, impact, recommended action, owner, status, plus a by-capability summary. `PMO-02.03` has a gap column but is AI-only. |
| 4 | **Current State Assessment** | `ba-08-current-state-assessment.docx` | No equivalent. The structured as-is that feeds gap analysis and the roadmap. Pairs with #3. |
| 5 | **UAT Test Plan** | `ba-06-uat-test-plan.docx` + `ba-12-uat-test-plan.xlsx` | `PMO-06.10` is the **sign-off only** (summary, environment, pass/fail, known defects). Missing: objectives, scope, strategy, **test case register** (scenario, steps, test data, expected result, priority, tester, defect ref), defect management, exit criteria. |
| 6 | **PMO Maturity Assessment** | `pmo-maturity-assessment-word.docx` + `13-pmo-maturity-assessment.xlsx` | No equivalent. 5 dimensions scored 1–5 against target, gap, priority actions, overall maturity band. Distinct from `PMO-02.03` (AI readiness only). |
| 7 | **PMO Governance Framework / PMO Charter** | `09-governance-framework.docx` | `PMO-00.02` is a *program* charter. Nothing covers the **PMO itself**: PMO type taxonomy (Controlling / Supportive / Directive), governance bodies (Portfolio Review Board, Steering Group, PMO Ops, CAB) with members/frequency/chair, stage gates, escalation framework, reporting cadence, standards & compliance. |
| 8 | **Escalation Register** | `16-escalation-register.xlsx` | `PMO-00.03` has an escalation *subsection*; `PMO-05.02` logs decisions. No dedicated register: ref, description, type, raised by, escalated to, date, decision required, decision made, status, date resolved. |
| 9 | **Resource Demand Forecast** | `resource-demand-forecast.xlsx` | `PMO-00.04` is a snapshot. This is a **rolling 6-month forward** view by project/role/grade/month with total FTE, named resource, and Confirmed / At Risk / Gap status — a hiring and prioritisation input. |
| 10 | **Portfolio Status Report** | `portfolio-dashboard.xlsx` + `25-portfolio-status-report.pptx` | The repo has single-project reporting only. No portfolio roll-up: active/on-track/at-risk/critical counts, budget used, benefits on track, period highlights, per-project RAG with key action, top risks across the portfolio. The deck version is the same content — port once, as a form. |

Also worth adding if the same batch is done (lower priority, same family):
**Process Map (As-Is / To-Be)** ← `27-process-map.pptx` — trigger, steps, decision,
handover, pain points, key improvements. Pairs naturally with #3 and #4.

---

### C. Skip — source adds nothing (6)

| Source | Why skip |
| --- | --- |
| `10-post-implementation-review.docx` | Covered by `PMO-07.03 Project/Phase Closeout` (summary, performance, variances, benefits) + `PMO-07.01 Lessons Learned` (14 knowledge areas, risks, defects, vendors). See D. |
| `11-programme-brief.docx` | `PMO-00.02 Program Charter` already covers purpose, objectives, components, benefits, authority, risks. The brief's only addition is strategic-alignment mapping. |
| `ba-10-gap-analysis.xlsx` | Folded into #3 — same content as the `.docx`, and the formulas are a spreadsheet affordance Markdown does not need. |
| `ba-12-uat-test-plan.xlsx` | Folded into #5 — same content as the `.docx`. |
| `13-pmo-maturity-assessment.xlsx` | Folded into #6 — same content as the `.docx`. |
| `04-meeting-minutes.docx` | See A — this is an *enrichment*, not a skip. Listed here only so the count reconciles. |

---

### D. Merge, do not add (3)

- **Post-Implementation Review** — adding it would give the repo *three* closeout
  artefacts (`07.01`, `07.03`, and a PIR). Its one genuinely unique section is
  **Stakeholder Feedback**, which appears in neither `07.01` nor `07.03` — add
  that section to `07.03` and skip the form.
- **Project Health Check** — the 7-dimension RAG scorecard is a *stage gate*, not
  a periodic report. Do not bolt it onto `06.01`; give it its own form (or a
  dedicated `06.x` stage-gate form) so it is not confused with the monthly report.
- **User Story Template vs Product Backlog** — one story per form vs a ranked
  backlog. Enrich `04.02.08`; do not add a form.

---

### E. Sequencing and constraints (when work starts)

1. **Enrichments first (Section A).** Smallest diff, no new doc IDs, no new
   directory, and they close the largest content gaps. Do these before any new form.
2. **Then the new forms (Section B),** grouped so related forms land together:
   gap analysis + current state assessment (they feed each other); UAT test plan
   (pairs with the existing `06.10` sign-off); maturity assessment + governance
   framework (both PMO-level).
3. **Placement decision required before any new form.** These are largely
   business-analysis artefacts and the hierarchy has no `Business_Analysis`
   branch. Either extend `01_Business_and_Value_Delivery` or add a new
   `08_…` branch. **A hierarchy cannot have two branches with the same name** —
   check new category names against each other, not only against the corpus.
4. **Doc IDs** must not collide with the existing `PMO-00.x`–`PMO-07.x` range.
5. **Every new form needs the full artefact set:** form `.md`, `_Guide.md`,
   `_Template.md`, `.json`, `.csv`, plus Arabic mirrors. Every *enriched* form
   needs the same set regenerated, in both languages.
6. **Arabic generation follows the documented pipeline only**
   (`tr_lookup.check()` → `guidance_ar.check()` → `gen_en.py` → `gen_en_md.py`
   → `gen_ar_tpl.py` → `gen_ar_all.py` → `gen_ar_md.py`), in that order.
   `gen_ar_all` reads labels from the generated Arabic template, so running it
   out of order gives a misleading "no guidance for" error.
7. **Every Arabic word must have a committed precedent** in the tree before it is
   typed — this is the check that makes typing Arabic safe. New domain vocabulary
   (RAG, stage gate, UAT, maturity band) will have **no precedent** and must be
   cut from existing shipped files or added to the guidance table first.
8. **Read the rendered output before declaring done.** Every automated check has
   reported false negatives; reading the rendered form is what finds the dropped
   preposition, the duplicate branch name, and the short separator row.
9. Source `.docx`/`.xlsx`/`.pptx` files are **inputs only** — do not commit
   binaries into `forms/`. Record the attribution (Open PMO, Terms of Use) in the
   form's guide if any wording is carried across verbatim.
