# Local output/flags; shared dependency paths also work on Overleaf.
# Run latexmk from Proposal/. Overleaf exports omit this local adapter.
require './latexmkrc';
$pdf_mode = 1;
$out_dir = 'build';
$aux_dir = 'build';
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 -recorder %O %S';
$bibtex = 'bibtex %O %B';
