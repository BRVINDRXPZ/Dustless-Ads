#!/usr/bin/env python3
from pathlib import Path
import json,re,sys,csv
root=Path(__file__).resolve().parents[3]; p=root/'dashboard/prototype'; errors=[]
data=json.loads((p/'data/sample-data.json').read_text()); leads=data['leads']
def check(cond,msg):
 if not cond: errors.append(msg)
ids=[x['id'] for x in leads];check(len(ids)==len(set(ids)),'duplicate lead IDs')
required={'id','date','source','campaign','service','geography','segment','owner','stage','qualified','revenue','grossProfit'}
check(all(required<=x.keys() for x in leads),'missing required lead fields')
valid_stages={'New','Contacted','Qualified','Disqualified','Estimate Scheduled','Estimate Completed','Proposal Sent','Won','Lost','No Response','Future Opportunity'}
check(all(x['stage'] in valid_stages for x in leads),'invalid stage')
valid_sources={'Google Ads','Google Business Profile','Organic search','Direct','Referral','Contractor referral','Realtor','Designer','Social','Facebook','Instagram','TikTok','YouTube','Email','Commercial outreach','Contractor outreach','Past customer','Unknown'}
check(all(x['source'] in valid_sources for x in leads),'invalid source')
check(all(x['revenue']>=0 and x['grossProfit']>=0 for x in leads),'negative currency')
check(all(not x['revenue'] or (x['stage']=='Won' and x['projectId']) for x in leads),'revenue without won project')
check(all(x['grossProfit']<=x['revenue'] for x in leads),'gross profit greater than revenue')
check(all(re.fullmatch(r'\d{4}-\d{2}-\d{2}',x['date']) for x in leads),'missing/invalid dates')
for f in p.rglob('*'):
 if f.is_file() and f.suffix in {'.html','.js','.json','.md'}:
  txt=f.read_text();check(not re.search(r'(?i)(api[_-]?key|secret|password)\s*[:=]\s*["\'][^"\']+["\']',txt),f'possible credential in {f.relative_to(root)}')
html=(p/'index.html').read_text();check('SYNTHETIC DEMONSTRATION DATA' in html,'missing screen disclosure');check('data/sample-data.json' in (p/'assets/app.js').read_text(),'sample file not linked')
for src in re.findall(r'(?:href|src)="([^"]+)"',html):
 if not src.startswith(('http','#')): check((p/src).exists(),f'broken dashboard link {src}')
for schema in (root/'crm').glob('*_SCHEMA.csv'):
 with schema.open() as f: check(next(csv.reader(f))==['Field','Type','Required','Validation/definition'],f'schema header mismatch {schema.name}')
print(f'Checked {len(leads)} synthetic leads, prototype links, disclosures, credentials, and {len(list((root/"crm").glob("*_SCHEMA.csv")))} CRM schemas.')
if errors:
 print('\n'.join('ERROR: '+x for x in errors));sys.exit(1)
print('PASS')
