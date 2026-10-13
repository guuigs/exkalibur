"""Jonctions de chemins (BD TOPO + OSM) à 200-1600 m de la tour, bois <= 80 m, bâtiments >= 80 m. Sortie : cibles pour visib.py."""
import json, math, sys
import numpy as np
from collections import defaultdict
from scipy.spatial import cKDTree as KD
sys.path.insert(0,'.')
LAT0, LON0 = 45.429083, 6.030808
KX = math.cos(math.radians(LAT0))*111320.0; KY = 111132.0
xy = lambda lon,lat: ((lon-LON0)*KX, (lat-LAT0)*KY); ll = lambda x,y: (LAT0+y/KY, LON0+x/KX)
lines = lambda g: [g['coordinates']] if g['type']=='LineString' else (g['coordinates'] if g['type']=='MultiLineString' else [])
polys = lambda g: [g['coordinates'][0]] if g['type']=='Polygon' else ([p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [])
J = []
deg, kind = {}, {}
for f in json.load(open('troncon_de_route.json')):
    n = f['properties']['nature']
    for l in lines(f['geometry']):
        for p in (l[0], l[-1]):
            q = xy(p[0],p[1]); k=(round(q[0]/2),round(q[1]/2)); deg[k]=deg.get(k,0)+1; kind.setdefault(k,[]).append(n)
J += [((k[0]*2,k[1]*2),'BDT:'+'/'.join(sorted(set(kind[k])))) for k,v in deg.items() if v>=3 and sum(n in ('Chemin','Sentier','Route empierrée') for n in kind[k])>=2]
cnt = defaultdict(int); kinds = defaultdict(set)
for e in json.load(open('osm.json'))['elements']:
    t = e.get('tags',{})
    if e['type']=='way' and t.get('highway') in ('path','track','footway','bridleway','unclassified','service'):
        g = e['geometry']
        for i,p in enumerate(g):
            k=(round(p['lat'],6),round(p['lon'],6)); cnt[k]+= (1 if i in (0,len(g)-1) else 2); kinds[k].add(t['highway'])
J += [(xy(k[1],k[0]),'OSM:'+'/'.join(sorted(kinds[k]))) for k,v in cnt.items() if v>=3 and len(kinds[k]&{'path','track','footway','bridleway'})>=1]
def dens(P, step):
    out=[]
    for a,b in zip(P,P[1:]):
        n=max(1,int(np.hypot(*(b-a))/step)); out += [a+(b-a)*t/n for t in range(n+1)]
    return out
FO=[]
for f in json.load(open('zone_de_vegetation.json')):
    if f['properties'].get('nature') in ('Bois','Forêt fermée de feuillus','Forêt fermée mixte','Forêt fermée de conifères','Forêt ouverte','Lande ligneuse'):
        for r in polys(f['geometry']): FO += dens(np.array([xy(p[0],p[1]) for p in r]),15)
S=[]
for f in json.load(open('troncon_hydrographique.json')):
    for l in lines(f['geometry']): S += dens(np.array([xy(p[0],p[1]) for p in l]),10)
for e in json.load(open('osm.json'))['elements']:
    if e['type']=='way' and e.get('tags',{}).get('waterway') in ('stream','river','drain','canal'):
        S += dens(np.array([xy(p['lon'],p['lat']) for p in e['geometry']]),10)
B=[np.array([xy(p[0],p[1]) for p in r]).mean(0) for f in json.load(open('batiment.json')) for r in polys(f['geometry'])]
tF,tB,tS = KD(np.array(FO)),KD(np.array(B)),KD(np.array(S))
rows=[]; seen=[]
for p,src in J:
    p=np.array(p,float); d=math.hypot(*p)
    if not (200<=d<=1600): continue
    if any(math.hypot(*(p-q))<15 for q in seen): continue
    seen.append(p)
    df,_=tF.query(p); db,_=tB.query(p); ds,_=tS.query(p)
    if df<=80 and db>=80:
        az=(math.degrees(math.atan2(p[0],p[1]))+360)%360
        rows.append(('p az%.0f d%.0f %s ruis%.0f bat%.0f'%(az,d,src,ds,db),*ll(*p)))
rows.sort(key=lambda r:r[0])
print(len(rows)); json.dump(rows,open('targets_proches.json','w'))
