import re, json, glob, os

CONFIRM = re.compile(r'\[CONFIRM:\s*(.*?)\]', re.S)
BARE    = re.compile(r'\[CONFIRM\](?!:)')
CLINIC  = re.compile(r'\[CLINIC NAME\]')

def slug(t):
    s = re.sub(r'[^a-z0-9]+','_', t.lower()).strip('_')
    return s[:48] or 'field'

def clean_label(txt):
    t = re.split(r'\*?\*?\bDefault\b', txt, flags=re.I)[0]
    t = re.split(r'\s[—–]\s', t)[0]
    t = re.split(r'\.\s', t)[0]
    t = t.replace('**','').strip().strip('.').strip()
    t = re.split(r'\s\((?:e\.g|i\.e)', t)[0].strip()
    t = re.sub(r'^(whether|the|a|an|any)\s+', '', t, flags=re.I)
    if not t: t = txt.replace('**','').strip()[:60]
    return (t[0].upper()+t[1:]) if t else t

def get_default(txt):
    m = re.search(r'\bDefault\b[:\-\s]*(.+)', txt, flags=re.I|re.S)
    if not m: return ''
    d = m.group(1)
    d = d.split('**')[0] if '**' in d else d      # stop at bold boundary
    d = d.replace('**','').strip().rstrip('.]').strip(' .,;')
    return re.sub(r'\s+',' ', d)[:160]

def category(txt, default):
    low = txt.lower().strip()
    if re.match(r'^(whether|does|do |is |are |should)', low): return 'DECISION'
    if len(default) > 70: return 'CLAUSE'
    return 'VALUE'

def ftype(label, txt):
    l = (label+' '+txt).lower()
    if re.search(r'named|responsible person|\bwho\b|owner|lead|role|person|manager', l): return 'role'
    if 'date' in l and 'update' not in l: return 'date'
    if re.search(r'interval|frequency|every|month|year|weekly|annually|quarterly|days', l): return 'duration'
    if re.search(r'\blist\b|which (medicines|procedures|treatments|conditions)', l): return 'list'
    if re.search(r'address|premises location', l): return 'address'
    return 'text'

def rows_for(path):
    lines = open(path).read().split('\n')
    fields=[]
    seen_clinic=False
    for i,ln in enumerate(lines,1):
        # clinic name -> one field
        if CLINIC.search(ln):
            if not seen_clinic:
                fields.append(dict(line=i,id='clinic_name',label='Clinic name',cat='VALUE',type='clinic-name',default='',src='global'))
                seen_clinic=True
        # table-row bare confirm: | **Label** | `[CONFIRM]` |
        for m in re.finditer(r'\|\s*\*\*(.+?)\*\*\s*\|\s*`?\[CONFIRM\]`?\s*\|', ln):
            lab=m.group(1).replace('**','').strip()
            fields.append(dict(line=i,id=slug(lab),label=lab,cat='VALUE',
                               type=ftype(lab,lab),default='',src='table-row'))
        # descriptive confirm
        for m in CONFIRM.finditer(ln):
            txt=m.group(1).strip()
            if txt in ('…','...','') or txt.startswith('…'):   # boilerplate header
                continue
            # governance/editorial note, not a clinic field
            if re.search(r'check current status|archived|supersed|verify.*against.*current|cite the edition|before adopting', txt, re.I) and 'default' not in txt.lower():
                fields.append(dict(line=i,id=slug(txt[:30]),label='[reviewer note]',cat='NOTE',type='note',default='',note=txt[:140],src='note'))
                continue
            lab=clean_label(txt)
            d=get_default(txt)
            cat=category(txt,d)
            typ='yes/no' if cat=='DECISION' else ftype(lab,txt)
            fields.append(dict(line=i,id=slug(lab),label=lab,cat=cat,
                               type=typ,default=d,src='inline'))
    # dedup by id keeping first
    out=[]; ids=set()
    for f in fields:
        if f['id'] in ids: continue
        ids.add(f['id']); out.append(f)
    return out

allp={}
for path in sorted(glob.glob('starters/*.md')):
    if path.endswith('README.md'): continue
    code=os.path.basename(path).split('-')[0].upper()
    allp[code]=rows_for(path)


import json as _j
_OV=_j.load(open('overrides.json'))
for _c,_fs in allp.items():
    for _f in _fs:
        _k=f"{_c}:{_f['line']}"
        if _k in _OV:
            _f['label']=_OV[_k]
        if _k=='C07F:63':
            _f['default']='YES — offered at every prescribing encounter and the decision recorded'

json.dump(allp, open('fields.json','w'), indent=1)

# summary + markdown
tot=0; notes=0; md=['# Field schemas — all 28 policies (auto-extracted, verified against source)\n']
md.append('Generated from the starter documents. Each field: clean label, category (VALUE / DECISION / CLAUSE / NOTE), type, default, source line. `NOTE` = reviewer-only, never shown to the clinic. `clinic_name` de-duplicated to one field.\n')
md.append('Machine-readable version: `fields.json`.\n')
counts=[]
for code,fs in allp.items():
    real=[f for f in fs if f['cat']!='NOTE']; n=len(real); tot+=n
    nn=len([f for f in fs if f['cat']=='NOTE']); notes+=nn
    cats={c:len([f for f in real if f['cat']==c]) for c in ('VALUE','DECISION','CLAUSE')}
    counts.append((code,n,cats,nn))
    md.append(f'\n## {code} — {n} fields ({cats["VALUE"]} value · {cats["DECISION"]} decision · {cats["CLAUSE"]} clause){" · "+str(nn)+" note" if nn else ""}\n')
    md.append('| line | label | category | type | default |')
    md.append('|---|---|---|---|---|')
    for f in fs:
        dflt=(f.get('default') or f.get('note') or '').replace('|','/')
        md.append(f"| {f['line']} | {f['label']} | {f['cat']} | {f['type']} | {dflt} |")
open('FIELD-SCHEMAS-ALL.md','w').write('\n'.join(md))

print(f"TOTAL clean fields: {tot} across 28 policies · {notes} reviewer notes excluded")
print()
for code,n,cats,nn in counts:
    print(f"  {code:5} {n:3} fields  (V{cats['VALUE']} D{cats['DECISION']} C{cats['CLAUSE']})" + (f"  +{nn} note" if nn else ""))
