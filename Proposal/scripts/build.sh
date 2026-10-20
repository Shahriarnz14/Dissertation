#!/bin/sh
set -eu
proposal_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$proposal_dir"
python3 -B scripts/verify_sources.py
case "${1-}" in
  "")
    test "$#" -eq 0
    /Library/TeX/texbin/latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
    ;;
  --clean)
    test "$#" -eq 1
    /Library/TeX/texbin/latexmk -gg -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
    ;;
  *)
    echo 'Usage: sh scripts/build.sh [--clean]' >&2
    exit 2
    ;;
esac
python3 -B scripts/check_build.py
