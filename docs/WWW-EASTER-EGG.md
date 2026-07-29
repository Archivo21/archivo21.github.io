# `www` Easter Egg

## Intended routing

- `https://archivo21.org/` remains the institutional homepage.
- `https://www.archivo21.org/` opens the hidden Archie homepage stored at `/www/`.
- `/www/` is deliberately excluded from the sitemap and carries `noindex, nofollow`.

## Why an edge redirect is required

The GitHub Pages custom domain is `archivo21.org`. When both the apex and `www`
DNS records point to the same Pages site, GitHub automatically redirects the
non-canonical hostname to the configured custom domain before the website's
JavaScript runs.

The root page includes a hostname check as a fallback, but the reliable route is
a Cloudflare Single Redirect that intercepts `www` first.

## Cloudflare rule

The `www` DNS record must exist and be **Proxied**.

Create a Single Redirect with:

- **Rule name:** `Archivo 21 www Easter egg`
- **When incoming requests match:** custom filter expression
- **Expression:**

  ```text
  (http.host eq "www.archivo21.org" and http.request.uri.path eq "/")
  ```

- **Then:** static URL redirect
- **Target URL:** `https://archivo21.org/www/`
- **Status code:** `302`
- **Preserve query string:** enabled

Use `302` while the Easter egg is provisional. It avoids browsers permanently
caching the destination during testing.

## Checks after deployment

1. Open `https://archivo21.org/` in a private window: the institutional homepage
   should load.
2. Open `https://www.archivo21.org/` in a private window: the Archie page should
   load at `https://archivo21.org/www/`.
3. Confirm the sound remains off until **TURN THE NOISE ON** is pressed.
4. Keyboard-tab through all fifteen linked objects and confirm each receives a
   visible dotted focus outline.
5. Open `/www/` on a portrait phone: Archie should remain central, all fifteen
   objects should remain fully tappable inside the tall stage, and the noise
   control should be reachable without rotating the device.

The routing and text-fallback structure was verified before publication. The
two rendered checks above are retained for the user's post-publication visual
inspection; no agent visual pass was performed under the PRE003 release
instruction.

The fifteenth object is a small `web.` terminal icon. It opens the Legacy
Edition at `https://web.archivo21.org/`; its visible `web.` caption is the
textual fallback for clients that cannot draw the SVG artwork.

## Smartphone layout

Portrait displays up to 700 CSS pixels wide use a separate tall composition
rather than squeezing the desktop scatter horizontally. The same fifteen
links retain deliberately mismatched sizes and animation styles, but are
distributed through seven staggered rows around Archie. Every link keeps a
minimum 48 × 48 CSS-pixel tap target; the noise control keeps a minimum
44-pixel height.

Landscape phones and larger displays retain the original wide composition.
Reduced-motion preferences continue to disable the movement in either layout.

## References

- GitHub Pages custom-domain redirects:
  <https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site>
- Cloudflare Single Redirect settings:
  <https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/>
- Cloudflare proxy status:
  <https://developers.cloudflare.com/dns/proxy-status/>
