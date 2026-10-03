import numpy as np,json,math
from shapely.geometry import shape,Point,LineString
from shapely.ops import transform as stf
exec(open('ring1068.py').read().split('out=[]')[0])
acc=np.load('acc.npy')*4.0;fdir=np.load('fdir.npy');g=2
d=json.load(open('cad/38426-parcelles.json'))
B71=[stf(lambda x,y,z=None:T.transform(x,y),shape(f['geometry'])).buffer(0) for f in d['features'] if f['properties']['id']=='384260000B0071'][0]
# downstream trace from the max-acc cell inside B0071 using D8 (pysheds dirmap 64,128,1,2,4,8,16,32 = N,NE,E,SE,S,SW,W,NW)
dm={64:(-1,0),128:(-1,1),1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1)}
x,y=T.transform(6.048914,45.426838);r,c=int((YN-y)/g),int((x-X0)/g)
down=[]
for i in range(400):
  down.append((X0+c*g+1,YN-r*g-1));v=int(fdir[r,c])
  if v not in dm: break
  dr,dc=dm[v];r,c=r+dr,c+dc
# upstream: follow max-acc neighbour flowing into cell
x,y=T.transform(6.048914,45.426838);r,c=int((YN-y)/g),int((x-X0)/g);up=[]
inv={v:(-a,-b) for v,(a,b) in dm.items()}
for i in range(400):
  best=None
  for v,(a,b) in dm.items():
    rr,cc=r-a,c-b  # neighbour that would flow into (r,c) with direction v
    if int(fdir[rr,cc])==v and (best is None or acc[rr,cc]>acc[best[0],best[1]]): best=(rr,cc)
  if best is None or acc[best]<0.3e4: break
  r,c=best;up.append((X0+c*g+1,YN-r*g-1))
line=LineString(up[::-1]+down)
print('ravin : longueur',round(line.length),'m ; part dans B0071',round(line.intersection(B71).length),'m')
print('amont',[round(v,6) for v in Ti.transform(*line.coords[0])[::-1]],'z',round(z(mnt,*line.coords[0])),'| aval',[round(v,6) for v in Ti.transform(*line.coords[-1])[::-1]],'z',round(z(mnt,*line.coords[-1])))
# which bank is B0071 (relative to flow downstream)
cen=B71.centroid;pr=line.project(cen);p0=line.interpolate(pr);p1=line.interpolate(min(line.length,pr+5))
cr=(p1.x-p0.x)*(cen.y-p0.y)-(p1.y-p0.y)*(cen.x-p0.x)
print('B0071 est sur la rive',('GAUCHE' if cr>0 else 'DROITE'),'du ravin ; le ravin est',('dans' if line.intersection(B71).length>0 else 'hors de'),'la parcelle')
# junctions near the downstream outlet / along ravine
for dd,m in sorted([(line.distance(Point(m[0],m[1])),m) for m in M],key=lambda t:t[0])[:6]:
  lo,la=Ti.transform(m[0],m[1]);db=float(np.min(np.hypot(B[:,0]-m[0],B[:,1]-m[1])));pos=line.project(Point(m[0],m[1]))
  print(f'  croisement à {dd:.0f} m du ravin (à {pos:.0f} m de l\'amont) : {la:.6f},{lo:.6f} {m[2]} br {m[4][:3]} maisons {db:.0f}')
json.dump([Ti.transform(*c) for c in line.coords],open('ravin_B0071.json','w'))
