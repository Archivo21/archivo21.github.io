# archivo21.github.io

Source repository for the Archivo 21 institutional website at **archivo21.org** and **archivo21.github.io**.

## Purpose

This repository is the public front door for Archivo 21. It introduces projects, research routes, provenance, contribution routes and rights information without replacing the canonical evidence repositories.

The first active project is [ANHQV × The Sims 2 Preservation Project](https://github.com/Archivo21/anhqv-ts2-preservation-project).

## Structure

```text
.
├── index.html                 # institutional landing page
├── index/                     # complete click-through page index
├── about/                     # purpose and research principles
├── projects/                  # project directory and ANHQV-TS2 overview
├── research/                  # curated experiment routes
├── scaffold/                  # Project Scaffold, records and downloads
├── contribute/                # participation and recruitment
├── provenance/                # founding and attribution summary
├── rights/                    # licensing and third-party material
├── contact/                   # institutional contact routes
├── www/                       # hidden, noindex Archie Easter egg
├── assets/                    # CSS, JavaScript, icons and image policy
├── reference/                 # migrated source snapshots; not canonical
├── docs/                      # deployment, migration and review notes
└── .github/                   # issue forms and pull-request template
```

## Publish

This site has no build step and no external runtime dependencies. GitHub
Pages is the production origin; the repository is not published through a
ChatGPT Site.

1. Create the public repository `Archivo21/archivo21.github.io`.
2. Add these files at the repository root.
3. In **Settings → Pages**, select **Deploy from a branch**, `main`, `/(root)`.
4. In the Pages settings, save `archivo21.org` as the custom domain.
5. Configure the corresponding Cloudflare DNS records and then enforce HTTPS after GitHub makes it available.

The included `CNAME` file contains `archivo21.org`. Remove it before the first commit if the custom domain is not ready.

See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) for the complete checklist.
Change records use the decorative-only or full tier defined in
[`docs/CHANGE-DOCUMENTATION-POLICY.md`](docs/CHANGE-DOCUMENTATION-POLICY.md);
both tiers require a recoverable pre-change checkpoint retained for at least
28 days.

The `www` Easter egg contains fifteen linked objects, including the Project
Scaffold and the GitHub-backed Legacy Edition. See
[`docs/WWW-EASTER-EGG.md`](docs/WWW-EASTER-EGG.md).

## Contact activation

Institutional addresses are present in `assets/js/config.js` but are hidden while:

```js
contactRoutingActive: false
```

After all three Cloudflare routes have been tested, change the value to `true` and review `/contact/`, `/rights/`, `NOTICE.md`, `SECURITY.md`, and any Code of Conduct contact text before publishing.

## Canonical records and migration

Files under `reference/` are dated migration snapshots used to prepare the first website. Their canonical, evolving versions remain in the ANHQV-TS2 repository or its contributor archive. See [`docs/MIGRATION-MAP.md`](docs/MIGRATION-MAP.md).

## Licence

Original website text and structures are licensed under CC BY-SA 4.0 unless a file states otherwise. Third-party material is excluded. See [`NOTICE.md`](NOTICE.md).
