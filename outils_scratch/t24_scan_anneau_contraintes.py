import numpy as np,json,math
from pyproj import Transformer,Geod
t=Transformer.from_crs(4326,2154,always_xy=True);ti=Transformer.from_crs(2154,4326,always_xy=True);g=Geod(ellps='WGS84')
M=np.load('mnt.npy',mmap_mode='r');H=np.load('mnh.npy',mmap_mode='r');X0=933000;YN=6489000
r=np.load('rasters.npz');DB=r['d_bld']
def z(x,y): return float(M[int(YN-y),int(x-X0)])
def h(x,y): return float(H[int(YN-y),int(x-X0)])
T=(45.4288723,6.03101275);tx,ty=t.transform(T[1],T[0])
bx,by=t.transform(6.03095,45.42880)  # pied de tour / point de vue
zb=z(bx,by)+1.7; zt=440.46
# junctions
J=json.load(open('junc_attrs.json'));JP=np.array([(j['x'],j['y']) for j in J])
# streams
hyd=json.load(open('wfs_troncon_hydrographique.json'));SP=[]
for f in hyd['features']:
  gm=f['geometry'];cs=gm['coordinates'] if gm['type']=='LineString' else [c for l in gm['coordinates'] for c in l]
  nm=f['properties'].get('cpx_toponyme_de_cours_d_eau') or 'sans nom'
  for i in range(len(cs)-1):
    (x1,y1,*_),(x2,y2,*_)=cs[i],cs[i+1];L=math.hypot(x2-x1,y2-y1)
    for k in np.arange(0,L,5): SP.append((x1+(x2-x1)*k/L,y1+(y2-y1)*k/L,nm))
SA=np.array([(a,b) for a,b,_ in SP]);SN=[c for *_,c in SP]
def vis(ox,oy,oz,px,py,pz):
  D=math.hypot(px-ox,py-oy);w=-1e9
  for f in np.linspace(0.01,0.99,300):
    x=ox+(px-ox)*f;y=oy+(py-oy)*f;line=oz+(pz-oz)*f-(D*f)*(D*(1-f))/(2*6371000)*0.87
    w=max(w,z(x,y)-line)
  return w
res=[]
for az10 in range(400,1401,5):   # 0.5° step
  az=az10/10
  for R in (1840,1850,1860):
    lo,la,_=g.fwd(T[1],T[0],az,R);px,py=t.transform(lo,la)
    if not(X0+5<px<X0+6995 and YN-6995<py<YN-5): continue
    pz=z(px,py);can=h(px,py)
    db=float(DB[int((YN-py)/2),int((px-X0)/2)])
    dj=np.hypot(JP[:,0]-px,JP[:,1]-py);jd=float(dj.min())
    ds=np.hypot(SA[:,0]-px,SA[:,1]-py);si=int(ds.argmin())
    # stream reachable: stream points within 250 m, with |dz|<20 and building dist>100
    near=np.where(ds<250)[0];good=None
    for i in near[::3]:
      sx,sy=SA[i];dz=abs(z(sx,sy)-pz);sb=float(DB[int((YN-sy)/2),int((sx-X0)/2)])
      if dz<20 and sb>100: good=(float(ds[i]),SN[i],dz,sb);break
    res.append(dict(az=az,R=R,lat=la,lon=lo,z=pz,can=can,bld=db,jd=jd,st=(float(ds[si]),SN[si]),good=good))
json.dump(res,open('C/ringscan.json','w'))
# filter
cand=[q for q in res if q['jd']<60 and q['good'] and q['bld']>60]
print(len(res),'points ; candidats (jonction<60m, ruisseau accessible & loin des maisons, >60m bâti):',len(cand))
for q in cand:
  q['vb']=vis(bx,by,zb,*t.transform(q['lon'],q['lat']),q['z']+1.7)
  q['vt']=vis(tx,ty,zt,*t.transform(q['lon'],q['lat']),q['z']+1.7)
  print(f"cap {q['az']:5.1f} R {q['R']} {q['lat']:.5f},{q['lon']:.5f} z{q['z']:.0f} cano{q['can']:.0f} bâti{q['bld']:.0f} jonc{q['jd']:.0f} | ruisseau {q['good'][1]} {q['good'][0]:.0f}m dz{q['good'][2]:.0f} | masque sol pied {q['vb']:.0f} m / sommet {q['vt']:.0f} m")
