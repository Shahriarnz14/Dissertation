# Phase B validation - skeleton corrections and native editor workflow

Phase B only. Chapter 2 remains unstarted and requires explicit user authorization. Updated October 19, 2026 for the user's native LaTeX Workshop workflow request. This report supersedes the initial skeleton validation, archived at `build/toc-page-fix-before/metadata/validation-phase-b.md`, and the intervening shell-wrapper editor routing.

## Actual diagnosis

At the start of this correction, two independent PDFs existed:

- `Proposal/build/main.pdf`: the earlier converged skeleton, still showing the old metadata placeholders. Its hash matched the initial validation report.
- `Proposal/main.pdf`: the newer output showing the current author-entered metadata, an empty TOC on PDF page 3, and `Temporary page!` on page 27. This exactly reproduced the reported symptoms.

The newer root-level log showed `No file main.aux`, `No file main.toc`, root-level AUX/TOC output, `Temporary extra page added at the end. Rerun to get it removed`, and two `Illegal parameter number in definition of \tableofcontents` errors. It loaded `./cmu-thesis.sty` and `./cmu-style-files/`, which were unpatched copies matching the protected originals, rather than the documented repaired `template/` copies. The root `.toc` subsequently contained the generated entries, but the already-emitted PDF had not reread them. The root AUX absolute-page record was 26 while the faulty PDF physically contained 27 pages.

The mechanism was therefore an unconverged one-pass build, combined with duplicate template/output paths. The evidence does not identify which editor button initiated the earlier run. The workflow inspection now establishes the configuration cause: there was no repository-root `.vscode/settings.json`, so the root-folder window did not load nested Proposal settings. The existing global settings put a single-pass `pdfLaTeX` recipe first; its tool has no `-outdir` argument. This exactly matches the root-level log and bypasses `.latexmkrc`. Global settings were inspected read-only. Seven earlier duplicate artifacts were preserved under `build/legacy-single-pass/`, with hashes in `metadata/phase-b-correction-before.json`. Seven more root outputs observed during the workflow change were archived in the same directory with `workflow-2026-10-19-` prefixes; see `metadata/latex-workshop-archived-outputs.json`. The extra root-level template copies were left unchanged.

## CMU mechanism and fix

The supplied template uses `article` with custom structural commands:

- `\chapter` automatically advances its chapter counter and writes TOC entries using the template's `section` type. Treating only standard `chapter` records as chapters would miss them.
- `\part` writes `part` entries and `\appendix{Title}` writes `appendix` entries.
- `\tableofcontents` reads generated `main.toc` through `\@starttoc{toc}`. The entries written through AUX state are available for later passes, and TOC growth can change physical page totals.
- PDF management/tagging leaves last-page work in LaTeX's `shipout/lastpage` mechanism. The kernel writes the absolute-page total to AUX. With no usable prior total, pending last-page data may produce a temporary page; subsequent passes must stabilize the total and hook execution.

No TOC entries or page numbers were hardcoded. The custom CMU TOC commands, TOC depth, page counters, last-page hooks, and diagnostics were not disabled or rewritten for this correction.

The repository-root `.vscode/settings.json` now supplies one standard direct `/Library/TeX/texbin/latexmk` recipe. It builds on save, uses the built-in PDF viewer, and enables SyncTeX. Its cwd is `%WORKSPACE_FOLDER%/Proposal`, its input is `main.tex`, and its output argument is `-outdir=build`. The viewer's `%DIR%/build` is relative to the discovered dissertation root. Component root comments remain intact, fallback discovery searches only `Proposal/main.tex`, and protected-tree saves are excluded. The main file has no program/options magic override. The obsolete nested settings file was removed; the optional workspace now opens the repository root.

The optional `build.sh` still performs provenance/post-build checks, but the editor does not invoke it. Both use the same latexmk arguments, `.latexmkrc`, absolute MacTeX pdfLaTeX/BibTeX engines, and output directory. `.latexmkrc` searches `template/` first; the checker independently requires the actual recorder inputs to be those eight copies and all outputs to be under `build/`. Existing template compatibility fixes are persistent in the copied styles and `macros/template-compat.tex`, which were not changed during workflow simplification. Neither build method applies temporary source patches.

## Clean build evidence

The configured native LaTeX Workshop command was read from the new settings and executed directly from `Proposal/`, adding only `-gg` for the required clean rebuild:

```bash
/Library/TeX/texbin/latexmk -gg -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

The normal editor/CLI command, without a forced clean, is:

```bash
/Library/TeX/texbin/latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

Exit status: **0**. Latexmk performed **three pdfLaTeX passes**. The final pass has no unresolved rerun, temporary-page, wrong-last-page-hook, undefined reference/citation, duplicate-label, box, PDF-string, color-stack, or TeX-error diagnostic. The full clean transcript is `build/latex-workshop-clean.log`; its first-pass missing-TOC/AUX/rerun messages are intermediate and resolve in later passes. The converged compiler pass is `build/main.log`.

The exact normal native recipe was also executed after the clean build and reported the target up to date without changing the PDF hash (`build/latex-workshop-incremental.log`). The optional CLI script then used the same native flags, reported up to date, and passed all 119 consistency checks. All 322 skeleton checks passed. Settings were checked against the installed LaTeX Workshop 10.20.0 schema and root/recipe/placeholder implementation. SyncTeX forward lookup from Chapter 1's placeholder line 2 returns PDF page 7; reverse lookup at that location returns the same source file and line. `main.pdf` and `main.synctex.gz` both exist under `build/`.

The pinned tool input/cwd do not depend on the active document, so this recipe cannot compile a protected original. The installed extension's actual micromatch implementation confirms that protected-tree saves are ignored while Proposal chapter, appendix, and frontmatter saves are enabled. Fallback search has one candidate, and every Proposal component root comment resolves to it. No protected source currently contains a program/recipe magic override. LaTeX Workshop can still recognize a deliberately opened standalone paper as an active document; root-search filters do not disable that behavior. The pinned recipe still compiles only the dissertation. Use Proposal files for dissertation viewing and SyncTeX.

The graphical VS Code build, viewer-refresh, and navigation commands were not directly exercised. Manual verification: open/reload the repository-root folder, save a Proposal component, invoke normal Build and View PDF, then use SyncTeX from cursor and Command-click back to source. Confirm the build output shows the configured latexmk recipe and `build/main.pdf`. Evidence: `metadata/latex-workshop-validation.json`.

## Current PDF and substantive verification

Canonical PDF: `Proposal/build/main.pdf`.

SHA-256: `09d93797e90dcf5ba77aae49e3e3b193b9855b60023ec0a7fa8c105a4246b86d`.

The PDF has **27 physical US Letter pages**. Its last page is the genuine bibliography placeholder, numbered Arabic **21**. LaTeX's absolute-page record is also **27**. No PDF page contains the temporary-page notice. The total remains 27 because the populated TOC occupies an additional page while the temporary page disappears; total page count alone would not detect either fault.

The actual rendered TOC occupies PDF pages **3-4**. All **3 Parts, 10 chapters, and 7 appendices** were checked against the generated TOC record, AUX label, PDF destination, and visible destination-page footer. Additional automatically generated section entries are allowed by the checker, so subsequent migration can extend the TOC without manual entry lists. Exact reconciliation follows.

| Entry | Printed page | Physical PDF page |
|---|---|---|
| Chapter 1: Introduction | 1 | 7 |
| Part I Learning from Structured Longitudinal Clinical Trajectories | 2 | 8 |
| Chapter 2: Temporal Representation Learning | 3 | 9 |
| Part II Causal Inference from Longitudinal Clinical Data | 4 | 10 |
| Chapter 3: Medication Adherence and Causal Modeling of Longitudinal Clinical Outcomes | 5 | 11 |
| Chapter 4: Heterogeneous Treatment Effects under Censoring: SurvHTE | 6 | 12 |
| Part III Recovering and Reasoning over Clinical Trajectories from Text | 7 | 13 |
| Chapter 5: The Textual Time Series Framework / PMOA-TTS | 8 | 14 |
| Chapter 6: Reconstructing Sepsis Trajectories from Clinical Text | 9 | 15 |
| Chapter 7: Forecasting Clinical Risk from Textual Time Series | 10 | 16 |
| Chapter 8: Aligning Textual Trajectories with Structured EHR Data | 11 | 17 |
| Chapter 9: Verification and Decision-Making from Textual Sepsis Trajectories | 12 | 18 |
| Chapter 10: Discussion and Conclusion | 13 | 19 |
| Appendix A Temporal-SCL | 14 | 20 |
| Appendix B Medication Non-adherence | 15 | 21 |
| Appendix C SurvHTE-Bench | 16 | 22 |
| Appendix D PMOA-TTS | 17 | 23 |
| Appendix E T2S2 CHIL | 18 | 24 |
| Appendix F T2S2 AAAI | 19 | 25 |
| Appendix G Textual--Tabular Alignment | 20 | 26 |

Front-matter Roman footers and named PDF page labels agree on every page: abstract i, TOC ii-iii, figure list iv, table list v. Chapter 1 begins at Arabic 1 on PDF page 7. Arabic numbering continues without a reset through the appendix and bibliography pages.

## Stronger validation and regression evidence

`validate_skeleton.py` now passes **322 checks, zero errors**, including **119** shared build-consistency checks. Unlike the earlier checks, these verify the actual rendered TOC and current metadata, absolute-page convergence, source freshness, runtime template paths, and absence of a temporary page. Results are in `metadata/skeleton-checks.json` and `metadata/toc-page-verification.json`.

A negative check applied the stronger checker to the preserved faulty PDF, its populated `.toc`, and its AUX/log state. It correctly rejected missing rendered TOC entries, the temporary-page notice, the incorrect absolute-page total, and the unresolved TeX/rerun diagnostics, despite the same physical count of 27 pages. This evidence is in `metadata/phase-b-negative-check.json`.

All 27 current pages were rendered and visually inspected through five contact sheets. PDF pages **1, 3, 4, 7, and 27** were inspected individually; all appendix pages **20-26** were inspected through the rendered sheets. No clipping, overlap, missing TOC entries, unintended blank pages, or extraneous final page was found. Poppler word-bounds checks also found no words outside a physical page. Render hashes and inspection evidence are in `metadata/pdf-review-phase-b.json`; PNGs are in `build/pdf-review/`.

## Metadata and protected boundaries

`frontmatter/metadata.tex` was **not modified**. Its pre-fix and post-fix SHA-256 is `ca4b70250443c7f6f3b871ca12222e77aa3280968df737f4708ca571491047f5`. The current displayed values remain:

- Title: Representation and Reasoning over Longitudinal Clinical Trajectories from Structured Data and Text
- Date: Nov 6, 2026
- Copyright year: 2026

They remain independently editable through `\ProposalTitle`, `\ProposalSubmissionDate`, and `\ProposalCopyrightYear`. The canonical PDF now reflects these existing author-entered source values instead of the older build's placeholders. Validation reads the current macros; it does not reset them to fixed values.

All **587 protected files and their directory inventory remain unchanged**. Six registered template copies remain byte-identical to their originals; the same two documented compatibility copies remain unchanged from before this correction. No scientific content, paper bibliography, chapter/appendix placeholder, committee order, or required degree statement was altered. No paper migration, network fetch, staging, commit, or push occurred.

## Remaining diagnostics and limits

Exactly two expected CMU advisories remain visible:

1. `There are no tables or figures..` The empty lists are expected.
2. `It is recommended that you include the 'acknowledgments' section (environment).` No acknowledgment text was supplied.

No dummy figures, tables, references, acknowledgments, or scientific prose were added. BibTeX remains configured but is not invoked until genuine citations are migrated. Scientific equivalence and scientific typography are outside this skeleton correction. Accessibility conformance is not certified.

## Files and next approval gate

Workflow-specific modified/added/deleted files: `metadata/latex-workshop-files.txt`; reversible duplicate-output moves: `metadata/latex-workshop-archived-outputs.json`. Earlier correction files remain in `metadata/phase-b-correction-files.txt`. The original Phase B creation inventory remains in `metadata/changed-files.txt`; current ignored generated artifacts are listed in `metadata/build-artifacts.txt`. Build decisions and progress were updated in the README, source manifest, transformation log, and progress record.

**Stop here. Await explicit authorization before Chapter 2.**
