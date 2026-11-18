#!/bin/bash
# Publishes new/changed plan SVGs from the Studio Build folder to the live mover page.
# Run on the Mac from this clone:   ./sync.sh            (Studio Build = parent folder)
#                                   ./sync.sh "/path/to/Studio Build"
# 1) pulls the latest   2) mirrors every *.svg from Studio Build into plans/
# 3) rebuilds index.html   4) commits and pushes (GitHub Pages updates in about a minute)
set -euo pipefail
cd "$(dirname "$0")"
SRC="${1:-..}"
[ -d "$SRC/Bed2 DESIGN" ] || { echo "Can't find '$SRC/Bed2 DESIGN' - pass the Studio Build folder as the first argument."; exit 1; }

git pull --rebase --autostash -q
rsync -a --delete --prune-empty-dirs --exclude='bed2-mover-site/' --include='*/' --include='*.svg' --exclude='*' "$SRC/" plans/
python3 build.py
git add -A plans index.html
if git diff --cached --quiet; then
  echo "Nothing new to publish."
else
  git commit -q -m "Update plans and rebuild mover page"
  git push -q
  echo "Published: https://bmcolson80.github.io/bed2-mover-site/ (allow about a minute)"
fi
