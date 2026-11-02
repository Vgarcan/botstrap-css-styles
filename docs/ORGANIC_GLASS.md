# Organic Glass pilot — CSS + optional JavaScript architecture

## Contents
1. Goal and visual language
2. File association
3. Lifecycle and safety
4. Design tokens
5. Test and acceptance criteria

## 1. Goal and visual language

The first pilot modernises **Glassmorphism Pro** using organic geometry:
asymmetric translucent ellipses, controlled light sources, layered materials,
subtle edge reflections and different card elevations. Flat colour and loud
perpetual floating/morphing animations are intentionally replaced by quiet,
mostly static composition. This is an iterative visual baseline, not a redesign
of every theme.

## 2. File association

- \`themes/glassmorphism-pro.css\` — complete visual identity, no JS required.
- \`js/theme-core.js\` — common optional module loader and lifecycle.
- \`themes/glassmorphism-pro.js\` — optional organic-glass pointer response.

To integrate a theme in HTML/Django, load Bootstrap CSS first, then the one
selected theme CSS. Only if advanced visual interaction is desired, add the
general runtime after the DOM is available (or defer it) and call
\`ThemeRuntime.activate("glassmorphism-pro")\`.

A matching JS file is optional. The runtime has an **explicit allowlist**
of available modules to avoid a failed HTTP request for each CSS-only theme.
To add a new module, create \`themes/<theme-id>.js\`, export \`mount(context)\`,
and register the theme ID in \`js/theme-core.js\`. The loader derives
\`<theme-id>.js\` from the selected CSS identifier; it is not supplied from
arbitrary user input. No external JS library is necessary.

The gallery loads the runtime once, and theme switching triggers
\`activate(name)\`. It never loads 17 enhancement modules simultaneously.

## 3. Lifecycle and safety

- Theme Core cancels existing listeners with AbortController, calls cleanup,
  increments a request generation and only mounts the latest requested module.
- A delayed dynamic import cannot revive effects from a previously selected
  theme. Failed imports never block the CSS theme.
- The Glass module only listens to mouse/trackpad movement on card elements,
  using requestAnimationFrame for at most one update per frame.
- On detach it removes the \`glass-interactive\` class and inline CSS custom
  properties. It does not mutate Bootstrap markup or component state.
- The experience is static without JS, on touch screens and when
  \`prefers-reduced-motion: reduce\` is enabled.

## 4. Design tokens

The existing \`--theme-*\` contract is retained and extended by private
\`--glass-organic-*\` design tokens for radius, shadow, translucency and
surface lighting. The **shared responsive core is unchanged**; only the
Glass-specific section before the generated core is edited.

Geometry must express depth, not distract: page-level ambient shapes,
a restrained organic hero composition and stable glass card surfaces.
Never add an essential animated background or 3D card spins.

## 5. Test and acceptance criteria

- Single-theme download continues to produce a standalone usable CSS file.
- 17 selectable themes remain responsive at all eight established viewports.
- W3C CSS validator, token-contract, undefined-variable and axe contrast
  checks remain green.
- Quick switching: Glass → another theme → Glass, with no leftover classes,
  inline position variables or old pointer listeners.
- No extra theme JS is fetched for CSS-only themes; the optional Glass module
  loads once as an ES module when selected.
- JS disabled: all content, navigation, colours and geometry remain usable.
- Review actual desktop and mobile screenshots before merging. This pilot
  does not certify WCAG conformance or replace manual Safari/Android QA.
