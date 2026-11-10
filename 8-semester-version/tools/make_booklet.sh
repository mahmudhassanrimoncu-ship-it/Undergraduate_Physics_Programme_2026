#!/bin/sh
# Rebuild the 8-semester comparison booklet: 8-semester-version/Physics-Programme-Booklet-8-semester.pdf
set -e
cd "$(dirname "$0")"
python3 build_booklet.py
pdflatex -interaction=nonstopmode -halt-on-error booklet-8.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error booklet-8.tex > /dev/null
cp booklet-8.pdf ../Physics-Programme-Booklet-8-semester.pdf
echo "Built 8-semester-version/Physics-Programme-Booklet-8-semester.pdf"
