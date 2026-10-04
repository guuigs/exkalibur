import json,math,numpy as np
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0])
N=7000
Vp=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
HS=np.array([c[:2] for f in json.load(open('wfs_troncon_hydrographique.json'))['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']])
px,py=T.transform(6.03115,45.42887)
out=[]
for m in M:
  x,y=m[0],m[1]
  if not(X0+160<x<X0+6840 and YN-6840<y<YN-160): continue
  dt=math.hypot(x-px,y-py)
  if dt<300: continue
  r0,c0=int(YN-y),int(x-X0)
  v10=int(Vp[r0-10:r0+11,c0-10:c0+11].sum())
  if v10<20: continue
  db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
  D=mnt[r0-15:r0+16,c0-15:c0+16].astype(float);gy,gx=np.gradient(ndimage.uniform_filter(D,3))
  sl=float(np.median(np.degrees(np.arctan(np.hypot(gx,gy)))))
  yy,xx=np.mgrid[-150:151,-150:151];ring=((xx**2+yy**2)>=60**2)&((xx**2+yy**2)<=150**2)
  forest=float((mnh[r0-150:r0+151,c0-150:c0+151][ring]>5).mean())
  dw=float(np.min(np.hypot(HS[:,0]-x,HS[:,1]-y)))
  lon,lat=Ti.transform(x,y)
  out.append((round(db),round(lat,6),round(lon,6),round(dt),v10,round(sl),round(forest,2),round(dw),m[2],m[4]))
print('croisements dont le POINT est vu de la MURAILLE (≥20 m² à ±10 m), hors 300 m :',len(out))
for crit,(mb,fo,ww,ss) in {'strict':(100,0.30,200,12),'souple':(60,0.20,300,15)}.items():
  g=[o for o in out if o[0]>=mb and o[6]>=fo and o[7]<=ww and o[5]<=ss]
  print(f'--- {crit}: maisons≥{mb}, forêt≥{fo}, eau≤{ww}, pente≤{ss}° :',len(g))
  for o in sorted(g,reverse=True)[:15]: print('  maisons %d | %s,%s | tour %d m | vu %d m² | pente %d° | forêt %.2f | eau %d m | deg %s %s'%o)
print('--- meilleurs sans critère pente/forêt (maisons ≥100) :')
for o in sorted([o for o in out if o[0]>=100],key=lambda o:o[7])[:10]: print('  maisons %d | %s,%s | tour %d m | vu %d m² | pente %d° | forêt %.2f | eau %d m | deg %s %s'%o)
print('--- les 11, tous critères ouverts :')
for o in sorted(out,key=lambda o:o[3]): print('  maisons %d | %s,%s | tour %d m | vu %d m² | pente %d° | forêt %.2f | eau %d m | deg %s %s'%o)
