import json,gzip,csv,math,pickle,numpy as np
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
tr=lambda g:stf(lambda x,y,z=None:T.transform(x,y),g)
J=Point(*T.transform(6.040299,45.422426));SRC=Point(*T.transform(6.04019,45.42177))
own=json.load(open('cad/pm_38426.json'))
pm14={}
for r in csv.reader(open('cad/pm_38314.csv',encoding='latin-1'),delimiter=';'):
  if len(r)>23: pm14[(r[5].strip(),r[6].strip().zfill(4))]=(r[20],r[23])
P=[]
for code,f in (('38426','cad/38426-parcelles.json'),('38314','cad/38314-parcelles.json.gz')):
  d=json.load(gzip.open(f) if f.endswith('gz') else open(f))
  for ft in d['features']:
    g=tr(shape(ft['geometry'])).buffer(0)
    if g.distance(SRC)<220:
      p=ft['properties']
      if code=='38426': o=own.get(p['id']);o=(o[0],o[1]) if o else None
      else: o=pm14.get((p['section'].lstrip('0') or p['section'],p['numero'].zfill(4)))
      P.append((p['id'],g,o,p.get('contenance')))
print('parcelles à <220 m de la source :',len(P))
for pid,g,o,c in sorted(P,key=lambda t:t[1].distance(SRC))[:14]:
  print(f'  {pid} {c} m² à {g.distance(SRC):.0f} m de la source, {g.distance(J):.0f} m de la jonction -> {o if o else "particulier (non personne morale)"}')
allp=unary_union([g for _,g,_,_ in P])
# sentiers
rd=[(shape(f['geometry']),f['properties'].get('nature'),f['properties'].get('cleabs')) for f in json.load(open('large/troncon_de_route.json'))['features'] if shape(f['geometry']).distance(SRC)<200]
for g,n,c in rd: print('voie BD TOPO',n,round(g.length),'m, à',round(g.distance(SRC)),'m de la source, à',round(g.distance(J)),'m de la jonction')
# sentier sud = voie la plus proche de la source
sud=min(rd,key=lambda t:t[0].distance(SRC))[0]
L=sud.length;nc_len=0;tot=0
segs=[]
for s in np.arange(0,L,2):
  p=sud.interpolate(s);inside=allp.contains(p)
  owner=None
  for pid,g,o,c in P:
    if g.contains(p): owner=(pid,o);break
  segs.append((s,p,owner))
print('sentier sud : %.0f m'%L)
cur=None
for s,p,ow in segs:
  k=('NON CADASTRÉ' if ow is None else ow[0]+' '+(str(ow[1][1]) if ow[1] else 'particulier'))
  if k!=cur:
    print(f'   à {s:4.0f} m : {k} (source à {p.distance(SRC):.0f} m)');cur=k
pickle.dump({'P':[(pid,g,o) for pid,g,o,c in P],'sud':sud,'rd':rd},open('run/mouret_cad.pkl','wb'))
