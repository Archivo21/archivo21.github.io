# Validation Report

**Prepared:** 2026-07-27
**Result:** PASS

## Automated checks

- HTML pages: 13
- Candidate files: 64
- Internal file targets: resolved
- Required repository files: present
- Conventional institutional headers: 12
- Headers using the official provisional logo: 12
- Legacy CSS `A21` header marks: 0
- Header-logo source dimensions: 1254 × 1254 pixels
- Header-logo deployed SHA-256 matches the supplied master
- YAML files parsed: 3
- JSON files parsed: 1
- Sitemap XML: parsed
- Easter-egg linked objects: 14
- Easter-egg accessible link names: 14
- Distinct procedural sound cues: 14
- Easter-egg indexing directive: `noindex, nofollow`
- JavaScript syntax checks: PASS
- Portrait geometry checked at 320, 360, 375, 390, 412 and 430 CSS pixels
- Portrait Easter-egg links outside their stage: 0
- Portrait Easter-egg link targets below 48 × 48 CSS pixels: 0
- Portrait Easter-egg link overlaps above 15% of the smaller target: 0
- Mobile navigation/header offset uses the shared responsive header height
- HTML parser check: PASS

## Manual findings

- The site uses no external fonts, analytics, trackers, package manager, or build framework.
- Contact aliases are hidden while `contactRoutingActive` remains `false`.
- The user-supplied official provisional logo is used only as project branding;
  its third-party rights limits and exact integrity hash are documented.
- The approved EXP000 Short is the only public recording-platform URL.
- The website presents ANHQV-TS2 as the canonical research repository rather than duplicating its full tree.
- The hidden `/www/` route uses original Archivo 21 graphics and remains silent
  until the visitor activates its noise control.
- The ordinary institutional navigation and page structure are unchanged; only
  the old text-and-CSS brand is replaced by the official provisional logo.
- Portrait `/www/` uses its own tall composition and does not require device
  rotation.
- EXP000 credits the observation line to the persistent contributor identity
  `Archivo 21 (ANHQV-AI-001)`.

## Remaining human checks

- Test Cloudflare email routes and DNS.
- Add and test the Cloudflare `www` redirect described in `WWW-EASTER-EGG.md`.
- Confirm Pages, HTTPS, rendered header sizing and portrait `/www/` after publication.
