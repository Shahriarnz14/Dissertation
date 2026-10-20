# Codex repository instructions — CMU dissertation proposal

## Purpose and source of truth
This repository contains source manuscripts (`Papers/`), an existing CMU thesis template (`CMU-PhD-Template/`), and a separate dissertation workspace to be created in `Proposal/`. Read `DISSERTATION_PLAN.md` for the approved dissertation map, architecture, and phase acceptance criteria. Read only relevant source files and current progress/decision records for the active task.

## Non-negotiable boundaries
- Treat `Papers/`, the pre-existing `Chapters/`, and `CMU-PhD-Template/` as **read-only**. Do not edit, move, rename, delete, or generate build artifacts within them. Copy needed assets into `Proposal/`. Do not use network versions to silently override local sources.
- Scientific content in the selected FINAL active manuscript and its appendices is immutable: no rewriting, spelling/grammar correction, trimming, summarizing, synthesis, duplication removal, or invented connective prose. Preserve mathematics, values, footnotes, figure/table captions, algorithms, abstracts, and scientific results. Do not silently omit anything scientifically substantive.
- Allowed changes are narrowly technical: document wrappers, section hierarchy, paths, style/layout, labels/refs, citation keys, environment/macro namespacing, float placement, and related changes needed for CMU template compatibility. Preserve the meaning and rendered scientific content. Log nontrivial changes.
- Ignore inactive commented-out material. **Never strip LaTeX comments with a naive regex**; distinguish comments from escaped percent signs, verbatim, macro/conditional compilation, and other active content. Document the selected compilation branch when relevant.
- Identify final manuscript versions using internal evidence (READMEs, final PDFs, build configurations, complete source trees), not just file names/timestamps. If uncertain or sources are missing, report the alternatives and ask; don't guess.
- Use the actual CMU template as authoritative for formatting. Do not copy conference/journal `documentclass` or layout overrides into the dissertation.
- Every original paper is its **own** chapter. In particular, T2S2 CHIL is Chapter 6, T2S2 AAAI is Chapter 7, and multimodal alignment is Chapter 8. Let LaTeX number chapters, figures, tables, equations, and appendices automatically.
- Every existing paper appendix/supplement must be migrated in paper order into the unified appendix section. Do not generate an appendix when none exists; document that fact.
- For Chapters 1, 9, 10, and the overall abstract, create **clearly marked compilable placeholders**, never substantive fabricated text.
- Keep the output modular: chapter `chapter.tex`, individual `sections/`, raw `images/`, LaTeX `figures/`, LaTeX `tables/`; analogous appendix structure where applicable. Centralize compatible common macros, but namespace conflicting definitions.
- Use a unified bibliography; preserve citation targets and metadata. Resolve label/citation/macro collisions systematically and record old-to-new mappings.

## Execution and verification
- Work one approved phase/chapter at a time; do not start the next chapter until explicit user approval. Within an approved phase, continue through compilation, troubleshooting, and validation without needless check-ins.
- Preserve a source manifest, transformation log, progress tracker, and per-chapter validation reports in `Proposal/metadata/`. Distinguish **verified** content equivalence from plausible-but-unverified equivalence.
- Compile the **complete accumulated dissertation** after each migrated chapter with reproducible commands; keep build artifacts under `Proposal/build/`.
- Verify sections, active paragraphs, math, figures/images, tables, captions, footnotes, algorithms, labels, references, and appendices against the selected original. Use programmatic inventories/diffs where sensible, binary hashes for copied image assets, and visual PDF inspection where practical. Counts alone do not prove equivalence.
- Fix errors, missing citations/references and harmful layout issues; aim for no actionable warnings. Never conceal warnings or change science just to make a warning disappear. Explicitly report unavoidable diagnostics.
- Do not claim completion without actual build output, documented checks, known limitations, and a precise list of files changed. Before proceeding beyond a chapter, provide the user the built PDF and a concise review summary.
- Don't create Git commits, push, fetch external resources, or modify original paper directories without separate explicit authorization. If version control is already present, use diffs for auditing when useful.
