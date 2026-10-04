import numpy as np,math,json
src=open('t45_horizon.py').read().split("hz={a:horizon")[0]
exec(src)
N=7000
from shapely.geometry import shape
HS=[]
for f in json.load(open('wfs_troncon_hydrographique.json'))['features']:
  g=shape(f['geometry'])
  for l in getattr(g,'geoms',[g]):
    for s in np.arange(0,l.length,5): p=l.interpolate(s);HS.append((p.x,p.y,f['properties'].get('cpx_toponyme_de_cours_d_eau') or '?',f['properties'].get('persistance')))
for vname,vf,eye in (('pied','vs_pied.npy',1.7),('sommet','vs_sommet.npy',33)):
  V=np.unpackbits(np.load(vf))[:N*N].reshape(N,N).astype(bool)
  ozv=float(mnt[int(YN-oy),int(ox-X0)])+eye
  print('=== vue depuis',vname,'oeil',round(ozv,1))
  for nm,doy in (('Pâques 2026 (05/04)',95),('Pâques 1524 (06/04 grég.)',97),('équinoxe',80),('30/04 grég.',120)):
    dec=decl(doy);rows=[]
    first=None
    for h10 in range(-10,450):
      h=h10/10;az=sun_az(dec,h)
      hb,_=horizon(az)
      if h<hb: continue
      if first is None: first=(az,h)
      if h>first[1]+12: break
      for x,y,n,pers in HS:
        r,c=int(YN-y),int(x-X0)
        if not(0<=r<N and 0<=c<N) or not V[r,c]: continue
        d=math.hypot(x-ox,y-oy)
        if d<100: continue
        azp=(math.degrees(math.atan2(x-ox,y-oy))+2.2)%360
        dep=math.degrees(math.atan2(ozv-float(mnt[r,c]),d))
        if abs(azp-az)<3 and abs(dep-h)<1.5: rows.append((h,az,round(x),round(y),n,pers,round(d),round(dep,1)))
    print(f'{nm}: lever visible az {first[0]:.1f}° h {first[1]:.1f}° ; points d eau vus en reflet : {len(rows)}')
    seen=set()
    for r in rows:
      k=(r[4],r[2]//50,r[3]//50)
      if k in seen: continue
      seen.add(k);lo,la=Ti.transform(r[2],r[3])
      print(f'   soleil h {r[0]:.1f}° az {r[1]:.1f}° -> {la:.5f},{lo:.5f} {r[4]} ({r[5]}) à {r[6]} m, plongée {r[7]}°')
