import json,math,numpy as np
exec(open('ring1068.py').read().split('out=[]')[0])   # T,Ti,G,mnt,mnh,z,M (junctions),H (hydro pts),B (buildings),los
ox,oy=T.transform(6.03101275,45.4288723)
obs={'sommet':(ox,oy,z(mnt,ox,oy)+33.0)}
rx,ry=T.transform(6.03118,45.42977);obs['rue']=(rx,ry,z(mnt,rx,ry)+1.7)
px_,py_=T.transform(6.03115,45.42887);obs['pied']=(px_,py_,z(mnt,px_,py_)+1.7)
print('limite est LiDAR x=',X0+7000,'tour x=',round(ox))
res=[]
for m in M:
  dx,dy=m[0]-ox,m[1]-oy;d=math.hypot(dx,dy);az=math.degrees(math.atan2(dx,dy))%360
  if not (1500<=d<=3200 and 90<=az<=102): continue
  if m[0]>X0+7000-130: continue
  # openness around junction
  op=[];fo=[]
  for ddx in range(-60,61,3):
    for ddy in range(-60,61,3):
      rr=math.hypot(ddx,ddy);h=z(mnh,m[0]+ddx,m[1]+ddy)
      if rr<=20: op.append(h<2)
      elif 35<=rr<=60: fo.append(h>5)
  db=float(np.min(np.hypot(B[:,0]-m[0],B[:,1]-m[1])));dw=float(np.min(np.hypot(H[:,0]-m[0],H[:,1]-m[1])))
  v={}
  for k,(a,b,c) in obs.items():
    v[k+'_relief']=round(los(a,b,c,m[0],m[1],False),1)
    v[k+'_arbres']=round(los(a,b,c,m[0],m[1],True),1)
  # open cells within 40 m visible from sommet & pied (with trees)
  vis_open={'sommet':0,'pied':0};n_open=0
  for ddx in range(-40,41,8):
    for ddy in range(-40,41,8):
      if math.hypot(ddx,ddy)>40 or z(mnh,m[0]+ddx,m[1]+ddy)>=2: continue
      n_open+=1
      for k in ('sommet','pied'):
        a,b,c=obs[k]
        if los(a,b,c,m[0]+ddx,m[1]+ddy,True)<0: vis_open[k]+=1
  lon,lat=Ti.transform(m[0],m[1])
  res.append(dict(lat=round(lat,6),lon=round(lon,6),d=round(d),az=round(az,1),deg=m[2],nat=m[4],ouvert=round(np.mean(op),2),foret=round(np.mean(fo),2),bati=round(db),eau=round(dw),n_ouvert40=n_open,vis_ouvert=vis_open,**v))
json.dump(res,open('axe_loup.json','w'))
for e in sorted(res,key=lambda e:e['d']): print(e)
