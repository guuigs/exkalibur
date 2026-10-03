import numpy as np, math
from pyproj import Transformer, Geod
X0,YN,N=933000,6489000,7000
mnt=np.load('mnt.npy'); mnh=np.clip(np.nan_to_num(np.load('mnh.npy')),0,60)
tr=Transformer.from_crs(4326,2154,always_xy=True); G=Geod(ellps='WGS84')
def xy(lat,lon): return tr.transform(lon,lat)
def z(a,x,y):
  c=int(x-X0); r=int(YN-y); return a[r,c]
obs={'sommet tour (œil +33 m)':(45.4288723,6.03101275,33.0),'pied de la tour (1,7 m)':(45.4288723,6.03101275,1.7),'Rue du Rempart (1,7 m)':(45.42977,6.03118,1.7)}
tg={'K':(45.433594,6.044901),'K2':(45.434896,6.046208),'J2 (ancien)':(45.432042,6.043877)}
def los(o,t,th,canopy):
  x0,y0=xy(*o[:2]); x1,y1=xy(*t); z0=z(mnt,x0,y0)+o[2]; zt=z(mnt,x1,y1)+th
  D=math.hypot(x1-x0,y1-y0); worst=-1e9; wd=0
  for s in np.arange(15,D-3,1.0):
    x=x0+(x1-x0)*s/D; y=y0+(y1-y0)*s/D
    h=z(mnt,x,y)+(z(mnh,x,y) if canopy and D-s>3 else 0)
    need=z0+(zt-z0)*s/D
    if h-need>worst: worst,wd=h-need,s
  return worst,wd,D
for on,o in obs.items():
  print('\n###',on)
  for tn,t in tg.items():
    az=G.inv(o[1],o[0],t[1],t[0])[0]%360
    r1=los(o,t,1.5,False); r2=los(o,t,1.5,True)
    hc=z(mnh,*xy(*t))
    r3=los(o,t,hc,True) if hc>2 else None
    f=lambda r:("VISIBLE" if r[0]<0 else f"caché ({r[0]:+.1f} m à {r[1]:.0f} m)")
    print(f" {tn}: {r1[2]:.0f} m, cap {az:.1f}° | relief seul: {f(r1)} | relief+arbres, sol: {f(r2)}"+(f" | cime au point ({hc:.0f} m): {f(r3)}" if r3 else ''))
# fraction of a 30 m disc around K visible (ground) from tower top, terrain+trees
for tn in ['K','K2']:
  t=tg[tn]; x1,y1=xy(*t); o=obs['sommet tour (œil +33 m)']; vis=tot=0;visT=0
  for dx in range(-30,31,3):
    for dy in range(-30,31,3):
      if dx*dx+dy*dy>900: continue
      lon,lat=Transformer.from_crs(2154,4326,always_xy=True).transform(x1+dx,y1+dy)
      tot+=1; vis+= los(o,(lat,lon),1.5,True)[0]<0; visT+= los(o,(lat,lon),1.5,False)[0]<0
  print(f'{tn}: disque de 30 m, sol visible depuis le sommet (avec arbres) {vis}/{tot}, (relief seul) {visT}/{tot}')
print()
Ti=Transformer.from_crs(2154,4326,always_xy=True)
for tn in ['K','J2 (ancien)']:
  x1,y1=xy(*tg[tn]); o=obs['sommet tour (œil +33 m)']
  open_=vis=0; best=None
  for dx in range(-100,101,5):
    for dy in range(-100,101,5):
      if dx*dx+dy*dy>10000: continue
      if z(mnh,x1+dx,y1+dy)>1: continue
      open_+=1; lon,lat=Ti.transform(x1+dx,y1+dy)
      if los(o,(lat,lon),1.5,True)[0]<0:
        vis+=1; d=math.hypot(dx,dy)
        if best is None or d<best[0]: best=(d,lat,lon)
  print(f'{tn}: pré (sans arbre) dans 100 m : {open_} points, dont {vis} visibles du sommet ; plus proche visible : {best}')
