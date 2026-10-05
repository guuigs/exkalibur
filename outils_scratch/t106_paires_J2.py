import json,gzip,math,pickle,numpy as np
from shapely.geometry import shape,Point
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
tr=lambda g:stf(lambda x,y,z=None:T.transform(x,y),g)
TX,TY=936955.34,6485599.51
C={}  # classe -> [(nom,x,y)]
def add(c,n,g): 
  p=g.representative_point() if g.geom_type!='Point' else g;C.setdefault(c,[]).append((n,p.x,p.y))
ld=json.load(gzip.open('ld.json.gz'))
for f in ld['features']: add('lieux-dits',f['properties']['nom'],tr(shape(f['geometry'])).centroid)
for ft in json.load(open('wfs_toponymie.json'))['features']:
  p=ft['properties'];g=shape(ft['geometry']);add('topo:'+str(p['nature_de_l_objet']),p['graphie_du_toponyme'],g.centroid)
for ft in json.load(open('wfs_construction_ponctuelle.json'))['features']:
  add('constr:'+ft['properties']['nature'],ft['properties']['toponyme'],shape(ft['geometry']).centroid)
for ft in json.load(open('wfs_detail_hydrographique.json'))['features']:
  add('hydro:'+ft['properties']['nature'],ft['properties']['toponyme'],shape(ft['geometry']).centroid)
for ft in json.load(open('wfs_detail_orographique.json'))['features']:
  add('oro:'+ft['properties']['nature'],ft['properties']['toponyme'],shape(ft['geometry']).centroid)
for ft in json.load(open('wfs_batiment.json'))['features']:
  n=ft['properties']['nature']
  if n in ('Eglise','Château','Chapelle','Tour, donjon'): add('bat:'+n,None,shape(ft['geometry']).centroid)
# regroupements plausibles
groups={'lieux-dits':['lieux-dits'],'croix':[k for k in C if k=='topo:Croix' or k=='constr:Croix'],'sacré':[k for k in C if k in('bat:Eglise','bat:Chapelle','constr:Clocher')],'eau':[k for k in C if k.startswith('hydro:') and k not in ('hydro:Marais',)],'oro':[k for k in C if k.startswith('oro:')],'tours/châteaux':['bat:Château','bat:Tour, donjon'],'transfo':['constr:Transformateur'],'antennes':['constr:Antenne']}
for k,v in C.items(): print(k,len(v))
rows=pickle.load(open('run/rows_final.pkl','rb'))
pickle.dump((C,groups),open('run/classes.pkl','wb'))
def pairs(pts,tol=0.01):
  out=[]
  for i in range(len(pts)):
    for j in range(i+1,len(pts)):
      d=math.hypot(pts[i][1]-pts[j][1],pts[i][2]-pts[j][2])
      if 1850*(1-tol)<=d<=1850*(1+tol): out.append((pts[i],pts[j],d))
  return out
PA={}
for g,ks in groups.items():
  pts=[p for k in ks for p in C.get(k,[])]
  PA[g]=pairs(pts);print(g,len(pts),'points ;',len(PA[g]),'paires à 1850 m ±1 %')
pickle.dump(PA,open('run/paires1850.pkl','wb'))
def seg_d(px,py,a,b):
  ax,ay,bx,by=a[1],a[2],b[1],b[2];dx,dy=bx-ax,by-ay;t=max(0,min(1,((px-ax)*dx+(py-ay)*dy)/(dx*dx+dy*dy)));return math.hypot(px-ax-t*dx,py-ay-t*dy),t
def score(x,y):
  s={}
  for g,pl in PA.items():
    a=0;m=0;e=0
    for A,B,d in pl:
      dd,t=seg_d(x,y,A,B)
      if dd<=40: a+=1
      if math.hypot(x-(A[1]+B[1])/2,y-(A[2]+B[2])/2)<=100: m+=1
      if min(math.hypot(x-A[1],y-A[2]),math.hypot(x-B[1],y-B[2]))<=100: e+=1
    s[g]=(a,m,e)
  return s
J2=[r for r in rows if abs(r['la']-45.42337)<2e-5 and abs(r['lo']-6.04166)<2e-5][0]
sJ=score(J2['x'],J2['y']);print('J2',sJ)
allS=[score(r['x'],r['y']) for r in rows]
for g in PA:
  for ii,nm in enumerate(['sur segment ≤40 m','milieu ≤100 m','extrémité ≤100 m']):
    v=np.array([s[g][ii] for s in allS]);j=sJ[g][ii]
    print(g,nm,'J2=',j,'| junctions >=:',int((v>=j).sum()) if j>0 else 'n/a','/',len(v),'moy',round(v.mean(),2))
