#!/usr/bin/env python3
"""tools/stitch_screens_builder.py
Implements the exact Stitch Design System and Screens for the Tasleemat GitHub Pages portal:
- Screen 1 (80e3594dd2de4c31a6b3f5ddd4bed3b5): Arabic Interactive Form Viewer & Editor (FORM-03-01: Project Charter)
- Screen 2 (66631fc7bc5a4c4c91bf53e0e074c0aa): Arabic RTL Templates Catalog & Showcase
- Screen 3 (f699bea80c2c4c0dab54430a6b8e8378): Developer CLI, Python SDK & Bilingual Lexicon
- Screen 4 (f3e5b34906a04a2eb2c99a7262a48939): Stage-Gate Governance & Tailoring Profiles Portal
- Screen 5 (fe772f47175f48ab924c1b977d680f4a): Interactive 102 Deliverables Catalog
- Screen 6 (d5a82735c4a448e9962ccd685a4394ed): GitHub Pages Home & Executive Overview
"""

import os
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"


def get_screen1_form_viewer_html(rel_root: str = "../../") -> str:
    """Generates Stitch Screen 1: Arabic Interactive Form Viewer & Editor for FORM-03-01: Project Charter."""
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl" data-md-color-scheme="default">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>معاينة وتخصيص ميثاق المشروع القياسي | FORM-03-01 | Tasleemat</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="{rel_root}assets/custom.css">
  <link rel="icon" type="image/png" href="{rel_root}img/logo.png">
  <script src="{rel_root}assets/tasleemat_data.js"></script>
  <script src="{rel_root}assets/search.js"></script>
  <script src="{rel_root}assets/explorer.js"></script>
</head>
<body class="bg-slate-50 text-slate-900 min-h-screen flex flex-col font-arabic" dir="rtl">
  <!-- Top Global Header -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur border-b border-slate-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <a href="{rel_root}README_AR.html" class="flex items-center gap-2 text-decoration-none">
          <img src="{rel_root}img/logo.png" alt="Tasleemat Logo" class="h-9 w-auto">
          <span class="font-bold text-lg tracking-tight text-slate-900">تسليمات | <span class="text-blue-700">Tasleemat</span></span>
        </a>
      </div>

      <nav class="hidden md:flex items-center gap-1 font-medium text-sm">
        <a href="{rel_root}README_AR.html" class="px-3 py-2 rounded-md hover:bg-slate-100 text-slate-700 transition">🏠 الرئيسية</a>
        <a href="{rel_root}ar/04_stage_gates_and_governance.html" class="px-3 py-2 rounded-md hover:bg-slate-100 text-slate-700 transition">🚀 بوابات العبور</a>
        <a href="{rel_root}catalog/ar/index.html" class="px-3 py-2 rounded-md hover:bg-slate-100 text-slate-700 transition">📑 كتالوج النماذج</a>
        <a href="{rel_root}forms/ar/form-viewer.html" class="px-3 py-2 rounded-md bg-blue-50 text-blue-700 font-semibold transition">📝 معاينة النماذج</a>
        <a href="{rel_root}LEXICON.html" class="px-3 py-2 rounded-md hover:bg-slate-100 text-slate-700 transition">📖 المعجم</a>
        <a href="{rel_root}TECHNICAL.html" class="px-3 py-2 rounded-md hover:bg-slate-100 text-slate-700 transition">💻 مركز التطوير</a>
      </nav>

      <div class="flex items-center gap-2">
        <button class="tasleemat-search-btn flex items-center gap-2 bg-slate-100 hover:bg-slate-200 text-slate-600 px-3 py-1.5 rounded-lg text-xs font-medium border border-slate-200 transition">
          <span>🔍</span>
          <span class="hidden sm:inline">بحث...</span>
          <kbd class="hidden sm:inline bg-white px-1.5 py-0.5 rounded border text-[10px]">Ctrl K</kbd>
        </button>
        <a href="{rel_root}index.html" class="btn-lang">🇬🇧 English Portal</a>
        <button id="theme-toggle" class="p-2 rounded-lg text-slate-500 hover:bg-slate-100 transition" title="تبديل الوضع الليلي">🌙</button>
      </div>
    </div>
  </header>

  <!-- Main Viewer Content -->
  <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6">
    <!-- 1. Breadcrumbs & Document Header -->
    <div class="mb-4">
      <nav class="flex text-xs text-slate-500 gap-1 items-center mb-2">
        <a href="{rel_root}README_AR.html" class="hover:text-blue-700 transition">الرئيسية</a>
        <span>/</span>
        <a href="{rel_root}catalog/ar/index.html" class="hover:text-blue-700 transition">كتالوج النماذج</a>
        <span>/</span>
        <a href="{rel_root}forms/ar/03_البدء/index.html" class="hover:text-blue-700 transition">03. مرحلة البدء</a>
        <span>/</span>
        <span class="text-slate-800 font-semibold">FORM-03-01: ميثاق المشروع</span>
      </nav>

      <div class="flex flex-col lg:flex-row lg:items-center justify-between gap-4 bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
        <div>
          <div class="flex flex-wrap items-center gap-2 mb-2">
            <span class="badge badge-code">FORM-03-01</span>
            <span class="badge badge-phase">🚀 مرحلة البدء والترخيص</span>
            <span class="badge badge-tier-1">المستوى 1-3 (إلزامي لكافة المشاريع)</span>
            <span class="badge" style="background:#f0fdf4;color:#166534;border:1px solid #bbf7d0;">✓ معتمد ومطابق لـ PMI PMBOK®</span>
          </div>
          <h1 class="text-2xl font-bold text-slate-900 m-0">ميثاق المشروع القياسي المعتمد (Project Charter)</h1>
          <p class="text-xs text-slate-500 mt-1">الرمز المرجعي: <code class="font-mono text-slate-700 font-semibold">TASLEEMAT-FORM-03-01</code> | الإصدار: 2.1 | حالة الوثيقة: معتمدة ومطابقة للمواصفات الحكومية</p>
        </div>

        <!-- Action Bar -->
        <div class="flex flex-wrap items-center gap-2">
          <button onclick="window.print()" class="btn-secondary text-xs">📄 تصدير إلى Word / PDF</button>
          <button onclick="navigator.clipboard.writeText('# ميثاق المشروع القياسي\\n...'); alert('تم نسخ قالب Markdown إلى الحافظة!');" class="btn-secondary text-xs">📋 نسخ قالب Markdown</button>
          <button onclick="populateAIModal()" class="btn-emerald text-xs font-semibold">🤖 توليد تلقائي بالذكاء الاصطناعي (AI Populate)</button>
          <a href="https://github.com/fakhruldeen/Tasleemat/tree/main/forms/ar/03_البدء" target="_blank" class="btn-secondary text-xs">🐙 مزامنة مع GitHub ↗</a>
          <button onclick="alert('تم حفظ المسودة بنجاح في التخزين المحلي للمتصفح!');" class="btn-primary text-xs">💾 حفظ كمسودة</button>
        </div>
      </div>
    </div>

    <!-- 2. Document Meta Bar (4 Stat Cards) -->
    <div class="doc-meta-bar rounded-xl mb-6 shadow-sm">
      <div class="doc-meta-chip">
        <div class="meta-chip-label">راعي المشروع (Project Sponsor)</div>
        <div class="meta-chip-val text-slate-900">معالي رئيس الهيئة / وكيل الوزارة</div>
        <div class="text-[11px] text-slate-400 mt-1">صاحب الصلاحية المالية والترخيص المؤسسي</div>
      </div>
      <div class="doc-meta-chip">
        <div class="meta-chip-label">مدير المشروع (Project Manager)</div>
        <div class="meta-chip-val text-slate-900">م. فهد بن خالد السالم (PMP®)</div>
        <div class="text-[11px] text-slate-400 mt-1">المفوض بإدارة الموارد وتطبيق النطاق</div>
      </div>
      <div class="doc-meta-chip">
        <div class="meta-chip-label">تاريخ الاعتماد الرسمي</div>
        <div class="meta-chip-val text-slate-900">15 رجب 1447هـ (الموافق 2026م)</div>
        <div class="text-[11px] text-slate-400 mt-1">بوابة الاعتماد: Gate 1 (Charter Sign-off)</div>
      </div>
      <div class="doc-meta-chip">
        <div class="meta-chip-label">الميزانية التقديرية المعتمدة</div>
        <div class="meta-chip-val text-emerald-600 font-mono">4,500,000 ر.س (SAR)</div>
        <div class="text-[11px] text-slate-400 mt-1">تشمل احتياطي الطوارئ والاحتياطي الإداري</div>
      </div>
    </div>

    <!-- Layout: 2 Columns (Main Form Sections + Sidebar) -->
    <div class="grid grid-cols-1 lg:grid-cols-4 gap-6">
      <!-- 3. Form Sections (Interactive Accordions) - 3 Columns -->
      <div class="lg:col-span-3 space-y-4">
        <div class="form-viewer-container">
          <!-- Section 1 -->
          <details class="form-section-item" open>
            <summary class="form-section-header">
              <span class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold">1</span>
                <span>مبررات المشروع والأهداف الاستراتيجية (Business Need & Objectives)</span>
              </span>
              <span class="text-xs text-slate-400 font-normal">انقر للتوسيع / الطي ▾</span>
            </summary>
            <div class="form-section-body space-y-4">
              <p class="text-sm text-slate-600">يهدف المشروع إلى أتمتة حوكمة المشاريع الحكومية والتحول الرقمي الشامل لرفع كفاءة الإنفاق وتحقيق مستهدفات رؤية 2030.</p>
              <div class="overflow-x-auto">
                <table>
                  <thead>
                    <tr>
                      <th>الهدف الاستراتيجي</th>
                      <th>المؤشر المستهدف (KPI)</th>
                      <th>المستهدف الرقمي</th>
                      <th>الارتباط ببرامج رؤية 2030</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td class="font-semibold text-slate-800">أتمتة إدارة التسليمات والمراحل</td>
                      <td>نسبة التسليمات المؤتمتة عبر المنصة</td>
                      <td class="font-mono text-blue-600 font-bold">100%</td>
                      <td>برنامج التحول الرقمي الحكومي</td>
                    </tr>
                    <tr>
                      <td class="font-semibold text-slate-800">تقليص مدة دورة تدقيق المخرجات</td>
                      <td>متوسط أيام اعتماد التسليمة (Cycle Time)</td>
                      <td class="font-mono text-emerald-600 font-bold">انخفاض من 14 إلى 3 أيام</td>
                      <td>برنامج تطوير القطاع المالي ورفع الكفاءة</td>
                    </tr>
                    <tr>
                      <td class="font-semibold text-slate-800">الامتثال لحوكمة الذكاء الاصطناعي</td>
                      <td>نسبة النماذج الموثقة ببطاقات Model Cards</td>
                      <td class="font-mono text-purple-600 font-bold">100% امتثال لمعايير سدايا / NIST</td>
                      <td>الاستراتيجية الوطنية للبيانات والذكاء الاصطناعي</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </details>

          <!-- Section 2 -->
          <details class="form-section-item" open>
            <summary class="form-section-header">
              <span class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold">2</span>
                <span>حدود ونطاق العمل العام (High-Level Scope & Boundaries)</span>
              </span>
              <span class="text-xs text-slate-400 font-normal">انقر للتوسيع / الطي ▾</span>
            </summary>
            <div class="form-section-body grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="p-4 bg-emerald-50/50 border border-emerald-200 rounded-lg">
                <h4 class="text-sm font-bold text-emerald-900 mb-2 flex items-center gap-1.5">
                  <span>✓</span> داخل النطاق المعتمد (In Scope)
                </h4>
                <ul class="scope-in-list text-xs space-y-1.5 text-slate-700">
                  <li>بناء وتطوير بوابة إدارة التسليمات ثنائية اللغة (102 تسليمة).</li>
                  <li>توفير حزم النماذج الكاملة بصيغ Markdown وJSON Schema وPython SDK.</li>
                  <li>تنفيذ بوابات العبور الست (Stage-Gates 0-5) والتحقق التلقائي.</li>
                  <li>تدريب مدراء المشاريع وضباط الحوكمة في الهيئة على المنصة.</li>
                </ul>
              </div>

              <div class="p-4 bg-rose-50/50 border border-rose-200 rounded-lg">
                <h4 class="text-sm font-bold text-rose-900 mb-2 flex items-center gap-1.5">
                  <span>✕</span> خارج النطاق لمنع زحف النطاق (Out of Scope)
                </h4>
                <ul class="scope-out-list text-xs space-y-1.5 text-slate-700">
                  <li>تخصيص أنظمة ERP الخارجية مثل SAP وOracle (سيتم عبر واجهات API لاحقة).</li>
                  <li>إدارة العقود القانونية الخارجية والمشتريات خارج نطاق بوابة PMO.</li>
                  <li>تطوير خوارزميات تعلم آلي مخصصة للجهات التابعة خارج الهيئة.</li>
                </ul>
              </div>
            </div>
          </details>

          <!-- Section 3 -->
          <details class="form-section-item" open>
            <summary class="form-section-header">
              <span class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold">3</span>
                <span>المعالم الرئيسية والجدول الزمني التقديري (Key Milestones & Schedule)</span>
              </span>
              <span class="text-xs text-slate-400 font-normal">انقر للتوسيع / الطي ▾</span>
            </summary>
            <div class="form-section-body overflow-x-auto">
              <table>
                <thead>
                  <tr>
                    <th>رمز المعلم</th>
                    <th>المعلم الرئيسي (Milestone)</th>
                    <th>التاريخ المستهدف</th>
                    <th>بوابة المراجعة المرتبطة</th>
                    <th>الحالة</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="font-mono text-xs">M-01</td>
                    <td class="font-semibold">اعتماد دراسة الجدوى وميثاق المشروع</td>
                    <td>15 رجب 1447هـ</td>
                    <td><span class="badge badge-phase">Gate 1: Charter</span></td>
                    <td><span class="text-emerald-600 font-bold">✓ مكتمل</span></td>
                  </tr>
                  <tr>
                    <td class="font-mono text-xs">M-02</td>
                    <td class="font-semibold">اعتماد خط الأساس المتكامل (النطاق، الجدول، التكلفة)</td>
                    <td>30 شعبان 1447هـ</td>
                    <td><span class="badge badge-phase">Gate 2: Baseline</span></td>
                    <td><span class="text-blue-600 font-bold">قيد التنفيذ</span></td>
                  </tr>
                  <tr>
                    <td class="font-mono text-xs">M-03</td>
                    <td class="font-semibold">إطلاق النسخة التجريبية الأولى (MVP)</td>
                    <td>15 شوال 1447هـ</td>
                    <td><span class="badge badge-phase">Gate 3: Execution</span></td>
                    <td><span class="text-slate-400">مجدول</span></td>
                  </tr>
                  <tr>
                    <td class="font-mono text-xs">M-04</td>
                    <td class="font-semibold">اختبارات القبول والتسليم التشغيلي (UAT)</td>
                    <td>30 ذو القعدة 1447هـ</td>
                    <td><span class="badge badge-phase">Gate 4: Handover</span></td>
                    <td><span class="text-slate-400">مجدول</span></td>
                  </tr>
                  <tr>
                    <td class="font-mono text-xs">M-05</td>
                    <td class="font-semibold">إغلاق العقود وتقرير الدروس المستفادة النهائي</td>
                    <td>15 ذو الحجة 1447هـ</td>
                    <td><span class="badge badge-phase">Gate 5: Closeout</span></td>
                    <td><span class="text-slate-400">مجدول</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </details>

          <!-- Section 4 -->
          <details class="form-section-item">
            <summary class="form-section-header">
              <span class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold">4</span>
                <span>مصفوفة أصحاب المصلحة والحوكمة (RACI Governance Matrix)</span>
              </span>
              <span class="text-xs text-slate-400 font-normal">انقر للتوسيع / الطي ▾</span>
            </summary>
            <div class="form-section-body overflow-x-auto">
              <table class="raci-table">
                <thead>
                  <tr>
                    <th>المهمة / المخرج الإداري</th>
                    <th>راعي المشروع (Sponsor)</th>
                    <th>مدير المشروع (PM)</th>
                    <th>فريق التطوير الفني</th>
                    <th>مدير مكتب PMO</th>
                    <th>لجنة المراجعة</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="font-semibold">اعتماد ميثاق المشروع وتخصيص الميزانية</td>
                    <td class="text-center font-bold text-emerald-600">A (المعتمد)</td>
                    <td class="text-center font-bold text-blue-600">R (المسؤول)</td>
                    <td class="text-center text-slate-400">I (مطلع)</td>
                    <td class="text-center font-bold text-purple-600">C (مستشار)</td>
                    <td class="text-center font-bold text-purple-600">C (مستشار)</td>
                  </tr>
                  <tr>
                    <td class="font-semibold">إعداد وتحديث خطط الأساس (WBS، الجدول، التكلفة)</td>
                    <td class="text-center text-slate-400">I</td>
                    <td class="text-center font-bold text-blue-600">R / A</td>
                    <td class="text-center font-bold text-blue-600">R</td>
                    <td class="text-center font-bold text-purple-600">C</td>
                    <td class="text-center text-slate-400">I</td>
                  </tr>
                  <tr>
                    <td class="font-semibold">إدارة التغييرات والتجاوزات المالية (>10%)</td>
                    <td class="text-center font-bold text-emerald-600">A</td>
                    <td class="text-center font-bold text-blue-600">R</td>
                    <td class="text-center text-slate-400">C</td>
                    <td class="text-center font-bold text-purple-600">C</td>
                    <td class="text-center font-bold text-purple-600">C</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </details>

          <!-- Section 5 -->
          <details class="form-section-item">
            <summary class="form-section-header">
              <span class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold">5</span>
                <span>المخاطر الأولية والافتراضات (Initial Risks & Assumptions)</span>
              </span>
              <span class="text-xs text-slate-400 font-normal">انقر للتوسيع / الطي ▾</span>
            </summary>
            <div class="form-section-body overflow-x-auto">
              <table>
                <thead>
                  <tr>
                    <th>رمز الخطر</th>
                    <th>وصف الخطر المحتمل</th>
                    <th>درجة الأثر</th>
                    <th>خطة الاستجابة الأولية</th>
                    <th>مسؤول المتابعة</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td class="font-mono text-xs">RSK-01</td>
                    <td>تأخر تدقيق النماذج ثنائية اللغة من اللجان الاستشارية</td>
                    <td><span class="badge" style="background:#fee2e2;color:#991b1b;">مرتفع</span></td>
                    <td>جدولة جلسات اعتماد أسبوعية متزامنة مع مدير PMO</td>
                    <td>مدير المشروع</td>
                  </tr>
                  <tr>
                    <td class="font-mono text-xs">RSK-02</td>
                    <td>تغييرات في المعايير التنظيمية لأخلاقيات الذكاء الاصطناعي</td>
                    <td><span class="badge" style="background:#fef3c7;color:#92400e;">متوسط</span></td>
                    <td>تضمين معايير NIST AI RMF المرنة والقابلة للتحديث التلقائي</td>
                    <td>مسؤول حوكمة الذكاء الاصطناعي</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </details>

          <!-- Section 6 -->
          <details class="form-section-item" open>
            <summary class="form-section-header">
              <span class="flex items-center gap-2">
                <span class="w-6 h-6 rounded-full bg-blue-100 text-blue-700 text-xs flex items-center justify-center font-bold">6</span>
                <span>قسم الاعتماد والتوقيعات الرسمية (Formal Sign-off & Authorizations)</span>
              </span>
              <span class="text-xs text-slate-400 font-normal">انقر للتوسيع / الطي ▾</span>
            </summary>
            <div class="form-section-body">
              <p class="text-xs text-slate-500 mb-3">توقيع الأطراف المعنية يفوض رسميًا استخدام الموارد المالية والبشرية المخصصة للمشروع وفق ما ورد في هذا الميثاق:</p>
              <div class="signoff-grid">
                <div class="signoff-box border-emerald-300 bg-emerald-50/30">
                  <div class="signoff-role">راعي المشروع (Project Sponsor)</div>
                  <div class="text-xs font-semibold text-slate-800 mt-1">معالي رئيس الهيئة</div>
                  <div class="signoff-status text-emerald-700">✓ تم التوقيع والاعتماد الرقمي</div>
                  <div class="text-[10px] text-slate-400 mt-2 font-mono">HASH: 8F7E21...9B02 (15/07/1447H)</div>
                </div>

                <div class="signoff-box border-blue-300 bg-blue-50/30">
                  <div class="signoff-role">مدير مكتب PMO (PMO Director)</div>
                  <div class="text-xs font-semibold text-slate-800 mt-1">د. عبدالله بن سليمان المنصور</div>
                  <div class="signoff-status text-emerald-700">✓ تم التدقيق والتحقق المؤسسي</div>
                  <div class="text-[10px] text-slate-400 mt-2 font-mono">HASH: 3A1C90...4D11 (14/07/1447H)</div>
                </div>

                <div class="signoff-box border-slate-300 bg-slate-50">
                  <div class="signoff-role">المدير المالي التنفيذي (CFO)</div>
                  <div class="text-xs font-semibold text-slate-800 mt-1">أ. سامي بن أحمد الشريف</div>
                  <div class="signoff-status text-emerald-700">✓ تم حجز الميزانية وتأكيد التدفقات</div>
                  <div class="text-[10px] text-slate-400 mt-2 font-mono">HASH: 6C9B44...11F7 (15/07/1447H)</div>
                </div>
              </div>
            </div>
          </details>
        </div>
      </div>

      <!-- 4. Context Sidebar - 1 Column -->
      <div class="lg:col-span-1 space-y-4">
        <!-- Chapters Index -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
          <h3 class="text-sm font-bold text-slate-900 mb-3 flex items-center gap-1.5">
            <span>📑</span> فهرس أقسام الوثيقة
          </h3>
          <ul class="text-xs space-y-2 text-slate-600">
            <li class="flex items-center justify-between font-semibold text-blue-700">
              <span>1. مبررات المشروع</span>
              <span class="text-[10px] bg-blue-100 px-1.5 py-0.5 rounded">مكتمل</span>
            </li>
            <li class="flex items-center justify-between">
              <span>2. حدود ونطاق العمل</span>
              <span class="text-[10px] bg-emerald-100 text-emerald-700 px-1.5 py-0.5 rounded">مكتمل</span>
            </li>
            <li class="flex items-center justify-between">
              <span>3. المعالم الرئيسية</span>
              <span class="text-[10px] bg-emerald-100 text-emerald-700 px-1.5 py-0.5 rounded">مكتمل</span>
            </li>
            <li class="flex items-center justify-between">
              <span>4. مصفوفة RACI</span>
              <span class="text-[10px] bg-emerald-100 text-emerald-700 px-1.5 py-0.5 rounded">مكتمل</span>
            </li>
            <li class="flex items-center justify-between">
              <span>5. المخاطر والافتراضات</span>
              <span class="text-[10px] bg-emerald-100 text-emerald-700 px-1.5 py-0.5 rounded">مكتمل</span>
            </li>
            <li class="flex items-center justify-between">
              <span>6. التوقيعات الرسمية</span>
              <span class="text-[10px] bg-emerald-100 text-emerald-700 px-1.5 py-0.5 rounded">معتمد</span>
            </li>
          </ul>
        </div>

        <!-- AI Assistant Widget -->
        <div class="bg-gradient-to-br from-slate-900 to-indigo-950 text-white p-4 rounded-xl border border-indigo-800 shadow-md">
          <div class="flex items-center gap-2 mb-2">
            <span class="text-base">🤖</span>
            <h3 class="text-xs font-bold tracking-tight">مساعد تسليمات الذكي (AI Assistant)</h3>
          </div>
          <p class="text-[11px] text-slate-300 leading-relaxed mb-3">
            المساعد مدرب على معايير PMBOK وأدلة هيئة الحكومة الرقمية للمساعدة في صياغة الأهداف وتحديد المخاطر.
          </p>
          <button onclick="suggestOKRs()" class="w-full text-xs font-semibold py-2 px-3 bg-indigo-600 hover:bg-indigo-500 rounded-lg transition text-center mb-2">
            ✨ اقتراح أهداف متوافقة مع OKR
          </button>
          <div id="ai-response-box" class="hidden text-[11px] p-2 bg-slate-800/80 rounded border border-indigo-500/30 text-indigo-200 mt-2"></div>
        </div>

        <!-- Related Artifacts -->
        <div class="bg-white p-4 rounded-xl border border-slate-200 shadow-sm">
          <h3 class="text-sm font-bold text-slate-900 mb-2 flex items-center gap-1.5">
            <span>🔗</span> النماذج المرتبطة
          </h3>
          <ul class="text-xs space-y-2 text-slate-600">
            <li>
              <a href="{rel_root}catalog/ar/index.html" class="hover:text-blue-700 font-medium">FORM-03-02: سجل أصحاب المصلحة</a>
            </li>
            <li>
              <a href="{rel_root}catalog/ar/index.html" class="hover:text-blue-700 font-medium">FORM-03-03: سجل الافتراضات والقيود</a>
            </li>
            <li>
              <a href="{rel_root}catalog/ar/index.html" class="hover:text-blue-700 font-medium">FORM-04-03: خطة إدارة النطاق (WBS)</a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </main>

  <footer class="bg-slate-900 text-slate-400 text-xs py-8 border-t border-slate-800">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4">
      <div>
        <p class="font-medium text-slate-300">منظومة تسليمات لإدارة المشاريع المؤسسية (Tasleemat PMO)</p>
        <p class="text-slate-500 mt-1">PMI PMBOK® 6th, 7th & 8th Edition Compliant | ISO 21500 & OKF v0.2 Standard</p>
      </div>
      <div class="flex items-center gap-4">
        <a href="https://github.com/fakhruldeen/Tasleemat" target="_blank" class="hover:text-white transition">مستودع GitHub</a>
        <a href="{rel_root}LEXICON.html" class="hover:text-white transition">المعجم الموحد</a>
        <a href="{rel_root}TECHNICAL.html" class="hover:text-white transition">دليل المطورين</a>
      </div>
    </div>
  </footer>

  <script>
    function suggestOKRs() {{
      const box = document.getElementById("ai-response-box");
      box.classList.remove("hidden");
      box.innerHTML = "<strong>💡 مقترح المساعد الذكي:</strong><br/>1. خفض التباين في الجدول الزمني (SV) بنسبة 25%.<br/>2. تحقيق معدل رضا المستفيدين (CSAT) لا يقل عن 92% عند تسليم المعلم M-03.";
    }}
    function populateAIModal() {{
      alert("تم تفعيل أمر التوليد الذكي (Tasleemat AI Engine) لتعبئة حقول الميثاق تلقائياً بناءً على بيانات دراسة الجدوى!");
    }}
  </script>
</body>
</html>"""


def get_screen4_governance_md() -> str:
    """Generates Stitch Screen 4: Stage-Gate Governance & Tailoring Profiles Portal."""
    return """<!--
---
type: Guide
---
-->

<div class="hero-wrapper">
  <div class="hero-tag">
    <span class="pulse-dot"></span> Stage-Gate Governance & Tailoring Architecture • PMI PMBOK® 6/7/8 & ISO 21500
  </div>
  <h1 class="hero-title">Tasleemat Stage-Gate Governance & Tailoring Profiles</h1>
  <div class="hero-title-ar">منظومة بوابات العبور الحوكمية ومستويات تخصيص المشاريع</div>
  <p class="hero-subtitle">
    Structured gatekeeper decision checkpoints (Gate 0 Idea to Gate 5 Closeout) paired with 4 scalable project sizing tiers to ensure auditability, rigorous fiscal control, and zero governance bloat.
  </p>
  <div class="hero-actions">
    <a href="#six-gates" class="btn-primary">🚪 Inspect 6 Stage-Gates</a>
    <a href="#tailoring-matrix" class="btn-secondary">⚖️ Tailoring Tiers Matrix</a>
    <a href="#calculator" class="btn-emerald">🧮 Launch Sizing Calculator</a>
  </div>
</div>

---

<h2 id="executive-framework">🏛️ 1. Executive Governance Framework</h2>

Every project passing through Tasleemat undergoes rigorous stage-gate governance. Each gate represents a formal review where a designated governing authority evaluates deliverables and decides between **Three Gate Outcomes**:

1. 🟢 **Proceed (Go):** Deliverables satisfy exit criteria. Authorized to release subsequent tranche and advance to the next lifecycle phase.
2. 🟡 **Conditional Approval (Go with Actions):** Minor non-critical deficiencies noted. Conditional approval granted subject to remedial actions completed within 14 calendar days.
3. 🔴 **Reject / Terminate (No-Go):** Critical variance or strategic misalignment. Project is halted, redirected for baseline replanning, or formally closed.

```mermaid
flowchart LR
    G0["<b>Gate 0</b><br/>Concept Review"] -->|Approved| G1["<b>Gate 1</b><br/>Charter & Auth"]
    G1 -->|Approved| G2["<b>Gate 2</b><br/>Baseline Approval"]
    G2 -->|Approved| G3["<b>Gate 3</b><br/>Execution Health"]
    G3 -->|Approved| G4["<b>Gate 4</b><br/>Operational UAT"]
    G4 -->|Approved| G5["<b>Gate 5</b><br/>Final Closeout"]
    
    style G0 fill:#f0fdf4,stroke:#10b981,stroke-width:2px
    style G1 fill:#eff6ff,stroke:#2563eb,stroke-width:2px
    style G2 fill:#eff6ff,stroke:#2563eb,stroke-width:2px
    style G3 fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style G4 fill:#f0fdf4,stroke:#10b981,stroke-width:2px
    style G5 fill:#f8fafc,stroke:#0b132b,stroke-width:2px
```

---

<h2 id="six-gates">🚪 2. Interactive 6 Stage-Gates Visual Inspector</h2>

<div class="space-y-6">

  <!-- Gate 0 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 0: Strategic Concept & Portfolio Alignment</span>
      <span class="badge badge-code">Phase 00 & 01</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">Authority: Investment Review Board / CFO</span>
    </div>
    <h3 class="dash-card-title">بوابة 0: دراسة الفكرة والمواءمة الاستراتيجية</h3>
    <p class="dash-card-desc">
      Validates strategic alignment, OKR linkage, high-level feasibility, and preliminary ROI before allocating capital or assigning project teams.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Initiative directly aligns with corporate OKRs or Vision 2030 strategic objectives.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Business Case contains quantified cost of inaction and preliminary NPV/IRR analysis.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Initial feasibility study verifies technical and legal compliance.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-00-06: OKR Alignment</span>
      <span class="badge badge-code">FORM-01-01: Business Case</span>
      <span class="badge badge-code">FORM-01-02: Feasibility Study</span>
    </div>
  </div>

  <!-- Gate 1 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 1: Project Charter & Authorization</span>
      <span class="badge badge-code">Phase 02 & 03</span>
      <span class="badge" style="background:#eff6ff;color:#1e3a8a;">Authority: Executive Sponsor & PMO Director</span>
    </div>
    <h3 class="dash-card-title">بوابة 1: ميثاق المشروع والترخيص الرسمي</h3>
    <p class="dash-card-desc">
      Formally authorizes project existence, assigns the Project Manager, establishes high-level scope boundaries, and defines the initial budget envelope.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Signed Project Charter by Executive Sponsor and PMO Director.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Governance tier selected (Tier 1-4) with tailored deliverable bundle.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Initial stakeholder register and assumption log established.</span></label>
    </div>
    <div class="dash-card-actions">
      <a href="forms/ar/form-viewer.html" class="card-btn" style="background:#0d9488;color:#fff!important;">🎯 معاينة تفاعلية (FORM-03-01)</a>
      <span class="badge badge-code">FORM-03-01: Project Charter</span>
      <span class="badge badge-code">FORM-03-04: Stakeholder Register</span>
      <span class="badge badge-code">FORM-02-01: Tailoring Plan</span>
    </div>
  </div>

  <!-- Gate 2 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 2: Integrated Baselines Approval</span>
      <span class="badge badge-code">Phase 04</span>
      <span class="badge" style="background:#eff6ff;color:#1e3a8a;">Authority: PMO Steering Committee</span>
    </div>
    <h3 class="dash-card-title">بوابة 2: اعتماد خطوط الأساس المتكاملة</h3>
    <p class="dash-card-desc">
      Rigorous lock-in of Scope Baseline (WBS), Critical Path Schedule, Cost Baseline, and Risk Response Plans before major expenditure.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>100% WBS Work Package coverage matching agreed scope dictionary.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Cost baseline includes validated contingency and management reserves.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Risk Register contains proactive response plans for all High/Critical risks.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-04-03: Scope & WBS</span>
      <span class="badge badge-code">FORM-04-12: Schedule Baseline</span>
      <span class="badge badge-code">FORM-04-15: Cost Baseline</span>
      <span class="badge badge-code">FORM-04-18: Risk Register</span>
    </div>
  </div>

  <!-- Gate 3 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 3: Execution Mid-Stage Health Check</span>
      <span class="badge badge-code">Phase 05 & 06</span>
      <span class="badge" style="background:#fef3c7;color:#92400e;">Authority: PMO Performance Board</span>
    </div>
    <h3 class="dash-card-title">بوابة 3: مراقبة الأداء وتحليل القيمة المكتسبة</h3>
    <p class="dash-card-desc">
      Continuous monitoring using Earned Value Analysis (EVA): verifies Cost Performance Index (CPI >= 0.95) and Schedule Performance Index (SPI >= 0.95).
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>SPI and CPI within acceptable control thresholds (>= 0.95).</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>All major issues have assigned owners and active remediation dates.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Change requests vetted through formal Change Control Board (CCB).</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-06-03: Earned Value Report</span>
      <span class="badge badge-code">FORM-05-03: Issue Log</span>
      <span class="badge badge-code">FORM-05-04: Change Request</span>
    </div>
  </div>

  <!-- Gate 4 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 4: Operational Handover & UAT</span>
      <span class="badge badge-code">Phase 06 & 07</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">Authority: Operations Director & End-User Sponsor</span>
    </div>
    <h3 class="dash-card-title">بوابة 4: القبول والتسليم التشغيلي</h3>
    <p class="dash-card-desc">
      Formal transition of project deliverables into business-as-usual (BAU) operations, warranty signoffs, and training sign-off.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>100% user acceptance testing (UAT) test cases verified and signed off.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Operational handover protocols and SLA agreements executed.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Operations team fully trained with operational manuals delivered.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-06-05: Quality Acceptance</span>
      <span class="badge badge-code">FORM-07-02: Operational Handover</span>
    </div>
  </div>

  <!-- Gate 5 Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-phase">Gate 5: Contract Closeout & Value Realization</span>
      <span class="badge badge-code">Phase 07</span>
      <span class="badge" style="background:#f8fafc;color:#0b132b;">Authority: Executive Sponsor & Audit Committee</span>
    </div>
    <h3 class="dash-card-title">بوابة 5: الإغلاق النهائي وتقييم الفوائد</h3>
    <p class="dash-card-desc">
      Final contract reconciliation, vendor evaluations, lessons learned archive, and post-implementation review (PIR) schedule.
    </p>
    <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg text-xs space-y-2 mb-3">
      <div class="font-bold text-slate-800">📋 Auditable Gate Checklist:</div>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>All procurement contracts closed with final settlements executed.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" checked class="rounded text-teal-600"> <span>Comprehensive Lessons Learned Register archived in organizational repository.</span></label>
      <label class="flex items-center gap-2 cursor-pointer"><input type="checkbox" class="rounded text-teal-600"> <span>Post-Implementation Review (PIR) calendar established with Value Lead.</span></label>
    </div>
    <div class="dash-card-actions">
      <span class="badge badge-code">FORM-07-01: Lessons Learned</span>
      <span class="badge badge-code">FORM-07-03: Contract Closeout</span>
      <span class="badge badge-code">FORM-07-05: Post-Implementation Review</span>
    </div>
  </div>

</div>

---

<h2 id="tailoring-matrix">⚖️ 3. Tailoring Profiles Matrix (4 Project Sizing Tiers)</h2>

| Tier | Project Profile | Artifact Bundle | Governance Cadence | Required Approvals |
| :--- | :--- | :---: | :--- | :--- |
| **Tier 1: Micro / Small** | Budget < $100K, Duration < 3 mo, Low Risk | **5 Core Artifacts** | Bi-weekly flash report | Project Sponsor only |
| **Tier 2: Standard Core** | Budget $100K–$1M, 3–12 mo, Medium Risk | **18 Artifacts** | Monthly PMO review | Sponsor & PMO Lead |
| **Tier 3: Enterprise Transformation** | Budget > $1M, Multi-vendor, High Impact | **45+ Artifacts** | Formal Steering Committee | Sponsor, PMO, CFO, SteerCo |
| **Tier 4: Agile / AI Iterative** | Machine learning, SaaS, Fast sprints | **25 Artifacts** | Sprint review & Model audit | Product Owner & AI Ethics Lead |

---

<h2 id="calculator">🧮 4. Interactive Project Tailoring Calculator</h2>

<div class="tailoring-calculator-card">
  <div class="calc-grid">
    <div class="calc-field">
      <label>Project Budget Envelope:</label>
      <select id="calc-budget" class="calc-select" onchange="runTailoringCalc()">
        <option value="1">Small (Under $100K / 400K SAR)</option>
        <option value="2" selected>Medium ($100K – $1M / 400K - 4M SAR)</option>
        <option value="3">Enterprise (Over $1M / 4M+ SAR)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Estimated Project Duration:</label>
      <select id="calc-duration" class="calc-select" onchange="runTailoringCalc()">
        <option value="1">Under 3 Months</option>
        <option value="2" selected>3 to 12 Months</option>
        <option value="3">Over 1 Year (Multi-Year)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Delivery Methodology:</label>
      <select id="calc-method" class="calc-select" onchange="runTailoringCalc()">
        <option value="predictive" selected>Traditional / Predictive (Waterfall)</option>
        <option value="agile">Agile / Scrum / Kanban</option>
        <option value="ai">AI / Machine Learning / Data Science</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Regulatory & Compliance Level:</label>
      <select id="calc-reg" class="calc-select" onchange="runTailoringCalc()">
        <option value="standard" selected>Standard Enterprise Compliance</option>
        <option value="high">High Regulatory (Gov / Financial / DGA)</option>
      </select>
    </div>
  </div>

  <div id="calc-result" class="calc-result-box">
    <div>
      <div class="text-xs text-emerald-800 font-bold uppercase tracking-wider">Recommended Governance Profile:</div>
      <div id="calc-tier-title" class="text-lg font-bold text-emerald-950 mt-1">Tier 2: Standard Core Pack (18 Artifacts)</div>
      <div id="calc-tier-desc" class="text-xs text-emerald-800 mt-1">Full Baselines (Scope, Schedule, Cost, Risk, Communications) with formal stage-gate approval at Gates 1, 2, and 4.</div>
    </div>
    <div>
      <span id="calc-cli-btn" class="inline-flex items-center gap-2 px-3 py-2 bg-slate-900 text-slate-100 font-mono text-xs rounded-lg border border-slate-700 shadow-sm cursor-pointer" onclick="copyCalcCLI()">
        <span class="text-emerald-400">$</span> <span id="calc-cli-cmd">tasleemat init --tier 2 --pack standard --lang both</span>
        <span class="text-[10px] bg-slate-800 text-slate-400 px-1 py-0.5 rounded">📋 Copy</span>
      </span>
    </div>
  </div>
</div>

<script>
function runTailoringCalc() {
  const budget = parseInt(document.getElementById("calc-budget").value);
  const duration = parseInt(document.getElementById("calc-duration").value);
  const method = document.getElementById("calc-method").value;
  const reg = document.getElementById("calc-reg").value;

  let tier = 2;
  let pack = "standard";
  let title = "Tier 2: Standard Core Pack (18 Artifacts)";
  let desc = "Full Baselines (Scope, Schedule, Cost, Risk, Communications) with formal stage-gate approval at Gates 1, 2, and 4.";

  if (method === "ai") {
    tier = 4;
    pack = "ai";
    title = "Tier 4: AI & Machine Learning Governance (25 Artifacts)";
    desc = "AI Canvas, Model Cards, Bias Assessment, NIST AI RMF compliance, and iterative MLOps monitoring.";
  } else if (method === "agile" && budget < 3) {
    tier = 4;
    pack = "agile";
    title = "Tier 4: Agile / Lean Iterative Pack (25 Artifacts)";
    desc = "Sprint Backlog, Retrospectives, Flow Metrics, Product Vision, and Definition of Done checklists.";
  } else if (budget === 3 || reg === "high") {
    tier = 3;
    pack = "enterprise";
    title = "Tier 3: Enterprise Transformation Pack (45+ Artifacts)";
    desc = "Full institutional governance: Multi-vendor procurement, ESG compliance, steering committee signoffs, and independent audit trails.";
  } else if (budget === 1 && duration === 1) {
    tier = 1;
    pack = "lean";
    title = "Tier 1: Micro / Small Fast-Track (5 Core Artifacts)";
    desc = "Charter, Action Log, Milestones Schedule, Status Report, and Operational Closeout.";
  }

  document.getElementById("calc-tier-title").textContent = title;
  document.getElementById("calc-tier-desc").textContent = desc;
  document.getElementById("calc-cli-cmd").textContent = `tasleemat init --tier ${tier} --pack ${pack} --lang both`;
}

function copyCalcCLI() {
  const cmd = document.getElementById("calc-cli-cmd").textContent;
  navigator.clipboard.writeText(cmd);
  alert("Copied to clipboard: " + cmd);
}
</script>
"""


def get_screen3_developer_md() -> str:
    """Generates Stitch Screen 3: Developer CLI, Python SDK & Bilingual Lexicon."""
    return """<!--
---
type: Guide
---
-->

<div class="hero-wrapper">
  <div class="hero-tag">
    <span class="pulse-dot"></span> Developer Manual, CLI Scaffolder & Python SDK • OKF Compliant
  </div>
  <h1 class="hero-title">Tasleemat Developer Tooling, Python SDK & Bilingual Lexicon</h1>
  <div class="hero-title-ar">دليل المطورين، أدوات سطر الأوامر (CLI)، وحزمة بايثون، والمعجم الموحد</div>
  <p class="hero-subtitle">
    Programmatic scaffolding, friction-free schema validation, AI agent integration via <code>tasleemat.ai</code>, and standardized bilingual project management terminology.
  </p>
  <div class="hero-actions">
    <span class="inline-flex items-center gap-2 px-3 py-2 bg-slate-900 text-slate-100 font-mono text-xs rounded-lg border border-slate-700 shadow-sm cursor-pointer" onclick="navigator.clipboard.writeText('pip install tasleemat'); alert('Copied: pip install tasleemat');">
      <span class="text-emerald-400">$</span> pip install tasleemat
      <span class="text-[10px] bg-slate-800 text-slate-400 px-1 py-0.5 rounded">📋 Copy</span>
    </span>
    <a href="https://pypi.org/project/tasleemat/" target="_blank" class="btn-secondary">📦 PyPI Release ↗</a>
    <a href="#cli-builder" class="btn-emerald">⚡ Interactive CLI Builder</a>
    <a href="#lexicon" class="btn-secondary">📖 Master Lexicon Glossary</a>
  </div>
</div>

---

<h2 id="installation">📦 1. Installation & Environment Verification</h2>

```bash
# Install the official global package
pip install --upgrade tasleemat

# Verify CLI version and environment readiness
tasleemat --version
tasleemat doctor
```

---

<h2 id="cli-builder">⚡ 2. Interactive CLI Command Generator</h2>

Use the interactive generator below to build customized scaffolding commands:

<div class="tailoring-calculator-card">
  <div class="calc-grid">
    <div class="calc-field">
      <label>Governance Tier:</label>
      <select id="cli-gen-tier" class="calc-select" onchange="updateCLICmd()">
        <option value="1">Tier 1: Micro / Small (5 Artifacts)</option>
        <option value="2" selected>Tier 2: Standard Core (18 Artifacts)</option>
        <option value="3">Tier 3: Enterprise Transformation (45+ Artifacts)</option>
        <option value="4">Tier 4: Agile / AI Iterative (25 Artifacts)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Package Pack Type:</label>
      <select id="cli-gen-pack" class="calc-select" onchange="updateCLICmd()">
        <option value="standard" selected>Standard Predictive / PMBOK</option>
        <option value="agile">Agile / Scrum / Kanban</option>
        <option value="gov">Saudi Gov / DGA Digital Transformation</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Artifact Language:</label>
      <select id="cli-gen-lang" class="calc-select" onchange="updateCLICmd()">
        <option value="ar" selected>🇸🇦 Arabic Standardized (العربية)</option>
        <option value="en">🇬🇧 English Only</option>
        <option value="both">🌐 Bilingual Synchronized (Both)</option>
      </select>
    </div>

    <div class="calc-field">
      <label>Project Directory Name:</label>
      <input type="text" id="cli-gen-name" class="calc-select" value="منصة_التحول_الرقمي" oninput="updateCLICmd()" />
    </div>
  </div>

  <div class="cli-terminal-window">
    <div class="terminal-header">
      <div class="terminal-dots">
        <span class="terminal-dot dot-red"></span>
        <span class="terminal-dot dot-yellow"></span>
        <span class="terminal-dot dot-green"></span>
      </div>
      <span class="terminal-title">bash — tasleemat cli scaffolder</span>
      <button class="card-btn" style="padding: 2px 8px; font-size: 11px;" onclick="copyLiveCLI()">📋 Copy Command</button>
    </div>
    <div class="terminal-body">
      <div class="flex items-center gap-2">
        <span class="terminal-prompt">$</span>
        <span id="live-cli-display" class="terminal-cmd">tasleemat init --tier 2 --pack standard --lang ar --name "منصة_التحول_الرقمي"</span>
      </div>
      <div class="terminal-output">
        <span class="text-slate-400">[INFO] Initializing Tasleemat project directory structure...</span><br>
        <span class="text-slate-400">[INFO] Generating 18 synchronized artifact bundles in Arabic (RTL)...</span><br>
        <span class="terminal-badge-ok">[OK] Successfully generated project scaffold! Ready for delivery.</span>
      </div>
    </div>
  </div>
</div>

<script>
function updateCLICmd() {
  const tier = document.getElementById("cli-gen-tier").value;
  const pack = document.getElementById("cli-gen-pack").value;
  const lang = document.getElementById("cli-gen-lang").value;
  const name = document.getElementById("cli-gen-name").value || "my_pmo_project";

  const cmd = `tasleemat init --tier ${tier} --pack ${pack} --lang ${lang} --name "${name}"`;
  document.getElementById("live-cli-display").textContent = cmd;
}

function copyLiveCLI() {
  const cmd = document.getElementById("live-cli-display").textContent;
  navigator.clipboard.writeText(cmd);
  alert("Copied to clipboard: " + cmd);
}
</script>

---

<h2 id="python-sdk">🤖 3. Programmatic Python SDK (`tasleemat.ai`)</h2>

Automate document drafting and LLM verification using the Python SDK:

```python
from tasleemat.ai import AIClient

# 1. Initialize client (supports Gemini, OpenAI, Claude, or local mock engines)
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# 2. Automated artifact population using PMI PMBOK principle grounding
charter_md = client.generate_deliverable(
    code="FORM-03-01",
    lang="ar",
    project_context={
        "name": "منصة الحوكمة الرقمية",
        "sponsor": "معالي رئيس الهيئة",
        "budget": "4,500,000 SAR",
        "strategic_goal": "أتمتة مخرجات PMO وتحقيق مستهدفات التحول الرقمي 2030"
    }
)

print(charter_md)
```

---

<h2 id="lexicon">📖 4. Bilingual PMO Terminology Lexicon & Search</h2>

Searchable glossary of core project management terminology aligned with PMI PMBOK® Lexicon and Arab regional standards:

<div class="mb-4">
  <input type="text" id="lex-search-input" class="dash-search-box" placeholder="🔍 ابحث في المعجم (مثال: الخط الأساسي، WBS، EVA، المخاطر)..." oninput="filterLexicon()" />
</div>

<div class="overflow-x-auto">
  <table id="lex-table">
    <thead>
      <tr>
        <th>English Term</th>
        <th>المصطلح العربي المعتمد</th>
        <th>Definition & Context (التعريف والسياق)</th>
        <th>Lifecycle Domain</th>
        <th>PMBOK Reference</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="font-bold">Baseline</td>
        <td class="font-bold text-blue-700">الخط الأساسي</td>
        <td>The approved version of a work product, schedule, or cost envelope that can only be changed through formal change control.</td>
        <td><span class="badge badge-phase">Planning</span></td>
        <td>PMBOK® 6/7/8</td>
      </tr>
      <tr>
        <td class="font-bold">Work Breakdown Structure (WBS)</td>
        <td class="font-bold text-blue-700">هيكل تجزئة العمل</td>
        <td>A hierarchical decomposition of the total scope of work to be carried out by the project team.</td>
        <td><span class="badge badge-phase">Scope (04.02)</span></td>
        <td>ISO 21502 / PMBOK®</td>
      </tr>
      <tr>
        <td class="font-bold">Earned Value Analysis (EVA)</td>
        <td class="font-bold text-blue-700">تحليل القيمة المكتسبة</td>
        <td>Methodology that combines scope, schedule, and resource measurements to assess project performance and progress.</td>
        <td><span class="badge badge-phase">Monitoring (06)</span></td>
        <td>ANSI/EIA-748</td>
      </tr>
      <tr>
        <td class="font-bold">Stage-Gate Review</td>
        <td class="font-bold text-blue-700">مراجعة بوابة المرحلة</td>
        <td>A formal checkpoint at the end of a phase where a decision is made to continue, conditionally proceed, or terminate.</td>
        <td><span class="badge badge-phase">Governance (00-07)</span></td>
        <td>PMI Standard</td>
      </tr>
      <tr>
        <td class="font-bold">Deliverable</td>
        <td class="font-bold text-blue-700">المُسلَّم / التسليمة القياسية</td>
        <td>Any unique and verifiable product, result, or capability to perform a service that is required to be produced to complete a phase.</td>
        <td><span class="badge badge-phase">All Lifecycle</span></td>
        <td>OKF / PMBOK®</td>
      </tr>
      <tr>
        <td class="font-bold">Stakeholder Engagement</td>
        <td class="font-bold text-blue-700">إشراك أصحاب المصلحة</td>
        <td>Strategies and actions to involve individuals and groups in project decisions and execution based on interests and influence.</td>
        <td><span class="badge badge-phase">Initiating (03)</span></td>
        <td>PMBOK® Principle 3</td>
      </tr>
      <tr>
        <td class="font-bold">Risk Appetite</td>
        <td class="font-bold text-blue-700">القابلية للمخاطر</td>
        <td>The degree of uncertainty an organization or individual is willing to accept in anticipation of a reward.</td>
        <td><span class="badge badge-phase">Risk (04.08)</span></td>
        <td>ISO 31000</td>
      </tr>
      <tr>
        <td class="font-bold">Contingency Reserve</td>
        <td class="font-bold text-blue-700">احتياطي الطوارئ</td>
        <td>Time or budget allocated within the cost baseline for known-unknown risks managed by the Project Manager.</td>
        <td><span class="badge badge-phase">Cost (04.04)</span></td>
        <td>PMBOK® 6th/7th</td>
      </tr>
    </tbody>
  </table>
</div>

<script>
function filterLexicon() {
  const query = document.getElementById("lex-search-input").value.toLowerCase();
  const rows = document.querySelectorAll("#lex-table tbody tr");
  rows.forEach(r => {
    const text = r.textContent.toLowerCase();
    r.style.display = text.includes(query) ? "" : "none";
  });
}
</script>

---

<h2 id="citation">📚 5. Academic Citation & Zenodo DOI</h2>

If you utilize the Tasleemat framework or dataset in enterprise research, audit manuals, or academia, please cite:

<div class="dash-card">
  <div class="flex items-center justify-between mb-3">
    <div class="flex items-center gap-2">
      <span class="badge badge-code">DOI: 10.5281/zenodo.23193523</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">Open Access • MIT License</span>
    </div>
    <div class="flex gap-2">
      <button class="card-btn" onclick="copyBibTeX()">📋 Copy BibTeX</button>
      <button class="card-btn" onclick="copyAPA()">📋 Copy APA</button>
    </div>
  </div>
  <pre class="bg-slate-900 text-slate-100 p-4 rounded-lg text-xs font-mono overflow-x-auto"><code id="bibtex-code">@software{fakhruldeen_tasleemat_2026,
  author       = {Fakhruldeen, Mohamed (Fouad)},
  title        = {Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework},
  year         = {2026},
  version      = {v2.0.2},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23193523},
  url          = {https://doi.org/10.5281/zenodo.23193523}
}</code></pre>
</div>

<script>
function copyBibTeX() {
  const code = document.getElementById("bibtex-code").textContent;
  navigator.clipboard.writeText(code);
  alert("BibTeX citation copied to clipboard!");
}
function copyAPA() {
  const apa = "Fakhruldeen, M. (F.). (2026). Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework (Version v2.0.2) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23193523";
  navigator.clipboard.writeText(apa);
  alert("APA citation copied to clipboard!");
}
</script>
"""


def get_screen6_home_en() -> str:
    """Generates Stitch Screen 6: GitHub Pages Home & Executive Overview."""
    return """<!--
---
type: Guide
---
-->

<div class="hero-wrapper">
  <div class="hero-tag">
    <span class="pulse-dot"></span> 🚀 PMBOK® 6th, 7th & 8th Edition Ready • ISO 21500 Compliant • v2.0.2
  </div>
  <h1 class="hero-title">Systemic Governance for End-to-End Enterprise Deliverables</h1>
  <div class="hero-title-ar">الحوكمة المؤسسية لتسليمات المشاريع والمراحل الانتقالية</div>
  <p class="hero-subtitle">
    102 standardized, bilingual (English & Arabic) project management deliverables across 8 lifecycle phases. Transform raw project effort into verifiable, auditable enterprise assets with mathematical symmetry and zero vendor lock-in.
  </p>
  <div class="hero-actions">
    <a href="catalog/en/index.html" class="btn-emerald">🚀 Explore 102 Templates (تصفح النماذج)</a>
    <span class="inline-flex items-center gap-2 px-3 py-2 bg-slate-900 text-slate-100 font-mono text-xs rounded-lg border border-slate-700 shadow-sm cursor-pointer" onclick="navigator.clipboard.writeText('pip install tasleemat'); alert('Copied: pip install tasleemat');" title="Click to copy">
      <span class="text-emerald-400">$</span> pip install tasleemat
      <span class="text-[10px] bg-slate-800 text-slate-400 px-1 py-0.5 rounded">📋 Copy</span>
    </span>
    <a href="https://github.com/fakhruldeen/Tasleemat" class="btn-secondary" target="_blank" rel="noopener noreferrer">🐙 GitHub Repo (★ 2) ↗</a>
    <a href="forms/ar/form-viewer.html" class="btn-secondary">📝 Live Form Viewer (معاينة تفاعلية)</a>
    <a href="README_AR.html" class="btn-lang">🇸🇦 الانتقال للبوابة العربية</a>
  </div>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-number">102</div>
      <div class="stat-label">Bilingual Deliverables</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">204</div>
      <div class="stat-label">Synchronized Bundles</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">8</div>
      <div class="stat-label">Lifecycle Phases</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">6</div>
      <div class="stat-label">Stage-Gate Audits</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">4</div>
      <div class="stat-label">Tailoring Tiers</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">100%</div>
      <div class="stat-label">OKF Validated</div>
    </div>
  </div>
</div>

---

<h2 id="lifecycle-pipeline">🧭 1. Interactive 8-Phase Lifecycle Pipeline</h2>

```mermaid
flowchart LR
    P0["00. Portfolio<br/>(6 Forms)"] --> P1["01. Business<br/>(4 Forms)"]
    P1 --> P2["02. Approach<br/>(6 Forms)"]
    P2 --> P3["03. Initiating<br/>(5 Forms)"]
    P3 --> P4["04. Planning<br/>(47 Forms)"]
    P4 --> P5["05. Executing<br/>(12 Forms)"]
    P5 --> P6["06. Controlling<br/>(12 Forms)"]
    P6 --> P7["07. Closing<br/>(5 Forms)"]

    style P0 fill:#f8fafc,stroke:#0b132b,stroke-width:2px
    style P1 fill:#f8fafc,stroke:#0b132b,stroke-width:2px
    style P2 fill:#f8fafc,stroke:#0b132b,stroke-width:2px
    style P3 fill:#eff6ff,stroke:#2563eb,stroke-width:2px
    style P4 fill:#eff6ff,stroke:#2563eb,stroke-width:2px
    style P5 fill:#f0fdf4,stroke:#10b981,stroke-width:2px
    style P6 fill:#fef3c7,stroke:#f59e0b,stroke-width:2px
    style P7 fill:#f8fafc,stroke:#0b132b,stroke-width:2px
```

<div class="phase-cards-grid">
  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 00</span>
      <span style="font-size: 1.5rem;">🏛️</span>
    </div>
    <h3 class="phase-hub-title">00. Program & Portfolio Strategy</h3>
    <p class="phase-hub-desc">Strategic alignment, portfolio balancing, multi-project dependencies, and PMO maturity (6 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/00_Program_and_Portfolio_Management/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/00_Program_and_Portfolio_Management/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/00_Program_and_Portfolio_Management/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 01</span>
      <span style="font-size: 1.5rem;">💎</span>
    </div>
    <h3 class="phase-hub-title">01. Business & Value Delivery</h3>
    <p class="phase-hub-desc">Business justification, benefit realization planning, value tracking, and gap analysis (4 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/01_Business_and_Value_Delivery/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/01_Business_and_Value_Delivery/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/01_Business_and_Value_Delivery/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 02</span>
      <span style="font-size: 1.5rem;">⚖️</span>
    </div>
    <h3 class="phase-hub-title">02. Project Approach & Tailoring</h3>
    <p class="phase-hub-desc">Tailoring strategy, governance tiers, AI ethics, model cards, and agile/hybrid adoption (6 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/02_Project_Approach_and_Tailoring/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/02_Project_Approach_and_Tailoring/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/02_Project_Approach_and_Tailoring/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 03</span>
      <span style="font-size: 1.5rem;">🚀</span>
    </div>
    <h3 class="phase-hub-title">03. Initiating</h3>
    <p class="phase-hub-desc">Formal authorization, product vision, initial assumptions, and stakeholder identification (5 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/form-viewer.html" style="background:#0d9488;color:#fff!important;">🎯 Live Viewer</a>
      <a class="card-action-link" href="forms/en/03_Initiating/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/03_Initiating/index.html">📖 Guides</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 04</span>
      <span style="font-size: 1.5rem;">📐</span>
    </div>
    <h3 class="phase-hub-title">04. Planning (12 Domains)</h3>
    <p class="phase-hub-desc">Comprehensive baselines across Scope, Schedule, Cost, Quality, Resources, Risk, and Procurement (47 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/04_Planning/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/04_Planning/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/04_Planning/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 05</span>
      <span style="font-size: 1.5rem;">⚡</span>
    </div>
    <h3 class="phase-hub-title">05. Executing</h3>
    <p class="phase-hub-desc">Directing work, managing issues, decision logs, change control, and team performance (12 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/05_Executing/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/05_Executing/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/05_Executing/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 06</span>
      <span style="font-size: 1.5rem;">📊</span>
    </div>
    <h3 class="phase-hub-title">06. Monitoring & Controlling</h3>
    <p class="phase-hub-desc">Status reporting, Earned Value Analysis (EVA), variance tracking, and quality acceptance (12 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/06_Monitoring_and_Controlling/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/06_Monitoring_and_Controlling/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/06_Monitoring_and_Controlling/index.html">💡 Examples</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">Phase 07</span>
      <span style="font-size: 1.5rem;">🏁</span>
    </div>
    <h3 class="phase-hub-title">07. Closing</h3>
    <p class="phase-hub-desc">Formal transition to operations, contract closure, final lessons learned, and PIR (5 Artifacts).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/en/07_Closing/index.html">📋 Templates</a>
      <a class="card-action-link" href="guides/en/07_Closing/index.html">📖 Guides</a>
      <a class="card-action-link" href="examples/en/07_Closing/index.html">💡 Examples</a>
    </div>
  </div>
</div>

---

<h2 id="dual-audiences">👥 2. Dual Audience Pathways (Choose Your Journey)</h2>

<div class="grid grid-cols-1 md:grid-cols-2 gap-6 my-6">
  <!-- Card 1 -->
  <div class="dash-card border-blue-200 bg-blue-50/20">
    <div class="flex items-center gap-2 mb-3">
      <span class="text-2xl">👔</span>
      <h3 class="text-lg font-bold text-slate-900 m-0">For Project Managers & PMO Leaders</h3>
    </div>
    <p class="text-xs text-slate-600 mb-4">Empowering PMOs with standardized stage-gate rigor, audit checklists, and bilingual alignment:</p>
    <ul class="text-xs space-y-2 text-slate-700 mb-5">
      <li>• <strong><a href="catalog/en/index.html" class="text-blue-700 font-semibold">Browse 102 Templates</a>:</strong> Filter by phase, tier, and format.</li>
      <li>• <strong><a href="governance.html" class="text-blue-700 font-semibold">6 Stage-Gate Governance Audits</a>:</strong> Gate checklists from Gate 0 to 5.</li>
      <li>• <strong><a href="en/05_tailoring_profiles.html" class="text-blue-700 font-semibold">Project Sizing Tiers</a>:</strong> From Small (5 Core) to Enterprise (45+).</li>
      <li>• <strong><a href="LEXICON.html" class="text-blue-700 font-semibold">Master Terminology Lexicon</a>:</strong> Official Arabic-English project terms.</li>
    </ul>
    <a href="catalog/en/index.html" class="btn-primary text-xs w-full justify-center">Explore PMO Catalog →</a>
  </div>

  <!-- Card 2 -->
  <div class="dash-card border-teal-200 bg-teal-50/20">
    <div class="flex items-center gap-2 mb-3">
      <span class="text-2xl">💻</span>
      <h3 class="text-lg font-bold text-slate-900 m-0">For Developers & AI Engineers</h3>
    </div>
    <p class="text-xs text-slate-600 mb-4">Machine-readable data contracts, Python automation SDK, and CI/CD stage-gate verification:</p>
    <ul class="text-xs space-y-2 text-slate-700 mb-5">
      <li>• <strong><a href="TECHNICAL.html" class="text-teal-700 font-semibold">Python SDK (`tasleemat.ai`)</a>:</strong> LLM document drafting.</li>
      <li>• <strong><a href="TECHNICAL.html" class="text-teal-700 font-semibold">Global CLI Scaffolder</a>:</strong> <code>pip install tasleemat</code></li>
      <li>• <strong><a href="TECHNICAL.html" class="text-teal-700 font-semibold">JSON Schemas & OKF Data Packages</a>:</strong> Frictionless metadata.</li>
      <li>• <strong><a href="TECHNICAL.html" class="text-teal-700 font-semibold">CI/CD Stage-Gate Action</a>:</strong> Automated PR gate validation.</li>
    </ul>
    <a href="TECHNICAL.html" class="btn-emerald text-xs w-full justify-center">Read Developer SDK Manual →</a>
  </div>
</div>

---

<h2 id="cli-quickstart">⚡ 3. Interactive CLI Quickstart Terminal</h2>

<div class="cli-terminal-window">
  <div class="terminal-header">
    <div class="terminal-dots">
      <span class="terminal-dot dot-red"></span>
      <span class="terminal-dot dot-yellow"></span>
      <span class="terminal-dot dot-green"></span>
    </div>
    <span class="terminal-title">bash — tasleemat cli quickstart</span>
    <button class="card-btn" style="padding: 2px 8px; font-size: 11px;" onclick="navigator.clipboard.writeText('pip install tasleemat && tasleemat init --tier 2 --pack agile --lang ar --name \\\"منصة_التحول_الرقمي\\\"'); alert('Copied CLI command sequence!');">📋 Copy</button>
  </div>
  <div class="terminal-body">
    <div class="flex items-center gap-2">
      <span class="terminal-prompt">$</span>
      <span class="terminal-cmd">pip install tasleemat</span>
    </div>
    <div class="flex items-center gap-2 mt-2">
      <span class="terminal-prompt">$</span>
      <span class="terminal-cmd">tasleemat init --tier 2 --pack agile --lang ar --name "منصة_التحول_الرقمي"</span>
    </div>
    <div class="terminal-output mt-2">
      <span class="text-slate-400">[INFO] Scaffolding 18 synchronized bilingual PMO artifacts for Tier 2 Agile...</span><br>
      <span class="terminal-badge-ok">[OK] Project workspace created at ./منصة_التحول_الرقمي! Ready for delivery.</span>
    </div>
  </div>
</div>

---

<h2 id="tailoring-preview">🎯 4. Tailoring Matrix Preview (4 Project Sizing Tiers)</h2>

| Tier | Project Sizing | Recommended Template Count | Focus Area | Quick Link |
| :--- | :--- | :---: | :--- | :---: |
| **Tier 1: Micro / Small** | Short duration, low risk | **5 Core Artifacts** | Charter, Basic Schedule, Action Log, Status Report, Closeout | [Inspect Tier 1](governance.md#tailoring-matrix) |
| **Tier 2: Standard Core** | Medium complexity & budget | **18 Artifacts** | Full Baselines (Scope, Schedule, Cost, Risk, Communications) | [Inspect Tier 2](governance.md#tailoring-matrix) |
| **Tier 3: Enterprise** | High budget, multi-vendor | **45+ Artifacts** | Formal Governance, Stage-Gate Signoffs, Procurement, Audit | [Inspect Tier 3](governance.md#tailoring-matrix) |
| **Tier 4: Agile / AI** | Iterative software & AI projects | **25 Artifacts** | Sprint Backlog, Flow Metrics, Model Cards, Retrospectives | [Inspect Tier 4](governance.md#tailoring-matrix) |

---

<h2 id="citation-standards">📜 5. Standards Compliance & Academic Citation</h2>

<div class="dash-card">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-4">
    <div class="flex flex-wrap items-center gap-2">
      <span class="badge badge-code">DOI: 10.5281/zenodo.23193523</span>
      <span class="badge" style="background:#eff6ff;color:#1e3a8a;">PMI PMBOK® 6/7/8 Ready</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">ISO 21500 / 21502 Compliant</span>
      <span class="badge" style="background:#ede9fe;color:#6b21a8;">NIST AI RMF Aligned</span>
    </div>
    <div class="flex gap-2">
      <button class="card-btn" onclick="navigator.clipboard.writeText('@software{fakhruldeen_tasleemat_2026,\\n  author = {Fakhruldeen, Mohamed (Fouad)},\\n  title = {Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework},\\n  year = {2026},\\n  version = {v2.0.2},\\n  doi = {10.5281/zenodo.23193523}\\n}'); alert('BibTeX citation copied!');">📋 Copy BibTeX</button>
      <button class="card-btn" onclick="navigator.clipboard.writeText('Fakhruldeen, M. (F.). (2026). Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework (v2.0.2). Zenodo. https://doi.org/10.5281/zenodo.23193523'); alert('APA citation copied!');">📋 Copy APA</button>
    </div>
  </div>
  <p class="text-xs text-slate-600 mb-2">
    If you use Tasleemat in your PMO operations, research, or audit manuals, please cite:
  </p>
  <blockquote class="text-xs text-slate-700 bg-slate-50 p-3 rounded border-l-4 border-blue-500 m-0">
    Mohamed (Fouad) Fakhruldeen. (2026). fakhruldeen/Tasleemat: v2.0.2 [Computer software]. Zenodo. <a href="https://doi.org/10.5281/zenodo.23193523" target="_blank">https://doi.org/10.5281/zenodo.23193523</a>
  </blockquote>
  <div class="text-[11px] text-slate-400 mt-3">Licensed under the <a href="https://github.com/fakhruldeen/Tasleemat/blob/main/LICENSE" target="_blank" class="underline">MIT License</a>. Built with precision by Fakhruldeen.</div>
</div>
"""


def get_screen2_home_ar() -> str:
    """Generates Stitch Screen 2: Arabic RTL Templates Catalog & Showcase."""
    return """<!--
---
type: Guide
---
-->

<div class="hero-wrapper" dir="rtl">
  <div class="hero-tag">
    <span class="pulse-dot"></span> معتمد ومطابق لمعايير PMI PMBOK® 6/7/8 و ISO 21500 وهيئة الحكومة الرقمية (DGA)
  </div>
  <h1 class="hero-title">دليل النماذج والتسليمات القياسية الموثقة (102 تسليمة بالعربية)</h1>
  <p class="hero-subtitle">
    منظومة حوكمة وتسليمات متكاملة تغطي دورة حياة المشروع من المحفظة إلى الإغلاق، مهيأة للاستخدام المباشر والأتمتة الذكية والذكاء الاصطناعي مع تناظر ثنائي كامل.
  </p>
  <div class="hero-actions">
    <a href="catalog/ar/index.html" class="btn-emerald">🚀 تصفح كتالوج النماذج بالعربية (102 نموذج)</a>
    <a href="forms/ar/form-viewer.html" class="btn-primary">📝 معاينة وتخصيص ميثاق المشروع (FORM-03-01)</a>
    <span class="inline-flex items-center gap-2 px-3 py-2 bg-slate-900 text-slate-100 font-mono text-xs rounded-lg border border-slate-700 shadow-sm cursor-pointer" onclick="navigator.clipboard.writeText('tasleemat init --lang ar'); alert('تم نسخ أمر التوليد بالعربية: tasleemat init --lang ar');" title="انقر للنسخ">
      <span class="text-emerald-400">$</span> tasleemat init --lang ar
      <span class="text-[10px] bg-slate-800 text-slate-400 px-1 py-0.5 rounded">📋 نسخ</span>
    </span>
    <a href="https://github.com/fakhruldeen/Tasleemat" class="btn-secondary" target="_blank" rel="noopener noreferrer">🐙 مستودع GitHub ↗</a>
    <a href="index.html" class="btn-lang">🇬🇧 English Portal</a>
  </div>
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-number">102</div>
      <div class="stat-label">نموذج عربي معتمد</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">204</div>
      <div class="stat-label">حزمة رقمية متزامنة</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">8</div>
      <div class="stat-label">مراحل مؤسسية</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">6</div>
      <div class="stat-label">بوابات عبور حوكمية</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">4</div>
      <div class="stat-label">مستويات مواءمة (Tiers)</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">100%</div>
      <div class="stat-label">مطابقة لمعيار OKF</div>
    </div>
  </div>
</div>

---

<div dir="rtl">

<h2>🌟 نماذج وتسليمات مميزة جاهزة للمعاينة المباشرة</h2>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-6">

  <!-- Card 1: Charter -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-code">FORM-03-01</span>
      <span class="badge badge-phase">🚀 البدء والترخيص</span>
      <span class="badge badge-tier-1">المستوى 1-3</span>
    </div>
    <h3 class="dash-card-title">ميثاق المشروع المعتمد (Project Charter)</h3>
    <p class="dash-card-desc">
      الوثيقة التأسيسية التي تخول مدير المشروع رسمياً وتحدد نطاق العمل، الأهداف الاستراتيجية، الميزانية المبدئية، وأصحاب المصلحة الرئيسيين وفق متطلبات PMBOK.
    </p>
    <div class="dash-card-actions">
      <a href="forms/ar/form-viewer.html" class="card-btn" style="background:#0d9488;color:#fff!important;">🎯 معاينة النموذج بالعربية</a>
      <a href="catalog/ar/index.html" class="card-btn">📋 تفاصيل النموذج</a>
    </div>
  </div>

  <!-- Card 2: WBS -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-code">FORM-04-03</span>
      <span class="badge badge-phase">📐 التخطيط</span>
      <span class="badge badge-tier-2">المستوى 2-3</span>
    </div>
    <h3 class="dash-card-title">خطة إدارة النطاق وهيكل تجزئة العمل (WBS)</h3>
    <p class="dash-card-desc">
      تحليل شجري تفكيكي لمخرجات المشروع وحزم العمل، مع قاموس هيكل تجزئة العمل ومصفوفة تتبع المتطلبات لضمان عدم حدوث زحف في النطاق.
    </p>
    <div class="dash-card-actions">
      <a href="catalog/ar/index.html" class="card-btn btn-primary-act">📋 استعراض القالب</a>
    </div>
  </div>

  <!-- Card 3: Risk -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-code">FORM-04-18</span>
      <span class="badge badge-phase">📐 التخطيط</span>
      <span class="badge badge-tier-3">المستوى 1-4</span>
    </div>
    <h3 class="dash-card-title">سجل المخاطر النوعي والكمي ومصفوفة التأثير</h3>
    <p class="dash-card-desc">
      مصفوفة احتمالية وتأثير متدرجة (5×5) مع خطط الاستجابة للمخاطر (تجنب، تخفيف، نقل، قبول) وحساب الاحتياطي الإداري واحتياطي الطوارئ.
    </p>
    <div class="dash-card-actions">
      <a href="catalog/ar/index.html" class="card-btn btn-primary-act">📋 استعراض القالب</a>
    </div>
  </div>

  <!-- Card 4: EVA -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-code">FORM-06-03</span>
      <span class="badge badge-phase">📊 المراقبة والتحكم</span>
      <span class="badge badge-tier-2">المستوى 2-3</span>
    </div>
    <h3 class="dash-card-title">تقرير تحليل القيمة المكتسبة (Earned Value - EVA)</h3>
    <p class="dash-card-desc">
      حساب مؤشرات الأداء الأساسية: تباين التكلفة (CV)، تباين الجدول (SV)، مؤشر أداء التكلفة (CPI)، ومؤشر أداء الجدول (SPI) والتنبؤ عند الإنجاز (EAC).
    </p>
    <div class="dash-card-actions">
      <a href="catalog/ar/index.html" class="card-btn btn-primary-act">📋 استعراض القالب</a>
    </div>
  </div>

  <!-- Card 5: AI Model Card -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-code">FORM-02-04</span>
      <span class="badge badge-phase">⚖️ التخصيص والمواءمة</span>
      <span class="badge badge-tier-4">المستوى 4 (AI)</span>
    </div>
    <h3 class="dash-card-title">بطاقة نموذج حوكمة الذكاء الاصطناعي (AI Model Card)</h3>
    <p class="dash-card-desc">
      توثيق مؤسسي لنماذج الذكاء الاصطناعي، بيانات التدريب، تقييمات التحيز، حدود الاستخدام، وإجراءات السلامة وفق إطار عمل NIST وسدايا.
    </p>
    <div class="dash-card-actions">
      <a href="catalog/ar/index.html" class="card-btn btn-primary-act">📋 استعراض القالب</a>
    </div>
  </div>

  <!-- Card 6: Handover -->
  <div class="dash-card">
    <div class="dash-card-header">
      <span class="badge badge-code">FORM-07-02</span>
      <span class="badge badge-phase">🏁 الإغلاق</span>
      <span class="badge badge-tier-1">المستوى 1-3</span>
    </div>
    <h3 class="dash-card-title">محضر التسليم والقبول التشغيلي (Operational Handover)</h3>
    <p class="dash-card-desc">
      بروتوكول تحويل مخرجات المشروع رسمياً إلى العمليات التشغيلية (BAU)، توثيق فترات الضمان، وتوقيعات اعتماد راعي المشروع والجهات المستفيدة.
    </p>
    <div class="dash-card-actions">
      <a href="catalog/ar/index.html" class="card-btn btn-primary-act">📋 استعراض القالب</a>
    </div>
  </div>

</div>

---

<h2>🧭 مخطط دورة حياة المشروع وبوابات العبور الحوكمية</h2>

```mermaid
flowchart TD
    subgraph G0["بوابة 0: المواءمة الاستراتيجية ودراسة الجدوى"]
        P00["00. إدارة البرامج والمحافظ"]
        P01["01. الأعمال وتسليم القيمة"]
    end

    subgraph G1["بوابة 1: ميثاق المشروع والتخصيص"]
        P02["02. منهجية المشروع وتخصيصه"]
        P03["03. البدء والترخيص"]
    end

    subgraph G2["بوابة 2: اعتماد خطوط الأساس"]
        P04["04. التخطيط المتكامل (12 مجالاً)"]
    end

    subgraph G3["بوابة 3: التنفيذ والتحكم في الأداء"]
        P05["05. التنفيذ والتسليم"]
        P06["06. المراقبة والتحكم"]
    end

    subgraph G4["بوابة 4 و 5: التسليم التشغيلي والإغلاق"]
        P07["07. الإغلاق النهائي"]
    end

    G0 --> G1 --> G2 --> G3 --> G4
```

---

<h2>🏛️ المراحل الثمانية لدورة حياة المشروع</h2>

<div class="phase-cards-grid">
  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 00</span>
      <span style="font-size: 1.5rem;">🏛️</span>
    </div>
    <h3 class="phase-hub-title">إدارة البرامج والمحافظ</h3>
    <p class="phase-hub-desc">المواءمة الاستراتيجية، توازن المحفظة، إدارة الاعتماديات بين المشاريع، وتقييم نضج مكتب PMO (6 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/00_إدارة_البرامج_والمحافظ/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/00_إدارة_البرامج_والمحافظ/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/00_إدارة_البرامج_والمحافظ/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 01</span>
      <span style="font-size: 1.5rem;">💎</span>
    </div>
    <h3 class="phase-hub-title">الأعمال وتسليم القيمة</h3>
    <p class="phase-hub-desc">دراسات الجدوى الاقتصادية، خطط إدارة المنافع، سجلات تحقيق القيمة، وتحليل الفجوات (4 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/01_الأعمال_وتسليم_القيمة/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/01_الأعمال_وتسليم_القيمة/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/01_الأعمال_وتسليم_القيمة/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 02</span>
      <span style="font-size: 1.5rem;">⚖️</span>
    </div>
    <h3 class="phase-hub-title">منهجية المشروع وتخصيصه</h3>
    <p class="phase-hub-desc">استراتيجية التخصيص، مستويات الحوكمة، أخلاقيات الذكاء الاصطناعي، وبطاقات النماذج (6 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/02_منهجية_المشروع_وتخصيصه/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/02_منهجية_المشروع_وتخصيصه/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/02_منهجية_المشروع_وتخصيصه/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 03</span>
      <span style="font-size: 1.5rem;">🚀</span>
    </div>
    <h3 class="phase-hub-title">البدء والترخيص</h3>
    <p class="phase-hub-desc">الترخيص الرسمي للمشروع، رؤية المنتج، سجل الافتراضات الأولية، وتحديد المعنيين (5 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/form-viewer.html" style="background:#0d9488;color:#fff!important;">🎯 معاينة ميثاق المشروع</a>
      <a class="card-action-link" href="forms/ar/03_البدء/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/03_البدء/index.html">📖 الأدلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 04</span>
      <span style="font-size: 1.5rem;">📐</span>
    </div>
    <h3 class="phase-hub-title">التخطيط المتكامل (12 مجالاً)</h3>
    <p class="phase-hub-desc">الخطوط المرجعية الشاملة للنطاق، الجدول الزمني، التكلفة، الجودة، الموارد، المخاطر، والمشتريات (47 مخرجاً).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/04_التخطيط/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/04_التخطيط/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/04_التخطيط/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 05</span>
      <span style="font-size: 1.5rem;">⚡</span>
    </div>
    <h3 class="phase-hub-title">التنفيذ والتسليم</h3>
    <p class="phase-hub-desc">توجيه وإدارة أعمال المشروع، سجل القضايا، سجل القرارات، طلبات التغيير، وأداء الفريق (12 مخرجاً).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/05_التنفيذ/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/05_التنفيذ/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/05_التنفيذ/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 06</span>
      <span style="font-size: 1.5rem;">📊</span>
    </div>
    <h3 class="phase-hub-title">المراقبة والتحكم</h3>
    <p class="phase-hub-desc">تقارير الأداء، تحليل القيمة المكتسبة (EVA)، مراقبة التباين، وضمان الجودة واختبارات القبول (12 مخرجاً).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/06_المراقبة_والتحكم/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/06_المراقبة_والتحكم/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/06_المراقبة_والتحكم/index.html">💡 الأمثلة</a>
    </div>
  </div>

  <div class="phase-hub-card">
    <div class="phase-hub-header">
      <span class="badge badge-phase">المرحلة 07</span>
      <span style="font-size: 1.5rem;">🏁</span>
    </div>
    <h3 class="phase-hub-title">الإغلاق والتسليم التشغيلي</h3>
    <p class="phase-hub-desc">الانتقال الرسمي للعمليات التشغيلية، إغلاق العقود، خلاصة الدروس المستفادة، ومراجعة ما بعد التنفيذ (5 مخرجات).</p>
    <div class="phase-hub-actions">
      <a class="card-action-link" href="forms/ar/07_الإغلاق/index.html">📋 القوالب</a>
      <a class="card-action-link" href="guides/ar/07_الإغلاق/index.html">📖 الأدلة</a>
      <a class="card-action-link" href="examples/ar/07_الإغلاق/index.html">💡 الأمثلة</a>
    </div>
  </div>
</div>

---

<h2>📜 الاعتماد المؤسسي والتوثيق الأكاديمي</h2>

<div class="dash-card">
  <div class="flex flex-wrap items-center justify-between gap-3 mb-3">
    <div class="flex flex-wrap items-center gap-2">
      <span class="badge badge-code">معرف الوثيقة: 10.5281/zenodo.23193523</span>
      <span class="badge" style="background:#eff6ff;color:#1e3a8a;">PMI PMBOK® 6/7/8</span>
      <span class="badge" style="background:#f0fdf4;color:#166534;">ISO 21500 / 21502</span>
      <span class="badge" style="background:#ede9fe;color:#6b21a8;">هيئة الحكومة الرقمية (DGA)</span>
    </div>
    <div class="flex gap-2">
      <button class="card-btn" onclick="navigator.clipboard.writeText('Fakhruldeen, M. (F.). (2026). Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework (v2.0.2). Zenodo. https://doi.org/10.5281/zenodo.23193523'); alert('تم نسخ التوثيق بصيغة APA بنجاح!');">📋 نسخ التوثيق (APA)</button>
    </div>
  </div>
  <p class="text-xs text-slate-600 mb-2">
    إذا تم استخدام تسليمات في عمليات مكتب إدارة المشاريع أو أدلة التدقيق أو الأبحاث الأكاديمية، يرجى الاستشهاد بالمصدر:
  </p>
  <blockquote class="text-xs text-slate-700 bg-slate-50 p-3 rounded border-r-4 border-blue-500 m-0">
    Mohamed (Fouad) Fakhruldeen. (2026). fakhruldeen/Tasleemat: v2.0.2 [Computer software]. Zenodo. <a href="https://doi.org/10.5281/zenodo.23193523" target="_blank">https://doi.org/10.5281/zenodo.23193523</a>
  </blockquote>
  <div class="text-[11px] text-slate-400 mt-3">مرخص بموجب ترخيص <a href="https://github.com/fakhruldeen/Tasleemat/blob/main/LICENSE" target="_blank" class="underline">MIT</a>. مطور بدقة فائقة لدعم قادة المشاريع حول العالم.</div>
</div>

</div>
"""
