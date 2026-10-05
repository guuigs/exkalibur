import json,gzip,math,pickle,numpy as np,time
from scipy import ndimage
from scipy.spatial import cKDTree
from shapely.geometry import shape,Point,LineString
from shapely.prepared import prep
from shapely import contains_xy
exec(open('ring1068.py').read().split('out=[]')[0]);N=7000
t0=time.time()
Vs=np.unpackbits(np.load('vs_muraille_sol.npy'))[:N*N].reshape(N,N).astype(bool)
Vm=np.unpackbits(np.load('vs_muraille.npy'))[:N*N].reshape(N,N).astype(bool)
acc=np.load('acc.npy');fd=np.load('fdir.npy')
mv={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
PUB2=pickle.load(open('run/PUB2.pkl','rb'));PUB3=pickle.load(open('run/PUB3.pkl','rb'));PP=prep(PUB3);PP2=prep(PUB2)
BV=np.load('run/bat_dense.npy');kb=cKDTree(BV)
def line_pts(fn,step=3):
  pts=[]
  for f in json.load(open(fn))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
      for s in np.arange(0,l.length,step): p=l.interpolate(s);pts.append((p.x,p.y))
  return np.array(pts)
RP=line_pts('large/troncon_de_route.json');kr=cKDTree(RP)
HP=line_pts('large/troncon_hydrographique.json');kh=cKDTree(HP)
print('couches prêtes',round(time.time()-t0),'s',flush=True)
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32);print('relief local prêt',round(time.time()-t0),'s',flush=True)
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
# lieux-dits pour la série 3e/11e
from shapely.ops import transform as stf
ld=json.load(gzip.open('ld.json.gz'));LDg=[(f['properties'].get('nom'),stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) for f in ld['features']]
def ld_series(az):
  line=LineString([T.transform(*G.fwd(tlo,tla,az,d)[:2]) for d in range(0,3200,40)])
  seq=[]
  for n,g in LDg:
    it=g.intersection(line)
    if not it.is_empty and it.length>5:
      pts=[Point(c) for gg in getattr(it,'geoms',[it]) for c in gg.coords];seq.append((min(line.project(p) for p in pts),n,g))
  seq.sort()
  if len(seq)<11: return None
  d=seq[2][2].centroid.distance(seq[10][2].centroid);return d,seq[2][1],seq[10][1],seq[10][2]
DATES={'30/04':73.9,'Pâques 2023':90.1,'Pâques 1524':91.3,'Pâques 2026':92.9,'équinoxe':104.0,'1er nov':128.7}
JD=[67.7,74.0,90.0,91.4,93.0,104.0];PAS=(0.65,0.75)
sN=(math.sin(math.radians(-2.2)),math.cos(math.radians(-2.2)))
def vec(az_true): a=math.radians(az_true-2.2);return math.sin(a),math.cos(a)
nE=vec(90.0)
def coffre(x,y,jd,pas):
  x1=x+10*pas*sN[0];y1=y+10*pas*sN[1];x2=x1+10*pas*nE[0];y2=y1+10*pas*nE[1];v=vec(jd);return x2+8*pas*v[0],y2+8*pas*v[1]


rows0=pickle.load(open('run/rows_final.pkl','rb'))
r0=[r for r in rows0 if abs(r['la']-45.42337)<2e-5 and abs(r['lo']-6.04166)<2e-5][0]
x,y=r0['x'],r0['y']
sN=(math.sin(math.radians(-2.2)),math.cos(math.radians(-2.2)))
def vec(az_true): a=math.radians(az_true-2.2);return math.sin(a),math.cos(a)
nE=vec(90.0)
def coffre(x,y,jd,pas):
  x1=x+10*pas*sN[0];y1=y+10*pas*sN[1];x2=x1+10*pas*nE[0];y2=y1+10*pas*nE[1];v=vec(jd);return x2+8*pas*v[0],y2+8*pas*v[1]
r2,c2=int((YN-y)/2),int((x-X0)/2);W=150
sub=acc[r2-W:r2+W+1,c2-W:c2+W+1]*4>=3000
rr,cc=np.where(sub);rr=rr+r2-W;cc=cc+c2-W
X=X0+cc*2+1;Y=YN-rr*2-1;dj=np.hypot(X-x,Y-y);ka=int(np.argmin(dj));print('ancre eau à',round(float(dj[ka])),'m')
cellset={(int(a),int(b)) for a,b in zip(rr,cc)};adj={}
for a,b in cellset:
  mvv=mv.get(int(fd[a,b]))
  if mvv:
    u=(a+mvv[0],b+mvv[1]);adj.setdefault((a,b),[]).append(u);adj.setdefault(u,[]).append((a,b))
anchor=(int(rr[ka]),int(cc[ka]));par={anchor:None};depth={anchor:0};q=[anchor];order=[]
while q:
  c=q.pop(0)
  for u in adj.get(c,[]):
    if u not in par and depth[c]+1<=200 and math.hypot(X0+u[1]*2+1-x,YN-u[0]*2-1-y)<=300:
      par[u]=c;depth[u]=depth[c]+1;q.append(u);order.append(u)
def path_up(u):
  p=[u]
  while par[p[-1]] is not None: p.append(par[p[-1]])
  return p
cells=[]
for c in order:
  cx,cy=X0+c[1]*2+1,YN-c[0]*2-1;dcj=math.hypot(cx-x,cy-y)
  if dcj<12: continue
  bp=float(bump[int(YN-cy),int(cx-X0)]);nn=c;zc=float(mnt[int(YN-cy),int(cx-X0)])
  for _ in range(5):
    mvv=mv.get(int(fd[nn[0],nn[1]]))
    if not mvv: break
    nn=(nn[0]+mvv[0],nn[1]+mvv[1])
  zn=float(mnt[int(YN-(YN-nn[0]*2-1)),int((X0+nn[1]*2+1)-X0)]);drop=zc-zn
  if not(bp>=0.9 or drop>=2.5): continue
  pxy=np.array([(X0+b*2+1,YN-a*2-1) for a,b in path_up(c)]);frac=float((kr.query(pxy)[0]<=30).mean())
  cells.append((cx,cy,dcj,frac,bp,drop))
print('cellules ressaut sur l eau :',len(cells))
JD={'28/10 astro (107.6)':107.6,'28/10 visible (126.6)':126.6,'30/04 julien astro (63.7)':63.7,'30/04 visible (74.0)':74.0,'Pâques 2025 (81.7)':81.7,'est (90)':90.0}
for nm,jd in JD.items():
  for pas in (0.65,0.75):
    n=0;ns=0;best=None
    for (cx,cy,dcj,frac,bp,drop) in cells:
      qx,qy=coffre(cx,cy,jd,pas)
      if PP.contains(Point(qx,qy)):
        hq=float(kb.query([qx,qy])[0]);rq=float(kr.query([qx,qy])[0])
        if hq>=100 and rq<=30:
          n+=1;s=PP2.contains(Point(qx,qy));ns+=s
          if best is None or (s and frac>=.5): best=(round(qx),round(qy),round(dcj),round(frac,2),s)
    print(nm,'pas',pas,'-> coffres publics possibles',n,'dont sûrs',ns,best)
