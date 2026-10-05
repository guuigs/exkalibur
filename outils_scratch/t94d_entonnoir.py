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
rows=[]
cand=[m for m in M if m[2]>=3 and 100<=math.hypot(m[0]-TX,m[1]-TY)<=2500 and X0+250<m[0]<X0+6750 and YN-6750<m[1]<YN-250]
print('croisements ≥3 voies entre 100 m et 2,5 km :',len(cand),flush=True)
for n_,m in enumerate(cand):
  x,y=m[0],m[1];lo,la=Ti.transform(x,y);az=G.inv(tlo,tla,lo,la)[0]%360;d=math.hypot(x-TX,y-TY)
  r1,c1=int(YN-y),int(x-X0)
  op=(mnh[r1-60:r1+61,c1-60:c1+61]<1.5)
  yy,xx=np.mgrid[-60:61,-60:61];disk=(xx**2+yy**2)<=3600
  vs=int((Vs[r1-60:r1+61,c1-60:c1+61]&op&disk).sum());vm=int((Vm[r1-60:r1+61,c1-60:c1+61]&op&disk).sum())
  op30=float((mnh[r1-30:r1+31,c1-30:c1+31]<1.5).mean())
  ring=((xx**2+yy**2)>=25**2)
  fo=float((mnh[r1-100:r1+101,c1-100:c1+101][(np.hypot(*np.mgrid[-100:101,-100:101])>=50)]>5).mean())
  hb=float(kb.query([x,y])[0]);wd=float(kh.query([x,y])[0]);rd0=float(kr.query([x,y])[0])
  ta=float(acc[r1//2-20:r1//2+21,c1//2-20:c1//2+21].max())*4/1e4
  D=mnt[r1-8:r1+9,c1-8:c1+9].astype(float);gy,gx=np.gradient(D);slope=float(np.degrees(np.arctan(np.hypot(gx,gy))).mean())
  # eau : cellules d'eau (talweg ≥ 0,3 ha) dans 300 m, reliées à l'ancre
  r2,c2=int((YN-y)/2),int((x-X0)/2);W=150
  sub=acc[r2-W:r2+W+1,c2-W:c2+W+1]*4>=3000
  rr,cc=np.where(sub);rr=rr+r2-W;cc=cc+c2-W
  best=None
  rocks=[]
  if len(rr):
    X=X0+cc*2+1;Y=YN-rr*2-1;dj=np.hypot(X-x,Y-y)
    k_anchor=int(np.argmin(dj));anch_d=float(dj[k_anchor])
    if anch_d<=80:
      cellset={(int(a),int(b)) for a,b in zip(rr,cc)}
      nxt={}
      for a,b in cellset:
        mvv=mv.get(int(fd[a,b]))
        if mvv: nxt[(a,b)]=(a+mvv[0],b+mvv[1])
      rev={}
      for k_,v_ in nxt.items(): rev.setdefault(v_,[]).append(k_)
      anchor=(int(rr[k_anchor]),int(cc[k_anchor]))
      adj={}
      for k_,v_ in nxt.items():
        adj.setdefault(k_,[]).append(v_);adj.setdefault(v_,[]).append(k_)
      par={anchor:None};depth={anchor:0};q=[anchor];order=[]
      while q:
        c=q.pop(0)
        for u in adj.get(c,[]):
          if u not in par and depth[c]+1<=200 and math.hypot(X0+u[1]*2+1-x,YN-u[0]*2-1-y)<=300:
            par[u]=c;depth[u]=depth[c]+1;q.append(u);order.append(u)
      def path_up(u):
        p=[u]
        while par[p[-1]] is not None: p.append(par[p[-1]])
        return p
      allc=[('eau',depth[u],u) for u in order]
      for sens,i,c in allc:
        cx,cy=X0+c[1]*2+1,YN-c[0]*2-1;dcj=math.hypot(cx-x,cy-y)
        if dcj<12 or dcj>300: continue
        bp=float(bump[int(YN-cy),int(cx-X0)])
        nn=c;zc=float(mnt[int(YN-cy),int(cx-X0)])
        for _ in range(5):
          mvv=mv.get(int(fd[nn[0],nn[1]]))
          if not mvv: break
          nn=(nn[0]+mvv[0],nn[1]+mvv[1])
        zn=float(mnt[int(YN-(YN-nn[0]*2-1)),int((X0+nn[1]*2+1)-X0)]);drop=zc-zn
        ress=(bp>=0.9 or drop>=2.5)
        if (not ress) and (len(rocks)>=600 or (i%2)): continue
        pathc=path_up(c)
        pxy=np.array([(X0+b*2+1,YN-a*2-1) for a,b in pathc])
        frac=float((kr.query(pxy)[0]<=30).mean())
        res=[]
        for jd in JD:
          for pas in PAS:
            qx,qy=coffre(cx,cy,jd,pas)
            if PP.contains(Point(qx,qy)):
              hq=float(kb.query([qx,qy])[0]);rq=float(kr.query([qx,qy])[0])
              if hq>=100 and rq<=30: res.append((jd,pas,qx,qy,hq,rq,PP2.contains(Point(qx,qy))))
        if res: rocks.append(dict(sens=sens,dist=dcj,bump=bp,drop=drop,ress=ress,frac=frac,cx=cx,cy=cy,res=res))
  # coffre public possible dans 300 m (surface raster 10 m)
  gx_=np.arange(x-300,x+301,10);gy_=np.arange(y-300,y+301,10);GX,GY=np.meshgrid(gx_,gy_)
  inside=(np.hypot(GX-x,GY-y)<=300)&contains_xy(PUB3,GX,GY)
  pts_=np.column_stack([GX[inside],GY[inside]])
  if len(pts_):
    okb=kb.query(pts_)[0]>=100;okr=kr.query(pts_)[0]<=30;cs=int((okb&okr).sum())*100
  else: cs=0
  # logique
  dz=d
  P_reach=(1008<=dz<=1128) and (100<=az<=170 or 10<=az<=80)
  th=None
  if P_reach:
    th=(az+315)%360 if 100<=az<=170 else (az-315)%360
  dateflag=[k for k,v in DATES.items() if abs(az-v)<=1.0]
  K=abs(az-95.4)<=1.5 and abs(dz-1850)<=18.5
  D10=abs(dz-1850)<=18.5
  ldr=None
  if any(abs(az-v)<=1.0 for v in DATES.values()):
    s=ld_series(az)
    if s: ldr=(round(s[0]),s[1],s[2],bool(abs(s[0]-1850)<=18.5 and s[3].distance(Point(x,y))<=100))
  rows.append(dict(la=la,lo=lo,x=x,y=y,d=d,az=az,deg=m[2],nat=sorted(set(m[4])),vs=vs,vm=vm,op=op30,fo=fo,hb=hb,wd=wd,ta=ta,slope=slope,cs=cs,rocks=rocks,P_reach=P_reach,theta=th,dates=dateflag,K=K,D10=D10,ld=ldr))
  if n_%40==0: print(n_,'/',len(cand),round(time.time()-t0),'s',flush=True)
pickle.dump(rows,open('run/entonnoir4_rows.pkl','wb'));print('terminé',len(rows),round(time.time()-t0),'s')
