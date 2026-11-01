# Issue #8 — Rendered contrast evidence (triage)

## Contents
1. Purpose
2. Method and thresholds
3. Running the evidence collector
4. Interpretation and limitations

## Purpose
Axe-core produces many incomplete colour-contrast results in themes with
gradients, transparent surfaces, textures or pseudo-elements. They are neither
passes nor confirmed failures. We preserve the full axe report and gather an
additional independent *estimate* of foreground readability against actual
background pixels painted by Chromium.

## Method
The collector uses Playwright and axe-core to locate incomplete nodes in the
real demo. It records the computed text foreground colour and element box,
then takes a full-page screenshot with text made transparent **without hiding
the background decoration**. It samples 20 interior pixels behind each node
and records the lowest and highest foreground/background contrast estimates.

Compare with WCAG 2.2 AA text criteria: 4.5:1 normal, 3:1 large or bold.
The collector flags cases whose minimum estimate falls short. It marks text
gradients, opacity and unsupported colours manual-only. It never asserts
conformance: text boxes can contain whitespace, nested differently coloured
text, overlays, patterns and moving backgrounds. The minimum sampled pixel
may not be exactly under a glyph.

Each scan records selector, excerpt, computed style, the worst sampled colour
and coordinate, ratio, and separate uncertainty notes.

## Reproduce
Run the local demo, then install Playwright, Chromium, Pillow and axe-core:

    python3 -m http.server 8765 --bind 127.0.0.1
    python3 -m pip install playwright==1.56.0 Pillow
    python3 -m playwright install chromium
    npm install --no-save --no-package-lock axe-core@4.10.3
    python3 scripts/audit_rendered_contrast.py

Artifacts: quality-results/visual-contrast/report.json and summary.json.

## Follow-up decisions
1. Inspect highest-risk foreground/background pairs visually.
2. Confirm colour pairing and pixel position before altering any theme.
3. Fix real failures in the theme's owning CSS. Do not enforce a common
   appearance or simply hide elements from the evaluator.
4. Rerun official W3C CSS, the existing axe checks and responsive browser tests.
5. Keep Issue #8 open until every incomplete category is reviewed.

This collector is an audit aid, NOT a new pass/fail quality gate.
