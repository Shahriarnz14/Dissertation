# Copy-paste prompts for Codex

Place `AGENTS.md`, `DISSERTATION_PLAN.md`, and this file in the **same project root directory** that contains `Papers/`, `Chapters/`, and `CMU-PhD-Template/`. Open Codex in that root. Do not extract these files into `Proposal/` or into a manuscript folder.

## 1. First session — read-only audit (start here)

Read `AGENTS.md` and `DISSERTATION_PLAN.md`, then perform **Phase A only**. Inspect the repository and the actual CMU dissertation template. Identify likely manuscript roots and dependencies at a high level, find the available LaTeX build tools, and propose the exact dissertation architecture/build strategy. Explain any source-version or template uncertainties. **Do not modify or create any files yet.** Stop and show me your plan and any decisions I need to make.

## 2. After reviewing Phase A — build the skeleton

Proceed with **Phase B** from `DISSERTATION_PLAN.md`, following `AGENTS.md`. Create the new `Proposal/` tree, copying only required CMU template components. Build the front matter, 10 chapter entry points, Part I/II/III divisions, appendices infrastructure, and placeholders for Chapters 1, 9, 10 and abstract. Set up macros, unified bibliography, metadata logs, and reproducible compilation. Compile the entire skeleton, fix actionable issues, and show the PDF path, changed files, and warnings. **Do not migrate a research paper yet. Stop for review.**

## 3. After reviewing the skeleton — migrate Chapter 2

Proceed with **Phase C: Chapter 2 only**. Deep-audit the final Temporal-SCL source and any appendix, obtain my decision if its final version is genuinely ambiguous, migrate it into `Proposal/` according to the specification, and preserve **all active scientific material verbatim**. Compile the full dissertation and produce the documented validation report with original-to-destination mapping, content checks, figures/tables/equations, bibliography/references, appendix checks, layout diagnostics and PDF path. Fix issues within this chapter's scope before reporting. **Stop; do not start Chapter 3.**

## 4. Repeat for later chapters

I approve Chapter [N-1]. Now migrate **Chapter [N] only** according to `AGENTS.md` and `DISSERTATION_PLAN.md`, using the same source-selection, modularization, appendix, content-preservation, full-build, and validation workflow. Inspect the existing progress and transformation logs first. Check for regressions affecting previously approved chapters. Summarize exact evidence and any remaining uncertainties, provide the compiled PDF path, and stop for my approval before continuing.

## 5. Independent review of a completed chapter

Do a **read-only audit** of Chapter [N] in `Proposal/` against its selected original final manuscript in `Papers/`, including appendix. Review source-to-output completeness, unchanged scientific prose/math/captions, images and table values, label/citation correctness, compilation evidence, and obvious PDF layout problems. Report discrepancies with file paths and locations, distinguish confirmed issues from uncertain ones, and propose repairs. **Do not modify any files during this audit.**
