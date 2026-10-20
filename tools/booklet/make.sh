#!/bin/sh
# Rebuild the printable booklet: docs/Physics-Programme-Booklet.pdf
set -e
cd "$(dirname "$0")"
python3 build.py
pdflatex -interaction=nonstopmode -halt-on-error booklet.tex > /dev/null
pdflatex -interaction=nonstopmode -halt-on-error booklet.tex > /dev/null
cp booklet.pdf ../../docs/Physics-Programme-Booklet.pdf
echo "Built docs/Physics-Programme-Booklet.pdf"
