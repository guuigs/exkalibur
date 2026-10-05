import json,gzip,csv,pickle,numpy as np
from shapely.geometry import shape,box,LineString
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
tr=lambda g:stf(lambda x,y,z=None:T.transform(x,y),g)
# 1) sommets de tous les bâtiments (anneaux densifiés tous les 3 m)
pts=[]
for f in json.load(open('wfs_batiment.json'))['features']:
  g=shape(f['geometry'])
  for pg in getattr(g,'geoms',[g]):
    L=LineString([c[:2] for c in pg.exterior.coords])
    for s in np.arange(0,L.length,3.0): p=L.interpolate(s);pts.append((p.x,p.y))
    pts.append(tuple(pg.exterior.coords[0][:2]))
BV=np.array(pts);np.save('run/bat_dense.npy',BV);print('points de bâtiments (densifiés) :',len(BV))
# 2) domaine public sûr + Le Moutaret (38268)
C=pickle.load(open('PUB_cat.pkl','rb'))
pm={}
for r in csv.reader(open('cad/pm_38268.csv',encoding='latin-1'),delimiter=';'):
  if len(r)>23: pm[(r[5].strip(),r[6].strip().zfill(4))]=(r[20],r[23])
extra=[]
for ft in json.load(gzip.open('cad/38268-parcelles.json.gz'))['features']:
  p=ft['properties'];o=pm.get((p['section'].lstrip('0') or p['section'],p['numero'].zfill(4)))
  if o and o[0][:1] in '1234': extra.append(tr(shape(ft['geometry'])).buffer(0))
PUB2=unary_union([C['PUBSUR']]+extra).buffer(0)
pickle.dump(PUB2,open('run/PUB2.pkl','wb'));print('PUB2 prêt ; parcelles publiques Moutaret ajoutées :',len(extra))
