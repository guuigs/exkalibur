import json,math,numpy as np
from collections import defaultdict
from scipy import ndimage
from shapely.geometry import LineString,Point
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy')*4.0
# path graph endpoints degree (BD TOPO + OSM merged by 6 m)
r=json.load(open('wfs_troncon_de_route.json'))
ends=[];lines=[]
for f in r['features']:
  cs=[c[:2] for c in f['geometry']['coordinates']];lines.append((cs,f['properties']['nature']))
  ends+= [tuple(cs[0]),tuple(cs[-1])]
cnt=defaultdict(int)
for e in ends: cnt[(round(e[0]/6),round(e[1]/6))]+=1
HS=[np.array([c[:2] for c in f['geometry']['coordinates']]) for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString']
HSall=np.vstack(HS)
gy,gx=np.gradient(mnt.astype(np.float32))
res=[]
for cs,nat in lines:
  for end,prev in ((cs[0],cs[min(1,len(cs)-1)]),(cs[-1],cs[max(-2,-len(cs))])):
    if cnt[(round(end[0]/6),round(end[1]/6))]!=1: continue   # cul-de-sac
    x,y=end
    if not(X0+200<x<X0+6800 and YN-6800<y<YN-200): continue
    dw=float(np.min(np.hypot(HSall[:,0]-x,HSall[:,1]-y)))
    r2,c2=int((YN-y)/2),int((x-X0)/2);w=acc[r2-20:r2+21,c2-20:c2+21];ys,xs=np.where(w>=2e4)
    dt=float(np.min(np.hypot(ys-20,xs-20))*2) if len(ys) else 99
    if min(dw,dt)>30: continue
    db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
    if db<100: continue
    r0,c0=int(YN-y),int(x-X0);S=np.degrees(np.arctan(np.hypot(gx[r0-25:r0+26,c0-25:c0+26],gy[r0-25:r0+26,c0-25:c0+26])))
    D=mnt[r0-25:r0+26,c0-25:c0+26].astype(float);bump=D-ndimage.gaussian_filter(D,5)
    steep=int(((S>45)&(bump>0.8)).sum())
    lo,la=Ti.transform(x,y);az,_,dd=G.inv(6.03101275,45.4288723,lo,la)
    res.append((steep,round(la,6),round(lo,6),nat,round(min(dw,dt)),round(db),round(dd),round(az%360)))
res.sort(reverse=True)
print('culs-de-sac à ≤30 m de l\'eau et ≥100 m des maisons :',len(res))
for x in res[:25]: print(f'roche raide {x[0]:4d} m² | {x[1]},{x[2]} | {x[3]} | eau {x[4]} m | maisons {x[5]} m | tour {x[6]} m cap {x[7]}°')
json.dump(res,open('deadend_rock.json','w'))
