# Issue #8 — First measured contrast repairs

## Contents
1. Source of evidence
2. Repairs
3. Non-claims and remaining work

## Evidence
Source: CI artifact `issue8-rendered-contrast` from PR #9 baseline.
34 viewport/theme scans (17 themes at 390px and 1440px) sampled 2,246
candidate elements, marking 796 for review and 24 manual-only. These counts
are not unique WCAG violations: rectangles include background pixels not
necessarily directly behind glyphs, and text gradients need human inspection.

The new audit is a triage layer alongside the official W3C validator and
axe-core. We only change CSS when the underlying colour pairing is clearly
low-contrast, not because an estimated count is nonzero.

## Repairs

- **Modern Gradient**: primary gradient starts at #5366c1 for 5.2:1 white
  contrast; formerly #667eea was just 3.66:1. Brighter status gradients
  switch to ink #142238 with minimum endpoint ratio 4.65:1.
  Previously transparent Bootstrap-5 badge aliases now have actual coloured
  backgrounds and readable text. Primary alerts use a pale surface.
- **Kids Friendly**: pale blue/mint/yellow/pink gradients retain their
  colours, but primary/secondary buttons, card headings and progress labels
  switch from white to dark #172334. Sky gradient's worst white ratio was
  about 1.27:1, versus at least 9:1 for this ink over its endpoints.
- **Neumorphism Soft**: darken only the raised violet functional gradient
  (white contrast >=5.19:1 at endpoints). Mint, gold and coral actions
  keep the soft colour but use dark ink, minimum recorded endpoint 4.8:1.
- **Glassmorphism Pro**: the white text + translucent-white frosted glass
  against the former pink gradient cannot reliably meet AA. A navy
  overlay darkens the same underlying purple/pink gradient while
  keeping the frosted-glass character.

Endpoint calculations use the standard sRGB luminance formula on opaque
gradient stops. These checks are valuable, but overlays, composited alpha,
hover animation and intermediate pixel positions still require browser QA.

## Scope and remaining work
This is the **first remediation batch**, not completion of Issue #8.
W3C CSS and axe confirmed-violation gates are mandatory on every PR.
The screenshot-pixel classifier is *not* an enforcing gate because it is an
estimate and can flag false positives, especially nested or clipped text.

Other themes and unfinished categories (contrast of focus borders, SVG/icon
graphics, gradients and textured overlays, modal, offcanvas, disabled states,
Safari/Android devices) remain open and must not be described as certified.
