import json,math,numpy as np
from shapely.geometry import shape,Polygon,Point
from shapely import affinity
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51
pts=[(25,12),(60,12),(100,18),(150,8),(200,10),(235,12),(270,5),(300,25),(325,55),(338,100),(343,150),(335,190),(320,215),(285,228),(245,228),(210,210),(180,190),(150,165),(125,152),(95,147),(70,130),(50,105),(35,75),(22,45)]
P0=Polygon([(x,-y) for x,y in pts]).buffer(0)
def norm(p):
    p=affinity.translate(p,-p.centroid.x,-p.centroid.y);return affinity.scale(p,1/math.sqrt(p.area),1/math.sqrt(p.area),origin=(0,0))
N0=norm(P0)
def best_iou(q,step=3):
    qn=norm(q);b=(0,0,0)
    for mirror in (0,1):
        qq=affinity.scale(qn,-1,1,origin=(0,0)) if mirror else qn
        for a in range(0,360,step):
            r=affinity.rotate(qq,a,origin=(0,0))
            i=N0.intersection(r).area;u=N0.union(r).area
            if i/u>b[0]: b=(i/u,a,mirror)
    return b
C=[]
for ft in json.load(open('wfs_surface_hydrographique.json'))['features']:
    gm=shape(ft['geometry'])
    for p in getattr(gm,'geoms',[gm]):
        if p.geom_type=='Polygon' and p.area>300: C.append(('bdtopo '+str(ft['properties'].get('nature')),p))
d=json.load(open('osm.json'));nodes=d['nodes']
for w in d['ways']:
    tags=w[2];ids=w[1]
    if (tags.get('natural')=='water' or tags.get('water') in('pond','lake','reservoir') or tags.get('landuse')=='basin') and ids and ids[0]==ids[-1]:
        pp=[nodes[str(i)] for i in ids if str(i) in nodes]
        if len(pp)>=4:
            p=Polygon([T.transform(lo,la) for la,lo in pp]).buffer(0)
            if p.area>300: C.append(('osm '+str(tags.get('name') or tags.get('water') or ''),p))
print('candidats',len(C))
res=[]
for nm,p in C:
    b=best_iou(p.simplify(1.0));lo,la=Ti.transform(p.centroid.x,p.centroid.y)
    res.append((b[0],nm,round(p.area),round(p.centroid.distance(Point(TX,TY))),round(la,5),round(lo,5),b[1],b[2]))
res.sort(reverse=True)
for r in res[:12]: print('IoU %.3f'%r[0],r[1],r[2],'m²',r[3],'m de la tour',r[4],r[5],'rot',r[6],'miroir',r[7])
v=[r for r in res if 'Vernay' in r[1]]
print('Vernay :',v)
ious=np.array([r[0] for r in res]);print('médiane IoU %.3f ; 90e centile %.3f'%(np.median(ious),np.percentile(ious,90)))
print('\nPlans d eau à moins de 1,5 km de la tour :')
for i,r in enumerate(res,1):
    if r[3]<=1500: print('rang %d/%d IoU %.3f'%(i,len(res),r[0]),r[1],r[2],'m²',r[3],'m',r[4],r[5])
print('rang du Vernay : %d/%d'%([i for i,r in enumerate(res,1) if 'Vernay' in r[1]][0],len(res)))
