# Neumorphism 2.0 — Mineral Graphite (tactile hybrid pilot)

## Contents
1. Direction and intent
2. Physical surface rules
3. Component mapping
4. Architecture and implementation
5. Test plan and release gate

## 1. Direction

The user liked direction **B Warm Mineral** for its color and **C Soft Elastomer** for its elegance. The hybrid uses **C as its structural material** (deep graphite soft-touch polymer, precise pressed controls and grounded weight) while importing **B selectively as warm ivory / mineral edging and touches of copper/peach**.

This is **not** a 50/50 mix of full-page beige and technical rubber. It should feel like an expensive hand-held audio interface with a warm ceramic inlay: quiet, physical, contemporary, and not another purple neon dashboard.

## 2. Physics of the surface

- One dominant upper-left light source throughout the page.
- Raised objects cast a **small dark contact shadow** plus a broader diffuse shadow; a subtle upper-left light catches their edge.
- Recessed inputs and active tabs use a **sharper inset shadow**, with the opposing edge lit. Keyboard focus is indicated independently using a visible warm outline/ring.
- A deliberately fine, embedded 160px SVG fractal noise tile adds micrograin on the **substrate only** via `background-blend-mode: soft-light`; the component foreground text is always clean.
- Decorative imprinted dots by section titles recall the user's Braille-like relief interest, but are **not Braille text** and encode no information.
- Cards and accordions no longer bob or pulse in place. Button click temporarily presses into its surface.
- Warm ivory/copper is used on selection and the primary action, lilac is secondary. Most of the surface is neutral graphite.

## 3. Component map

| Element | Intended material |
| --- | --- |
| Page canvas | Graphite substrate with low-contrast micrograin and subtle ambient light |
| Hero | Single large raised molded slab; preview card floats only via static shadow |
| Titles | High-contrast ivory; short engraved dot signature beneath section titles |
| Navbar | Integral molded graphite rail, no glass or industrial cut corners |
| Cards | Raised graphite plates, broad diffuse and tight contact shadows |
| Buttons | Raised soft-touch keys; warm mineral primary; pressed activation |
| Inputs | Deep graphite inset wells, legible labels and independently visible focus |
| Tabs | Sunken tray with raised inactive keys, pressed selected key |
| Tables | Low relief (readable text first), engraved separators and a warm header accent |
| Modals, accordion, offcanvas | Stable raised pieces, correctly readable content |
| Small metadata | Warm tactile rounded badge, supporting semantic color variants |

## 4. Implementation boundary

Production changes are limited to `themes/neumorphism-soft.css`. Source artwork file `docs/NEUMORPHISM_MINERAL_GRAIN.svg` documents the embedded SVG texture. The original CSS classes and all 13 semantic `--theme-*` tokens remain, while theme palette values and material shadows change with this selected pilot.

- The shared HTML gallery remains unchanged.
- The generated Responsive Core block is byte-identical.
- All other themes remain unchanged.
- The theme remains a downloadable, standalone stylesheet with no JS dependency.
- CSS-only micrograin can be removed without affecting semantics or layout.

## 5. QA before merge

- W3C CSS validity; 13 alias contract; CSS custom property references; generated core drift.
- Real browser 17-theme regression on 320/375/390/430/768/1024/1280/1440 widths, offcanvas and horizontal tabs.
- Rendered contrast, focus ring, label and form control accessibility.
- Compare actual screenshots from desktop and mobile plus sections below the hero (cards, tabs, forms, tables).
- Fix any unintended contrast regression from legacy light-theme declarations.
- User reviews the tactile feel **before** refactoring redundant legacy CSS.
- No merge until the user expressly authorizes the tested direction.

**Status:** research-backed draft pilot; visual approval pending.

## 6. Graphite Cockpit 2.1 — high-end automotive revision

**User feedback:** "más oscuro.... pensemos que es para un coche de altagama". This replaces the relative dominance of warm mineral from 2.0. The goal is **precision manufacturing and luxury automotive upholstery**, not generic dark UI, a racing-game dashboard, or a literal branded car interior.

### Research behind the revision

- [Mercedes-Benz design and materials](https://www.mbusa.com/en/behind-the-mercedes-benz-star/design) — manufacturer describes deliberate coordination of textures, gloss levels, grain and control usability.
- [Porsche Panamera interior](https://newsroom.porsche.eu/en/press-kits/panamera/Interior.html) — manufacturer emphasizes modern technical detailing, premium materials, slender trim and a wide dark panel with ambient light.
- [Mercedes-AMG GT 4-Door Coupe interior](https://media.mercedes-benz.com/en/article/e3ffb9b3-1fdc-4e2c-ab13-b3fa1a9f3f72) — manufacturer describes one restrained strip of ambient lighting and matching display/control colors.
- [Bugatti Tourbillon interior](https://newsroom.bugatti.com/press-releases/bugatti-tourbillon-interior) — manufacturer explicitly values mechanical haptics, resistance and tactile travel.
- [ams OSRAM smart surfaces](https://ams-osram.com/applications/automotive-mobility/smart-surface) — supplier discusses subtle backlighting, 3D tactile shapes and selectively illuminated controls as modern HMI concepts.

These are *material/interaction references*, not visual assets or copied designs. Our code is an original CSS treatment of unchanged Bootstrap markup.

### Palette, surface hierarchy and spec

| Role | CSS private token | Color |
| --- | --- | --- |
| Unlit dashboard substrate | `--cockpit-canvas` | `#111319` |
| Mounting body / lower plates | `--cockpit-shell` | `#171a20` |
| Main raised tactile face | `--cockpit-panel` | `#1e2229` |
| Upper light-catching face | `--cockpit-panel-lit` | `#292d35` |
| Inset well and presses | `--cockpit-well` | `#090b10` |
| Precision gasket | `--cockpit-gasket` | `#0a0c11` |
| Main ivory text | `--cockpit-light` | `#e8e5e1` |
| Supporting text | `--cockpit-secondary-ink` | `#d1cfd0` |
| Minimal champagne trim | `--cockpit-warm-metal` | `#c9ac88` |

The theme's original public semantic tokens remain and retain their **names and order**. Its existing `--neu-*` base palette now resolves to deeper graphite and small metal accents, so any reusable legacy utility also draws from the new material.

### Physical grammar and what remains from 2.0

1. The **same original SVG soft-touch micrograin** remains embedded in the standalone CSS. No new images or JS.
2. Base substrate and raised panels have visibly different darkness, but lights only pick up narrow top edges. Large blur under all cards would look artificial.
3. Cards are stationary raised structures; only actual buttons get a short pressed response.
4. The primary button is now **graphite with a champagne locator rim**, NOT a large salmon/peach block. Success, warning and danger keep distinct semantic colors for function.
5. Tabs use a recessed control bank. Inactive tabs feel shallow-raised; selected ones are pressed into the slot.
6. Inputs are deep inset cavities with dark interiors and a narrow polished line on focus. Focus remains independently obvious through the gallery-wide dark outline + white halo contract.
7. Braille-like dots remain decorative and stylized as shallow machined dimples; no real Braille wording or semantic encoding.
8. Form text, tables, dialogs and small controls retain high-contrast readable ink and keyboard access.

### Design risk

The art direction must read as **automotive tactile premium**, not merely become a near-black recolor. Inspect contact shadows, inset lips, microtexture, light falloff and elevation distinction in screenshots at desktop and phone widths. A dark solid fill by itself is **not acceptance**.

**Status:** Graphite Cockpit 2.1 draft pilot. This direction is being tested; no explicit approval to merge has been given.

## 7. Graphite Cockpit 2.2 — Recessed Console review

**New user direction:** "personalmente me falta mas relieve invertido". The design still felt too raised after the move to dark automotive material. Increase **visible recessed geometry**, not just shadows everywhere.

### Implemented physical balance
- **Raised chassis:** overall hero, outer cards, and primary CTA stay lifted and weighty.
- **Deeper cavities:** hero-preview card interior, form mounting bay, inputs/selects/textarea, active tabs, table housing, progress track and opened accordion.
- **Shallow recesses:** card headers, secondary buttons, nav pill tray, grouped field collars, badges, section markings. Unselected tabs remain elevated to create a testable depth hierarchy.
- **Light direction:** narrow upper edge chamfer → short black lip → longer asymmetric internal shadow, with subtle opposite-side fill. Dark graphite, soft-touch micrograin and champagne accents remain.
- **Decorative engraved dots:** small four-dot impression added to card header, complementing the existing three-dot section signature. It is not actual Braille and conveys no status or content.
- **Accessibility boundary:** active tabs retain bright labels; all form controls retain standard focus state and keyboard functionality. No change to shared generated responsive rules.

### Architecture and test gate
- CSS appended as a **temporary review section** within `themes/neumorphism-soft.css` before generated Responsive Core. Consolidate older duplicate rules **after** visual approval.
- No gallery HTML/JS changes. Theme-owned syntax only and no new external materials.
- Inspect real full-page and component screenshots (390/768/1440) to verify the new recesses are visible outside the hero.
- Re-run 17-theme responsive, W3C CSS, focus, and contrast suites. This draft cannot merge without explicit user approval.

**Status:** 2.2 art-direction pilot, awaiting rendered review and user feedback.

## 8. Final visual approval and CSS consolidation (2026-11-03)

The user approved Graphite Cockpit 2.2 Recessed Console with "me gusta". This confirms **visual direction**, not permission to merge to `main`.

The final CSS housekeeping pass removed **258 redundant single-line declarations** from earlier same-selector rules, a net **8,259 bytes (12.6%)** less CSS. Only declarations conclusively shadowed by a later rule of the *exact same selector/property* and sufficient `!important` priority were removed. Existing at-rules, media rules, custom-property root contract and generated Responsive Core were explicitly preserved. Non-trivial multi-line declarations and different-specificity cases were deliberately left in place rather than risk altering the cascade.

**Acceptance gate:** confirm W3C, accessibility, responsive CI and pixel-level screenshot equivalence with the visual-approved Graphite Cockpit 2.2 baseline. If any visual mismatch is observed, re-evaluate the removed declarations before release.

PR #15 remains **draft** and must not be merged until explicit authorization. The documented approved design is preserved independently of any future code refactoring.
