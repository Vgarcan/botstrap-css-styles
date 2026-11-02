# Neon Coast — Boulevard Component System (V2 visual pilot)

## Contents
1. Review trigger and problem statement
2. Real design references and principles
3. Boulevard visual system
4. Component-by-component contract
5. Non-goals and accessibility boundaries
6. Test plan and merge gate

## 1. Review trigger

Following merge of PR #13, user feedback (2026-11-02): **"el cambio ha sido mayormente del fondo.... pero los detalles del tema siguen igual... me falta cuerpo en el estilo"**.

This is a **valid unresolved art-direction issue**, not a request to intensify the coastal background. The original scene, palette and baseline visual contrast are accepted; components were still largely uniform legacy neon borders.

Hypothesis to test: a recurring but varied set of **marquee sign caps, sunset bands, poster frames and recessed console controls** gives Neon Coast an identifiable component language throughout a Bootstrap page, even without the hero.

## 2. References studied

| Source | Medium | Evidence / extracted design principle | Implementation choice |
| --- | --- | --- | --- |
| [Horizon Drive landing design](https://www.behance.net/gallery/57289207/Landing-Page-%2880s-style%29) | Behance visual concept | Broad display typography, strong star/triangle framing, dramatic focal hierarchy | Larger editorial section headings and restrained ornamental bands (no cloned assets) |
| [Supernova Nightclub](https://www.behance.net/gallery/87537437/Daily-UI-005-80s-Nightclub-Website) | Behance visual concept | Graphic script/display hierarchy, low horizon, bold all-caps accents | Display-first headline hierarchy, not all-caps on paragraph/fields |
| [Retrowave / Newwave mobile UI kit](https://de.brusheezy.com/bursten/67540-retrowave-ui-kit-newwave-ui-mobile-kit) | Static graphic/UI kit, not verified production site | Rounded fluorescent CTAs, dark recessed fields, compact neon chrome | Capsule buttons, sunlit top edges, inset form controls and small metadata-like capsules |
| [Dylan Bartoli Synthwave Portfolio](https://www.awwwards.com/sites/dylan-bartoli) | Gallery of web portfolio | Structural neon lines are used as accents, typography/readability are separated | A small colored line signature on cards and headings, no page-wide continuous glowing borders |
| [Synthwave style analysis](https://stylogeny.com/styles/synthwave-outrun/) | Design-history explainer | Display typography, symmetric focal points, fluorescent color and geometric primitives | The page has a recurring sunset/louver motif, but different components use it differently |

These are references for **analysis**, not licensed art assets. The actual CSS is original and authored for our Bootstrap gallery. Do not automatically infer that any Behance design has been tested for accessibility or real responsive behavior.

## 3. Boulevard design language

### Surfaces and material
- Page: existing coastal-night artwork, kept unchanged.
- Cards: dark-purple poster frames with compact top sunset strip and subtle physical elevation.
- Hero preview: stronger poster frame, not a plain glowing box.
- Forms/menus: matte, recessed cassette-console surfaces, not glass tiles.

### Typography
- Orbitron or existing theme-retro font only where it reinforces interface hierarchy: headings, CTA labels, card header, tabs.
- Inter for paragraphs, form entry, dropdown menus and tables.
- Section heading uses **three horizontal sunset louver bars** plus a tight underline instead of glowing every character.

### Shapes
- Capsule buttons and badges, rounded card frames, cassette tabs, recessed input wells.
- Unlike Cyberpunk Hardline's industrial cut-corner panels, the silhouette is smooth, playful, and poster-like.
- Make each surface role legible through its thickness, border, material and focus state—not only through color.

### Color roles
- Magenta/orange: main CTA and sunset accent strip.
- Cyan: keyboard focus and secondary interaction.
- Cream/warm white: display typography.
- Purple/night: card surfaces.
- Success/warning/destructive: distinct semantic states; do not rely solely on hue.

## 4. Component mapping

| Shared Bootstrap component | Boulevard system |
| --- | --- |
| Navbar | Neon-sign plinth, gradient bottom strip, understated link capsules |
| Hero preview | Raised poster/card, subtle colored frame, sunset stripe |
| Cards | Poster frame with top strip and header louver detail |
| Buttons | Warm raised capsule primary, cyan night capsule secondary and proper semantic variants |
| Section titles | Display-heading motif made of three horizontal bars and horizontal rule |
| Forms | Dark inset wells, chromed labels, distinct cyan keyboard focus |
| Tabs/pills | Recessed cassette deck with active warm-gradient cartridge |
| Tables | Film-strip headings, structured row hover and readable cell copy |
| Alerts/progress/badges | Ticket-edge alerts, sunset meters and compact capsules |
| Accordion/modal/offcanvas/dropdown | Matching night-console material with clear state changes |

## 5. Boundaries and cautions

- Only `themes/retrowave-synthwave.css` is modified in production source.
- `index.html`, theme switching JS, other theme CSS, the 13 semantic `--theme-*` contract, original `--retro-*` palette, and the entire generated responsive core are unchanged.
- The coastal SVG data URI remains byte-identical.
- All enhancements are static CSS; no new JS, animations or third-party art.
- Avoid rebranding *every* component with the same glow/gradient. Accent intensity follows hierarchy.
- A browser visual review is necessary because Bootstrap + generated core can override theme-specific spacing and interactions.

## 6. QA and approval

1. Verify W3C CSS, token contract and generated responsive-core drift checks.
2. Confirm tests for all 17 themes; no overflow at 320/375/390/430/768/1024/1280/1440 px.
3. Check computed contrast and focus for tabs, offcanvas, modal, forms and nav.
4. Compare before/after real Chromium screenshots at 1440, 768 and 390 px, including mobile nav.
5. Inspect component sections (cards, tables, form and accordion), not just the top of the page.
6. Iteratively adjust visual details based on user review; **do not merge until user explicitly approves this iteration**.
7. Consolidate redundant legacy component overrides *after* visual approval, with screenshot-equivalence testing.

**Status:** exploratory V2 component styling, intentionally separate from already-merged Neon Coast background.
