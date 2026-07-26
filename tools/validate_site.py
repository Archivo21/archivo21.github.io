#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
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
        parsed = urlparse(value)
        if parsed.scheme in ('http','https'):
            continue
        target_text = unquote(parsed.path)
        if target_text.startswith('/'):
            target = ROOT / target_text.lstrip('/')
        else:
            target = html.parent / target_text
        if target_text.endswith('/'):
            target = target / 'index.html'
        elif target.is_dir():
            target = target / 'index.html'
        if not target.exists():
            errors.append(f'{html.relative_to(ROOT)}: missing {key} target {value}')

required = ['index.html','.nojekyll','.gitignore','.gitattributes','.github','CNAME','NOTICE.md','LICENSE']
for item in required:
    if not (ROOT/item).exists():
        errors.append(f'missing required item: {item}')

for p in ROOT.rglob('*'):
    if p.is_file() and p.stat().st_size == 0 and p.name != '.nojekyll':
        errors.append(f'unexpected zero-byte file: {p.relative_to(ROOT)}')

if errors:
    print('FAIL')
    for err in errors:
        print('-', err)
    sys.exit(1)
print(f'PASS: {len(html_files)} HTML files; internal file targets resolved; required repository files present.')
