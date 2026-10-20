# Phase B validation - ready for review

Date: October 19, 2026. Phase B only; no scientific manuscript migration has begun. Chapter 2 remains subject to explicit user approval.

## Result

The complete skeleton builds successfully to `Proposal/build/main.pdf` (27 US Letter pages, PDF 2.0). The current compiler log has no compilation errors, undefined references/citations, duplicate labels, overfull/underfull boxes, PDF-string warnings, or color-stack warnings. Exactly two expected CMU advisories remain, listed below; they are not suppressed.

PDF SHA-256: `d2eb9daa7c42bed7c61b1b47b5450ea6ff88c5b939949960925b04e29e529a48`.

## Actual compilation evidence

Working directory: `Proposal/`. Existing installation: TeX Live 2026; pdfTeX 1.40.29; latexmk 4.88; BibTeX 0.99e is configured.

The normal command used successfully was:

```bash
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

A final clean rebuild used the same command with `-gg`; exit status **0**. Full stdout/stderr is retained in `build/latexmk-final.log`, with the converged final compiler pass in `build/main.log`. First-pass missing AUX/list/TOC files and rerun requests in the clean-build transcript resolve during latexmk's subsequent passes; they are not unresolved final diagnostics. Exact command/working-directory evidence is in `metadata/build-phase-b.json`.

The repository-root wrapper `sh Proposal/scripts/build.sh` also exited **0**, including its protected-source/provenance guard (`build/build-script-final.log`). The actual expanded LaTeX Workshop recipe exited **0** (`build/latex-workshop-recipe.log`).

BibTeX was intentionally not invoked: the skeleton has no citations or bibliography entries. Numeric natbib/unsrtnat and the installed BibTeX executable are configured; bibliography rendering must be checked with genuine citations during the approved Chapter 2 migration. No dummy entry was used for testing.

## Structural and programmatic checks

`python3 -B Proposal/scripts/validate_skeleton.py` passed **203 checks, zero errors**. Full check descriptions are retained in `metadata/skeleton-checks.json` (also `build/validation-skeleton.json`). These include:

- Approved order of ten chapters, three Parts, and seven existing-supplement appendix modules; independent CHIL/AAAI Chapters 6 and 7.
- Actual compiled labels automatically produce Chapters 1-10, Parts I-III, and Appendices A-G. Every chapter/appendix target resolves to the PDF page containing its heading; no manual chapter/appendix counter assignments appear in authored TeX.
- Exact title-page degree statement, confirmed author, committee order, and editable dissertation-title placeholder.
- Component root directives resolve to `Proposal/main.tex`, with no main-file magic-root loop or direct-engine override.
- All explicit authored input targets exist. The build recorder does not read papers, pre-existing chapters, or the original template tree.
- Lists of figures/tables are truly empty; `references.bib` has no entries, and no fabricated BBL exists.
- All 587 protected files and their directory inventory match the pre-copy/build snapshot. Six copied styles are byte-identical; the other two match the documented technical adaptation hashes/diff.
- No unexpected warnings or actionable compiler diagnostics remain in the converged log.

`git check-ignore` confirmed that the PDF, AUX, and review PNGs are ignored. No Git commit, staging, push, or external fetch was performed. `AGENTS.md` and `CODEX_PROMPTS.md` were already untracked at the start; neither was modified. The only modified pre-existing project document is the explicitly authorized `DISSERTATION_PLAN.md`.

## PDF inspection

All 27 pages were rendered with Poppler and visually inspected through five contact sheets. PDF pages **1, 3, and 11** were also inspected individually for title-page wording/layout, the wrapped table of contents, and the longest chapter heading. No clipping, overlapping text, missing headings, or unintended blank pages were found. Large empty areas on chapter/supplement pages are intentional skeleton layout.

The final clean-build PDF was re-rendered; all 27 PNGs are byte-identical to the reviewed renders. An independent Poppler word-bounds check found no words outside a PDF page (1269 words checked). PDF destinations were inspected and checked against AUX labels. Render hashes and inspection evidence are in `metadata/pdf-review-phase-b.json`; review files are under `build/pdf-review/`.

| PDF pages | Content and numbering |
|---|---|
| 1 | Unnumbered title page |
| 2 | Abstract placeholder; Roman i |
| 3-4 | Contents; Roman ii-iii |
| 5-6 | Empty figure/table lists; Roman iv-v |
| 7-19 | Chapters 1-10 and the three Part dividers; Arabic 1-13 |
| 20-26 | Existing-paper supplement placeholders; automatic Appendices A-G, Arabic 14-20 |
| 27 | Single bibliography placeholder; Arabic 21 |

## Remaining diagnostics and limits

1. `LaTeX Warning: There are no tables or figures..` Expected in a skeleton with no scientific floats.
2. `LaTeX Warning: It is recommended that you include the 'acknowledgments' section (environment).` The section is optional and no acknowledgment text was supplied.

Both messages remain visible in the compiler log. No artificial figures, tables, bibliography entries, acknowledgment text, or transitions were added to silence diagnostics.

This validates architecture and placeholder rendering only. No scientific equivalence, reference-PDF agreement, per-paper typography, scientific float/equation numbering, or scientific bibliography rendering is claimed. Tagpdf/PDF management is retained, but `pdfinfo` reports `Tagged: no`; accessibility conformance has not been certified.

VS Code settings were checked against the installed LaTeX Workshop 10.20.0 schema and root/recipe implementation. The expanded recipe was executed successfully; an interactive editor build-button session was not exercised. Open the supplied workspace or `Proposal/` folder to load the local settings.

## Files and decisions

- Exact modified/added source/configuration/documentation inventory: `metadata/changed-files.txt`.
- Separate generated/ignored artifact inventory: `metadata/build-artifacts.txt`.
- Original-to-copy provenance and technical decisions: `source-manifest.md`, `template-copies.json`, `template-compatibility.patch`, and `transformation-log.md`.
- Persistent source choices are recorded in the root plan and both source-manifest formats; they do not authorize migration.
- No blocking decision remains for this skeleton. Dissertation title, submission date, copyright year, and optional college/department display remain editable metadata.

**Stop here. Await the user's explicit approval before Chapter 2.**
