# Retrowave Synthwave 2.0 — reference study and background design brief

## Table of contents
1. Current CSS baseline and user direction
2. Real/reference designs and learnings
3. Design grammar of synthwave / outrun
4. Three background compositions
5. Recommended first prototype
6. Implementation boundary and technical risks
7. Validation and decision gates

## 1. Current CSS baseline and user direction

**User intent:** User likes the existing theme colors; the background should be significantly more elaborate and representative of retrowave/synthwave, with broad artistic freedom. Preserve collection standards.

Repository inspected on `main` (2026-11-02): `themes/retrowave-synthwave.css`, 37,042 bytes, 1,616 lines, first 1,178 theme-owned lines, generated Responsive Core v1 begins around line 1,179.

Observed:
- Current palette already includes `--retro-pink: #ff0080`, `--retro-cyan: #00d4ff`, `--retro-purple: #8b00ff`, `--retro-orange: #ff8c00`, `--retro-yellow: #ffd700`, plus deep violet/near-black background.
- `body` currently renders a repetitive flat pink 30px grid over radial background gradients. It has **no perspective horizon** or compositional landscape.
- `body::before` adds an always-running scanline at `z-index: 1000`.
- Headings, cards and controls use strong glow, animated title gradients, Orbitron widely and translucent surface panels.
- Same 13 semantic `--theme-*` contract and common generated responsive core as other themes. Pre-generated theme-specific mobile rules at max-width 768px are a compatibility consideration.

**Interpretation:** The palette is genre-correct. The existing page lacks the defining sky → horizon → perspective floor composition, so it feels like neon wallpaper rather than a synthesized 1980s landscape. Do NOT throw away the colors just because background geometry changes.

## 2. Real/reference designs and learnings

| Reference / category | URL | Visual observation and transferable idea | Constraint |
| --- | --- | --- | --- |
| Bruno Peviani, **Horizon Drive** (Behance website concept) | https://www.behance.net/gallery/57289207/Landing-Page-%2880s-style%29 | Skyline, racing-road convergence, triangle framing, title hierarchy. The skyline and point of convergence direct attention toward central content. | Concept, not proven production/mobile design; do not copy imagery/assets |
| **Synthwave Vista** image in SongSmith | https://songsmith.studio/ | Layered violet sky, bright horizon, polygonal mountains, palm silhouettes and glowing grid. Clean front/back/middle scene separation. | Image illustration, not ready-to-use website CSS |
| **Sonivis** Synthwave Sunset Grid | https://sonivis.studio/library | Sunset disc, low-poly mountains, perspective grid, sharp cyan/pink complementary light. | Visualization library art, not directly reusable assets |
| **Webflow Synthwave Gallery** | https://webflow.com/made-in-webflow/synthwave | Varied genuine interactive sites and experiments; inspect content-heavy pages and nav, not only hero screenshots. | Some links are concepts, templates, or demos; distinguish them |
| **Retrowave: How to Create Synthwave Art** (2026) | https://retrowave.com/how-to-create-your-own-rad-synthwave-art-from-scratch/ | Perspective grid with vanishing point, horizontally banded sun, mountains and high-contrast silhouettes as compositional tools. | Explanatory article; broad design vocabulary |
| **CSS 3D Lab: Synthwave floor** | https://css3dlab.edgarasneverdauskas.com/models/grid/ | 3D floor can be created with gradients, perspective and rotateX; CSS-only appearance and motion loop possible. | Evaluate browser performance and reduced-motion |
| **Ravindra Nath Jha: Outrun Horizon** | https://www.ravindranathjha.in/templates/retro-80s-outrun-grid | Example of a CSS-only horizon and striped sun using lightweight layers. | Its sample markup cannot be assumed to exist in our boilerplate |
| **Shadcn retro grid background** | https://www.shadcn.io/background/solid/retro-grid | Keep upper sky calm so the heading remains readable; fade grid into horizon. | Framework-specific example, **do not install framework dependency** |
| **Stylogeny Synthwave/Outrun** | https://stylogeny.com/styles/synthwave-outrun/ | Distinguishes nostalgia-driven outrun from other neon cyberpunk and emphasizes spatial depth. | General historical/art-direction analysis |

Research reference dates and author claims are source-reported, not independent verification.

## 3. Design grammar of synthwave / outrun

**Spatial architecture**
1. Deep violet, star-speckled sky with open negative space.
2. Gradient orange/pink **sun disc** at or just above horizon, with period-appropriate horizontal slits.
3. Midground silhouette (distant low-poly mountains or skyline) to establish scale.
4. Perspective ground grid: large cells in foreground, converging at horizon.
5. Dark foreground framing that protects interaction and reading contrast.

**Color**: Retain current CSS palette and assign intentional roles: violet sky, orange/gold sunset, hot-pink horizon/grid, cyan active focus and occasional reflected light. Existing bright color aliases should remain compatible.

**Typography**: Original Orbitron-like display type has thematic value; use lighter-weight readable body text for paragraphs and forms only if testing warrants. Chromed titles are optional focal art, not a universal accessibility-proof text style.

**Motion**: Natural scene illusion is valuable even with *zero motion*. If later approved, optional horizon drift or mild pointer parallax may use theme-specific JS with cleanup and reduced-motion support; avoid persistent scanline crossing page content.

## 4. Three deliberately different backgrounds to compare

### A. Sunset Highway (recommended)

Core: twilight starfield, huge striped sunset, one-point magenta/cyan perspective floor, a thin distant mountain silhouette and softer lower-page atmospheric gradients.

Strengths: most authentic Outrun; the original color palette gains depth immediately. Distinct from Cyberpunk Hardline's industrial layout and Organic Glass's translucent shapes.

Risks: scene may compete with the two-column common Bootstrap hero or look like a generic poster if all symbols dominate equally.

### B. Neon Coast

Core: violet–magenta skyline, stylized palm silhouettes, mirror-like sea/light trails, sun farther right; floor grid only on small horizons/section dividers.

Strengths: Miami Vice / night-drive nostalgia, more organic and atmospheric. Good for artistic mood.

Risks: palm tree graphics may require layered art or embedded SVG/data URI, which must be original, optional and not undermine standalone CSS.

### C. Cosmic Arcade

Core: starfield, abstract orbit rings, segmented sunset/planet, diagonal beams, small floating wireframe shapes; no literal car/road/palm imagery.

Strengths: high visual freedom; looks retro-futuristic without reproducing the standard postcard.

Risks: can drift toward generic space neon or glassmorphism; preserve clear synthwave horizon and warm light.

## 5. Recommended first prototype

**Sunset Highway** as a visual experiment, *not yet approved as final*.

- Retain all current `--retro-*` palette variables and the 13 `--theme-*` contract.
- Use existing hero `#home` in the gallery for **scene framing** without editing `index.html`.
- Prefer a **CSS-only** composited scene: sky gradients on `#home` or body, decorative sun/mountains using pseudoelements and layered gradients, perspective grid bounded to the hero. Test exact stacking and overflow; avoid obscuring nav, interactive controls or mobile content.
- The global page below hero becomes a relatively quiet purple-night canvas with occasional glows, not an endless full-page grid.
- Expose future private theme tokens such as `--retro-horizon-y`, `--retro-sun-size`, `--retro-scene-intensity` for maintenance.
- Any extra scene element should have real compositional value, *not* just add more neon.
- No new `retrowave-synthwave.js` initially, unless CSS implementation demonstrates a meaningful interactive benefit.

## 6. Implementation boundaries and risk management

- One theme CSS remains downloadable and works on arbitrary Bootstrap 5 pages independently of the gallery's `#home` (fallback atmospheric `body` remains).
- Generated responsive block between official markers is untouchable.
- Existing theme-specific @media block needs review to avoid conflicting with shared responsive core, not blind deletion.
- `body::before` scanline has z-index 1000: global overlay may cover UI; reassess before adding scene layers.
- Do not make the scene fixed over all content by default; no distracting motion and respect `prefers-reduced-motion`.
- Avoid image fetches/CDN and third-party artwork in downloadable CSS. Gradients, CSS shapes, or **original** local data art are safer.
- Keep contrast and focus legible against gradient sky and luminous hotspots.
- **CSS feasibility caution:** A convincing grid + sun + skyline may need more than two pseudo-elements. Evaluate layered CSS backgrounds and masks in-browser first, rather than assuming a concept illustration is directly achievable with the existing DOM.

## 7. Validation and decision gates

1. Select primary composition or blend from A/B/C and define background hierarchy (sun placement / grid intensity / silhouette type).
2. Develop a self-contained CSS branch pilot on **the unchanged shared gallery**.
3. Confirm the generated responsive block and other 16 selectable themes are unchanged.
4. Compare screenshots on desktop 1440px and mobile 390px before/after, with 320/375/430/768/1024px regression checks.
5. Test theme downloads, no-JS fallback, interactive modal/accordion/nav, CSS validity, contrast and reduced motion.
6. Revise after user's visual feedback; consolidate CSS only after rendered equivalence verification; no merge without explicit approval.

**State:** research + proposal. No CSS modified as part of this research branch.
