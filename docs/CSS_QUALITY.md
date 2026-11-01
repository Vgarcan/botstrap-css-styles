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
The initial audit intentionally only reports results. A successful audit job
means it executed; it does not mean that the CSS is valid or accessible.
Review all errors and axe incomplete findings (especially gradients, glass
panels and background images). Do not suppress violations to force a green CI.
After remediation, turn reports into failing quality gates.
Include focus states, tab panels, forms, menus, modals, mobile and tablet
in the follow-up accessibility audit.

References:
https://www.w3.org/TR/WCAG22/#contrast-minimum
https://www.w3.org/TR/WCAG22/#non-text-contrast
https://jigsaw.w3.org/css-validator/DOWNLOAD.html.en
