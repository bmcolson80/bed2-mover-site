# bed2-mover-site

Drum kit mover tool for Brendan's Bed 2 studio renovation (112 The Gateway, Lilydale). Published at
https://bmcolson80.github.io/bed2-mover-site/ (GitHub Pages, branch `main`, folder `/`). This repo is public: never
commit house details beyond the plan SVGs, and never commit context files, credentials or documents.

## How it works
- `plans/` holds the plan SVGs. They mirror the layout of the `Studio Build` folder on Brendan's Mac. The path
  matters: a path containing `archive` is grouped as Archive, `BASE PLAN` as existing conditions, `DESIGN` as designs.
- `src/drum_kit_mover_template.html` is the tool (HTML/JS). `build.py` embeds every SVG in `plans/` into it and writes
  `index.html`. Never hand-edit `index.html`; change the template or the SVGs and run `python3 build.py`.
- `.github/workflows/build.yml` rebuilds and commits `index.html` when `plans/`, `src/` or `build.py` change.
- `sync.sh` (run on the Mac) copies SVGs from `Studio Build` into `plans/`, rebuilds, commits and pushes.
- The designs themselves are made in the Claude chat project "Home Renovations" (generator scripts in
  `Studio Build/Bed2 DESIGN/`), not here. This repo only consumes their SVGs.

## Adding a design
1. SVG named `Bed2 DESIGN vN plan.svg`, in `plans/Bed2 DESIGN/` (superseded ones move to `plans/Bed2 DESIGN/archive/`).
2. It must contain `<clipPath id="room"><polygon points="...">` or the build skips it, and should end with
   `<!-- studio-clear: x0,y0,x1,y1 -->` (studio clear area in mm from the window wall and laundry wall).
3. Run `python3 build.py`, open `index.html` to check the new design appears in the plan dropdown, then commit and push.

## Rules
- Australian English, metric units (mm), DD Mon YYYY dates, Melbourne time.
- Designs are Claude concepts, unconfirmed until Brendan says otherwise. Keep the "unconfirmed" labelling in the tool.
- `BASE PLAN - do not edit` content is frozen: never modify those SVGs.
- Deploy is Pages from `main`; no other hosting. Brendan places any orders himself (not relevant here, but never imply otherwise).
- Keep it dependency-free: Python 3 standard library only, one self-contained `index.html`.

## Verify before finishing
`python3 build.py` reports the expected plan count, no unexpected "skipped" lines, and `index.html` opens and shows every design in the dropdown.
