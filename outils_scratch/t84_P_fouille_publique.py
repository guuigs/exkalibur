import numpy as np,math,pickle,json
from scipy import ndimage
from shapely.geometry import Point
from shapely import contains_xy
exec(open('ring1068.py').read().split('out=[]')[0])
C=pickle.load(open('PUB_cat.pkl','rb'));B_=np.array(B)
acc=np.load('acc.npy')
J=T.transform(6.040299,45.422426);SRC=T.transform(6.04019,45.42177)
HS=np.array([c[:2] for f in json.load(open('large/troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']])
rd=[]
for f in json.load(open('large/troncon_de_route.json'))['features']:
  from shapely.geometry import shape
  g=shape(f['geometry'])
  if g.distance(Point(J))<700: rd.append(g)
from shapely.ops import unary_union
RD=unary_union(rd)
cands=[]
r0,c0=int((YN-J[1])/2),int((J[0]-X0)/2)
for dr in range(-150,151):
  for dc in range(-150,151):
    if dr*dr+dc*dc>150*150: continue
    r,c=r0+dr,c0+dc
    if acc[r,c]*4<5000: continue        # talweg ≥ 0,5 ha
    x=X0+c*2+1;y=YN-r*2-1;cands.append((x,y,acc[r,c]*4/1e4))
print('cellules de talweg ≥0,5 ha dans 300 m :',len(cands))
JD={'Pâques 1524 (91,4°)':91.4,'Pâques 2026 (93,0°)':93.0,'30/04 grég. (74°)':74.0,'30/04/1524 jul. (67,7°)':67.7,'est (90°)':90.0}
res=[]
for x,y,ha in cands:
  lo,la=Ti.transform(x,y);dj=math.dist((x,y),J)
  R,Cc=int(YN-y),int(x-X0);D=mnt[R-6:R+7,Cc-6:Cc+7].astype(float);bump=float((D-ndimage.gaussian_filter(D,2.5)).max())
  for jn,jd in JD.items():
    ok=[]
    for pas in (0.65,0.75):
      l1,a1,_=G.fwd(lo,la,0,10*pas);l1,a1,_=G.fwd(l1,a1,90,10*pas);l2,a2,_=G.fwd(l1,a1,jd,8*pas)
      qx,qy=T.transform(l2,a2);q=Point(qx,qy)
      hb=float(np.min(np.hypot(B_[:,0]-qx,B_[:,1]-qy)))
      ok.append((C['PUBSUR'].contains(q) and hb>=100 and RD.distance(q)<=30,a2,l2,hb,RD.distance(q)))
    if all(o[0] for o in ok): res.append((dj,jn,la,lo,ha,bump,ok[1][1],ok[1][2],ok[1][3],ok[1][4],math.dist((x,y),SRC)))
print('roches donnant un coffre public sûr (pas 0,65 ET 0,75) :',len(res))
seen=set()
for r in sorted(res):
  k=(round(r[2],4),round(r[3],4),r[1])
  if k in seen: continue
  seen.add(k)
  print(f'roche à {r[0]:3.0f} m de la jonction ({r[2]:.6f},{r[3]:.6f}) talweg {r[4]:.1f} ha saillie +{r[5]:.1f} m, source à {r[10]:.0f} m | jour dernier {r[1]} → coffre {r[6]:.6f},{r[7]:.6f} (maisons {r[8]:.0f} m, chemin {r[9]:.0f} m)')
