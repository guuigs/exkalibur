import json,math,numpy as np
from pyproj import Transformer
exec(open('ring1068.py').read().split('out=[]')[0])
Z=np.load('couloir_vis.npz')  # visible open cells (east sector only) -> recompute generically below instead
BNG=Transformer.from_crs(27700,4326,always_xy=True)
mm={'3':BNG.transform(191006,632457),'11':BNG.transform(191213,632426),'4':BNG.transform(191000,632350),'5':BNG.transform(190878,632353),
    '1':(-5.3108749,55.5404868),'2':(-5.3119322,55.5406772)}
# local metric frame on Arran (azimuth/distance from MM3)
vec={}
for k,(lo,la) in mm.items():
  if k=='3': continue
  az,_,d=G.inv(mm['3'][0],mm['3'][1],lo,la);vec[k]=(az%360,d)
print({k:(round(a,1),round(d)) for k,(a,d) in vec.items()})
scale=1850/vec['11'][1]
# start points: tower top, foot, rue, + enceinte wall nodes
o=json.load(open('osm.json'));nodes=o['nodes']
wall=[w for w in o['ways'] if w[0]=='711947270']
starts={'sommet':(45.4288723,6.03101275),'pied':(45.42887,6.03115),'rue_rempart':(45.42977,6.03118)}
if wall:
  nl=wall[0][1]
  for i,n in enumerate(nl[::2]):
    if n in nodes: starts[f'mur{i}']=tuple(nodes[n])
print('départs',len(starts))
X0t,Y0t=T.transform(6.03101275,45.4288723);Zs=z(mnt,X0t,Y0t)+33
Xp,Yp=T.transform(6.03115,45.42887);Zp=z(mnt,Xp,Yp)+1.7
def visopen(x,y,r=60):
  n=vs=vp=0
  for a in range(-r,r+1,10):
    for b in range(-r,r+1,10):
      if math.hypot(a,b)>r or z(mnh,x+a,y+b)>=1.5: continue
      n+=1
      vs+= los(X0t,Y0t,Zs,x+a,y+b,True)<0
      vp+= los(Xp,Yp,Zp,x+a,y+b,True)<0
  return n,vs,vp
rows=[]
for orient,dtheta in [('nord vrai',0.0),('magnétique +3°',3.0),('image enl.11',109.8-95.78)]:
  for sn,(la,lo) in starts.items():
    for k,(az,d) in vec.items():
      tl,ta,_=G.fwd(lo,la,az+dtheta,d*scale);x,y=T.transform(tl,ta)
      if not(X0+150<x<X0+6850 and YN-6850<y<YN-150): continue
      j=min(M,key=lambda m:math.hypot(m[0]-x,m[1]-y));dj=math.hypot(j[0]-x,j[1]-y)
      db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
      rows.append([orient,sn,k,round(ta,6),round(tl,6),round(d*scale),round(dj),j[2],round(db),x,y])
print('placements',len(rows))
# filter: junction <=80 m, buildings >=100 m ; then compute visibility
cand=[r for r in rows if r[6]<=80 and r[8]>=100]
print('avec croisement <=80 m et maisons >=100 m :',len(cand))
out=[]
seen=set()
for r in cand:
  key=(round(r[9]/25),round(r[10]/25))
  if key in seen: continue
  seen.add(key)
  n,vs,vp=visopen(r[9],r[10])
  ring=np.mean([z(mnh,r[9]+a,r[10]+b)>5 for a in range(-120,121,8) for b in range(-120,121,8) if 60<=math.hypot(a,b)<=120])
  out.append(r[:9]+[n,vs,vp,round(float(ring),2)])
print('orientation départ cercle lat lon dist croisement(m) branches maisons | cellules_ouvertes60 vues_sommet vues_pied forêt_autour')
for r in sorted(out,key=lambda r:-(r[10]+r[11])): print(r)
