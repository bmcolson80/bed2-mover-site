# bed2-mover-site

Drum kit mover tool for Brendan's Bed 2 studio renovation. Published at
https://bmcolson80.github.io/bed2-mover-site/ (GitHub Pages, branch `main`, folder `/`). This repo is public: never
commit house details (including the address) beyond the plan SVGs, and never commit context files, credentials or
documents.

## How it works
- `plans/` holds the plan SVGs. They mirror the layout of the `Studio Build` folder on Brendan's Mac. The path
  matters: a path containing `archive` is grouped as Archive, `BASE PLAN` as existing conditions, `DESIGN` as designs.
- `src/drum_kit_mover_template.html` is the tool (HTML/JS). `build.py` embeds every SVG in `plans/` into it and writes
  `index.html`. Never hand-edit `index.html`; change the template or the SVGs and run `python3 build.py`.
- `.github/workflows/build.yml` rebuilds and commits `index.html` when `plans/`, `src/` or `build.py` change.
- `sync.sh` (run on the Mac) copies SVGs from `Studio Build` into `plans/`, rebuilds, commits and pushes.
- The designs themselves are made in the Claude chat project "Home Renovations" (generator scripts in
  `Studio Build/Bed2 DESIGN/`), not here. This repo only consumes their SVGs.

## Wall builder (v5 of the tool, 18 Nov 2026)
- The plan picker offers BASE PLAN v2 and v3 only (designs and archive SVGs are still embedded but not listed); all configuration is in the options. The panel's wall builder (v5: 10 mm plaster strip-back, continuous air gaps, internal dimension lines, P2 moved 200 and DL2/H2 hidden when the dividing wall is on, Fanco Infinity-iD 48 fan, 100 mm vents + 2 inline fans box) works on those two.
- On BASE PLAN v2 and v3, the panel's "Studio walls" section draws concept wall layers over the plan: dividing wall from the
  laundry end, then window, ensuite and living room walls built from their existing face into the studio (Soundchek sheets 13,
  stud 90, air gap 25 or 50, optional second stud wall), a doorway on the living room wall (one door swings in; with a second stud
  wall the outer door swings out; hinged on the ensuite side), plus ceiling fan and ventilation placeholders. All widths are editable.
- The kit fit check uses the studio clear area those layers produce. Existing studio walls are shown as stud with faces unchanged.
- Plan geometry is read from the plan's `clipPath id="room"` polygon and hard-coded v2/v3 constants (2440 step line, 112 walls,
  window 1 position); a new base plan with different geometry needs those checked in `drawWalls()`.
- Match plan names case-insensitively (the files are named "BASE plan v2").

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
