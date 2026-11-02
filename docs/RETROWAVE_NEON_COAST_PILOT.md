# Retrowave Synthwave 2.0 — Neon Coast CSS pilot

## Contents
1. Design identity and user choice
2. Embedded coastal scene
3. Bootstrap compatibility
4. Visual testing
5. Review and acceptance

## 1. Design identity and user choice

**Approved exploration direction:** Neon Coast (option B), rather than Sunset Highway or Cosmic Arcade.

The user wants to preserve the theme's existing vivid pink, cyan, violet, orange and yellow while giving its background a richer, more authentic synthwave visual narrative.

The new composition uses a layered, static violet/magenta sky, a horizontally-banded amber/pink sun, distant coastal mountain/city silhouettes, silhouetted palms and reflective water. The look emphasizes a late-night Miami coast, not an endless Outrun grid or Cyberpunk Hardline's industrial machinery.

The original `--retro-*` values remain unchanged in this first pilot. Non-background components receive targeted legibility fixes but remain recognizable.

## 2. Embedded coastal scene

**Source of truth for illustration:** `docs/RETROWAVE_NEON_COAST_SCENE.svg` (original authored vector artwork).
**Runtime:** a percent-encoded copy of the SVG is embedded as the `--coast-scene` value inside `themes/retrowave-synthwave.css`, so the theme remains a downloadable standalone CSS file. External images, JS, requests and additional asset paths are **not** required.

To edit scene geometry:
1. Change the documented SVG artwork.
2. Percent-encode the entire updated SVG and replace the data URI of `--coast-scene` in CSS. Keep both identical.
3. Inspect screenshots at 390px, 768px and 1440px to ensure correct placement.
4. Check CSS validity and reduced-motion behavior.

Design/composition:
- The scenic background is applied to the existing `#home` section of `index.html` without changing HTML.
- General page background is a subtle dark purple gradient for stable content readability.
- A left-to-right dark scrim helps hero text remain legible against the sunset.
- For narrow phones, the scene shifts toward the sun and horizon, and the dark scrim is stronger.
- The first desktop screenshot exposed a composition error: the scene's rasterized sun was blocked by the right-hand preview card. A CSS masked sunset disc now occupies the open upper-right sky, while the original vector horizon remains behind the card. On mobile the extra disc is hidden to avoid duplication and the original vector scales to 86% height.
- Static art is the default; no animations or theme-specific JS required.

## 3. Bootstrap compatibility

- Only `themes/retrowave-synthwave.css` is modified among production sources. `index.html`, `js/theme-core.js`, `scripts/responsive-core.css` and all 16 other selectable themes remain untouched.
- **All 13 standard semantic CSS tokens** remain defined, in their original names and order.
- The entire generated Responsive Core v1 section is byte-for-byte identical to `main`.
- Standalone CSS is used after Bootstrap 5.3; themed content can run without `#home` (background falls back to ambient purple).
- Existing public `--retro-*` palette and specialty utility names remain available.
- Focus, form text, table color variables and motion are brought under control for the richer scenic background.

## 4. Visual testing

Required before considering any release:
- GitHub CI static checks for W3C, token contract and responsive-core parity.
- Browser checks for all 17 themes, viewport scroll and interactive controls.
- Contrast/focus checks across cards, tables, navigation, tabs, modal and offcanvas.
- Screenshot inspection at 1440px / 768px / 390px (closed/open offcanvas) and comparison with baseline.
- No broken download and no JS dependency for the scene.

## 5. Review and acceptance

Status: **draft visual pilot**, not ready for `main`.

The illustration is deliberately elaborate but should not overwhelm the standard Bootstrap hero and other components. Review the landscape's placement and intensity before refining typography, motion and secondary components. Consolidate any redundant overwritten legacy rules only after visual approval and screenshot equivalence.
