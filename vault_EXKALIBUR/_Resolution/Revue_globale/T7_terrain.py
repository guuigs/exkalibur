# T7 : inventaire terrain IGN (ruisseaux, intersections de sentiers, roches) dans 5 km + corridor Bayard->Avalon
# Sortie : T7_terrain.json (schéma imposé par l'orchestrateur). Sources : BD TOPO v3 (GeoJSON en cache), cadastre Etalab (T4).
import json, math, re
from collections import defaultdict
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py', encoding='utf-8').read())
W = r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
OUT = r'C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/'

# Coordonnées exactes (toponymes BD TOPO, pas les 45.4931,6.1497 de la tâche qui sont erronés)
TOUR = (45.4288723, 6.03101275)   # "tour d'avallon" (toponymie_12km)
BAYARD = (45.42337066, 6.0189374) # "château bayard" (toponymie_12km)

def compass16(b):
    dd = ["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSO","SO","OSO","O","ONO","NO","NNO"]
    return dd[int(((b % 360) + 11.25) // 22.5) % 16]
def axis_compass(a):
    pairs = {0:"N–S",22.5:"NNE–SSO",45:"NE–SO",67.5:"ENE–OSO",90:"E–O",112.5:"ESE–ONO",135:"SE–NO",157.5:"SSE–NNO"}
    return pairs.get(round(a/22.5)*22.5 % 180, "E–O")

h = load('troncon_hydrographique_12km'); c = load('cours_d_eau')
cdeau = {f['properties']['cleabs']: f['properties'].get('toponyme') for f in c}
named = defaultdict(list); unnamed = []
for f in h:
    p = f['properties']
    if p['nature'] != 'Ecoulement naturel': continue
    lk = p.get('liens_vers_cours_d_eau'); nm = cdeau.get(lk) if lk else None
    (named[nm] if nm else unnamed).append(f)

def flow(fs):
    ini = {}; fin = {}
    for f in fs:
        for L in ([f['geometry']['coordinates']] if f['geometry']['type']=='LineString' else f['geometry']['coordinates']):
            a = (L[0][1], L[0][0]); b = (L[-1][1], L[-1][0])
            ini[(round(a[0],6),round(a[1],6))] = a; fin[(round(b[0],6),round(b[1],6))] = b
    srcs = [v for k,v in ini.items() if k not in fin]; mths = [v for k,v in fin.items() if k not in ini]
    if not srcs or not mths: return None
    best = None
    for s in srcs:
        for m in mths:
            d = hav(s, m)
            if best is None or d > best[0]: best = (d, s, m)
    return brg(best[1], best[2])

streams = []
for nm, fs in named.items():
    pts = [(q[1],q[0]) for f in fs for L in ([f['geometry']['coordinates']] if f['geometry']['type']=='LineString' else f['geometry']['coordinates']) for q in L]
    d = min(hav(p, TOUR) for p in pts)
    if d > 5: continue
    near = min(pts, key=lambda p: hav(p, TOUR)); db = min(hav(p, BAYARD) for p in pts)
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    mx = sum(xs)/len(xs); my = sum(ys)/len(ys)
    sxx = sum((x-mx)**2 for x in xs); syy = sum((y-my)**2 for y in ys); sxy = sum((x-mx)*(y-my) for x,y in pts)
    axis = (math.degrees(0.5*math.atan2(2*sxy, sxx-syy))) % 180
    streams.append((nm, near, d, db, axis, flow(fs)))
streams.sort(key=lambda r: r[2])

ruisseaux = []
for nm, near, d, db, axis, fl in streams:
    ruisseaux.append(dict(nom=nm, position="%.5f, %.5f"%(near[0],near[1]),
        cap_general="%s ; coule %s"%(axis_compass(axis), compass16(fl) if fl is not None else "?"),
        dist_tour="%.2f km"%d,
        source="IGN BD TOPO (cours_d_eau, statut Validé) ; dist château Bayard %.2f km ; identifiable: oui"%db))
for f in unnamed:  # 4 sans nom à <=1 km
    Ls = [f['geometry']['coordinates']] if f['geometry']['type']=='LineString' else f['geometry']['coordinates']
    pts = [(q[1],q[0]) for L in Ls for q in L]
    d = min(hav(q, TOUR) for q in pts)
    if d <= 1:
        near = min(pts, key=lambda q: hav(q, TOUR)); db = min(hav(q, BAYARD) for q in pts)
        ruisseaux.append(dict(nom="(sans nom)", position="%.5f, %.5f"%(near[0],near[1]),
            cap_general="coule %s"%compass16(brg(pts[0],pts[-1])), dist_tour="%.2f km"%d,
            source="IGN BD TOPO (tronçon Ecoulement naturel sans toponyme) ; dist château Bayard %.2f km ; identifiable: non"%db))
ruisseaux.sort(key=lambda r: float(r['dist_tour'].split()[0]))

# Intersections : liste T1 filtrée (deg>=4 = croisement de 2+ sentiers, pas les fourches deg=3)
tj = json.load(open(OUT+'T1_tour_jonctions.json', encoding='utf-8'))
cross = [r for r in tj if r['deg'] >= 4]
# (natures exactes déjà recalculées et sauvées dans t7_crossings.json)
json.dump(dict(ruisseaux=ruisseaux), open(W+'t7_final_streams.json','w'), ensure_ascii=False, indent=1)
print('OK :', len(ruisseaux), 'ruisseaux ;', len(cross), 'croisements (voir T7_terrain.json final)')
