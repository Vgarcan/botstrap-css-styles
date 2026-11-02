# Cyberpunk Neon 2.0 — Hardline pilot (Signal District origin)

## Contents
1. What we borrowed from research
2. Visual decisions
3. Compatibility and change boundaries
4. Test matrix
5. Open design questions

## 1. What we borrowed from research

Hardline is the visually selected direction, evolving from the Signal District pilot. This implementation translates the [initial research](CYBERPUNK_NEON_RESEARCH.md) and [six further reference families](CYBERPUNK_NEON_REFERENCES_02.md) into a standalone Bootstrap CSS skin. The user selected **Hardline** over Signal District after reviewing identical desktop and mobile screenshots. Selection approves the art direction, **not an automatic merge**.

| Reference family | Extracted principle | Pilot translation |
| --- | --- | --- |
| Neo-Tokyo editorial | Bold composition, large condensed-feeling type and sharp contrast | Strong title hierarchy and asymmetric technical rails in the common gallery hero |
| Deus Ex-inspired instrumental | UI elements appear engineered, not floating | Dark steel panels, signal-line borders, segmented navigation, restrained elevation |
| RUINER / underground | One deliberate hot accent is stronger than five competing glows | Restrained coral signal accents and a cyan primary action |
| Terminal cybernetics | Tiny metadata and precise arrangement communicate machine-like intent | Typography separation: Orbitron display headings, Inter body copy and controls |
| Atmospheric dystopia | Localized ambience can make a simple page feel like a place | Static radial light and a low-opacity technical grid |
| Accessibility / reusable UI | Form/content usability is more important than decorative glitch | No global scanline, no card-shaking, no automatic terminal animation |

## 2. Visual decisions

**Selected visual direction:** Hardline. The feature branch keeps its original Signal District name for traceability.

- Graphite canvas `#0b1017` and midnight steel surface `#17232f`, with cyan `#63ede2` and coral `#ff476f`, plus amber `#f2c46b` for warning.
- Ordinary copy uses off-white and cool grey instead of neon cyan.
- Preserve recognizable dark cyberpunk personality while improving optical hierarchy and reading comfort.
- The hero uses CSS-only framed geometric decoration; the gallery's HTML is unmodified.
- No mandatory images or JavaScript. `cyberpunk-neon.js` intentionally does not exist.
- Preserve legacy utility class names `.neon-text`, `.glitch-effect` and `.matrix-bg`; make decorative motion opt-in and safe.
- The large hero showcase card has a decorative beveled silhouette. Buttons and text are inset; actual focusable controls are not clipped.
- Hardline adds strong cyan editorial title plates, red/coral section rails and an asymmetric decorative system label. The label is illustrative, never live system data.
- The design is intentionally **not** Glassmorphism: no `backdrop-filter` material on cards.

## 3. Compatibility and change boundaries

- `themes/cyberpunk-neon.css` is the **only production source** modified.
- The 13 names of the semantic `--theme-*` contract stay in their existing root declaration. Private pilot settings use `--cyber-*` variables.
- Public `--neon-*` variable names stay defined; their values change as part of the visual redesign.
- The generated `/* BEGIN RESPONSIVE CORE v1 ... */` to `/* END RESPONSIVE CORE v1 */` block is byte-for-byte unchanged.
- `scripts/responsive-core.css`, `index.html`, all 16 other theme CSS files and `js/theme-core.js` are untouched.
- The final CSS remains a single downloadable file working with Bootstrap 5.3, without a runtime JS module.
- The 13 semantic aliases, legacy public tokens, and all private `--cyber-*` tokens are consolidated in a **single leading `:root`**. The visual overrides remain in a named section after the original component declarations, which protects experimental visual behavior during comparison.
- **Completed cleanup (commit `63b4e9a`):** removed 267 legacy declarations that were superseded by matching Hardline selectors, across 89 legacy selector blocks. Theme CSS decreased from 50,620 to 40,377 bytes (10,243 bytes removed). The approved Hardline override section and generated responsive core are byte-for-byte unchanged.
- Only exact-selector, exact-property replacements with suitable `!important` priority were removed; declarations providing still-needed Bootstrap behaviour remain. The remaining legacy compatibility rules are intentionally retained, rather than rewriting the whole theme.
- The next safeguard is identical screenshot comparison at 1440px, 768px, 390px and mobile-navigation-open, followed by automated contrast/focus and theme-switch checks. Any difference must be inspected before release.

## 4. Test matrix

Check current CI status for:
- W3C validity for all 18 non-empty stylesheets.
- Semantic-token checks, local variable resolution and generated responsive-core drift.
- 17-theme gallery navigation, stable CSS switching and 320/375/390/430/768/1024/1280/1440px widths.
- Axe contrast and focus on cards, alerts, forms, tables, tabs, modal, offcanvas and mobile navigation.
- CSS-only rendering, no cyberpunk JS module fetch or leaked module state.
- Inspect generated screenshots (1440px and 390px) and compare against `main`.

Do not assert full WCAG conformance from passing CI.

## 5. Remaining quality checks
6. Refactor verification record

1. Compare unchanged markup before/after root-token consolidation at desktop and phone sizes.
2. Ensure no horizontal clipping or obscured keyboard focus from clipped decorative card edges.
3. Inspect representative Bootstrap components beneath the hero, not only the initial viewport.
4. Preserve inherited responsive rules and all other theme appearance during future cleanup.
5. Keep the current Hardline palette and geometry unless a functional/accessibility issue warrants a targeted fix.

**Status:** Hardline visual direction selected by the user. CSS refactor and validation in feature branch; keep PR in draft until final technical review and explicit merge approval.

## 6. Refactor verification record

- **Scope:** only `themes/cyberpunk-neon.css` changed; no shared HTML, JS, generated responsive rules or other theme files modified.
- **Technique:** eliminate redundant declarations in the original component rules only when the same selector/property is redeclared in Hardline at compatible cascade priority. Existing partial rules and all other declarations remain.
- **Integrity checks:** exactly 13 semantic `--theme-*` tokens, single leading `:root`, unchanged Hardline visual rules, unchanged generated responsive core.
- **Visual review:** compare screenshots after the CSS cleanup against the prior approved Hardline version. If screenshots differ, revert or adjust targeted removals before considering merge.
