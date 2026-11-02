# Cyberpunk Neon 2.0 — visual research and design brief

## Contents
1. Scope and evidence
2. Reference studies
3. Common design grammar
4. Current theme audit
5. Candidate art directions
6. Proposed pilot and component specifications
7. Architecture and accessibility
8. Acceptance criteria and next decision

## 1. Scope and evidence

Research-only preparation for a future Cyberpunk Neon redesign. This is **not** approved production styling. Study real web implementations and designer case studies before making visual changes.

Separate **observed design characteristics** from **our interpretation**. Do not copy logos, proprietary assets, game interface screens or brand-specific visual identity. Preserve standalone CSS, the common theme contract and the shared generated responsive rules.

## 2. Reference studies

| Source | Kind | Evidence / principle to learn | Caution |
| --- | --- | --- | --- |
| [CD Projekt RED: four visual styles](https://www.cyberpunk.net/es/news/28465/c-usb-01-backup/concept-art/cp-visual-styles) | Official design language; use canonical alternative [here](https://www.cyberpunk.net/es/news/28465/c-usb-01-backup-concept-art-cp-visual-styles) | Entropism, kitsch, neomilitarism and neokitsch can coexist; the theme does not require a rainbow palette | These are fictional-world aesthetics, not direct Bootstrap UI specifications |
| [Cyberpunk.net](https://www.cyberpunk.net/us/en/) | Live official site | Branding, strong editorial blocks, navigation hierarchy and embedded news modules | Avoid imitating distinctive proprietary branding |
| [Vladimír Vilimovský UI studies](https://www.behance.net/gallery/133185623/Cyberpunk-2077User-Interface-%28Part-2%29) | Professional UI concept/production portfolio | Consistent visual blueprint; aggressive red can be a *base* colour, not only an error colour | Keep form-status semantics legible in everyday web UI |
| [Michael Rigley / MFR](https://www.michaelrigley.com/work/cyberpunk-2077/) | Art-direction concepts | UI should have a coherent system: layout, title treatments, framing, hierarchy | Reference only, no reproduction |
| [Dopamine Studio: Cyberpunk Redone](https://www.dopaminestudio.io/project/cyberpunk-redone) and [live experiment](https://cyberpunkredone.webflow.io/) | Real interactive web prototype | Hard beveled HUD frames, CRT-inspired scanline texture, terminal language and interactions that behave like a system | Do not apply scanlines/glitches to all reading text |
| [Neon Nexus](https://www.mirnesa.me/projects/neon-nexus/index.html) | Web design case study | Reading UX can coexist with dark neon; Orbitron for headings and a more legible text face for interface copy | A concept case study is not blanket proof of WCAG compliance |
| [Origamix by Bachoo](https://bachoodesign.com/portfolio/origamix/) | Real commissioned web design case | Neon signs + retro futurism require careful contrast of visually loud and quiet regions | Avoid ornamental overload |
| [Cyberpunk web inspiration by Wendy Zhou](https://www.wendyzhou.se/blog/cyberpunk-ui-website-design-inspiration/) | Curated web UI analysis | Clipped corners and terminal typography can communicate cyberpunk with less excessive decoration | Curated examples include both real sites and concept designs |

## 3. Common design grammar — findings

**Geometry**
- Chamfered/diagonal corners, asymmetrically cut panels, segmented border rails and precise corners instead of rounded glass bubbles.
- Layered editorial grids, panels of unequal visual weight, thin coordinate/ruler patterns used sparingly.
- Deliberate separation of content structure from decorative telemetry.

**Colour and contrast**
- Near-black graphite and blue-black are a useful canvas, not a mandatory all-black background.
- Reserve bright neon for functional highlights, active states, select borders and focal text.
- Use one primary luminous accent and one secondary contrasting accent; treat additional colours as semantic/status colours rather than equal-weight decoration.
- Red/pink are not automatically errors: semantic meaning must also come from icons, labels, position and patterns.

**Typography**
- Heading typography may be condensed, technical or display-specific; sustained paragraph text must remain easy to read.
- Labels, coordinates and status readouts can use monospace, uppercase and tracking.
- Avoid universal uppercase/tracking on all body copy.

**Motion**
- Glitch, flicker, scanline, cursor trails and boot states are motifs, not requirements.
- Prefer short, contextual states and reversible effects. Never shake interactive controls, prevent form completion or obscure text.
- Honour reduced-motion preferences; avoid constant global scanning lines.

## 4. Audit of `main/themes/cyberpunk-neon.css` (2026-11-02)

Observed in the theme-owned block before `BEGIN RESPONSIVE CORE v1`:
- 20 `animation:` declarations, five `@keyframes` blocks, approximately 46 `box-shadow:` declarations.
- Shared body and UI typography uses Orbitron with a Courier fallback.
- Persistent `body:before` scanning line every three seconds.
- Button and card hover states invoke glitch/flicker and spatial transforms.
- Black background with a uniform 20px cyan grid, fully saturated cyan/magenta/green/orange accents and frequent luminous outlines.
- Core semantic 13 `--theme-*` tokens are present.
- The generated shared responsive core starts at the recorded marker and must never be hand-edited.

**Interpretation:** The current visual style strongly signals the genre but distributes neon and motion too evenly. It lacks clear quiet/loud hierarchy, typographic contrast and distinctive structural geometry. The theme is an appropriate candidate for a CSS-first art-direction pass.

## 5. Candidate art directions (not yet selected)

| Direction | Character | Advantages | Risks |
| --- | --- | --- | --- |
| Neon Underground | Night signage, magenta/cyan, light pollution and distressed elements | Immediately recognizable cyberpunk, high energy | Can resemble generic retro gaming and lose content readability |
| Neo-Military Interface | Technical red, graphite, precise hard-edged frames, segmented labels | Strong system discipline and sharp visual signature | Can overfit a specific game's aesthetic, feel sterile or imply error status |
| Industrial Neon (proposed hybrid) | Near-black graphite + cyan, selective hot coral/magenta, amber and precision-cut geometries | Retains the project's Neon identity with stronger composition and readability | Requires disciplined contrast and careful restraint to avoid flat dashboards |

## 6. Initial pilot for review — Industrial Neon

This is a *hypothesis*, not a user-approved final design.

- **Canvas**: multi-level graphite and blue-black with a faint technical grid confined to the hero/feature area, not the entire document.
- **Hero**: dominant high-contrast editorial headline, left-aligned informational hierarchy, one bright signal panel and carefully designed frame segments.
- **Cards**: segmented top edge, one chamfered corner or asymmetrical cut, two variants (signal/quiet). Depth from dark surfaces and bounded reflections, **not glass blur**.
- **Buttons**: crisp solid primary action, outlined secondary action. Clear focused and disabled states. No glitch on every hover.
- **Navigation/tabs**: tab strips remain stable and scroll horizontally on small screens through the generated shared core.
- **Forms/modal/alerts**: utilitarian readability; alerts have real semantic distinctions; subtle visual motifs are secondary.
- **Palette prototype** (illustrative; not validated as a final colour system):
  - canvas #090D13
  - surface #111A24
  - elevated surface #19232D
  - primary neon cyan #4BE9E3
  - secondary signal coral #FF5476
  - caution amber #F5C65B
  - base text #E8F2F6
  - muted text #9DB1BE
- **Typography**: consider Rajdhani / condensed sans for headlines; a legible humanist sans for paragraphs; monospace only for system metadata. Verify asset loading and fallbacks.
- **Geometry**: `clip-path: polygon(...)` for purely decorative layers only when keyboard focus and borders survive clipping. Pseudo-elements for accents where safer.

## 7. Architecture and accessibility

Maintain:
- 13 `--theme-*` semantic tokens (stable names and order).
- Current `--neon-*` legacy tokens unless intentionally migrated with compatibility.
- One standalone downloadable `themes/cyberpunk-neon.css` with no JS dependency.
- Shared `js/theme-core.js` unchanged until a genuinely useful theme interaction is specified.
- Optional `themes/cyberpunk-neon.js` only for a user-visible, purposeful enhancement with synchronous cleanup; if unused, do not create it.
- Generated responsive core untouched; focus/contrast tests, mobile-first widths, touch controls and reduced motion intact.

## 8. Acceptance criteria and next decision

Before visual implementation:
1. Review these references and select the stylistic mix (Underground, Neo-Military, Industrial Neon or a new direction).
2. Approve a composition strategy (hero + card + form + mobile navigation), **not just a colour palette**.
3. Implement a CSS-only, testable pilot on a separate branch; no merge until screenshot review.
4. Check all 17 themes at established breakpoints and verify theme-switching cleanup; run W3C/contrast/focus checks.
5. Compare before/after screenshots at 1440px and 390px with the same page content.

Status: **research complete; art direction remains a proposal; no theme code changed**.
