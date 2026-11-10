"""The 8-semester variant: one source of truth for its semesters and dates.

Used by make_semesters.py (Markdown semester files) and build_booklet.py (PDF).
"""
import datetime as dt

WEEKS = 22          # weeks per semester
MIDTERM_WEEK = 11
REVISION_WEEK = 20
FINALS_WEEK = 21
LAST_WEEK = 22      # grading and feedback; in the second semester of each year, the annual exam and viva

# (number, year of study, season label, first Monday, course codes, annual exam or None)
SEMESTERS = [
    (1, 1, "Spring 2027", dt.date(2027, 2, 1), ["PHY 101", "MTH 101", "MTH 103", "CMP 101"], None),
    (2, 1, "Autumn 2027", dt.date(2027, 7, 19), ["PHY 102", "MTH 102", "MTH 104", "LAB 101", "PHY 203"], "EXM 100"),
    (3, 2, "Spring 2028", dt.date(2028, 1, 31), ["PHY 103", "PHY 202", "PHY 204", "MTH 201", "LAB 201"], None),
    (4, 2, "Autumn 2028", dt.date(2028, 7, 17), ["PHY 201", "PHY 205", "CMP 201", "PHY 306"], "EXM 200"),
    (5, 3, "Spring 2029", dt.date(2029, 1, 29), ["PHY 206", "LAB 301", "IND 301", "PHY 401"], None),
    (6, 3, "Autumn 2029", dt.date(2029, 7, 16), ["PHY 301", "PHY 302", "PHY 402", "IND 302", "ELE I"], "EXM 300"),
    (7, 4, "Spring 2030", dt.date(2030, 2, 4), ["PHY 303", "PHY 304", "PHY 305", "LAB 401", "THS 401"], None),
    (8, 4, "Autumn 2030", dt.date(2030, 7, 22), ["OPT I", "OPT II", "ELE II", "THS 402"], "EXM 400"),
]

# Where each course sat in the 12-term plan (for the comparison table)
OLD_TERM = {
    "PHY 101": 1, "MTH 101": 1, "CMP 101": 1, "PHY 102": 2, "MTH 102": 2, "LAB 101": 2,
    "PHY 103": 3, "MTH 103": 3, "MTH 104": 3, "PHY 201": 4, "PHY 202": 4, "PHY 203": 4,
    "PHY 204": 5, "MTH 201": 5, "LAB 201": 5, "PHY 205": 6, "PHY 206": 6, "CMP 201": 6,
    "PHY 301": 7, "PHY 302": 7, "LAB 301": 7, "PHY 303": 8, "PHY 304": 8, "IND 301": 8,
    "PHY 305": 9, "PHY 306": 9, "IND 302": 9, "PHY 401": 10, "PHY 402": 10, "LAB 401": 10,
    "OPT I": 11, "ELE I": 11, "THS 401": 11, "OPT II": 12, "ELE II": 12, "THS 402": 12,
}

# Prerequisites that this variant takes concurrently instead of beforehand
CONCURRENT = {
    "MTH 103": "MTH 101 taken concurrently (Oxford teaches matrices in the first term, CP3)",
    "MTH 104": "MTH 102 taken concurrently (as MIT allows for 18.03 with 18.02)",
    "PHY 203": "PHY 102 taken concurrently (special relativity is part of the Oxford Prelims, CP1)",
    "PHY 306": "CMP 201 taken concurrently",
}


def week(start, k):
    """Monday of week k (1-based)."""
    return start + dt.timedelta(weeks=k - 1)


def end(start):
    return start + dt.timedelta(weeks=WEEKS, days=-1)


def fmt(d, year=True):
    return f"{d.day} {d.strftime('%b')}" + (f" {d.year}" if year else "")


def span(a, b):
    """'3–9 May' or '28 Jun – 4 Jul'."""
    if a.month == b.month:
        return f"{a.day}–{b.day} {b.strftime('%b')}"
    return f"{fmt(a, False)} – {fmt(b, False)}"


def week_span(start, k):
    m = week(start, k)
    return span(m, m + dt.timedelta(days=6))


# ------------------------------------------------ 16-week syllabus weeks -> 22-week semester weeks
def _one(w):
    if w <= 6:                       # teaching weeks 1-6 -> 1-10
        return round((w - 1) * 10 / 6) + 1, round(w * 10 / 6)
    if w == 7:
        return MIDTERM_WEEK, MIDTERM_WEEK
    if w <= 13:                      # teaching weeks 8-13 -> 12-19
        k = w - 7
        return 11 + round((k - 1) * 8 / 6) + 1, 11 + round(k * 8 / 6)
    return {14: (REVISION_WEEK,) * 2, 15: (FINALS_WEEK,) * 2, 16: (LAST_WEEK,) * 2}[w]


def map_week(label, dash="–"):
    """'3' -> '4–5', '14--15' -> '20–21', '7' -> '11'. Anything else is returned unchanged."""
    import re
    m = re.fullmatch(r"\s*(\d+)\s*(?:--|–|-)?\s*(\d+)?\s*", label)
    if not m:
        return label
    a = int(m.group(1)); b = int(m.group(2) or a)
    if not (1 <= a <= 16 and 1 <= b <= 16):
        return label
    lo, hi = _one(a)[0], _one(b)[1]
    return str(lo) if lo == hi else f"{lo}{dash}{hi}"
