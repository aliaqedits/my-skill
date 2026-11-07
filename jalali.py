#!/usr/bin/env python3
"""Gregorian -> Jalali (Shamsi) date conversion without dependencies.
Usage: python3 jalali.py 2026-11-07   ->  1405/08/16
       python3 jalali.py "Jan 5, 2026"  (also accepts 'Jan 5, 2026', '5 January 2026', '2026/01/05')
As a module: from jalali import to_jalali_str
"""
import sys, re
from datetime import datetime

def g2j(gy, gm, gd):
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    gy2 = gy + 1 if gm > 2 else gy
    days = 355666 + 365 * gy + (gy2 + 3) // 4 - (gy2 + 99) // 100 + (gy2 + 399) // 400 + gd + g_d_m[gm - 1]
    jy = -1595 + 33 * (days // 12053)
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461
    if days > 365:
        jy += (days - 1) // 365
        days = (days - 1) % 365
    if days < 186:
        jm, jd = 1 + days // 31, 1 + days % 31
    else:
        jm, jd = 7 + (days - 186) // 30, 1 + (days - 186) % 30
    return jy, jm, jd

FORMATS = ["%Y-%m-%d", "%Y/%m/%d", "%b %d, %Y", "%B %d, %Y", "%d %B %Y", "%d %b %Y", "%m/%d/%Y", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%SZ"]

def parse_gregorian(text):
    t = re.sub(r"\s+", " ", text.strip().replace("Sept", "Sep"))
    for f in FORMATS:
        try:
            return datetime.strptime(t, f)
        except ValueError:
            pass
    raise ValueError(f"unrecognized date: {text!r} (relative dates like '3 months ago' must be computed from today's date first)")

def to_jalali_str(text):
    d = parse_gregorian(text)
    return "%04d/%02d/%02d" % g2j(d.year, d.month, d.day)

if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(to_jalali_str(a))
