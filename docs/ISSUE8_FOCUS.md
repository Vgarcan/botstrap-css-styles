# Issue #8 — Visible keyboard focus and non-text contrast

## Contents
1. Requirement and defect
2. Implementation and integration
3. Automated evidence
4. Remaining manual review

## 1. Requirement and defect
WCAG 2.2 AA requires visible keyboard focus (2.4.7), focus not entirely
obscured (2.4.11), and contrast of essential non-text user-interface
state indicators (1.4.11). The previous single-colour focus outline used
\`--theme-accent\`; it could disappear against a gradient, glass panel, or
theme-specific control background.

## 2. Implementation and integration
\`scripts/responsive-core.css\` now contains a two-tone \`:focus-visible\`
indicator: 3px ink outline (#101827) and a 6px white halo. White and ink
contrast strongly with each other, so at least one ring edge remains
perceptible against light and dark surfaces. The indicator is restricted
to focus-visible keyboard interactions; normal theme hover/colour rules
are preserved. Forced-colours users receive the operating system's
\`Highlight\` colour instead of hard-coded shadow rings.

The shared source is **generated into all 18 non-empty standalone theme
CSS files**, preserving single-file integration in Django and static HTML.

    python3 scripts/sync_responsive.py --check

## 3. Automated evidence
\`scripts/test_focus_accessibility.py\` tests 17 selectable themes at 390,
768 and 1440px. It opens the Settings tab to inspect real input and checkbox
focus and opens the mobile offcanvas to inspect close/navigation links.
Checks cover computed focus-visible style, focus presence, in-viewport
geometry and whether the element centre is entirely obscured. Results and
sample screenshots are archived as the GitHub Actions \`focus-evidence\` artifact.

Official W3C CSS validation, the axe-core text contrast gate, and responsive
browser tests continue independently. A green focus test is not full WCAG
certification; non-text contrast is not fully automated by axe-core.

## 4. Still requires inspection
- Borders and functional icons (particularly radio, checkboxes, arrows and
  form validation) at 3:1 against adjacent surfaces.
- Focus in scrollable tab strips, popups, modal overlays, dropdowns and tooltips.
- Keyboard-only traversal; Windows forced-colours; 200%/400% zoom.
- Chrome for Android, Safari for iOS and real tablet portrait/landscape.
- All \`axe incomplete\` gradient, image and transparent-text cases.
Keep GitHub Issue #8 open until these have recorded evidence.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast
- https://www.w3.org/WAI/WCAG22/Understanding/focus-visible
- https://www.w3.org/TR/WCAG22/#focus-not-obscured-minimum
