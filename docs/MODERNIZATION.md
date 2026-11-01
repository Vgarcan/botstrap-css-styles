# Bootstrap themes — modernisation plan

## Objective
Turn this repository into a reusable, accessible, mobile-first Bootstrap
theme library with a live GitHub Pages testing gallery.

## Principles
1. Keep each visual personality distinct. Modernisation is not
   homogenisation.
2. Avoid breaking Bootstrap's components or project integrations.
3. Design for touch, keyboard, narrow screens, and reduced motion.
4. Prefer CSS custom properties for colours, spacing, radii, and typography.
5. Ship one testable theme improvement per small pull request.

## Iterations
### 0. Establish a dependable preview (this PR)
- Use the existing GitHub Pages site published directly from `main` (already enabled).
- Keep all 17 existing selectable CSS themes intact.
- Replace the demo-only CSS download with a download of the real file.
- Add static checks to detect missing theme assets.
- Allow direct links to individual themes via a `?theme=` query parameter.

### 1. Review and define acceptance criteria
- Check typography, contrast, spacing, cards, forms, navigation and tables.
- Establish light/dark and `prefers-reduced-motion` behaviour per theme.
- Document components that currently fail on mobile or with keyboard input.

### 2. Modernise a pilot theme
- Start with `minimalist-clean.css` for a small, measurable baseline.
- Focus on semantic tokens, spacing, focus-visible, responsive layout.
- Compare old and new screenshots at mobile and desktop widths.

### 3. Expand to other themes
- Group revisions into corporate, experimental, retro, kids and premium.
- Preserve each theme's identity; audit potentially distracting motion.
- Replace obsolete or misleading documentation and demo interactions.

### 4. Extract a maintainable gallery
- Separate large HTML/JS into small modules only if that reduces complexity.
- Add visual regression tests once the baseline screenshots are reliable.
- Publish clear integration examples for HTML and Django templates.

## Definition of done for a theme
- Works with the supported Bootstrap 5 version.
- Readable contrast and visible keyboard focus.
- Responsive and touch-friendly controls.
- No essential animation for functionality; reduced motion respected.
- No broken interactive components in the shared gallery.
- Actual CSS can be downloaded and reused.
