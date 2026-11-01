# Responsive layout contract v1

## Contents
1. Objective
2. Architecture and compatibility
3. Breakpoints and acceptance criteria
4. Reusing and updating the CSS
5. Verification and remaining manual QA

## 1. Objective
Every visual theme must adapt from small phones through tablets to desktop
without hiding content or causing horizontal page scrolling. Visual identities
remain different; responsive behaviour is consistent.

## 2. Architecture
The single editable source is `scripts/responsive-core.css`. The build script
`scripts/sync_responsive.py` embeds its content at the end of all **18**
non-empty stylesheets (17 selectable plus the legacy `bootstrap-theme.css`).
Each CSS file is still standalone, so downloads and Django static integration
do **not** rely on a second HTTP request or a CSS `@import`.

Theme-specific rules remain in their original files; the responsive core handles
shared compatibility concerns. Do not manually edit the marked generated block.
The empty, unselected `corporate-blue.css` remains untouched.

## 3. Breakpoints and acceptance criteria

| Target | Representative viewports | Acceptance |
| --- | --- | --- |
| Small phones | 320, 375 px | No document-level horizontal scrolling |
| Phones | 390, 430 px | Readable text and reachable controls |
| Tablets | 768, 1024 px | Fluid columns and contained content |
| Desktops | 1280, 1440 px | Components remain usable and well aligned |

CSS uses mobile adjustments up to 767.98 px and tablet adjustments from 768
through 1199.98 px. Bootstrap 5's existing grid supplies the major layout.
A responsive table **may** scroll within `.table-responsive`; the full page
must not scroll horizontally just to view a table.

Touch targets have a 44 px minimum on coarse-pointer devices. Heading sizes
scale fluidly on phones and tablets. Media and offcanvas widths are contained.
Every theme respects `prefers-reduced-motion`.

The gallery's theme selector is a bottom-right floating button on desktop
and a scrollable near-full-screen panel on phones, not a control covering the
mobile navigation. It remains separate from each reusable theme's CSS.

## 4. Development workflow

```bash
# Update generated responsive blocks after editing the shared source.
python3 scripts/sync_responsive.py

# Static CI checks.
python3 scripts/sync_responsive.py --check
python3 scripts/verify_theme_contract.py
python3 scripts/verify_site.py
```

Import Bootstrap CSS first, then one complete theme stylesheet as documented in
`docs/THEME_CONTRACT.md`. The gallery still uses `main` as its Pages source.

## 5. Verification and limitations

The PR workflow performs static checks and runs Chromium viewport tests for
all 17 gallery themes, including opening the selector on mobile. Browser tests
need installation of Playwright/Chromium and are intentionally separated from
the fast static checks.

The automated checks detect overflow, theme loading and basic controls, but
**do not prove** correct visual composition, colour contrast, screen-reader
support, or device-specific Safari behaviour. Before considering responsive
work finished, inspect the screenshot evidence and manually check iOS Safari,
Android Chrome, tablet portrait/landscape and desktop keyboard use.
