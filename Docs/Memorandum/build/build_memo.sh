#!/bin/bash
# Build the Word version of the design memo for Studies 1 to 4 of the tracking paper from its Markdown source.
# Run from Docs/Memorandum:  bash build/build_memo.sh
# The figures are copied from the analysis output first, so the memo always shows the
# figures of the latest run.
set -e
PANDOC="${PANDOC:-/Applications/RStudio.app/Contents/Resources/app/quarto/bin/tools/aarch64/pandoc}"
# RStudio's bundled pandoc moves when RStudio updates; fall back to the pandoc on the PATH.
[ -x "$PANDOC" ] || PANDOC="$(command -v pandoc)"
[ -n "$PANDOC" ] || { echo "pandoc not found"; exit 1; }
PY="${PY:-/Library/Frameworks/Python.framework/Versions/3.12/bin/python3}"
SRC=Tracking_Studies_Design_Memo_2026-11-19.md
FIGS=../../Analysis/v4_rebuild/18_tracking_studies_design/figures
mkdir -p figures
for f in law_review_study_items_expected_by_prevalence.png power_one_feature_ratings.png power_one_feature_tracking.png; do
  cp "$FIGS/$f" "figures/$f"
done
"$PANDOC" -o build/reference_default.docx --print-default-data-file reference.docx
"$PY" build/make_reference.py build/reference_default.docx build/reference.docx
"$PANDOC" "$SRC" -f markdown -o "${SRC%.md}.docx" --reference-doc=build/reference.docx --resource-path=.
"$PY" build/fix_content_types.py "${SRC%.md}.docx"
echo "wrote ${SRC%.md}.docx"
