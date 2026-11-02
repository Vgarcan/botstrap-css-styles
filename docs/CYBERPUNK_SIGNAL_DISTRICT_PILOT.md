# Cyberpunk Neon 2.0 — Signal District pilot

## Contents
1. What we borrowed from research
2. Visual decisions
3. Compatibility and change boundaries
4. Test matrix
5. Open design questions

## 1. What we borrowed from research

This pilot translates the [initial research](CYBERPUNK_NEON_RESEARCH.md) and [six further reference families](CYBERPUNK_NEON_REFERENCES_02.md) into a standalone Bootstrap CSS skin. It is a hypothesis to review, **not** a locked design identity.

| Reference family | Extracted principle | Pilot translation |
| --- | --- | --- |
| Neo-Tokyo editorial | Bold composition, large condensed-feeling type and sharp contrast | Strong title hierarchy and asymmetric technical rails in the common gallery hero |
| Deus Ex-inspired instrumental | UI elements appear engineered, not floating | Dark steel panels, signal-line borders, segmented navigation, restrained elevation |
| RUINER / underground | One deliberate hot accent is stronger than five competing glows | Restrained coral signal accents and a cyan primary action |
| Terminal cybernetics | Tiny metadata and precise arrangement communicate machine-like intent | Typography separation: Orbitron display headings, Inter body copy and controls |
| Atmospheric dystopia | Localized ambience can make a simple page feel like a place | Static radial light and a low-opacity technical grid |
| Accessibility / reusable UI | Form/content usability is more important than decorative glitch | No global scanline, no card-shaking, no automatic terminal animation |

## 2. Visual decisions

**Working name:** Signal District (pilot only).

- Graphite canvas `#0b1017` and midnight steel surface `#17232f`, with cyan `#63ede2` and limited coral `#ff6a85`, plus amber `#f2c46b` for warning.
- Ordinary copy uses off-white and cool grey instead of neon cyan.
- Preserve recognizable dark cyberpunk personality while improving optical hierarchy and reading comfort.
- The hero uses CSS-only framed geometric decoration; the gallery's HTML is unmodified.
- No mandatory images or JavaScript. `cyberpunk-neon.js` intentionally does not exist.
- Preserve legacy utility class names `.neon-text`, `.glitch-effect` and `.matrix-bg`; make decorative motion opt-in and safe.
- Avoid `clip-path` on actual interactive elements, because clipped control focus outlines could disappear.
- The design is intentionally **not** Glassmorphism: no `backdrop-filter` material on cards.

## 3. Compatibility and change boundaries

- `themes/cyberpunk-neon.css` is the **only production source** modified.
- The 13 names of the semantic `--theme-*` contract stay in their existing root declaration. Private pilot settings use `--cyber-*` variables.
- Public `--neon-*` variable names stay defined; their values change as part of the visual redesign.
- The generated `/* BEGIN RESPONSIVE CORE v1 ... */` to `/* END RESPONSIVE CORE v1 */` block is byte-for-byte unchanged.
- `scripts/responsive-core.css`, `index.html`, all 16 other theme CSS files and `js/theme-core.js` are untouched.
- The final CSS remains a single downloadable file working with Bootstrap 5.3, without a runtime JS module.
- Pilot edits are currently consolidated in a named override section after the legacy theme rules to allow safe comparison. **Before release**, inspect redundant overridden declarations and simplify only if screenshot/contrast evidence shows equivalence; do not blindly collapse the stylesheet.

## 4. Test matrix

Check current CI status for:
- W3C validity for all 18 non-empty stylesheets.
- Semantic-token checks, local variable resolution and generated responsive-core drift.
- 17-theme gallery navigation, stable CSS switching and 320/375/390/430/768/1024/1280/1440px widths.
- Axe contrast and focus on cards, alerts, forms, tables, tabs, modal, offcanvas and mobile navigation.
- CSS-only rendering, no cyberpunk JS module fetch or leaked module state.
- Inspect generated screenshots (1440px and 390px) and compare against `main`.

Do not assert full WCAG conformance from passing CI.

## 5. Questions for visual review

1. Does the hero feel editorial enough while still looking like a reusable theme?
2. Are cyan and coral distributed deliberately or still too evenly?
3. Is the contrast between surface levels and the card geometry expressive enough?
4. Does mobile preserve a strong personality without overlap or cramped type?
5. Would a second iteration benefit more from selective material contrast, geometry, or a bespoke optional JS enhancement?

**Status:** CSS pilot staged on feature branch. No merge without visual approval.
