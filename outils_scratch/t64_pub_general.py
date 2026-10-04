import json,gzip,csv,pickle
from shapely.geometry import shape,box
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
tr=lambda g:stf(lambda x,y,z=None:T.transform(x,y),g)
def pm(fn):
  o={}
  for r in csv.reader(open(fn,encoding='latin-1'),delimiter=';'):
    if len(r)>23: o[(r[5].strip(),r[6].strip().zfill(4))]=r[20]
  return o
pubs=[];allp=[]
for code,f,pmf in (('38426','cad/38426-parcelles.json',None),('38314','cad/38314-parcelles.json.gz','cad/pm_38314.csv'),('38270','cad/38270-parcelles.json.gz','cad/pm_38270.csv'),('38027','cad/38027-parcelles.json.gz','cad/pm_38027.csv'),('73141','cad/73141-parcelles.json.gz','cad/pm_73141.csv')):
  d=json.load(gzip.open(f) if f.endswith('gz') else open(f))
  if pmf: o=pm(pmf)
  else:
    own=json.load(open('cad/pm_38426.json'))
  n=0
  for ft in d['features']:
    p=ft['properties'];g=tr(shape(ft['geometry'])).buffer(0);allp.append(g)
    if pmf:
      gr=o.get((p['section'].lstrip('0') or p['section'],p['numero'].zfill(4))) or o.get((p['section'],p['numero'].zfill(4)))
      ok=gr and gr[:1] in '1234'
    else:
      ok=own.get(p['id']) and own[p['id']][0][:1] in '1234'
    if ok: pubs.append(g);n+=1
  print(code,len(d['features']),'parcelles,',n,'publiques',flush=True)
P=unary_union(allp)
B0=box(X0+100,YN-6900,X0+6900,YN-100)
EMP=P.buffer(40).buffer(-40)
NC=EMP.intersection(B0).difference(P.buffer(0.3)).buffer(-0.2)
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
PUB=unary_union(pubs+[NC,FP]).buffer(0)
print('surface publique (km²)',round(PUB.intersection(B0).area/1e6,2),' non cadastré',round(NC.area/1e6,2))
pickle.dump(PUB,open('PUB_general.pkl','wb'))
