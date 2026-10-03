import json,numpy as np,math
from pyproj import Transformer
from scipy import ndimage
X0,Y0,N,g=933000,6482000,7000,2; n=N//g
M=np.load('M2.npy');H=np.load('H2.npy');dsm=M+H
V=np.load('viewsheds.npz')['tour_sommet']
acc=np.load('acc.npy')*g*g
inv=Transformer.from_crs(2154,4326,always_xy=True); tr=Transformer.from_crs(4326,2154,always_xy=True)
TX,TY=tr.transform(6.03101275,45.4288723)
def rc(x,y): return int((Y0+N-y)/g),int((x-X0)/g)
# distance rasters
chan=acc>2e4
d_chan=ndimage.distance_transform_edt(~chan)*g
wat=np.zeros((n,n),bool)
def burn(cs,R):
    for (x0,y0),(x1,y1) in zip(cs[:-1],cs[1:]):
        L=max(1,int(math.hypot(x1-x0,y1-y0)/1))
        for t in np.linspace(0,1,L+1):
            r,c=rc(x0+(x1-x0)*t,y0+(y1-y0)*t)
            if 0<=r<n and 0<=c<n: R[r,c]=True
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
    gm=f['geometry']; cs=gm['coordinates'] if gm['type']=='LineString' else [c for l in gm['coordinates'] for c in l]
    burn([(c[0],c[1]) for c in cs],wat)
d=json.load(open('osm.json'));Nn=d['nodes']
for wid,nds,t in d['ways']:
    if t.get('waterway') in ('stream','river','ditch','canal','brook'):
        burn([tr.transform(Nn[k][1],Nn[k][0]) for k in nds if k in Nn],wat)
d_wat=ndimage.distance_transform_edt(~wat)*g
bld=np.zeros((n,n),bool)
for f in json.load(open('wfs_batiment.json'))['features']:
    gm=f['geometry']; polys=gm['coordinates'] if gm['type']=='Polygon' else [p for mp in gm['coordinates'] for p in mp]
    for ring in polys[:1] if gm['type']=='Polygon' else polys:
        cs=ring if isinstance(ring[0][0],(int,float)) else ring[0]
        burn([(c[0],c[1]) for c in cs],bld)
d_bld=ndimage.distance_transform_edt(~bld)*g
forest=(H>5).astype(float)
ring=ndimage.uniform_filter(forest,size=41)   # ~80 m window
core=ndimage.uniform_filter(forest,size=9)    # ~18 m window
np.savez_compressed('rasters.npz',d_chan=d_chan,d_wat=d_wat,d_bld=d_bld,ring=ring,core=core)
# sun test
def lit(r,c,az,alt):
    z=M[r,c]+1; ta=math.tan(math.radians(alt))
    dx=math.sin(math.radians(az)); dy=-math.cos(math.radians(az))
    for s in range(1,2500):
        rr=int(r+dy*s); cc=int(c+dx*s)
        if not(0<=rr<n and 0<=cc<n): return True
        if dsm[rr,cc] > z+ s*g*ta: return False
    return True
SUN=[(64.5,0.5),(69,5),(74,10),(80,15),(85,20),(91,25)]
J=json.load(open('junctions.json')); out=[]
for j in J:
    r,c=rc(j['x'],j['y'])
    if not(3<=r<n-3 and 3<=c<n-3): continue
    dist=math.hypot(j['x']-TX,j['y']-TY)
    if dist<150 or dist>3500: continue
    lon,lat=inv.transform(j['x'],j['y'])
    b=math.degrees(math.atan2(j['x']-TX,j['y']-TY))%360
    sl=next((alt for az,alt in SUN if lit(r,c,az,alt)),None)
    out.append(dict(j,lat=round(lat,6),lon=round(lon,6),d=round(dist),cap=round(b,1),
        vis=bool(V[r-3:r+4,c-3:c+4].any()), canopy=float(H[r-1:r+2,c-1:c+2].mean()),
        ring=float(ring[r,c]),core=float(core[r,c]),d_chan=float(d_chan[r,c]),d_wat=float(d_wat[r,c]),
        d_bld=float(d_bld[r,c]),z=float(M[r,c]),sun_alt=sl))
json.dump(out,open('junc_attrs.json','w')); print(len(out))
