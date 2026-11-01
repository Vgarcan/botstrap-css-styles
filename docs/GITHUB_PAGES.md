# GitHub Pages — live theme laboratory

## Goal
Use the repository's existing GitHub Pages site to compare and modernise
the Bootstrap themes gradually, without replacing their original identities.

## Publishing setup (confirmed 1 November 2026)
- Repository: public, with default branch `main`.
- GitHub Pages: configured by the owner to publish from `main`.
- GitHub's automatic **pages build and deployment** completed successfully.
- Published site address:
  https://vgarcan.github.io/botstrap-css-styles/
- Site source: `index.html` and `themes/*.css` in the repository root.
- **Do not** add an additional GitHub Actions deployment workflow. GitHub
  already handles publishing the selected branch through its built-in Pages job.
- GitHub Pages publishing can take a little time after a merge.
  Check **Actions > pages build and deployment** for the actual result.

The owner has already configured the source. There is no need to change
**Settings > Pages** while the current branch-based publication works.

## Working on a theme
1. Create a short-lived feature branch from `main`.
2. Modify the selected theme, with small, reviewable changes.
3. Open a pull request. The validation workflow checks CSS references.
4. Check mobile, desktop, keyboard, focus, contrast and reduced motion.
5. Merge into `main` when ready; the existing Pages setup republishes it.
6. Compare before/after on the same gallery page.

Shareable theme links use `?theme=<theme-id>`, for example:
https://vgarcan.github.io/botstrap-css-styles/?theme=minimalist-clean

## Local preview
From the repository root, run:

```bash
python3 -m http.server 8000
```

Then visit http://localhost:8000/ . Use HTTP rather than `file://` because
downloading the CSS uses `fetch()`.

## Known baseline issues
- `themes/corporate-blue.css` is empty and not selectable.
- `docs.html` previously mentioned in the README was never committed.
- The page still uses Bootstrap 5.3.2 and Font Awesome 6.4.0 via CDN,
  so dependency upgrades need testing.
- The large `index.html` should be simplified in a separate change.
