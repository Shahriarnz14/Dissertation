#!/usr/bin/env python3
"""Render the full PDF for review; keep every artifact under build/pdf-review."""
from pathlib import Path
import subprocess

proposal = Path(__file__).resolve().parents[1]
review = proposal / "build/pdf-review"
review.mkdir(parents=True, exist_ok=True)
subprocess.run(["pdftoppm", "-r", "90", "-png", str(proposal / "build/main.pdf"), str(review / "page")], check=True)
from PIL import Image, ImageDraw

pages = sorted(review.glob("page-*.png"))
for start in range(0, len(pages), 6):
    group = pages[start:start + 6]
    panel_width, panel_height = 612, 816
    sheet = Image.new("RGB", (panel_width * 2, panel_height * 3), "#dddddd")
    draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(group):
        im = Image.open(path).convert("RGB")
        im.thumbnail((panel_width - 20, panel_height - 38))
        x, y = (index % 2) * panel_width, (index // 2) * panel_height
        draw.text((x + 10, y + 6), f"PDF page {start + index + 1}", fill="black")
        sheet.paste(im, (x + (panel_width - im.width) // 2, y + 26))
    sheet.save(review / f"contact-{start // 6 + 1:02d}.png")
print(f"Rendered {len(pages)} pages and {(len(pages) + 5) // 6} contact sheets to {review}")
