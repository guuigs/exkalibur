import numpy as np, math, json
from scipy import ndimage
from pyproj import Transformer
X0,Y0,N=933000,6482000,7000
mnt=np.load('mnt.npy').astype(np.float32); mnh=np.nan_to_num(np.load('mnh.npy'))
tr=Transformer.from_crs(4326,2154,always_xy=True); inv=Transformer.from_crs(2154,4326,always_xy=True)
TX,TY=tr.transform(6.03101275,45.4288723)
R=np.load('rasters.npz'); d_bld2=R['d_bld']; d_wat2=R['d_wat']
# flat patches: slope < 1.5 deg on 1 m grid, smoothed DEM
gy,gx=np.gradient(ndimage.uniform_filter(mnt,3))
slope=np.degrees(np.arctan(np.hypot(gx,gy)))
# local depression: flat AND lower than 20 m ring median by >0.3 m (basin)
med=ndimage.median_filter(mnt[::2,::2],size=21); med=np.kron(med,np.ones((2,2)))[:N,:N]
flat=(slope<1.5)&(mnt<med-0.2)
yy,xx=np.mgrid[0:N,0:N]
D=np.hypot(X0+xx-TX,(Y0+N-yy)-TY)
flat&=(D>200)&(D<3500)
lab,k=ndimage.label(flat)
print('patches',k)
res=[]
sizes=ndimage.sum(flat,lab,range(1,k+1))
for i in np.where((sizes>=40)&(sizes<=4000))[0]+1:
    sl=ndimage.find_objects(lab==i)[0] if False else None
objs=ndimage.find_objects(lab)
for i,sl in enumerate(objs,1):
    if sl is None: continue
    m=lab[sl]==i; a=m.sum()
    if a<40 or a>4000: continue
    rr,cc=np.argwhere(m).mean(0); r=int(rr+sl[0].start); c=int(cc+sl[1].start)
    # compactness
    h,w=m.shape; ext=a/(h*w)
    # steepness upstream: max slope within 15 m
    win=slope[max(0,r-15):r+16,max(0,c-15):c+16]
    canopy=float(mnh[sl][m].mean())
    db=float(d_bld2[r//2,c//2]); dw=float(d_wat2[r//2,c//2])
    x=X0+c; y=Y0+N-r; lo,la=inv.transform(x,y)
    res.append(dict(lat=round(la,6),lon=round(lo,6),area=int(a),ext=round(ext,2),maxslope15=round(float(win.max()),1),canopy=round(canopy,1),d_bld=round(db),d_wat=round(dw),d=round(math.hypot(x-TX,y-TY)),cap=round(math.degrees(math.atan2(x-TX,y-TY))%360,1)))
json.dump(res,open('basins.json','w'))
print(len(res))
sel=[b for b in res if b['d_bld']>100 and b['maxslope15']>35]
for b in sorted(sel,key=lambda b:b['d'])[:40]: print(b)
print(len(sel),'avec bâtiment>100 m et pente forte <15 m (chute ?)')
