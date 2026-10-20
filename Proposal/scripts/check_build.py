#!/usr/bin/env python3
"""Reject stale or unconverged PDFs; verify rendered CMU contents and pagination.

This reads generated TOC/AUX records, not scientific manuscripts. It never
manufactures document entries, changes counters, or suppresses diagnostics.
"""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

PROPOSAL = Path(__file__).resolve().parents[1]


def group(text, start):
    """Read one balanced TeX group, respecting escaped braces."""
    while start < len(text) and text[start].isspace():
        start += 1
    if start >= len(text) or text[start] != "{":
        raise ValueError(f"Expected a group near {text[start:start + 50]!r}")
    depth, position = 1, start + 1
    while position < len(text):
        if text[position] == "\\":
            position += 2
            continue
        if text[position] == "{":
            depth += 1
        elif text[position] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:position], position + 1
        position += 1
    raise ValueError("Unbalanced generated TeX record")


def records(text, command, count):
    result = []
    for match in re.finditer(r"\\" + re.escape(command) + r"(?![A-Za-z@])", text):
        values, position = [], match.end()
        for _ in range(count):
            value, position = group(text, position)
            values.append(value)
        result.append(values)
    return result


def metadata_values(proposal=PROPOSAL):
    text = (proposal / "frontmatter/metadata.tex").read_text()
    result = {}
    for name in ["ProposalTitle", "ProposalSubmissionDate", "ProposalCopyrightYear"]:
        match = re.search(r"\\newcommand\{\\" + name + r"\}", text)
        if match is None:
            raise ValueError(f"Editable metadata macro missing: {name}")
        result[name], _ = group(text, match.end())
    return result


def normalized(text):
    text = text.replace("--", "-")
    text = text.translate(str.maketrans({c: "-" for c in "\u2010\u2011\u2012\u2013\u2014\u2212"}))
    for escaped, plain in [(r"\&", "&"), (r"\%", "%"), (r"\_", "_"), ("~", " ")]:
        text = text.replace(escaped, plain)
    return " ".join(text.split()).casefold()


def roman(number):
    result = ""
    for value, digits in [(1000, "m"), (900, "cm"), (500, "d"), (400, "cd"), (100, "c"), (90, "xc"), (50, "l"), (40, "xl"), (10, "x"), (9, "ix"), (5, "v"), (4, "iv"), (1, "i")]:
        while number >= value:
            result += digits
            number -= value
    return result


def inspect_build(proposal=PROPOSAL, *, build=None):
    build = build or proposal / "build"
    errors, checks = [], []

    def check(condition, description):
        (checks if condition else errors).append(description)

    def run(*args):
        return subprocess.run(args, check=True, capture_output=True, text=True).stdout

    pdf = build / "main.pdf"
    text = run("pdftotext", "-layout", str(pdf), "-")
    pages = text.split("\f")
    if not pages[-1].strip():
        pages.pop()
    destinations = {name: int(page) for page, name in re.findall(r'^\s*(\d+)\s+\[.*?\]\s+"([^"]+)"', run("pdfinfo", "-dests", str(pdf)), re.M)}
    aux = (build / "main.aux").read_text()
    labels = {}
    for name, body in records(aux, "newlabel", 2):
        values, position = [], 0
        for _ in range(5):
            value, position = group(body, position)
            values.append(value)
        labels[name] = {"value": values[0], "page": values[1], "target": values[3]}
    toc = [{"kind": kind, "title_tex": title, "page": page, "target": target} for kind, title, page, target in records((build / "main.toc").read_text(), "contentsline", 4)]
    first_toc, after_toc = destinations.get("toc.1"), destinations.get("lof.1")
    check(first_toc is not None and after_toc is not None and after_toc > first_toc, "TOC has a distinct PDF page range before the List of Figures")
    toc_text = normalized(" ".join(pages[first_toc - 1:after_toc - 1])) if first_toc and after_toc else ""
    selections = json.loads((proposal / "metadata/source-selections.json").read_text())
    expected = []
    for number in range(1, 11):
        expected.append((f"chap:ch{number:02d}", "section", selections["chapters"][str(number)]["title"], "chapter"))
    for number, name in enumerate(["structured", "causal", "text"], 1):
        title = records((proposal / f"Parts/part-{number:02d}.tex").read_text(), "part", 1)[0][0]
        expected.append((f"part:{name}", "part", f"Part {roman(number).upper()} {title}", "part"))
    for number, letter in zip(range(2, 9), "ABCDEFG"):
        title = records((proposal / f"Appendices/appendix-ch{number:02d}/appendix.tex").read_text(), "appendix", 1)[0][0]
        expected.append((f"app:ch{number:02d}", "appendix", f"Appendix {letter} {title}", "appendix"))
    reconciled = []
    for name, kind, title, category in expected:
        label = labels.get(name, {})
        entries = [entry for entry in toc if entry["target"] == label.get("target") and entry["kind"] == kind]
        check(len(entries) == 1, f"One automatic TOC record for {name} (CMU type {kind})")
        if len(entries) != 1:
            continue
        entry = entries[0]
        physical = destinations.get(label.get("target"))
        check(entry["page"] == label.get("page") and physical is not None, f"TOC page/target agrees with compiled label: {name}")
        pattern = re.escape(normalized(title)) + r"[ .]+" + re.escape(entry["page"].casefold()) + r"(?=\s|$)"
        check(re.search(pattern, toc_text) is not None, f"Rendered TOC contains title and automatic page number: {name}")
        if physical:
            check(pages[physical - 1].strip().splitlines()[-1].strip() == entry["page"], f"TOC page matches the visible destination-page footer: {name}")
        reconciled.append({"label": name, "category": category, "title": title, "printed_page": entry["page"], "pdf_page": physical, "target": label.get("target")})
    absolute = re.search(r"\\gdef\s*\\@abspage@last\s*\{(\d+)\}", aux)
    check(absolute is not None and int(absolute.group(1)) == len(pages), "LaTeX last-page record equals the actual physical PDF page count")
    check("temporary page!" not in text.casefold() and "unable to guess the total number of pages" not in text.casefold(), "PDF contains no temporary-page notice")
    check("Bibliography" in pages[-1] and "PLACEHOLDER" in pages[-1], "Final skeleton page is the genuine bibliography placeholder")
    body_start = destinations.get(labels.get("chap:ch01", {}).get("target"))
    check(body_start is not None, "First chapter target exists")
    if body_start:
        for physical in range(2, body_start):
            value = roman(physical - 1)
            check(pages[physical - 1].strip().splitlines()[-1].strip() == value and destinations.get("page." + value) == physical, f"Roman footer and PDF page label agree on physical page {physical}: {value}")
        for physical in range(body_start, len(pages) + 1):
            value = str(physical - body_start + 1)
            check(pages[physical - 1].strip().splitlines()[-1].strip() == value and destinations.get("page." + value) == physical, f"Continuous Arabic footer/page label on physical page {physical}: {value}")
    values = metadata_values(proposal)
    for name, value in values.items():
        check(normalized(value) in normalized(pages[0]), f"PDF title page reflects the current editable {name} value")
    log = (build / "main.log").read_text()
    check(re.search(r"Rerun|Temporary extra page|executed on wrong page|Illegal parameter number|^!|Fatal error", log, re.I | re.M) is None, "Final compiler pass has no unresolved rerun, temporary-page, last-page-hook, or TeX error diagnostic")
    recorder = build / "main.fls"
    check(recorder.is_file(), "A compiler recorder exists for verifying the actual input/output paths")
    recorder_text = recorder.read_text() if recorder.is_file() else ""
    inputs = [(proposal / line[6:]).resolve() for line in recorder_text.splitlines() if line.startswith("INPUT ")]
    cmu = {path for path in inputs if path.name == "cmu-thesis.sty" or path.parent.name == "cmu-style-files"}
    check(len(cmu) == 8 and all(path.is_relative_to(proposal / "template") for path in cmu), "All eight actual CMU style inputs come from Proposal/template; root-level duplicates cannot shadow them")
    authored = {path for path in inputs if path.is_relative_to(proposal) and not path.is_relative_to(build) and path.suffix in {".tex", ".sty", ".bib"}}
    check(all(path.stat().st_mtime_ns <= pdf.stat().st_mtime_ns for path in authored), "PDF is newer than every actual local TeX/style/bibliography input")
    outputs = [(proposal / line[7:]).resolve() for line in recorder_text.splitlines() if line.startswith("OUTPUT ")]
    check(all(path.is_relative_to(build) for path in outputs), "Recorder confirms compilation outputs are confined to build/")
    return {"passed": not errors, "checks_passed": len(checks), "checks": checks, "errors": errors, "pdf_pages": len(pages), "pdf_sha256": hashlib.sha256(pdf.read_bytes()).hexdigest(), "toc_pdf_pages": list(range(first_toc, after_toc)) if first_toc and after_toc else [], "toc_expected_counts": {"parts": 3, "chapters": 10, "appendices": 7}, "toc_reconciliation": reconciled, "metadata_values": values, "metadata_sha256": hashlib.sha256((proposal / "frontmatter/metadata.tex").read_bytes()).hexdigest(), "source_input_sha256": {path.relative_to(proposal).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in sorted(authored)}}


if __name__ == "__main__":
    result = inspect_build()
    (PROPOSAL / "build/build-consistency.json").write_text(json.dumps(result, indent=2) + "\n")
    print(f"{'PASS' if result['passed'] else 'FAIL'}: {result['checks_passed']} build-consistency checks; {len(result['errors'])} errors.")
    for error in result["errors"]:
        print(error, file=sys.stderr)
    sys.exit(not result["passed"])
