# Cyberpunk Neon 2.0 — second visual-reference study

## Contents
1. Research question and source classifications
2. Six different interpretations
3. Contrasts with adjacent styles
4. Transfer to a reusable Bootstrap theme
5. Cross-reference comparison
6. Interaction and accessibility
7. Working conclusions and next experiment

> Status: research only, 2026-11-02. No production CSS/JS modifications or art-direction approval. Companion to `docs/CYBERPUNK_NEON_RESEARCH.md`.

## 1. Research question and source classifications

**Question:** Which parts of a cyberpunk visual language make an effective *reusable web theme* without copying a game HUD, making information unreadable, or losing the theme's distinctive identity?

Evidence categories:
- **Real interactive web experience:** an actual website with navigation/content, not necessarily externally audited.
- **Case study / prototype:** designer-described work or demonstration, with no inferred production readiness.
- **Game or film reference:** intended to teach material, mood and layout, NOT a directly compatible browser interaction pattern.
- **Interpretation:** our proposed translation, explicitly not a proven fact.

## 2. Six different interpretations

### 2.1 Neo-Tokyo Editorial — Utopia Tokyo (2026)

- **Source:** [Abduzeedo case study](https://abduzeedo.com/utopia-tokyo-interactive-web-design-meets-japanese-masks).
- **Type:** interactive web design project.
- **Observed:** dominant red/black; enormous monospaced headlines; formal rectangular column structure; floating 3D mask; surveillance cues, kanji graphics and corner brackets. It offers a *Safe Mode* versus *Glitch Effect* choice, per the article.
- **Interpretation:** colour saturation and typographic mass can create cyberpunk without conventional cyan/magenta glow. The strongest element is the high-impact editorial grid rather than individual card shadows.
- **Bootstrap experiment:** an asymmetrical hero, large display heading, compact small-caps metadata bar, optional pseudo-element corner cut; keep forms quiet and safe by default.
- **Avoid:** unearned Japanese motifs or making seizure-risk content the default.

### 2.2 Augmented Industrial — Deus Ex UI

- **Source:** [Benoit Perreault, UI Director / Lead UI Artist on Mankind Divided](https://www.benoitperreault.com/deusex) and [Human Revolution interface gallery](https://www.behance.net/gallery/2465641/Deus-Ex-Human-Revolution-User-Interface).
- **Type:** first-person production account and game UI portfolio/screens.
- **Observed:** spatially registered information, angular module frames and system-status views; restrained use of amber/teal and dark surfaces; design team explicitly linked overlays to the objects being managed.
- **Interpretation:** a successful “tech interface” should make components *read like instruments with a purpose*. One strong highlight colour can carry navigational information.
- **Bootstrap experiment:** status rails, card-top metadata, selected item hierarchy, anchored action menus; do not copy original HUD overlay design.

### 2.3 Redline / Underground — RUINER

- **Source:** [Analog Stick Gaming review including menu and skill-screen captures](https://www.analogstickgaming.com/game-reviews/2017/11/30/ruiner-2hfrw).
- **Type:** gameplay menu visual reference, secondary source.
- **Observed:** large black-to-crimson contrast, red accent blocks, hard navigation dividers, interface glyphs; strong selected-state emphasis.
- **Interpretation:** cyberpunk can feel brutal and forceful without rainbow accents. It may become hard to distinguish errors from primary actions if red is overused.
- **Bootstrap experiment:** thick active tab indicator, bold button variant, angular card heading; maintain explicit success/error labels and symbols.

### 2.4 Terminal Underground — N-OST / NODE

- **Sources:** [Awwwards N-OST / ASCII-style project inspiration](https://www.awwwards.com/inspiration/retro-loading), [Wendy Zhou's study of n-o-d-e.net](https://www.wendyzhou.se/blog/cyberpunk-ui-website-design-inspiration/).
- **Type:** actual web-interface references, snapshot and write-up.
- **Observed:** nearly monochrome pages, small monospace lines, ASCII-art markers, few visual effects, information first.
- **Interpretation:** the command-line metaphor expresses a dystopian, hacker identity with greater clarity than permanent “glitch”.
- **Bootstrap experiment:** code-like overlines and an optional terminal panel class, but **never** make every form input simulate a command prompt.

### 2.5 Atmospheric Dystopia

- **Source:** [Dystopian world landing hero](https://dribbble.com/shots/23353949-Landing-page-hero-for-Dystopian-world-cyberpunk-exploration).
- **Type:** static concept design.
- **Observed:** large environment artwork, UI frame lines layered above the picture, emphasized primary CTA and a smaller media teaser.
- **Interpretation:** scenery carries atmosphere; navigation and text can remain relatively conventional. Pure CSS can reproduce much of the geometry but not the illustrative narrative.
- **Bootstrap experiment:** hero with optional authored imagery and simple technical frame shapes. CSS-only theme must still work when no image assets are supplied.

### 2.6 Analog Cybernetics — Ghost in the Shell (1995)

- **Source:** [Interface Love frame analysis](https://ilikeinterfaces.com/2015/02/26/analysis-ui-ghost-in-the-shell/).
- **Type:** film/interface visual study.
- **Observed:** phosphor-green medical/hacking readouts, diagnostic labels, technical numeric content, imaging scans.
- **Interpretation:** a retro-futuristic feeling can come from representing actual information rather than covering the background in decorative matrix rain.
- **Bootstrap experiment:** a clearly optional “diagnostic panel” component; legible mono labels, no fabricated live telemetry.

## 3. Distinguishing adjacent aesthetics

| Adjacent vocabulary | Distinctive signal | When useful | Risk of misclassification |
| --- | --- | --- | --- |
| Synthwave/Outrun | Pink-purple gradients, wireframe horizon, sunset, chrome text | Music, nostalgia and retro showcases | Becomes 1980s nostalgia rather than high-tech/low-life cyberpunk |
| Futuristic military HUD | Angular frames, data markers, on-object overlays, hierarchy | Status-intensive interfaces | Looks like a combat/game UI instead of a website |
| Techno-brutalism/editorial | Huge type, strong asymmetry, exposed grid, extreme contrast | Showcase/hero areas | Decorative harshness can overpower actual Bootstrap controls |
| Terminal/hacker | Monospace, command labels, ASCII/CRT, dark field | Developer-oriented panels, documentation | Extremely constrained visual variety |
| Japanese dystopian editorial | Red/black blocks, kanji, oversized technical type | Narrative and experimental promotions | Cultural appropriation or unearned ornament without content rationale |
| Atmospheric/cinematic sci-fi | City imagery, silhouette, light shafts, framed layers | Campaign hero | Non-portable image dependency and weaker reusable CSS identity |

References: [Webflow on retrofuturism](https://webflow.com/blog/retrofuturism), [Adobe on cyberpunk's film-noir heritage](https://blog.adobe.com/en/publish/2020/01/09/4-design-trends-that-will-define-2020), and [Deus Ex UI production notes](https://www.benoitperreault.com/deusex).

## 4. Transfer into Bootstrap (before picking art direction)

| Component | Transferable visual idea | Must remain usable |
| --- | --- | --- |
| Hero | Editorial asymmetry, large title, small system annotation, restrained decorative framing | Content readable without theme JS or image assets |
| Navigation | Hard-edge surfaces, selection rail, descriptive active state | Mobile offcanvas, keyboard focus, proper contrast |
| Cards | Distinct signal/quiet variants, small notch and divided header | Normal `.card` interoperable; no hover-dependent information |
| Tabs | Segmented high-contrast active indicator | Horizontal scroll on phones, no broken tab behaviour |
| Buttons | One visually primary action, quiet alternative | Disabled/hover/focus and touch states |
| Alerts | Hazard-stripe / coloured semantic edge *with labels* | Distinguish warning, danger, success without colour alone |
| Inputs | Industrial border geometry, focus readout | Placeholder/text clarity, visible caret and validation |
| Tables | Narrow label gutters and precision rules | Responsive horizontal scrolling, no forced body monospace |
| Modals | Bracketed header + dark solid body | Bootstrap stacking, focus trap, contrast and close controls |

## 5. Reference comparison — observations, not score claims

| Ref | Colour dependency | Geometry | Texture & motion | UX transfer |
| --- | --- | --- | --- | --- |
| Utopia Tokyo | red/black | editorial grid, brackets | interactive glitch optional | hero, typography |
| Deus Ex | dark + amber/teal | instrument panel, cutouts | context-driven | cards, states, controls |
| RUINER | red/black | angular, compressed | high intensity | active navigation, buttons |
| N-OST/NODE | monochrome | straight grid, ASCII | minimal | diagnostics, text hierarchy |
| Dystopian Hero | cyan/atmosphere | overlays, media frame | background atmosphere | gallery/landing hero |
| Ghost in the Shell | green/black | readout panes | analog screen texture | optional diagnostic variant |

This table describes source properties; it is **not** a quantified performance or accessibility ranking.

## 6. Interaction and accessibility

- Prefer *static structural cyberpunk* over a mandatory perpetual scanline or RGB displacement.
- Active/focus states must remain visible without animations. Respect `prefers-reduced-motion`.
- Preserve WCAG 2.2 AA text contrast targets (4.5:1 normal; 3:1 large) and non-text interface contrast as applicable; see [W3C WCAG 2.2](https://www.w3.org/TR/wcag/).
- Utopia Tokyo's Safe Mode choice is an example of optional effects; do not assume a product is accessibility-conformant merely because it exposes this choice.
- Keep `theme-core.js` optional; any eventual `cyberpunk-neon.js` must be a justified progressive enhancement with lifecycle cleanup.
- Never copy art, fonts, logos or distinctive original game assets.

## 7. Working conclusions and next experiment

**Finding:** The common ingredient across widely different references is *information framed as part of a fictional system*: precision labels, distinct layers, geometry and clear status cues — **not** just luminous palette.

**Design uncertainty:** We still do not know whether the collection's Cyberpunk Neon should emphasize editorial/poster composition, tactical hardware, minimal terminal, atmospheric city or a contrasting hybrid.

**Proposed next experiment (not yet implementing):**
1. Sketch the **same exact hero/card/form/tab layout** in three visual grammars: editorial, instrument, and terminal.
2. Compare composition before fine-tuning colour or adding glow.
3. Review one phone-first configuration and one desktop configuration for each.
4. Have the user select attributes they like from different designs; avoid prematurely freezing a named direction.
5. Only then prototype CSS in a separate implementation PR and keep `main` unmodified until approved.

Research sources are inspiration/evidence, not templates authorized for direct copying.
