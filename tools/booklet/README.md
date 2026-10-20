# Printable programme booklet

This folder generates [docs/Physics-Programme-Booklet.pdf](../../docs/Physics-Programme-Booklet.pdf), a printable information booklet for the programme. Its layout follows the University of Chittagong CSE information booklet: rules and regulations, outcomes and the curriculum at a glance, then one outline per course (rationale, CLO table, assessment strategy, weekly schedule, texts), options and electives, and the class routine.

| File | Contents |
|---|---|
| `data_y1.py` … `data_y4.py` | Course data for each year, as LaTeX-ready strings |
| `build.py` | Writes `booklet.tex`: rules, outcomes, curriculum tables, course pages, routine (the routine tables are read from `semesters/timetables/`) |
| `make.sh` | Builds the PDF and copies it to `docs/` |

To rebuild after changing a course or a rule: edit the data file (or `build.py`), then run `./make.sh`. It needs Python 3 and a TeX Live install with `pdflatex`.

When the markdown syllabi in `semesters/` change, update the matching data file too, so that the booklet and the repository stay in step.
