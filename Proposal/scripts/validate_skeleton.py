#!/usr/bin/env python3
"""Phase B checks against the actual PDF, AUX targets, logs, and source boundary.

This validates the skeleton only. It cannot certify migrated scientific content.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
from check_build import inspect_build, metadata_values

proposal = Path(__file__).resolve().parents[1]
build = proposal / "build"
errors = []
checks = []

def check(condition, description):
    (checks if condition else errors).append(description)

def run(*args):
    return subprocess.run(args, check=True, text=True, capture_output=True).stdout

run(sys.executable, "-B", str(proposal / "scripts/verify_sources.py"))
checks.append("Protected source hashes and copied-template provenance match")
selections = json.loads((proposal / "metadata/source-selections.json").read_text())
main = (proposal / "main.tex").read_text()
expected = []
for number in range(1, 11):
    if number in {2, 3, 5}:
        expected.append(f"Parts/part-{ {2: 1, 3: 2, 5: 3}[number]:02d}")
    expected.append(f"Chapters/chapter-{number:02d}/chapter")
expected += [f"Appendices/appendix-ch{n:02d}/appendix" for n in range(2, 9)]
actual = re.findall(r"\\input\{((?:Chapters|Parts|Appendices)/[^}]+)\}", main)
check(actual == expected, "Ten chapters, three Parts, and seven appendix modules are input in the approved order")
tex_files = [p for p in proposal.rglob("*.tex") if "build" not in p.relative_to(proposal).parts]
for path in tex_files:
    text = path.read_text()
    root = re.search(r"^%\s*!\s*T[Ee]X\sroot\s*=\s*(.*\.tex)$", text, re.M)
    if path == proposal / "main.tex":
        check(root is None and r"\documentclass[letterpaper,12pt]{article}" in text and not re.search(r"^%\s*!\s*T[Ee]X\s(?:program|options)\s*=", text, re.M), "Main is the article-class root, without a root loop or magic program/options overriding the native latexmk recipe")
    else:
        check(root is not None and (path.parent / root.group(1)).resolve() == proposal / "main.tex", f"Root directive resolves to main.tex: {path.relative_to(proposal)}")
    for target in re.findall(r"^\\input\{([^}]+)\}", text, re.M):
        check((proposal / (target + ".tex")).is_file(), f"Input exists: {target}.tex")
    check(not re.search(r"\\(?:setcounter|addtocounter)\{(?:chapter|appendix)\}", text), f"No hardcoded chapter/appendix counters: {path.relative_to(proposal)}")
check(not re.search(r"^\s*@", (proposal / "references.bib").read_text(), re.M), "No fabricated BibTeX entries")
check(not (build / "main.bbl").exists(), "Empty skeleton does not fabricate a BBL or run BibTeX")
check(not (build / "main.lof").read_text().strip(), "List of Figures is empty")
check(not (build / "main.lot").read_text().strip(), "List of Tables is empty")
aux = (build / "main.aux").read_text()
labels = {name: (value, page, target) for name, value, page, target in re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{([^}]*)\}\{[^}]*\}\{([^}]*)\}", aux)}
destinations = {name: int(page) for page, name in re.findall(r'^\s*(\d+)\s+\[.*?\]\s+"([^"]+)"', run("pdfinfo", "-dests", str(build / "main.pdf")), re.M)}
text = run("pdftotext", "-layout", str(build / "main.pdf"), "-")
pages = text.split("\f")
if not pages[-1].strip():
    pages.pop()
check(len(pages) == 27, "Complete skeleton PDF contains 27 pages")
first = " ".join(pages[0].split())
check("Submitted in partial fulfillment of the requirements for the degree of Doctor of Philosophy in Machine Learning and Public Policy." in first, "Exact required degree statement appears on the title page")
committee = ["George H. Chen (Co-Chair)", "Jeremy C. Weiss (Co-Chair)", "Zachary C. Lipton", "Vaishnavh Nagarajan"]
positions = [first.find(x) for x in committee]
check(all(x >= 0 for x in positions) and positions == sorted(positions), "Committee appears in the required order")
check("Shahriar Noroozizadeh" in first and metadata_values()["ProposalTitle"] in first, "Confirmed author and current editable title appear")
for number in range(1, 11):
    name = f"chap:ch{number:02d}"
    value, page, target = labels.get(name, (None, None, None))
    check(value == str(number), f"Automatically numbered Chapter {number}")
    pdf_page = destinations.get(target)
    check(pdf_page is not None and f"Chapter {number}\n" in pages[pdf_page - 1], f"Chapter {number} label points to its actual PDF page")
    check(pdf_page is not None and "PLACEHOLDER" in pages[pdf_page - 1], f"Chapter {number} is explicitly marked as a placeholder")
    title = selections["chapters"][str(number)]["title"]
    check(pdf_page is not None and title in " ".join(pages[pdf_page - 1].split()), f"Chapter {number} title matches the approved plan")
for number, letter in zip(range(2, 9), "ABCDEFG"):
    value, page, target = labels.get(f"app:ch{number:02d}", (None, None, None))
    pdf_page = destinations.get(target)
    check(value == letter and pdf_page is not None and f"Appendix {letter}" in pages[pdf_page - 1], f"Automatic Appendix {letter} for Chapter {number} has a valid target")
for name, value in [("structured", "I"), ("causal", "II"), ("text", "III")]:
    check(labels.get(f"part:{name}", (None,))[0] == value, f"Automatic Part {value} label")
log = (build / "main.log").read_text()
check(not re.search(r"(?:Overfull|Underfull) \\[hv]box|undefined|multiply defined|Token not allowed|pop empty|^!|Fatal error", log, re.I | re.M), "No box diagnostics, undefined references/citations, duplicate labels, PDF-string or color-stack errors")
warning_blocks = re.findall(r"(?:LaTeX|Package [^\n]+) Warning:[\s\S]*?(?=\n\n)", log)
expected_warnings = ["There are no tables or figures", "It is recommended that you include the 'acknowledgments' section"]
check(len(warning_blocks) == 2 and all(any(x in block for x in expected_warnings) for block in warning_blocks), "Only the two documented template advisories remain")
protected_roots = [proposal.parent / name for name in ["Papers", "Chapters", "CMU-PhD-Template"]]
inputs = [(proposal / line[6:]).resolve() for line in (build / "main.fls").read_text().splitlines() if line.startswith("INPUT ")]
check(not any(path.is_relative_to(root) for path in inputs for root in protected_roots), "Build reads copied workspace components, not protected source manuscripts")
consistency = inspect_build()
checks.extend(consistency["checks"])
errors.extend(consistency["errors"])
result = {"phase": "B", "passed": not errors, "pdf_pages": len(pages), "checks_passed": len(checks), "errors": errors, "checks": checks, "warnings": warning_blocks, "build_consistency": consistency}
(build / "validation-skeleton.json").write_text(json.dumps(result, indent=2) + "\n")
print(f"{'PASS' if not errors else 'FAIL'}: {len(checks)} checks; {len(errors)} errors; {len(warning_blocks)} documented advisories.")
for error in errors:
    print(error, file=sys.stderr)
sys.exit(bool(errors))
