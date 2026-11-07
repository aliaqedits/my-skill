# scripts
- `jalali.py` : Gregorian -> Jalali date (no dependencies). Tested: 2026-11-07 -> 1405/08/16.
- `build_rows.py` : parsed reviews (JSON) -> sheet rows in the exact column order of a layout (comments / g2 / trustradius).
- `verify_rows.py` : checks column count and Jalali text dates; prints counts (Excluded / Incentivized / AI) for the report.
Typical flow: parse input -> parsed.json -> build_rows.py -> verify_rows.py -> write with Sheets `update_values` in chunks of <=20 rows.
