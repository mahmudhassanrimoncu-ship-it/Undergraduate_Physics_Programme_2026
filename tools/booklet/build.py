#!/usr/bin/env python3
"""Generate the printable programme booklet (LaTeX) from the course data files.

Usage:  python3 build.py            # writes booklet.tex next to this file
        pdflatex booklet.tex (twice) # or run ./make.sh

The layout follows the University of Chittagong CSE "Information Booklet":
rules first, then outcomes and the curriculum at a glance, then one page
per course with rationale, CLO table, assessment strategy and weekly schedule.
"""
import os
import re

from data_y1 import ORI, SEMESTERS_Y1
from data_y2 import SEMESTERS_Y2
from data_y3 import SEMESTERS_Y3
from data_y4 import SEMESTERS_Y4, OPTIONS, ELECTIVES

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
SEMESTERS = SEMESTERS_Y1 + SEMESTERS_Y2 + SEMESTERS_Y3 + SEMESTERS_Y4

KIND_LABEL = {"theory": "Theory", "lab": "Laboratory", "comp": "Computational",
              "ind": "Independent work", "ths": "Research", "opt": "Option / elective",
              "exm": "Exam + viva", "ori": "Bridging"}

# ---------------------------------------------------------------- annual exams
ANNUAL = {
    "Third Semester": dict(
        code="EXM 100", title="Prelims (Annual Examination I)", when="Week 16 (13--19 Dec 2027)",
        model="Oxford Prelims (CP1--CP4) and the Dhaka viva voce PV~102.",
        papers=[("Paper 1: Physics", "PHY 101, PHY 102, PHY 103. Section A: 10 short compulsory questions; Section B: 3 long questions from 6.", "3 h"),
                ("Paper 2: Mathematical Methods", "MTH 101--104. Same format.", "3 h"),
                ("Viva voce", "The year's physics and the student's own laboratory and computing work.", "30 min")],
        progress="Year~2"),
    "Sixth Semester": dict(
        code="EXM 200", title="Part A (Annual Examination II)", when="Week 16 (11--17 Dec 2028)",
        model="Oxford Part A.",
        papers=[("A1: Quantum Physics and Relativity", "PHY 201, PHY 203, PHY 206.", "3 h"),
                ("A2: Thermal Physics, Classical Mechanics and Electrodynamics", "PHY 202, PHY 204, PHY 205.", "3 h"),
                ("A3: Mathematical and Computational Methods", "MTH 201, CMP 201 (written questions only).", "2 h"),
                ("Viva voce", "The year's physics and the LAB 201 project.", "30 min")],
        progress="Year~3"),
    "Ninth Semester": dict(
        code="EXM 300", title="Part B (Annual Examination III)", when="Week 16 (10--16 Dec 2029)",
        model="Oxford Part B.",
        papers=[("B1: Quantum, Atomic and Condensed Matter", "PHY 301, PHY 303, PHY 304.", "3 h"),
                ("B2: Statistical, Nuclear and Particle, Nonlinear Physics", "PHY 302, PHY 305, PHY 306.", "3 h"),
                ("B3: General Paper", "Order-of-magnitude estimates, Fermi problems and short questions across the whole core so far.", "2 h"),
                ("Viva voce", "The year's physics and both Junior Papers.", "45 min")],
        progress="Year~4"),
    "Twelfth Semester": dict(
        code="EXM 400", title="Finals (Part C, Annual Examination IV)", when="Week 16 (16--22 Dec 2030)",
        model="Oxford Part C and the Princeton departmental examination.",
        papers=[("C1: General Physics", "Synoptic questions across all four years, at the level of a PhD qualifying examination.", "3 h"),
                ("C2: Major Option I", "OPT 4x1.", "2 h"),
                ("C3: Major Option II", "OPT 4x2.", "2 h"),
                ("Viva voce", "Combined with the Senior Thesis defence.", "45 min")],
        progress=None),
}

# ------------------------------------------------------- assessment by course type
DEFAULT_ASSESS = {
    "theory": [
        ("Problem sets", "about ten weekly sets marked by the ten-point rubric; the lowest is dropped.", "25\\%"),
        ("Concept quizzes", "a ten-minute quiz at the start of each weekly recitation.", "5\\%"),
        ("Tutorials", "Oxford-style oral defence of the student's own solutions, scored 0--3.", "10\\%"),
        ("Midterm examination", "week~7; 90 minutes; closed book with a one-sided A4 formula sheet.", "20\\%"),
        ("Final examination", "week~15; 3 hours; cumulative; closed book with a two-sided A4 formula sheet.", "40\\%"),
    ],
    "lab": [
        ("Laboratory notebook", "kept continuously and checked fortnightly.", "15\\%"),
        ("Laboratory reports", "3--4 reports in journal-article format.", "45\\%"),
        ("Oral presentations", "MIT 8.13-style presentation and questioning on an experiment.", "15\\%"),
        ("Pre-lab quizzes", "pre-lab questions and error-analysis exercises.", "10\\%"),
        ("Final practical", "week~15; analysis of unseen data or a build-and-debug practical.", "15\\%"),
    ],
    "comp": [
        ("Coding assignments", "weekly programs applying the method to a physics problem.", "35\\%"),
        ("Midterm project", "weeks 7--8; a short simulation with a written report.", "20\\%"),
        ("Final project", "a physics simulation or data analysis with a written report.", "30\\%"),
        ("Code review", "oral walkthrough of the final project.", "15\\%"),
    ],
    "ori": [
        ("Diagnostics D1 and D2", "ungraded; used for placement and the bridging plan.", "--"),
        ("Advanced Standing Exams", "optional; 70\\% or more gives credit by examination (CR).", "CR"),
        ("Mock problem set and tutorial", "marked with the real rubric for practice; not recorded.", "--"),
    ],
}
DELIVERY = {
    "theory": ("two 80-minute lectures and one recitation each week, Oxford-style tutorials and office hours; the matching MIT OpenCourseWare lectures serve as a second source",
               "problem sets, concept quizzes, tutorials, a midterm and a final examination"),
    "lab": ("pre-lab briefings, experiments at home with a smartphone (phyphox), an Arduino and simple apparatus, analysis of open research data, and supervision in office hours",
            "the laboratory notebook, reports, oral presentations, pre-lab quizzes and a final practical"),
    "comp": ("a weekly lecture on the numerical method and a weekly laboratory in which it is coded on a physics problem",
             "coding assignments, a midterm project, a final project and a code review"),
    "ind": ("weekly supervision meetings, written feedback on drafts from the editor, and talks",
            "the proposal, progress meetings, the paper and oral presentations"),
    "ths": ("weekly supervision meetings, written feedback on chapters and drafts, and presentations",
            "written submissions, presentations and an oral defence"),
    "ori": ("live welcome and bridging lectures, tools laboratories and a mock teaching week",
            "timed diagnostics and optional Advanced Standing Exams"),
}

PLOS = [
    ("Physics Knowledge", "Explain and apply the core of physics --- classical and quantum mechanics, electromagnetism, thermal and statistical physics, waves, optics and relativity --- at the level of a graduating major from a leading department."),
    ("Mathematical Methods", "Use calculus, linear algebra, differential equations, complex analysis, Fourier methods, special functions, probability and tensors fluently as tools."),
    ("Problem Solving and Physical Reasoning", "Set up and solve unseen problems; check results by units, limiting cases, symmetry and order-of-magnitude estimates."),
    ("Experimental Practice", "Design, build and carry out experiments safely, and keep a complete laboratory record."),
    ("Computation", "Solve physics problems without closed-form answers using numerical methods, simulation and well-tested code."),
    ("Data Analysis and Uncertainty", "Analyse data statistically, fit and test models, and quantify statistical and systematic uncertainty."),
    ("Research and Independent Inquiry", "Read the research literature, reproduce published results, and carry out an original research project."),
    ("Communication", "Communicate physics clearly in reports, papers, a thesis, talks and oral examinations."),
    ("Modern Physics in Context", "Connect the core to modern and frontier physics --- relativity, quantum information, particle physics, cosmology, condensed matter --- and to other disciplines, especially computer science."),
    ("Independent and Lifelong Learning", "Plan and regulate one's own learning, act with integrity, and keep learning beyond the degree."),
]
PEOS = [
    "Be prepared for graduate study or research in physics or a neighbouring field, or to bring a physicist's methods to a career in computing.",
    "Apply physical modelling, computation and quantitative reasoning to complex problems, including those met as a computer scientist.",
    "Continue to learn independently and act with scientific integrity throughout their careers.",
]
# PLO -> PEOs it serves
PLO_PEO = {1: (1,), 2: (1, 2), 3: (1, 2), 4: (1,), 5: (1, 2), 6: (1, 2), 7: (1, 3), 8: (1, 3), 9: (1, 2), 10: (3,)}


# ------------------------------------------------------------------- helpers
def plo_tex(s):
    """'PLO1, PLO3' -> small-caps plo with subscripts."""
    return ", ".join("\\textsc{plo}$_{%s}$" % m for m in re.findall(r"PLO(\d+)", s))


UNICODE = {
    "–": "--", "—": "---", "−": "$-$", "≥": "$\\geq$", "≤": "$\\leq$", "·": "$\\cdot$",
    "×": "$\\times$", "χ²": "$\\chi^2$", "χ": "$\\chi$", "∇": "$\\nabla$", "ψ": "$\\psi$",
    "Υ": "$\\Upsilon$", "θ": "$\\theta$", "μ": "$\\mu$", "²": "$^2$", "’": "'", "‘": "`",
    "“": "``", "”": "''", "→": "$\\to$", "≈": "$\\approx$", "…": "\\dots{}",
}


def md(s):
    """Convert a Markdown table cell to LaTeX."""
    s = s.strip()
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    for a, b in (("\\", "\\textbackslash{}"), ("&", "\\&"), ("%", "\\%"), ("#", "\\#"), ("_", "\\_")):
        s = s.replace(a, b)
    s = re.sub(r"`([^`]+)`", r"\\texttt{\1}", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s)
    s = re.sub(r"\*(.+?)\*", r"\\emph{\1}", s)
    s = re.sub(r'"([^"]+)"', r"``\1''", s)
    for a, b in UNICODE.items():
        s = s.replace(a, b)
    s = s.replace("F = $-$$\\nabla$U", "$F=-\\nabla U$")
    return s


def md_table(path, heading):
    """Return the rows (header excluded) of the first table after a '## heading'."""
    lines = open(os.path.join(REPO, path), encoding="utf-8").read().splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("#") and heading in l) if heading else 0
    rows, seen = [], False
    for l in lines[start + 1:]:
        if l.startswith("|"):
            seen = True
            cells = [c for c in l.strip().strip("|").split("|")]
            if set("".join(cells).strip()) <= set("-: "):
                continue
            rows.append([md(c) for c in cells])
        elif seen:
            break
    return rows[1:]


def textbf_course(code):
    return "\\textbf{%s}" % code


# ------------------------------------------------------------------- preamble
PREAMBLE = r"""\documentclass[11pt,a4paper,twoside,openany]{book}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{charter}
\usepackage[scaled=0.9]{helvet}
\usepackage{amsmath,amssymb}
\usepackage{microtype}
\usepackage[a4paper,top=27mm,bottom=27mm,inner=27mm,outer=25mm,headsep=9mm,headheight=14pt]{geometry}
\usepackage[table]{xcolor}
\usepackage{array,booktabs,tabularx,xltabular,makecell,multirow}
\usepackage{enumitem}
\usepackage{titlesec,titletoc}
\usepackage{fancyhdr}
\usepackage{needspace}
\usepackage{pifont}
\usepackage{pgfornament}
\usepackage{tikz}
\usepackage{url}
\usepackage[hidelinks,bookmarksnumbered]{hyperref}

\definecolor{cublue}{RGB}{28,78,150}
\definecolor{taggrey}{gray}{0.86}
\definecolor{rowgrey}{gray}{0.93}

\raggedbottom
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus 1pt}
\renewcommand{\arraystretch}{1.18}
\setlist{nosep,leftmargin=1.6em}
\urlstyle{same}

% Chapter and section styles, after the CU booklet
\titleformat{\chapter}[display]{\normalfont\bfseries}{\Large\chaptertitlename\ \thechapter}{18pt}{\Huge}
\titlespacing*{\chapter}{0pt}{40pt}{36pt}
\titleformat{\section}{\normalfont\large\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries}{\thesubsection}{1em}{}
\titleformat{\subsubsection}[runin]{\normalfont\normalsize\bfseries}{}{0pt}{}[.]

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\thepage\hspace{2.2em}}
\fancyhead[RE]{\slshape\nouppercase{\leftmark}}
\fancyhead[LO]{\slshape\nouppercase{\rightmark}}
\fancyhead[RO]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\chaptermark}[1]{\markboth{\MakeUppercase{\chaptername\ \thechapter.\ #1}}{}}
\renewcommand{\sectionmark}[1]{\markright{\MakeUppercase{\thesection.\ #1}}}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\thepage}}

\newcommand{\acr}[1]{\textsc{#1}}
\newcommand{\clo}[1]{\textsc{clo}$_{#1}$}
\newcommand{\coursesub}[1]{\par\needspace{8\baselineskip}\medskip\noindent\textbf{#1}\par\nopagebreak\smallskip}
\newcommand{\semtag}[2]{\par\needspace{8\baselineskip}\bigskip\noindent\colorbox{taggrey}{\sffamily #1}\hfill{\small\sffamily #2}\par\smallskip}
\newcommand{\coursehead}[4]{%
  \par\needspace{12\baselineskip}\bigskip
  \noindent\colorbox{taggrey}{\strut\textbf{#1}}\par\smallskip
  \noindent\begin{minipage}[t]{0.66\linewidth}\raggedright\large\textbf{\textcolor{cublue}{#2}}\end{minipage}%
  \hfill\begin{minipage}[t]{0.32\linewidth}\raggedleft\sffamily #3, #4\end{minipage}\par\smallskip}
\newcommand{\infoline}[2]{\noindent{\small\textbf{#1}\quad #2}\par}
\newcommand{\pen}{\ding{46}}
"""


# ------------------------------------------------------------------- cover + front
def cover():
    return r"""
\begin{titlepage}
\centering
\vspace*{8mm}
\pgfornament[width=11cm,color=cublue]{88}\par
\vspace{30mm}
{\LARGE\scshape Information Booklet\par}
\vspace{8mm}
{\Large B.S.\ (Honours) Programme\par in\par Physics\par}
\vspace{6mm}
{\large Self-Directed Edition\par Session 2026--2030\par}
\vspace{10mm}
\rule{0.55\linewidth}{0.6pt}\par
\vspace{6mm}
{\large\scshape Undergraduate Physics Programme 2026\par}
\vspace{2mm}
{\normalsize Modelled on the curricula of MIT, Harvard, Oxford, Princeton and Caltech,\par with the University of Dhaka as a regional reference\par}
\vfill
{\normalsize Student: \textbf{Rimon}\qquad Instructor, tutor and examiner: \textbf{Claude}\par}
\vspace{4mm}
{\small Version 1.3 \quad October 2026\par}
\vspace{10mm}
\pgfornament[width=11cm,color=cublue,symmetry=h]{88}\par
\end{titlepage}
"""


def intro():
    return r"""
\chapter{Introduction}

This booklet sets out the four-year B.S.\ (Honours) programme in Physics that Rimon is following alongside his degree in Computer Science and Engineering. It is laid out like a university information booklet so that it can be printed, kept at the desk and consulted offline. It first states the rules and regulations that govern progression through the programme, and then gives the outlines of every course in the curriculum, semester by semester.

The programme lives in a Git repository,
\url{https://github.com/mahmudhassanrimoncu-ship-it/Undergraduate_Physics_Programme_2026}.
If this booklet and the repository ever disagree, the repository is current and this booklet is reissued.

\section{The Programme}

The programme is a self-directed undergraduate degree built from the actual curricula of five leading physics departments, with the University of Dhaka as a regional reference. It runs for four years of three 16-week semesters each (Spring, Summer and Autumn), preceded by a seven-week Orientation Term, and takes 18--22 hours a week: three courses per semester. Like a real department it has a calendar, syllabi, prerequisites, problem sets, midterm and final examinations, annual comprehensive examinations with a viva voce, two junior papers, a senior thesis, a transcript and a final degree classification.

Claude acts as instructor, teaching assistant, tutor, librarian, editor and examiner. Classes are taught live at fixed slots on a weekly class routine (Chapter~\ref{ch:routine}), or later the same week when the student's CSE commitments clash.

\section{What Is Borrowed from Where}

\begin{xltabular}{\linewidth}{>{\raggedright\arraybackslash}p{0.27\linewidth}>{\raggedright\arraybackslash}p{0.27\linewidth}X}
\toprule
\sffamily Feature & \sffamily Borrowed from & \sffamily How it works here\\ \midrule
Three terms a year & Oxford; Caltech & Three 16-week semesters a year\\
Tutorials & Oxford & Weekly oral defence of the student's own problem-set solutions\\
Problem sets, midterm and final & MIT, Harvard, Princeton & The weekly rhythm of every theory course\\
Calculus-based core sequence & MIT 8.01--8.04; Harvard 15a/b/c & Years 1 and 2\\
Collections & Oxford & An ungraded diagnostic test in week~1 on the previous semester\\
Annual examinations & Oxford Prelims, Parts A, B and C & A comprehensive examination at the end of each year\\
Viva voce & University of Dhaka (PV~102--402) & A 30--45 minute oral examination each year\\
Junior Lab and experiment project & MIT 8.13/8.14; Harvard 191; Caltech Ph~77 & LAB 301 and LAB 401\\
Junior Papers & Princeton & IND 301 and IND 302\\
Communication requirement & MIT CI-M; Caltech Ph~70; Harvard 95 & Built into IND 302 and the thesis\\
Senior Thesis & MIT 8.THU; Princeton; Oxford MPhys & THS 401 and THS 402\\
Two major options & Oxford Part C (C1--C7) & Major Options I and II in Year 4\\
Advanced Standing Exams & MIT & Testing out of MTH 101--104 or CMP 101\\
Honour code & Caltech & Section~\ref{sec:conduct}\\
\bottomrule
\end{xltabular}

\section{Document Organisation}

The rest of this document consists of the following parts:
\begin{itemize}[label=\pen,leftmargin=2em,itemsep=3pt]
\item The rules and regulations of the programme --- course system, calendar, grading, examinations, progression and the degree --- are presented in Chapter~\ref{ch:rules}.
\item The programme's mission, educational objectives and learning outcomes, and a summary of the whole curriculum, are given in Chapter~\ref{ch:obe}.
\item The details of every course --- rationale, learning outcomes, assessment strategy, weekly schedule and texts --- are given semester by semester in Chapter~\ref{ch:courses}, with the annual examinations at the end of each year.
\item The Year~4 major options and electives are described in Chapter~\ref{ch:options}, and the class routines in Chapter~\ref{ch:routine}.
\end{itemize}
"""


def rules():
    return r"""
\chapter{Rules and Regulations}\label{ch:rules}

These are the rules of the department. Where a course syllabus says something different, the syllabus wins for that course. Any change agreed between the student and the instructor is recorded in the changelog of the Programme Handbook in the repository.

\section{Programme's Course System}

\subsubsection{Duration and semesters} The programme runs for four academic years. Each year has three semesters of 16 weeks: Spring (January--April), Summer (May--August) and Autumn (late August--December). A seven-week, ungraded Orientation Term precedes the first semester.

\subsubsection{Load} Three courses are taken each semester, at about 6--7 hours each, for a total of 18--22 hours a week. Some weeks before examinations will reach about 25 hours.

\subsubsection{Credits} Every course carries 4 credits, and one credit is roughly 25 hours of total work. Each annual examination also carries 4 credits.

\begin{center}
\begin{tabular}{lccc}
\toprule
\sffamily Item & \sffamily Credits & \sffamily Count & \sffamily Total\\ \midrule
Course (theory, laboratory, computational or independent work) & 4 & 36 & 144\\
Annual examination (written papers and viva voce) & 4 & 4 & 16\\ \midrule
\multicolumn{3}{r}{\textbf{Degree total}} & \textbf{160}\\
\bottomrule
\end{tabular}
\end{center}

\subsubsection{Course types} \emph{Theory} courses (PHY, MTH, options and most electives) have two 80-minute lectures and a one-hour recitation a week. \emph{Computational} courses (CMP) have a lecture and a laboratory. \emph{Laboratory} courses (LAB) replace problem sets with experiments, a notebook and reports. \emph{Independent work} (IND) and the \emph{Senior Thesis} (THS) are supervised research.

\subsubsection{Weekly rhythm} Each Monday the week's reading, lectures and problem set are released. Problem sets are due on Sunday at 23:59 (Bangladesh time) and are returned within 48 hours with written feedback, after which the tutorial on that set takes place. Work may be handwritten and uploaded, or committed to the repository under \texttt{work/}.

\subsubsection{Prerequisites} A course used as a prerequisite must have been passed with C (55\%) or better.

\subsubsection{Advanced Standing} During the Orientation Term the student may sit a 2-hour Advanced Standing Exam (ASE) in MTH 101, MTH 102, MTH 103, MTH 104 or CMP 101. A score of 70\% or more exempts the course; it is recorded as Credit by Examination (CR), carries credits and is not counted in the GPA. The freed slot is filled by an Honours Extra from the electives list.

\section{Academic Calendar}

Every semester follows the same 16-week pattern.

\begin{center}
\begin{tabularx}{0.9\linewidth}{cX}
\toprule
\sffamily Week & \sffamily Purpose\\ \midrule
1 & Teaching starts; \emph{Collection} (ungraded diagnostic) on the previous semester\\
1--6 & Teaching\\
7 & Midterm examinations (teaching continues at a lighter pace)\\
8--13 & Teaching\\
14 & Revision week: no new material; practice papers\\
15 & Final examinations\\
16 & Grading, feedback and the Semester Report; in Autumn, the Annual Examination and viva\\
\bottomrule
\end{tabularx}
\end{center}

""" + calendar_table() + r"""

There is a one-week break after the Spring and Summer semesters and a two-week break after Autumn.

\subsubsection{Flexibility} The student's CSE degree comes first when its examinations fall in the same weeks. A semester may be \emph{shifted} by up to two weeks with notice before week~1, or \emph{paused} for up to three weeks mid-semester (for example, for CSE finals or Eid). The calendar is then reissued and the change logged.

\section{Grading System and Marks Distribution}

\subsection{Letter grades}

\begin{center}
\rowcolors{2}{white}{rowgrey}
\begin{tabular}{ccc|ccc}
\toprule
\sffamily Letter & \sffamily Marks (\%) & \sffamily Grade point & \sffamily Letter & \sffamily Marks (\%) & \sffamily Grade point\\ \midrule
A & 85--100 & 4.0 & C$+$ & 60--64 & 2.3\\
A$-$ & 80--84 & 3.7 & C & 55--59 & 2.0\\
B$+$ & 75--79 & 3.3 & D & 50--54 & 1.0\\
B & 70--74 & 3.0 & F & below 50 & 0.0\\
B$-$ & 65--69 & 2.7 & CR & ASE $\geq 70$ & not in GPA\\
\bottomrule
\end{tabular}
\end{center}

Problems are set at MIT, Oxford and Princeton difficulty, so the boundaries are placed where a leading department's curve usually puts them. If an examination turns out harder or easier than intended, the examiner may scale it once, with a written justification recorded in the gradebook.

\subsection{Marks distribution by course type}

""" + weights_tables() + r"""

\needspace{12\baselineskip}\subsection{How written work is marked}

Every problem is marked out of 10.

\begin{center}
\begin{tabular}{lc}
\toprule
\sffamily Criterion & \sffamily Marks\\ \midrule
Physical set-up: principles, diagram, coordinates, stated assumptions & 3\\
Mathematical execution & 3\\
Correct final result, boxed & 2\\
Sanity checks: units, limiting cases, order of magnitude & 1\\
Clarity: someone else could follow the solution & 1\\
\bottomrule
\end{tabular}
\end{center}

A correct answer with no reasoning earns at most 3/10; a clear, correct method with an arithmetic slip earns 8--9/10.

\subsubsection{Late work} Late work loses 10\% a day for up to three days and then scores zero. Three \emph{late tokens} per semester each give a 24-hour extension with no questions asked. Examinations cannot be late, but they may be rescheduled before the examination week begins.

\subsection{Tutorials}
After each problem set is graded, the tutor picks one or two problems and the student explains the reasoning, in writing or by voice note, and handles follow-up questions (``what changes if\ldots'', ``estimate\ldots''). Each tutorial also includes a \emph{self-explanation round}, in which the student talks through the posted solution to the problem found hardest. Each tutorial is scored 0 (absent), 1 (cannot explain own work), 2 (solid) or 3 (insightful).

\section{Teaching Method}

Every lecture, recitation, problem set and tutorial is designed by cognitive load theory (Sweller), as summarised by Scott H.~Young. Working memory is small for new material and effectively unlimited for mastered material, and physics has high \emph{element interactivity}, so the aim is to keep the load of each class in the productive zone. The full method is in \texttt{docs/teaching-method.md}; in summary:

\begin{center}\small
\rowcolors{2}{white}{rowgrey}
\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}p{0.3\linewidth}X}
\toprule
\sffamily Principle & \sffamily What happens in class\\ \midrule
Worked-example effect & Every new method is first shown as a fully worked example, then practised: example, completion problem, full problem, mixed problems.\\
Expertise reversal & Support fades topic by topic; once a method is mastered, the student solves first and sees no example.\\
Prerequisite fluency & Each lecture opens with a five-minute warm-up on the components it depends on; gaps get a short fluency drill.\\
Split attention and extraneous load & Integrated notes (labels on figures, equations beside their figures), one primary text, one weekly release.\\
Goal-free effect & New topics may open with ``find everything you can'' warm-ups where the possible moves are few.\\
Germane load & Weekly quizzes (retrieval), self-explanation in tutorials, and interleaved problems once a topic is secure.\\
Load check & After each lecture and problem set the student rates mental effort from 1 to 9; the rating, with quiz scores, sets the pace.\\
\bottomrule
\end{tabularx}
\end{center}

Problem sets have up to three parts: \textbf{A}~example pairs (each problem with a solved twin, early in a topic), \textbf{B}~core problems, and \textbf{C}~mixed and stretch problems (once the topic is secure). The share of Part~A shrinks as each course and the programme go on. The method changes no grading weights.

\section{Examinations and Progression}

\subsubsection{Passing a course} A course is passed when the overall weighted mark is at least 50\% (grade D) \emph{and} the final-examination mark is at least 40\%.

\subsubsection{Resit} A student who fails a course, or fails only the final-examination hurdle, may take one resit of the final examination in week~16 or in week~1 of the next semester. The resit replaces the final mark and the course grade is capped at C.

\subsubsection{Retake} A course still failed after the resit is retaken in full in a later semester. The new grade replaces the old one in the GPA, but the original F remains visible on the transcript.

\needspace{10\baselineskip}\subsubsection{Semester standing}
\begin{center}
\begin{tabularx}{\linewidth}{>{\bfseries}lXX}
\toprule
\sffamily\mdseries Standing & \sffamily Rule & \sffamily Consequence\\ \midrule
Dean's List & Semester GPA $\geq 3.70$ with no grade below B & Noted on the transcript\\
Good standing & Semester GPA $\geq 2.00$ and every course passed & Continue as planned\\
Warning & Semester GPA $\geq 2.00$ but a course failed & Resit or retake plan agreed in week~16\\
Probation & Semester GPA $< 2.00$ & Next semester drops to two courses with a remedial plan; two consecutive probations trigger a programme review\\
\bottomrule
\end{tabularx}
\end{center}

\subsubsection{Annual examinations} In week~16 of each Autumn semester the student sits an Oxford-style annual examination on the whole year's core courses: \emph{Prelims} (Year~1), \emph{Part~A} (Year~2), \emph{Part~B} (Year~3) and \emph{Finals, Part~C} (Year~4). The written papers carry 80\% and the viva voce 20\%, and each counts as a 4-credit item in the CGPA. A mark of at least 50\% is required to progress to the next year; one resit is allowed in week~1 of the next semester, capped at C. The papers for each year are listed at the end of that year in Chapter~\ref{ch:courses}.

\subsubsection{Viva voce} An oral examination, as at Dhaka and Oxford, covering the year's material and the student's own submitted work. The student is asked to derive, explain and estimate. It is marked for correctness (40\%), depth of understanding (30\%), clarity (15\%) and handling of unfamiliar follow-up questions (15\%).

\subsubsection{Progression} To progress to the next year the student must pass all of that year's courses and its annual examination.

\section{Degree and Results}

\subsubsection{GPA} The semester GPA is $\sum(\text{grade points}\times\text{credits})/\sum\text{credits}$ over the items graded that semester; the CGPA is the same sum over every graded item to date, including annual examinations. The transcript records every course with its code, title, credits, grade, grade points and any resit or retake, together with the SGPA, CGPA, standing and annual-examination results.

\subsubsection{Degree requirements} The degree is awarded when the student has (1) passed 160 credits, including all 36 courses or approved substitutes; (2) passed all core courses, with C or better wherever a course was used as a prerequisite; (3) passed all four annual examinations; (4) passed THS 402 Senior Thesis II with C or better; and (5) a CGPA of at least 2.00.

\needspace{10\baselineskip}\subsubsection{Classification}
\begin{center}
\rowcolors{2}{white}{rowgrey}
\begin{tabular}{lll}
\toprule
\sffamily CGPA & \sffamily Classification & \sffamily US equivalent\\ \midrule
$\geq 3.85$ & First Class Honours with Distinction & Summa cum laude\\
3.70--3.84 & First Class Honours & Magna cum laude\\
3.30--3.69 & Upper Second Class (2:1) & Cum laude\\
2.70--3.29 & Lower Second Class (2:2) & --\\
2.00--2.69 & Pass & --\\
\bottomrule
\end{tabular}
\end{center}

A First requires the Senior Thesis to be graded A$-$ or better; otherwise the classification is capped at 2:1 (Princeton and Harvard practice). If the Year~3--4 CGPA is higher than the overall CGPA, the higher figure is used for classification (Oxford practice).

\section{Conduct, Submissions and Appeals}\label{sec:conduct}

\subsubsection{Honour code} Caltech's Honor Code reads: \emph{``No member of the Caltech community shall take unfair advantage of any other member of the Caltech community.''} Here the only person who can be cheated is the student. Accordingly:
\begin{enumerate}[label=(\alph*)]
\item for problem sets, the textbook, lecture notes and the tutor may be used for hints, but not solution manuals, answer websites or another AI's answers to the specific problem before submission (the solved twins in a set's Part~A are part of the set and may be used);
\item examinations are closed book apart from the stated formula sheet, use a simple scientific calculator and no internet, are timed, and have their start and end times written on the first page;
\item laboratory data must be real; a well-analysed failure scores better than a fabricated success;
\item papers and the thesis must be the student's own writing, with sources quoted and cited.
\end{enumerate}
A breach scores zero on that item and is noted on the transcript.

\subsubsection{Submissions} Work may be uploaded as photographs or a PDF in the course thread, or committed to \texttt{work/<semester>/<course>/<item>/} in the repository. Handwritten work is encouraged for problem sets and examinations. Final answers are boxed, with units and limiting cases checked. Code is submitted as \texttt{.py} or \texttt{.ipynb} files with a short README.

\subsubsection{Feedback} Every problem set receives written feedback; there is a mid-semester check-in in week~8; and at the end of each semester the student receives a Semester Report, in the manner of an Oxford college report, with grades, strengths, weaknesses and adjustments for the next semester.

\subsubsection{Appeals} A student who believes a mark is wrong says so within seven days. The item is re-marked in full and the decision explained; as at a real university, the re-mark may go up or down.
"""


def calendar_table():
    rows = [
        ("Orientation Term", "Mon 2 Nov 2026", "--", "--", "Sun 20 Dec 2026"),
        ("1 Spring 2027", "Mon 4 Jan 2027", "15 Feb", "12 Apr", "Sun 25 Apr 2027"),
        ("2 Summer 2027", "Mon 3 May 2027", "14 Jun", "9 Aug", "Sun 22 Aug 2027"),
        ("3 Autumn 2027", "Mon 30 Aug 2027", "11 Oct", "6 Dec", "Sun 19 Dec 2027 (Prelims)"),
        ("4 Spring 2028", "Mon 3 Jan 2028", "14 Feb", "10 Apr", "Sun 23 Apr 2028"),
        ("5 Summer 2028", "Mon 1 May 2028", "12 Jun", "7 Aug", "Sun 20 Aug 2028"),
        ("6 Autumn 2028", "Mon 28 Aug 2028", "9 Oct", "4 Dec", "Sun 17 Dec 2028 (Part A)"),
        ("7 Spring 2029", "Mon 1 Jan 2029", "12 Feb", "9 Apr", "Sun 22 Apr 2029"),
        ("8 Summer 2029", "Mon 30 Apr 2029", "11 Jun", "6 Aug", "Sun 19 Aug 2029"),
        ("9 Autumn 2029", "Mon 27 Aug 2029", "8 Oct", "3 Dec", "Sun 16 Dec 2029 (Part B)"),
        ("10 Spring 2030", "Mon 7 Jan 2030", "18 Feb", "15 Apr", "Sun 28 Apr 2030"),
        ("11 Summer 2030", "Mon 6 May 2030", "17 Jun", "12 Aug", "Sun 25 Aug 2030"),
        ("12 Autumn 2030", "Mon 2 Sep 2030", "14 Oct", "9 Dec", "Sun 22 Dec 2030 (Finals)"),
    ]
    out = [r"\begin{center}\small", r"\rowcolors{2}{white}{rowgrey}",
           r"\begin{tabular}{lllll}", r"\toprule",
           r"\sffamily Semester & \sffamily Teaching starts & \sffamily Midterms & \sffamily Finals & \sffamily Ends\\ \midrule"]
    out += [" & ".join(r) + r"\\" for r in rows]
    out += [r"\bottomrule", r"\end{tabular}", r"\end{center}"]
    return "\n".join(out)


def weights_tables():
    def block(title, comps):
        rows = "\n".join("%s & %s\\\\" % (c[0], c[2]) for c in comps)
        return (r"\begin{minipage}[t]{0.48\linewidth}\centering\small" "\n"
                r"\begin{tabular}{lr}\toprule" "\n"
                r"\multicolumn{2}{l}{\sffamily %s}\\ \midrule" "\n" % title
                + rows + "\n" r"\midrule Total & 100\%\\ \bottomrule\end{tabular}\end{minipage}")
    ind = [("Proposal", "", "10\\%"), ("Progress meetings / three talks", "", "15 / 25\\%"),
           ("Paper", "", "55 / 50\\%"), ("Presentation / referee report", "", "20 / 15\\%")]
    ths = [("Thesis I: proposal and literature review", "", "25\\%"), ("Thesis I: progress report", "", "25\\%"),
           ("Thesis I: interim presentation", "", "25\\%"), ("Thesis I: supervisor's assessment", "", "25\\%")]
    return ("\\noindent" + block("Theory courses", DEFAULT_ASSESS["theory"]) + "\\hfill"
            + block("Laboratory courses", DEFAULT_ASSESS["lab"]) + "\n\n\\bigskip\\noindent"
            + block("Computational courses (no closed-book exam)", DEFAULT_ASSESS["comp"]) + "\\hfill"
            + block("Junior Papers (IND 301 / IND 302)", ind) + "\n\n\\bigskip"
            + "\nThe Senior Thesis is weighted as shown on its course pages: in THS 401, the proposal and literature review, progress report, interim presentation and supervisor's assessment carry 25\\% each; in THS 402, the thesis carries 60\\%, the oral defence 25\\% and the poster or public talk 15\\%. Where an individual course departs from these weights, its own page says so.\n")


# ------------------------------------------------------------------- chapter 3
def obe():
    out = [r"""
\chapter{OBE and Curriculum Summary}\label{ch:obe}

\section{Programme Mission}

To give a computer scientist the education of a physics major from a leading department: a deep, problem-solving command of the core of physics, the mathematics and computation it is written in, the experimental and statistical habits that make it a science, and the experience of original research --- learnt on a timetable, assessed honestly, and documented so that it can be shown to others.

\section{PEO and PLO}

\subsection*{Programme Educational Objectives (PEO)}
A few years after completing the programme, the graduate is expected to:
\begin{description}[leftmargin=3.4em,labelwidth=3em,font=\normalfont\scshape]"""]
    for i, p in enumerate(PEOS, 1):
        out.append(r"\item[peo$_{%d}$] %s" % (i, p))
    out.append(r"""\end{description}

\subsection*{Programme Learning Outcomes (PLO)}
On completing the programme, the graduate will be able to:
\begin{description}[leftmargin=3.4em,labelwidth=3em,font=\normalfont\scshape]""")
    for i, (t, d) in enumerate(PLOS, 1):
        out.append(r"\item[plo$_{%d}$] {\sffamily %s:} %s" % (i, t, d))
    out.append(r"\end{description}")
    out.append(r"""
\subsection*{Mapping of PLOs to PEOs}
\begin{center}
\begin{tabular}{l""" + "c" * 10 + r"""}
\toprule
""" + " & ".join(["\\sffamily"] + [r"\textsc{plo}$_{%d}$" % i for i in range(1, 11)]) + r"\\ \midrule")
    for j in range(1, 4):
        out.append(" & ".join([r"\textsc{peo}$_{%d}$" % j] + [r"\ding{51}" if j in PLO_PEO[i] else "" for i in range(1, 11)]) + r"\\")
    out.append(r"""\bottomrule
\end{tabular}
\end{center}

Every course page in Chapter~\ref{ch:courses} lists its course learning outcomes (\textsc{clo}s) with the Bloom's taxonomy level and the \textsc{plo}s each one serves.

\section{Curriculum at a Glance}

Each semester carries three 4-credit courses; the Autumn semesters of each year also carry the 4-credit annual examination.
""")
    for name, dates, courses in [("Orientation Term", "2 Nov -- 20 Dec 2026 (7 weeks, ungraded)", [ORI])] + SEMESTERS:
        out.append(semester_table(name, dates, courses))
    out.append(credit_distribution())
    return "\n".join(out)


def semester_table(name, dates, courses, tag=True):
    exam = ANNUAL.get(name)
    rows = []
    for c in courses:
        credits = "0" if c["kind"] == "ori" else "4"
        rows.append("%s & %s & %s & %s & %s\\\\" % (c["code"], c["title"], KIND_LABEL[c["kind"]], credits,
                                                  c["hours"].replace(" Hours/Week", "")))
    if exam:
        rows.append("%s & %s & %s & 4 & --\\\\" % (exam["code"], exam["title"], KIND_LABEL["exm"]))
    total = 0 if courses[0]["kind"] == "ori" else 4 * len(courses) + (4 if exam else 0)
    head = r"\semtag{%s}{%s}" % (name, dates) if tag else ""
    return head + r"""
\begin{center}\small
\rowcolors{2}{rowgrey}{white}
\begin{tabularx}{\linewidth}{lXlcc}
\toprule
\rowcolor{white}\sffamily \makecell[l]{Course\\Code} & \sffamily Course Title & \sffamily Type & \sffamily Credits & \sffamily \makecell{Hours/\\Week}\\ \midrule
""" + "\n".join(rows) + r"""
\midrule\rowcolor{white}
\multicolumn{3}{r}{Total} & %d & \\
\bottomrule
\end{tabularx}
\end{center}
""" % total


def credit_distribution():
    return r"""
\section{Credit Distribution}

The distribution of credits across the categories of course is summarised below.

\begin{center}
\rowcolors{2}{white}{rowgrey}
\begin{tabularx}{\linewidth}{lXcc}
\toprule
\sffamily Category & \sffamily Courses & \sffamily Courses & \sffamily Credits\\ \midrule
Core physics (theory) & PHY 101--103, 201--206, 301--306, 401--402 & 17 & 68\\
Mathematics & MTH 101--104, MTH 201 & 5 & 20\\
Computation & CMP 101, CMP 201 & 2 & 8\\
Laboratory & LAB 101, 201, 301, 401 & 4 & 16\\
Independent work and thesis & IND 301, IND 302, THS 401, THS 402 & 4 & 16\\
Specialisation & Two major options and two electives & 4 & 16\\
Annual examinations & EXM 100, 200, 300, 400 & 4 & 16\\ \midrule
\rowcolor{white}\multicolumn{2}{r}{\textbf{Total}} & \textbf{40} & \textbf{160}\\
\bottomrule
\end{tabularx}
\end{center}
"""


# ------------------------------------------------------------------- chapter 4
def course(c):
    k = c["kind"]
    credits = "Ungraded" if k == "ori" else "4 Credits"
    o = [r"\coursehead{%s}{%s}{%s}{%s}" % (c["code"], c["title"], credits, c["hours"])]
    o.append(r"\infoline{Prerequisites}{%s}" % c["prereq"])
    o.append(r"\infoline{Modelled on}{%s}" % c["models"])
    o.append(r"\coursesub{Rationale}" + "\n" + c["rationale"])
    o.append(r"\coursesub{Course Learning Outcomes and Related Mapping}")
    o.append(r"""{\small
\begin{xltabular}{\linewidth}{c>{\raggedright\arraybackslash}Xcc}
\toprule
 & {\sffamily Course Learning Outcome (\textsc{clo})}\newline Upon successful completion of this course, the student will be able to: & \sffamily\makecell{Bloom's\\Level} & \sffamily\makecell{Associated\\\textsc{plo}}\\ \midrule
\endhead""")
    for i, (txt, bloom, plo) in enumerate(c["clos"], 1):
        o.append(r"\clo{%d} & %s & %s & %s\\" % (i, txt, bloom, plo_tex(plo)))
    o.append(r"\bottomrule" "\n" r"\end{xltabular}}")
    deliv, tools = DELIVERY[k]
    o.append(r"\infoline{Delivery methods and activities}{include %s.}" % deliv)
    o.append(r"\infoline{Assessment tools}{are %s.}" % tools)
    assess = c.get("assess")
    if assess:
        assess = [(a[0], "", a[1]) if len(a) == 2 else a for a in assess]
    else:
        assess = DEFAULT_ASSESS[k]
    o.append(r"\needspace{9\baselineskip}\infoline{Assessment strategy}{is comprised of the following elements, with the distribution of marks shown.}")
    o.append(r"""\begin{center}\small
\begin{tabularx}{0.92\linewidth}{rXr}
\toprule""")
    for i, (lab, desc, pct) in enumerate(assess, 1):
        d = (" --- " + desc) if desc else ""
        o.append(r"%d & \textsc{%s}%s & %s\\" % (i, lab, d, pct))
    o.append(r"\midrule & \hfill Total & %s\\" % ("--" if k == "ori" else "100\\%"))
    o.append(r"\bottomrule\end{tabularx}\end{center}")
    if c.get("assess_note"):
        o.append(r"{\small %s\par}" % c["assess_note"])
    o.append(r"\coursesub{Content Outline and Course Schedule}")
    o.append(schedule_table(c))
    o.append(r"\coursesub{Texts and Materials}")
    o.append(r"\begin{enumerate}[label=\arabic*.,itemsep=1pt]\small")
    o += [r"\item " + t for t in c["texts"]]
    o.append(r"\end{enumerate}")
    return "\n".join(o)


def schedule_table(c):
    sections = c["kind"] in ("theory", "comp")
    o = [r"""{\small
\begin{xltabular}{\linewidth}{c>{\raggedright\arraybackslash}X}
\toprule
\sffamily Week & \sffamily Topic\\ \midrule
\endhead"""]
    if sections:
        o.append(r"\multicolumn{2}{l}{\footnotesize\textsc{section a}}\\[-2pt]")
    for week, topic in c["schedule"]:
        o.append(r"%s & %s\\" % (week, topic))
        if sections and "idterm" in topic:
            o.append(r"\multicolumn{2}{l}{\footnotesize\textsc{section b}}\\[-2pt]")
    o.append(r"\bottomrule" "\n" r"\end{xltabular}}")
    return "\n".join(o)


def annual(e):
    o = [r"\coursehead{%s}{%s}{4 Credits}{Papers and Viva}" % (e["code"], e["title"])]
    o.append(r"\infoline{When}{%s}" % e["when"])
    o.append(r"\infoline{Modelled on}{%s}" % e["model"])
    o.append(r"""\begin{center}\small
\begin{tabularx}{\linewidth}{>{\raggedright\arraybackslash}p{0.3\linewidth}Xc}
\toprule
\sffamily Paper & \sffamily Content & \sffamily Time\\ \midrule""")
    o += [r"%s & %s & %s\\" % p for p in e["papers"]]
    o.append(r"\bottomrule\end{tabularx}\end{center}")
    nxt = ("A mark of at least 50\\%% is required to progress to %s." % e["progress"]) if e["progress"] else \
        "Once EXM 400 and THS 402 are graded, the degree is classified and the final transcript is issued."
    o.append(r"Written papers 80\%%, viva voce 20\%%. %s" % nxt)
    return "\n".join(o)


def courses_chapter():
    o = [r"""
\chapter{Course Details}\label{ch:courses}

Detailed outlines of all the courses belonging to the different semesters are produced in the following. Week numbers refer to the 16-week semester of Section~2.2; in theory and computational courses, \textsc{section a} covers the material examined at the midterm and \textsc{section b} the remainder.

\section{Orientation Term}
""" + semester_table("Orientation Term", "2 Nov -- 20 Dec 2026", [ORI], tag=False)]
    o.append(course(ORI))
    for i, (name, dates, cs) in enumerate(SEMESTERS):
        o.append(r"\clearpage" "\n" r"\section{%s}" % name)
        o.append(r"{\small\sffamily %s}" % dates)
        o.append(semester_table(name, dates, cs, tag=False))
        real = [c for c in cs if c["kind"] != "opt"]
        if len(real) < len(cs):
            o.append(r"The major option and elective are chosen by week~12 of the Ninth Semester; their outlines are in Chapter~\ref{ch:options}.")
        for c in real:
            o.append(course(c))
        if name in ANNUAL:
            o.append(annual(ANNUAL[name]))
    return "\n".join(o)


# ------------------------------------------------------------------- chapter 5
def options_chapter():
    o = [r"""
\chapter{Major Options and Electives}\label{ch:options}

In Year~4 the student takes two \emph{major options} (Oxford Part~C model) and two \emph{electives}, in the Eleventh and Twelfth Semesters. The options are chosen by week~12 of the Ninth Semester. All options and electives are theory courses with the standard weights (problem sets 25\%, quizzes 5\%, tutorials 10\%, midterm 20\%, final 40\%) unless stated otherwise, and each option's final examination also forms a Part~C paper. A full week-by-week syllabus is issued in the semester before the course runs.

\section{Major Options}
"""]
    for code, title, model, pre, text, topics in OPTIONS:
        o.append(r"\coursehead{%s}{%s}{4 Credits}{4 Hours/Week}" % (code, title))
        o.append(r"\infoline{Prerequisites}{%s}" % pre)
        o.append(r"\infoline{Modelled on}{%s}" % model)
        o.append(r"\infoline{Texts}{%s.}" % text)
        o.append(r"\coursesub{Content}" + "\n" + topics)
    o.append(r"""
\section{Electives}

\begin{center}\small
\rowcolors{2}{rowgrey}{white}
\begin{xltabular}{\linewidth}{l>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}p{0.17\linewidth}>{\raggedright\arraybackslash}p{0.15\linewidth}>{\raggedright\arraybackslash}p{0.16\linewidth}}
\toprule
\rowcolor{white}\sffamily Code & \sffamily Elective & \sffamily Prerequisites & \sffamily Text & \sffamily Notes\\ \midrule
\endhead""")
    o += [r"%s & %s & %s & %s & %s\\" % e for e in ELECTIVES]
    o.append(r"""\bottomrule
\end{xltabular}
\end{center}
""")
    return "\n".join(o)


# ------------------------------------------------------------------- chapter 6
def routine_chapter():
    s01 = "semesters/timetables/S01-2027-spring-timetable.md"
    s00 = "semesters/timetables/S00-orientation-timetable.md"
    o = [r"""
\chapter{Class Routine}\label{ch:routine}

Every term has a fixed weekly class routine, like a university's. A slot is when a class is \emph{scheduled}: the student attends it live with the instructor at that time, or later the same day or week when CSE work clashes. To attend, the student writes the course and lecture number in the course thread (for example, ``PHY 101 L5''); the lecture is taught live, and its notes are saved to \texttt{lectures/} in the repository. All times are Bangladesh time (UTC+6). The routine for each later semester is issued at least two weeks before it starts, so that it fits around the CSE timetable for that term.

\section{Default Weekly Pattern}

Each theory course has two 80-minute lectures and a one-hour recitation (which opens with the weekly quiz); each computational course has a lecture and a laboratory. Tutorials and office hours are on Saturday afternoon, problem-set blocks on Friday and Saturday mornings, and problem sets are due on Sunday at 23:59.

\section{Orientation Term (2 November -- 20 December 2026)}

{\small
\rowcolors{2}{white}{rowgrey}
\begin{xltabular}{\linewidth}{c>{\raggedright\arraybackslash}p{0.27\linewidth}>{\raggedright\arraybackslash}X}
\toprule
\rowcolor{white}\sffamily Week & \sffamily Date and time & \sffamily Session\\ \midrule
\endhead"""]
    o += [" & ".join(r) + r"\\" for r in md_table(s00, "")]
    o.append(r"""\bottomrule
\end{xltabular}}

\section{First Semester, Spring 2027}

\subsection*{Weekly routine (teaching weeks 1--6 and 8--13)}
{\small
\begin{center}
\renewcommand{\arraystretch}{1.5}
\begin{tabularx}{\linewidth}{>{\bfseries}l>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X}
\toprule
\sffamily\mdseries Day & \sffamily Morning & \sffamily Afternoon & \sffamily 19:30--20:50 & \sffamily 21:00--22:20\\ \midrule
Mon & & & PHY 101 Lecture & MTH 101 Lecture\\
Tue & & & CMP 101 Lecture & PHY 101 Recitation (21:00--22:00, opens with the quiz)\\
Wed & & & PHY 101 Lecture & MTH 101 Lecture\\
Thu & & & CMP 101 Lab & MTH 101 Recitation (21:00--22:00, opens with the quiz)\\
Fri & Problem-set block (09:00--12:00) & & & \\
Sat & Problem-set block (10:00--12:30) & Tutorials: PHY 101, MTH 101, CMP 101 (16:00--17:30); office hours (17:30--18:30) & & \\
Sun & & & Problem-set wrap-up (19:30--21:30) & \textbf{Problem sets due 23:59}\\
\bottomrule
\end{tabularx}
\end{center}}
Weekly totals: lectures, recitations and laboratories 10~h; tutorials and office hours 2.5~h; problem-set blocks 7.5~h; about 20~h in all.

\subsection*{Lecture calendar: PHY 101 and MTH 101}
{\small
\rowcolors{2}{white}{rowgrey}
\begin{xltabular}{\linewidth}{cl>{\raggedright\arraybackslash}X>{\raggedright\arraybackslash}X}
\toprule
\rowcolor{white}\sffamily Week & \sffamily Date & \sffamily PHY 101, 19:30 & \sffamily MTH 101, 21:00\\ \midrule
\endhead""")
    for r in md_table(s01, "Lecture calendar: PHY 101 and MTH 101"):
        r[2] = r[2].replace("PHY 101 ", "", 1)
        r[3] = r[3].replace("MTH 101 ", "", 1)
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
    for r in md_table(s01, "Lecture calendar: CMP 101"):
        if len(r) == 3:
            r = [r[0], r[1], r"\multicolumn{2}{l}{%s}" % r[2]]
        o.append(" & ".join(r) + r"\\")
    o.append(r"""\bottomrule
\end{xltabular}}

\subsection*{Examination and special weeks}
{\small
\begin{xltabular}{\linewidth}{cl>{\raggedright\arraybackslash}X}
\toprule
\sffamily Week & \sffamily Dates & \sffamily What happens\\ \midrule
\endhead""")
    o += [" & ".join(r) + r"\\" for r in md_table(s01, "Exam and special weeks")]
    o.append(r"""\bottomrule
\end{xltabular}}

\subsubsection{Ramadan and Eid} Ramadan 2027 is expected to run from about 8 February to 9 March, with Eid al-Fitr around 10 March, subject to the moon sighting. If needed, evening slots can move to 21:30--23:30 after tarawih, or a one-week Eid pause can be taken in week~10. Nothing changes until the student asks.

\subsubsection{Clashes} If the CSE timetable clashes, the slots are moved but the weekly structure stays the same.
""")
    return "\n".join(o)


def build():
    parts = [PREAMBLE, r"\begin{document}", r"\frontmatter", cover(),
             r"\cleardoublepage", r"\setcounter{tocdepth}{1}", r"\tableofcontents", r"\mainmatter",
             intro(), rules(), obe(), courses_chapter(), options_chapter(), routine_chapter(),
             r"\end{document}"]
    tex = "\n".join(parts)
    with open(os.path.join(HERE, "booklet.tex"), "w", encoding="utf-8") as f:
        f.write(tex)
    print("wrote booklet.tex (%d lines)" % tex.count("\n"))


if __name__ == "__main__":
    build()
