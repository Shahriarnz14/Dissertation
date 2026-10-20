#!/usr/bin/env python3
"""Verify protected sources and the documented copied-template versions."""
from pathlib import Path
import hashlib
import json
import sys

PROPOSAL = Path(__file__).resolve().parents[1]
REPO = PROPOSAL.parent
snapshot = json.loads((PROPOSAL / "metadata/protected-source-hashes.json").read_text())
actual = {}
directories = []
for name in snapshot["roots"]:
    for item in sorted((REPO / name).rglob("*")):
        relative = item.relative_to(REPO).as_posix()
        if item.is_file():
            actual[relative] = hashlib.sha256(item.read_bytes()).hexdigest()
        elif item.is_dir():
            directories.append(relative)
expected = snapshot["sha256"]
errors = []
for name in sorted(expected.keys() | actual.keys()):
    if expected.get(name) != actual.get(name):
        errors.append(f"Protected file changed, added, or missing: {name}")
if sorted(directories) != snapshot["directories"]:
    errors.append("Protected source directory inventory changed")
template = REPO / "CMU-PhD-Template/Carnegie_Mellon_University_UNOFFICIAL_Thesis_Template"
copies = json.loads((PROPOSAL / "metadata/template-copies.json").read_text())
copied = sorted((PROPOSAL / "template").rglob("*.sty"))
if {x.relative_to(PROPOSAL).as_posix() for x in copied} != set(copies):
    errors.append("Copied-template file inventory changed")
for name, record in copies.items():
    destination = PROPOSAL / name
    if not destination.is_file() or hashlib.sha256(destination.read_bytes()).hexdigest() != record["copy_sha256"]:
        errors.append(f"Template copy differs from documented version: {name}")
    if expected.get(record["source"]) != record["source_sha256"]:
        errors.append(f"Template source provenance mismatch: {name}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
unchanged = sum(r["source_sha256"] == r["copy_sha256"] for r in copies.values())
print(f"PASS: {len(actual)} protected files and directory inventory unchanged; {unchanged} template copies identical, {len(copies) - unchanged} documented compatibility adaptations verified.")
