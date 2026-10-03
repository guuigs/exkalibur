import json,math,numpy as np
exec(open('table_orient.py').read().split('r=1068')[0])
cx,cy=T.transform(6.0388,45.4210)
# real junctions within 450 m
print('Croisements réels autour du Mouret / Les Tilles :')
for dd,m in sorted([(math.hypot(m[0]-cx,m[1]-cy),m) for m in M],key=lambda t:t[0]):
  if dd>450: break
  lon,lat=Ti.transform(m[0],m[1]);az,_,d=G.inv(TOP[1],TOP[0],lon,lat)
  db=float(np.min(np.hypot(B[:,0]-m[0],B[:,1]-m[1])));dw=float(np.min(np.hypot(HS[:,0]-m[0],HS[:,1]-m[1])))
  op=np.mean([z(mnh,m[0]+a,m[1]+b)<2 for a in range(-25,26,3) for b in range(-25,26,3) if math.hypot(a,b)<=25])
  ring=np.mean([z(mnh,m[0]+a,m[1]+b)>5 for a in range(-120,121,8) for b in range(-120,121,8) if 50<=math.hypot(a,b)<=120])
  n=vs=vp=0
  for a in range(-50,51,10):
    for b in range(-50,51,10):
      if math.hypot(a,b)>50 or z(mnh,m[0]+a,m[1]+b)>=1.5: continue
      n+=1;vs+=los(X0t,Y0t,Zs,m[0]+a,m[1]+b,True)<0;vp+=los(Xp,Yp,Zp,m[0]+a,m[1]+b,True)<0
  rel=los(X0t,Y0t,Zs,m[0],m[1],False);relp=los(Xp,Yp,Zp,m[0],m[1],False)
  print(f' {lat:.6f},{lon:.6f} | tour {d:.0f} m cap {az%360:.0f}° | {m[2]} br {m[4][:3]} | maisons {db:.0f} | eau {dw:.0f} | ouvert25 {op:.2f} forêt {ring:.2f} | ouvert50 {n} vus sommet {vs} pied {vp} | relief sommet {rel:+.1f} pied {relp:+.1f} | {topo(m[0],m[1])[1]}')
