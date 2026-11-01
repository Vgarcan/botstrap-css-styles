# GitHub Pages preview environment

## Goal
Host the existing Bootstrap theme showcase as a static visual laboratory
before gradually modernising each theme. The original CSS files stay in
`themes/` and are edited incrementally.

## Deployment
- Workflow: `.github/workflows/deploy-pages.yml`
- Source: the root `index.html` and `themes/*.css` files.
- Published destination (once GitHub Pages is enabled):
  https://vgarcan.github.io/botstrap-css-styles/
- Every push to `main` starts verification and, if successful, deployment.
- A pull request **does not** publish a live site until merged.

## One-time account configuration
1. **Repository visibility**: this repository was private at setup time.
   GitHub Pages with GitHub Free requires a **public** repository.
   GitHub Pro/Team/Enterprise may deploy from a private repository,
   but the Pages website itself is still public.
   Decide about visibility before enabling the site.
2. Navigate to **Settings > Pages** in this repository.
3. Under **Build and deployment**, select **GitHub Actions** as the source.
4. After the workflow is merged to `main`, review the
   **Actions > Deploy theme laboratory** run.
5. Open the published site from **Settings > Pages**.
   Do not assume that the site is live until a successful deployment.

## Local preview
Start a basic HTTP server from the repository root:

```bash
python3 -m http.server 8000
```

Open http://localhost:8000/ in your browser. Running from `file://` is
not recommended because CSS downloads use `fetch()`.

## How we modernise
- Keep the shared component showcase stable so visual regressions are visible.
- Change one theme stylesheet at a time.
- Test on narrow mobile and desktop widths, keyboard navigation,
  colour contrast, and reduced-motion settings.
- Make sure the downloaded CSS matches the current selected theme.
- Check the site after each merged pull request.

## Known baseline issues
- `themes/corporate-blue.css` is empty and not selectable.
- The README mentions `docs.html`, which is not in the repository.
- The showcase currently loads Bootstrap 5.3.2 and Font Awesome 6.4.0
  from CDNs; dependency upgrades should be tested separately.
- The source HTML is large; future work can separate the gallery's
  controls and metadata without rewriting all themes simultaneously.
