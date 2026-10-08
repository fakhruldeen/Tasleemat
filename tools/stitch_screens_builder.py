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
    """Generates Stitch Screen 4: Stage-Gate Governance & Tailoring Profiles Portal in clean GitHub-flavored Markdown."""
    return """<!--
---
type: Guide
---
-->

# Stage-Gate Governance & Tailoring Architecture

> **منظومة بوابات العبور الحوكمية ومستويات تخصيص المشاريع**  
> *PMI PMBOK® 6/7/8 & ISO 21500 / ISO 21502:2021 Compliant*

Structured gatekeeper decision checkpoints (Gate 0 Idea to Gate 5 Closeout) paired with 4 scalable project sizing tiers to ensure auditability, rigorous fiscal control, and zero governance bloat.

---

## 🏛️ 1. Executive Governance Framework

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

## 🚪 2. Six Stage-Gates Specification

### Gate 0: Strategic Concept & Portfolio Alignment
*بوابة 0: دراسة الفكرة والمواءمة الاستراتيجية*

- **Lifecycle Phases:** Phase 00 (Discovery) & Phase 01 (Ideation)
- **Governing Authority:** Investment Review Board / CFO / Portfolio Steering Committee
- **Purpose:** Validates strategic alignment, OKR linkage, high-level feasibility, and preliminary ROI before allocating capital or assigning project teams.
- **Auditable Gate Checklist:**
  - [x] Initiative directly aligns with corporate OKRs or Vision 2030 strategic objectives.
  - [x] Business Case contains quantified cost of inaction and preliminary NPV/IRR analysis.
  - [ ] Initial feasibility study verifies technical and legal compliance.
- **Key Artifacts:**
  - `FORM-00-06`: OKR Alignment
  - `FORM-01-01`: Business Case
  - `FORM-01-02`: Feasibility Study

---

### Gate 1: Project Charter & Authorization
*بوابة 1: ميثاق المشروع والترخيص الرسمي*

- **Lifecycle Phases:** Phase 02 (Preparation) & Phase 03 (Initiation)
- **Governing Authority:** Executive Sponsor & PMO Director
- **Purpose:** Formally authorizes project existence, assigns the Project Manager, establishes high-level scope boundaries, and defines the initial budget envelope.
- **Auditable Gate Checklist:**
  - [x] Signed Project Charter by Executive Sponsor and PMO Director.
  - [x] Governance tier selected (Tier 1-4) with tailored deliverable bundle.
  - [x] Initial stakeholder register and assumption log established.
- **Key Artifacts:**
  - `FORM-03-01`: Project Charter ([معاينة تفاعلية](forms/ar/form-viewer.html))
  - `FORM-03-04`: Stakeholder Register
  - `FORM-02-01`: Tailoring Plan

---

### Gate 2: Integrated Baselines Approval
*بوابة 2: اعتماد خطوط الأساس المتكاملة*

- **Lifecycle Phases:** Phase 04 (Planning)
- **Governing Authority:** PMO Steering Committee
- **Purpose:** Rigorous lock-in of Scope Baseline (WBS), Critical Path Schedule, Cost Baseline, and Risk Response Plans before major expenditure.
- **Auditable Gate Checklist:**
  - [x] 100% WBS Work Package coverage matching agreed scope dictionary.
  - [x] Cost baseline includes validated contingency and management reserves.
  - [ ] Risk Register contains proactive response plans for all High/Critical risks.
- **Key Artifacts:**
  - `FORM-04-03`: Scope & WBS
  - `FORM-04-12`: Schedule Baseline
  - `FORM-04-15`: Cost Baseline
  - `FORM-04-18`: Risk Register

---

### Gate 3: Execution Mid-Stage Health Check
*بوابة 3: مراقبة الأداء وتحليل القيمة المكتسبة*

- **Lifecycle Phases:** Phase 05 (Execution) & Phase 06 (Monitoring & Controlling)
- **Governing Authority:** PMO Performance Board
- **Purpose:** Continuous monitoring using Earned Value Analysis (EVA): verifies Cost Performance Index (CPI ≥ 0.95) and Schedule Performance Index (SPI ≥ 0.95).
- **Auditable Gate Checklist:**
  - [x] SPI and CPI within acceptable control thresholds (≥ 0.95).
  - [x] All major issues have assigned owners and active remediation dates.
  - [ ] Change requests vetted through formal Change Control Board (CCB).
- **Key Artifacts:**
  - `FORM-06-03`: Earned Value Report
  - `FORM-05-03`: Issue Log
  - `FORM-05-04`: Change Request

---

### Gate 4: Operational Handover & UAT
*بوابة 4: القبول والتسليم التشغيلي*

- **Lifecycle Phases:** Phase 06 (Controlling) & Phase 07 (Closing)
- **Governing Authority:** Operations Director & End-User Sponsor
- **Purpose:** Formal transition of project deliverables into business-as-usual (BAU) operations, warranty signoffs, and training sign-off.
- **Auditable Gate Checklist:**
  - [x] 100% user acceptance testing (UAT) test cases verified and signed off.
  - [ ] Operational handover protocols and SLA agreements executed.
  - [ ] Operations team fully trained with operational manuals delivered.
- **Key Artifacts:**
  - `FORM-06-05`: Quality Acceptance
  - `FORM-07-02`: Operational Handover

---

### Gate 5: Contract Closeout & Value Realization
*بوابة 5: الإغلاق النهائي وتقييم الفوائد*

- **Lifecycle Phases:** Phase 07 (Closing)
- **Governing Authority:** Executive Sponsor & Audit Committee
- **Purpose:** Final contract reconciliation, vendor evaluations, lessons learned archive, and post-implementation review (PIR) schedule.
- **Auditable Gate Checklist:**
  - [x] All procurement contracts closed with final settlements executed.
  - [x] Comprehensive Lessons Learned Register archived in organizational repository.
  - [ ] Post-Implementation Review (PIR) calendar established with Value Lead.
- **Key Artifacts:**
  - `FORM-07-01`: Lessons Learned
  - `FORM-07-03`: Contract Closeout
  - `FORM-07-05`: Post-Implementation Review

---

## ⚖️ 3. Tailoring Profiles Matrix (4 Project Sizing Tiers)

| Tier | Project Profile | Artifact Bundle | Governance Cadence | Required Approvals |
| :--- | :--- | :---: | :--- | :--- |
| **Tier 1: Micro / Small** | Budget < $100K, Duration < 3 mo, Low Risk | **5 Core Artifacts** | Bi-weekly flash report | Project Sponsor only |
| **Tier 2: Standard Core** | Budget $100K–$1M, 3–12 mo, Medium Risk | **18 Artifacts** | Monthly PMO review | Sponsor & PMO Lead |
| **Tier 3: Enterprise Transformation** | Budget > $1M, Multi-vendor, High Impact | **45+ Artifacts** | Formal Steering Committee | Sponsor, PMO, CFO, SteerCo |
| **Tier 4: Agile / AI Iterative** | Machine learning, SaaS, Fast sprints | **25 Artifacts** | Sprint review & Model audit | Product Owner & AI Ethics Lead |

---

## 🧮 4. Project Tailoring Decision Matrix & CLI Automation

Use the project parameter table below to determine the recommended governance pack:

| Parameter | Options | Recommended Action / Pack |
| :--- | :--- | :--- |
| **Budget Envelope** | Small (< $100K) / Medium ($100K–$1M) / Enterprise (> $1M) | Low budgets qualify for Tier 1; Enterprise requires Tier 3 |
| **Duration** | < 3 months / 3–12 months / Multi-Year | Short durations qualify for Tier 1; Multi-year requires Tier 3 |
| **Methodology** | Traditional Waterfall / Agile Scrum / AI & Data Science | Agile & AI use Tier 4 specialized bundles |
| **Compliance** | Standard Enterprise / High Regulatory (Gov, DGA, SAMA) | High regulatory triggers mandatory Tier 3 oversight |

### Automated Project Initialization via CLI

Initialize tailored project structures directly with the CLI:

```bash
# Tier 1: Micro / Small Fast-Track (5 Core Artifacts)
tasleemat init --tier 1 --pack lean --lang both

# Tier 2: Standard Core Pack (18 Artifacts)
tasleemat init --tier 2 --pack standard --lang both

# Tier 3: Enterprise Transformation Pack (45+ Artifacts)
tasleemat init --tier 3 --pack enterprise --lang both

# Tier 4: Agile / Lean Iterative Pack (25 Artifacts)
tasleemat init --tier 4 --pack agile --lang both

# Tier 4: AI & Machine Learning Governance (25 Artifacts)
tasleemat init --tier 4 --pack ai --lang both
```
"""


def get_screen3_developer_md() -> str:
    """Generates Stitch Screen 3: Developer CLI, Python SDK & Bilingual Lexicon in clean GitHub-flavored Markdown."""
    return """<!--
---
type: Guide
---
-->

# Developer Manual, CLI Scaffolder & Python SDK (`tasleemat.ai`)

> **Bilingual PMO Governance, Automated Scaffolding & Standardized Terminology**  
> *دليل المطورين، أدوات سطر الأوامر (CLI)، وحزمة بايثون، والمعجم الموحد*

[![PyPI Version](https://img.shields.io/pypi/v/tasleemat.svg?color=blue)](https://pypi.org/project/tasleemat/)
[![Python Versions](https://img.shields.io/pypi/pyversions/tasleemat.svg)](https://pypi.org/project/tasleemat/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.23193523-blue)](https://doi.org/10.5281/zenodo.23193523)

---

## ⚡ Quick Start & Installation

Install the official Tasleemat distribution package directly from PyPI:

```bash
# Install the core CLI and Python SDK
pip install --upgrade tasleemat

# Verify CLI version and environment health
tasleemat --version
tasleemat doctor
```

### Standards & Compliance Grounding

| Dimension | Specification | Notes |
|:---|:---|:---|
| **Global Standard** | PMI PMBOK® 6th, 7th & 8th Edition | Complete alignment with Performance Domains |
| **Data Architecture** | OKF Frictionless Datapackage (v0.2) | Machine-readable schema validation |
| **International Quality**| ISO 21500 / ISO 21502:2021 | Governance and guidance for project management |
| **AI Governance** | NIST AI RMF 1.0 & ISO 42001 | Grounded prompts and audit checklists |
| **Language Parity** | Dual RTL/LTR (Arabic & English) | 1:1 bilingual field parity |

---

## 🛠️ CLI Automation & Project Scaffolding

Tasleemat includes an interactive scaffolding engine designed for command-line automation and CI/CD pipelines.

### Common CLI Commands

```bash
# 1. Initialize a Standard Tier 2 Project in Arabic
tasleemat init --tier 2 --pack standard --lang ar --name "منصة_التحول_الرقمي"

# 2. Initialize a Fast Agile / Scrum Project with Dual Language
tasleemat init --tier 4 --pack agile --lang both --name "digital_agile_hub"

# 3. Scaffold an Individual Deliverable Template
tasleemat scaffold FORM-03-01 --lang dual --out ./deliverables/

# 4. Validate All Deliverables against Frictionless Data Schemas
tasleemat validate ./deliverables/ --strict
```

### Supported Governance Sizing Tiers

1. **Tier 1 (Micro / Small - 5 Artifacts):** Lean execution for experimental or internal departmental initiatives.
2. **Tier 2 (Standard Core - 18 Artifacts):** Standard enterprise project delivery with foundational governance.
3. **Tier 3 (Enterprise Transformation - 45+ Artifacts):** High-budget, mission-critical transformations with strict oversight.
4. **Tier 4 (Agile / AI Iterative - 25 Artifacts):** Sprint-based delivery with continuous AI validation loops.

---

## 🤖 Programmatic Python SDK (`tasleemat.ai`)

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

## 📖 Master Bilingual PMO Lexicon

Core terminology aligned with the official PMI PMBOK® Lexicon and MENA government project standards:

| English Term | المصطلح العربي المعتمد | Definition & Context (التعريف والسياق) | Lifecycle Domain | Standard Reference |
|:---|:---|:---|:---|:---|
| **Baseline** | **الخط الأساسي** | The approved version of a work product, schedule, or cost envelope that can only be changed through formal change control. | Planning | PMBOK® 6/7/8 |
| **Work Breakdown Structure (WBS)** | **هيكل تجزئة العمل** | A hierarchical decomposition of the total scope of work to be carried out by the project team. | Scope (04.02) | ISO 21502 / PMBOK® |
| **Earned Value Analysis (EVA)** | **تحليل القيمة المكتسبة** | Methodology that combines scope, schedule, and resource measurements to assess project performance and progress. | Monitoring (06) | ANSI/EIA-748 |
| **Stage-Gate Review** | **مراجعة بوابة المرحلة** | A formal checkpoint at the end of a phase where a decision is made to continue, conditionally proceed, or terminate. | Governance (00-07) | PMI Standard |
| **Deliverable** | **المُسلَّم / التسليمة القياسية** | Any unique and verifiable product, result, or capability to perform a service that is required to be produced to complete a phase. | All Lifecycle | OKF / PMBOK® |
| **Stakeholder Engagement** | **إشراك أصحاب المصلحة** | Strategies and actions to involve individuals and groups in project decisions and execution based on interests and influence. | Initiating (03) | PMBOK® Principle 3 |
| **Risk Appetite** | **القابلية للمخاطر** | The degree of uncertainty an organization or individual is willing to accept in anticipation of a reward. | Risk (04.08) | ISO 31000 |
| **Contingency Reserve** | **احتياطي الطوارئ** | Time or budget allocated within the cost baseline for known-unknown risks managed by the Project Manager. | Cost (04.04) | PMBOK® 6th/7th |

*For the complete interactive lexicon with instant search and filtering, visit the web portal at [developer.html](developer.html#lexicon) or [docs/LEXICON.md](LEXICON.md).*

---

## 📚 Academic Citation & Zenodo DOI

If you utilize the Tasleemat framework or dataset in enterprise research, audit manuals, or academia, please cite:

```bibtex
@software{fakhruldeen_tasleemat_2026,
  author       = {Fakhruldeen, Mohamed (Fouad)},
  title        = {Tasleemat: The Enterprise Bilingual (English & Arabic) Project Management Artifact & AI Governance Framework},
  year         = {2026},
  version      = {v2.0.2},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23193523},
  url          = {https://doi.org/10.5281/zenodo.23193523}
}
```

---

## 🔗 Related Resources

- [Stage-Gate Governance & Tailoring](governance.md)
- [Master Bilingual Lexicon](LEXICON.md)
- [Getting Started Guide (English)](en/01_getting_started.md)
- [دليل البدء السريع (العربية)](ar/01_getting_started.md)
- [GitHub Repository](https://github.com/fakhruldeen/Tasleemat)
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


def get_screen5_catalog_html(deliverables: list, lang: str = "en", rel_root: str = "../../") -> str:
    """Generates Stitch Screen 5: Interactive 102 Deliverables Catalog for English or Arabic."""
    import html as pyhtml
    is_ar = (lang == "ar")

    def get_tiers(d):
        code_raw = d.get("code_raw", "")
        tiers = []
        if code_raw in {"03_01", "04_03_04", "04_03_08", "05_01", "06_01", "07_02", "07_01"}:
            tiers.append("t1")
        if "t1" in tiers or code_raw in {
            "01_01", "02_01", "03_04", "04_02_01", "04_02_06", "04_04_04", 
            "04_05_01", "04_06_01", "04_07_01", "04_08_02", "04_09_01", "04_10_01", 
            "05_02", "05_03", "06_03"
        }:
            tiers.append("t2")
        if code_raw.startswith("02_") or code_raw in {
            "03_01", "03_02", "04_02_08", "04_02_09", "04_03_09", "04_03_10", 
            "04_05_03", "04_06_05", "04_06_06", "04_08_02", "05_01", "05_04", 
            "05_05", "05_06", "05_07", "06_01", "06_02", "06_06", "06_07", 
            "07_01", "07_02"
        } or "AI" in d.get("tier", ""):
            tiers.append("t4")
        if "t1" in tiers or "t2" in tiers or code_raw.startswith("00_") or code_raw.startswith("01_") or "04_11" in code_raw or "04_12" in code_raw or code_raw in {"05_08", "05_09", "05_10", "06_04", "06_05", "06_08", "06_09", "07_03", "07_04", "07_05"}:
            tiers.append("t3")
        if not tiers:
            tiers = ["t3"]
        return tiers

    cards_html = []
    for d in deliverables:
        code_pmo = d.get("code", "")
        code_raw = d.get("code_raw", "")
        code_form = code_pmo.replace("PMO-", "FORM-").replace(".", "-")
        phase = d.get("phase", "00")
        name_en = d.get("name_en", "")
        name_ar = d.get("name_ar", "")
        phase_name_en = d.get("phase_name_en", "")
        phase_name_ar = d.get("phase_name_ar", "")
        tier_list = get_tiers(d)
        data_tier = ",".join(tier_list)

        tier_badges_labels = {
            "t1": "Tier 1" if not is_ar else "المستوى 1",
            "t2": "Tier 2" if not is_ar else "المستوى 2",
            "t3": "Tier 3" if not is_ar else "المستوى 3",
            "t4": "Tier 4 AI" if not is_ar else "المستوى 4 AI",
        }
        if "t1" in tier_list and "t3" in tier_list:
            tier_badge = "Tier 1-3" if not is_ar else "المستويات 1-3"
        elif "t2" in tier_list and "t3" in tier_list:
            tier_badge = "Tier 2-3" if not is_ar else "المستويات 2-3"
        elif "t4" in tier_list:
            tier_badge = "Tier 4 AI" if not is_ar else "المستوى 4 ذكاء اصطناعي"
        else:
            tier_badge = tier_badges_labels.get(tier_list[0], "Standard")

        short_phase_en = phase_name_en.split(".")[1].strip().split("&")[0].strip() if "." in phase_name_en else phase_name_en
        short_phase_ar = phase_name_ar.split(".")[1].strip().split("و")[0].strip() if "." in phase_name_ar else phase_name_ar
        phase_badge = f"{phase} {short_phase_en}" if not is_ar else f"{phase} {short_phase_ar}"

        desc_en = f"Standard {name_en} deliverable and specification within {short_phase_en}. Includes bilingual markdown template, OKF data schema, and authoring guide."
        desc_ar = f"تسليمة معتمدة لـ {name_ar} ضمن مرحلة {short_phase_ar}. تتضمن قالب ماركداون ثنائي اللغة، مخطط بيانات OKF، ودليلاً إرشادياً تطبيقياً."
        desc = desc_ar if is_ar else desc_en

        search_tokens = f"{code_form} {code_pmo} {code_raw} {name_en} {name_ar} {phase_name_en} {phase_name_ar} {phase} pmi pmbok iso nist okf"
        
        url_tpl = f"{rel_root}{d.get('url_tpl_ar' if is_ar else 'url_tpl_en', '')}"
        url_guide = f"{rel_root}{d.get('url_guide_ar' if is_ar else 'url_guide_en', '')}"

        tag1 = "PMBOK 7/8"
        tag2 = "Schema OKF" if "04" in phase or "06" in phase else "ISO 21500"
        tag3 = "5-File Bundle"

        card = f"""<div class="deliverable-card group bg-surface-container-lowest rounded-xl p-space-md shadow-sm hover:shadow-md transition-all flex flex-col justify-between" 
     data-code="{code_form}" 
     data-code-alt="{code_pmo}" 
     data-phase="{phase}" 
     data-tier="{data_tier}" 
     data-search="{pyhtml.escape(search_tokens.lower())}">
  <div class="space-y-space-sm">
    <div class="flex items-center justify-between">
      <span class="font-label-code text-badge-caps px-2 py-0.5 rounded bg-surface-container-high text-on-surface font-bold">{code_form}</span>
      <div class="flex items-center gap-1">
        <span class="px-2 py-0.5 rounded text-badge-caps font-badge-caps bg-surface-container text-secondary">{phase_badge}</span>
        <span class="px-1.5 py-0.5 rounded text-badge-caps font-badge-caps bg-secondary/15 text-secondary">{tier_badge}</span>
      </div>
    </div>
    <div>
      {f'''<h2 class="font-headline-sm text-headline-sm text-on-surface group-hover:text-secondary transition-colors" dir="rtl">{pyhtml.escape(name_ar)}</h2>
      <div class="font-body-sm text-body-sm text-on-surface-variant font-medium mt-0.5" dir="ltr">{pyhtml.escape(name_en)}</div>''' if is_ar else f'''<h2 class="font-headline-sm text-headline-sm text-on-surface group-hover:text-secondary transition-colors">{pyhtml.escape(name_en)}</h2>
      <div class="font-body-sm text-body-sm text-on-surface-variant font-medium mt-0.5" dir="rtl">{pyhtml.escape(name_ar)}</div>'''}
    </div>
    <p class="font-body-sm text-body-sm text-on-surface-variant line-clamp-2">
      {pyhtml.escape(desc)}
    </p>
    <div class="flex items-center gap-1.5 flex-wrap pt-1 font-label-code text-[11px] text-on-surface-variant">
      <span class="bg-surface-container-low px-1.5 py-0.5 rounded">{tag1}</span>
      <span class="bg-surface-container-low px-1.5 py-0.5 rounded">{tag2}</span>
      <span class="bg-surface-container-low px-1.5 py-0.5 rounded">{tag3}</span>
    </div>
  </div>
  <div class="pt-space-md mt-space-sm flex items-center justify-between border-t border-surface-container-high/40">
    <button class="inline-flex items-center gap-1 text-label-code font-label-code text-secondary hover:text-on-surface font-bold transition-colors" onclick="openFormDrawer('{code_pmo}')">
      <span class="material-symbols-outlined text-[17px]">visibility</span>
      <span>{'معاينة التسليمة' if is_ar else 'Inspect Spec'}</span>
    </button>
    <div class="flex items-center gap-1">
      <button class="p-1.5 rounded-lg bg-surface-container-low hover:bg-surface-container text-on-surface-variant hover:text-on-surface transition-colors" onclick="copySnippet('{code_form}')" title="{'نسخ أمر CLI' if is_ar else 'Copy CLI Command'}">
        <span class="material-symbols-outlined text-[18px]">content_copy</span>
      </button>
      <a class="p-1.5 rounded-lg bg-surface-container-low hover:bg-surface-container text-on-surface-variant hover:text-on-surface transition-colors inline-flex items-center" href="{url_tpl}" title="{'عرض القالب المعتمد' if is_ar else 'View Markdown Template'}">
        <span class="material-symbols-outlined text-[18px]">description</span>
      </a>
      <a class="p-1.5 rounded-lg bg-surface-container-low hover:bg-surface-container text-on-surface-variant hover:text-on-surface transition-colors inline-flex items-center" href="{url_guide}" title="{'عرض الدليل الإرشادي' if is_ar else 'View Practice Guide'}">
        <span class="material-symbols-outlined text-[18px]">menu_book</span>
      </a>
    </div>
  </div>
</div>"""
        cards_html.append(card)

    rendered_cards = "\n".join(cards_html)

    # Dynamic language variables
    doc_lang = "ar" if is_ar else "en"
    doc_dir = "rtl" if is_ar else "ltr"
    page_title = "كتالوج النماذج والتسليمات القياسية (102 تسليمة) | مستكشف تسليمات" if is_ar else "102 Deliverables & Templates Catalog | Tasleemat PMO Explorer"
    
    sidebar_class = "fixed right-0 top-16 bottom-0 w-64 bg-surface-container-low z-40 border-l border-surface-container-high overflow-y-auto p-space-md" if is_ar else "fixed left-0 top-16 bottom-0 w-64 bg-surface-container-low z-40 border-r border-surface-container-high overflow-y-auto p-space-md"
    main_wrapper_class = "pr-64" if is_ar else "pl-64"

    nav_home = f"{rel_root}README_AR.html" if is_ar else f"{rel_root}index.html"
    nav_gov = f"{rel_root}governance.html"
    nav_tailor = f"{rel_root}governance.html#tailoring-matrix"
    nav_dev = f"{rel_root}developer.html"
    nav_lex = f"{rel_root}developer.html#lexicon"
    lang_toggle_url = "../en/index.html" if is_ar else "../ar/index.html"
    lang_toggle_text = "🇬🇧 English" if is_ar else "🇸🇦 العربية"

    hero_badge = "متوافق مع PMI PMBOK® 6/7/8th و ISO 21500 و هيئة الحكومة الرقمية" if is_ar else "PMI PMBOK® 6/7/8th & ISO 21500 Aligned"
    hero_title = "فهرس النماذج والتسليمات القياسية الموحدة" if is_ar else "Bilingual Deliverables & Templates Catalog"
    hero_subtitle = "Bilingual Deliverables & Templates Catalog (102 Forms)" if is_ar else "فهرس نماذج وتسليمات المشاريع الموحدة (102 تسليمة)"
    hero_desc = "استكشف وابحث وفلتر كافة النماذج القياسية الـ 102 لمكاتب إدارة المشاريع (PMO)، المتوفرة بحزم ماركداون ثنائية اللغة، ومخططات بيانات OKF JSON، وضوابط حوكمة الذكاء الاصطناعي NIST AI RMF." if is_ar else "Search, filter, and inspect all 102 standardized PMO forms with synchronized English & Arabic markdown bundles, OKF JSON data schemas, and NIST AI RMF governance controls."

    search_placeholder = "ابحث باسم النموذج، الرمز (مثل FORM-03-01)، الكلمة المفتاحية، أو المرحلة..." if is_ar else "Search templates by name, code (e.g. FORM-03-01), keyword or Arabic term..."
    filter_phase_label = "تصفية حسب المرحلة (دورة حياة المشروع)" if is_ar else "Filter By Phase (Project Lifecycle)"
    filter_tier_label = "مستوى التخصيص الحوكمي:" if is_ar else "Tailoring Tier:"
    showing_label_init = f"عرض {len(deliverables)} تسليمة من إجمالي {len(deliverables)}" if is_ar else f"Showing {len(deliverables)} of {len(deliverables)} Deliverables"

    phase_btns = [
        ("all", "الكل (102)" if is_ar else "All (102)"),
        ("00", "00 إدارة المحفظة (6)" if is_ar else "00 Portfolio (6)"),
        ("01", "01 دراسة الجدوى (4)" if is_ar else "01 Business (4)"),
        ("02", "02 المنهجية والتخصيص (6)" if is_ar else "02 Approach (6)"),
        ("03", "03 البدء (5)" if is_ar else "03 Initiating (5)"),
        ("04", "04 التخطيط (52)" if is_ar else "04 Planning (52)"),
        ("05", "05 التنفيذ (12)" if is_ar else "05 Executing (12)"),
        ("06", "06 المراقبة والتحكم (12)" if is_ar else "06 Controlling (12)"),
        ("07", "07 الإغلاق (5)" if is_ar else "07 Closing (5)"),
    ]
    phase_btns_html = "\n".join([
        f'<button class="phase-btn {"active" if p[0] == "all" else ""} px-3 py-1.5 rounded-lg text-label-code font-label-code whitespace-nowrap {"bg-primary text-on-primary" if p[0] == "all" else "bg-surface-container-low text-on-surface hover:bg-surface-container"} transition-all" data-phase="{p[0]}" onclick="filterPhase(\'{p[0]}\')">{p[1]}</button>'
        for p in phase_btns
    ])

    tier_btns = [
        ("all", "كافة المستويات" if is_ar else "All Tiers"),
        ("t1", "المستوى 1: مصغر (7)" if is_ar else "Tier 1: Small (7)"),
        ("t2", "المستوى 2: أساسي (22)" if is_ar else "Tier 2: Core (22)"),
        ("t3", "المستوى 3: مؤسسي (78)" if is_ar else "Tier 3: Enterprise (78)"),
        ("t4", "المستوى 4: مرن / ذكاء اصطناعي (32)" if is_ar else "Tier 4: Agile/AI (32)"),
    ]
    tier_btns_html = "\n".join([
        f'<button class="tier-btn {"active" if t[0] == "all" else ""} px-2.5 py-1 rounded text-badge-caps font-badge-caps {"bg-surface-container-highest text-on-surface" if t[0] == "all" else "bg-surface-container-low text-on-surface hover:bg-surface-container"} transition-all" data-tier="{t[0]}" onclick="filterTier(\'{t[0]}\')">{t[1]}</button>'
        for t in tier_btns
    ])

    return f"""<!DOCTYPE html>
<html lang="{doc_lang}" dir="{doc_dir}">
<head>
  <meta charset="utf-8"/>
  <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
  <meta content="web_dashboard" name="shell-type"/>
  <title>{page_title}</title>
  <link rel="icon" type="image/png" href="{rel_root}img/logo.png"/>
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet"/>
  <link href="https://fonts.googleapis.com" rel="preconnect"/>
  <link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&family=Noto+Sans+Arabic:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
  <style>
    @layer base {{
      html, body {{ margin: 0; padding: 0; }}
      body {{ overscroll-behavior: none; }}
      main > :first-child {{ margin-top: 0 !important; }}
      main > :last-child {{ margin-bottom: 0 !important; }}
    }}
    ::-webkit-scrollbar {{ display: none; }}
  </style>
  <script src="https://cdn.tailwindcss.com"></script>
  <script id="tailwind-config">
    tailwind.config = {{
      darkMode: "class",
      theme: {{
        extend: {{
          colors: {{
            "on-primary-container": "#7b83a0",
            "on-error-container": "#93000a",
            "outline-variant": "#c6c6ce",
            "on-primary-fixed": "#131a33",
            "on-surface": "#131b2e",
            "surface-container-highest": "#dae2fd",
            "error": "#ba1a1a",
            "on-surface-variant": "#45464d",
            "on-tertiary": "#ffffff",
            "primary": "#000000",
            "surface-container-low": "#f2f3ff",
            "surface-tint": "#565d79",
            "background": "#faf8ff",
            "primary-fixed": "#dbe1ff",
            "on-secondary": "#ffffff",
            "on-error": "#ffffff",
            "on-tertiary-fixed": "#2a1700",
            "surface-container": "#eaedff",
            "inverse-surface": "#283044",
            "secondary": "#006a61",
            "primary-fixed-dim": "#bec5e5",
            "on-background": "#131b2e",
            "outline": "#76767e",
            "surface-container-high": "#e2e7ff",
            "inverse-on-surface": "#eef0ff",
            "on-primary": "#ffffff",
            "surface": "#faf8ff",
            "surface-bright": "#faf8ff",
            "tertiary-fixed": "#ffddb8",
            "on-secondary-fixed-variant": "#005049",
            "surface-variant": "#dae2fd",
            "tertiary-fixed-dim": "#ffb95f",
            "inverse-primary": "#bec5e5",
            "on-secondary-container": "#006f66",
            "on-primary-fixed-variant": "#3e4660",
            "error-container": "#ffdad6",
            "tertiary": "#000000",
            "surface-container-lowest": "#ffffff",
            "surface-dim": "#d2d9f4",
            "on-secondary-fixed": "#00201d",
            "primary-container": "#131a33",
            "secondary-fixed-dim": "#6bd8cb",
            "on-tertiary-fixed-variant": "#653e00",
            "secondary-fixed": "#89f5e7",
            "secondary-container": "#86f2e4",
            "tertiary-container": "#2a1700",
            "on-tertiary-container": "#b87500"
          }},
          borderRadius: {{ DEFAULT: "0.25rem", lg: "0.5rem", xl: "0.75rem", full: "9999px" }},
          spacing: {{ "margin-tablet": "1.5rem", "space-xs": "0.25rem", "margin-desktop": "2rem", "margin": "1rem", "gutter-desktop": "1.5rem", "space-2xl": "3rem", "space-lg": "1.5rem", "space-sm": "0.5rem", "gutter": "1rem", "space-xl": "2rem", "space-md": "1rem" }},
          fontFamily: {{
            "headline-lg": ["IBM Plex Sans", "Noto Sans Arabic", "sans-serif"],
            "badge-caps": ["JetBrains Mono", "monospace"],
            "body-base": ["Inter", "Noto Sans Arabic", "sans-serif"],
            "display-hero-mobile": ["IBM Plex Sans", "Noto Sans Arabic", "sans-serif"],
            "headline-sm": ["IBM Plex Sans", "Noto Sans Arabic", "sans-serif"],
            "label-code": ["JetBrains Mono", "monospace"],
            "display-hero": ["IBM Plex Sans", "Noto Sans Arabic", "sans-serif"],
            "body-sm": ["Inter", "Noto Sans Arabic", "sans-serif"],
            "headline-md": ["IBM Plex Sans", "Noto Sans Arabic", "sans-serif"]
          }},
          fontSize: {{
            "headline-lg": ["24px", {{ lineHeight: "32px", letterSpacing: "-0.015em", fontWeight: "700" }}],
            "badge-caps": ["11px", {{ lineHeight: "14px", letterSpacing: "0.03em", fontWeight: "600" }}],
            "body-base": ["15px", {{ lineHeight: "24px", fontWeight: "400" }}],
            "display-hero-mobile": ["28px", {{ lineHeight: "36px", letterSpacing: "-0.02em", fontWeight: "800" }}],
            "headline-sm": ["16px", {{ lineHeight: "24px", letterSpacing: "-0.005em", fontWeight: "600" }}],
            "label-code": ["12px", {{ lineHeight: "16px", letterSpacing: "0.02em", fontWeight: "700" }}],
            "display-hero": ["36px", {{ lineHeight: "44px", letterSpacing: "-0.025em", fontWeight: "800" }}],
            "body-sm": ["13.5px", {{ lineHeight: "20px", fontWeight: "400" }}],
            "headline-md": ["20px", {{ lineHeight: "28px", letterSpacing: "-0.01em", fontWeight: "700" }}]
          }}
        }}
      }}
    }};
  </script>
  <script src="{rel_root}assets/tasleemat_data.js"></script>
</head>
<body class="bg-background font-body-base text-body-base text-on-surface antialiased">
  <!-- Top Navigation Header -->
  <header class="fixed top-0 left-0 right-0 w-full h-16 z-50 bg-surface-container-lowest/90 backdrop-blur-md shadow-[0_1px_8px_rgba(0,0,0,0.04)] border-b border-surface-container-high">
    <div class="h-16 w-full px-margin md:px-margin-tablet lg:px-margin-desktop flex items-center justify-between gap-space-md">
      <div class="flex items-center gap-space-md">
        <a class="flex items-center gap-space-sm" data-path="overview" href="{nav_home}">
          <img alt="Tasleemat PMO Logo" class="h-8 w-auto object-contain" src="{rel_root}img/logo.png"/>
          <span class="font-headline-sm text-headline-sm text-on-surface tracking-tight">Tasleemat (تسليمات)</span>
        </a>
        <span class="inline-flex items-center px-space-xs py-0.5 rounded bg-surface-container text-on-surface-variant font-label-code text-label-code border border-outline-variant/40">v2.0.2</span>
      </div>
      <div class="flex items-center gap-space-sm">
        <a class="inline-flex items-center gap-1 px-space-sm py-1 rounded-lg border border-outline-variant/60 bg-surface-container-low text-on-surface font-label-code text-label-code hover:bg-surface-container transition-colors" href="{lang_toggle_url}">
          <span>{lang_toggle_text}</span>
        </a>
        <a class="hidden sm:inline-flex items-center gap-1.5 px-space-sm py-1 rounded-lg bg-surface-container text-on-surface-variant font-label-code text-label-code border border-outline-variant/40 hover:bg-surface-container-high hover:text-on-surface transition-colors" href="https://github.com/fakhruldeen/Tasleemat" target="_blank" rel="noopener noreferrer">
          <span class="text-sm leading-none">★</span><span>GitHub</span><span class="text-outline-variant">|</span><span>v2.0.2</span>
        </a>
      </div>
    </div>
  </header>

  <!-- Sidebar -->
  <aside class="{sidebar_class}">
    <div class="mb-space-md px-space-sm">
      <span class="font-badge-caps text-badge-caps uppercase tracking-wider text-on-surface-variant">{'التنقل والحوكمة' if is_ar else 'Navigation & Governance'}</span>
    </div>
    <nav class="flex flex-col gap-space-xs" data-active-classes="bg-surface-container-high text-on-surface font-semibold rounded-lg">
      <a class="flex items-center gap-space-sm px-space-sm py-2 rounded-lg text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors" data-path="overview" href="{nav_home}">
        <span class="material-symbols-outlined text-[18px]">home</span>
        <span class="font-body-sm text-body-sm">{'الرئيسية / نظرة عامة' if is_ar else 'Home / Overview'}</span>
      </a>
      <a aria-current="page" class="flex items-center gap-space-sm px-space-sm py-2 transition-colors bg-surface-container-high text-on-surface font-semibold rounded-lg" data-path="templates-catalog" href="./index.html">
        <span class="material-symbols-outlined text-[18px]">library_books</span>
        <span class="font-body-sm text-body-sm">{'فهرس النماذج (102 تسليمة)' if is_ar else '102 Templates Catalog'}</span>
      </a>
      <a class="flex items-center gap-space-sm px-space-sm py-2 rounded-lg text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors" data-path="stage-gate-governance" href="{nav_gov}">
        <span class="material-symbols-outlined text-[18px]">verified</span>
        <span class="font-body-sm text-body-sm">{'بوابات العبور الحوكمية' if is_ar else 'Stage-Gate Governance'}</span>
      </a>
      <a class="flex items-center gap-space-sm px-space-sm py-2 rounded-lg text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors" data-path="tailoring-profiles" href="{nav_tailor}">
        <span class="material-symbols-outlined text-[18px]">tune</span>
        <span class="font-body-sm text-body-sm">{'مستويات التخصيص' if is_ar else 'Tailoring Profiles'}</span>
      </a>
      <a class="flex items-center gap-space-sm px-space-sm py-2 rounded-lg text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors" data-path="developer-cli" href="{nav_dev}">
        <span class="material-symbols-outlined text-[18px]">terminal</span>
        <span class="font-body-sm text-body-sm">{'دليل المطورين وCLI' if is_ar else 'Developer & CLI'}</span>
      </a>
      <a class="flex items-center gap-space-sm px-space-sm py-2 rounded-lg text-on-surface-variant hover:bg-surface-container hover:text-on-surface transition-colors" data-path="bilingual-lexicon" href="{nav_lex}">
        <span class="material-symbols-outlined text-[18px]">translate</span>
        <span class="font-body-sm text-body-sm">{'المعجم الموحد للمصطلحات' if is_ar else 'Bilingual Lexicon'}</span>
      </a>
    </nav>
  </aside>

  <!-- Main Content Container -->
  <div class="{main_wrapper_class}">
    <main class="w-full pt-16 bg-background min-h-screen px-space-md py-space-lg">
      <div class="flex flex-col w-full">
        <div class="max-w-[1400px] w-full mx-auto space-y-space-lg pb-space-2xl">
          <!-- Hero / Metrics Ribbon -->
          <div class="relative overflow-hidden rounded-xl bg-surface-container-lowest p-space-lg shadow-sm">
            <div class="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-space-lg">
              <div class="max-w-3xl space-y-space-xs">
                <div class="inline-flex items-center gap-2 px-2.5 py-1 rounded-full bg-surface-container text-secondary font-label-code text-badge-caps uppercase tracking-wider">
                  <span class="inline-block w-2 h-2 rounded-full bg-secondary animate-pulse"></span>
                  {hero_badge}
                </div>
                <h1 class="font-headline-lg text-headline-lg text-on-surface tracking-tight">
                  {hero_title}
                  <span class="block text-secondary font-body-base text-body-base mt-1" dir="{'ltr' if is_ar else 'rtl'}">{hero_subtitle}</span>
                </h1>
                <p class="font-body-base text-body-base text-on-surface-variant leading-relaxed">
                  {hero_desc}
                </p>
              </div>
              <!-- Quick Lifecycle Counter Chips -->
              <div class="flex flex-wrap sm:flex-nowrap gap-space-sm items-center">
                <div class="p-space-sm rounded-lg bg-surface-container-low text-center min-w-[90px]">
                  <span class="block font-headline-md text-headline-md text-on-surface">102</span>
                  <span class="font-label-code text-badge-caps text-on-surface-variant">{'نماذج قياسية' if is_ar else 'FORMS'}</span>
                </div>
                <div class="p-space-sm rounded-lg bg-surface-container-low text-center min-w-[90px]">
                  <span class="block font-headline-md text-headline-md text-secondary">204</span>
                  <span class="font-label-code text-badge-caps text-on-surface-variant">{'حزم ثنائية' if is_ar else 'BUNDLES (EN/AR)'}</span>
                </div>
                <div class="p-space-sm rounded-lg bg-surface-container-low text-center min-w-[90px]">
                  <span class="block font-headline-md text-headline-md text-on-surface">8</span>
                  <span class="font-label-code text-badge-caps text-on-surface-variant">{'مراحل' if is_ar else 'PHASES'}</span>
                </div>
                <div class="p-space-sm rounded-lg bg-surface-container-low text-center min-w-[90px]">
                  <span class="block font-headline-md text-headline-md text-secondary">4</span>
                  <span class="font-label-code text-badge-caps text-on-surface-variant">{'مستويات' if is_ar else 'TIERS'}</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Live Filter & Control Deck -->
          <div class="bg-surface-container-lowest rounded-xl p-space-md shadow-sm space-y-space-md">
            <!-- Search row & high-level toggles -->
            <div class="flex flex-col md:flex-row gap-space-md items-stretch md:items-center justify-between">
              <!-- Search bar with kbd -->
              <div class="relative flex-1 max-w-2xl">
                <span class="material-symbols-outlined absolute {'right-3' if is_ar else 'left-3'} top-1/2 -translate-y-1/2 text-outline text-[20px]">search</span>
                <input class="w-full bg-surface-container-low text-on-surface {'pr-10 pl-16' if is_ar else 'pl-10 pr-16'} py-2.5 rounded-lg text-body-sm font-body-sm focus:outline-none focus:bg-surface-container-lowest focus:ring-2 focus:ring-secondary/40 transition-all placeholder:text-outline" 
                       id="template-search" 
                       placeholder="{search_placeholder}" 
                       type="text"/>
                <div class="absolute {'left-3' if is_ar else 'right-3'} top-1/2 -translate-y-1/2 hidden sm:flex items-center gap-1 font-label-code text-[11px] text-on-surface-variant bg-surface-container px-1.5 py-0.5 rounded">
                  <span>/</span>
                </div>
              </div>
              <!-- Utility Action Buttons -->
              <div class="flex items-center gap-space-sm flex-wrap">
                <div class="inline-flex items-center rounded-lg bg-surface-container-low p-1 text-on-surface-variant">
                  <button class="px-2.5 py-1 rounded text-badge-caps font-badge-caps bg-surface-container-lowest text-on-surface shadow-xs transition-all flex items-center gap-1" id="view-mode-dual" onclick="setDualMode('dual')">
                    <span class="material-symbols-outlined text-[15px]">splitscreen</span>
                    <span>{'عرض مزدوج' if is_ar else 'Dual View'}</span>
                  </button>
                  <button class="px-2.5 py-1 rounded text-badge-caps font-badge-caps hover:text-on-surface transition-all flex items-center gap-1" id="view-mode-en" onclick="setDualMode('en')">
                    <span>English</span>
                  </button>
                  <button class="px-2.5 py-1 rounded text-badge-caps font-badge-caps hover:text-on-surface transition-all flex items-center gap-1" id="view-mode-ar" onclick="setDualMode('ar')">
                    <span>العربية</span>
                  </button>
                </div>
                <!-- Quick Actions / Scaffolder Trigger -->
                <button class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-surface-container text-on-surface hover:bg-surface-container-high transition-colors font-label-code text-label-code" onclick="openScaffolderModal()">
                  <span class="material-symbols-outlined text-[17px]">terminal</span>
                  <span>{'أداة Scaffolder' if is_ar else 'CLI Scaffolder'}</span>
                </button>
                <button class="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-primary text-on-primary hover:opacity-90 transition-opacity font-label-code text-label-code" onclick="batchExportZip()">
                  <span class="material-symbols-outlined text-[17px]">folder_zip</span>
                  <span>{'تصدير الحزمة (.ZIP)' if is_ar else 'Export Pack (.ZIP)'}</span>
                </button>
              </div>
            </div>

            <!-- Phase Selector Pills -->
            <div class="space-y-space-xs">
              <div class="flex items-center justify-between text-on-surface-variant">
                <span class="font-badge-caps text-badge-caps uppercase tracking-wider">{filter_phase_label}</span>
                <span class="font-label-code text-badge-caps text-secondary font-bold" id="active-count-label">{showing_label_init}</span>
              </div>
              <div class="flex items-center gap-1.5 overflow-x-auto pb-1" id="phase-filter-bar">
                {phase_btns_html}
              </div>
            </div>

            <!-- Secondary Filters: Tiers and Formats -->
            <div class="flex flex-wrap items-center justify-between gap-space-sm pt-space-xs border-t border-surface-container-high/40">
              <div class="flex items-center gap-space-sm flex-wrap">
                <span class="font-badge-caps text-badge-caps uppercase tracking-wider text-on-surface-variant">{filter_tier_label}</span>
                <div class="flex items-center gap-1">
                  {tier_btns_html}
                </div>
              </div>
              <div class="flex items-center gap-space-sm text-on-surface-variant font-label-code text-badge-caps">
                <span>{'الحزم المتضمنة:' if is_ar else 'Format Assets Included:'}</span>
                <span class="inline-flex items-center gap-1 bg-surface-container px-2 py-0.5 rounded text-on-surface">
                  <span class="material-symbols-outlined text-[13px] text-secondary">check</span> Markdown .md
                </span>
                <span class="inline-flex items-center gap-1 bg-surface-container px-2 py-0.5 rounded text-on-surface">
                  <span class="material-symbols-outlined text-[13px] text-secondary">check</span> OKF JSON
                </span>
                <span class="inline-flex items-center gap-1 bg-surface-container px-2 py-0.5 rounded text-on-surface">
                  <span class="material-symbols-outlined text-[13px] text-secondary">check</span> AI Prompt
                </span>
              </div>
            </div>
          </div>

          <!-- Deliverables Grid / Catalog View (All 102 Cards) -->
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-space-md" id="catalog-card-grid">
            {rendered_cards}
          </div>

          <!-- Empty State (Hidden by default) -->
          <div class="hidden p-space-2xl text-center bg-surface-container-lowest rounded-xl space-y-space-sm" id="no-results-state">
            <span class="material-symbols-outlined text-[48px] text-outline">search_off</span>
            <h3 class="font-headline-sm text-headline-sm text-on-surface">{'لم يتم العثور على أي تسليمات' if is_ar else 'No deliverables found'}</h3>
            <p class="font-body-sm text-body-sm text-on-surface-variant max-w-md mx-auto">
              {'لا توجد نماذج تسليمات تطابق معايير البحث أو تصفيات المراحل والمستويات المحددة. جرب كلمة بحث أخرى أو أعد تعيين الفلاتر.' if is_ar else 'No PMO forms match your active search terms and tier filters. Clear filters or explore other lifecycle phases.'}
            </p>
            <button class="px-4 py-2 bg-surface-container-high rounded-lg text-label-code font-label-code text-on-surface hover:bg-surface-container transition-colors" onclick="resetAllFilters()">
              {'إعادة تعيين كافة الفلاتر' if is_ar else 'Reset All Filters'}
            </button>
          </div>

          <!-- Enterprise Standards Compliance Banner -->
          <div class="bg-surface-container-low rounded-xl p-space-lg flex flex-col md:flex-row items-start md:items-center justify-between gap-space-md">
            <div class="space-y-1">
              <span class="font-badge-caps text-badge-caps uppercase tracking-wider text-secondary font-bold">{'مصفوفة الامتثال والمعايير الدولية' if is_ar else 'Standard Alignment Matrix'}</span>
              <h3 class="font-headline-sm text-headline-sm text-on-surface">{'الاعتماد المؤسسي والتوثيق القياسي' if is_ar else 'Institutional Compliance & Certifications'}</h3>
              <p class="font-body-sm text-body-sm text-on-surface-variant">
                {'كل نموذج ومخرج مصمم ليتوافق بدقة مع معايير ISO 21500 / 21502، ومجالات الأداء في PMBOK 7/8، وأطر حوكمة الذكاء الاصطناعي NIST AI RMF.' if is_ar else 'Every form is structured to meet auditable ISO 21500 / 21502 tranches, PMBOK 7th performance domains, and NIST AI RMF governance frameworks.'}
              </p>
            </div>
            <div class="flex items-center gap-2 flex-wrap">
              <span class="px-3 py-1.5 rounded-lg bg-surface-container-lowest text-on-surface font-label-code text-label-code shadow-xs">PMI PMBOK® 8th Ready</span>
              <span class="px-3 py-1.5 rounded-lg bg-surface-container-lowest text-on-surface font-label-code text-label-code shadow-xs">ISO 21500:2021</span>
              <span class="px-3 py-1.5 rounded-lg bg-surface-container-lowest text-on-surface font-label-code text-label-code shadow-xs">NIST AI 100-1</span>
              <span class="px-3 py-1.5 rounded-lg bg-surface-container-lowest text-on-surface font-label-code text-label-code shadow-xs">ESG / UN SDGs</span>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>

  <!-- Multi-Artifact Slide-Over Drawer / Inspector Modal -->
  <div class="fixed inset-0 z-50 pointer-events-none opacity-0 transition-opacity duration-300" id="artifact-drawer">
    <div class="absolute inset-0 bg-on-surface/40 backdrop-blur-xs transition-opacity cursor-pointer" onclick="closeFormDrawer()"></div>
    <div class="absolute top-0 {'left-0 -translate-x-full' if is_ar else 'right-0 translate-x-full'} bottom-0 w-full max-w-4xl bg-surface-container-lowest shadow-2xl flex flex-col transition-transform duration-300 ease-out pointer-events-auto" id="drawer-panel">
      <!-- Drawer Header -->
      <div class="p-space-md bg-surface-container-low flex items-center justify-between gap-space-md border-b border-surface-container-high">
        <div class="flex items-center gap-space-sm min-w-0">
          <span class="font-label-code text-label-code px-2 py-0.5 rounded bg-primary text-on-primary" id="drawer-code">FORM-03-01</span>
          <div class="min-w-0">
            <h2 class="font-headline-sm text-headline-sm text-on-surface truncate" id="drawer-title-primary">Project Charter Spec</h2>
            <p class="font-body-sm text-body-sm text-secondary truncate" id="drawer-title-secondary">ميثاق المشروع والاعتماد الرسمي</p>
          </div>
        </div>
        <div class="flex items-center gap-2 flex-shrink-0">
          <button class="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-surface-container text-on-surface hover:bg-surface-container-high font-label-code text-label-code transition-colors" onclick="copyCurrentBundle()">
            <span class="material-symbols-outlined text-[16px]">content_copy</span>
            <span>{'نسخ الحزمة' if is_ar else 'Copy Bundle'}</span>
          </button>
          <button class="p-1.5 rounded-lg hover:bg-surface-container text-on-surface-variant hover:text-on-surface transition-colors" onclick="closeFormDrawer()">
            <span class="material-symbols-outlined text-[20px]">close</span>
          </button>
        </div>
      </div>

      <!-- Drawer Tabs -->
      <div class="px-space-md bg-surface-container-low flex items-center gap-2 overflow-x-auto border-b border-surface-container-high">
        <button class="drawer-tab active px-3 py-2 text-label-code font-label-code text-on-surface bg-surface-container-lowest rounded-t-lg transition-colors" id="tab-btn-spec" onclick="switchTab('spec')">
          {'الهيكل والبيانات' if is_ar else 'Bilingual Schema'}
        </button>
        <button class="drawer-tab px-3 py-2 text-label-code font-label-code text-on-surface-variant hover:text-on-surface transition-colors" id="tab-btn-template" onclick="switchTab('template')">
          {'قالب ماركداون' if is_ar else 'Markdown Template'}
        </button>
        <button class="drawer-tab px-3 py-2 text-label-code font-label-code text-on-surface-variant hover:text-on-surface transition-colors" id="tab-btn-guide" onclick="switchTab('guide')">
          {'الدليل الإرشادي' if is_ar else 'Practice Guide'}
        </button>
        <button class="drawer-tab px-3 py-2 text-label-code font-label-code text-on-surface-variant hover:text-on-surface transition-colors" id="tab-btn-prompt" onclick="switchTab('prompt')">
          {'موجه الذكاء الاصطناعي' if is_ar else 'AI Prompt'}
        </button>
        <button class="drawer-tab px-3 py-2 text-label-code font-label-code text-on-surface-variant hover:text-on-surface transition-colors" id="tab-btn-cli" onclick="switchTab('cli')">
          CLI & SDK
        </button>
      </div>

      <!-- Drawer Body -->
      <div class="flex-1 overflow-y-auto p-space-lg space-y-space-lg bg-surface-container-lowest" id="drawer-body-container">
        <div class="tab-pane space-y-space-md" id="tab-content-spec"></div>
        <div class="tab-pane hidden space-y-space-md" id="tab-content-template"></div>
        <div class="tab-pane hidden space-y-space-md" id="tab-content-guide"></div>
        <div class="tab-pane hidden space-y-space-md" id="tab-content-prompt"></div>
        <div class="tab-pane hidden space-y-space-md" id="tab-content-cli"></div>
      </div>

      <!-- Drawer Footer -->
      <div class="p-space-md bg-surface-container-low flex items-center justify-between border-t border-surface-container-high">
        <span class="font-label-code text-xs text-on-surface-variant">{'حزمة متزامنة: 5 ملفات موثقة (.md, .json, .prompt, .py)' if is_ar else 'Bundle: 5 Synchronized Files (.md, .json, .prompt, .py)'}</span>
        <div class="flex items-center gap-space-sm">
          <button class="px-4 py-2 rounded-lg bg-surface-container hover:bg-surface-container-high text-on-surface font-label-code text-label-code transition-colors" onclick="closeFormDrawer()">
            {'إغلاق' if is_ar else 'Close Inspector'}
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- CLI Scaffolder Modal -->
  <div class="fixed inset-0 z-50 pointer-events-none opacity-0 transition-opacity duration-200" id="scaffolder-modal">
    <div class="absolute inset-0 bg-on-surface/50 backdrop-blur-xs cursor-pointer" onclick="closeScaffolderModal()"></div>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full max-w-xl bg-surface-container-lowest rounded-xl shadow-2xl p-space-lg space-y-space-md pointer-events-auto">
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="material-symbols-outlined text-secondary text-[24px]">terminal</span>
          <h3 class="font-headline-sm text-headline-sm text-on-surface">{'مساعد أوامر CLI لتسليمات' if is_ar else 'Tasleemat CLI Scaffolder Helper'}</h3>
        </div>
        <button class="p-1 rounded hover:bg-surface-container text-on-surface-variant" onclick="closeScaffolderModal()">
          <span class="material-symbols-outlined text-[20px]">close</span>
        </button>
      </div>
      <p class="font-body-sm text-body-sm text-on-surface-variant">
        {'حدد خصائص مشروعك لتوليد الأمر التنفيذي التلقائي لإنشاء كافة مجلدات وتسليمات المشروع:' if is_ar else 'Configure your project attributes to generate the automated terminal command for scaffolding full delivery structures:'}
      </p>
      <div class="space-y-space-sm">
        <div>
          <label class="block font-label-code text-badge-caps uppercase tracking-wider text-on-surface-variant mb-1">{'مستوى الحوكمة (Tier)' if is_ar else 'Tailoring Tier'}</label>
          <select class="w-full bg-surface-container-low px-3 py-2 rounded-lg text-body-sm font-body-sm focus:outline-none" id="cli-tier-select">
            <option value="1">Tier 1: Small Project (5 Core Artifacts)</option>
            <option selected="" value="2">Tier 2: Standard Core (18 Artifacts)</option>
            <option value="3">Tier 3: Enterprise Program (45+ Artifacts)</option>
            <option value="4">Tier 4: Agile / AI Governance (25 Artifacts)</option>
          </select>
        </div>
        <div>
          <label class="block font-label-code text-badge-caps uppercase tracking-wider text-on-surface-variant mb-1">{'حزمة اللغة' if is_ar else 'Language Pack'}</label>
          <select class="w-full bg-surface-container-low px-3 py-2 rounded-lg text-body-sm font-body-sm focus:outline-none" id="cli-lang-select">
            <option selected="" value="both">Dual Bundle (English + العربية)</option>
            <option value="ar">Arabic Only (العربية فقط)</option>
            <option value="en">English Only</option>
          </select>
        </div>
        <div>
          <label class="block font-label-code text-badge-caps uppercase tracking-wider text-on-surface-variant mb-1">{'اسم المشروع (أو المجلد)' if is_ar else 'Project Name (or Directory)'}</label>
          <input class="w-full bg-surface-container-low px-3 py-2 rounded-lg text-body-sm font-body-sm focus:outline-none" id="cli-name-input" type="text" value="Digital-Transformation-PMO"/>
        </div>
      </div>
      <div class="space-y-1">
        <span class="font-label-code text-badge-caps uppercase text-on-surface-variant">{'الأمر المولد:' if is_ar else 'Generated Command:'}</span>
        <div class="p-3 rounded-lg bg-primary-container text-on-primary font-label-code text-xs flex items-center justify-between">
          <code id="cli-generated-code">tasleemat init --tier 2 --pack standard --lang both --name "Digital-Transformation-PMO"</code>
          <button class="ml-2 hover:underline" onclick="copySnippetText(document.getElementById('cli-generated-code').innerText)">
            <span class="material-symbols-outlined text-[16px]">content_copy</span>
          </button>
        </div>
      </div>
      <div class="flex justify-end gap-2 pt-2">
        <button class="px-4 py-2 rounded-lg bg-surface-container text-on-surface font-label-code text-label-code" onclick="closeScaffolderModal()">
          {'تم' if is_ar else 'Done'}
        </button>
      </div>
    </div>
  </div>

  <!-- Notification Toast -->
  <div class="fixed bottom-6 right-6 z-50 bg-inverse-surface text-inverse-on-surface px-4 py-2.5 rounded-lg shadow-xl font-label-code text-xs flex items-center gap-2 transform translate-y-20 opacity-0 transition-all duration-300" id="catalog-toast">
    <span class="material-symbols-outlined text-secondary text-[18px]">check_circle</span>
    <span id="toast-message">Snippet copied to clipboard</span>
  </div>

  <!-- Interactive Logic Script -->
  <script>
    const isArabic = {'true' if is_ar else 'false'};
    const relRoot = "{rel_root}";
    let activePhase = 'all';
    let activeTier = 'all';
    let currentDrawerForm = 'PMO-03.01';

    const searchInput = document.getElementById('template-search');
    const cards = Array.from(document.querySelectorAll('.deliverable-card'));
    const noResults = document.getElementById('no-results-state');
    const activeCountLabel = document.getElementById('active-count-label');

    function normStr(str) {{
      if (!str) return '';
      return str.toLowerCase()
        .replace(/[أإآ]/g, 'ا')
        .replace(/ة/g, 'ه')
        .replace(/ى/g, 'ي')
        .replace(/[\u064B-\u065F]/g, '') // remove tashkeel
        .replace(/[-_.\\s]/g, ''); // ignore separators
    }}

    function applyFilters() {{
      let visibleCount = 0;
      const qRaw = (searchInput.value || '').trim().toLowerCase();
      const qNorm = normStr(qRaw);
      const qWords = qRaw.split(/\\s+/).filter(Boolean);

      cards.forEach(card => {{
        const cPhase = card.dataset.phase;
        const cTiers = card.dataset.tier ? card.dataset.tier.split(',') : [];
        const cSearch = (card.dataset.search || '').toLowerCase();
        const cCode = (card.dataset.code || '').toLowerCase();
        const cCodeAlt = (card.dataset.codeAlt || '').toLowerCase();
        const cSearchNorm = normStr(card.dataset.search || '');

        const matchesPhase = (activePhase === 'all' || cPhase === activePhase);
        const matchesTier = (activeTier === 'all' || cTiers.includes(activeTier));

        let matchesSearch = true;
        if (qRaw) {{
          const matchesWords = qWords.every(w => cSearch.includes(w));
          const matchesNorm = cSearchNorm.includes(qNorm) || cCode.includes(qRaw) || cCodeAlt.includes(qRaw);
          matchesSearch = matchesWords || matchesNorm;
        }}

        if (matchesPhase && matchesTier && matchesSearch) {{
          card.classList.remove('hidden');
          visibleCount++;
        }} else {{
          card.classList.add('hidden');
        }}
      }});

      if (activeCountLabel) {{
        activeCountLabel.innerText = isArabic 
          ? `عرض ${{visibleCount}} تسليمة من إجمالي ${{cards.length}}`
          : `Showing ${{visibleCount}} of ${{cards.length}} Deliverables`;
      }}

      if (noResults) {{
        if (visibleCount === 0) {{
          noResults.classList.remove('hidden');
        }} else {{
          noResults.classList.add('hidden');
        }}
      }}
    }}

    searchInput.addEventListener('input', applyFilters);

    window.addEventListener('keydown', (e) => {{
      if (e.key === '/' && document.activeElement !== searchInput) {{
        e.preventDefault();
        searchInput.focus();
      }}
      if (e.key === 'Escape') {{
        closeFormDrawer();
        closeScaffolderModal();
      }}
    }});

    function filterPhase(phase) {{
      activePhase = phase;
      document.querySelectorAll('.phase-btn').forEach(btn => {{
        if (btn.dataset.phase === phase) {{
          btn.className = "phase-btn px-3 py-1.5 rounded-lg text-label-code font-label-code whitespace-nowrap bg-primary text-on-primary transition-all";
        }} else {{
          btn.className = "phase-btn px-3 py-1.5 rounded-lg text-label-code font-label-code whitespace-nowrap bg-surface-container-low text-on-surface hover:bg-surface-container transition-all";
        }}
      }});
      applyFilters();
    }}

    function filterTier(tier) {{
      activeTier = tier;
      document.querySelectorAll('.tier-btn').forEach(btn => {{
        if (btn.dataset.tier === tier) {{
          btn.className = "tier-btn px-2.5 py-1 rounded text-badge-caps font-badge-caps bg-surface-container-highest text-on-surface";
        }} else {{
          btn.className = "tier-btn px-2.5 py-1 rounded text-badge-caps font-badge-caps bg-surface-container-low text-on-surface hover:bg-surface-container";
        }}
      }});
      applyFilters();
    }}

    function resetAllFilters() {{
      searchInput.value = '';
      filterPhase('all');
      filterTier('all');
    }}

    function setDualMode(mode) {{
      const bDual = document.getElementById('view-mode-dual');
      const bEn = document.getElementById('view-mode-en');
      const bAr = document.getElementById('view-mode-ar');
      [bDual, bEn, bAr].forEach(b => {{
        if (b) b.className = "px-2.5 py-1 rounded text-badge-caps font-badge-caps hover:text-on-surface transition-all flex items-center gap-1";
      }});

      if (mode === 'dual' && bDual) {{
        bDual.className = "px-2.5 py-1 rounded text-badge-caps font-badge-caps bg-surface-container-lowest text-on-surface shadow-xs transition-all flex items-center gap-1";
        showToast(isArabic ? "تم تفعيل العرض المزدوج" : "Switched to Dual English / Arabic View");
      }} else if (mode === 'en' && bEn) {{
        bEn.className = "px-2.5 py-1 rounded text-badge-caps font-badge-caps bg-surface-container-lowest text-on-surface shadow-xs transition-all flex items-center gap-1";
        showToast(isArabic ? "تم تفعيل العرض بالإنجليزية" : "Switched to English View");
      }} else if (mode === 'ar' && bAr) {{
        bAr.className = "px-2.5 py-1 rounded text-badge-caps font-badge-caps bg-surface-container-lowest text-on-surface shadow-xs transition-all flex items-center gap-1";
        showToast(isArabic ? "تم تفعيل العرض بالعربية" : "Switched to Arabic View");
      }}
    }}

    // Drawer Management
    const drawer = document.getElementById('artifact-drawer');
    const drawerPanel = document.getElementById('drawer-panel');

    function escapeHtml(s) {{
      if (!s) return '';
      return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
    }}

    function openFormDrawer(code) {{
      currentDrawerForm = code;
      let item = null;
      if (window.TASLEEMAT_DATA) {{
        item = window.TASLEEMAT_DATA.find(d => 
          d.code === code || 
          d.code_raw === code || 
          d.code.replace('PMO-', 'FORM-').replace('.', '-') === code ||
          d.code_raw.replace('_', '-') === code
        );
      }}

      if (!item) {{
        const card = document.querySelector(`.deliverable-card[data-code="${{code}}"], .deliverable-card[data-code-alt="${{code}}"]`);
        if (card) {{
          item = {{
            code: card.dataset.codeAlt || code,
            name_en: card.querySelector('h2').innerText,
            name_ar: card.querySelector('[dir="rtl"], [dir="ltr"]').innerText,
            phase: card.dataset.phase,
            tier: card.dataset.tier,
            template_en: "# " + code,
            template_ar: "# " + code
          }};
        }}
      }}

      if (item) {{
        const formCode = item.code.replace('PMO-', 'FORM-').replace('.', '-');
        document.getElementById('drawer-code').innerText = formCode;
        document.getElementById('drawer-title-primary').innerText = isArabic ? item.name_ar : item.name_en;
        document.getElementById('drawer-title-secondary').innerText = isArabic ? item.name_en : item.name_ar;

        // Tab 1: Spec Overview
        const specTab = document.getElementById('tab-content-spec');
        if (specTab) {{
          specTab.innerHTML = `
            <div class="grid grid-cols-1 md:grid-cols-2 gap-space-md">
              <div class="bg-surface-container-low rounded-xl p-space-md space-y-space-sm">
                <span class="font-label-code text-badge-caps uppercase tracking-wider text-secondary font-bold">English Deliverable Spec</span>
                <div class="space-y-2 text-body-sm text-on-surface">
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">Standard Code:</span> ${{item.code}} (${{formCode}})
                  </div>
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">Lifecycle Phase:</span> ${{item.phase_name_en || item.phase}}
                  </div>
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">Governance Tier:</span> ${{item.tier || 'Tier 1 | Tier 2 | Tier 3'}}
                  </div>
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">Standard Reference:</span> PMI PMBOK® 6/7/8 • ISO 21500
                  </div>
                </div>
              </div>
              <div class="bg-surface-container-low rounded-xl p-space-md space-y-space-sm" dir="rtl">
                <span class="font-label-code text-badge-caps uppercase tracking-wider text-secondary font-bold">المواصفة المعتمدة بالعربية</span>
                <div class="space-y-2 text-body-sm text-on-surface">
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">الرمز المعتمد:</span> ${{formCode}}
                  </div>
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">مرحلة دورة الحياة:</span> ${{item.phase_name_ar || item.phase}}
                  </div>
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">مستوى التخصيص:</span> ${{item.tier || 'المستويات 1-3'}}
                  </div>
                  <div class="p-2.5 rounded bg-surface-container-lowest">
                    <span class="font-bold text-xs">التوافق الوطني:</span> هيئة الحكومة الرقمية (DGA) • رؤية 2030
                  </div>
                </div>
              </div>
            </div>
            <div class="p-3 bg-surface-container-low rounded-xl border border-surface-container-high text-xs flex justify-between items-center">
              <span>Frictionless Datapackage (JSON Schema) & CSV data tables validated.</span>
              <button onclick="copySnippet('${{formCode}}')" class="font-bold text-secondary hover:underline">Copy CLI Scaffold</button>
            </div>
          `;
        }}

        // Tab 2: Markdown Template
        const tplTab = document.getElementById('tab-content-template');
        if (tplTab) {{
          const tplText = isArabic ? (item.template_ar || item.template_en) : (item.template_en || item.template_ar);
          tplTab.innerHTML = `
            <div class="flex items-center justify-between pb-2">
              <span class="font-label-code text-xs text-on-surface-variant font-bold">${{formCode}} Markdown Template</span>
              <button class="px-2.5 py-1 rounded bg-surface-container text-xs font-label-code text-on-surface hover:bg-surface-container-high transition" onclick="copyDrawerCode('drawer-tpl-raw')">📋 ${{isArabic ? 'نسخ القالب' : 'Copy Template'}}</button>
            </div>
            <pre class="p-4 bg-surface-container-low text-on-surface font-mono text-xs rounded-xl overflow-x-auto max-h-[60vh] border border-surface-container-high"><code id="drawer-tpl-raw">${{escapeHtml(tplText)}}</code></pre>
          `;
        }}

        // Tab 3: Practice Guide
        const guideTab = document.getElementById('tab-content-guide');
        if (guideTab) {{
          const guideText = isArabic ? (item.guide_ar || item.guide_en) : (item.guide_en || item.guide_ar);
          guideTab.innerHTML = `
            <div class="flex items-center justify-between pb-2">
              <span class="font-label-code text-xs text-on-surface-variant font-bold">${{formCode}} Authoring Practice Guide</span>
              <a class="px-2.5 py-1 rounded bg-secondary/10 text-secondary text-xs font-label-code font-bold hover:bg-secondary/20 transition" href="${{relRoot}}${{isArabic ? item.url_guide_ar : item.url_guide_en}}" target="_blank">${{isArabic ? 'فتح الدليل كاملاً ↗' : 'Open Full Guide ↗'}}</a>
            </div>
            <pre class="p-4 bg-surface-container-low text-on-surface font-mono text-xs rounded-xl overflow-x-auto max-h-[60vh] border border-surface-container-high"><code id="drawer-guide-raw">${{escapeHtml(guideText)}}</code></pre>
          `;
        }}

        // Tab 4: AI Copilot Prompt
        const promptTab = document.getElementById('tab-content-prompt');
        if (promptTab) {{
          const promptText = isArabic ? (item.prompt_ar || item.prompt_en) : (item.prompt_en || item.prompt_ar);
          promptTab.innerHTML = `
            <div class="flex items-center justify-between pb-2">
              <span class="font-label-code text-xs text-on-surface-variant font-bold">NIST AI RMF Compliant Prompt</span>
              <button class="px-2.5 py-1 rounded bg-surface-container text-xs font-label-code text-on-surface hover:bg-surface-container-high transition" onclick="copyDrawerCode('drawer-prompt-raw')">📋 ${{isArabic ? 'نسخ الموجه' : 'Copy Prompt'}}</button>
            </div>
            <pre class="p-4 bg-surface-container-low text-on-surface font-mono text-xs rounded-xl overflow-x-auto max-h-[60vh] border border-surface-container-high"><code id="drawer-prompt-raw">${{escapeHtml(promptText || 'Standard System Prompt for AI copilots.')}}</code></pre>
          `;
        }}

        // Tab 5: CLI
        const cliTab = document.getElementById('tab-content-cli');
        if (cliTab) {{
          cliTab.innerHTML = `
            <div class="space-y-4">
              <div class="bg-surface-container-low p-4 rounded-xl space-y-2 border border-surface-container-high">
                <span class="font-label-code text-xs text-secondary font-bold">1. Scaffold Single Deliverable:</span>
                <pre class="p-3 bg-surface-container-lowest text-on-surface font-mono text-xs rounded-lg flex justify-between items-center"><code>tasleemat scaffold ${{formCode}} --lang both</code><button onclick="copySnippetText('tasleemat scaffold ${{formCode}} --lang both')" class="text-xs text-secondary font-bold">${{isArabic ? 'نسخ' : 'Copy'}}</button></pre>
              </div>
              <div class="bg-surface-container-low p-4 rounded-xl space-y-2 border border-surface-container-high">
                <span class="font-label-code text-xs text-secondary font-bold">2. Python SDK Access:</span>
                <pre class="p-3 bg-surface-container-lowest text-on-surface font-mono text-xs rounded-lg"><code>from tasleemat import Catalog\nitem = Catalog.get("${{formCode}}")\nprint(item.template(lang="${{isArabic ? 'ar' : 'en'}}"))</code></pre>
              </div>
            </div>
          `;
        }}
      }}

      switchTab('spec');
      drawer.classList.remove('pointer-events-none', 'opacity-0');
      drawerPanel.classList.remove(isArabic ? '-translate-x-full' : 'translate-x-full');
    }}

    function closeFormDrawer() {{
      drawerPanel.classList.add(isArabic ? '-translate-x-full' : 'translate-x-full');
      setTimeout(() => {{
        drawer.classList.add('pointer-events-none', 'opacity-0');
      }}, 200);
    }}

    function switchTab(tabName) {{
      document.querySelectorAll('.drawer-tab').forEach(btn => {{
        btn.classList.remove('active', 'bg-surface-container-lowest', 'text-on-surface');
        btn.classList.add('text-on-surface-variant');
      }});
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.add('hidden'));

      const activeBtn = document.getElementById(`tab-btn-${{tabName}}`);
      const activePane = document.getElementById(`tab-content-${{tabName}}`);
      if (activeBtn) {{
        activeBtn.classList.add('active', 'bg-surface-container-lowest', 'text-on-surface');
        activeBtn.classList.remove('text-on-surface-variant');
      }}
      if (activePane) {{
        activePane.classList.remove('hidden');
      }}
    }}

    // Scaffolder Modal
    const scaffolderModal = document.getElementById('scaffolder-modal');
    function openScaffolderModal() {{
      scaffolderModal.classList.remove('pointer-events-none', 'opacity-0');
      updateCliCode();
    }}
    function closeScaffolderModal() {{
      scaffolderModal.classList.add('pointer-events-none', 'opacity-0');
    }}

    const cliTierSelect = document.getElementById('cli-tier-select');
    const cliLangSelect = document.getElementById('cli-lang-select');
    const cliNameInput = document.getElementById('cli-name-input');
    const cliGeneratedCode = document.getElementById('cli-generated-code');

    function updateCliCode() {{
      const tier = cliTierSelect ? cliTierSelect.value : '2';
      const lang = cliLangSelect ? cliLangSelect.value : 'both';
      const name = (cliNameInput ? cliNameInput.value.trim() : '') || 'Digital-Transformation-PMO';
      if (cliGeneratedCode) {{
        cliGeneratedCode.innerText = `tasleemat init --tier ${{tier}} --pack standard --lang ${{lang}} --name "${{name}}"`;
      }}
    }}

    [cliTierSelect, cliLangSelect, cliNameInput].forEach(el => {{
      if (el) {{
        el.addEventListener('change', updateCliCode);
        el.addEventListener('input', updateCliCode);
      }}
    }});

    // Toast Utilities
    function showToast(msg) {{
      const toast = document.getElementById('catalog-toast');
      document.getElementById('toast-message').innerText = msg;
      toast.classList.remove('translate-y-20', 'opacity-0');
      setTimeout(() => {{
        toast.classList.add('translate-y-20', 'opacity-0');
      }}, 2400);
    }}

    function copySnippet(code) {{
      navigator.clipboard.writeText(`tasleemat scaffold ${{code}} --lang both`);
      showToast(isArabic ? `تم نسخ أمر ${{code}}` : `Copied scaffold command for ${{code}}`);
    }}

    function copySnippetText(text) {{
      navigator.clipboard.writeText(text);
      showToast(isArabic ? 'تم النسخ إلى الحافظة' : 'CLI command copied to clipboard');
    }}

    function copyDrawerCode(elementId) {{
      const el = document.getElementById(elementId);
      if (el) {{
        navigator.clipboard.writeText(el.innerText);
        showToast(isArabic ? 'تم النسخ بنجاح' : 'Content copied to clipboard');
      }}
    }}

    function copyCurrentBundle() {{
      navigator.clipboard.writeText(`tasleemat scaffold ${{currentDrawerForm}} --lang both`);
      showToast(isArabic ? `تم نسخ حزمة ${{currentDrawerForm}}` : `Copied bundle command for ${{currentDrawerForm}}`);
    }}

    function batchExportZip() {{
      showToast(isArabic ? 'جاري تجهيز حزمة الـ 102 تسليمة بصيغة ZIP...' : 'Generating complete 102 Deliverables ZIP archive...');
    }}
  </script>
</body>
</html>
"""

