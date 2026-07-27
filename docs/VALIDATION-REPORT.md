# Validation Report

**Prepared:** 2026-07-27
**Result:** PASS

## Automated checks

- HTML pages: 13
- Candidate files: 67
- Internal file targets: resolved
- Required repository files: present
- Conventional institutional headers: 12
- Headers using the transparent provisional emblem: 12
- Headers using the angular emblem housing and ochre navigation rail: 12
- Legacy CSS `A21` header marks: 0
- Opaque source-master dimensions: 1254 × 1254 pixels
- Opaque source-master SHA-256 remains
  `62bad7f03f1f9b522e08ee4f1a113c4652428c8be0dae24dbf57d2f14be2c06f`
- Full transparent derivative: 1254 × 1254 PNG with alpha
- Full transparent derivative SHA-256:
  `6ce29cc2151c512783760385cfb336dc6b96ed12bde9fa3c90631f8d372d73d0`
- Header derivative: 360 × 360 PNG with alpha
- Header derivative SHA-256:
  `2d98c10c7b5f088364e346251cb894eedd3ee9930a009d7d74eed6b7eb16990a`
- Full derivative corner alpha: transparent
- Sampled yellow sign, black plaque and CRT regions: opaque
- YAML files parsed: 3
- JSON files parsed: 1
- Sitemap XML: parsed
- JavaScript syntax checks: PASS
- CSS delimiters, strings and comments: balanced
- Desktop header rail/nav breakpoint: above 850 CSS pixels
- Collapsible mobile header/nav breakpoint: 850 CSS pixels and below
- HTML parser check: PASS
- Duplicate HTML IDs: 0
- Images without an `alt` attribute: 0
- Local HTTP routes/assets tested: 15
- Local HTTP failures: 0
- Homepage institutional route cards: 3
- Homepage primary calls to action: 2
- Easter-egg linked objects: 14
- Easter-egg accessible link names: 14
- Distinct procedural sound cues: 14
- Easter-egg indexing directive: `noindex, nofollow`

## Responsive findings

- The internal-page emblem remains 120 CSS pixels at the desktop maximum and
  86 CSS pixels below 850 pixels, matching the previous presentation.
- The homepage hero uses a three-column emblem-centred stage above 1120 pixels,
  a centred emblem above two supporting columns between 851 and 1120 pixels,
  and a single vertical flow below 851 pixels.
- Below 520 pixels, homepage buttons expand to the available width, the status
  ledger becomes a single column and all layout grids collapse.
- The full emblem is constrained to the available content width, so it does not
  require phone rotation.
- Short landscape displays constrain the hero emblem to 68% of the viewport
  height.
- The mobile navigation/header offset continues to use the shared responsive
  header height.
- The desktop rail reserves a 158 × 142 CSS-pixel angular emblem housing and
  aligns the navigation above a four-pixel ochre structural line.
- The mobile rail compresses to a 112 × 104 CSS-pixel housing, retains the
  86-pixel emblem and anchors the expandable menu below the shared 104-pixel
  header height.
- Portrait `/www/` keeps its independent tall composition and remains
  unaffected by the institutional homepage redesign.

## Manual findings

- The user-supplied JPEG remains byte-for-byte unchanged as the source master.
- The deployed transparent foreground uses the source master’s original
  decoded pixels; an image-generation chroma reference was rejected as a
  foreground source after it failed the exact-preservation requirement.
- Exterior transparency was removed only from the four corner-connected
  background regions. Black lettering, panels, shadows and dark game details
  inside the emblem remain visible and opaque.
- The homepage is now composed around the emblem: institutional declaration,
  status ledger, current-project file, method card and three linked collection
  routes.
- Site-wide header wording, destinations and active-page semantics are
  unchanged; the new rail is a visual treatment of the existing navigation.
- `docs/CHANGE-DOCUMENTATION-POLICY.md` records the decorative-only and full
  documentation tiers. Both retain a recoverable pre-change checkpoint for at
  least 28 days.
- The site uses no external fonts, analytics, trackers, package manager or
  runtime framework.
- Contact aliases remain hidden while `contactRoutingActive` is `false`.
- The approved EXP000 Short remains the only public recording-platform URL.
- The website continues to present ANHQV-TS2 as the canonical research
  repository rather than duplicating its full tree.
- EXP000 continues to credit the observation line to the persistent contributor
  identity `Archivo 21 (ANHQV-AI-001)`.

## Remaining live checks

- Confirm the GitHub Pages deployment completes for the published commit.
- Confirm the homepage, all transparent assets, EXP000 and `/www/` return
  successful public responses after publication.
- Inspect the live homepage at one desktop and one narrow portrait viewport
  when an interactive browser is available.
- Add and test the separate Cloudflare `www` redirect described in
  `WWW-EASTER-EGG.md`.
