import json,math,numpy as np
exec(open('ring1068.py').read().split('out=[]')[0])
Z=np.load('couloir_vis.npz');cx,cy,vs,vp=Z['cx'],Z['cy'],Z['vs'],Z['vp']
hyd=json.load(open('wfs_troncon_hydrographique.json'))
HS=np.array([c[:2] for f in hyd['features'] if f['geometry']['type']=='LineString' for c in f['geometry']['coordinates']])
ox,oy=T.transform(6.03101275,45.4288723)
rows=[]
for m in M:
  dx,dy=m[0]-ox,m[1]-oy;d=math.hypot(dx,dy);az=math.degrees(math.atan2(dx,dy))%360
  if not(1300<=d<=2800 and 70<=az<=120) or m[0]>X0+6870: continue
  dd=np.hypot(cx-m[0],cy-m[1]);n50=int(((dd<=50)&vs).sum());p50=int(((dd<=50)&vp).sum())
  if n50+p50==0: continue
  op=np.mean([z(mnh,m[0]+a,m[1]+b)<2 for a in range(-30,31,3) for b in range(-30,31,3) if math.hypot(a,b)<=30])
  ring=np.mean([z(mnh,m[0]+a,m[1]+b)>5 for a in range(-120,121,6) for b in range(-120,121,6) if 60<=math.hypot(a,b)<=120 and m[0]+a<X0+6999])
  db=float(np.min(np.hypot(B[:,0]-m[0],B[:,1]-m[1])));dw=float(np.min(np.hypot(HS[:,0]-m[0],HS[:,1]-m[1])))
  lon,lat=Ti.transform(m[0],m[1])
  rows.append((lat,lon,round(d),round(az,1),m[2],m[4][:3],round(op,2),round(ring,2),n50,p50,round(db),round(dw)))
print('lat lon dist cap deg nature ouvert30 foret60-120 vis_sommet50 vis_pied50 bati eau')
for r in sorted(rows,key=lambda r:(-(r[10]>=100),-r[7])): print(r)
