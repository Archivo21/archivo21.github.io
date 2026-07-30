# Navigation and public-publication record — 2026-07-30

## Classification

Tier F. This release changes public wording, route discovery, navigation and
the relationship between the main and Legacy Editions.

## Pre-change state

- Repository: `Archivo21/archivo21.github.io`
- Branch: `main`
- Commit: `bb20b47`
- Recoverable Git bundle retained for at least 28 days
- Bundle SHA-256:
  `b22d28f3763870ea977e783a23a7bedf3661d0c0d13b66f26dd64e5c907efa70`

## Scope

- Rewrite the homepage as the public front door to an institution with more
  than 200 pages across its two editions.
- Add a complete main-site index and link it from every standard footer.
- Link the Project Scaffold directly from the homepage.
- Keep `/www/` at exactly fifteen linked objects.
- Replace its duplicate contribution object with a literal scaffolding icon
  linked to `/scaffold/`.
- Retain the fifteenth GitHub-backed Legacy Edition object and its complete
  plain-text fallback.
- Add the new index and Scaffold family to the sitemap.
- Enforce internal-target validity, placeholder-copy rejection and click-only
  reachability from `/` for every HTML page.

## Verification

`python3 tools/validate_site.py` must pass before publication. The resulting
commit and live GitHub Pages responses are recorded after deployment.
