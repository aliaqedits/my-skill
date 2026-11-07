#!/usr/bin/env python3
"""Turn parsed reviews (JSON list of dicts) into sheet rows for a chosen layout.

python3 build_rows.py parsed.json --layout comments --software "Jira" --source g2 --start-row 601 --out rows.json
Layouts: comments | g2 | trustradius
Each parsed review dict may contain (missing = ""):
  reviewer, job_title, industry, company_size, date (Gregorian or already Jalali YYYY/MM/DD),
  rating (number), rating_scale (5 or 10), title, pros, cons, use_case, recommendation,
  source_detail, excluded, incentivized (bool), ai_translated (bool), page, summary_fa
Output: rows.json = list of rows (lists of cell values) in the layout's exact column order.
"""
import argparse, json, re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from jalali import to_jalali_str

JAL = re.compile(r"^1[34]\d\d/\d\d/\d\d$")

def jdate(v):
    v = (v or "").strip()
    if not v:
        return ""
    return v if JAL.match(v) else to_jalali_str(v)

def rating5(r, scale):
    if r in ("", None):
        return ""
    return round(float(r) * 5 / float(scale or 5) * 2) / 2 if scale and float(scale) != 5 else float(r)

def yn(b):
    return "Yes" if b else "No"

def review_title_cell(r, software):
    parts = [r.get("title", "").strip()]
    if r.get("pros"): parts.append("[Pros] " + r["pros"].strip())
    if r.get("cons"): parts.append("[Cons] " + r["cons"].strip())
    if r.get("use_case"): parts.append("[Use case] " + r["use_case"].strip())
    s = "\n".join(p for p in parts if p)
    if r.get("recommendation"):
        s += f"\n\n[Recommendations to others considering {software}] " + r["recommendation"].strip()
    return s

def row_comments(r, a, i):
    return [r.get("job_title", ""), r.get("industry", ""), r.get("company_size", ""), jdate(r.get("date")),
            rating5(r.get("rating", ""), r.get("rating_scale", 5)), review_title_cell(r, a.software),
            a.source, str(r.get("page", a.page or "")), a.software, str(a.start_row - 1 + i), a.coding_flag]

def row_g2(r, a, i):
    return [r.get("reviewer", ""), r.get("job_title", ""), r.get("industry", ""), r.get("company_size", ""), jdate(r.get("date")),
            rating5(r.get("rating", ""), r.get("rating_scale", 5)), r.get("title", ""), r.get("pros", ""), r.get("cons", ""),
            "\n\n".join(x for x in [r.get("use_case", ""), ("[Recommendations to others considering %s] %s" % (a.software, r["recommendation"])) if r.get("recommendation") else ""] if x),
            r.get("source_detail", ""), r.get("excluded", ""), yn(r.get("incentivized")), yn(r.get("ai_translated")),
            r.get("summary_fa", ""), str(r.get("page", a.page or "")), a.software]

def row_tr(r, a, i):
    return [a.software, r.get("title", ""), r.get("rating", ""), jdate(r.get("date")), yn(r.get("incentivized")),
            r.get("use_case", ""), r.get("pros", ""), r.get("cons", ""), r.get("recommendation", ""), r.get("reviewer", ""),
            r.get("job_title", ""), r.get("industry", ""), r.get("company", ""), r.get("company_size", ""), r.get("years", ""),
            r.get("reviewer_status", ""), str(r.get("page", a.page or "")), r.get("summary_fa", "")]

LAYOUTS = {"comments": (row_comments, 11), "g2": (row_g2, 17), "trustradius": (row_tr, 18)}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("parsed"); p.add_argument("--layout", required=True, choices=LAYOUTS)
    p.add_argument("--software", required=True); p.add_argument("--source", default="g2")
    p.add_argument("--start-row", type=int, required=True, help="sheet row number of the first new row")
    p.add_argument("--page", default=""); p.add_argument("--coding-flag", default="1")
    p.add_argument("--out", default="rows.json")
    a = p.parse_args()
    fn, ncols = LAYOUTS[a.layout]
    reviews = json.load(open(a.parsed, encoding="utf-8"))
    rows = [fn(r, a, i) for i, r in enumerate(reviews)]
    assert all(len(x) == ncols for x in rows), "column count mismatch"
    json.dump(rows, open(a.out, "w", encoding="utf-8"), ensure_ascii=False)
    last = chr(ord("A") + ncols - 1)
    print(f"{len(rows)} rows -> {a.out}; write to A{a.start_row}:{last}{a.start_row + len(rows) - 1} (chunks of <=20 rows)")

if __name__ == "__main__":
    main()
