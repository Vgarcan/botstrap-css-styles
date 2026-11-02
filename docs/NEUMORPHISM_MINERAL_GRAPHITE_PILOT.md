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
