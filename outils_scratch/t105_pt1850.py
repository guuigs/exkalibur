import json,gzip,math,numpy as np
from shapely.geometry import shape,Point
exec(open('ring1068.py').read().split('out=[]')[0])
TX,TY=936955.34,6485599.51;tlo,tla=Ti.transform(TX,TY)
az=126.3506
def pt(d): lo,la=G.fwd(tlo,tla,az,d)[:2];return T.transform(lo,la),(la,lo)
for d in (1850,925,3700):
  (x,y),(la,lo)=pt(d);print(d,'m ->',round(la,5),round(lo,5))
(x,y),_=pt(1850);P=Point(x,y)
def near(f,key,R=250):
  for ft in json.load(open(f))['features']:
    g=shape(ft['geometry']);dd=g.distance(P)
    if dd<=R:
      p=ft['properties'];print('  ',f.split('_',1)[1][:18],int(dd),'m',{k:p[k] for k in p if k in ('nature','toponyme','graphie_du_toponyme','nature_de_l_objet','usage_1')})
for f in ['wfs_toponymie.json','wfs_construction_ponctuelle.json','wfs_detail_orographique.json','wfs_lieu_dit_non_habite.json','wfs_detail_hydrographique.json']: near(f,None)
import collections
for ft in json.load(open('wfs_batiment.json'))['features']:
  g=shape(ft['geometry'])
  if g.distance(P)<=250 and ft['properties']['nature']!='Indifférenciée': print('  bat',int(g.distance(P)),ft['properties']['nature'])
