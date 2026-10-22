# Dissertation proposal specification and phased execution plan

This document is the authoritative project specification. `AGENTS.md` contains the non-negotiable working rules. The folders `Papers/`, `Chapters/`, and `CMU-PhD-Template/` already exist; **only** `Proposal/` is the generated thesis workspace. Preserve the source trees.

## Degree and title page
- Degree: **Doctor of Philosophy in Machine Learning and Public Policy**, Carnegie Mellon University.
- Required exact statement:

  > Submitted in partial fulfillment of the requirements  
  > for the degree of Doctor of Philosophy  
  > in Machine Learning and Public Policy.

- Thesis committee, in this exact order:
  - George H. Chen (Co-Chair)
  - Jeremy C. Weiss (Co-Chair)
  - Zachary C. Lipton
  - Vaishnavh Nagarajan
- Author: **Shahriar Noroozizadeh** (explicitly confirmed by the user during Phase B authorization).
- Dissertation title has not been determined: use a clear editable placeholder/macro. Submission date, copyright year, and optional college/department display remain editable until confirmed.
- Use the copied CMU template for front matter, title page formatting, abstract placeholder, contents, list of figures, list of tables, pagination, appendices, and single bibliography. Retain required template files inside `Proposal/`.

## Structure and source mapping
The following chapter titles are working headings; their use does not authorize rewriting existing paper text.

| Order | Part | Chapter/title | Read-only source (within `Papers/`) |
|---|---|---|---|
| 1 | — | Introduction | Placeholder; no source manuscript |
| 2 | I: Learning from Structured Longitudinal Clinical Trajectories | Temporal Representation Learning | `Part-i/Temporal-SCL-ML4H2023/` |
| 3 | II: Causal Inference from Longitudinal Clinical Data | Medication Adherence and Causal Modeling of Longitudinal Clinical Outcomes | `Part-ii/Impact-of-Medication-Non-adherence-CHIL2025/` |
| 4 | II | Heterogeneous Treatment Effects under Censoring: SurvHTE | `Part-ii/SurvHTE-Bench-ICLR2026/` |
| 5 | III: Recovering and Reasoning over Clinical Trajectories from Text | The Textual Time Series Framework / PMOA-TTS | `Part-iii/PMOA-TTS-ScientificData2027/` |
| 6 | III | Reconstructing Sepsis Trajectories from Clinical Text | `Part-iii/T2S2-CHIL2026/` |
| 7 | III | Forecasting Clinical Risk from Textual Time Series | `Part-iii/T2S2-Forecasting-AAAI2026/` |
| 8 | III | Aligning Textual Trajectories with Structured EHR Data | `Part-iii/Text-Knows-What-Tables-Know-When-PSB2027/` |
| 9 | III | Verification and Decision-Making from Textual Sepsis Trajectories | Placeholder for RL/sepsis verification proposal |
| 10 | — | Discussion and Conclusion | Placeholder; no source manuscript |

### Authoritative manuscript roots and selection authority

The user confirmed the Chapter 2, 5 and 7 source selections after reviewing Phase A on October 19, 2026, and explicitly confirmed Chapters 3 and 4 on October 20, 2026. These decisions persist across sessions and supersede the corresponding preflight ambiguities.

| Chapter | Authoritative root, relative to the paper directory above | Selection authority |
|---|---|---|
| 2 | `noroozizadeh23.tex` | Explicit user selection; the alternative `CopyOfMain.tex` was byte-identical during preflight. |
| 3 | `main.tex` | Explicit user confirmation and migration approval, October 20, 2026; follow all 15 active `Sections/` inputs, including all six supplementary modules. |
| 4 | `main.tex` | Explicit user confirmation and complete SurvHTE/Appendix C migration approval, October 20, 2026; active `\iclrfinalcopy`, mathematical macros, local artwork and complete inline supplement. |
| 5 | `Scientific_data/main_pmoa_tts_V4.tex` | Explicit user selection, described as `V4.tex`; this is the actual existing V4 filename. |
| 6 | `main.tex` | Explicit Phase F approval, October 20, 2026; selected CHIL reconstruction manuscript, all four active inputs and entire inline appendix. Keep separate from Chapter 7. |
| 7 | `CameraReady/LaTeX/main_with_appendix.tex` | Explicit Phase 0 selection reaffirmed in Phase G; all seven active input/include edges and complete thirteen-parent camera-ready supplement. |
| 8 | `psb_camera_ready.tex` | Identified under explicit Phase H authorization: only complete local root, matching requested title, accepted PSB 2027 declaration and revised paired-bootstrap claims; includes complete `supplementary_material_psb.tex`. No competing main manuscript locally. |

Follow each selected root's actual active `\input`, `\include`, bibliography, artwork, and supplementary dependencies. Do not mix content from other manuscript versions. In particular, Chapter 5 currently includes `Scientific_data/supplementary_v4plus.tex`, and Chapter 7 includes `CameraReady/LaTeX/appendix.tex` through its original `AAAI_2026/` path prefix. Preserve these dependency choices when adapting paths. Deep audits and scientific-content migration remain subject to each chapter's approval gate.

Phase B was authorized in the same user instruction. Chapter 2 migration is **not** authorized until the completed skeleton is reviewed and explicitly approved.

Current approval checkpoint (October 20, 2026): Chapters 2-7 and Appendices A-F are independently audited and approved. Phase H authorizes Chapter 8 and its entire active supplement as Appendix G, the final existing research-paper migration. The identified authoritative local root is `psb_camera_ready.tex`, with its exact active dependencies and false-color rebuttal branch. Preserve approved science, artwork, sizing, formatting, citations and editor/build configuration. Chapter 8/G is compiled and validated for independent user review (October 21, 2026; `Proposal/metadata/validation-ch08.md`). Stop here; do not begin Chapters 1, 9, 10 or the overarching abstract. Earlier phase-gate descriptions are historical requirements, superseded only by explicit approvals.

Source cross-check links (not substitutes for local sources):
- Ch 2: https://arxiv.org/abs/2312.05933
- Ch 3: https://arxiv.org/abs/2506.18187
- Ch 4: https://arxiv.org/abs/2603.05483
- Ch 5: https://arxiv.org/abs/2505.20323
- Ch 6: https://arxiv.org/abs/2504.12326
- Ch 7: https://arxiv.org/abs/2504.10340
- Ch 8: https://arxiv.org/abs/2605.15168

Insert Part I before Chapter 2, Part II before Chapter 3, and Part III before Chapter 5. Avoid hardcoded counters and cross-reference numbers. Each of the seven research manuscripts is an independent thesis chapter; **do not combine Chapters 6 and 7**.

## Appendix order
After Chapter 10, place the existing full appendices/supplementary materials in paper/chapter order, each independently organized:
1. Ch 2 Temporal-SCL
2. Ch 3 non-adherence
3. Ch 4 SurvHTE
4. Ch 5 PMOA-TTS
5. Ch 6 T2S2 CHIL
6. Ch 7 T2S2 AAAI
7. Ch 8 textual–tabular alignment

Assign Appendix A/B/... automatically and only to appendix material that actually exists. Convert appendix material into native thesis LaTeX, not an external appended PDF. Update references throughout the main text and supplementary text without changing scientific wording.

## Output layout
Create a clean working tree similar to:

```text
Proposal/
  main.tex
  references.bib
  README.md
  .latexmkrc
  template/                      # copied needed CMU template components
  macros/
    packages.tex
    commands.tex
    theorem-environments.tex
    ...                          # namespaced paper-specific macros as necessary
  frontmatter/
    titlepage.tex
    abstract.tex
  Chapters/
    chapter-01/
      chapter.tex
      sections/
      images/
      figures/
      tables/
    ...
    chapter-10/
      chapter.tex
      sections/
      images/
      figures/
      tables/
  Appendices/
    appendix-ch02/
      appendix.tex
      sections/
      images/
      figures/
      tables/
    ...                          # additional appendix folders only for sources present
  scripts/                       # reproducible inventory / validation scripts
  metadata/
    source-manifest.md
    transformation-log.md
    progress.md
    validation-ch02.md
    ...
  build/                         # compilation intermediates and final PDF
```

`main.tex` should mostly contain preamble + front matter + ordered `\input{...}` directives for chapter and appendix entry points + unified bibliography. Use explicit `\input` for section, figure, and table modules. Maintain paper-origin provenance (original path -> destination path) in the manifest. The appendix folder's finer layout can adapt to an actual paper's content.

## Scientific preservation protocol
Preserve every active scientific passage, mathematical statement, figure/table caption, footnote, abstract, algorithm, theorem, and original supplementary section. Even known typos are immutable. No paraphrase, grammatical fixes, deduplication across papers, or newly authored transitions. Preserve original scientific float data and artwork. The original manuscript's document-specific wrappers, venue title pages, and author affiliations need review: keep scientific abstracts, and flag potentially substantive or ambiguous discarded material instead of silently deleting it.

Technical edits allowed: `\documentclass`/wrapper removal, chapter/section-level adaptation, path changes, namespaced labels/macros, citation-key changes with equivalent bibliography entries, package conflict resolution, and layout adaptations that preserve meaning and visible data. Log every nontrivial transformation and map old labels/keys to new labels/keys. Use the CMU template, not paper-specific styles, as the base.

## Source selection and source manifest
For each source folder examine candidate root `.tex` files, input/include graph, actual build selection, final PDFs, README/metadata, bibliography, images, tables, supplementary material, conditional compilation, and custom macros. Prefer evidence over filenames/timestamps. If the final source is unclear or mismatched with available PDFs, request a decision. List unresolved ambiguities before migrating that paper.

## Phase sequence and approval gates

### Phase A — Read-only preflight (no writes)
- Inspect directory names and structure and how the CMU template builds.
- Identify obvious candidate roots and dependencies for the paper sources at a high level; deep-audit one paper when it is its turn.
- Report missing software/dependencies, possible main-file ambiguity, and an implementation plan.
- Do not create/edit files; wait for approval before Phase B.

### Phase B — Compilable skeleton
- Create only `Proposal/` outputs; copy, not move, necessary template files.
- Construct `main.tex`, front matter, parts, chapters 1–10, placeholders (1/9/10), appendices structure, macros, bibliography configuration, reproducible build command, manifest/progress/log files.
- Ensure correct numbering and compilation before migrating scientific content.
- Record exact compilation command and any remaining diagnostics; wait for approval.

### Phase C — Chapter 2 migration
- Audit/version-select Temporal-SCL; surface genuine ambiguity.
- Copy sources and images, split active section text to `sections/`, extract LaTeX figures/tables to their folders, preserve all active material.
- Integrate exact appendix and bibliography; namespace labels and conflicting macros, documenting mappings.
- Compile the **entire thesis**, repeat reference/bibliography passes, and perform programmatic plus visual checks.
- Report selected manuscript, section inventories and content reconciliation, figure/table/equation/footnote inventory, appendix, changes made, warnings/errors, and compiled PDF path.
- **Stop and await explicit approval before Chapter 3**.

### Subsequent phases — one paper per chapter
Repeat Chapter 2's cycle for Chapters 3, 4, 5, 6, 7, and 8, compiling the whole accumulated dissertation and rechecking approved chapters for regressions. Seek approval between chapters. Do not invent content for 1, 9, 10.

## Chapter acceptance evidence
Each migrated chapter must have `Proposal/metadata/validation-chXX.md` recording:
- Exact selected source root/branch, justification, source and appendix file inventory.
- Original -> output map; expected vs actual sections, images, figures, tables, equations, theorems, algorithms, footnotes, and scientific abstracts where applicable.
- Evidence of unchanged prose and math (with allowed structural transformation exceptions). Counts/hashes aid checking but are **not proof** alone; disclose items requiring manual review.
- Citation/label collision resolutions and all changed reference mappings.
- Actual full-dissertation compile command + exit status; log diagnostics, unresolved warnings, and meaningful layout exceptions.
- PDF path and recommended pages needing visual inspection.
- Specific user decisions/blockers and ready-for-review status.

Do not suppress compiler warnings to claim cleanliness. Do not claim scientific-text equivalence without corresponding evidence. Reuse the same validated workflow for later chapters and improve the scripts as lessons arise.
