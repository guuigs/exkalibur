import numpy as np,json,math
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy')*4.0;fdir=np.load('fdir.npy');g=2
dm={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
jx,jy=T.transform(6.040299,45.422426)
r2,c2=int((YN-jy)/g),int((jx-X0)/g);w=acc[r2-5:r2+6,c2-5:c2+6]
ys,xs=np.where(w>=2e4);k=np.argmin(np.hypot(ys-5,xs-5));r,c=r2-5+ys[k],c2-5+xs[k]
print('talweg près du croisement : bassin',round(acc[r,c]/1e4,2),'ha')
def trace_down(r,c,n=500):
  out=[]
  for i in range(n):
    out.append((X0+c*g+1,YN-r*g-1));v=int(fdir[r,c])
    if v not in dm: break
    a,b=dm[v];r,c=r+a,c+b
  return out
def trace_up(r,c,n=500):
  out=[]
  for i in range(n):
    best=None
    for v,(a,b) in dm.items():
      rr,cc=r-a,c-b
      if int(fdir[rr,cc])==v and (best is None or acc[rr,cc]>acc[best]): best=(rr,cc)
    if best is None or acc[best]<0.5e4: break
    r,c=best;out.append((X0+c*g+1,YN-r*g-1))
  return out
up=trace_up(r,c);dn=trace_down(r,c)
line=LineString(up[::-1]+dn);pj=line.project(Point(jx,jy))
print('longueur',round(line.length),'m ; croisement à',round(pj),'m de l\'amont')
for nm,pt in [('amont',line.coords[0]),('croisement',(jx,jy)),('aval',line.coords[-1])]:
  lo,la=Ti.transform(*pt[:2]);print(f'  {nm}: {la:.6f},{lo:.6f} z {z(mnt,*pt[:2]):.0f}')
# sources positions vs talweg
for nm,(la,lo) in {'source 1':(45.421767,6.040189),'source 2':(45.421003,6.039873)}.items():
  x,y=T.transform(lo,la);print(f'  {nm} : à {line.distance(Point(x,y)):.0f} m du talweg, position {line.project(Point(x,y)):.0f} m')
# parcels along upstream part & non cadastré
d=json.load(open('cad/38426-parcelles.json'));own=json.load(open('cad/pm_38426.json'))
NC=shape(json.load(open('cad/noncad.json')))
upline=LineString(up[::-1]+[(jx,jy)])
print('amont : longueur',round(upline.length),'m ; dans une bande non cadastrée :',round(upline.intersection(NC.buffer(3)).length),'m')
for f in d['features']:
  gg=stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0)
  L=upline.intersection(gg).length
  if L>3: o=own.get(f['properties']['id']);print(f"   {f['properties']['id']} {L:.0f} m -> {o[1] if o else 'particulier'}")
json.dump([Ti.transform(*p) for p in line.coords],open('mouret_talweg.json','w'))
