# CMU dissertation proposal

Phase B creates a compilable skeleton only. All ten chapters, the dissertation abstract, seven existing-paper appendix modules, and the bibliography are explicitly marked placeholders. No paper prose, mathematics, abstracts, figures, table data, supplementary content, or bibliography entries have been migrated. Chapter 2 requires the user's next explicit approval.

The authoritative project rules and dissertation map remain in the parent directory: `../AGENTS.md`, `../DISSERTATION_PLAN.md`, and `../CODEX_PROMPTS.md`. The protected `../Papers/`, pre-existing `../Chapters/`, and `../CMU-PhD-Template/` trees must never be modified or built in place.

## Build with the existing MacTeX installation

From the repository root:

```bash
sh Proposal/scripts/build.sh
```

The script verifies the protected source snapshot and copied-template provenance, changes into `Proposal/`, and executes:

```bash
/Library/TeX/texbin/latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

The PDF is `Proposal/build/main.pdf` relative to the repository root. Compiler logs, AUX files, SyncTeX, recorder files, and review renders remain under `Proposal/build/`, which is ignored by Git. `.latexmkrc` uses `/Library/TeX/texbin/pdflatex` and `/Library/TeX/texbin/bibtex`; numeric `natbib` uses the CMU template's `unsrtnat` style. Biber is not used.

For a forced clean rebuild, run the same latexmk command from `Proposal/` with `-gg` added. This cleans/rebuilds generated compilation outputs only. Do not run cleanup commands in any protected source tree.

## VS Code / LaTeX Workshop

Open `Dissertation-Proposal.code-workspace` in VS Code, or open `Proposal/` as the folder. This loads the local `.vscode/settings.json`; it does not change global preferences or settings for the original papers. The installed LaTeX Workshop extension can build using **CMU proposal (MacTeX pdfLaTeX + BibTeX)** and view `build/main.pdf` with SyncTeX.

Every component `.tex` file has a relative `% !TeX root = .../main.tex` directive. The main file declares `article` and has no self-referencing root directive or `TeX program` override. This matters because the installed extension prioritizes a `TeX program` magic comment over its configured latexmk recipe. Root discovery is restricted to `main.tex` in this workspace. When the enclosing repository is open instead, component magic comments still identify the dissertation root; open the provided workspace to activate the supplied build recipe and output-directory settings.

Configuration and root resolution were checked against the installed LaTeX Workshop 10.20.0 schema/source. The expanded recipe is tested as a command; no claim is made that an interactive VS Code build button was exercised.

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

Edit `frontmatter/metadata.tex` for the dissertation title, submission date, copyright year, and optional college/department display. The author and four committee members are explicitly confirmed; the degree statement matches the plan verbatim. `[Dissertation Title]`, `[Submission date]`, and `[Year]` remain intentional editable placeholders.

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
python3 -B Proposal/scripts/validate_skeleton.py
python3 -B Proposal/scripts/render_pdf.py
```

The first two scripts use Python's standard library; skeleton verification also uses Poppler's `pdfinfo` and `pdftotext`. PDF rendering uses `pdftoppm` and the already installed Pillow package for contact sheets. Every render is kept in `build/pdf-review/`.

`validate_skeleton.py` is intentionally a Phase B acceptance check. Update it deliberately as scientific migrations replace placeholders; it does not certify scientific content. It verifies the actual PDF, numeric labels and PDF destinations, required title-page wording, empty float lists and bibliography, component root directives, input order, protected boundaries, and compiler diagnostics. Complete results are in `metadata/validation-phase-b.md`.

Two expected CMU advisories remain visible: there are no figures/tables, and an acknowledgments section is recommended. No acknowledgment text was supplied, and no artificial content was added to silence either message. The sparse pages are intentional placeholders. Tagpdf/PDF management support from the template is retained; the skeleton is not certified as an accessible/tagged PDF. Scientific typography, bibliography rendering, algorithms, and paper-specific package compatibility must be validated during each approved migration.
