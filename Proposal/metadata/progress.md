# Dissertation progress

Updated October 19, 2026.

| Phase | Status | Approval boundary |
|---|---|---|
| A / Phase 0 - read-only inspection | Completed; reviewed by user | User resolved source choices and authorized Phase B. |
| B - compilable skeleton | Skeleton corrected; native root-folder LaTeX Workshop workflow built and validated; awaiting user's interactive verification | Stop after delivery. Chapter 2 is not yet authorized. |
| C - Chapter 2 migration | Not started | Requires explicit approval of the skeleton and Chapter 2 migration. |
| Chapters 3-8 migrations | Not started | Separate explicit approval between chapters. |

## Chapter and supplement status

| Chapter | Main text | Existing supplement | Content equivalence |
|---|---|---|---|
| 1 | Marked introduction placeholder | None planned | Not applicable |
| 2 | Temporary placeholder; `noroozizadeh23.tex` confirmed | Marked infrastructure placeholder | Not evaluated; no migration |
| 3 | Temporary placeholder | Marked infrastructure placeholder | Not evaluated; no migration |
| 4 | Temporary placeholder | Marked infrastructure placeholder | Not evaluated; no migration |
| 5 | Temporary placeholder; exact V4 root confirmed | V4 supplement infrastructure placeholder | Not evaluated; no migration |
| 6 | Temporary placeholder; independent CHIL chapter | Marked infrastructure placeholder | Not evaluated; no migration |
| 7 | Temporary placeholder; camera-ready root confirmed | Camera-ready supplement infrastructure placeholder | Not evaluated; no migration |
| 8 | Temporary placeholder | Marked infrastructure placeholder | Not evaluated; no migration |
| 9 | Marked proposed-work placeholder | None planned | Not applicable |
| 10 | Marked discussion/conclusion placeholder | None planned | Not applicable |

Overall abstract and bibliography are marked placeholders. Lists of figures and tables contain no fabricated entries.

## Persistent decisions

- Source choices for Chapters 2, 5, and 7 are authoritative user decisions; exact paths are in the root plan and source manifest. Follow actual active dependencies without mixing versions.
- Author and committee order are confirmed. The current author-entered title, date, and year are preserved in `frontmatter/metadata.tex` and remain independently editable. Optional college/department display remains unset.
- Retain the actual CMU `article` template and pdfLaTeX/BibTeX workflow. Technical repairs are isolated/documented; all protected originals remain unchanged.
- Appendices follow Chapter 10 in paper order; a single bibliography follows them.

## Review artifacts

- PDF: `build/main.pdf`.
- Build/check instructions: `README.md`.
- Phase B evidence and remaining diagnostics: `metadata/validation-phase-b.md`.
- Full source/provenance and technical-change records: `metadata/source-manifest.md`, `metadata/transformation-log.md`, and JSON/hash companions.
- Per-chapter validation reports exist as explicitly unverified reporting placeholders; they do not claim migrated content or scientific equivalence.

The next step is the user's interactive VS Code verification. Do not start Chapter 2 without separate explicit approval.

## Phase B post-review corrections

The reported empty TOC and temporary final page were reproduced in a separate one-pass root-level PDF; the earlier canonical build was stale relative to the current metadata. The correction initially routed editor entry paths through a shared multipass wrapper. The subsequent workflow simplification replaces that routing with a direct native latexmk recipe in the repository-root `.vscode/settings.json`; `build.sh` is optional. Both share `.latexmkrc`, pdfLaTeX/BibTeX, SyncTeX, and `build/main.pdf`. Actual template inputs, rendered TOC entries, and final-page convergence are checked separately. Duplicate generated root outputs were archived under `build/legacy-single-pass/`, preserving the evidence. No paper, chapter placeholder, original template, or title/date/year macro was changed.

A clean latexmk run converged in three pdfLaTeX passes. The TOC occupies PDF pages 3-4, the first chapter starts on PDF page 7 with Arabic 1, appendices occupy pages 20-26, and the last page is the bibliography on PDF page 27 (Arabic 21). Roman front matter is i-v. The stronger validator also rejects the archived faulty PDF, which had the same total of 27 pages; page count alone does not prove correct output. See `metadata/validation-phase-b.md` and `metadata/phase-b-negative-check.json`.
