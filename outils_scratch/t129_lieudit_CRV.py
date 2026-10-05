import json,gzip,math,pickle,numpy as np
from shapely.geometry import shape,Point,box
from shapely.ops import transform as stf
from shapely import contains_xy
from scipy.spatial import cKDTree
from scipy import ndimage
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51
ld=json.load(gzip.open('ld.json.gz'))
LD=[(f['properties']['nom'],stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)) for f in ld['features']]
G1=[g for n,g in LD if n.startswith('LE CHENE LA')][0]
print('lieu-dit : aire %.0f m² ; centroïde %.0f m de la tour, cap %.0f°'%(G1.area,G1.centroid.distance(Point(TX,TY)),G1.centroid and G.inv(*Ti.transform(TX,TY),*Ti.transform(G1.centroid.x,G1.centroid.y))[0]%360))
PUB2=pickle.load(open('run/PUB2.pkl','rb'));BV=np.load('run/bat_dense.npy');kb=cKDTree(BV)
print('part publique sûre du lieu-dit : %.0f %%'%(100*G1.intersection(PUB2).area/G1.area))
GX,GY,ok,ok2,hb,dw,drk,dT=pickle.load(open('run/zone_autorisee.pkl','rb'))
inside=contains_xy(G1,GX,GY)
print('points 5 m dans le lieu-dit : %d ; public sûr+maisons>=100+chemin<=30 : %d ; +eau<=100 : %d ; +roche<=60 : %d'%(inside.sum(),(inside&ok).sum(),(inside&ok2).sum(),(inside&ok2&(drk<=60)).sum()))
# roches (bosses) dans le lieu-dit
bump=(mnt-ndimage.gaussian_filter(mnt,2.5)).astype(np.float32)
b=G1.bounds;r0=int(YN-b[3]);r1=int(YN-b[1]);c0=int(b[0]-X0);c1=int(b[2]-X0)
sub=bump[r0:r1,c0:c1];ry,rx=np.where(sub>=0.9);X=X0+c0+rx+0.5;Y=YN-(r0+ry)-0.5
m=contains_xy(G1,X,Y);X=X[m];Y=Y[m]
print('cellules rocheuses (bosse ≥0,9 m) dans le lieu-dit :',len(X))
if len(X):
    from scipy.cluster.hierarchy import fcluster,linkage
    P=np.column_stack([X,Y]);cl=fcluster(linkage(P,'single'),8,'distance')
    for c in sorted(set(cl),key=lambda c:-(cl==c).sum())[:8]:
        q=P[cl==c];lo,la=Ti.transform(q[:,0].mean(),q[:,1].mean())
        print('  amas rocheux %d cellules : %.5f,%.5f ; %.0f m de la tour ; maison la + proche %.0f m ; public %s'%(len(q),la,lo,math.hypot(q[:,0].mean()-TX,q[:,1].mean()-TY),kb.query([q[:,0].mean(),q[:,1].mean()])[0],PUB2.contains(Point(q[:,0].mean(),q[:,1].mean()))))
# croisements dans ou à <=30 m du lieu-dit
rows=pickle.load(open('run/rows_final2.pkl','rb'))
print('croisements ≥3 voies dans le lieu-dit (±30 m) :')
for r in sorted(rows,key=lambda r:r['d']):
    if G1.buffer(30).contains(Point(r['x'],r['y'])): print('  %.5f,%.5f %dm cap %.0f deg %d maison %d eauL %d eauS %d open %.2f vu %d pub2 %s'%(r['la'],r['lo'],r['d'],r['az'],r['deg'],r['hb'],r['wd'],r['eauS'],r['op'],max(r['vs'],r['vm']),r['pub2']))
