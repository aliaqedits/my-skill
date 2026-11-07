#!/usr/bin/env python3
"""Sanity-check rows.json before writing and print counts for the final report.
python3 verify_rows.py rows.json --layout comments
"""
import json, re, sys, argparse
from collections import Counter
N = {"comments": 11, "g2": 17, "trustradius": 18}
DATE_COL = {"comments": 3, "g2": 4, "trustradius": 3}
a = argparse.ArgumentParser(); a.add_argument("rows"); a.add_argument("--layout", required=True, choices=N)
a = a.parse_args()
rows = json.load(open(a.rows, encoding="utf-8")); bad = 0
for i, r in enumerate(rows, 1):
    if len(r) != N[a.layout]: print(f"row {i}: {len(r)} columns, expected {N[a.layout]}"); bad += 1
    d = r[DATE_COL[a.layout]]
    if d and not re.match(r"^1[34]\d\d/\d\d/\d\d$", d): print(f"row {i}: date not Jalali text: {d!r}"); bad += 1
if a.layout == "g2":
    print("Excluded:", dict(Counter(r[11] for r in rows)), "| Incentivized:", dict(Counter(r[12] for r in rows)), "| AI:", dict(Counter(r[13] for r in rows)))
print(f"{len(rows)} rows checked, {bad} problems")
sys.exit(1 if bad else 0)
