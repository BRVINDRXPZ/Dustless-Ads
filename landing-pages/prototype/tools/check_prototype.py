#!/usr/bin/env python3
"""Dependency-free checks for the static Phase 5 prototype."""
from html.parser import HTMLParser
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
class P(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.titles=[];self.h1=0;self.img_missing=[];self.labels=set();self.controls=[];self.track=[];self._title=False
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='a' and d.get('href'):self.links.append(d['href'])
  if t=='title':self._title=True
  if t=='h1':self.h1+=1
  if t=='img' and 'alt' not in d:self.img_missing.append(d.get('src','?'))
  if t=='label' and d.get('for'):self.labels.add(d['for'])
  if t in ('input','select','textarea') and d.get('type')!='hidden':self.controls.append((d.get('id'),d.get('name')))
  if d.get('data-track'):self.track.append(d['data-track'])
 def handle_endtag(self,t):
  if t=='title':self._title=False
 def handle_data(self,d):
  if self._title:self.titles.append(d.strip())
errors=[]; titles={}; htmls=list(ROOT.rglob('*.html'))
for f in htmls:
 p=P();txt=f.read_text();p.feed(txt); title=''.join(p.titles)
 if not title:errors.append(f'{f}: missing title')
 elif title in titles:errors.append(f'{f}: duplicate title with {titles[title]}')
 else:titles[title]=f
 if not re.search(r'<meta\s+name="description"',txt,re.I):errors.append(f'{f}: missing meta description')
 if p.h1!=1:errors.append(f'{f}: expected one H1, got {p.h1}')
 for x in p.img_missing:errors.append(f'{f}: image missing alt: {x}')
 for ident,name in p.controls:
  if not ident or ident not in p.labels:errors.append(f'{f}: unlabeled control {name or ident}')
 for href in p.links:
  if href.startswith(('#','http:','https:','tel:','mailto:')):continue
  target=(f.parent/href.split('?',1)[0].split('#',1)[0]).resolve()
  if not target.exists():errors.append(f'{f}: broken link {href}')
# Source-level deliberate language and tracking checks.
alltext='\n'.join(x.read_text() for x in ROOT.rglob('*') if x.is_file() and x.suffix in ('.html','.js','.css')).lower()
for phrase in ('dust'+'-free','best flooring','number one','guaranteed results','five-star'):
 if phrase in alltext:errors.append(f'prohibited claim language: {phrase}')
app=(ROOT/'assets/app.js').read_text()
for event in ('click_to_call','form_start','faq_expand','gallery_view','service_area_view'):
 if event not in app:errors.append(f'missing service-page tracking hook: {event}')
print(f'Checked {len(htmls)} HTML files; {len(titles)} unique titles.')
if errors:
 print('\n'.join('ERROR '+e for e in errors));sys.exit(1)
print('PASS metadata, titles, H1s, labels, alt text, internal links, claims, and tracking hooks.')
