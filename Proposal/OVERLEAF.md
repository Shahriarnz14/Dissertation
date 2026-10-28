# Standalone dissertation sources

Upload the ZIP as **New project → Upload project**. `main.tex` and `latexmkrc`
must be at the project root; do not upload the outer dissertation repository.

In **Settings → Compiler**, select **pdfLaTeX**, **TeX Live 2026**, and
**main.tex** as the main document. Select **Normal** compilation mode and
**Stop on first error**, then **Recompile from scratch** once after uploading.
Overleaf runs latexmk and BibTeX automatically; do not run Biber or upload a
cached `.bbl`. `references.bib` is the unified database; the unchanged
`unsrtnat.bst` style is supplied by TeX Live's standard natbib installation.

`latexmkrc` supplies the recursive `template/` search path required by the
eight copied CMU styles. It deliberately leaves Overleaf's engine and output
directory handling intact. No shell escape, Python, original paper folders,
VS Code settings, or repository metadata is required to compile.

The original bitmap bbm font may need automatic `mktexpk` generation on a
cold TeX installation. This uses TeX Live's supplied font sources; it is not
a font file missing from the archive. Font-generation permission or version
errors should be reported using the full compiler log, without substituting
the scientific indicator glyph.

The full dissertation takes multiple LaTeX and BibTeX passes. Overleaf's
published limits (checked October 27, 2026) are 10 seconds for Free projects
and 240 seconds for Premium projects. A local measurement does not predict
the server's time or prove that a timeout caused an earlier failure.

If no PDF is produced, provide the exact error banner and **Logs and output
files → full/raw log** (including its first error and final lines), the main
document/compiler/TeX Live settings, and the project owner's plan. A timeout
banner, `File ... not found`, an engine error, and a viewer loading error
require different remedies. If compilation succeeds but preview fails,
download the PDF to check whether this is a viewer issue.

Official references:

- [Custom dependencies](https://docs.overleaf.com/managing-projects-and-files/adding-latex-dependencies)
- [Project latexmkrc](https://docs.overleaf.com/managing-projects-and-files/the-latexmkrc-file)
- [Compiler settings](https://docs.overleaf.com/getting-started/recompiling-your-project/selecting-a-tex-live-version-and-latex-compiler)
- [TeX Live 2026 availability](https://www.overleaf.com/blog/tex-live-2026-is-now-available)
- [Plan limits](https://docs.overleaf.com/getting-started/free-and-premium-plans/plan-limits)
- [Compile timeouts](https://docs.overleaf.com/troubleshooting-and-support/fixing-and-preventing-compile-timeouts)

This archive is generated from a single shared source tree by
`python3 -B Proposal/scripts/export_overleaf.py` in the original repository.
The adjacent ZIP manifest records every exported file's SHA-256 hash.
Standalone MacTeX compilation is a portability test; actual Overleaf success
must be confirmed by compiling the uploaded project on Overleaf.
