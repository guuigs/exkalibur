"""Critères par étape (FAQ) :
 - jonction : croisement de chemins/sentiers au sens premier (degré >= 3, au moins 2 tronçons Chemin/Sentier/Route empierrée) ;
 - visible depuis le sommet de la tour (FAQ05-155 + 05-165) -> testé ensuite par visib.py ;
 - clairière restée clairière (03-274) : bois à <= 80 m (lisière ou trouée) ;
 - coffre 'tout près' (05-051) et loin de tout bâtiment (05-107) : distance au bâtiment le plus proche, seuil 80 m ;
 - PAS de contrainte de ruisseau cartographié (06-060 : 'il faudra vous rendre sur place'), seulement noté.
Anneau : 1 850 m ± 60 m autour de la tour (incertitude du départ + 1 %)."""
import json, math, sys
import numpy as np
from scipy.spatial import cKDTree as KD
LAT0, LON0 = 45.429083, 6.030808
KX = math.cos(math.radians(LAT0))*111320.0; KY = 111132.0
xy = lambda lon,lat: ((lon-LON0)*KX, (lat-LAT0)*KY)
ll = lambda x,y: (LAT0+y/KY, LON0+x/KX)
lines = lambda g: [g['coordinates']] if g['type']=='LineString' else (g['coordinates'] if g['type']=='MultiLineString' else [])
polys = lambda g: [g['coordinates'][0]] if g['type']=='Polygon' else ([p[0] for p in g['coordinates']] if g['type']=='MultiPolygon' else [])
deg, kind = {}, {}
for f in json.load(open('troncon_de_route.json')):
    n = f['properties']['nature']
    for l in lines(f['geometry']):
        for p in (l[0], l[-1]):
            q = xy(p[0],p[1]); k = (round(q[0]/2), round(q[1]/2))
            deg[k] = deg.get(k,0)+1; kind.setdefault(k,[]).append(n)
J = [((k[0]*2,k[1]*2), kind[k]) for k,v in deg.items() if v>=3 and sum(n in ('Chemin','Sentier','Route empierrée') for n in kind[k])>=2]
def dens(P, step):
    out=[]
    for a,b in zip(P,P[1:]):
        n=max(1,int(np.hypot(*(b-a))/step)); out += [a+(b-a)*t/n for t in range(n+1)]
    return out
S=[]
for f in json.load(open('troncon_hydrographique.json')):
    for l in lines(f['geometry']): S += dens(np.array([xy(p[0],p[1]) for p in l]),10)
FO=[]
for f in json.load(open('zone_de_vegetation.json')):
    if f['properties'].get('nature') in ('Bois','Forêt fermée de feuillus','Forêt fermée mixte','Forêt fermée de conifères','Forêt ouverte','Lande ligneuse'):
        for r in polys(f['geometry']): FO += dens(np.array([xy(p[0],p[1]) for p in r]),15)
B=[np.array([xy(p[0],p[1]) for p in r]).mean(0) for f in json.load(open('batiment.json')) for r in polys(f['geometry'])]
tS,tF,tB = KD(np.array(S)),KD(np.array(FO)),KD(np.array(B))
rows=[]
for (p,kinds) in J:
    p=np.array(p,float); d=math.hypot(*p)
    if abs(d-1850)>60: continue
    ds,_=tS.query(p); df,_=tF.query(p); db,_=tB.query(p)
    az=(math.degrees(math.atan2(p[0],p[1]))+360)%360
    rows.append(dict(lat=ll(*p)[0],lon=ll(*p)[1],d=d,az=az,d_ruis=ds,d_bois=df,d_bat=db,kinds=kinds))
rows.sort(key=lambda r:r['az'])
for r in rows:
    flag = ('OK' if r['d_bois']<=80 and r['d_bat']>=80 else '--')
    print('%s az %5.1f d %4.0f m  %.5f %.5f  bois %4.0f  bât %4.0f  ruisseau BDT %4.0f  %s'%(flag,r['az'],r['d'],r['lat'],r['lon'],r['d_bois'],r['d_bat'],r['d_ruis'],'/'.join(sorted(set(r['kinds'])))))
json.dump(rows,open('jonctions_anneau.json','w'))
json.dump([('j az%.0f d%.0f'%(r['az'],r['d']),r['lat'],r['lon']) for r in rows if r['d_bois']<=80 and r['d_bat']>=80],open('targets3.json','w'))
