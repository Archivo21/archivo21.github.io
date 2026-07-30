#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
from collections import deque
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        for key in ('href','src'):
            if key in d:
                self.links.append((tag, key, d[key]))

html_files = sorted(ROOT.rglob('*.html'))
main_site_pages = [html for html in html_files if html.relative_to(ROOT).as_posix() != 'www/index.html']
html_set = set(html_files)
link_graph = {html: set() for html in html_files}

def local_target(html, value):
    parsed = urlparse(value)
    if parsed.scheme in ('http', 'https') or value.startswith(('mailto:', 'tel:', 'data:', 'javascript:')):
        return None
    target_text = unquote(parsed.path)
    if not target_text:
        return html
    if target_text.startswith('/'):
        target = ROOT / target_text.lstrip('/')
    else:
        target = html.parent / target_text
    if target_text.endswith('/'):
        target = target / 'index.html'
    elif target.is_dir():
        target = target / 'index.html'
    return target.resolve()

for html in html_files:
    parser = LinkParser()
    try:
        parser.feed(html.read_text(encoding='utf-8'))
    except Exception as exc:
        errors.append(f'{html.relative_to(ROOT)}: parse error: {exc}')
        continue
    for tag, key, value in parser.links:
        if not value or value.startswith(('#','mailto:','tel:','data:','javascript:')):
            continue
        target = local_target(html, value)
        if target is None:
            continue
        if not target.exists():
            errors.append(f'{html.relative_to(ROOT)}: missing {key} target {value}')
        elif key == 'href' and target in html_set:
            link_graph[html].add(target)

required = ['index.html','index/index.html','.nojekyll','.gitignore','.gitattributes','.github','CNAME','NOTICE.md','LICENSE']
for item in required:
    if not (ROOT/item).exists():
        errors.append(f'missing required item: {item}')

for p in ROOT.rglob('*'):
    if p.is_file() and p.stat().st_size == 0 and p.name != '.nojekyll':
        errors.append(f'unexpected zero-byte file: {p.relative_to(ROOT)}')

legacy_url = 'https://web.archivo21.org/'
for html in main_site_pages:
    markup = html.read_text(encoding='utf-8')
    if markup.count(legacy_url) < 2:
        errors.append(f'{html.relative_to(ROOT)}: missing persistent header/footer Legacy Edition links')
    if 'class="legacy-escape"' not in markup or 'style="display:inline-block;background:#0b0906' not in markup:
        errors.append(f'{html.relative_to(ROOT)}: Legacy Edition header link is not fail-open raw HTML')

home_markup = (ROOT / 'index.html').read_text(encoding='utf-8')
if '<a href="/www/">There is a side door.</a>' not in home_markup:
    errors.append('index.html: missing documented discoverable /www/ side-door link')
if 'href="/scaffold/"' not in home_markup:
    errors.append('index.html: missing direct Project Scaffold link')
if 'href="/index/"' not in home_markup:
    errors.append('index.html: missing direct complete-index link')
if '200+ pages across both editions' not in home_markup:
    errors.append('index.html: public-corpus summary is missing')

www_markup = (ROOT / 'www' / 'index.html').read_text(encoding='utf-8')
if www_markup.count('class="retro-link ') != 15:
    errors.append('www/index.html: expected exactly fifteen linked objects')
if (
    legacy_url not in www_markup
    or 'icon-legacy' not in www_markup
    or '<span class="icon-caption">web.</span>' not in www_markup
    or '<span class="sr-only">Legacy Edition: web.archivo21.org</span>' not in www_markup
):
    errors.append('www/index.html: missing text-backed Legacy Edition icon')
if (
    'id="icon-scaffold"' not in www_markup
    or 'item-13" href="/scaffold/"' not in www_markup
    or '<span class="sr-only">Archivo 21 Project Scaffold</span>' not in www_markup
):
    errors.append('www/index.html: missing literal Scaffold object')

for html in main_site_pages:
    markup = html.read_text(encoding='utf-8')
    if 'class="footer-links"' in markup and 'href="/index/"' not in markup:
        errors.append(f'{html.relative_to(ROOT)}: footer is missing the site index')

root_page = (ROOT / 'index.html').resolve()
visited = {root_page}
queue = deque([root_page])
while queue:
    page = queue.popleft()
    for target in link_graph.get(page, ()):
        if target not in visited:
            visited.add(target)
            queue.append(target)
unreachable = sorted(html_set - visited)
for html in unreachable:
    errors.append(f'{html.relative_to(ROOT)}: not reachable by links from the homepage')

placeholder_patterns = (
    r'\blorem ipsum\b',
    r'\bplaceholder text\b',
    r'\bexample text\b',
    r'\bTBD\b',
    r'\bTODO\b',
)
for html in html_files:
    visible_copy = re.sub(r'<[^>]+>', ' ', html.read_text(encoding='utf-8'))
    for pattern in placeholder_patterns:
        if re.search(pattern, visible_copy, flags=re.IGNORECASE):
            errors.append(f'{html.relative_to(ROOT)}: placeholder-like public copy matches {pattern}')

if errors:
    print('FAIL')
    for err in errors:
        print('-', err)
    sys.exit(1)
print(
    f'PASS: {len(html_files)} HTML files; internal targets resolved; '
    'every page is click-reachable from the homepage; required repository files present.'
)
