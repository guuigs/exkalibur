import json,math,re,numpy as np,networkx as nx
from pyproj import Transformer,Geod
T=Transformer.from_crs(4326,2154,always_xy=True);Ti=Transformer.from_crs(2154,4326,always_xy=True);G=Geod(ellps='WGS84')
# --- scratch main chain (3,0) -> (126,683), then tail to (159,837)
svg=open('/home/user/exkalibur/vault_EXKALIBUR/_Resolution/Revue_globale/rayure_epee_guilhem_blanc.svg').read()
dstr=re.search(r'd="([^"]+)"',svg).group(1)
def parse(seg):
  toks=re.findall(r'[MLVHC]|-?\d+\.?\d*',seg);pts=[];cur=None;i=0;cmd=None
  while i<len(toks):
    t=toks[i]
    if t in 'MLVHC': cmd=t;i+=1;continue
    if cmd in 'ML': cur=(float(toks[i]),float(toks[i+1]));pts.append(cur);i+=2
    elif cmd=='V': cur=(cur[0],float(t));pts.append(cur);i+=1
    elif cmd=='H': cur=(float(t),cur[1]);pts.append(cur);i+=1
    elif cmd=='C': cur=(float(toks[i+4]),float(toks[i+5]));pts.append(cur);i+=6
  return pts
subs=['M'+s for s in dstr.split('M') if s.strip()]
paths=[parse(s) for s in subs]
main=[p for p in paths if p[0]==(3.0,0.0)][0]
tail=[p for p in paths if p[0]==(159.0,837.0)][0][::-1]  # from 126,683 to 159,837
print('tronc',len(main),'pts, fin',main[-1],'| queue',tail[0],'->',tail[-1])
def resample(pts,n=150):
  P=np.array(pts,float);d=np.r_[0,np.cumsum(np.hypot(*np.diff(P,axis=0).T))];t=np.linspace(0,d[-1],n)
  return np.c_[np.interp(t,d,P[:,0]),np.interp(t,d,P[:,1])],d[-1]
S,Ls=resample([(x,-y) for x,y in main])   # y up
chord=np.hypot(*(S[-1]-S[0]));print('rayure : longueur/corde =',round(Ls/chord,2))
# --- path graph (BD TOPO)
r=json.load(open('wfs_troncon_de_route.json'))
Gr=nx.Graph();key=lambda c:(round(c[0],1),round(c[1],1))
for f in r['features']:
  cs=[c[:2] for c in f['geometry']['coordinates']]
  L=sum(math.dist(cs[i],cs[i+1]) for i in range(len(cs)-1))
  a,b=key(cs[0]),key(cs[-1])
  if a==b: continue
  if Gr.has_edge(a,b) and Gr[a][b]['w']<=L: continue
  Gr.add_edge(a,b,w=L,geom=cs)
px,py=T.transform(6.03115,45.42887)
starts=sorted(Gr.nodes,key=lambda n:math.hypot(n[0]-px,n[1]-py))[:3]
print('départs (nœuds proches du pied) :',[round(math.hypot(n[0]-px,n[1]-py)) for n in starts])
def align_score(R,S):
  # similarity transform mapping S endpoints onto R endpoints, then mean distance / chord
  s0,s1=S[0],S[-1];r0,r1=R[0],R[-1]
  vs=s1-s0;vr=r1-r0;sc=np.hypot(*vr)/np.hypot(*vs);ang=math.atan2(vr[1],vr[0])-math.atan2(vs[1],vs[0])
  Rm=np.array([[math.cos(ang),-math.sin(ang)],[math.sin(ang),math.cos(ang)]])
  St=(S-s0)@Rm.T*sc+r0
  return float(np.mean(np.hypot(*(St-R).T))/np.hypot(*vr))
res=[]
for st in starts:
  dist,paths_=nx.single_source_dijkstra(Gr,st,weight='w',cutoff=6000)
  for n,pth in paths_.items():
    if Gr.degree(n)<3: continue
    eu=math.hypot(n[0]-px,n[1]-py)
    if eu<300 or eu>4000: continue
    geo=[]
    for a,b in zip(pth,pth[1:]):
      g=Gr[a][b]['geom'];g=g if key(g[0])==a else g[::-1];geo+=g
    R,Lr=resample(geo)
    sc=align_score(R,S);sm=align_score(R,S*np.array([-1,1]))  # mirror control
    res.append((sc,sm,n,eu,Lr/eu,len(pth)))
res.sort()
print('itinéraires testés',len(res))
allsc=np.array([x[0] for x in res]);allm=np.array([x[1] for x in res])
print('meilleur score',round(allsc.min(),3),'| meilleur miroir',round(allm.min(),3),'| médiane',round(np.median(allsc),3))
seen=set()
for sc,sm,n,eu,ratio,k in res[:25]:
  if n in seen: continue
  seen.add(n);lo,la=Ti.transform(*n);az,_,_=G.inv(6.03115,45.42887,lo,la)
  print(f'score {sc:.3f} (miroir {sm:.3f}) | croisement {la:.6f},{lo:.6f} deg {Gr.degree(n)} | {eu:.0f} m cap {az%360:.0f}° | sinuosité {ratio:.2f}')

print('\n=== avec sinuosité (±25 %) + queue au bon angle ===')
Tq,_=resample([(x,-y) for x,y in tail],20)
def tail_dir(S_,tq):
  v=S_[-1]-S_[0];w=tq[-1]-tq[0]
  return math.degrees(math.atan2(w[1],w[0])-math.atan2(v[1],v[0])), np.hypot(*w)/np.hypot(*v)
td,tr=tail_dir(S,Tq);print('queue de la rayure : angle par rapport à la corde',round(td,1),'°, longueur relative',round(tr,2))
def eval_set(S_,Tq_):
  out=[]
  td,tr=tail_dir(S_,Tq_)
  for sc,sm,n,eu,ratio,k in res:
    if not(1.62*0.75<=ratio<=1.62*1.25): continue
    # chord direction of route
    for st in starts[:1]:
      pass
    out.append((sc,n,eu,ratio))
  return out
# recompute properly with tail check
best=[];bestm=[]
for st in starts:
  dist,paths_=nx.single_source_dijkstra(Gr,st,weight='w',cutoff=6000)
  for n,pth in paths_.items():
    if Gr.degree(n)<3: continue
    eu=math.hypot(n[0]-px,n[1]-py)
    if eu<300 or eu>4000: continue
    geo=[]
    for a,b in zip(pth,pth[1:]):
      g=Gr[a][b]['geom'];g=g if key(g[0])==a else g[::-1];geo+=g
    R,Lr=resample(geo);ratio=Lr/eu
    if not(1.2<=ratio<=2.05): continue
    vr=R[-1]-R[0];cang=math.atan2(vr[1],vr[0])
    for mirror,store in ((1,best),(-1,bestm)):
      Sx=S*np.array([mirror,1]);Tx=Tq*np.array([mirror,1])
      sc=align_score(R,Sx);td,tr=tail_dir(Sx,Tx)
      # best continuation edge from n (not the arriving one)
      prev=pth[-2];tb=9
      for nb in Gr[n]:
        if nb==prev: continue
        g=Gr[n][nb]['geom'];g=g if key(g[0])==n else g[::-1]
        w=np.array(g[min(len(g)-1,5)])-np.array(g[0]);a=math.degrees(math.atan2(w[1],w[0])-cang)
        dA=abs((a-td+180)%360-180);tb=min(tb,dA/180)
      store.append((sc+0.15*tb,sc,tb*180,n,eu,ratio))
best.sort();bestm.sort()
print('itinéraires gardés',len(best),'| meilleur réel',round(best[0][0],3),'| meilleur miroir',round(bestm[0][0],3))
qs=[0.01,0.05,0.5];print('quantiles réel',[round(np.quantile([b[0] for b in best],q),3) for q in qs],'miroir',[round(np.quantile([b[0] for b in bestm],q),3) for q in qs])
seen=set()
for tot,sc,ta,n,eu,ratio in best[:30]:
  if n in seen: continue
  seen.add(n);lo,la=Ti.transform(*n);az,_,_=G.inv(6.03115,45.42887,lo,la)
  print(f'total {tot:.3f} forme {sc:.3f} écart queue {ta:.0f}° | {la:.6f},{lo:.6f} deg {Gr.degree(n)} | {eu:.0f} m cap {az%360:.0f}° | sinuosité {ratio:.2f}')
  if len(seen)>=10: break
