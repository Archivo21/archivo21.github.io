# Pre-commit Checklist

## Change record

- [ ] Classify the change under
      [`CHANGE-DOCUMENTATION-POLICY.md`](CHANGE-DOCUMENTATION-POLICY.md).
- [ ] Record the exact pre-change ref and retain a recoverable checkpoint for
      at least 28 days.
- [ ] If any part is not decorative-only, use the full record.

## Repository identity

- [ ] Repository name is exactly `archivo21.github.io`.
- [ ] Owner is `Archivo21`.
- [ ] Default branch is `main`.
- [ ] The root contains `index.html`, `.nojekyll`, `.gitignore`, `.gitattributes`, and `.github/`.

## Content

- [ ] lcd97 is used as the public contributor name where intended.
- [ ] `ANHQV-HUM-001` refers to lcd97.
- [ ] `ANHQV-AI-001` refers to Archivo 21.
- [ ] ANHQV-TS2 status and release language match the canonical repository.
- [ ] EXP000 is labelled concluded and its retrospective documentation limits remain explicit.
- [ ] EXP001 is still labelled ongoing unless a reviewed conclusion now exists.
- [ ] The approved EXP000 Short is the only public recording-platform URL.
- [ ] Any newer local files have replaced stale migration snapshots.

## Privacy and rights

- [ ] No personal Gmail address is present.
- [ ] No passwords, recovery codes, keys, tokens, private evidence, raw recordings, or financial records are present.
- [ ] Contact routing remains disabled until tested.
- [ ] Every new image has alt text and a rights record.
- [ ] Third-party material is not presented as CC BY-SA project material.

## Deployment

- [ ] `CNAME` is present only if `archivo21.org` is ready.
- [ ] Pages publishes from `main` and `/(root)`.
- [ ] Custom domain is also saved in GitHub Pages settings.
- [ ] Cloudflare DNS and DNSSEC are reviewed.
- [ ] HTTPS works before advertising the domain.
- [ ] The `www` Cloudflare redirect opens `/www/` without replacing the apex homepage.
- [ ] All fourteen Easter-egg objects remain keyboard-operable links.
- [ ] All fourteen Easter-egg objects remain fully tappable in the portrait-phone composition.
- [ ] `python tools/validate_site.py` passes.
