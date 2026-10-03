import numpy as np,json,math
from pyproj import Transformer,Geod
t=Transformer.from_crs(4326,2154,always_xy=True);g=Geod(ellps='WGS84')
M=np.load('mnt.npy',mmap_mode='r');H=np.load('mnh.npy',mmap_mode='r');X0=933000;YN=6489000
DB=np.load('rasters.npz')['d_bld']
J=json.load(open('junc_attrs.json'))
hyd=json.load(open('wfs_troncon_hydrographique.json'));SP=[]
for f in hyd['features']:
  gm=f['geometry'];cs=gm['coordinates'] if gm['type']=='LineString' else [c for l in gm['coordinates'] for c in l]
  nm=f['properties'].get('cpx_toponyme_de_cours_d_eau') or 'sans nom'
  for i in range(len(cs)-1):
    (x1,y1,*_),(x2,y2,*_)=cs[i],cs[i+1];L=math.hypot(x2-x1,y2-y1)
    for k in np.arange(0,L,5): SP.append((x1+(x2-x1)*k/L,y1+(y2-y1)*k/L,nm))
SA=np.array([(a,b) for a,b,_ in SP]);SN=[c for *_,c in SP]
T=(45.4288723,6.03101275);bx,by=t.transform(6.03095,45.42880)
def z(x,y): return float(M[int(YN-y),int(x-X0)])
zb=z(bx,by)+1.7
def vis(px,py,pz):
  D=math.hypot(px-bx,py-by);w=-1e9
  for f in np.linspace(0.01,0.99,300):
    x=bx+(px-bx)*f;y=by+(py-by)*f;line=zb+(pz-zb)*f-(D*f)*(D*(1-f))/(2*6371000)*0.87;w=max(w,z(x,y)-line)
  return w
out=[]
for j in J:
  q=g.inv(T[1],T[0],j['lon'],j['lat']);d=q[2];az=q[0]%360
  if not(300<d<3200 and 20<=az<=170): continue
  x,y=j['x'],j['y'];r=int(YN-y);c=int(x-X0)
  if not(60<r<6940 and 60<c<6940): continue
  if float(H[r,c])>3: continue
  sub=np.array(H[r-25:r+26,c-25:c+26]);openfrac=float((sub<3).mean())
  ann=np.array(H[r-120:r+121,c-120:c+121]);yy,xx=np.mgrid[-120:121,-120:121];rr=np.hypot(yy,xx)
  forest=float((ann[(rr>50)&(rr<120)]>5).mean())
  if openfrac<0.35 or forest<0.45: continue
  ds=np.hypot(SA[:,0]-x,SA[:,1]-y);i=int(ds.argmin())
  if ds[i]>80: continue
  zj=z(x,y)
  good=[k for k in np.where(ds<200)[0][::2] if abs(z(*SA[k])-zj)<20 and DB[int((YN-SA[k][1])/2),int((SA[k][0]-X0)/2)]>100]
  if not good: continue
  v=vis(x,y,zj+1.7)
  if v>3: continue
  out.append((round(d),round(az,1),j['lat'],j['lon'],j['deg'],j['nat'][:3],round(openfrac,2),round(forest,2),SN[i],round(float(ds[i])),len(good),round(float(DB[r//2,c//2])),round(v,1),round(zj)))
out.sort()
for o in out: print(o)
print(len(out))
json.dump(out,open('C/freescan.json','w'))
