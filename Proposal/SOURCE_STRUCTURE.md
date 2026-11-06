# Dissertation source structure

The numbered directories follow the finalized dissertation: Chapters 1–9 and Appendices A–F. `main.tex` is the sole build entry point. Displayed numbering comes from LaTeX, not directory names, module filename prefixes, or internal label names.

## Chapters and appendices

| Displayed chapter | Source directory | Associated appendix |
|---|---|---|
| 1 — Introduction | `Chapters/chapter-01/` | None |
| 2 — Temporal-SCL | `Chapters/chapter-02/` | A: `Appendices/appendix-ch02/` |
| 3 — Medication non-adherence | `Chapters/chapter-03/` | B: `Appendices/appendix-ch03/` |
| 4 — SurvHTE-Bench | `Chapters/chapter-04/` | C: `Appendices/appendix-ch04/` |
| 5 — Constructing and Validating Textual Clinical Trajectories | `Chapters/chapter-05/` | D: `Appendices/appendix-ch05/` |
| 6 — Forecasting | `Chapters/chapter-06/` | E: `Appendices/appendix-ch06/` |
| 7 — Multimodal alignment | `Chapters/chapter-07/` | F: `Appendices/appendix-ch07/` |
| 8 — Verification and Decision-Making from Textual Sepsis Trajectories | `Chapters/chapter-08/` | None |
| 9 — Discussion and Conclusion | `Chapters/chapter-09/` | None |

Table descriptions abbreviate some research titles; the wrappers contain the unchanged full displayed titles. Chapters 1, 8 and 9 remain placeholders. The abstract, acknowledgments and title-page assembly are in `main.tex`; Part dividers are in `Parts/`.

Each chapter has one active `chapter.tex`; each appendix has one active `appendix.tex`. Their explicit inputs control compilation order. Subdirectories contain section modules, LaTeX figure/table compositions, original image assets and algorithms where applicable. Preserve the explicit input order; numerical filename prefixes are not a sorting instruction.

## Merged Chapter 5 and Appendix D

The top-level `sections/`, `figures/`, `tables/` and `images/` under `chapter-05/` contain the general PMOA-TTS and shared reconstruction material. `chapter-05/sepsis/` holds the former standalone sepsis chapter's modules, with the same descriptive filenames and corresponding subdirectories. `chapter-05/chapter.tex` assembles both scopes.

Appendix D uses the same arrangement: shared/general material under `appendix-ch05/` and sepsis modules under `appendix-ch05/sepsis/`. The merged appendix wrapper remains `appendix-ch05/appendix.tex`.

Physical ownership follows the active rendering. The schema, demographics, matching-threshold and prompt-ablation figure modules are in Appendix D. `clinician-annotation-review.tex` is in the chapter's sepsis tables; `model-annotator-comparison.tex` is in the appendix's sepsis tables. These locations do not change their order or displayed numbering.

## Stable internal namespaces

Historical identifiers intentionally remain unchanged. They are stable reference and formatting interfaces, not displayed chapter numbers.

| Current material | Internal labels and formatting |
|---|---|
| Chapters 2–4 / Appendices A–C | Existing `ch02`, `ch03`, `ch04` namespaces |
| Merged Chapter 5 / Appendix D | Both `ch05` and `ch06`; `ChFive…` and `ChSix…` macros |
| Forecasting Chapter 6 / Appendix E | `ch07`; `ChSeven…` macros |
| Alignment Chapter 7 / Appendix F | `ch08`; `ChEight…` macros |
| Planned Chapter 8 | `chap:ch09` |
| Conclusion Chapter 9 | `chap:ch10` |

Merged Chapter 5 retains both `chap:ch05` and `chap:ch06` aliases. Appendix D retains both `app:ch05` and `app:ch06`. Preserve macro loading and initialization order, nested groups, and float barriers. The existing `macros/ch05.tex` through `macros/ch08.tex` filenames also remain stable.

## Active and inactive sources

Presence on disk does not imply inclusion in the dissertation. Inactive abstracts, acknowledgments, historical scientific modules, figure assets, algorithms and duplicate supplementary tables are retained in their topic directories. Do not reactivate, remove or deduplicate them as routine cleanup.

Two inactive standalone wrappers are preserved in `archive/legacy-wrappers/`:

- `sepsis-chapter.tex`: former separate sepsis chapter assembly.
- `sepsis-appendix.tex`: former separate sepsis appendix assembly.

Neither is included from `main.tex`. They preserve historical assembly information and are not alternate current build roots.

The complete activity classification and original-to-current paths are in [metadata/task4-file-mapping.md](metadata/task4-file-mapping.md), with machine-readable JSON/CSV companions. [metadata/task4-active-graph-after.json](metadata/task4-active-graph-after.json) records the selected active dependency graph. Historical validation reports retain the paths that existed when those reports were written.

## Build and export

From `Proposal/`, the existing local workflow is:

```sh
latexmk -pdf -synctex=1 -interaction=nonstopmode -halt-on-error \
  -file-line-error -outdir=build main.tex
```

`latexmkrc` supplies relative template and bibliography search paths. No original-paper directory or archived wrapper is required. Both the repository and Proposal-local LaTeX Workshop configurations write to `Proposal/build/`, so opening either folder uses the same PDF and auxiliary files. Let latexmk finish all BibTeX and LaTeX passes before reviewing `build/main.pdf`; intermediate passes can have missing references and incomplete contents. A successful completed build reports that all targets are up to date.

If LaTeX Workshop still shows old warnings after a successful terminal build, open `main.tex`, run **LaTeX Workshop: Build with recipe**, and choose **latexmk (force rebuild and refresh diagnostics)**. This runs `latexmk -g` through the extension so it receives fresh compiler output and refreshes the Problems panel. The normal first recipe remains incremental. No warning filters or auxiliary-file deletion are needed.

For a standalone source export, place `main.tex`, `latexmkrc`, `references.bib`, `Chapters/`, `Appendices/`, `Parts/`, `macros/` and `template/` at the export root. Documentation may accompany them. Exclude build products, editor settings, metadata and archived standalone wrappers. Do not upload cached bibliography or auxiliary files.

`OVERLEAF.md` contains existing compiler/setup guidance but references an exporter script absent from this checkout. Task 4 did not recreate that script. Its manifest-based source ZIP and isolated local compilation evidence are under `build/task4-structure/`; an actual Overleaf server build was not performed.

The approved appearance baseline is the 281-page Task 3 PDF. Directory changes must preserve scientific content, input order, typography, numbering and navigation. The known forecasting Figure 6.2 test-count typo remains unchanged.
