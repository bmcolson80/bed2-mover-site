#!/usr/bin/env python3
"""Builds index.html (the drum kit mover) from every plan SVG under plans/.

    python3 build.py                 # plans/ -> index.html
    python3 build.py --plans DIR --out FILE

The folder layout under plans/ matters: the template groups plans by their path
(a path containing "archive" = Archive, "BASE PLAN" = existing conditions,
"DESIGN" = designs) and labels them from the file name. Name new designs
"Bed2 DESIGN vN plan.svg" and put them in plans/Bed2 DESIGN/.

Each design SVG should end with  <!-- studio-clear: x0,y0,x1,y1 -->  (studio clear
area in mm from the window wall / laundry wall) so the fit check uses that design's size.

Concept tool only (Claude drawing aid, not confirmed by Brendan, not for construction).
"""
import argparse
import json
import re
import sys
from pathlib import Path

here = Path(__file__).resolve().parent
ap = argparse.ArgumentParser()
ap.add_argument("--plans", default=str(here / "plans"))
ap.add_argument("--out", default=str(here / "index.html"))
args = ap.parse_args()
root, out = Path(args.plans), Path(args.out)

plans = []
for f in sorted(root.rglob("*.svg")):
    txt = f.read_text(encoding="utf-8")
    if not re.search(r'<clipPath id="room">\s*<polygon points="', txt):
        print("skipped (no room outline):", f.relative_to(root))
        continue
    txt = re.sub(r"<metadata[\s\S]*?</metadata>", "", txt)   # drop C2PA blobs
    plans.append({"name": f.relative_to(root).as_posix(), "svg": txt})
    print("embedded:", f.relative_to(root))

if not plans:
    sys.exit("No usable plan SVGs found in " + str(root))

template = (here / "src" / "drum_kit_mover_template.html").read_text(encoding="utf-8")
data = json.dumps(plans).replace("</", "<\\/")
out.write_text(template.replace("__PLANS__", data), encoding="utf-8")
print("wrote", out, round(out.stat().st_size / 1024), "KB,", len(plans), "plans")
