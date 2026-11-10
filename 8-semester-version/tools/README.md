# Tools for the 8-semester version

Everything in this folder is generated from the main 12-term files, so the two versions can't drift apart by accident.

| File | What it does |
|---|---|
| `plan.py` | The 8 semesters: dates, which courses go where, and the conversion from 16-week to 22-week week numbers |
| `make_semesters.py` | Writes `../semesters/S1…S8` by copying each course syllabus from `../../semesters/` and converting its week numbers |
| `make_docs.py` | Writes `../docs/handbook.md` and `../docs/curriculum-map.md` from the main ones, changing only the calendar, load and semester plan |
| `make_s1_timetable.py` | Writes the Semester 1 class timetable |
| `build_booklet.py`, `make_booklet.sh` | Build `../Physics-Programme-Booklet-8-semester.pdf` from the main booklet generator (needs `pdflatex`) |

To regenerate everything after the main syllabi change:

```sh
cd 8-semester-version/tools
python3 make_semesters.py && python3 make_docs.py && python3 make_s1_timetable.py && ./make_booklet.sh
```
