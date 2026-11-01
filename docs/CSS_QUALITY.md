# CSS quality audit — baseline

## Contents
1. Requirements
2. Tools
3. Execution
4. Interpretation and limitations

## Requirements
Target WCAG 2.2 AA: text 4.5:1, large text 3:1, essential UI components 3:1.
CSS syntactic validity and visual accessibility are independent requirements.

## Tools
Official W3C CSS Validator (2025-02-26 release), run on 18 nonempty CSS files.
The excluded corporate-blue.css is an empty, unselected placeholder.
Axe-core 4.10.3 scans all 17 selectable themes at widths of 390 and 1440px
inside Chromium, with the actual Bootstrap and gallery styles.

## Execution
Download the official css-validator.jar from
https://github.com/w3c/css-validator/releases/tag/cssval-20250226
then run: python3 scripts/audit_css_w3c.py /path/to/css-validator.jar

For contrast, start: python3 -m http.server 8765
Install Playwright 1.56.0, Chromium and axe-core 4.10.3, then run:
python3 scripts/audit_contrast.py

Reports are uploaded as GitHub Actions artifacts and saved under
quality-results/css and quality-results/contrast.

## Interpretation
The W3C CSS validator now enforces validity for all 18 populated stylesheets.
The axe-core contrast audit is now an enforcing CI gate for confirmed text
contrast violations across 17 themes at mobile and desktop widths. However,
axe incomplete findings are still unresolved and require manual inspection.
Review all errors and axe incomplete findings (especially gradients, glass
panels and background images). Do not suppress violations to force a green CI.
After remediation, turn reports into failing quality gates.
Include focus states, tab panels, forms, menus, modals, mobile and tablet
in the follow-up accessibility audit.

References:
https://www.w3.org/TR/WCAG22/#contrast-minimum
https://www.w3.org/TR/WCAG22/#non-text-contrast
https://jigsaw.w3.org/css-validator/DOWNLOAD.html.en

## Interactive states
The separate states-report.json baseline checks Profile, Contact and Settings
tabs, the open modal, and the open navigation drawer for every theme at 390px.
It is report-only pending remediation. The regular default-state contrast
check is enforcing. Mobile drawer screenshots are attached for manual QA.

## Undefined CSS variables
Run `python3 scripts/verify_css_references.py`. All populated theme files
must resolve their local `var(--name)` references; Bootstrap `--bs-*`
variables are upstream and therefore excluded from this standalone check.

## Manually evaluated gradient endpoints
Some gradients are marked `incomplete` by axe even when the colours are
known. We explicitly checked these endpoints using relative luminance:
- Art Deco: cream text on emerald `#50c878` is only 1.92:1; we now use
  dark ink. Cream on ruby `#e0115f` is 4.30:1; we now use white.
- Kids Friendly: white text on the sky gradient `#87ceeb` is 1.74:1;
  the pastel gradients now use dark ink on active tabs/pills/accordions.
- Kids Vibrant: the magic/ocean gradients mix light cyan with dark purple;
  functional active pills/accordion headers now use solid violet and white.

These targeted fixes do not establish conformance for **all** incomplete
backgrounds. Those still require explicit component-by-component review.
