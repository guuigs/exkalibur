import json
from shapely.geometry import shape,Point
from shapely.strtree import STRtree
d=json.load(open('38426-parcelles.json'));own=json.load(open('pm_38426.json'))
G=[shape(f['geometry']) for f in d['features']];ids=[f['properties']['id'] for f in d['features']]
tree=STRtree(G)
PUB=('4 - Commune','1 -','2 -','3 -','5 -')
def cls(pid):
  o=own.get(pid)
  if not o: return 'particulier'
  g,n,c=o
  if g.startswith(('1','2','3','4')) or 'SYND' in n or 'COMMUNAUTE' in n: return 'PUBLIC : '+n
  return 'personne morale privée : '+n
pts={'Croisement du Mouret':(45.422426,6.040299),'Place de Simon':(45.42208,6.04066),'Source 1':(45.421767,6.040189),'Source 2':(45.421003,6.039873),
 'Pré visible (centre)':(45.4232,6.0385),'Affleurement 45.423998,6.042453':(45.423998,6.042453),'Affleurement 45.423874,6.042977':(45.423874,6.042977),
 'Affleurement 45.423544,6.04383':(45.423544,6.04383),'Affleurement 45.423402,6.044154':(45.423402,6.044154),'Affleurement 45.422775,6.044514':(45.422775,6.044514),
 'Affleurement 45.42252,6.044485':(45.42252,6.044485),'Affleurement 45.421319,6.045054':(45.421319,6.045054),
 'J5 (loup)':(45.42696,6.05477),'Muraillat J2':(45.432042,6.043877),'Muraillat K':(45.433594,6.044901)}
for k,(la,lo) in pts.items():
  p=Point(lo,la);hit=[i for i in tree.query(p) if G[i].contains(p)]
  if not hit:
    near=min(range(len(G)),key=lambda i:G[i].distance(p)) if False else None
    print(f'{k:35s} : NON CADASTRÉ (domaine public : chemin, ruisseau…)')
  else:
    i=hit[0];print(f'{k:35s} : parcelle {ids[i]} ({d["features"][i]["properties"]["contenance"]} m²) -> {cls(ids[i])}')
