<div class="lang-switch-bar">
  <span class="lang-switch-label">🌐 <strong>اللغة:</strong> الدليل باللغة العربية</span>
  <div class="lang-switch-actions">
    <a class="lang-switch-btn github-btn" href="https://github.com/fakhruldeen/Tasleemat/blob/main/docs/ar/11_tools_and_automation.md" target="_blank" rel="noopener noreferrer">🐙 عرض على GitHub ↗</a>
    <a class="lang-switch-btn" href="../en/11_tools_and_automation.html">🇬🇧 Switch to English Version (النسخة الإنجليزية) ←</a>
  </div>
</div>

---
type: Guide
token_pointer: /_tokens/docs/ar/11_tools_and_automation.npy
token_count: 2313
tokenizer_model_id: tiktoken/o200k_base
created_at: '2026-10-06T16:05:28.216685+00:00'
---

<p align="center">
  <img src="../img/logo-ar.png" alt="شعار تسليمات" width="280" />
</p>

---

# 🛠️ دليل الأدوات البرمجية والأتمتة والتكامل السحابي (CI/CD)
**مرجع الوثيقة:** `TASLEEMAT-GUIDE-11-TOOLS-AUTOMATION-AR`  
**الإصدار:** 2.0  
**الفئات المستهدفة:** مهندسو DevOps، مسؤولو أنظمة PMO، المطورون ومدراء المشاريع  

---

## 🎯 قدرات الأتمتة والحوكمة البرمجية (Governance-as-Code)

صُمم نظام «تسليمات» بفلسفة **الوثائق كشيفرة برمجية (Docs-as-Code)** و**الحوكمة كشيفرة برمجية (Governance-as-Code)**؛ مما يتيح تتبع النسخ عبر Git، والتحقق التلقائي في خطوط أنابيب CI/CD، وتوليد مساحات العمل المخصصة للمشاريع في ثوانٍ معدودة.

```mermaid
flowchart LR
    A["102 نموذج تسليم ثنائي اللغة"] --> B["أداة سطر الأوامر tasleemat-cli"]
    A --> C["حزمة الفحص البرمجي في بايثون"]
    C --> D["خطوط أنابيب GitHub Actions CI"]
    A --> E["محرك التصدير المجمع (HTML/PDF)"]
    A --> F["توثيق ماركداون المباشر في المستودع"]
```

---

## 🚀 1. أداة سطر الأوامر الرسمية (`tasleemat`)

يوفر نظام "تسليمات" حزمة بايثون (SDK) وأداة سطر أوامر رسمية لتسهيل تأسيس مساحات عمل المشاريع واستكشاف النماذج. يمكنك تثبيتها عالمياً عبر PyPI:

```bash
pip install tasleemat
```

### أ. تأسيس مساحة عمل مخصصة لمشروع جديد (`init`)
توليد مجلد مشروع متكامل يضم فقط النماذج الإلزامية وفقاً لمستوى الحوكمة (Tier 1 أو 2 أو 3) وحزمة المنهجية المختارة:

```bash
# وضع المعالج التفاعلي (يسألك خطوة بخطوة في الطرفية)
tasleemat init

# وضع المعاملات السريعة: المستوى 2 (المتوسط) مع حزمة أجايل باللغة العربية
tasleemat init \
  --tier 2 \
  --pack agile \
  --lang ar \
  --name "منصة الخدمات الرقمية الموحدة" \
  --code "PRJ-2026-DIGITAL-01" \
  --pm "سارة الأحمد" \
  --sponsor "خالد المنصور" \
  --out ./my_new_project

# مشروع استراتيجي من المستوى 1 باللغتين العربية والإنجليزية
tasleemat init \
  --tier 1 \
  --pack hybrid \
  --lang both \
  --name "برنامج التحول المؤسسي الشامل" \
  --code "PRJ-2026-CORE-01" \
  --pm "محمد السعيد" \
  --sponsor "فهد العتيبي" \
  --out ./enterprise_workspace
```

#### ما تقوم به الأداة تلقائياً:
1. تصفية الـ 102 نموذج لاختيار الباقة الإلزامية المناسبة لحجم المشروع وحزمة المنهجية (`agile`, `ai`, `predictive`, `hybrid`).
2. نسخ القوالب، والأدلة، ومخططات JSON، وقواميس CSV.
3. التعبئة التلقائية لبيانات الترويسة (اسم المشروع، رمزه، اسم المدير، الراعي، وتاريخ اليوم) في كافة الملفات المستنسخة.
4. إنشاء ملف `PROJECT_README.md` تفصيلي يحتوي على قائمة تدقيق لبوابات العبور وروابط مباشرة للنماذج.

---

### ب. البحث في فهرس النماذج (`search`)
البحث في كافة النماذج الـ 102 عبر الكلمات المفتاحية باللغتين العربية والإنجليزية:

```bash
# البحث باللغة العربية
tasleemat search "مخاطر" --lang ar
tasleemat search "ميثاق" --lang ar
tasleemat search "ذكاء اصطناعي" --lang ar
tasleemat search "سبرنت" --lang ar

# البحث باللغة الإنجليزية
tasleemat search "Risk" --lang en
tasleemat search "Charter" --lang en
tasleemat search "Model Card" --lang en
```

---

### ج. استعراض الفهرس الشامل للنماذج (`list`)
عرض قائمة النماذج الكاملة مع رموزها ومجلداتها:

```bash
tasleemat list --lang ar
tasleemat list --lang en
```

### د. إدارة إعدادات وحسابات الذكاء الاصطناعي (`config`)
ضبط وتكوين مفاتيح الربط البرمجي (API Keys) ومزودي نماذج الذكاء الاصطناعي للتوليد التلقائي للوثائق:

```bash
# عرض الإعدادات الحالية
tasleemat config show

# ضبط المزود والنموذج الافتراضي (يدعم: gemini, openai, anthropic, ollama, mock)
tasleemat config set --provider gemini --model gemini-2.5-flash
tasleemat config set --provider openai --model gpt-4o

# ضبط المفتاح البرمجي مباشرة (أو تعيين المتغير GEMINI_API_KEY في البيئة)
tasleemat config set --provider gemini --key "AIzaSy..."
```

---

### هـ. التوليد والاستيفاء التلقائي للوثائق بالذكاء الاصطناعي (`generate`)
توليد واستيفاء مخرجات المشروع الاحترافية تلقائياً باستخدام حساب الذكاء الاصطناعي وملاحظات الاجتماعات:

```bash
# استيفاء ميثاق المشروع (PMO-03.01) تلقائياً من ملاحظات الاجتماع
tasleemat generate --form PMO-03.01 --notes ./meeting_notes.txt --out ./03_01_Project_Charter.md

# استيفاء سجل المخاطر باللغة العربية باستخدام نموذج OpenAI
tasleemat generate --form PMO-04.08.02 --notes ./risk_workshop_notes.txt --lang ar --provider openai --out ./04_08_02_Risk_Register.md

# تشغيل تجربة توليد وهمية (Mock) دون استهلاك رصيد المفتاح البرمجي
tasleemat generate --form PMO-03.01 --notes "مشروع التحول الرقمي السحابي" --mock
```

---

### و. تشغيل حزمة الفحوصات والاختبارات الآلية (`test`)
تشغيل حزمة الفحص الشاملة (بما في ذلك فحوصات عميل الذكاء الاصطناعي):

```bash
# تشغيل حزمة الاختبارات مع الملخص
tasleemat test

# تشغيل الاختبارات بالوضع المفصل
tasleemat test -v

# أو التشغيل عبر أداة unittest القياسية في بايثون
python3 -m unittest discover -s tests -v
```

---

## 🖨️ 2. محرك التصدير المجمع للوثائق (`tools/export_deliverables.py`)

تحويل أي وثيقة أو مجلد مشروع كامل من صيغة Markdown إلى صفحات HTML منسقة وجاهزة للطباعة وتصدير PDF، مع دعم كامل للاتجاه العربي (RTL) وخطوط Cairo و Inter:

```bash
# تصدير وثيقة مفردة
python3 tools/export_deliverables.py forms/ar/03_البدء/01_ميثاق_المشروع/03_01_ميثاق_المشروع_قالب.md -o output.html

# تصدير نموذج عربي مع دعم RTL
python3 tools/export_deliverables.py forms/ar/03_البدء/01_ميثاق_المشروع/03_01_ميثاق_المشروع_قالب.md -o charter.html

# تصدير مجلد مشروع بالكامل
python3 tools/export_deliverables.py my_project_workspace/
```

---

## 🌐 3. هيكلية التوثيق المباشر عبر المستودع (Repository-First)

تحتفظ تسليمات بكافة أدلة الحوكمة، والأدلة التشغيلية، والنماذج ثنائية اللغة بصيغة ماركداون الأصلية المباشرة داخل مستودع GitHub. تم إيقاف بوابة الويب السابقة لضمان بقاء التوثيق خاضعاً لإدارة النسخ وتدقيق التغييرات جنباً إلى جنب مع الشيفرات والقوالب. يمكن تصفح جميع الأدلة بدءاً من [`docs/README.md`](../README.md).

---

## 🛡️ 4. حزمة التدقيق والفحص البرمجي في بايثون

يحتوي مجلد `tests/` و `tools/` على منظومة اختبارات وتدقيق آلية متكاملة:

### 1. حزمة الاختبارات الرئيسية (`tests/`)
- **طريقة التشغيل:** `python3 -m unittest discover -s tests -v`
- **الوحدات:** التماثل اللغوي (`test_parity.py`)، المخططات الهيكلية (`test_schemas.py`)، حزمة البيانات المفتوحة (`test_okf_datapackage.py`)، قوالب الحوكمة (`test_governance_templates.py`)، الامتثال للبيانات الافتراضية (`test_fictional_compliance.py`)، أدوات CLI (`test_cli_and_exporters.py`)، والأدلة التوثيقية (`test_documentation.py`).

### 2. مدقق جودة النماذج والمخططات (`tools/audit_forms.py`)
- **طريقة التشغيل:** `python3 tools/audit_forms.py`
- **الوظيفة:** يفحص جميع النماذج الـ 102 باللغتين العربية والإنجليزية (204 ملفات) للتأكد من وجود جدول الاعتماد وتسلسل العناوين وصحة الروابط.

### 3. مدقق حزمة البيانات المفتوحة Frictionless OKF (`tools/validate_okf.py`)
- **طريقة التشغيل:** `python3 tools/validate_okf.py`
- **الوظيفة:** يتحقق من مطابقة ملف `datapackage.json` والمخططات الـ 204 لمعايير حزم البيانات المفتوحة الدولية.

### 4. فاحص التماثل والتطابق اللغوي (`tools/parity.py`)
- **طريقة التشغيل:** `python3 tools/parity.py forms/en forms/ar`
- **الوظيفة:** يضمن التطابق التام 1:1 في البنية والملفات بين المجلدات العربية والإنجليزية.

---

## ⚙️ 5. خط أنابيب التكامل المستمر (`.github/workflows/ci.yml`)

يتم تشغيل فحص آلي عبر GitHub Actions مع كل عملية دفع أو سحب (Pull Request) إلى الفرع الرئيسي `main` يشمل:
1. التحقق من سلامة المخططات الهيكلية لكافة النماذج الـ 204 (`audit_forms.py`).
2. فحص العرض والتنسيق للجداول والمخططات (`check_rendering.py`).
3. التحقق من التماثل الثنائي التام عربي/إنجليزي 1:1 (`parity.py`).
4. فحص حزمة البيانات المفتوحة Frictionless (`validate_okf.py`).
5. تشغيل حزمة الاختبارات الآلية الشاملة المكونة من 28 فحصاً (`tests/`).
6. اختبار واجهة الأوامر والتصدير (`tasleemat_cli.py`).