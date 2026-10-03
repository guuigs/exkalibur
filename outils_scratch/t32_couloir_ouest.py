import json,math,numpy as np
exec(open('sens.py').read().split('for az in (95.78')[0])
X,Y=T.transform(6.03101275,45.4288723);Z0=z(mnt,X,Y)+33
Xp,Yp=T.transform(6.03115,45.42887);Zp=z(mnt,Xp,Yp)+1.7
rows=[]
for m in M:
  lon,lat=Ti.transform(m[0],m[1]);az,_,d=G.inv(6.03101275,45.4288723,lon,lat);az%=360
  if not(1700<=d<=3200 and 271<=az<=281): continue
  op,ring,db,w,rl,ra=info(m[0],m[1],(X,Y,Z0))
  rp=los(Xp,Yp,Zp,m[0],m[1],True)
  t=topo(m[0],m[1])
  rows.append((round(d),round(az,1),round(lat,6),round(lon,6),m[2],m[4][:3],round(op,2),round(ring,2),round(db),round(w[0]),w[1],round(rl,1),round(ra,1),round(rp,1),t[1]))
print('dist cap lat lon br nature ouvert forêt maisons eau(nom) relief arbres(sommet) arbres(pied) lieu-dit')
for r in sorted(rows): print(r)
