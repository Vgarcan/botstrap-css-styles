# Theme Contract v1 — CSS standardisation

## Contents
1. Purpose and compatibility
2. Semantic token contract
3. How to integrate a theme
4. Migration phases
5. Automated checks and known gaps

## 1. Purpose and compatibility

Every **non-empty** `themes/*.css` file now exposes exactly the same 13
`--theme-*` semantic custom properties in `:root`. That means 17 selectable
themes plus the older unused `bootstrap-theme.css` (18 total).

The values reflect each theme's existing palette and visual identity.
**This first step is intentionally non-visual**: no existing component selector,
declaration or legacy variable is changed. The tokens are *aliases* for
existing theme variables wherever possible, not replacements.

The existing `corporate-blue.css` is empty and is explicitly excluded.
It is not a working theme.

## 2. Semantic token contract

| Token | Meaning |
| --- | --- |
| `--theme-primary` | Primary brand/control colour |
| `--theme-secondary` | Secondary brand colour |
| `--theme-accent` | Decorative or emphasis colour |
| `--theme-success` | Success-state colour |
| `--theme-warning` | Warning-state colour |
| `--theme-danger` | Destructive/error-state colour |
| `--theme-background` | Main page background (solid or gradient) |
| `--theme-surface` | Basic panel/card surface (may be translucent) |
| `--theme-text` | Principal text colour on the theme canvas |
| `--theme-font-body` | Body font family, including fallback |
| `--theme-font-heading` | Heading font family, including fallback |
| `--theme-radius` | Characteristic corner radius |
| `--theme-shadow` | Characteristic box shadow |

These are **semantic design tokens**, not direct Bootstrap `--bs-*` replacements.
Values may be light, dark or translucent depending on the theme. For example,
`--theme-primary` does not guarantee accessible text contrast against
`--theme-surface`. Accessibility remains a separate audit item.

## 3. How to integrate a theme

Each stylesheet remains standalone and can be used in any static HTML
or Django project, with Bootstrap loaded **before** the chosen theme.

```html
<!-- Bootstrap components and responsive utilities. -->
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">

<!-- Exactly one theme stylesheet. -->
<link rel="stylesheet" href="/static/themes/corporate-tech.css">
```

New custom components can reference the stable contract without knowing
theme-specific variables:

```css
/* A consumer-owned component, not a change to the themes themselves. */
.project-heading {
  color: var(--theme-primary);
  font-family: var(--theme-font-heading);
}

.project-panel {
  background: var(--theme-surface);
  border-radius: var(--theme-radius);
  box-shadow: var(--theme-shadow);
}
```

For the repository's GitHub Pages gallery, the theme is selected in
`index.html`; the URL query parameter `?theme=corporate-tech` provides
a direct link. **Do not load all 17 CSS files simultaneously.**

## 4. Migration phases

### Phase 1 — completed in this PR
- Define the same token names and order in 18 non-empty files.
- Keep all pre-existing CSS rules and public legacy variables intact.
- Validate the 13-token contract in CI.
- Maintain the original file and download structure.

### Phase 2 — after visual baselines
- Migrate component rules towards the semantic tokens incrementally.
- Introduce Bootstrap component-variable overrides (e.g. `--bs-btn-bg`)
  only where they are proven compatible.
- Establish contrast-aware text-on-primary, borders and focus tokens.
- Add reduced-motion support and visual regression testing.

This is deliberate: replacing existing references everywhere would change
how scoped overrides resolve and could alter real-world applications.

## 5. Checks and known gaps

```bash
python3 scripts/verify_theme_contract.py
python3 scripts/verify_site.py
```

Known pre-existing issues, not silently fixed by standardisation:
- `modern-gradient.css` uses an undefined `--border-glass` variable.
- `art-deco-luxury.css` uses an undefined `--deco-brown` variable.
- Some themes rely on fonts not currently loaded by the gallery.
- None of the selectable themes currently adds its own
  `prefers-reduced-motion` fallback.
- The repository has one empty, unselected `corporate-blue.css`.

The **visual appearance is intended to remain unchanged** in this PR.
Browser-based visual and accessibility validation still needs to happen.
