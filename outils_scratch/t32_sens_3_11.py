import json,math,numpy as np
exec(open('ring1068.py').read().split('out=[]')[0])
hyd=json.load(open('wfs_troncon_hydrographique.json'))['features']
HS=[(np.array([c[:2] for c in f['geometry']['coordinates']]),f['properties'].get('cpx_toponyme_de_cours_d_eau')) for f in hyd if f['geometry']['type']=='LineString']
L=json.load(open('wfs_lieu_dit_non_habite.json'))['features']+json.load(open('wfs_toponymie.json'))['features']
def topo(x,y):
  b=[]
  for f in L:
    c=f['geometry']['coordinates']
    while isinstance(c[0],list): c=c[0]
    p=f['properties'];b.append((math.hypot(c[0]-x,c[1]-y),p.get('toponyme') or p.get('graphie_du_toponyme')))
  return min(b)
starts={'sommet tour':(45.4288723,6.03101275,33.0),'pied tour':(45.42887,6.03115,1.7),'Rue du Rempart':(45.42977,6.03118,1.7)}
def info(x,y,obsxy):
  op=np.mean([z(mnh,x+a,y+b)<2 for a in range(-30,31,3) for b in range(-30,31,3) if math.hypot(a,b)<=30])
  ring=np.mean([z(mnh,x+a,y+b)>5 for a in range(-120,121,6) for b in range(-120,121,6) if 60<=math.hypot(a,b)<=120])
  db=float(np.min(np.hypot(B[:,0]-x,B[:,1]-y)))
  w=min(((float(np.min(np.hypot(s[:,0]-x,s[:,1]-y))),n) for s,n in HS),key=lambda t:t[0])
  X,Y,Z0=obsxy
  return op,ring,db,w,los(X,Y,Z0,x,y,False),los(X,Y,Z0,x,y,True)
for az in (95.78,275.78):
  print('\n######## cap',az)
  for nm,(la,lo,eh) in starts.items():
    X,Y=T.transform(lo,la);Z0=z(mnt,X,Y)+eh
    tl,ta,_=G.fwd(lo,la,az,1850);tx,ty=T.transform(tl,ta)
    op,ring,db,w,rl,ra=info(tx,ty,(X,Y,Z0))
    js=sorted(M,key=lambda m:math.hypot(m[0]-tx,m[1]-ty))[:2]
    t=topo(tx,ty)
    print(f'{nm}: cible {ta:.6f},{tl:.6f} | lieu-dit {t[1]} ({t[0]:.0f} m) | ouvert {op:.2f} forêt autour {ring:.2f} | maisons {db:.0f} m | eau {w[0]:.0f} m {w[1]} | vue relief {rl:+.1f} arbres {ra:+.1f}')
    for m in js:
      jl=Ti.transform(m[0],m[1]);print(f'    croisement à {math.hypot(m[0]-tx,m[1]-ty):.0f} m : {jl[1]:.6f},{jl[0]:.6f} ({m[2]} branches) {m[4][:3]}')
