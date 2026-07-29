# Display and degradation test matrix

**Recorded:** 29 July 2026
**Scope:** Institutional main site (`archivo21.org`), its `/www/` side door and the permanent route to the Legacy Edition (`web.archivo21.org`).

## Fail-open invariant

Every institutional HTML page contains two direct, raw-HTML links to `https://web.archivo21.org/`:

1. a high-contrast header link, **Use the Legacy Edition (plain HTML)**, with the contrast and boundary colours carried in an inline style; and
2. a permanent footer link with the same destination.

Neither depends on JavaScript, a stylesheet, an image, or a web font. The header link is deliberately retained in ordinary reading order so it remains visible if CSS and JavaScript are absent.

The homepage also carries the intentionally quiet `/www/` discovery link, **There is a side door.** The Archie page then provides a separate, text-backed `web.` icon: browsers which cannot render its SVG still render the linked `web.` text.

## Matrix

| Case | Method | Required result | Status |
|---|---|---|---|
| Normal desktop | 1440 × 900; CSS/JS enabled | Header and footer Legacy Edition links are visible and usable; normal navigation is intact. | Static structure verified |
| Large desktop | 2560 × 1440; CSS/JS enabled | Header does not overlap navigation; footer link wraps rather than clips. | CSS/markup review complete; visual release check pending |
| Portrait phone | 360 × 800; CSS/JS enabled | Menu and the Legacy Edition link form separate, tappable rows; no horizontal overflow. | CSS/markup review complete; visual release check pending |
| Landscape phone | 800 × 360; CSS/JS enabled | Header remains readable; link and menu remain independently tappable. | CSS/markup review complete; visual release check pending |
| JavaScript unavailable | Block `assets/js/config.js` and `assets/js/site.js` | The header and footer Legacy Edition links work because they are ordinary HTML; no JavaScript is needed to reach the fallback. | Static structure verified |
| External CSS unavailable | Block `assets/css/site.css` | Inline header Legacy Edition link stays high contrast and underlined; footer text link remains present. | Static structure verified |
| Image failure | Block a non-critical image | The header Legacy Edition link and footer link remain; ordinary textual content remains usable. | Static structure verified |
| SVG unavailable on `/www/` | Disable SVG rendering or use a text-only client | The `web.` caption remains a direct link to the Legacy Edition. | Static structure verified |
| Keyboard-only | Tab through each page | Skip link, primary navigation, header Legacy link, main content, and footer Legacy link receive a visible focus indicator. | CSS/markup review complete; interactive release check pending |
| Legacy textual client | Read source without CSS, JS or images | `Use the Legacy Edition (plain HTML)` and `web.` are both rendered as usable hyperlinks. | Static structure verified |

## Release disposition

The structural and fail-open checks above are the release evidence for this
change. On 29 July 2026 the user explicitly directed publication without an
agent-performed visual pass. The rendered desktop and mobile checks therefore
remain a **user-owned post-publication inspection**, not an unperformed claim
of validation. Record any layout deviation here rather than removing the
raw-HTML escape route.
