# Image assets

Image-specific provenance and rights limits are recorded below. Inclusion in
this directory does not imply that Archivo 21 owns or relicenses third-party
marks, screenshots, characters or source material visible inside a composite.

## Official provisional Archivo 21 emblem

`archivo21-provisional-header-logo.jpg` is the user-supplied official
provisional Archivo 21 logo preserved as the unchanged opaque source master
from 2026-07-27.

- role: project branding, not research evidence;
- dimensions: 1254 × 1254 pixels;
- status: provisional source master, preserved as supplied without overwriting
  the favicon artwork or any earlier branding record;
- rights: Archivo 21 claims no ownership of third-party game imagery, names,
  logos or trade marks visible in the composite.

The exact source master has SHA-256:

```text
62bad7f03f1f9b522e08ee4f1a113c4652428c8be0dae24dbf57d2f14be2c06f
```

`archivo21-provisional-logo-transparent.png` is the lossless transparent web
derivative used from 2026-07-27:

- it is the 1254 × 1254 source used for the institutional homepage hero and
  future full-size presentation;
- the institutional homepage presents the same emblem at a larger scale as
  the centre of its responsive first viewport;
- the exterior black field alone was removed by four-corner connected
  background extraction at 4% colour tolerance;
- visible foreground pixels come from the supplied source master: no
  generative retouching, redrawing, text replacement or rearrangement is
  present in the deployed derivative;
- black panels, typography, shadows and other dark areas inside the emblem
  remain opaque;
- an image-generation chroma pass was used only as a silhouette reference and
  rejected as a foreground source because it did not satisfy the
  pixel-preservation requirement.

The transparent derivative is 1254 × 1254 pixels and has SHA-256:

```text
6ce29cc2151c512783760385cfb336dc6b96ed12bde9fa3c90631f8d372d73d0
```

`archivo21-provisional-logo-transparent-header.png` is a 360 × 360 lossless
responsive-header derivative. All twelve conventional page headers use it,
including the homepage header, at the previous 120-pixel desktop and 86-pixel
mobile presentation. The full-size emblem remains separately centred in the
homepage hero. Its SHA-256 is:

```text
2d98c10c7b5f088364e346251cb894eedd3ee9930a009d7d74eed6b7eb16990a
```

## Archie `www` assets

The hidden `/www/` page uses two transparent PNGs:

- `archie-www-wave.png` — extracted from the user-supplied established Archie
  reference;
- `archie-www-easter-egg.png` — a generated alternate side-step pose derived
  from that reference on 2026-07-27.

Both images depict the Archivo 21 character rather than a television character.
The surrounding linked objects are original inline SVG graphics stored in
`www/index.html`; no graphics were copied from the reference television clip.

The alternate pose was generated with OpenAI image generation and its flat
chroma-key background was removed locally. The final file has an alpha channel
and SHA-256:

```text
ab3e664e85ae6a822f41e68885810dff4af2f03f7481a8225241796db2f45d51
```

Before adding an image, record:

- creator or source;
- copyright or licence status;
- permission or legal basis;
- alt text;
- whether it is an original, reference, evidence item, or decorative asset.

A future social preview image should be exported as `social-card.png` (recommended 1200 × 630 px) and then added to each page's Open Graph metadata.
