# T18 : séries numérotées réelles autour de la tour d'Avalon, test « 3e–11e à 1850 ± 18 m »
import sys, re, json, itertools, random
sys.path.insert(0,'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12')
from geo12 import hav, TA
import xml.etree.ElementTree as ET
T, TOL = 1850, 18
K='{http://www.opengis.net/kml/2.2}'
def ok(d): return abs(d-T)<=TOL
S={}   # nom -> {numéro: [ (lat,lon), ...]}
# 1) KMZ « bornes 1822/1823 » (sentier-nature.com)
root=ET.parse('t18_bornes.kml').getroot(); kml={}
for pm in root.iter(K+'Placemark'):
    nm=(pm.findtext(K+'name') or '').strip(); c=pm.findtext('.//'+K+'coordinates')
    m=re.fullmatch(r'B(\d+)(?:\s.*)?',nm)
    if m and c and ',' in c and len(c.split())==1:
        lo,la=map(float,c.strip().split(',')[:2]); kml.setdefault(int(m.group(1)),[]).append((la,lo))
S['KMZ bornes frontière 1822 (sentier-nature)']=kml
# 2) OSM boundary_stone numérotées (rayon 15 km)
d=json.load(open('t18_boundary.json')); osm={}
for e in d['elements']:
    t=e['tags']; r=t.get('ref') or (t.get('name') if t.get('name','').isdigit() else None)
    if r and r.isdigit(): osm.setdefault(int(r),[]).append((e['lat'],e['lon']))
S['OSM boundary_stone numérotées']=osm
# KMZ ∪ OSM
u={k:list(v) for k,v in kml.items()}
for k,v in osm.items(): u.setdefault(k,[]).extend(v)
S['Union KMZ+OSM bornes (numéros mélangés: séries partiellement différentes)']=u
# 3) pylônes RTE, hydrants (OSM, 3 km), avec coordonnées
d=json.load(open('t18_ref3km_xy.json')); pyl={}; hyd={}
for e in d['elements']:
    t=e.get('tags',{}); r=t.get('ref','')
    if not r.isdigit(): continue
    if t.get('power') in('tower','pole'): pyl.setdefault(int(r),[]).append((e['lat'],e['lon']))
    if t.get('emergency')=='fire_hydrant': hyd.setdefault(int(r),[]).append((e['lat'],e['lon']))
S['Pylônes RTE (OSM ref, 3 km)']=pyl; S['Poteaux incendie (OSM ref, 3 km)']=hyd
rnd=random.Random(1)
def report(name,ser):
    ks=sorted(ser); n=sum(len(v) for v in ser.values())
    print(f"\n=== {name}\n  effectif: {len(ks)} numéros distincts ({n} points), de {ks[0]} à {ks[-1]}")
    for lst in (3,11): print(f"  n°{lst}:", ser.get(lst,'ABSENT'))
    if 3 in ser and 11 in ser:
        for a in ser[3]:
            for b in ser[11]:
                dd=hav(a,b); print(f"  >>> 3e–11e : {dd:.0f} m  ({'DANS' if ok(dd) else 'hors'} 1850±18) | 3e à {hav(TA,a):.0f} m de la tour, 11e à {hav(TA,b):.0f} m")
    # contrôle (i,i+8)
    p8=[(i,hav(a,b)) for i in ks if i+8 in ser for a in ser[i] for b in ser[i+8]]
    h8=[(i,round(x)) for i,x in p8 if ok(x)]
    print(f"  paires (i,i+8): {len(p8)} ; dans 1850±18: {h8}")
    # toutes paires i<j
    allp=[(i,j,hav(a,b)) for i,j in itertools.combinations(ks,2) for a in ser[i] for b in ser[j]]
    hits=[(i,j,round(x)) for i,j,x in allp if ok(x)]
    print(f"  toutes paires: {len(allp)} ; dans 1850±18: {len(hits)} ({100*len(hits)/max(1,len(allp)):.2f} %) {hits[:8]}")
    return len(allp),len(hits)
for k,v in S.items(): report(k,v)
# bornes 1822 : 3 et 11 sont très loin de la tour (série numérotée depuis le sud-ouest, hors Chartreuse pour 1-6)
print("\n=== Bornes 1822 — géographie de la série")
for i in (5,6,10,14,22,35,44):
    if i in kml: print(f"  B{i:02d} {kml[i][0]}  à {hav(TA,kml[i][0])/1000:.1f} km de la tour")
print("  distance B05–B10 = %.1f km ; B06–B10 = %.1f km ; B10–B14 = %.1f km"%tuple(hav(kml[a][0],kml[b][0])/1000 for a,b in((5,10),(6,10),(10,14))))
print("  => 3e et 11e de cette série (3 en Ain/Isère sud Pont-de-Beauvoisin, 11 près de St-Pierre-d'Entremont) sont à >20 km l'une de l'autre, pas à 1,85 km.")
# bornes proches de la tour
near=[(round(hav(TA,p)),i) for i,v in {**kml,**osm}.items() for p in v]; near.sort(); print("  bornes numérotées les plus proches de la tour (m, n°):",near[:6])
# 4) Randonnée des Hameaux : 4 points numérotés sur la carte du topo
print("\n=== Randonnée des Hameaux : topo Isère Outdoor = 4 pastilles numérotées (1-4) ; GPX 310 trkpt, 0 waypoint ; nœuds OSM = noms sans numéro => pas de 11e.")
# 5) Golf
print("=== Golfs ≤15 km (OSM): Porte-de-Savoie 8,1 km, Granier-Apremont 11,1 km ; aucun golf=hole/tee/green dans OSM (requête vide).")
# Taux de faux positifs : N nœuds aléatoires dans la zone, séries de 11+ points => P(|d-1850|<=18) pour une paire donnée
import math
R=3000; hits=0; N=200000
for _ in range(N):
    def pt():
        while True:
            x,y=rnd.uniform(-R,R),rnd.uniform(-R,R)
            if x*x+y*y<=R*R: return x,y
    a,b=pt(),pt(); hits+= abs(math.hypot(a[0]-b[0],a[1]-b[1])-T)<=TOL
print(f"\n=== Témoin : 2 points aléatoires dans un disque de 3 km : P(d=1850±18) = {100*hits/N:.2f} % (=> une paire (3,11) donnée sur un jeu de 3 km tombe par hasard ~ ce taux)")
