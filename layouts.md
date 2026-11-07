# چیدمان‌های شناخته‌شده (ستون‌ها به ترتیب)

## A) تب `comments` (چیدمان فعلی، A–K)
Job Title | Industry | Company Size | Review Date | Rating (out of 5) | Review Title | Source | G2 Page | Software | row | بررسی کدگذاری

- Review Title سلول ترکیبی است:
  ```
  <عنوان>
  [Pros] ...
  [Cons] ...
  [Use case] ...

  [Recommendations to others considering <Software>] ...   (فقط اگر وجود داشت)
  ```
- Job Title برای Verified User خالی. Industry و Company Size از منبع.
- Rating از ۵ (مقیاس ۱۰ → نصف، گرد به ۰٫۵؛ در گزارش ذکر شود).
- Source حروف کوچک: g2, trustradius, capterra, reddit, x, telegram, instagram, appstore, ...
- G2 Page شماره صفحه یا خالی. row = شماره ردیف شیت − ۱ (ادامه از ۳ ردیف آخر). «بررسی کدگذاری» مثل ردیف‌های قبلی (۱).
- ستون Reviewer / Incentivized / AI / خلاصه فارسی در این چیدمان نیست.

## B) تب قدیمی `g2` (A–Q)
Reviewer | Job Title | Industry | Company Size | Review Date | Rating | Review Title | What users like best | What users dislike | Problems solved & benefits | Source | Excluded from G2 scores (reason) | Incentivized | AI Translated | خلاصه فارسی | G2 Page | Software

- Excluded فقط: `Guest / non-business user` | `Business partner / seller's competitor` | خالی.
- Incentivized و AI Translated فقط Yes/No.
- Verified User: Reviewer=`Verified User`، Job خالی، Industry همان صنعت.

## C) تب `trustradius` (A–R)
Product | Review Title | Rating (out of 10) | Review Date | Incentivized | Use Cases and Deployment Scope | Pros | Cons | Likelihood to Recommend | Reviewer Name | Reviewer Role | Department / Industry | Company | Company Size | Years of Experience | Reviewer Status | Page | خلاصه فارسی

- Pros/Cons جمله‌های جداشده با `; `. مقیاس امتیاز ۱۰.

## D) تب‌های تحلیلی (فقط‌خواندنی؛ هرگز ننویس)
- `کدنامه v1`: کد | نام کد | تعریف (K01…K28 کدهای شکایت).
- `کدگذاری`: نام کد | محصول | تعداد نظرات | تعداد بازدارنده | N محصول | شناسه‌های نظرات (ستون row در comments).
این دو تب به ستون `row` تب comments وابسته‌اند؛ درج/حذف/مرتب‌سازی ردیف در comments ممنوع است.

## مقصد جدید یا اکسل دیگر
هدر ردیف ۱ و ۳ ردیف آخر را بخوان و ستون‌ها را بر اساس **نام هدر** نگاشت کن. اگر مقصد خالی است، چیدمان A را با هدر دقیق بساز. فایل xlsx: روی کپی با openpyxl کار کن و با SendUserFile برگردان.
