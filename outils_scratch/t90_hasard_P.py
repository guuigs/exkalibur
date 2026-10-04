import json,math,pickle,random,numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import shape
exec(open('ring1068.py').read().split('out=[]')[0])
rows=pickle.load(open('run/crible_rows.pkl','rb'))
def L93(r): return T.transform(r['lo'],r['la'])
Q=[r for r in rows if r['hb']>=100 and (r['wd']<=200 or r['ta']>=2) and r['cs']>=200 and r['fo']>=0.2]
J=np.array([L93(r) for r in Q]);print('croisements « qualifiés » (terrain seul, sans visibilité ni ouverture) :',len(Q),'sur',len(rows))
SRCp=[]
for f in json.load(open('large/detail_hydrographique.json'))['features']:
  if f['properties'].get('nature') in ('Source','Source captée'):
    c=shape(f['geometry']).centroid;SRCp.append((c.x,c.y))
SRCp=np.array(SRCp);tj=cKDTree(J);ts=cKDTree(SRCp)
def seat(cx,cy,az,k,dirn,R=1068.0):
  a=math.radians(az-dirn*(k-0.5)*30-2.2)
  return cx+R*math.sin(a),cy+R*math.cos(a)
def chord_dist(p3,p11,pt):
  ax,ay=p3;bx,by=p11;px,py=pt;dx,dy=bx-ax,by-ay;t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)));return math.hypot(ax+t*dx-px,ay+t*dy-py)
def frac(cx,cy,step=0.1):
  n1=n13=n123=0;tot=0
  for az in np.arange(55,125.01,step):
    for dirn in (1,-1):
      s11=seat(cx,cy,az,11,dirn);s3=seat(cx,cy,az,3,dirn);tot+=1
      d,i=tj.query(s11)
      if d<=60:
        n1+=1
        if chord_dist(s3,s11,J[i])<=25:
          n13+=1
          if ts.query(s11)[0]<=40: n123+=1
  return n1/tot,n13/tot,n123/tot
cr,ccn=3400.49,3955.34;TX,TY=X0+ccn,YN-cr
ft=frac(TX,TY)
print('TOUR : P(seat11≤60 m d un croisement qualifié)=%.2f %% | + corde ≤25 m de ce croisement=%.2f %% | + source ≤40 m=%.2f %%'%tuple(100*v for v in ft))
random.seed(7);res=[]
for _ in range(120):
  r=random.uniform(0,1300);a=random.uniform(0,2*math.pi);res.append(frac(TX+r*math.cos(a),TY+r*math.sin(a),0.2))
res=np.array(res)
print('centres au hasard (120, ≤1,3 km de la tour), moyenne : seat11 %.2f %% | +corde %.2f %% | +source %.2f %%'%tuple(100*res.mean(0)))
for j,nm in enumerate(('seat11','seat11+corde','seat11+corde+source')):
  print(f'   {nm}: rang de la tour = {(res[:,j]>=ft[j]).mean()*100:.1f} % des centres font au moins aussi bien ; 95e centile {100*np.percentile(res[:,j],95):.2f} %')
pickle.dump((ft,res),open('run/hasard_P.pkl','wb'))
