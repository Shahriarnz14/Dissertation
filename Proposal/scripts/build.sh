#!/bin/sh
set -eu
proposal_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$proposal_dir"
python3 -B scripts/verify_sources.py
exec /Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
