import json,math,pickle,numpy as np
from shapely.geometry import shape,Point,LineString,MultiLineString
from shapely.ops import unary_union,linemerge
from scipy.spatial import cKDTree
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy')
TX,TY=936955.34,6485599.51
Jx,Jy=T.transform(6.0320,45.42684)
PUB2=pickle.load(open('run/PUB2.pkl','rb'));BV=np.load('run/bat_dense.npy');kb=cKDTree(BV)
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)
roads=[]
for f in json.load(open('large/troncon_de_route.json'))['features']:
    g=shape(f['geometry'])
    if g.distance(Point(Jx,Jy))<=700:
        for l in getattr(g,'geoms',[g]): roads.append((l,f['properties'].get('nature')))
print('tronçons ≤700 m :',len(roads))
# réseau : nœuds aux extrémités ; on ré-échantillonne chaque ligne
def pts(l,step=5):
    n=max(2,int(l.length/step)+1);return [l.interpolate(i*l.length/(n-1)) for i in range(n)]
# bras sortants de J16 : lignes dont une extrémité est à <=15 m de J16
arms=[]
for l,nat in roads:
    for end,idx in ((l.coords[0],0),(l.coords[-1],-1)):
        if math.hypot(end[0]-Jx,end[1]-Jy)<=15:
            c=list(l.coords) if idx==0 else list(l.coords)[::-1]
            arms.append((LineString(c),nat))
print('bras sortants :',len(arms))
tw=np.column_stack(np.where(acc*4>=3000))
TW=np.column_stack([X0+tw[:,1]*2+1,YN-tw[:,0]*2-1]);kt=cKDTree(TW)
HY=[]
for f in json.load(open('large/troncon_hydrographique.json'))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
        for s in np.arange(0,l.length,3): p=l.interpolate(s);HY.append((p.x,p.y))
kh=cKDTree(np.array(HY))
SH=[]
for f in json.load(open('wfs_surface_hydrographique.json'))['features']:
    g=shape(f['geometry'])
    for p in getattr(g,'geoms',[g]):
        if p.geom_type=='Polygon':
            for s in np.arange(0,p.exterior.length,3): q=p.exterior.interpolate(s);SH.append((q.x,q.y))
ks=cKDTree(np.array(SH))
for ai,(arm,nat) in enumerate(arms):
    c=list(arm.coords);b=math.degrees(math.atan2(c[1][0]-c[0][0],c[1][1]-c[0][1]))%360
    # cap vrai moyen sur les 40 premiers mètres
    p40=arm.interpolate(min(40,arm.length));b40=(math.degrees(math.atan2(p40.x-c[0][0],p40.y-c[0][1]))+2.2)%360
    print('\n== bras %d (%s) longueur %.0f m ; cap vrai initial %.0f°'%(ai,nat,arm.length,b40))
    for s in np.arange(0,min(arm.length,420),30):
        p=arm.interpolate(s);q=arm.interpolate(min(arm.length,s+8));vx,vy=q.x-p.x,q.y-p.y
        L=math.hypot(vx,vy) or 1;vx/=L;vy/=L;lx,ly=-vy,vx   # gauche = rotation +90°
        # eau à gauche / droite (talweg ≥0,3 ha, ligne hydro, surface)
        def side(k):
            best=None
            for dist in (4,8,14,22,32):
                for sg,nm in ((1,'G'),(-1,'D')):
                    x=p.x+sg*lx*dist;y=p.y+sg*ly*dist
                    dd=min(kt.query([x,y])[0],kh.query([x,y])[0],ks.query([x,y])[0])
                    if dd<=4: 
                        if best is None: best=(nm,dist)
            return best
        w=side(0)
        r_,c_=int(YN-p.y),int(p.x-X0);bmax=float(bump[r_-8:r_+9,c_-8:c_+9].max())
        lo,la=Ti.transform(p.x,p.y)
        print('  %3d m : %.5f,%.5f | eau %s | bosse≤8 m %.2f | maisons %.0f m | public %s | dist J16 %.0f'%(s,la,lo,w,bmax,kb.query([p.x,p.y])[0],PUB2.contains(p),math.hypot(p.x-Jx,p.y-Jy)))
