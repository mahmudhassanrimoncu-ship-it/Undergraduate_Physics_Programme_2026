"""Write 8-semester-version/semesters/S1..S8 from the main 12-term semester files.

The course syllabi are copied word for word from ../semesters/; only the semester
headers, dates, week mapping notes and annual exams are new.
Run from anywhere: python3 8-semester-version/tools/make_semesters.py
"""
import glob
import os
import re

from plan import (SEMESTERS, CONCURRENT, OLD_TERM, MIDTERM_WEEK, REVISION_WEEK, FINALS_WEEK, LAST_WEEK,
                  end, fmt, week, week_span, map_week)

HERE = os.path.dirname(os.path.abspath(__file__))
VAR = os.path.dirname(HERE)
REPO = os.path.dirname(VAR)

# ---------------------------------------------------------------- read the main syllabi
SECTIONS, ROWS = {}, {}
for path in sorted(glob.glob(os.path.join(REPO, "semesters", "S[01][0-9]-*.md"))):
    text = open(path, encoding="utf-8").read()
    for m in re.finditer(r"^\| ((?:PHY|MTH|CMP|LAB|IND|THS|OPT|ELE|EXM) [0-9x]+) \| (.+?) \| (\d) \| (.+?) \|$", text, re.M):
        ROWS[m.group(1)] = (m.group(2), m.group(3), m.group(4))
    parts = re.split(r"^## ", text, flags=re.M)
    for p in parts[1:]:
        m = re.match(r"((?:PHY|MTH|CMP|LAB|IND|THS) \d{3}):", p)
        if m:
            body = "## " + p.split("\n---\n")[0].rstrip()
            SECTIONS[m.group(1)] = body

ROWS["OPT I"] = ("Major Option I (from the list in options-and-electives.md)", "4", "Theory")
ROWS["OPT II"] = ("Major Option II", "4", "Theory")
ROWS["ELE I"] = ("Elective I", "4", "Theory or seminar")
ROWS["ELE II"] = ("Elective II", "4", "Theory or seminar")
ROWS["EXM 100"] = ("**Prelims** (Annual Examination I)", "4", "Exam + viva")
ROWS["EXM 200"] = ("**Part A** (Annual Examination II)", "4", "Exam + viva")
ROWS["EXM 300"] = ("**Part B** (Annual Examination III)", "4", "Exam + viva")
ROWS["EXM 400"] = ("**Finals (Part C)** (Annual Examination IV)", "4", "Exam + viva")

YEAR_NAME = {1: "Foundations", 2: "Core Physics I", 3: "Core Physics II and Independent Work", 4: "Specialisation and Research"}

WEEK_NOTE = (
    "> **About the week numbers.** The course syllabi below are the same as in the 12-term version, but each course now runs "
    "over a 22-week semester at about two-thirds of the pace. The week numbers in the course tables have been converted: "
    "syllabus weeks 1–6 now spread over weeks 1–10, the midterm is in week %d, weeks 8–13 spread over weeks 12–19, revision is week %d "
    "and finals are week %d. Problem sets come every two weeks per course instead of every week, so the work per course stays about the same."
    % (MIDTERM_WEEK, REVISION_WEEK, FINALS_WEEK)
)


def remap_tables(text):
    out, inside = [], False
    for line in text.split("\n"):
        if line.startswith("| Week |"):
            inside = True
            out.append(line)
            continue
        if inside and line.startswith("|"):
            cells = line.split("|")
            if not set(cells[1].strip()) <= set("-: "):
                cells[1] = " " + map_week(cells[1].strip()) + " "
            out.append("|".join(cells))
            continue
        inside = False
        out.append(line)
    return "\n".join(out)


EXAMS = {
    "EXM 100": """## EXM 100: Prelims (Annual Examination I)

**Week 22 ({w}).** The format follows the Oxford Prelims (CP1–CP4) and the Dhaka viva PV 102. In this version Year 1 contains special relativity (as the Oxford Prelims do) and waves move to Year 2.

| Paper | Content | Time |
|---|---|---|
| Paper 1: Physics | PHY 101, PHY 102, PHY 203. Section A has 10 short questions, all compulsory. Section B has 3 long questions chosen from 6 | 3 h |
| Paper 2: Mathematical Methods | MTH 101–104. Same format | 3 h |
| Viva voce | 30 min oral covering the year's physics and your own lab and computing work | 30 min |

Weighting: papers 80%, viva 20%. You need ≥ 50% to progress to Year 2. See [assessment-and-grading.md §7](../../docs/assessment-and-grading.md).""",
    "EXM 200": """## EXM 200: Part A (Annual Examination II)

**Week 22 ({w}).** Modelled on Oxford's Part A.

| Paper | Content | Time |
|---|---|---|
| A1: Waves & Quantum Physics | PHY 103, PHY 201 | 3 h |
| A2: Thermal Physics, Classical Mechanics & Electrodynamics | PHY 202, PHY 204, PHY 205, PHY 306 | 3 h |
| A3: Mathematical & Computational Methods | MTH 201, CMP 201 (written questions only, no coding) | 2 h |
| Viva voce | The year's physics plus your LAB 201 project | 30 min |

You need ≥ 50% to progress to Year 3.""",
    "EXM 300": """## EXM 300: Part B (Annual Examination III)

**Week 22 ({w}).** Modelled on Oxford's Part B.

| Paper | Content | Time |
|---|---|---|
| B1: Quantum Physics & Quantum Information | PHY 206, PHY 301, PHY 402 | 3 h |
| B2: Statistical Physics, Relativity & Cosmology | PHY 302, PHY 401 | 3 h |
| B3: General Paper | Order-of-magnitude estimates, Fermi problems, and short questions across the whole core so far | 2 h |
| Viva voce | The year's physics plus your Junior Papers | 45 min |

You need ≥ 50% to progress to Year 4.""",
    "EXM 400": """## EXM 400: Finals (Part C, Annual Examination IV)

**Week 22 ({w}).** In this version atomic, condensed-matter and nuclear and particle physics are taught in Year 4, so the Finals add one paper on them (C4).

| Paper | Content | Time |
|---|---|---|
| C1: General Physics | Synoptic questions across all four years, in the style of a PhD qualifying exam (Lim Yung-Kuo / Princeton Problems level) | 3 h |
| C2: Major Option I | OPT I | 2 h |
| C3: Major Option II | OPT II | 2 h |
| C4: Atomic, Condensed Matter, Nuclear & Particle Physics | PHY 303, PHY 304, PHY 305 | 3 h |
| Viva voce | Combined with the thesis defence | 45 min |

Once EXM 400 and THS 402 are graded, the degree is classified and the final transcript is issued.""",
}

OPT_TEXT = {
    "OPT I": "## OPT I and OPT II: Major Options\n\nTwo Oxford-style major options, taken together in this semester. Choose them by **week 16 of S6**. All prerequisites are met by the end of S7. Syllabi: [options-and-electives.md](../../semesters/options-and-electives.md).",
    "ELE I": "## ELE I: Elective I\n\nChoose by the end of S5. Because S6 is earlier in the degree than S11 in the 12-term version, choose an elective whose prerequisites are met by the end of S5 (or taken alongside it in S6): ELE 410, ELE 413, ELE 415, ELE 416 (with PHY 301 concurrently), ELE 417 or ELE 419. Syllabi: [options-and-electives.md](../../semesters/options-and-electives.md).",
    "ELE II": "## ELE II: Elective II\n\nAny elective from [options-and-electives.md](../../semesters/options-and-electives.md). Choose by week 16 of S7.",
}


def build():
    os.makedirs(os.path.join(VAR, "semesters"), exist_ok=True)
    for n, yr, season, start, codes, exam in SEMESTERS:
        e = end(start)
        name = f"S{n}-{season.split()[1]}-{season.split()[0].lower()}.md"
        lines = [f"# Semester {n}: {season} (Mon {fmt(start, start.year != e.year)} – Sun {fmt(e)})", ""]
        lines.append(
            f"**Year {yr}, {YEAR_NAME[yr]}.** {len(codes)} courses. Midterms in week {MIDTERM_WEEK} ({week_span(start, MIDTERM_WEEK)}). "
            f"Revision in week {REVISION_WEEK} ({week_span(start, REVISION_WEEK)}). Finals in week {FINALS_WEEK} ({week_span(start, FINALS_WEEK)}). "
            + (f"**{ROWS[exam][0].split('**')[1]} and viva in week {LAST_WEEK} ({week_span(start, LAST_WEEK)}).**" if exam
               else f"Feedback and Semester Report in week {LAST_WEEK}.")
        )
        if n == 6:
            lines.append("")
            lines.append("**Senior Thesis proposal due at the end of week 19.** Major options chosen by week 16.")
        lines += ["", "| Code | Course | Credits | Type | Was in (12-term) |", "|---|---|---|---|---|"]
        for c in codes + ([exam] if exam else []):
            t, cr, ty = ROWS[c]
            was = f"S{OLD_TERM[c]}" if c in OLD_TERM else "S" + {"EXM 100": "3", "EXM 200": "6", "EXM 300": "9", "EXM 400": "12"}[c]
            lines.append(f"| {c} | {t} | {cr} | {ty} | {was} |")
        conc = [f"- **{c}:** {CONCURRENT[c]}." for c in codes if c in CONCURRENT]
        if conc:
            lines += ["", "**Prerequisites taken alongside rather than before** (the only changes from the 12-term version):", ""] + conc
        lines += ["", WEEK_NOTE, ""]
        done = set()
        for c in codes:
            if c in done:
                continue
            lines.append("---")
            lines.append("")
            if c in SECTIONS:
                sec = SECTIONS[c].replace("](../docs/", "](../../docs/").replace("](options-and-electives.md", "](../../semesters/options-and-electives.md").replace("approved at the end of S10", "approved at the end of S6 (due in week 19)")
                lines.append(remap_tables(sec).replace("weeks 1–6", "weeks 1–10"))
            elif c in OPT_TEXT:
                lines.append(OPT_TEXT[c])
                if c == "OPT I":
                    done.add("OPT II")
            lines.append("")
        if exam:
            lines += ["---", "", EXAMS[exam].format(w=week_span(start, LAST_WEEK) + f" {week(start, LAST_WEEK).year}"), ""]
        open(os.path.join(VAR, "semesters", name), "w", encoding="utf-8").write("\n".join(lines))
        print("wrote", name)


if __name__ == "__main__":
    build()
