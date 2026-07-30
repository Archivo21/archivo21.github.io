# Validation Report

**Prepared:** 2026-07-30
**Result:** PASS

## Automated checks

- HTML pages: 18
- Internal `href` and `src` targets: resolved
- Pages reachable by click from `/`: 18 of 18
- Required repository and GitHub Pages files: present
- Unexpected zero-byte files: 0
- Standard pages carrying fail-open Legacy Edition header links: 17
- Standard pages carrying Legacy Edition footer links: 17
- Standard footers carrying the complete site index: 17
- Homepage direct routes: complete index, Scaffold, `/www/`, institutional
  records, projects, research and Legacy Edition
- Homepage public-corpus summary: present
- `/www/` linked objects: exactly 15
- `/www/` Scaffold object: literal scaffolding icon plus accessible text
- `/www/` Legacy object: icon caption plus complete plain-text fallback
- Placeholder-like interface copy: 0 matches
- Sitemap XML: includes the main index and complete Scaffold route family

## Public structure

The homepage now introduces Archivo 21 as an institution before presenting
the current project. It provides direct routes into the institutional record,
projects, research, Scaffold, provenance and complete index, and explains that
the public corpus spans more than 200 pages across the main and Legacy
Editions.

The complete index and persistent footer link ensure that every main-site HTML
page can be reached by ordinary click interaction beginning at `/`. The
Legacy Edition independently enforces the same property for its own corpus.

## Hosting boundary

The main site is published from `Archivo21/archivo21.github.io` through GitHub
Pages at `archivo21.org`. The Legacy Edition is published from
`Archivo21/archivo21-legacy-edition` through GitHub Pages at
`web.archivo21.org`. A ChatGPT Site is not a production origin for either
edition.

## Remaining live checks

- Confirm the GitHub Pages publication completes for the resulting commit.
- Confirm `/`, `/index/`, `/scaffold/` and `/www/` return successful public
  responses.
- Confirm the Legacy Edition link opens `https://web.archivo21.org/`.
- User visual review remains separate from this structural release gate.
