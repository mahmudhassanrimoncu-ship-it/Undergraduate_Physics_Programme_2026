#!/usr/bin/env python3
"""Build the 8-semester comparison booklet from the main booklet generator.

It imports ../../tools/booklet/build.py, regroups the same course data into
8 semesters, converts week numbers to the 22-week semester, rewrites the
calendar and load rules, and writes booklet-8.tex next to this file.
Run ./make_booklet.sh to get the PDF.
"""
import copy
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VAR = os.path.dirname(HERE)
REPO = os.path.dirname(VAR)
sys.path.insert(0, os.path.join(REPO, "tools", "booklet"))

import build as b  # noqa: E402
from data_y1 import ORI  # noqa: E402,F401
from plan import (SEMESTERS, CONCURRENT, WEEKS, MIDTERM_WEEK, REVISION_WEEK, FINALS_WEEK, LAST_WEEK,  # noqa: E402
                  end, fmt, week, map_week)

b.UNICODE["π"] = "$\\pi$"

ORD = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth"]

# ---------------------------------------------------------------- regroup the courses
BYCODE = {}
for name, dates, cs in b.SEMESTERS:
    for c in cs:
        key = {"OPT 4x1": "OPT I", "OPT 4x2": "OPT II"}.get(c["code"], c["code"])
        if c["code"] == "ELE 4xx":
            key = "ELE I" if name == "Eleventh Semester" else "ELE II"
        BYCODE[key] = c


def hours(h):
    m = re.match(r"(\d+(?:\.\d+)?) Hours/Week", h)
    if not m:
        return h
    v = round(float(m.group(1)) * 16 / 22 * 2) / 2
    return ("%g Hours/Week" % v)


NEW = []
for n, yr, season, s, codes, exam in SEMESTERS:
    cs = []
    for code in codes:
        c = copy.deepcopy(BYCODE[code])
        c["hours"] = hours(c["hours"])
        if "schedule" in c:
            c["schedule"] = [(map_week(w, "--"), t.replace("weeks 1--6", "weeks 1--10").replace("weeks~1--6", "weeks~1--10"))
                             for w, t in c["schedule"]]
        if code in CONCURRENT:
            c["prereq"] = c["prereq"] + r" \emph{(8-semester version: %s.)}" % CONCURRENT[code].replace("&", r"\&")
        if code == "THS 401":
            c["prereq"] = c["prereq"].replace("Tenth Semester", "Sixth Semester").replace("S10", "S6")
        cs.append(c)
    NEW.append(("%s Semester" % ORD[n - 1], "%s (%s -- %s)" % (season, fmt(s, False), fmt(end(s))), cs))
b.SEMESTERS = NEW


def when(n):
    import datetime as dt
    a = week(SEMESTERS[n - 1][3], LAST_WEEK)
    z = a + dt.timedelta(days=6)
    rng = "%d--%d %s" % (a.day, z.day, z.strftime("%b")) if a.month == z.month else "%s -- %s" % (fmt(a, False), fmt(z, False))
    return "Week %d (%s %d)" % (LAST_WEEK, rng, z.year)


old = b.ANNUAL
A1, A2, A3, A4 = (copy.deepcopy(old[k]) for k in ("Third Semester", "Sixth Semester", "Ninth Semester", "Twelfth Semester"))
A1["when"] = when(2)
A1["papers"][0] = ("Paper 1: Physics", "PHY 101, PHY 102, PHY 203 (special relativity is in Year~1 here, as in the Oxford Prelims). Section A: 10 short compulsory questions; Section B: 3 long questions from 6.", "3 h")
A2["when"] = when(4)
A2["papers"][0] = ("A1: Waves and Quantum Physics", "PHY 103, PHY 201.", "3 h")
A2["papers"][1] = ("A2: Thermal Physics, Classical Mechanics and Electrodynamics", "PHY 202, PHY 204, PHY 205, PHY 306.", "3 h")
A3["when"] = when(6)
A3["papers"][0] = ("B1: Quantum Physics and Quantum Information", "PHY 206, PHY 301, PHY 402.", "3 h")
A3["papers"][1] = ("B2: Statistical Physics, Relativity and Cosmology", "PHY 302, PHY 401.", "3 h")
A4["when"] = when(8)
A4["papers"][1] = ("C2: Major Option I", "OPT I.", "2 h")
A4["papers"][2] = ("C3: Major Option II", "OPT II.", "2 h")
A4["papers"].insert(3, ("C4: Atomic, Condensed Matter, Nuclear and Particle Physics", "PHY 303, PHY 304, PHY 305 (taught in Year~4 in this version).", "3 h"))
b.ANNUAL = {"Second Semester": A1, "Fourth Semester": A2, "Sixth Semester": A3, "Eighth Semester": A4}


def calendar_table():
    rows = [("Orientation Term", "Mon 7 Dec 2026", "--", "--", "Sun 24 Jan 2027")]
    tag = {"EXM 100": " (Prelims)", "EXM 200": " (Part A)", "EXM 300": " (Part B)", "EXM 400": " (Finals)"}
    for n, yr, season, s, codes, exam in SEMESTERS:
        rows.append(("%d %s" % (n, season), "Mon " + fmt(s), fmt(week(s, MIDTERM_WEEK), False),
                     fmt(week(s, FINALS_WEEK), False), "Sun " + fmt(end(s)) + tag.get(exam, "")))
    out = [r"\begin{center}\small", r"\rowcolors{2}{white}{rowgrey}", r"\begin{tabular}{lllll}", r"\toprule",
           r"\sffamily Semester & \sffamily Teaching starts & \sffamily Midterms & \sffamily Finals & \sffamily Ends\\ \midrule"]
    out += [" & ".join(r) + r"\\" for r in rows]
    out += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]
    return "\n".join(out)


b.calendar_table = calendar_table


def must_replace(text, pairs):
    for a, c in pairs:
        if a not in text:
            raise SystemExit("booklet text changed, cannot find: " + a[:80])
        text = text.replace(a, c)
    return text


_cover, _intro, _rules, _obe, _courses, _options, _routine = (b.cover, b.intro, b.rules, b.obe, b.courses_chapter,
                                                             b.options_chapter, b.routine_chapter)

b.cover = lambda: must_replace(_cover(), [
    (r"{\LARGE\scshape Information Booklet\par}", r"{\LARGE\scshape Information Booklet\par}\vspace{4mm}{\large\scshape 8-Semester Version, for comparison\par}"),
    (r"Session 2026--2031", r"Session 2026--2030"),
    (r"Version 1.4 \quad November 2026", r"8-semester variant of version 1.4 \quad November 2026"),
])

b.intro = lambda: must_replace(_intro(), [
    (r"\section{The Programme}", r"""\begin{center}\fbox{\parbox{0.9\linewidth}{\small\textbf{This is the 8-semester version of the booklet, made so that the two calendars can be compared side by side.} The programme being followed is the 12-term version. The courses, outcomes, rules and grading are the same in both; only the calendar, the number of courses per semester, the order of a few courses and the week numbers differ.}}\end{center}

\section{The Programme}"""),
    ("It runs for four years of three 16-week semesters each (Spring, Summer and Autumn), preceded by a seven-week Orientation Term, and takes 18--22 hours a week: three courses per semester.",
     "In this version it runs for four years of two 22-week semesters each (Spring and Autumn), preceded by a seven-week Orientation Term, and takes 18--22 hours a week: four or five courses per semester."),
    ("Three terms a year & Oxford; Caltech & Three 16-week semesters a year", "Two semesters a year & MIT, Harvard, Princeton; Dhaka & Two 22-week semesters a year"),
    ("Weekly oral defence of the student's own problem-set solutions", "Fortnightly oral defence of the student's own problem-set solutions in each course"),
])

b.rules = lambda: re.sub(
    r"Every semester follows the same 16-week pattern\..*?\\end\{center\}",
    lambda m: r"""Every semester follows the same 22-week pattern.

\begin{center}
\begin{tabularx}{0.9\linewidth}{cX}
\toprule
\sffamily Week & \sffamily Purpose\\ \midrule
1 & Teaching starts; \emph{Collection} (ungraded diagnostic) on the previous semester\\
1--10 & Teaching\\
11 & Midterm examinations (teaching continues at a lighter pace)\\
12--19 & Teaching\\
20 & Revision week: no new material; practice papers\\
21 & Final examinations\\
22 & Grading, feedback and the Semester Report; in the second semester of each year, the Annual Examination and viva\\
\bottomrule
\end{tabularx}
\end{center}""",
    must_replace(_rules(), [
        ("Each year has three semesters of 16 weeks: Spring (February--May), Summer (June--September) and Autumn (late September--mid January).",
         "Each year has two semesters of 22 weeks: Spring (February--early July) and Autumn (mid July--mid December)."),
        ("Three courses are taken each semester, at about 6--7 hours each, for a total of 18--22 hours a week.",
         "Four or five courses are taken each semester (alternately 4, 5, 5, 4, 4, 5, 5, 4), at about 4--5 hours each, for a total of 18--22 hours a week. Each course runs over 22 weeks instead of 16, so its total hours are about the same as in the 12-term version."),
        ("have two 80-minute lectures and a one-hour recitation a week.",
         "have one 80-minute lecture a week and a one-hour recitation every week in a four-course semester, or every other week in a five-course semester."),
        ("Each Monday the week's reading, lectures and problem set are released. Problem sets are due on Sunday",
         "Each Monday the week's reading and lectures are released, and each course has a problem set every other week, staggered so that two or three are due each Sunday. Problem sets are due on Sunday"),
        ("There is a one-week break after the Spring and Summer semesters and a two-week break after Autumn.",
         "There is a two-week break in July and a winter break of six to seven weeks between the Autumn semester and the next Spring semester. The programme ends on 22 December 2030."),
        ("Next semester drops to two courses with a remedial plan", "Next semester drops to three courses with a remedial plan"),
        ("in week~16 or in week~1 of the next semester", "in week~22 or in week~1 of the next semester"),
        ("Resit or retake plan agreed in week~16", "Resit or retake plan agreed in week~22"),
        ("In week~16 of each Autumn semester", "In week~22 of the second semester of each year"),
    ]), flags=re.S)

b.obe = lambda: must_replace(_obe(), [
    ("Each semester carries three 4-credit courses; the Autumn semesters of each year also carry the 4-credit annual examination.",
     "Each semester carries four or five 4-credit courses; the second semester of each year also carries the 4-credit annual examination."),
])


def courses_chapter():
    t = _courses()
    t = must_replace(t, [("Week numbers refer to the 16-week semester of Section~2.2;",
                          "Week numbers refer to the 22-week semester of Section~2.2 (they have been converted from the 16-week syllabi of the 12-term version);")])
    return t.replace("The major option and elective are chosen by week~12 of the Ninth Semester; their outlines are in Chapter~\\ref{ch:options}.",
                     "Elective~I is chosen by the end of the Fifth Semester, and the two major options by week~16 of the Sixth Semester; their outlines are in Chapter~\\ref{ch:options}.")


b.courses_chapter = courses_chapter

b.options_chapter = lambda: must_replace(_options(), [
    ("in the Eleventh and Twelfth Semesters. The options are chosen by week~12 of the Ninth Semester.",
     "in this version Elective~I in the Sixth Semester and the two options and Elective~II in the Eighth. The options are chosen by week~16 of the Sixth Semester. Elective~I must be one whose prerequisites are met by then: ELE~410, 413, 415, 416, 417 or 419."),
])


def routine_chapter():
    t = _routine()
    i = t.index(r"\section{First Semester, Spring 2027}")
    head = must_replace(t[:i], [
        ("Each theory course has two 80-minute lectures and a one-hour recitation (which opens with the weekly quiz);",
         "Each theory course has one 80-minute lecture a week and a one-hour recitation (which opens with the quiz) every week in a four-course semester, or every other week in a five-course semester;"),
        ("problem sets are due on Sunday at 23:59.", "two or three problem sets (each course every other week) are due on Sunday at 23:59."),
    ])
    s1 = "8-semester-version/semesters/timetables/S1-2027-spring-timetable.md"
    o = [head, r"""\section{First Semester, Spring 2027}

Four courses over 22 weeks. PHY~101 and MTH~103 problem sets are due on the Sundays of even teaching weeks, MTH~101 sets and CMP~101 assignments on the odd ones.

\subsection*{Weekly routine (teaching weeks 1--10 and 12--19)}
{\small
\begin{center}
\renewcommand{\arraystretch}{1.5}
\begin{tabularx}{\linewidth}{>{\bfseries}l>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X}
\toprule
\sffamily\mdseries Day & \sffamily Morning & \sffamily Afternoon & \sffamily 19:30--20:50 & \sffamily 21:00--22:20\\ \midrule
Mon & & & PHY 101 Lecture & MTH 101 Lecture\\
Tue & & & MTH 103 Lecture & CMP 101 Lecture\\
Wed & & & PHY 101 Recitation (19:30--20:30, opens with the quiz) & MTH 101 Recitation (21:00--22:00, opens with the quiz)\\
Thu & & & CMP 101 Lab & MTH 103 Recitation (21:00--22:00, opens with the quiz)\\
Fri & Problem-set block (09:00--12:00) & & & \\
Sat & Problem-set block (10:00--12:30) & Tutorials for the two courses whose sets came back (16:00--17:00); office hours (17:30--18:30) & & \\
Sun & & & Problem-set wrap-up (19:30--21:30) & \textbf{Two problem sets due 23:59}\\
\bottomrule
\end{tabularx}
\end{center}}
Weekly totals: lectures, recitations and laboratory about 9.7~h; tutorials and office hours 2~h; problem-set blocks 7.5~h; about 19--20~h in all.

\subsection*{Lecture calendar: PHY 101, MTH 101 and MTH 103}
{\scriptsize
\rowcolors{2}{white}{rowgrey}
\begin{xltabular}{\linewidth}{cl>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X}
\toprule
\rowcolor{white}\sffamily Week & \sffamily Mon & \sffamily PHY 101, Mon 19:30 & \sffamily MTH 101, Mon 21:00 & \sffamily MTH 103, Tue 19:30\\ \midrule
\endhead"""]
    for r in b.md_table(s1, "Lecture calendar: PHY 101, MTH 101 and MTH 103"):
        r = (r + ["", "", ""])[:5]
        o.append(" & ".join(r) + r"\\")
    o.append(r"""\bottomrule
\end{xltabular}}

\subsection*{Lecture calendar: CMP 101}
{\small
\rowcolors{2}{white}{rowgrey}
\begin{xltabular}{\linewidth}{c>{\raggedright\arraybackslash}p{0.22\linewidth}>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X}
\toprule
\rowcolor{white}\sffamily Week & \sffamily Lecture (Tue) / Lab (Thu) & \sffamily Method & \sffamily Physics application\\ \midrule
\endhead""")
    for r in b.md_table(s1, "Lecture calendar: CMP 101"):
        r = (r + ["", "", ""])[:4]
        o.append(" & ".join(r) + r"\\")
    o.append(r"""\bottomrule
\end{xltabular}}

\subsection*{Examination and special weeks}
{\small
\begin{xltabular}{\linewidth}{cl>{\raggedright\arraybackslash}X}
\toprule
\sffamily Week & \sffamily Dates & \sffamily What happens\\ \midrule
\endhead""")
    o += [" & ".join(r) + r"\\" for r in b.md_table(s1, "Exam and special weeks")]
    o.append(r"""\bottomrule
\end{xltabular}}

\subsubsection{Ramadan and Eid} Ramadan 2027 is expected to run from about 8 February to 9 March (weeks 2--6), with Eid al-Fitr around 10 March (week~6), subject to the moon sighting; the midterms are five weeks later. If needed, evening slots can move to 21:30--23:30 after tarawih, or a one-week Eid pause can be taken in week~6, absorbed by shortening the July break to one week.

\subsubsection{Five-course semesters} In S2, S3, S6 and S7 each theory course keeps its weekly lecture but has a recitation every other week, alternating with another course, so that classes stay at about 10 hours a week.
""")
    return "\n".join(o)


b.routine_chapter = routine_chapter

if __name__ == "__main__":
    b.HERE = HERE
    b.build()
    os.replace(os.path.join(HERE, "booklet.tex"), os.path.join(HERE, "booklet-8.tex"))
    print("renamed to booklet-8.tex")
