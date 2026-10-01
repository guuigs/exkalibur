# -*- coding: utf-8 -*-
"""T15 : hypothèse « 3e et 11e ponts/passerelles/gués le long d'un même cours d'eau », 10 stades = 1850 m ±18 m.

Entrées : ign/troncon_hydrographique_12km, construction_lineaire_12km, construction_surfacique_12km,
          ign/troncon_de_route (6 km), exk_e12/ov_bridges_waterways_7km.json (cours d'eau + ponts OSM),
          exk_e12/ov_fords_3km.json (gués OSM, récupérés par T15_fetch.py).
Sortie : stdout (-> T15_ponts.out.txt).
"""
import sys, json, math, heapq, random, collections, itertools
sys.path.insert(0, 'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12')
from geo12 import *
from shapely.geometry import LineString, MultiLineString, Point
from shapely.ops import unary_union

random.seed(1524)
TX, TY = xy(TA[1], TA[0])
TOL, TARGET = 18.0, 1850.0
DEDUP = 15.0
ZONE = 6000.0           # rayon d'étude autour de la tour
TOWER_NEAR = 1500.0
OV = S + 'exk_e12/'

def dtower_xy(x, y): return math.hypot(x - TX, y - TY)
def hav_xy(a, b): return hav(inv(*a), inv(*b))

# ------------------------------------------------------------------ 1. lignes de cours d'eau
def build_line(segs, snap=6.0, gap=60.0):
    """segs: liste de listes de (x,y). Renvoie (LineString plus long chemin dans la plus grande composante, info)
    Les segments sont raccordés par extrémités (snap ≤ 6 m) puis les composantes séparées par un trou ≤ gap (60 m,
    buses/ponts sous route) sont reliées par un segment droit. Plus long chemin = double balayage de Dijkstra."""
    # noeuds: union-find sur extrémités
    pts = []
    for s in segs:
        pts.append(s[0]); pts.append(s[-1])
    parent = list(range(len(pts)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    # grille pour accélérer
    grid = collections.defaultdict(list)
    for i, p in enumerate(pts):
        grid[(int(p[0] // snap), int(p[1] // snap))].append(i)
    for i, p in enumerate(pts):
        cx, cy = int(p[0] // snap), int(p[1] // snap)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for j in grid.get((cx + dx, cy + dy), []):
                    if j > i and math.hypot(p[0] - pts[j][0], p[1] - pts[j][1]) <= snap:
                        parent[find(i)] = find(j)
    node = [find(i) for i in range(len(pts))]
    edges = []   # (u, v, coords)
    for k, s in enumerate(segs):
        u, v = node[2 * k], node[2 * k + 1]
        L = LineString(s).length
        edges.append([u, v, s, L])
    # degrés / extrémités libres
    deg = collections.Counter()
    for u, v, s, L in edges:
        deg[u] += 1; deg[v] += 1
    npos = {}
    for k, s in enumerate(segs):
        npos[node[2 * k]] = s[0]; npos[node[2 * k + 1]] = s[-1]
    # composantes
    adj = collections.defaultdict(list)
    for ei, (u, v, s, L) in enumerate(edges):
        adj[u].append(ei); adj[v].append(ei)
    def comps():
        seen, out = set(), []
        for n0 in adj:
            if n0 in seen: continue
            st, c = [n0], set()
            while st:
                n = st.pop()
                if n in c: continue
                c.add(n)
                for ei in adj[n]:
                    u, v = edges[ei][0], edges[ei][1]
                    st.append(v if u == n else u)
            seen |= c; out.append(c)
        return out
    cs = comps()
    ngap = 0
    if len(cs) > 1:
        # raccord par extrémités: pour toute paire de composantes, plus proches extrémités libres (deg==1) < gap
        ends = [(n, npos[n]) for n in adj if deg[n] == 1]
        compof = {n: i for i, c in enumerate(cs) for n in c}
        cand = []
        for (n1, p1), (n2, p2) in itertools.combinations(ends, 2):
            if compof[n1] != compof[n2]:
                d = math.hypot(p1[0] - p2[0], p1[1] - p2[1])
                if d <= gap: cand.append((d, n1, n2))
        cand.sort()
        par = list(range(len(cs)))
        def f2(i):
            while par[i] != i: par[i] = par[par[i]]; i = par[i]
            return i
        for d, n1, n2 in cand:
            a, b = f2(compof[n1]), f2(compof[n2])
            if a != b:
                par[a] = b
                edges.append([n1, n2, [npos[n1], npos[n2]], d]); ei = len(edges) - 1
                adj[n1].append(ei); adj[n2].append(ei); ngap += 1
        cs = comps()
    # plus grande composante (longueur cumulée)
    def clen(c): return sum(e[3] for e in edges if e[0] in c)
    big = max(cs, key=clen)
    ncomp_other = [round(clen(c)) for c in cs if c is not big]
    def dijk(src):
        dist = {src: 0.0}; prev = {}; pq = [(0.0, src)]
        while pq:
            d, n = heapq.heappop(pq)
            if d > dist[n]: continue
            for ei in adj[n]:
                u, v, s, L = edges[ei]
                m = v if u == n else u
                nd = d + L
                if nd < dist.get(m, 1e18):
                    dist[m] = nd; prev[m] = (n, ei); heapq.heappush(pq, (nd, m))
        return dist, prev
    start = next(iter(big))
    d0, _ = dijk(start); a = max(d0, key=d0.get)
    d1, p1 = dijk(a); b = max(d1, key=d1.get)
    d2, p2 = dijk(b); a = max(d2, key=d2.get)
    dd, pp = d2, p2
    # reconstruit le chemin de a vers b
    path_edges = []; n = a
    while n != b:
        pn, ei = pp[n]; path_edges.append((pn, n, ei)); n = pn
    # pp[n] = (précédent depuis b) : on part de a et on remonte vers b
    coords = []
    for (frm, to, ei) in path_edges:   # frm est plus proche de b ; to est du côté a
        u, v, s, L = edges[ei]
        seg = list(s)
        # orienter de 'to' vers 'frm'
        if u == to and v == frm: pass
        elif v == to and u == frm: seg = seg[::-1]
        else: pass
        if coords and coords[-1] == seg[0]: coords.extend(seg[1:])
        else: coords.extend(seg)
    if len(coords) < 2: return None, None
    line = LineString(coords)
    info = dict(n_seg=len(segs), n_comp=len(comps()), gaps=ngap, long=round(line.length), total=round(sum(e[3] for e in edges)),
                autres=ncomp_other)
    return line, info

def seg_coords(g):
    if g.geom_type == 'LineString': return [list(g.coords)]
    return [list(x.coords) for x in g.geoms]

lines = []   # dict(name, src, line, info)
# BD TOPO
H = load('troncon_hydrographique_12km.geojson')
byname = collections.defaultdict(list)
for g, p in H:
    nm = p.get('cpx_toponyme_de_cours_d_eau')
    if not nm: continue
    for part in seg_coords(g):
        part = [(c[0], c[1]) for c in part]
        if len(part) >= 2:
            if p.get('sens_de_l_ecoulement') == 'Sens inverse': part = part[::-1]
            byname[nm].append(part)
for nm, segs in byname.items():
    ln, info = build_line(segs)
    if ln is None: continue
    if ln.distance(Point(TX, TY)) <= ZONE:
        lines.append(dict(name=nm, src='BDTOPO', line=ln, info=info))
# OSM
osm = json.load(open(OV + 'ov_bridges_waterways_7km.json', encoding='utf-8'))
byo = collections.defaultdict(list)
for e in osm:
    t = e.get('tags', {})
    if t.get('waterway') in ('stream', 'river', 'canal', 'drain', 'ditch') and t.get('name') and 'geometry' in e:
        part = [xy(c['lon'], c['lat']) for c in e['geometry']]
        if len(part) >= 2: byo[t['name']].append(part)
for nm, segs in byo.items():
    ln, info = build_line(segs)
    if ln is None: continue
    if ln.distance(Point(TX, TY)) <= ZONE:
        lines.append(dict(name=nm, src='OSM', line=ln, info=info))
print('== COURS D\'EAU NOMMÉS (ligne reconstruite) à ≤ 6 km de la tour: %d (BDTOPO %d, OSM %d)' % (
    len(lines), sum(1 for l in lines if l['src'] == 'BDTOPO'), sum(1 for l in lines if l['src'] == 'OSM')))

# altitude des extrémités (IGN RGE ALTI) pour étiqueter source / embouchure
ends = []
for l in lines:
    c = l['line'].coords
    l['A'], l['B'] = c[0], c[-1]
    ends += [inv(*c[0]), inv(*c[-1])]
alts = {}
try:
    for i in range(0, len(ends), 100):
        ch = ends[i:i + 100]
        el = alti(ch)
        for p, z in zip(ch, el): alts[(round(p[0], 6), round(p[1], 6))] = z
except Exception as ex:
    print('alti IGN indisponible:', ex)
for l in lines:
    za = alts.get((round(inv(*l['A'])[0], 6), round(inv(*l['A'])[1], 6)))
    zb = alts.get((round(inv(*l['B'])[0], 6), round(inv(*l['B'])[1], 6)))
    l['zA'], l['zB'] = za, zb
    # extrémité haute = source
    if za is not None and zb is not None and za > -900 and zb > -900:
        l['A_is_source'] = za >= zb
    else:
        l['A_is_source'] = True
    l['A_in'] = dtower_xy(*l['A']) <= ZONE - 500    # extrémité bien dans la zone couverte
    l['B_in'] = dtower_xy(*l['B']) <= ZONE - 500

# ------------------------------------------------------------------ 2. franchissements candidats (structures)
ROUTIER_N = {'Route à 1 chaussée', 'Route à 2 chaussées', 'Route empierrée', 'Rond-point', 'Bretelle', 'Type autoroutier'}
roads = load('troncon_de_route.geojson')
road_geoms = [g for g, p in roads]; road_tree = STRtree(road_geoms)
def road_class_nature(n):
    if n in ROUTIER_N: return 'routier'
    if n == 'Chemin': return 'chemin'
    if n == 'Sentier': return 'sentier'
    return 'autre'
def nearest_road_class(geom, r=15.0):
    idx = road_tree.query(geom.buffer(r))
    best = None
    for i in idx:
        d = geom.distance(road_geoms[i])
        if d <= r and (best is None or d < best[0]):
            best = (d, roads[i][1]['nature'])
    return road_class_nature(best[1]) if best else 'autre'

structs = []   # dict(kind, cls, src, geom(x,y repr point), geoms for intersection, label)
for fn in ('construction_lineaire_12km.geojson', 'construction_surfacique_12km.geojson'):
    for g, p in load(fn):
        if p.get('nature') != 'Pont': continue
        if g.distance(Point(TX, TY)) > 7000: continue
        if p.get('nature_detaillee') == 'Passerelle': cls = 'passerelle'
        else: cls = nearest_road_class(g)
        structs.append(dict(kind='BD_pont', cls=cls, src='BDTOPO', geom=g, rep=g.centroid,
                            label='BDTOPO ' + (p.get('nature_detaillee') or 'Pont') + ' ' + p['cleabs'][-8:]))
for e in osm:
    t = e.get('tags', {})
    if 'bridge' not in t or t['bridge'] == 'no' or 'geometry' not in e: continue
    pts = [xy(c['lon'], c['lat']) for c in e['geometry']]
    if len(pts) < 2: continue
    g = LineString(pts)
    hw = t.get('highway')
    if t.get('railway'): cls = 'rail'
    elif hw in ('footway', 'path', 'steps', 'pedestrian', 'bridleway', 'cycleway', 'corridor'): cls = 'sentier'
    elif hw == 'track': cls = 'chemin'
    elif hw: cls = 'routier'
    else: cls = 'autre'
    if cls == 'sentier' and (hw == 'footway' and g.length < 80): cls = 'passerelle'  # courtes passerelles piétonnes OSM
    structs.append(dict(kind='OSM_pont', cls=cls, src='OSM', geom=g, rep=g.centroid if g.length < 80 else None,
                        label='OSM bridge=%s %s way/%d %s' % (t['bridge'], hw or t.get('railway') or '', e['id'], t.get('name', ''))))
sgeoms = [s['geom'] for s in structs]; stree = STRtree(sgeoms)
print('structures pont: BDTOPO=%d OSM=%d  (classes: %s)' % (
    sum(1 for s in structs if s['src'] == 'BDTOPO'), sum(1 for s in structs if s['src'] == 'OSM'),
    dict(collections.Counter(s['cls'] for s in structs))))

# routes position=1 (tabliers) et routes au sol
roads_p1 = [(g, road_class_nature(p['nature']), p) for g, p in roads if p.get('position_par_rapport_au_sol') == '1']
roads_p0 = [(g, road_class_nature(p['nature']), p) for g, p in roads if p.get('position_par_rapport_au_sol') == '0']
p1_tree = STRtree([a[0] for a in roads_p1]); p0_tree = STRtree([a[0] for a in roads_p0])
fords = json.load(open(OV + 'ov_fords_3km.json', encoding='utf-8'))
ford_pts = []
for e in fords:
    if e['type'] == 'node': ford_pts.append((xy(e['lon'], e['lat']), e['id']))

def first_pt(geom):
    if geom.is_empty: return None
    if geom.geom_type == 'Point': return geom
    return geom.centroid

def crossings_for(line, buf):
    """liste de dict(kind, cls, src, pt (x,y), s (abscisse curviligne), label)"""
    out = []
    lb = line.buffer(buf)
    for i in stree.query(lb):
        st = structs[i]
        g = st['geom']
        inter = g.intersection(lb)
        if inter.is_empty: continue
        # pont court: son centre ; long: milieu de la partie qui coupe le cours d'eau
        rep = st['rep'] if st['rep'] is not None and st['rep'].distance(line) <= buf + 25 else first_pt(inter)
        # si le pont est une grande structure (>150 m) qui longe le cours d'eau, ignorer
        if st['geom'].length > 400 and inter.length > 0.6 * st['geom'].length and st['geom'].geom_type == 'LineString':
            pass
        out.append(dict(kind=st['kind'], cls=st['cls'], src=st['src'], pt=(rep.x, rep.y), label=st['label']))
    # routes au niveau position 1 : intersection exacte (buffer petit)
    for i in p1_tree.query(lb):
        g, cls, p = roads_p1[i]
        inter = g.intersection(lb)
        if inter.is_empty: continue
        rep = first_pt(inter)
        out.append(dict(kind='route_p1', cls=cls, src='BDTOPO', pt=(rep.x, rep.y), label='route pos=1 %s %s' % (p['nature'], p['cleabs'][-8:])))
    # gués OSM
    for (pt, fid) in ford_pts:
        if Point(pt).distance(line) <= buf + 10:
            out.append(dict(kind='gue', cls='gue', src='OSM', pt=pt, label='OSM ford node %d' % fid))
    # routes au sol (position 0) coupant le cours d'eau : franchissement 'au sol' (gué/buse/pont non cartographié)
    for i in p0_tree.query(line.buffer(2.0)):
        g, cls, p = roads_p0[i]
        inter = g.intersection(line.buffer(2.0))
        if inter.is_empty: continue
        rep = first_pt(inter)
        out.append(dict(kind='sol', cls='sol_' + cls, src='BDTOPO', pt=(rep.x, rep.y), label='route sol %s %s' % (p['nature'], p['cleabs'][-8:])))
    for c in out:
        c['s'] = line.project(Point(c['pt']))
    return out

PRIO = {'BD_pont': 0, 'OSM_pont': 1, 'route_p1': 2, 'gue': 3, 'sol': 4}
def dedupe(cs, d=DEDUP):
    """fusion à 15 m (distance planaire) ; représentant = type le plus prioritaire (vrai pont) ; ordre par s."""
    cs = sorted(cs, key=lambda c: (PRIO[c['kind']], c['s']))
    reps = []
    for c in cs:
        for r in reps:
            if math.hypot(c['pt'][0] - r['pt'][0], c['pt'][1] - r['pt'][1]) <= d:
                r['members'].append(c); break
        else:
            reps.append(dict(c, members=[c]))
    # une 2e passe (chaînage) : fusionner les représentants à ≤ d
    changed = True
    while changed:
        changed = False
        for a, b in itertools.combinations(range(len(reps)), 2):
            if math.hypot(reps[a]['pt'][0] - reps[b]['pt'][0], reps[a]['pt'][1] - reps[b]['pt'][1]) <= d:
                reps[a]['members'] += reps[b]['members']; del reps[b]; changed = True; break
    for r in reps:
        # s moyen des membres pour l'ordre
        r['s'] = sum(m['s'] for m in r['members']) / len(r['members'])
    return sorted(reps, key=lambda r: r['s'])

VARIANTS = {   # nom -> prédicat sur c['cls'] / kind
    'TOUS_PONTS':        lambda c: c['kind'] in ('BD_pont', 'OSM_pont', 'route_p1'),
    'TOUS+GUES':         lambda c: c['kind'] in ('BD_pont', 'OSM_pont', 'route_p1', 'gue'),
    'TOUS+GUES+SOL':     lambda c: True,
    'PIETON(passerelle/sentier)': lambda c: c['kind'] != 'sol' and c['cls'] in ('passerelle', 'sentier'),
    'PIETON+GUES':       lambda c: c['cls'] in ('passerelle', 'sentier', 'gue'),
    'PIETON+CHEMIN':     lambda c: c['kind'] != 'sol' and c['cls'] in ('passerelle', 'sentier', 'chemin'),
    'ROUTIER':           lambda c: c['kind'] != 'sol' and c['cls'] == 'routier',
}
SRCSETS = {'BD': lambda c: c['src'] == 'BDTOPO', 'OSM': lambda c: c['src'] == 'OSM', 'UNION': lambda c: True}

# ------------------------------------------------------------------ 3. numérotations
numberings = []  # dict(name, lsrc, srcset, variant, direction, seq[list of reps], line info)
for l in lines:
    buf = 20.0 if l['src'] == 'OSM' else 15.0
    cs = crossings_for(l['line'], buf)
    l['n_raw'] = len(cs)
    for vn, vp in VARIANTS.items():
        for sn, sp in SRCSETS.items():
            sub = [c for c in cs if vp(c) and sp(c)]
            # restriction à la zone de 6 km (couverture des données)
            sub = [c for c in sub if dtower_xy(*c['pt']) <= ZONE]
            seq = dedupe(sub)
            if len(seq) == 0: continue
            for dirn in ('A', 'B'):
                sq = seq if dirn == 'A' else seq[::-1]
                is_src = (dirn == 'A') == l['A_is_source']
                end_in = l['A_in'] if dirn == 'A' else l['B_in']
                numberings.append(dict(name=l['name'], lsrc=l['src'], srcset=sn, variant=vn, dirn=dirn,
                                       origin='SOURCE' if is_src else 'EMBOUCHURE', fiable=end_in, seq=sq, line=l))

def pos_ll(r): return inv(*r['pt'])
def pair_d(seq, i, j):  # numéros 1-based
    if len(seq) < j: return None
    return hav(pos_ll(seq[i - 1]), pos_ll(seq[j - 1]))
def dtow(r): return hav(TA, pos_ll(r))

print('\n== FRANCHISSEMENTS par ligne (après dédup 15 m, variante TOUS_PONTS / UNION) ==')
for l in lines:
    nb = [n for n in numberings if n['line'] is l and n['variant'] == 'TOUS_PONTS' and n['srcset'] == 'UNION' and n['dirn'] == 'A']
    k = len(nb[0]['seq']) if nb else 0
    print('%-8s %-45s long=%5dm (tot %5dm, comp+%s, trous=%d) n_raw=%3d  n_dedup=%3d  A:%s %s alt=%s  B:%s alt=%s' % (
        l['src'], l['name'][:45], l['info']['long'], l['info']['total'], l['info']['autres'][:4], l['info']['gaps'], l['n_raw'], k,
        'source' if l['A_is_source'] else 'embouch.', 'in' if l['A_in'] else 'hors-zone', l['zA'],
        'in' if l['B_in'] else 'hors-zone', l['zB']))

# ------------------------------------------------------------------ 4. test (3,11)
PAIRS = [(3, 11), (2, 10), (4, 12), (3, 13), (8, 16), (1, 9), (5, 13), (6, 14), (7, 15), (9, 17)]
stats = {p: [] for p in PAIRS}
cand = []
n_ge11 = 0
allpair_gap8 = []   # toutes les paires (i,i+8)
for nb in numberings:
    seq = nb['seq']
    if len(seq) >= 11: n_ge11 += 1
    for (i, j) in PAIRS:
        d = pair_d(seq, i, j)
        if d is not None:
            stats[(i, j)].append((d, nb))
    for i in range(1, len(seq) - 8 + 1):
        allpair_gap8.append(pair_d(seq, i, i + 8))
    d = pair_d(seq, 3, 11)
    if d is not None and abs(d - TARGET) <= TOL:
        r3, r11 = seq[2], seq[10]
        if min(dtow(r3), dtow(r11)) <= TOWER_NEAR:
            cand.append((nb, d, r3, r11))

print('\n== NUMÉROTATIONS (ligne × jeu de franchissements × variante × sens) : total=%d, avec ≥ 11 franchissements: %d' % (len(numberings), n_ge11))
print('   dont lignes distinctes (nom,src) avec ≥11 en variante quelconque: %d' % len({(n['name'], n['lsrc']) for n in numberings if len(n['seq']) >= 11}))
cnt = collections.Counter((n['name'], n['lsrc']) for n in numberings if len(n['seq']) >= 11)
for k, v in sorted(cnt.items(), key=lambda x: -x[1]): print('   ', k, v, 'numérotations ≥11')

# distribution 3e-11e
print('\n== DISTRIBUTION des distances 3e–11e (toutes numérotations ≥ 11) ==')
ds = [d for d, nb in stats[(3, 11)]]
if ds:
    ds_s = sorted(ds)
    print('  n=%d  min=%.0f  médiane=%.0f  max=%.0f' % (len(ds), ds_s[0], ds_s[len(ds_s) // 2], ds_s[-1]))
    bins = [0, 250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2500, 3000, 4000, 6000, 20000]
    for a, b in zip(bins, bins[1:]):
        print('   %5d–%5d m : %d' % (a, b, sum(1 for d in ds if a <= d < b)))
    near = [d for d in ds if abs(d - TARGET) <= TOL]
    print('  dans 1850±18 m : %d / %d = %.2f %%' % (len(near), len(ds), 100 * len(near) / len(ds)))
    print('  densité attendue si uniforme sur [%.0f,%.0f] (étendue observée): %.2f %%' % (ds_s[0], ds_s[-1], 100 * 2 * TOL / max(1, (ds_s[-1] - ds_s[0]))))
    # uniforme sur 1000–3000 m (zone plausible)
    inb = [d for d in ds if 1000 <= d <= 3000]
    print('  numérotations 3e–11e entre 1000 et 3000 m: %d ; probabilité uniforme 36/2000=1.8 %% -> attendu %.1f' % (len(inb), 0.018 * len(inb)))

print('\n== CONTRÔLE: autres paires (même nombre de ponts ≥ j) — proportion dans 1850±18 m (faux positifs) ==')
for p in PAIRS:
    v = [d for d, nb in stats[p]]
    hit = [d for d in v if abs(d - TARGET) <= TOL]
    print('  paire %2d-%2d : n=%3d  dans fenêtre=%2d (%.1f %%)' % (p[0], p[1], len(v), len(hit), 100 * len(hit) / len(v) if v else 0))
g8 = allpair_gap8
h8 = [d for d in g8 if abs(d - TARGET) <= TOL]
print('  toutes paires (i,i+8): n=%d dans fenêtre=%d (%.2f %%)' % (len(g8), len(h8), 100 * len(h8) / len(g8) if g8 else 0))

# contrôle par positions aléatoires le long des lignes réelles
print('\n== CONTRÔLE aléatoire: mêmes lignes, mêmes nombres de franchissements, positions tirées uniformément le long de la ligne ==')
NSIM = 300
sim_hits = 0; sim_tot = 0
seen = set()
for nb in numberings:
    n = len(nb['seq'])
    if n < 11: continue
    key = (nb['name'], nb['lsrc'], nb['variant'], nb['srcset'], n)
    if key in seen: continue   # une seule direction : les deux directions sont des numérotations symétriques
    seen.add(key)
    ln = nb['line']['line']
    for _ in range(NSIM):
        ss = sorted(random.uniform(0, ln.length) for _ in range(n))
        pts = [ln.interpolate(s) for s in ss]
        d = hav(inv(pts[2].x, pts[2].y), inv(pts[10].x, pts[10].y))
        sim_tot += 1
        if abs(d - TARGET) <= TOL: sim_hits += 1
        d = hav(inv(pts[n - 3].x, pts[n - 3].y), inv(pts[n - 11].x, pts[n - 11].y))
        sim_tot += 1
        if abs(d - TARGET) <= TOL: sim_hits += 1
print('  tirages=%d, dans fenêtre=%d (%.2f %%)' % (sim_tot, sim_hits, 100 * sim_hits / sim_tot if sim_tot else 0))
sim_rate = sim_hits / sim_tot if sim_tot else 0.0

# ------------------------------------------------------------------ 5. candidats
print('\n== CANDIDATS: 3e–11e à 1850 ± 18 m ET l\'un des deux à < 1,5 km de la tour: %d ==' % len(cand))
cand_sorted = sorted(cand, key=lambda c: abs(c[1] - TARGET))
for nb, d, r3, r11 in cand_sorted:
    la3, lo3 = pos_ll(r3); la11, lo11 = pos_ll(r11)
    print('-' * 100)
    print('%s [%s] | jeu=%s | variante=%s | numéroté depuis %s (extrémité %s, fiable=%s)' % (
        nb['name'], nb['lsrc'], nb['srcset'], nb['variant'], nb['origin'], nb['dirn'], nb['fiable']))
    print('   n franchissements=%d  d(3e,11e)=%.1f m (écart %+.1f)' % (len(nb['seq']), d, d - TARGET))
    for k, r in ((3, r3), (11, r11)):
        la, lo = pos_ll(r)
        print('   #%2d (%.6f, %.6f) nature=%s/%s  d_tour=%.0f m  membres=%s' % (k, la, lo, r['cls'], r['kind'], dtow(r), '; '.join(m['label'] for m in r['members'][:3])))

# les 20 plus proches de 1850 (toutes numérotations) pour information, sans filtre tour
print('\n== Pour information: 12 numérotations 3e–11e les plus proches de 1850 m (sans filtre tour) ==')
for d, nb in sorted(stats[(3, 11)], key=lambda x: abs(x[0] - TARGET))[:12]:
    r3, r11 = nb['seq'][2], nb['seq'][10]
    print('  %8.1f m | %-28s [%s/%s] %-26s %s | #3 %.5f,%.5f (%s, tour %.0f m) #11 %.5f,%.5f (%s, tour %.0f m)' % (
        d, nb['name'][:28], nb['lsrc'], nb['srcset'], nb['variant'][:26], nb['origin'],
        *pos_ll(r3), r3['cls'], dtow(r3), *pos_ll(r11), r11['cls'], dtow(r11)))

# ------------------------------------------------------------------ 6. faux positifs attendus
print('\n== TAUX DE FAUX POSITIFS ==')
nn = len(stats[(3, 11)])
print('  numérotations testables (≥11 franchissements) = %d (fortement redondantes: mêmes ponts, variantes emboîtées, 2 sens)' % nn)
rates = []
for p in PAIRS:
    v = [d for d, nb in stats[p]]
    rates.append(len([d for d in v if abs(d - TARGET) <= TOL]) / len(v) if v else 0)
print('  taux par chance (paires témoins ci-dessus + tirage aléatoire): %.2f %% (aléatoire) ; moyenne des paires: %.2f %%' % (100 * sim_rate, 100 * sum(rates) / len(rates)))
print('  nb de numérotations (3,11) dans fenêtre sans filtre tour: %d ; avec filtre tour: %d ; attendu par chance (taux aléatoire × n): %.1f' % (
    len([d for d in ds if abs(d - TARGET) <= TOL]), len(cand), sim_rate * nn))
