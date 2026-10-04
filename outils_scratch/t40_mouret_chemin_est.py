import numpy as np,json,math
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
jx,jy=T.transform(6.040299,45.422426)
r=json.load(open('wfs_troncon_de_route.json'))
path=None
for f in r['features']:
  cs=[c[:2] for c in f['geometry']['coordinates']]
  if min(math.dist(cs[0],(jx,jy)),math.dist(cs[-1],(jx,jy)))<20:
    if math.dist(cs[-1],(jx,jy))<math.dist(cs[0],(jx,jy)): cs=cs[::-1]
    far=cs[min(len(cs)-1,3)];az=math.degrees(math.atan2(far[0]-jx,far[1]-jy))%360
    if 60<az<100: path=LineString(cs);print('chemin vers l\'est :',f['properties']['nature'],round(path.length),'m')
tal=LineString([T.transform(*p) for p in json.load(open('mouret_talweg.json'))])
reb=[shape(f['geometry']) for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if (f['properties'].get('cpx_toponyme_de_cours_d_eau') or '')=='Ruisseau de Rebouchet']
from shapely.ops import unary_union
REB=unary_union([LineString([c[:2] for c in g.coords]) for g in reb])
NC=shape(json.load(open('cad/noncad.json')))
print('pos(m) | z | talweg: dist & côté | Rebouchet dist | pente locale | maisons')
prev=None
for s in range(0,int(path.length)+1,25):
  p=path.interpolate(s);q=path.interpolate(min(path.length,s+5))
  dx,dy=q.x-p.x,q.y-p.y
  pt=tal.interpolate(tal.project(p));side=dx*(pt.y-p.y)-dy*(pt.x-p.x)
  zz=z(mnt,p.x,p.y);sl='' if prev is None else f'{abs(zz-prev)/25*100:4.0f} %';prev=zz
  db=float(np.min(np.hypot(B[:,0]-p.x,B[:,1]-p.y)))
  print(f'{s:4d} | {zz:5.0f} | {p.distance(pt):4.0f} m {"GAUCHE" if side>0 else "droite"} | {REB.distance(p):4.0f} m | {sl} | {db:.0f} m')
e=Point(path.coords[-1]);lo,la=Ti.transform(e.x,e.y);print('fin du chemin',round(la,6),round(lo,6),'| bande non cadastrée à',round(NC.distance(e)),'m')
