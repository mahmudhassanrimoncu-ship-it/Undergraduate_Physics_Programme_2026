"""Write the 8-semester handbook and curriculum map from the main 12-term ones.

Everything not about the calendar or the load is copied unchanged, so the two
versions differ only where the semester system itself differs.
"""
import os
import re

from plan import (SEMESTERS, CONCURRENT, OLD_TERM, WEEKS, MIDTERM_WEEK, REVISION_WEEK, FINALS_WEEK, LAST_WEEK,
                  end, fmt, week)
import make_semesters as ms

HERE = os.path.dirname(os.path.abspath(__file__))
VAR = os.path.dirname(HERE)
REPO = os.path.dirname(VAR)
OWN = {"curriculum-map.md", "handbook.md"}


def relink(text):
    """Point links at the main repo's files, except the docs this variant has its own copy of."""
    def fix(m):
        t = m.group(1)
        if re.match(r"\w+://|#", t):
            return m.group(0)
        if t.startswith("../semesters/timetables") or t.startswith("../semesters/S"):
            return m.group(0)                      # variant has its own semesters/
        if t.startswith("../"):
            return "](../" + t + ")"               # ../lectures -> ../../lectures
        base = t.split("#")[0]
        if base in OWN:
            return m.group(0)
        return "](../../docs/" + t + ")"           # main docs
    return re.sub(r"\]\(([^)]+)\)", fix, text)


def section(text, num):
    """Return (start, end) of '## num.' section."""
    a = text.index(f"\n## {num}. ")
    b = text.index("\n## ", a + 5)
    return a, b


BANNER = ("> **This is the 8-semester version, made for comparison.** The programme you are actually following is the "
          "[12-term version](../../docs/handbook.md). Only the calendar, the load per semester and the order of a few courses "
          "differ; every rule not mentioned here is the same. See the [comparison](../README.md).\n")


def dates_table():
    rows = ["| Semester | Teaching starts | Midterm week | Finals week | Ends |", "|---|---|---|---|---|",
            "| **Orientation Term 0** (same as the 12-term version) | Mon 7 Dec 2026 | – | Diagnostics in week 1 | Sun 24 Jan 2027 |"]
    exam_name = {"EXM 100": "Prelims", "EXM 200": "Part A", "EXM 300": "Part B", "EXM 400": "Finals and thesis defence"}
    for n, yr, season, s, codes, exam in SEMESTERS:
        e = end(s)
        tail = f" ({exam_name[exam]} in week {LAST_WEEK})" if exam else ""
        rows.append(f"| **S{n}** {season} | Mon {fmt(s)} | {fmt(week(s, MIDTERM_WEEK), False)} | {fmt(week(s, FINALS_WEEK), False)} | Sun {fmt(e)}{tail} |")
    return "\n".join(rows)


def handbook():
    t = open(os.path.join(REPO, "docs", "handbook.md"), encoding="utf-8").read()
    t = t.replace("| Three terms per year | **Oxford** (Michaelmas, Hilary, Trinity) and **Caltech** (three quarters) | 3 × 16-week semesters per year |",
                  "| Two semesters per year | **MIT**, **Harvard**, **Princeton** (fall and spring) and **Dhaka** | 2 × 22-week semesters per year, with a long break around January |")
    a, b = section(t, 3)
    cal = f"""
## 3. Academic calendar

Every semester is **{WEEKS} weeks**:

| Week | Purpose |
|---|---|
| 1 | Teaching starts. **Collection** (diagnostic) on the previous semester |
| 1–10 | Teaching |
| {MIDTERM_WEEK} | **Midterm exams** (teaching continues at a lighter pace) |
| 12–19 | Teaching |
| {REVISION_WEEK} | Revision week. No new material. Practice papers |
| {FINALS_WEEK} | **Final exams** |
| {LAST_WEEK} | Grading, written feedback, semester report. In the second semester of each year this is the **Annual Examination and viva** |

### Dates

{dates_table()}

The year has a **Spring semester** (early February to early July) and an **Autumn semester** (mid July to mid December). Between them there is a 2-week break in July, and after the Autumn semester a 6–7 week winter break that also holds the gap before the next year. The programme ends on **Sun 22 Dec 2030**, four weeks earlier than the 12-term version, because there are fewer semester changeovers.

**Flexibility rule.** Your CSE degree comes first when its exams fall in the same weeks. You may **shift any semester by up to 2 weeks** with notice before Week 1, or **pause** a semester for up to 3 weeks mid-term (for example, CSE finals or Eid). The calendar is then re-issued. Every shift is logged in the changelog. If your CSE semesters run on a similar six-month pattern, the semesters can be aligned with them once, so that most clashes never happen.
"""
    t = t[:a] + "\n" + cal + t[b:]
    a, b = section(t, 4)
    s4 = t[a:b]
    s4 = s4.replace("You have chosen 18–22 hours per week, which means three courses per semester at about 6–7 hours each.",
                    "You have chosen 18–22 hours per week. In this version that means **four or five courses per semester** (alternating: 4, 5, 5, 4, 4, 5, 5, 4) at about 4–5 hours each. Each course runs over 22 weeks instead of 16, so its total hours stay about the same.")
    s4 = s4.replace("Each theory course has 2 × 80-minute lectures and 1 recitation (problem class) per week.",
                    "Each theory course has 1 × 80-minute lecture per week, plus a recitation (problem class) every week in a 4-course semester and every other week in a 5-course semester.")
    s4 = s4.replace("| Lectures (MIT OCW or equivalent video, or tutor-written notes) | ~2–2.5 h |", "| Lecture (MIT OCW or equivalent video, or tutor-written notes) | ~1.5 h |")
    s4 = s4.replace("| Reading the primary textbook, with worked examples | ~1.5 h |", "| Reading the primary textbook, with worked examples | ~1 h |")
    s4 = s4.replace("| Problem set | ~2.5–3 h |", "| Problem set (a longer set every two weeks) | ~1.5–2 h a week |")
    s4 = s4.replace("| Tutorial with the tutor (written or live, in a thread) | ~0.5 h |", "| Tutorial with the tutor, every two weeks (written or live, in a thread) | ~0.25 h a week |")
    s4 = s4.replace("- **Monday.** New week's material released: reading list, lecture videos, problem set.",
                    "- **Monday.** New week's material released: reading list and lecture videos. Each course's problem set is released every other Monday, staggered across courses.")
    s4 = s4.replace("- **Sunday 23:59 (your local time).** Problem set due.", "- **Sunday 23:59 (your local time).** Two or three problem sets due (each course every two weeks).")
    t = t[:a] + s4 + t[b:]
    t = t.replace("- **Probation:** if semester GPA < 2.00, the next semester drops to 2 courses and includes a remedial plan.",
                  "- **Probation:** if semester GPA < 2.00, the next semester drops to 3 courses and includes a remedial plan.")
    t = t.replace("- **Weekly:** written feedback on every problem set.", "- **Every problem set:** written feedback.")
    t = t.replace("- **Mid-semester (Week 8):**", f"- **Mid-semester (Week {MIDTERM_WEEK + 1}):**")
    t = t.replace("- **End of semester (Week 16):**", f"- **End of semester (Week {LAST_WEEK}):**")
    t = t.rstrip("\n") + "\n| 2026-11-10 | **8-semester version** created at Rimon's request, for comparison only. Same courses, rules and grading; 2 × 22-week semesters per year with 4–5 courses each |\n"
    t = relink(t)
    t = t.replace("# Programme Handbook\n", "# Programme Handbook (8-semester version)\n\n" + BANNER, 1)
    open(os.path.join(VAR, "docs", "handbook.md"), "w", encoding="utf-8").write(t)


def semester_tables():
    titles, prereq = {}, {}
    cm = open(os.path.join(REPO, "docs", "curriculum-map.md"), encoding="utf-8").read()
    for m in re.finditer(r"^\| S\d+(?: W16)? \| \*\*(\w+ [\w]+)\*\* \| (.+?) \| (.+?) \|$", cm, re.M):
        titles[m.group(1)], prereq[m.group(1)] = m.group(2), m.group(3)
    alias = {"OPT I": "OPT 4x1", "OPT II": "OPT 4x2", "ELE I": "ELE 4xx", "ELE II": "ELE 4xx"}
    out = []
    years = {1: "Year 1: Foundations", 2: "Year 2: Core Physics I", 3: "Year 3: Core Physics II and Independent Work", 4: "Year 4: Specialisation and Research"}
    for yr in range(1, 5):
        out += [f"### {years[yr]}", "", "| Sem | Code | Title | Prerequisites | Was in (12-term) |", "|---|---|---|---|---|"]
        for n, y, season, s, codes, exam in SEMESTERS:
            if y != yr:
                continue
            for c in codes + ([exam] if exam else []):
                k = alias.get(c, c)
                title = {"OPT I": "Major Option I (see §5)", "OPT II": "Major Option II (see §5)", "ELE I": "Elective I (see §6)", "ELE II": "Elective II (see §6)"}.get(c, titles.get(k, c))
                pre = prereq.get(k, "–").replace("by the end of S10", "by week 19 of S6")
                if c == "ELE I":
                    pre = "Elective-specific; choose one whose prerequisites are met by the end of S5 (see S6 file)"
                if c in CONCURRENT:
                    pre = prereq.get(k, "") + f". **Changed:** {CONCURRENT[c]}"
                was = f"S{OLD_TERM[c]}" if c in OLD_TERM else {"EXM 100": "S3 W16", "EXM 200": "S6 W16", "EXM 300": "S9 W16", "EXM 400": "S12 W16"}[c]
                sem = f"S{n}" + (f" W{LAST_WEEK}" if c == exam else "")
                code = c if c not in alias else alias[c].replace("4x1", "I").replace("4x2", "II").replace("4xx", c.split()[1])
                out.append(f"| {sem} | **{code}** | {title} | {pre} | {was} |")
        out.append("")
    return "\n".join(out)


def curriculum_map():
    t = open(os.path.join(REPO, "docs", "curriculum-map.md"), encoding="utf-8").read()
    a, b = section(t, 2)
    body = """
## 2. Semester-by-semester plan

Credits: every course is 4 credits. The 36 courses and 4 annual exams are exactly the same as in the 12-term version. Only their grouping changes: 4 or 5 courses at a time instead of 3.

**How the courses were regrouped.** The physics core keeps MIT's order (8.01 → 8.02 → 8.03 → 8.04 → 8.05 → 8.06), one step per semester. Four prerequisites are taken alongside instead of before, marked "changed" below. Three courses move noticeably: special relativity moves into Year 1 (as in the Oxford Prelims), waves and optics moves into Year 2 (as at MIT, where 8.03 is a sophomore course), and atomic, condensed-matter and nuclear and particle physics move into Year 4. One thing is lost: PHY 202 is no longer taken alongside PHY 201, as MIT recommends for 8.044.

### Orientation Term 0 (7 Dec 2026 – 24 Jan 2027, ungraded)
- **ORI 000 Orientation and Bridging.** The same as in the 12-term version.

""" + semester_tables()
    t = t[:a] + "\n" + body + t[b:]
    t = t.replace("Choose **two** by the end of S9.", "Choose **two** by week 16 of S6. Both are taken together in S8.")
    t = t.replace("The choice is deferred until S9", "The choice is deferred until S6")
    t = relink(t)
    t = t.replace("# Curriculum Map\n", "# Curriculum Map (8-semester version)\n\n" + BANNER.replace("../../docs/handbook.md", "../../docs/curriculum-map.md"), 1)
    open(os.path.join(VAR, "docs", "curriculum-map.md"), "w", encoding="utf-8").write(t)


if __name__ == "__main__":
    os.makedirs(os.path.join(VAR, "docs"), exist_ok=True)
    handbook()
    curriculum_map()
    print("wrote docs/handbook.md and docs/curriculum-map.md")
