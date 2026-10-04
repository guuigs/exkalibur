import numpy as np,json,math
from scipy import ndimage
from shapely.geometry import shape,Point
from shapely.ops import transform as stf,unary_union
exec(open('ring1068.py').read().split('out=[]')[0])
NC=shape(json.load(open('cad/noncad.json')))
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
PU=unary_union([stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if own.get(f['properties']['id']) and own[f['properties']['id']][0].startswith(('1','2','3','4'))])
PUB=unary_union([NC,PU])
jx,jy=T.transform(6.040299,45.422426);R=400
r0,c0=int(YN-jy)-R,int(jx-X0)-R;D=mnt[r0:r0+2*R,c0:c0+2*R].astype(float)
gy,gx=np.gradient(D);sl=np.degrees(np.arctan(np.hypot(gx,gy)));bump=D-ndimage.gaussian_filter(D,6)
lab,n=ndimage.label((sl>40)&(bump>0.9));rocks=[]
for i in range(1,n+1):
  ys,xs=np.where(lab==i)
  if len(ys)<6: continue
  rocks.append((X0+c0+xs.mean(),YN-(r0+ys.mean()),len(ys),float(bump[lab==i].max())))
print('affleurements candidats (≥6 m², pente>40°, saillie>0,9 m) à <400 m :',len(rocks))
hits=[]
for x,y,a,b in rocks:
  if float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))<100: continue
  for pas in (0.75,1.48):
    for nm,brg in (('est 90°',90),('lever 30/04/1524 67,6°',67.6),('lever 30/04 72,4°',72.4)):
      dx=10*pas+8*pas*math.sin(math.radians(brg+2.2));dy=10*pas+8*pas*math.cos(math.radians(brg+2.2))
      p=Point(x+dx,y+dy)
      if PUB.contains(p):
        lo,la=Ti.transform(x,y);lo2,la2=Ti.transform(p.x,p.y)
        db=float(np.min(np.hypot(B[:,0]-p.x,B[:,1]-p.y)))
        hits.append((math.hypot(x-jx,y-jy),round(la,6),round(lo,6),a,round(b,1),pas,nm,round(la2,6),round(lo2,6),round(db),'commune' if PU.contains(p) else 'chemin/ruisseau'))
print('combinaisons dont le point de fouille tombe en terrain public :',len(hits))
for h in sorted(hits)[:25]: print(f'roche à {h[0]:.0f} m de la jonction : {h[1]},{h[2]} ({h[3]} m², {h[4]} m) | pas {h[5]} m, {h[6]} -> fouille {h[7]},{h[8]} [{h[10]}], maisons {h[9]} m')
