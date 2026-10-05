import json,math,pickle,numpy as np
from shapely.geometry import shape,Polygon,Point
from shapely import affinity
from scipy.spatial import cKDTree
from scipy import ndimage
exec(open('/home/user/exkalibur/outils_scratch/t126_vernay_fit.py').read().split('Vn=norm(V)')[0])
TX,TY=936955.34,6485599.51
pts2=[(100,18),(150,8),(200,10),(235,12),(270,5),(300,25),(325,55),(338,100),(343,150),(335,190),(320,215),(285,228),(245,228),(210,210),(180,190),(150,165),(125,152),(100,147),(98,100),(100,50)]
P2=Polygon([(x,-y) for x,y in pts2]).buffer(0);c2=P2.centroid;s2=1/math.sqrt(P2.area)
fall=(205,5);cup=(130,41)
def line_pts(fn,step=4):
  pts=[]
  for f in json.load(open(fn))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
      for s in np.arange(0,l.length,step): p=l.interpolate(s);pts.append((p.x,p.y))
  return np.array(pts)
kh=cKDTree(line_pts('large/troncon_hydrographique.json'))
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)
C=[]
for ft in json.load(open('wfs_surface_hydrographique.json'))['features']:
    gm=shape(ft['geometry'])
    for p in getattr(gm,'geoms',[gm]):
        if p.geom_type=='Polygon' and p.area>300: C.append(('bdtopo '+str(ft['properties'].get('nature')),p))
for w in d['ways']:
    tags=w[2];ids=w[1]
    if (tags.get('natural')=='water' or tags.get('water') in('pond','lake','reservoir') or tags.get('landuse')=='basin') and ids and ids[0]==ids[-1]:
        pp=[nodes[str(i)] for i in ids if str(i) in nodes]
        if len(pp)>=4:
            p=Polygon([T.transform(lo,la) for la,lo in pp]).buffer(0)
            if p.area>300: C.append(('osm '+str(tags.get('name') or tags.get('water') or ''),p))
def place(q,rot):
    Qc=q.centroid;sq=math.sqrt(q.area)
    def tr(x,y):
        X,Y=(x-c2.x)*s2,(y-c2.y)*s2;a=math.radians(rot);return Qc.x+(X*math.cos(a)-Y*math.sin(a))*sq,Qc.y+(X*math.sin(a)+Y*math.cos(a))*sq
    return Polygon([tr(x,y) for x,y in P2.exterior.coords]),tr(*fall),tr(*cup)
rows=[]
for nm,q in C:
    qs=q.simplify(1.0);qn=affinity.scale(affinity.translate(qs,-qs.centroid.x,-qs.centroid.y),1/math.sqrt(qs.area),1/math.sqrt(qs.area),origin=(0,0))
    N2=affinity.scale(affinity.translate(P2,-c2.x,-c2.y),s2,s2,origin=(0,0))
    best=(0,0)
    for a in range(0,360,2):
        r=affinity.rotate(N2,a,origin=(0,0));i=qn.intersection(r).area/qn.union(r).area
        if i>best[0]: best=(i,a)
    pl,(fx,fy),(cx,cy)=place(q,best[1])
    dh=float(kh.query([fx,fy])[0]);dbd=float(Point(fx,fy).distance(q.exterior))
    r_,c_=int(YN-cy),int(cx-X0)
    bp=float(bump[r_-30:r_+31,c_-30:c_+31].max()) if 30<r_<mnt.shape[0]-30 and 30<c_<mnt.shape[1]-30 else None
    lo,la=Ti.transform(q.centroid.x,q.centroid.y)
    rows.append(dict(nm=nm,aire=round(q.area),iou=best[0],rot=best[1],d_tour=round(q.centroid.distance(Point(TX,TY))),la=la,lo=lo,dh=dh,dbd=dbd,bump=bp))
rows.sort(key=lambda r:-r['iou'])
print('IoU | nom | aire | dist tour | cours d eau BD TOPO à la chute | bord | bosse rocheuse max autour de la coupe')
for r in rows[:14]: print('%.3f'%r['iou'],r['nm'],r['aire'],'m²',r['d_tour'],'m','| hydro %.0f m'%r['dh'],'| bord %.0f m'%r['dbd'],'| bosse',None if r['bump'] is None else round(r['bump'],2),'|',round(r['la'],5),round(r['lo'],5))
print('\nOù un cours d eau BD TOPO arrive à ≤25 m de la chute et IoU ≥0,75 :')
for r in rows:
    if r['iou']>=0.75 and r['dh']<=25: print('%.3f'%r['iou'],r['nm'],r['aire'],'m²',r['d_tour'],'m','| hydro %.0f m'%r['dh'],'| bosse',None if r['bump'] is None else round(r['bump'],2),round(r['la'],5),round(r['lo'],5))
pickle.dump(rows,open('run/etang_discrim.pkl','wb'))
