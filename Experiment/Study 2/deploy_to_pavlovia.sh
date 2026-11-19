#!/bin/bash
# Push Study 2 to its ONE Pavlovia project:
#     https://gitlab.pavlovia.org/genres-and-themes/experiment-2
# It never pushes anywhere else: the repository address is fixed below and checked
# again after cloning, and it stops if the clone holds Study 1's experiment.
#
# It replaces index.html, experiment.js, style.css and captcha.png at the
# repository root, updates the stimuli/ folder (the six stimuli_<genre>.json files
# and stimuli_all.js), removes the item files of the retired two-genre build if the
# project still has them, and creates data/ (with an empty .gitkeep) if the project
# does not have it yet. It never pushes config.json: Pavlovia serves the correct one
# itself. It shows what will change and asks you to type experiment-2 before
# pushing. Git will ask for your Pavlovia GitLab username and password or token.

set -euo pipefail

TARGET="https://gitlab.pavlovia.org/genres-and-themes/experiment-2.git"
SRC="$(cd "$(dirname "$0")" && pwd)"
FILES=(index.html experiment.js style.css captcha.png)
STIMULI=(stimuli_western.json stimuli_horror.json stimuli_crime.json stimuli_science_fiction.json stimuli_comedy.json stimuli_fantasy.json stimuli_all.js)

echo "============================================================"
echo " Study 2 will be pushed to:"
echo "   https://gitlab.pavlovia.org/genres-and-themes/experiment-2"
echo " (not experiment-1, which holds Study 1)"
echo "============================================================"

for f in "${FILES[@]}"; do
  [ -f "$SRC/$f" ] || { echo "Missing $SRC/$f"; exit 1; }
done
for f in "${STIMULI[@]}"; do
  [ -f "$SRC/stimuli/$f" ] || { echo "Missing $SRC/stimuli/$f"; exit 1; }
done
grep -q "var STUDY_CODE = 'SAF_STUDY2';" "$SRC/experiment.js" || { echo "STOP: experiment.js is not the Study 2 code."; exit 1; }
if grep -q "credit_token=[0-9a-f]" "$SRC/experiment.js"; then
  echo "Note: experiment.js holds a SONA credit token. That is right for Pavlovia; blank it in any public copy."
fi

WORK="$(mktemp -d)"
echo "Cloning into $WORK ..."
git clone --quiet "$TARGET" "$WORK/experiment-2"
cd "$WORK/experiment-2"

ORIGIN="$(git remote get-url origin)"
if [ "$ORIGIN" != "$TARGET" ]; then
  echo "STOP: this clone points to $ORIGIN, not $TARGET. Nothing was pushed."
  exit 1
fi
if ! git rev-parse --verify --quiet HEAD > /dev/null; then
  echo "STOP: the clone is empty. Nothing was pushed."
  exit 1
fi
if grep -q "SAF_STUDY1" experiment.js 2>/dev/null; then
  echo "STOP: this repository holds Study 1's experiment, so it is not the Study 2 project. Nothing was pushed."
  exit 1
fi
BRANCH="$(git rev-parse --abbrev-ref HEAD)"

mkdir -p stimuli data
[ -e data/.gitkeep ] || : > data/.gitkeep
for f in "${FILES[@]}"; do cp "$SRC/$f" "./$f"; done
for f in "${STIMULI[@]}"; do cp "$SRC/stimuli/$f" "stimuli/$f"; done
# Item files of the retired two-genre build, if they were ever pushed.
git rm --quiet --ignore-unmatch stimuli/study2_items.json stimuli/study2_items.js

git add "${FILES[@]}" stimuli data/.gitkeep
if git diff --cached --quiet; then
  echo "Nothing changed; nothing to push."
  exit 0
fi

echo
echo "Files that will be added, changed or removed in genres-and-themes/experiment-2:"
git diff --cached --stat
echo
read -r -p "Type experiment-2 to push, or anything else to stop: " ok
[ "$ok" = "experiment-2" ] || { echo "Not pushed. Clone left at $WORK"; exit 0; }

git commit --quiet -m "Study 2 (one shared feature: three rated questions and a mouse-tracked copying choice)"
git push --quiet origin "HEAD:refs/heads/$BRANCH"
echo
echo "Pushed to genres-and-themes/experiment-2 (branch $BRANCH)."
echo "Test links (your own runs, no SONA, no credit), one per condition:"
for c in COPY GENRE STOCK TRACK; do
  echo "https://run.pavlovia.org/genres-and-themes/experiment-2/index.html?participant=PILOT_DK_$c&cond=$c"
done
