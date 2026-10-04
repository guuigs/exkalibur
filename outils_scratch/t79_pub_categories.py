import json,gzip,csv,pickle
from shapely.geometry import shape,box
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
tr=lambda g:stf(lambda x,y,z=None:T.transform(x,y),g)
def pm(fn):
  o={}
  for r in csv.reader(open(fn,encoding='latin-1'),delimiter=';'):
    if len(r)>23: o[(r[5].strip(),r[6].strip().zfill(4))]=(r[20],r[23])
  return o
own38426=json.load(open('cad/pm_38426.json'))
COM=[('38426','cad/38426-parcelles.json',None),('38314','cad/38314-parcelles.json.gz','cad/pm_38314.csv'),('38270','cad/38270-parcelles.json.gz','cad/pm_38270.csv'),('38027','cad/38027-parcelles.json.gz','cad/pm_38027.csv'),('73141','cad/73141-parcelles.json.gz','cad/pm_73141.csv'),('73075','cad/73075-parcelles.json.gz','cad/pm_73075.csv'),('38006','cad/38006-parcelles.json.gz','cad/pm_38006.csv'),('38062','cad/38062-parcelles.json.gz','cad/pm_38062.csv')]
B0=box(X0+100,YN-6900,X0+6900,YN-100)
pubs=[];allp=[];info={}
for code,f,pmf in COM:
  d=json.load(gzip.open(f) if f.endswith('gz') else open(f));o=pm(pmf) if pmf else None;n=0
  for ft in d['features']:
    g=shape(ft['geometry'])
    if not g.intersects(box(5.97,45.38,6.10,45.48)): continue
    g=tr(g).buffer(0);allp.append(g);p=ft['properties']
    if o is not None:
      gr=o.get((p['section'].lstrip('0') or p['section'],p['numero'].zfill(4))) or o.get((p['section'],p['numero'].zfill(4)))
      ok=gr and gr[0][:1] in '1234'
    else:
      ok=own38426.get(p['id']) and own38426[p['id']][0][:1] in '1234'
    if ok: pubs.append(g);n+=1
  print(code,'parcelles publiques (zone):',n,flush=True)
P=unary_union(allp)
EMP=P.buffer(40).buffer(-40)
NC=EMP.intersection(B0).difference(P.buffer(0.3)).buffer(-0.2)
FP=unary_union([shape(f['geometry']) for f in json.load(open('wfs_foret_publique.json'))['features']])
roads=unary_union([shape(f['geometry']) for f in json.load(open('large/troncon_de_route.json'))['features'] if shape(f['geometry']).intersects(B0)])
NC_voie=NC.intersection(roads.buffer(6))
NC_autre=NC.difference(roads.buffer(6))
PUBSUR=unary_union(pubs+[FP,NC_voie]).buffer(0)
pickle.dump({'PUBSUR':PUBSUR,'NC_autre':NC_autre.buffer(0),'PARC':unary_union(pubs).buffer(0),'FP':FP,'NC_voie':NC_voie.buffer(0)},open('PUB_cat.pkl','wb'))
print('km² : parcelles publiques %.2f, forêt publique %.2f, voirie non cadastrée %.2f, autre non cadastré (lits de ruisseaux…) %.2f'%(unary_union(pubs).intersection(B0).area/1e6,FP.intersection(B0).area/1e6,NC_voie.area/1e6,NC_autre.area/1e6))
