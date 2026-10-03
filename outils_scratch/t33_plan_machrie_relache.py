exec(open('mm_plan.py').read().split("cand=[r")[0])
out=[];seen=set()
for r in rows:
  key=(round(r[9]/40),round(r[10]/40))
  if key in seen: continue
  seen.add(key)
  n,vs,vp=visopen(r[9],r[10],100)
  if vs+vp==0: continue
  ring=np.mean([z(mnh,r[9]+a,r[10]+b)>5 for a in range(-120,121,8) for b in range(-120,121,8) if 60<=math.hypot(a,b)<=120])
  out.append(r[:9]+[n,int(vs),int(vp),round(float(ring),2)])
print('placements avec au moins une zone ouverte visible à <=100 m :',len(out))
for r in sorted(out,key=lambda r:-(r[10]+r[11]))[:25]: print(r)
