# Deployment — archivo21.github.io

## Before the first commit

- [ ] Create the public GitHub repository `Archivo21/archivo21.github.io`.
- [ ] Add any local files that were missing from the browser-uploaded ANHQV-TS2 repository.
- [ ] Review `docs/MIGRATION-MAP.md` and replace any snapshot that has a newer canonical version.
- [ ] Confirm `.gitignore`, `.gitattributes`, `.github/`, and `.nojekyll` are present.
- [ ] Decide whether `archivo21.org` is ready. If not, remove `CNAME` before committing.
- [ ] Keep `contactRoutingActive: false` until every email alias has been tested.

## GitHub Pages

This repository is designed to publish directly from the default branch without a build workflow.

1. Push the files to `main`.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select `main` and `/(root)`.
5. Save.

## Custom domain

1. In **Settings → Pages**, enter `archivo21.org` in **Custom domain** and save it.
2. Configure the apex-domain records in Cloudflare according to GitHub's current Pages documentation.
3. Keep Cloudflare's proxy disabled while GitHub verifies and provisions the domain unless current GitHub/Cloudflare guidance says otherwise.
4. Confirm both `archivo21.org` and `www.archivo21.org` behave as intended.
5. Enable **Enforce HTTPS** when GitHub offers it.
6. Confirm `CNAME` still contains only `archivo21.org`.

The `CNAME` file alone does not finish custom-domain configuration; the domain must also be saved in the repository's Pages settings.

## Contact routes

Configure and test:

- `contact@archivo21.org` — general enquiries;
- `conduct@archivo21.org` — private conduct reports;
- `rights@archivo21.org` — attribution, permission, provenance and rights enquiries.

After receiving a successful test through each route:

1. change `contactRoutingActive` to `true` in `assets/js/config.js`;
2. check `/contact/` and `/rights/`;
3. update `NOTICE.md`, `SECURITY.md`, and any Code of Conduct file if their temporary wording is no longer needed;
4. send a second test from an unrelated address.

## GitHub repository settings

Recommended:

- description: `Independent digital preservation, research, and documentation.`
- website: `https://archivo21.org`
- topics: `digital-preservation`, `research`, `documentation`, `fan-studies`, `game-research`
- enable issues;
- enable private vulnerability reporting;
- protect `main` after the first stable deployment;
- require pull-request review when more maintainers join.

## Final checks

Run `python tools/validate_site.py` from the repository root. Then review:

- mobile navigation;
- keyboard focus order;
- 404 page;
- canonical links;
- absence of public recording-platform URLs;
- custom-domain HTTPS;
- absence of personal Gmail addresses or credentials;
- whether the website still describes the project state accurately.
