# -*- coding: utf-8 -*-
"""T15 : croix/calvaires/oratoires <=6 km de la tour d'Avalon ; paires a 1850+-18 m ; taux attendu par hasard."""
import sys, json, re, math, random, itertools
sys.path.insert(0,'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12')
from geo12 import *
import numpy as np
RMAX=6000; D=1850; TOL=18
pts={}   # cle -> dict
# 1) BD TOPO IGN (construction_ponctuelle_12km) : nature Croix (+Oratoire/Vierge)
d=json.load(open(S+'ign/construction_ponctuelle_12km.geojson',encoding='utf-8'))
for f in d['features']:
    p=f['properties']
    if p.get('nature')!='Croix': continue
    lon,lat=f['geometry']['coordinates'][:2]
    pts['IGN:'+p['cleabs']]=dict(src='BDTOPO',lat=lat,lon=lon,kind=p.get('nature_detaillee') or 'Croix',name=p.get('toponyme'))
# 2) OSM (Overpass) : croix, wayside_shrine
for e in json.load(open(S+'exk_e12/t15_osm_raw.json',encoding='utf-8')):
    t=e['tags']
    if t.get('historic') in ('wayside_cross','wayside_shrine') or t.get('man_made')=='cross':
        la=e.get('lat') or e['center']['lat']; lo=e.get('lon') or e['center']['lon']
        pts[f"OSM:{e['type']}{e['id']}"]=dict(src='OSM',lat=la,lon=lo,kind=t.get('historic') or 'cross',name=t.get('name'))
# 3) lavieduvillage.fr (coordonnees relevees sur les fiches, voir rapport)
lvv={'LVV38:2380128':(45.479527,5.971419),'LVV38:2380129':(45.469093,5.98124),'LVV38:2380130':(45.46843,5.98934),
     'LVV38:2380131':(45.467995,5.966299),'LVV38:2380132':(45.465294,5.986202),'LVV38:2380133':(45.459064,5.967271),
     'LVV38:2380490':(45.420792,6.012769)}
for k,(la,lo) in lvv.items(): pts[k]=dict(src='LVV',lat=la,lon=lo,kind='Calvaire?/Croix',name=None)
# dedoublonnage : points a < 25 m = meme objet (on garde le 1er)
keys=sorted(pts,key=lambda k:(pts[k]['src']!='BDTOPO',k)); kept=[]
for k in keys:
    p=pts[k]
    if hav(TA,(p['lat'],p['lon']))>RMAX: continue
    if any(hav((p['lat'],p['lon']),(q['lat'],q['lon']))<25 for q in kept): continue
    p['id']=k; p['dist_TA']=hav(TA,(p['lat'],p['lon'])); kept.append(p)
print(f"Objets bruts: {len(pts)} ; uniques <=6 km (dedoublonnes a 25 m): {len(kept)}")
import collections
print(collections.Counter(p['src'] for p in kept), collections.Counter(p['kind'] for p in kept))
# paires
res=[]
for a,b in itertools.combinations(kept,2):
    dd=hav((a['lat'],a['lon']),(b['lat'],b['lon']))
    if abs(dd-D)<=TOL: res.append((dd,a,b))
res.sort(key=lambda x:abs(x[0]-D))
print(f"\nPAIRES a {D}+-{TOL} m : {len(res)} sur {len(kept)*(len(kept)-1)//2} paires")
for dd,a,b in res:
    print(f"  {dd:7.1f} m  {a['id']} ({a['kind']},{a['lat']:.6f},{a['lon']:.6f}, TA {a['dist_TA']:.0f} m)  <->  {b['id']} ({b['kind']},{b['lat']:.6f},{b['lon']:.6f}, TA {b['dist_TA']:.0f} m)")
# controle aleatoire : n points uniformes dans le disque 6 km (meme n), 20000 tirages
n=len(kept); rng=np.random.default_rng(15); obs=len(res)
cnt=[]
for _ in range(20000):
    r=RMAX*np.sqrt(rng.random(n)); th=2*np.pi*rng.random(n)
    x=r*np.cos(th); y=r*np.sin(th)
    dm=np.hypot(x[:,None]-x[None,:],y[:,None]-y[None,:])
    iu=np.triu_indices(n,1); dv=dm[iu]
    cnt.append(int(np.sum(np.abs(dv-D)<=TOL)))
cnt=np.array(cnt)
print(f"\nCONTROLE (n={n} points uniformes/disque 6 km, 20000 tirages) : nb paires a 1850+-18 : moyenne {cnt.mean():.2f}, mediane {np.median(cnt):.0f}, P(>=1)={np.mean(cnt>=1):.3f}, P(>={obs})={np.mean(cnt>=obs):.3f}, max={cnt.max()}")
# controle en conservant les positions reelles mais en decalant/pivotant aleatoirement tout le semis (rotation autour de TA ne change pas les distances) -> inutile ; remplace par jitter
# Taux analytique par paire
iu=np.triu_indices(n,1)
xs=np.array([xy(p['lon'],p['lat']) for p in kept]); dm=np.hypot(xs[:,None,0]-xs[None,:,0],xs[:,None,1]-xs[None,:,1])[iu]
print(f"Distribution observee des distances inter-croix : <=6 km: part dans [1832,1868] = {np.mean(np.abs(dm-D)<=TOL):.4f}")
# Chemins de croix numerotes : aucune station numerotee dans le semis
print("\nTotal 'chemin de croix' numerote retrouve dans 6 km : voir rapport (aucun).")
json.dump(dict(kept=kept,pairs=[(dd,a['id'],b['id']) for dd,a,b in res]),open(S+'exk_e12/t15_candidates.json','w'),ensure_ascii=False,indent=1)
