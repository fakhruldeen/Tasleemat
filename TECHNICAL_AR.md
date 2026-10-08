# 💻 دليل المطورين والهندسة الفنية - تسليمات

أهلاً بك في الدليل الفني والهندسي لمشروع **تسليمات (Tasleemat)**. يهدف هذا المستند إلى توفير الإرشادات البرمجية والفنية الخاصة بحزمة Python SDK، وأداة السطر البرمجي CLI، وبنية schemas بتنسيق JSON، وحزم البيانات القياسية OKF، وحزمة الاختبارات الآلية الشاملة.

> 👔 **هل تطلب قوالب وأدلة إدارة المشاريع؟** انتقل إلى **[README_AR.md](README_AR.md)** أو **[README.md](README.md)**.

---

## 🛠️ 1. أداة السطر البرمجي Tasleemat CLI

مشروع تسليمات متاح رسمياً عبر مستودع المكتبات PyPI كأداة سطر برمجي ومكتبة بايثون.

### التثبيت
```bash
pip install tasleemat
```

### أوامر CLI الأساسية
```bash
# إنشاء مشروع جديد عبر المعالج التفاعلي
tasleemat init --tier 2 --pack agile --lang ar --name "منصة التحول الرقمي" --code "PRJ-2026-01"

# البحث في قوالب تسليمات بالكلمات المفتاحية
tasleemat search "Risk" --lang en
tasleemat search "ميثاق" --lang ar

# استعراض كافة المراحل والرموز
tasleemat list --lang ar
```

---

## 🤖 2. حزمة تطوير البرمجيات (`tasleemat.ai`)

تتيح وحدة `tasleemat.ai` التكامل المباشر مع نماذج الذكاء الاصطناعي (مثل Google Gemini، OpenAI GPT-4، Anthropic Claude، أو المحركات المحلية) لتوليد وثائق إدارة المشاريع تلقائياً.

### إعداد مفتاح API
```bash
# ضبط المزود ومفتاح API عبر السطر البرمجي
tasleemat config set --provider gemini --model gemini-2.5-flash --key "YOUR_GEMINI_API_KEY"

# أو ضبط OpenAI
tasleemat config set --provider openai --model gpt-4o --key "YOUR_OPENAI_KEY"
```

### مثال بايثون
```python
from tasleemat.ai import AIClient

# تهيئة العميل
client = AIClient(provider="gemini", model="gemini-2.5-flash")

# توليد ميثاق مشروع كامل (PMO-03.01)
deliverable_md = client.generate(
    prompt="قم بتوليد ميثاق مشروع لتطوير منصة التجارة الإلكترونية بقيمة 2 مليون دولار",
    system_instruction="أنت مدير مكتب إدارة مشاريع (PMO Director). التزم بمعايير PMI PMBOK."
)

print(deliverable_md)
```

---

## 📦 3. حزم البيانات والخمسية المتزامنة

كل مخرج من مخرجات المشروع البالغ عددها 102 مخرج منظم في حزمة متزامنة من 5 ملفات:

| نوع الملف | صيغة التسمية | الهدف والاستخدام |
| :--- | :--- | :--- |
| **قالب جاهز للطباعة** | `*_قالب.md` / `*_Template.md` | قالب التوثيق البشري مع جداول التحكم والتوقيعات |
| **دليل الممارس** | `*_دليل.md` / `*_Guide.md` | دليل عملي وشرح تفصيلي ومحددات الربط والاعتماديات |
| **أوامر الذكاء الاصطناعي** | `*.md` | الأوامر الموجهة للنماذج اللغوية (LLM Prompts) |
| **مخطط JSON** | `*.json` | مخطط بيانات آلي للأنظمة والربط التقني |
| **قاموس البيانات** | `*.csv` | قاموس بيانات مبسط للربط مع Excel و PowerBI |

---

## 🧪 4. حزمة الاختبارات الآلية

تتضمن تسليمات حزمة اختبارات شاملة تغطي كافة القوالب البالغ عددها 102 قوالب (204 ملفات مرجعية) والأنظمة البرمجية:

```bash
# تشغيل حزمة الاختبارات بالكامل
python3 -m unittest discover -s tests -v

# أو تشغيل الاختبارات عبر CLI
tasleemat test -v
```

---

<div align="center">
  <sub>تم التطوير والتحديث بواسطة <a href="https://github.com/fakhruldeen">Fakhruldeen</a> • ترخيص مفتوح المصدر MIT</sub>
</div>
