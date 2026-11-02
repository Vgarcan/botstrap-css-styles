# Theme Modernization Playbook — shared project workflow

## Table of contents
1. Purpose and non-negotiable constraints
2. Research and critical visual analysis
3. Art-direction proposals and review
4. Implementation on an isolated branch
5. Quality assurance and validation
6. Approval, merge and preservation of evidence
7. Definition of done

## 1. Purpose and non-negotiable constraints

**Every theme follows the same process: investigate real examples → study what works and why → propose distinct directions → implement a pilot → validate on the common gallery → iterate after visual review → merge after approval.** The goal is a library with genuinely different visual identities, not a repeated house style.

The standardized Bootstrap 5 gallery is `index.html`, **not** a disposable custom landing page for any one theme. Preserve the shared component markup and theme selector behavior.

Required architecture:
- 13 semantic `--theme-*` variables per non-empty CSS as documented in `docs/THEME_CONTRACT.md`. Preserve token names/order, verify definitions and backward-compatibility with legacy theme-specific tokens.
- `scripts/responsive-core.css` is the single editable responsive source. `scripts/sync_responsive.py` generates its appended content into each standalone CSS. Never hand-edit `BEGIN RESPONSIVE CORE v1` ... `END RESPONSIVE CORE v1` in a theme.
- One downloaded `themes/<name>.css` works standalone with Bootstrap and **without JS**. No imports from other themes and no modifications affecting other CSS files.
- Optional `themes/<name>.js` must be named exactly like its CSS basename and activated only through the shared `js/theme-core.js` lifecycle, with synchronous cleanup. No JavaScript should be required for the core appearance.
- Mobile-first, responsive behavior, safe motion, color contrast, keyboard focus and Bootstrap interactions are essential.

## 2. Research and critical visual analysis

1. Discover **multiple real, credible and diverse** references on the web. Mark source type: deployed interactive site, prototype, visual concept, design essay, or tool/demo. Include links, dates where relevant, screenshots or descriptions.
2. Study **composition** (scale, negative space, hierarchy, rhythm), **geometry** (surfaces, forms, edges), **typography**, **palette**, **lighting/material**, **motion**, and **responsive/accessibility**.
3. Separate **observations** from **inferences** and the project's own **design proposals**. Avoid copying branded/trademarked images, layouts or protected creative assets.
4. Read the existing theme CSS and the actual gallery structure before deciding scope. Record strengths worth retaining and defects worth replacing.
5. Identify aesthetic clichés that would dilute this theme or make it too similar to other collection themes.

## 3. Art-direction proposals and review

- Show 2–3 genuinely distinct design concepts, not just swatches of color.
- State how each appears on the **same** Bootstrap hero, cards, nav, forms, tabs and tables.
- Recommend a first experiment, while inviting user critique. User chooses the visual direction.
- When requested, explore further before selecting. Keep style choices traceable to research.

## 4. Implementation on an isolated branch

- Start from current `main` and make the smallest sensible set of theme-owned changes.
- Preserve gallery `index.html`, responsive generator and unrelated theme styles unless an explicitly shared bug needs an independent fix.
- Prefer theme-private design tokens; keep existing public custom property names and specialty utility classes.
- For special scenes, use CSS-only progressive enhancement where feasible, and gracefully fall back when advanced features are unsupported.
- Document why a new effect exists. Never use permanent motion just to make a theme feel alive.
- Use screenshots for comparison; no blind replacement/rewrite of large original CSS without review.

## 5. Quality assurance and validation

- Run `python3 scripts/sync_responsive.py --check`, `python3 scripts/verify_theme_contract.py`, `python3 scripts/verify_site.py`.
- Run repository W3C CSS, contrast/focus, gallery and optional-theme-runtime CI.
- Compare the SAME HTML before/after on 320, 375, 390, 430, 768, 1024, 1280 and 1440 px when supported; inspect nav open/closed.
- Confirm all 17 selectable themes remain intact and the selected CSS downloads properly.
- Check keyboard focus, modals, tabs, controls, reduced-motion and scrolling with real rendered browser screenshots.
- Record meaningful bugs, correct on the branch, rerun tests. Passing automation does not prove complete WCAG compliance.
- Before merging, remove truly redundant CSS with careful cascade and screenshot equivalence checks; maintain explicit visual invariants.

## 6. Approval, merge and preservation of evidence

- Present before/after screenshots and explain what changed.
- Ask for / follow explicit user visual approval; revise until satisfied.
- Keep implementation PR in draft until review. Do not merge before the user agrees.
- Verify PR mergeability, exact head SHA and successful CI corresponding to that head SHA; squash merge is acceptable for a cohesive theme change.
- Verify the PR is merged and `main` has the expected CSS. Maintain research and design documents as durable project context.

## 7. Definition of done

A theme is complete when its **unique visual identity**, standalone CSS download, standardized component structure, shared responsive rules, accessibility baseline, runtime switching, and screenshot comparisons have all been validated and the user approved the merge. Continue with the next theme using the same playbook.

**Status:** established as the collection's working method after Organic Glass 2.0 and Cyberpunk Neon Hardline 2.0.
