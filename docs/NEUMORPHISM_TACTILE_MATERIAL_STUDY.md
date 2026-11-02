# Neumorphism Soft — Tactile Material Study

> Status: research and three proposed art directions only. No theme CSS, gallery or shared responsive code changed. User approval of a direction is required before implementation.

## Contents
1. User intent
2. Current implementation: verified findings
3. Real reference study
4. Physical principles and risks
5. Three art directions
6. Component material map
7. Recommended next prototype and acceptance criteria

## 1. User intent

The user likes *recessed / engraved relief* that resembles a tactile Braille pattern, but says the present theme lacks convincing realism. The new identity should have **texture and luminosity that make the surfaces feel touchable**. This is not a request for actual Braille writing or to make all text embossed. The shared design process is research → compare directions → user selection → pilot → real responsive screenshots → revisions → explicit permission to merge.

## 2. Verified existing CSS

Source: `themes/neumorphism-soft.css` on `main`, inspected 2026-11-02.

- 1,321 lines / ~29 KB, including an embedded generated responsive core beginning after ~884 lines of theme-owned CSS.
- Public palette includes `--neu-bg: #e0e5ec`, `--neu-light: #ffffff`, `--neu-dark: #a3b1c6`, `--neu-primary: #667eea`, `--neu-secondary: #764ba2`.
- `--shadow-light` and `--shadow-inset` each use just two symmetric shadow declarations: highlights upper-left, shadows lower-right. The same shapes and depth repeat widely.
- Cards, buttons, navbar and alerts are raised with near-identical softness. Inputs, several headers and tabs rely on inset effects. The theme has public `.neu-pressed` and `.neu-raised` utilities.
- `neuPulse` and `neuFloat` create exaggerated/continuous motion for some controls and containers; static physical objects should not appear to float rhythmically.
- Contrast overrides near the end protect hero and other components. Preserve until evaluated with real browser computed contrast.

**Diagnosis (our design interpretation):** a convincing tangible surface requires different optical responses by physical state and material, not more of the same blur. The current theme's one-size-fits-all lighting makes everything feel molded to the same depth.

## 3. External design research

These sources are references, not designs to copy. Distinguish interactive demos from editorial analyses and portfolio artwork.

| Source (URL) | Type | What we learn |
| --- | --- | --- |
| [Air&Ember — Neumorphism](https://airandember.com/pages/designs/neumorphism.html) | Interactive demo | A **shared light direction** is more important than sheer shadow size; tests raised, flat and pressed states interactively. |
| [Chris Lemke — Neumorphism](https://chrislemke.github.io/website_designs/examples/Neumorphism.html) | Interactive showcase | Contrast and perceived height change notably when controls shift between convex and concave. |
| [CodeFronts CSS neumorphism examples](https://codefronts.com/design-styles/css-neumorphism/) | CSS gallery/demos | Shows how flat, raised and inset can communicate interactions; avoids making all elements appear clickable. |
| [Setproduct — Neumorphism design guide](https://www.setproduct.com/blog/neumorphism-design-guide) | Design article / image examples | Rotary controls, pressed discs and small color indicators suggest physical tactility; large shadows are not always required. |
| [Neumorphism UI Design (Behance)](https://www.behance.net/gallery/113196321/Neumorphism-UI-Design) | Visual concept | Repeating round pressed wells can make consistent component vocabulary, but text legibility should be evaluated separately. |
| [Skya Designs — Claymorphism](https://www.skyadesigns.co.uk/web-design-insights/what-is-claymorphism-top-web-trend-2024/) | Design explainer / illustrations | Warm tan material, shallow relief and texture suggest physical surfaces; **avoid turning neumorphism into puffy toy claymorphism**. |
| [Dark Volume Knobs — Voicu Apostol](https://dribbble.com/shots/21408863-Neumorphic-Dark-Volume-Knobs) | Visual concept | Deep charcoal recess and a tiny spot highlight produce a tactile dark elastomer impression. |
| [Smashing Magazine — Claymorphism](https://www.smashingmagazine.com/2022/03/claymorphism-css-ui-design-trend/) | Critical editorial article | Uniform soft-surface components often look like buttons even when not interactive. A clear hierarchy and accessible controls are essential. |
| [W3C WCAG 2.2 Non-text Contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast) | Authoritative accessibility guidance | Necessary non-text identification/state indicators generally need **3:1 contrast** against adjacent colors; decorative shadow alone is not a robust identifier. |

## 4. Design physics: texture, direction and depth

- **Directional illumination:** one primary light source (upper-left); opposite lower-right shadow consistent across cards and buttons.
- **Contact shadow:** a short darker, slightly sharper shadow immediately where raised parts meet the base. A long diffuse shadow alone looks like a floating sticker.
- **Surface roughness:** microtexture extremely low-contrast, limited to large backgrounds/material areas. Keep text foreground crisp. A small embedded, static noise tile or CSS gradient can be tested; no external assets required.
- **Depth states:** 0 base substrate; 1 shallow molded ridge; 2 raised clickable control; 3 larger raised card; -1 recessed input or selected state. A deeper inset for special dials only.
- **Edge light:** thin highlight on the lit upper-left edge, darker falloff below-right. On satin materials this edge is narrower; on matte clay it is broader and diffuse.
- **Tactile 'Braille' dots:** decorative embossed dots or engraved dots near labels/headings, not actual Braille text and never the only way to convey meaning.
- **Motion:** continuous bobbing/pulsing is not an accurate physical affordance. A button may briefly move to its pressed surface, but no persistent ambient movement.

## 5. Three genuinely distinct directions

### A. Satin Porcelain — premium pearlescent ceramic

- **Visual:** ivory pearl, cool white upper-left light, blue-gray and lilac lower-right shadows; polished satin lip on a near-matte surface.
- **Geometry:** precision-molded panels, round inset wells, tidy smooth radii, thin ridges.
- **Signature:** small specular edge gleam and clear contrast from the *shallow-but-crisp* recessed form control.
- **Components:** cards become broad porcelain plates; CTAs are raised discs/pills; form inputs are narrow inset wells; tabs resemble molded ceramic keys.
- **Strength:** premium and subtle, offers brightness and clean alignment without a common glass/gradient effect.
- **Risk:** may look like conventional pale soft UI; grain must be controlled and controls must be identifiable.

### B. Warm Mineral — fine-grain ivory cast + pearly edges

- **Visual:** warm chalk/stone/ivory with cream highlights and cooler taupe-gray contact shadows; minimal muted indigo interaction accent.
- **Geometry:** molded soft rectangular slabs, small engraved seams and dotted indentations; no balloon-like clay blobs.
- **Signature:** *material micrograin under raking light*, subtle ceramic sheen at thin edges; broad but grounded contact shadow.
- **Components:** large raised hero slab, smaller lifted cards, primary action with polished lit rim, deeply recessed input channels, pressed active tabs, sparse engraved dot signatures.
- **Strength:** likely the most **touchable** without appearing nostalgic, following user's interest in relief/texture.
- **Risk:** warm gray-on-warm gray can become muddy or look like a rustic décor page; active states and typography must remain legible.

### C. Soft Elastomer — precision technical rubber

- **Visual:** graphite / blue-gray soft-touch polymer with concentrated rim highlights and much deeper recesses, technical indicator dots.
- **Geometry:** smaller radii; convincing molded controls / channels / concentric button indentations.
- **Signature:** tactile soft rubber, a controlled bright inset line and one small active-color ring.
- **Components:** device-like navbar and panels; pressure-key buttons, carved tab channels, rotary-like progress meters; consistent reading surface, not flashy.
- **Strength:** clearest raised versus pressed physical semantics.
- **Risk:** could become an equipment dashboard or resemble the project's hard-edge Cyberpunk theme; dark contrast work is more involved.

## 6. Bootstrap component material mapping

| Component | Physical metaphor | Expected state |
| --- | --- | --- |
| Page/hero | One continuous substrate and optional higher relief slab | Flat foundation; controlled light |
| Cards | Raised sculpted plates with grounded contact shadows | Raised, not "button" on hover by default |
| Primary button | Raised tactile control with readable label | Raised → temporarily pressed |
| Secondary button | Shallow molded key | Shallow raised → pressed |
| Input/select/textarea | Milled/pressed wells | Inset always; visible focus highlight |
| Radio/checkbox | Recess and movable nub | Visual state via more than shadow |
| Tabs | Molded controls / small sockets | Raised inactive, pressed or clearly selected active |
| Tables | Flat readable content with engraved separators | Avoid over-neumorphing every cell |
| Modal/offcanvas | Stable raised panel with safe focus | No animated floating |
| Dotted Braille-like motif | Decorative embossed/debossed imprints | Never substitutes for an accessible label |

## 7. Proposed workflow

**Recommendation for the FIRST pilot: B Warm Mineral with some narrow pearly highlights from A.** This best develops the requested tactile material / engraved relief. But A or C are equally valid alternative identities if the user prefers their atmosphere.

After user selects:
1. Start an isolated implementation branch off current `main`.
2. Build a consistent material token vocabulary while preserving the 13 semantic `--theme-*` and existing public `--neu-*`.
3. Demonstrate raised card, pressed button, and inset input first on **existing** Bootstrap gallery, then propagate to navbar, tabs, tables, accordion, modal and offcanvas.
4. Test mobile widths (320/375/390/430) and tablet/desktop (768/1024/1280/1440), keyboard focus, contrast and reduced motion. Run all repository CI.
5. Inspect screenshots **below the hero**, not only the background and title.
6. Request aesthetic review before simplifying redundant rules and before any merge.

**Research status:** user decision pending. No visual CSS has been changed.
