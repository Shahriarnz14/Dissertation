# Run from Proposal/; scripts/build.sh also works from another directory.
$pdf_mode = 1;
$out_dir = 'build';
$aux_dir = 'build';
$max_repeat = 8;
$pdflatex = '/Library/TeX/texbin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -synctex=1 -recorder %O %S';
$bibtex = '/Library/TeX/texbin/bibtex %O %B';
# Resolve the copied template without changing its internal style paths.
$ENV{'TEXINPUTS'} = './template//:' . ($ENV{'TEXINPUTS'} // '');
$ENV{'BIBINPUTS'} = '.:' . ($ENV{'BIBINPUTS'} // '');
