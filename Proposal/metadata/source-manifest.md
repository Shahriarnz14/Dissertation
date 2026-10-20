# Source manifest - Phase B

Recorded October 19, 2026. No scientific content, artwork, tables, abstracts, or bibliography entries have been copied from the papers. Chapter and appendix destinations currently contain only marked infrastructure placeholders.

## Persistent user decisions

The user explicitly selected Chapter 2 `noroozizadeh23.tex`, Chapter 5 V4, and Chapter 7 the camera-ready root. `V4.tex` is resolved to the actual local filename `Scientific_data/main_pmoa_tts_V4.tex`. These decisions are also recorded in the root `DISSERTATION_PLAN.md` and machine-readable `source-selections.json`. Do not reopen these selections based only on filenames or timestamps.

Follow each selected root's actual active input/include graph, bibliography, graphics options, macros, conditional branch, and supplement. Never combine material from another root to fill apparent gaps. Missing or ambiguous active dependencies must be reported before that chapter is migrated.

## Paper roots and prospective destinations

All original paths below are relative to the repository root. All destinations are relative to `Proposal/`. These are provenance reservations, not completed scientific migrations.

| Chapter | Original manuscript | Bibliography | Prospective destination | Authority |
|---|---|---|---|---|
| 2 | `Papers/Part-i/Temporal-SCL-ML4H2023/noroozizadeh23.tex` | `Papers/Part-i/Temporal-SCL-ML4H2023/noroozizadeh23.bib` | `Chapters/chapter-02/`; `Appendices/appendix-ch02/` | explicit user selection, 2026-10-19 |
| 3 | `Papers/Part-ii/Impact-of-Medication-Non-adherence-CHIL2025/main.tex` | `Papers/Part-ii/Impact-of-Medication-Non-adherence-CHIL2025/references.bib` | `Chapters/chapter-03/`; `Appendices/appendix-ch03/` | sole substantive local root identified during preflight; deep audit pending |
| 4 | `Papers/Part-ii/SurvHTE-Bench-ICLR2026/main.tex` | `Papers/Part-ii/SurvHTE-Bench-ICLR2026/references.bib` | `Chapters/chapter-04/`; `Appendices/appendix-ch04/` | sole substantive local root identified during preflight; deep audit pending |
| 5 | `Papers/Part-iii/PMOA-TTS-ScientificData2027/Scientific_data/main_pmoa_tts_V4.tex` | `Papers/Part-iii/PMOA-TTS-ScientificData2027/Scientific_data/references.bib` | `Chapters/chapter-05/`; `Appendices/appendix-ch05/` | explicit user selection, 2026-10-19 |
| 6 | `Papers/Part-iii/T2S2-CHIL2026/main.tex` | `Papers/Part-iii/T2S2-CHIL2026/refs.bib` | `Chapters/chapter-06/`; `Appendices/appendix-ch06/` | sole substantive local root identified during preflight; deep audit pending |
| 7 | `Papers/Part-iii/T2S2-Forecasting-AAAI2026/CameraReady/LaTeX/main_with_appendix.tex` | `Papers/Part-iii/T2S2-Forecasting-AAAI2026/CameraReady/LaTeX/aaai2026.bib` | `Chapters/chapter-07/`; `Appendices/appendix-ch07/` | explicit user selection, 2026-10-19 |
| 8 | `Papers/Part-iii/Text-Knows-What-Tables-Know-When-PSB2027/psb_camera_ready.tex` | `Papers/Part-iii/Text-Knows-What-Tables-Know-When-PSB2027/references.bib` | `Chapters/chapter-08/`; `Appendices/appendix-ch08/` | sole substantive local root identified during preflight; deep audit pending |

## Existing appendix/supplement sources

- Chapter 2: inline appendix in the selected root after `\appendix`. `CopyOfMain.tex` is byte-identical but is not the selected entry point.
- Chapter 3: six `Sections/zz_appendix_*.tex` modules included by `main.tex`.
- Chapter 4: inline appendix in `main.tex`; `math_commands.tex` is an active macro dependency; `\iclrfinalcopy` is active.
- Chapter 5: selected V4 explicitly inputs `Scientific_data/supplementary_v4plus.tex`; preserve that file's actual dependencies. V4 uses the `Scientific_data/Plots_tables/` table files. The root-level same-named tables differ and must not replace them. `\showrebuttalcolorfalse` retains the enclosed scientific text without revision coloring.
- Chapter 6: inline appendix plus `sections/aultc.tex`; main table modules in `tables/`.
- Chapter 7: selected root includes `AAAI_2026/CameraReady/LaTeX/appendix`; its bibliography points to `AAAI_2026/CameraReady/LaTeX/aaai2026`. The historical `AAAI_2026/` prefix maps to the enclosing local paper directory. Follow the camera-ready root's figure choices; do not substitute `for_arxiv.tex`, submission sections, or the root-level bibliography.
- Chapter 8: active `supplementary_material_psb.tex`, using custom supplementary macros and counters; `\showrebuttalcolorfalse` retains scientific text.

All seven existing supplements have placeholder modules in paper order. Appendix letters are assigned by the CMU template at compilation. No supplement is fabricated. Complete active-branch and content audits remain pending each chapter's authorization.

## Copied template components

The following are actual source-to-output copies. Two copied files have narrowly documented compatibility adaptations; all eight protected originals remain unchanged. Exact source and output hashes are in `template-copies.json`; the complete copy diff is in `template-compatibility.patch`.

| Original | Destination | Status |
|---|---|---|
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-style-files/cmu-thesis-compat.sty` | `template/cmu-style-files/cmu-thesis-compat.sty` | byte-identical |
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-style-files/cmu-thesis-encoding.sty` | `template/cmu-style-files/cmu-thesis-encoding.sty` | byte-identical |
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-style-files/cmu-thesis-environments.sty` | `template/cmu-style-files/cmu-thesis-environments.sty` | byte-identical |
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-style-files/cmu-thesis-lists.sty` | `template/cmu-style-files/cmu-thesis-lists.sty` | documented technical adaptation |
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-style-files/cmu-thesis-sanity.sty` | `template/cmu-style-files/cmu-thesis-sanity.sty` | byte-identical |
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-style-files/cmu-thesis-sections.sty` | `template/cmu-style-files/cmu-thesis-sections.sty` | byte-identical |
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-style-files/cmu-thesis-title.sty` | `template/cmu-style-files/cmu-thesis-title.sty` | byte-identical |
| `CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template/cmu-thesis.sty` | `template/cmu-thesis.sty` | documented technical adaptation |

The template example informed document orchestration and front matter. Its sample chapters, bibliography, custom scientific-equation examples, and artwork were not copied. Conference/journal classes were not imported.

## Verification boundary

Post-review build selection: additional root-level `Proposal/cmu-thesis.sty` and `Proposal/cmu-style-files/` copies were found to match the original, unpatched template. They are not the configured runtime copies in the table above and were left unchanged. The shared `Proposal/.latexmkrc` prepends `Proposal/template/` to the search path for both native LaTeX Workshop and CLI builds; the build recorder must confirm that all eight actual CMU inputs come from that directory. Separate root-level one-pass `main.*` outputs were archived under `build/legacy-single-pass/`. See the Phase B correction validation report; no scientific source selections or dependencies changed.

`protected-source-hashes.json` records SHA-256 hashes for all 587 pre-existing protected files and their directory inventory before Phase B copying/building. `scripts/verify_sources.py` compares the current protected trees with that snapshot and verifies the documented template copies. This proves file preservation within the captured boundary; it does not prove scientific equivalence of future migrations. No paper content has yet been transformed, and label/citation/macro mappings are currently empty.
