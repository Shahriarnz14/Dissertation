# CMU dissertation proposal

Phase B creates a compilable skeleton only. All ten chapters, the dissertation abstract, seven existing-paper appendix modules, and the bibliography are explicitly marked placeholders. No paper prose, mathematics, abstracts, figures, table data, supplementary content, or bibliography entries have been migrated. Chapter 2 requires the user's next explicit approval.

The authoritative project rules and dissertation map remain in the parent directory: `../AGENTS.md`, `../DISSERTATION_PLAN.md`, and `../CODEX_PROMPTS.md`. The protected `../Papers/`, pre-existing `../Chapters/`, and `../CMU-PhD-Template/` trees must never be modified or built in place.

## Build with the existing MacTeX installation

From the repository root:

```bash
sh Proposal/scripts/build.sh
```

This optional script verifies the protected source snapshot and copied-template provenance, changes into `Proposal/`, runs latexmk to convergence, and then checks the actual rendered TOC, last-page record, metadata, input paths, and pagination. LaTeX Workshop invokes latexmk directly; the script is not needed during editing. Both use this command from `Proposal/`:

```bash
/Library/TeX/texbin/latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

The PDF is `Proposal/build/main.pdf` relative to the repository root. Compiler logs, AUX files, SyncTeX, recorder files, and review renders remain under `Proposal/build/`, which is ignored by Git. `.latexmkrc` uses `/Library/TeX/texbin/pdflatex` and `/Library/TeX/texbin/bibtex`; numeric `natbib` uses the CMU template's `unsrtnat` style. Biber is not used.

For a clean, complete rebuild from the repository root, use:

```bash
sh Proposal/scripts/build.sh --clean
```

This adds `-gg` to latexmk and rebuilds generated compilation outputs. Latexmk determines the required passes; the verified Phase B clean rebuild required three pdfLaTeX passes. The first pass writes the CMU TOC records and absolute-page data, later passes read them and stabilize pagination. An intermediate PDF may have an empty TOC or a temporary final page, so review the converged `build/main.pdf`. Do not run cleanup commands in any protected source tree.

## VS Code / LaTeX Workshop

Open the existing **repository root `Dissertation-Proposal/`** in VS Code. Its `.vscode/settings.json` supplies the single default **latexmk (CMU dissertation)** recipe. Open `Proposal/main.tex` or a component file, edit, and save: LaTeX Workshop automatically runs `/Library/TeX/texbin/latexmk` and refreshes its built-in PDF viewer. The normal **Build LaTeX project** and **View LaTeX PDF file** commands use `Proposal/build/main.pdf`. No shell script or separate workspace is required. If the window was already open while these settings changed, run **Developer: Reload Window** once and close any old `Proposal/main.pdf` tab.

Every component `.tex` file has a relative `% !TeX root = .../main.tex` directive. The main file declares `article` and has no self-referencing root or program/options magic override. Workspace fallback searches only `Proposal/main.tex`. The standard latexmk tool has its working directory pinned to `%WORKSPACE_FOLDER%/Proposal`, its input pinned to `main.tex`, and `-outdir=build`; this prevents the recipe from compiling an original paper if another standalone document is active. The viewer setting `%DIR%/build` resolves relative to the discovered dissertation root. Save-triggered builds ignore the three protected trees; `Proposal/Chapters/` remains enabled. The ignore pattern for the original root `Chapters/` uses the repository folder name to distinguish these two directories.

The optional `Proposal/Dissertation-Proposal.code-workspace` now opens the same repository root. The obsolete nested `Proposal/.vscode/settings.json` was removed so there is one editor configuration. Opening `Proposal/` alone is no longer the documented workflow. Global VS Code settings and protected files were not changed.

SyncTeX is enabled in latexmk and uses `/Library/TeX/texbin/synctex`. Use **SyncTeX from cursor** for source-to-PDF navigation and Command-click in the built-in PDF viewer for PDF-to-source navigation. `main.synctex.gz` is alongside `main.pdf` in `build/`. The built-in viewer watches that PDF and refreshes it after a successful build.

Configuration and root resolution were checked against installed LaTeX Workshop 10.20.0 source/schema. The exact configured native tool passed a clean three-pass build and an incremental build; forward/reverse SyncTeX passed command-line checks. The graphical VS Code commands and refresh were not directly exercised. For a short manual check: reload the root-folder window, save a Proposal component, use Build and View PDF, then try SyncTeX from cursor and Command-click back to source. See `metadata/latex-workshop-validation.json` and `metadata/validation-phase-b.md` for evidence and limits.

The earlier mismatch had two configuration causes: the repository-root window did not load nested `Proposal/.vscode/settings.json`, and the existing global recipe list put single-pass pdfLaTeX first with no output-directory argument. That route wrote `Proposal/main.pdf`, bypassed `.latexmkrc`, and selected unpatched shadow template copies. The root workspace recipe now overrides that global list and uses `.latexmkrc` for the repaired template search path and all required reruns. Compatibility repairs remain in the copied template and `macros/template-compat.tex`; no script patches source files at build time. Duplicate generated root outputs were archived under `build/legacy-single-pass/`, with hashes in `metadata/latex-workshop-archived-outputs.json`. Historical PDFs there are evidence only; `build/main.pdf` is the sole live output.

## Architecture

```text
main.tex                         # Preamble and ordered input directives
template/                        # Eight copied CMU styles; original tree untouched
macros/                          # Packages, shared commands, theorem reservation, compatibility
frontmatter/                     # Editable metadata, title page, abstract, contents/lists
Parts/                           # Three automatic Part divisions
Chapters/chapter-01 ... -10/      # chapter.tex + sections/images/figures/tables
Appendices/appendix-ch02 ... 08/  # Existing supplements only; same modular layout
backmatter/bibliography.tex       # One unified bibliography or its Phase B placeholder
references.bib                   # Empty until an approved migration
scripts/                         # Build, preservation checks, skeleton checks, PDF rendering
metadata/                        # Decisions, manifests, hashes, logs, validation, progress
build/                           # All generated build and PDF-review artifacts
```

Part I precedes Chapter 2, Part II precedes Chapter 3, and Part III precedes Chapter 5. CHIL and AAAI sepsis papers remain separate Chapters 6 and 7. The existing supplements follow Chapter 10 in paper order, with the single bibliography afterward. The template assigns chapter numbers, Part numerals, appendix letters, and later scientific float/equation numbers automatically.

Each chapter and appendix entry point explicitly inputs its placeholder section module. Empty `images/`, `figures/`, and `tables/` directories are retained with `.gitkeep`; they contain no fabricated assets. A future migration must use explicit inputs for section, figure, and table modules.

The actual CMU template uses `article` with custom chapter/appendix commands. Its geometry, spacing, title-page arrangement, caption conventions, and pagination are retained. Six copied styles are byte-identical; two have minimal documented repairs. Further compatibility adaptations live in `macros/template-compat.tex`, with patch failures treated as compilation errors. No global sanity-check or warning suppression is used. See `metadata/transformation-log.md` and `metadata/template-compatibility.patch`.

## Editable metadata and bibliography activation

Edit `frontmatter/metadata.tex` for the dissertation title, submission date, copyright year, and optional college/department display. The three independent macros are `\ProposalTitle`, `\ProposalSubmissionDate`, and `\ProposalCopyrightYear`. Their current author-entered values were preserved byte-for-byte during the TOC/page-count correction. The author and four committee members are explicitly confirmed; the degree statement matches the plan verbatim. Validation compares the PDF with the current macro values, so it does not require or restore earlier placeholder values.

`references.bib` contains comments only. `\ProposalBibliographyReadyfalse` in `macros/commands.tex` displays the template's bibliography heading and a marked placeholder without invoking BibTeX on an empty database. During the approved Chapter 2 migration, populate the unified database from the selected bibliography and change this flag to `\ProposalBibliographyReadytrue`. Record all citation-key changes. Never add dummy entries merely to exercise BibTeX.

## Persistent source decisions

- Chapter 2: `../Papers/Part-i/Temporal-SCL-ML4H2023/noroozizadeh23.tex`.
- Chapter 5: `../Papers/Part-iii/PMOA-TTS-ScientificData2027/Scientific_data/main_pmoa_tts_V4.tex` (the user's V4 selection).
- Chapter 7: `../Papers/Part-iii/T2S2-Forecasting-AAAI2026/CameraReady/LaTeX/main_with_appendix.tex`.

Use only the actual active dependencies of these roots. In particular, do not replace the Scientific Data table copies with root-level alternatives or combine the AAAI camera-ready paper with its arXiv/submission versions. Exact selections, source hashes, appendix dependencies, and prospective destination maps are in `metadata/source-manifest.md` and `metadata/source-selections.json`.

## Verification and current limits

From the repository root:

```bash
python3 -B Proposal/scripts/verify_sources.py
python3 -B Proposal/scripts/check_build.py
python3 -B Proposal/scripts/validate_skeleton.py
python3 -B Proposal/scripts/render_pdf.py
```

Preservation/build/skeleton checks use Python's standard library; PDF checks also use Poppler's `pdfinfo` and `pdftotext`. PDF rendering uses `pdftoppm` and the already installed Pillow package for contact sheets. Every render is kept in `build/pdf-review/`.

`validate_skeleton.py` is intentionally a Phase B acceptance check. Update it deliberately as scientific migrations replace placeholders; it does not certify scientific content. It includes `check_build.py`, which reconciles rendered TOC titles/page numbers with automatic AUX/TOC records and actual PDF destinations, checks the absolute last-page total, rejects temporary-page/rerun diagnostics, verifies Roman/Arabic footers, and compares current metadata. Additional automatically generated section entries are allowed. The checks do not write document entries, set page numbers, or disable last-page hooks. Complete results are in `metadata/validation-phase-b.md`.

Two expected CMU advisories remain visible: there are no figures/tables, and an acknowledgments section is recommended. No acknowledgment text was supplied, and no artificial content was added to silence either message. The sparse pages are intentional placeholders. Tagpdf/PDF management support from the template is retained; the skeleton is not certified as an accessible/tagged PDF. Scientific typography, bibliography rendering, algorithms, and paper-specific package compatibility must be validated during each approved migration.
