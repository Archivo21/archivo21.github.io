# Pre-commit Checklist

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
- [ ] EXP001 is still labelled ongoing unless a reviewed conclusion now exists.
- [ ] The three public viewing links are correct.
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
- [ ] `python tools/validate_site.py` passes.
