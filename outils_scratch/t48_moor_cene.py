exec(open('t45_cene_rangee.py').read().split("starts={")[0])
Vs=np.unpackbits(np.load('vs_sommet.npy'))[:N*N].reshape(N,N).astype(bool)
src=np.array([shape(f['geometry']).coords[0][:2] for f in json.load(open('wfs_detail_hydrographique.json'))['features'] if f['properties'].get('nature')=='Source'])
AZ=95.78;step=1850/8
for sn,(slo,sla) in {'pied':(6.03115,45.42887),'sommet':(6.03101275,45.4288723)}.items():
  print(f'===== départ {sn} = place 7 (Jésus) ; axe Machrie Moor {AZ}°')
  for k in range(1,14):
    off=(k-7)*step
    if off==0: continue
    az=AZ if off>0 else (AZ+180)%360
    lo,la,_=G.fwd(slo,sla,az,abs(off));x,y=T.transform(lo,la)
    R,C=int(YN-y),int(x-X0)
    vs=int(Vs[R-80:R+81,C-80:C+81].sum()) if X0+100<x<X0+6900 else -1
    s=info(lo,la,f'place {k:2d} ({off:+.0f} m)').split('\n')
    print('  ',s[0],f'| vu sommet r80 {vs} | public {PUB.distance(Point(x,y)):.0f} m | source {np.min(np.hypot(src[:,0]-x,src[:,1]-y)):.0f} m')
    if k in (3,11,13): print('     ',s[1].strip());print('     ',s[2].strip())
