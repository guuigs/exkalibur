import json,math,pickle,numpy as np
from shapely.geometry import shape,Point
from shapely import contains_xy
from scipy.spatial import cKDTree
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0])
PUB2=pickle.load(open('run/PUB2.pkl','rb'));PUB3=pickle.load(open('run/PUB3.pkl','rb'));BV=np.load('run/bat_dense.npy');kb=cKDTree(BV)
def line_pts(fn,step=3):
  pts=[]
  for f in json.load(open(fn))['features']:
    g=shape(f['geometry'])
    for l in getattr(g,'geoms',[g]):
      for s in np.arange(0,l.length,step): p=l.interpolate(s);pts.append((p.x,p.y))
  return np.array(pts)
kr=cKDTree(line_pts('large/troncon_de_route.json'));kh=cKDTree(line_pts('large/troncon_hydrographique.json'))
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)
sN=(math.sin(math.radians(-2.2)),math.cos(math.radians(-2.2)))
def vec(az_true): a=math.radians(az_true-2.2);return math.sin(a),math.cos(a)
nE=vec(90.0)
def coffre(x,y,jd,pas):
  x1=x+10*pas*sN[0];y1=y+10*pas*sN[1];x2=x1+10*pas*nE[0];y2=y1+10*pas*nE[1];v=vec(jd);return x2+8*pas*v[0],y2+8*pas*v[1]
# roches : cellules bosse>=0,9 dans les zones autorisées du Châtelard (rayon 60 m autour des 4 centres)
cent=[(45.42524,6.03277),(45.42485,6.03222),(45.42544,6.03321),(45.42420,6.03014)]
cells=[]
for la,lo in cent:
    x,y=T.transform(lo,la);r0,c0=int(YN-y),int(x-X0)
    sub=bump[r0-60:r0+61,c0-60:c0+61];ry,rx=np.where(sub>=0.9)
    for a,b in zip(ry,rx): cells.append((X0+c0-60+b+0.5,YN-(r0-60+a)-0.5,la))
Jx,Jy=T.transform(6.0320,45.42684);cells=[c for c in cells if math.hypot(c[0]-Jx,c[1]-Jy)<=350];print('cellules rocheuses à ≤350 m de J16 :',len(cells))
JD={'30/04 julien astro 63.7':63.7,'30/04 plat 68.6':68.6,'30/04 visible 73.9':73.9,'28/10 visible 126.6':126.6}
for nm,jd in JD.items():
    for pas in (0.65,0.75):
        ok=[];ns=0
        for (cx,cy,la) in cells:
            qx,qy=coffre(cx,cy,jd,pas);p=Point(qx,qy)
            if PUB3.contains(p):
                hq=kb.query([qx,qy])[0];rq=kr.query([qx,qy])[0]
                if hq>=100 and rq<=30:
                    ok.append((qx,qy,hq,rq,PUB2.contains(p),la));ns+=PUB2.contains(p)
        print(nm,'pas',pas,'-> coffres publics possibles',len(ok),'dont sûrs',ns)
        if ok:
            a=ok[0];lo,la=Ti.transform(a[0],a[1]);print('     ex. %.6f,%.6f maisons %.0f chemin %.0f sûr %s (roche près de %.5f) ; toutes :'%(la,lo,a[2],a[3],a[4],a[5]),sorted(set((round(Ti.transform(o[0],o[1])[1],5),round(Ti.transform(o[0],o[1])[0],5)) for o in ok))[:6])
