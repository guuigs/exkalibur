import numpy as np,json,math
from pyproj import Transformer,Geod
t=Transformer.from_crs(4326,2154,always_xy=True);ti=Transformer.from_crs(2154,4326,always_xy=True);g=Geod(ellps='WGS84')
M=np.load('mnt.npy',mmap_mode='r');H=np.load('mnh.npy',mmap_mode='r');X0=933000;YN=6489000;DB=np.load('rasters.npz')['d_bld']
def at(x,y): r=int(YN-y);c=int(x-X0);return float(M[r,c]),float(H[r,c])
# conv. L93 grid north vs true north at this longitude
lo0,la0=6.0465,45.4355;x0,y0=t.transform(lo0,la0);x1,y1=t.transform(lo0,la0+0.001);conv=math.degrees(math.atan2(x1-x0,y1-y0))
print('convergence méridienne L93 :',round(conv,2),'°')
G={'G1 rebord de la chute':(45.43550,6.04650),'G2 éperon rive est':(45.43505,6.04704)}
caps={'lever 30/04 (calendrier moderne, horizon plat) 67.8°':67.8,'lever 30/04/1524 julien (=10/05) 63.6°':63.6}
res=[]
for gn,(la,lo) in G.items():
  for pas in (0.75,1.48):
    # 10 N then 10 E (true north)
    lo1,la1,_=g.fwd(lo,la,0,10*pas);lo2,la2,_=g.fwd(lo1,la1,90,10*pas)
    sx,sy=t.transform(lo2,la2)
    # souche: look in 6 m radius for tree/stump signature
    best=[]
    for dx in range(-6,7):
      for dy in range(-6,7):
        if dx*dx+dy*dy>36: continue
        zg,hh=at(sx+dx,sy+dy);best.append((hh,dx,dy))
    hs=[b[0] for b in best];zz,h0=at(sx,sy)
    print(f'{gn} | pas {pas} m -> souche théorique {la2:.6f},{lo2:.6f} z {zz:.0f} m, canopée au point {h0:.1f} m (min {min(hs):.1f} / max {max(hs):.1f} dans 6 m), bâti {float(DB[int((YN-sy)/2),int((sx-X0)/2)]):.0f} m')
    for cn,cap in caps.items():
      lo3,la3,_=g.fwd(lo2,la2,cap,8*pas);zz3,h3=at(*t.transform(lo3,la3))
      print(f'      8 pas cap {cap}° -> CREUSER {la3:.6f},{lo3:.6f} (z {zz3:.0f}, canopée {h3:.1f} m)')
      res.append((gn,pas,cap,la2,lo2,la3,lo3))
json.dump(res,open('C/pas.json','w'))
