# -*- coding: utf-8 -*-
"""T15 — lecture SOLAIRE de l'énigme É12.
Soleil du 30/04/1524 julien (= 10/05/1524 grégorien) à Saint-Maximin, heures temporaires / égales,
horizon réel (MNT 2 m + API IGN altimétrie), jonctions de chemins BD TOPO qualifiées, contrôle aléatoire.
Usage : python T15_solaire.py [fetch|run]   (fetch = remplit le cache altimétrique ; run = calculs + rapport)
"""
import sys, json, math, os, time, random, threading
sys.path.insert(0, 'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12')
from geo12 import *
import geo12
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, Counter
from shapely.geometry import Point, LineString
import shapely

CACHE = S + 'exk_e12/t15_alti_cache.json'
ORIG = {'RP': RP, 'TA': TA}
RMAX = 2500.0           # rayon de recherche clairière
TOLS = [1.5, 3.0, 5.0]  # demi-largeurs angulaires de cône testées (°)
TOL0 = 3.0
SEED = 15

# ---------------------------------------------------------------- cache altimétrique
_cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
_lock = threading.Lock()
def key(la, lo): return f"{la:.5f},{lo:.5f}"
def inmnt(la, lo): return alt(la, lo) is not None
def elev(la, lo):
    z = alt(la, lo)
    if z is not None: return z
    return _cache.get(key(la, lo))
def prefetch(points, label=''):
    need = sorted({key(*p) for p in points if not inmnt(*p) and key(*p) not in _cache})
    if not need: return
    B = 100
    batches = [need[i:i+B] for i in range(0, len(need), B)]
    print(f'  [fetch {label}] {len(need)} pts, {len(batches)} requêtes', flush=True)
    def work(b):
        pts = [tuple(map(float, k.split(','))) for k in b]
        for attempt in range(4):
            try:
                r = alti(pts)
                with _lock:
                    for k, z in zip(b, r): _cache[k] = z if z is not None and z > -1000 else None
                return
            except Exception as e:
                time.sleep(2 + attempt * 3)
        print('   échec batch', flush=True)
    done = 0
    with ThreadPoolExecutor(5) as ex:
        for _ in ex.map(work, batches):
            done += 1
            if done % 40 == 0:
                print(f'   {done}/{len(batches)}', flush=True)
                with _lock: json.dump(_cache, open(CACHE, 'w'))
    with _lock: json.dump(_cache, open(CACHE, 'w'))

# ---------------------------------------------------------------- éphéméride (Meeus, bas-précision)
def jd(y, m, d, cal):
    if m <= 2: y -= 1; m += 12
    B = 0
    if cal == 'G':
        A = y // 100; B = 2 - A + A // 4
    return math.floor(365.25 * (y + 4716)) + math.floor(30.6001 * (m + 1)) + d + B - 1524.5
JD_J = jd(1524, 4, 30, 'J'); JD_G = jd(1524, 5, 10, 'G')
assert abs(JD_J - JD_G) < 1e-9
def sun_eq(JD):
    T = (JD - 2451545.0) / 36525
    L0 = (280.46646 + 36000.76983 * T + 0.0003032 * T * T) % 360
    Mm = math.radians((357.52911 + 35999.05029 * T - 0.0001537 * T * T) % 360)
    C = ((1.914602 - 0.004817 * T - 0.000014 * T * T) * math.sin(Mm) + (0.019993 - 0.000101 * T) * math.sin(2 * Mm) + 0.000289 * math.sin(3 * Mm))
    tl = L0 + C
    om = math.radians(125.04 - 1934.136 * T)
    lam = math.radians(tl - 0.00569 - 0.00478 * math.sin(om))
    eps = 23.0 + 26.0 / 60 + 21.448 / 3600 - (46.8150 * T + 0.00059 * T * T - 0.001813 * T ** 3) / 3600
    eps = math.radians(eps + 0.00256 * math.cos(om))
    dec = math.degrees(math.asin(math.sin(eps) * math.sin(lam)))
    ra = math.degrees(math.atan2(math.cos(eps) * math.sin(lam), math.cos(lam))) % 360
    eot = ((L0 - 0.0057183 - ra + 180) % 360 - 180) * 4  # minutes
    return dec, eot
DEC, EOT = sun_eq(JD_G + 0.5 - 6.03 / 360 * 1.0)  # midi local
LATP = RP[0]
def sun_alt_az(t):
    """t = heure solaire VRAIE locale (h, 0..24). Retourne (hauteur géométrique vraie°, azimut° depuis N horaire)."""
    UT = t - 6.03 / 15 - EOT / 60
    dec, _ = sun_eq(JD_G + 0.5 - 0.5 + UT / 24 + 0.0)  # JD à 0h UT = JD_G (jd() donne .5 à 0h)
    H = math.radians(15 * (t - 12)); ph = math.radians(LATP); d = math.radians(dec)
    s = math.sin(ph) * math.sin(d) + math.cos(ph) * math.cos(d) * math.cos(H)
    h = math.degrees(math.asin(s))
    A = (math.degrees(math.atan2(math.sin(H), math.cos(H) * math.sin(ph) - math.tan(d) * math.cos(ph))) + 180) % 360
    return h, A
def refr(h):  # Bennett, degrés
    h = max(h, -1.5)
    return (1 / math.tan(math.radians(h + 7.31 / (h + 4.4)))) / 60
def app_upper(t):
    h, A = sun_alt_az(t)
    return h + refr(h) + 0.2667, A   # bord supérieur apparent

# ---------------------------------------------------------------- horizon
def prof_dists():
    return list(range(10, 1000, 10)) + list(range(1000, 3000, 40)) + list(range(3000, 12001, 100))
def horizon_points(o, azs):
    pts = []
    for a in azs:
        for d in prof_dists(): pts.append(dest(o, a, d))
    return pts
def hor_angle(o, a, h_obs=2.0, dists=None):
    """angle d'élévation max (°) de l'horizon depuis o dans la direction a ; (angle, distance)."""
    z0 = elev(*o)
    if z0 is None:
        prefetch([o], 'origine')
        z0 = elev(*o)
    if z0 is None:
        return None, None   # altitude d'origine introuvable (hors MNT et hors IGN) : inconnu
    best = -90; bd = None
    for d in (dists or prof_dists()):
        p = dest(o, a, d); z = elev(*p)
        if z is None: continue
        ang = math.degrees(math.atan2(z - z0 - h_obs - d * d / (2 * R) * 0.87, d))
        if ang > best: best = ang; bd = d
    return best, bd
EAZ = list(range(40, 126, 2)); WAZ = list(range(234, 322, 2))
_hor = {}
def horizon(oname, a):
    k = (oname, a)
    if k not in _hor: _hor[k] = hor_angle(ORIG[oname], a)
    return _hor[k]
def hor_interp(oname, a):
    a0 = 2 * math.floor(a / 2); a1 = a0 + 2
    h0 = horizon(oname, a0)[0]; h1 = horizon(oname, a1)[0]
    return h0 + (h1 - h0) * (a - a0) / 2

# ---------------------------------------------------------------- solve helpers
def bisect(f, a, b, n=60):
    fa = f(a)
    for _ in range(n):
        m = (a + b) / 2; fm = f(m)
        if (fa <= 0) == (fm <= 0): a, fa = m, fm
        else: b = m
    return (a + b) / 2
def hms(t): 
    h = int(t); m = (t - h) * 60; return f'{h:02d}h{int(m):02d}'

def solar_times(oname):
    """retourne dict de modèles -> liste de (label, t_heure_solaire_vraie)"""
    # lever / coucher conventionnels (horizon plat) : bord sup. apparent à 0°
    f = lambda t: app_upper(t)[0] - 0.0
    rise0 = bisect(f, 0.5, 12); set0 = bisect(f, 23.5, 12)
    # lever / coucher apparents avec relief
    def fr(t):
        h, a = app_upper(t); return h - hor_interp(oname, a)
    riseA = bisect(fr, 2.0 if fr(2.0) < 0 else 0.5, 12)
    # coucher : horizon ouest
    setA = bisect(fr, 22.0 if fr(22.0) < 0 else 23.9, 12)
    M = {}
    def temporaires(r, s, tag):
        u = (s - r) / 12
        for n, lab in ((3, '3e'), (11, '11e')):
            for sub, off in (('début', n - 1), ('milieu', n - 0.5), ('fin', n)):
                M.setdefault((tag, lab), []).append((sub, r + off * u))
    temporaires(rise0, set0, 'T1 temporaires (horizon plat)')
    temporaires(riseA, setA, 'T2 temporaires (lever/coucher apparents relief)')
    for n, lab in ((3, '3e'), (11, '11e')):
        for sub, off in (('début', n - 1), ('milieu', n - 0.5), ('fin', n)):
            M.setdefault(('E1 égales depuis le lever théorique', lab), []).append((sub, rise0 + off))
            M.setdefault(('E2 égales canoniales depuis 6h (tierce=9h)', lab), []).append((sub, 6 + off))
    # E3 : heures égales horloge (11h = matin, 3h = soleil sous l'horizon)
    M[('E3 égales depuis minuit', '3e')] = [('3h00', 3.0)]
    M[('E3 égales depuis minuit', '11e')] = [('11h00', 11.0)]
    return dict(rise0=rise0, set0=set0, riseA=riseA, setA=setA, M=M)

# ---------------------------------------------------------------- géodonnées
def angdiff(a, b): return abs((a - b + 180) % 360 - 180)
def build_junctions():
    rt = load('troncon_de_route.geojson')
    nat = {'Chemin', 'Sentier', 'Route empierrée'}
    deg = Counter(); co = {}
    kk = lambda c: (round(c[0] * 10), round(c[1] * 10))
    for g, p in rt:
        if p['nature'] not in nat or p.get('fictif'): continue
        gs = [g] if g.geom_type == 'LineString' else list(g.geoms)
        for l in gs:
            cs = list(l.coords)
            for c in (cs[0], cs[-1]):
                deg[kk(c)] += 1; co[kk(c)] = c
    return [(co[k], v) for k, v in deg.items() if v >= 3]

# ---------------------------------------------------------------- visibilité étendue (MNT + API)
def vis_pts(src, la, lo, step=20.0):
    d = hav(src, (la, lo)); n = max(2, int(d / step))
    return [(src[0] + (la - src[0]) * k / n, src[1] + (lo - src[1]) * k / n) for k in range(0, n + 1)]
def visible_ext(src, la, lo, h_obs=2, h_tgt=2, step=20.0):
    ps = vis_pts(src, la, lo, step); n = len(ps) - 1
    z0 = elev(*ps[0]); z1 = elev(*ps[-1])
    if z0 is None or z1 is None: return None, None
    a0 = z0 + h_obs; a1 = z1 + h_tgt; worst = 0.0
    for k in range(1, n):
        z = elev(*ps[k]); t = k / n
        if z is None: continue
        line = a0 + (a1 - a0) * t
        if z > line + 0.5: worst = max(worst, z - line)
    return worst == 0.0, round(worst, 1)

# ---------------------------------------------------------------- ensoleillement d'un point
def lit(la, lo, A, hsun, dists=None):
    ang, d = hor_angle((la, lo), A, h_obs=0.0, dists=dists or LITD)
    if ang is None: return None, None   # inconnu
    return hsun > ang, ang
LITD = list(range(20, 3000, 40)) + list(range(3000, 12001, 150))

# ================================================================ MAIN
def main(mode):
    random.seed(SEED)
    out = []
    P = lambda *a: print(*a, flush=True)
    junc = build_junctions()
    J = []
    for c, dg in junc:
        la, lo = inv(*c)
        J.append(dict(x=c[0], y=c[1], la=la, lo=lo, deg=dg))
    for j in J:
        for o in ORIG:
            j['d' + o] = hav(ORIG[o], (j['la'], j['lo'])); j['a' + o] = az(ORIG[o], (j['la'], j['lo']))
    Jn = [j for j in J if min(j['dRP'], j['dTA']) <= RMAX + 700]
    P(f'jonctions deg>=3 (Chemin/Sentier/Route empierrée) : {len(J)} au total ; {len(Jn)} dans {RMAX+700:.0f} m')

    # préchargement altimétrie
    if mode == 'fetch':
        pts = horizon_points(RP, EAZ + WAZ) + horizon_points(TA, [])
        prefetch(pts, 'horizon RP')
        cand = [j for j in Jn if min(j['dRP'], j['dTA']) <= RMAX]
        return

    # ------------------------------------------------ 1. éphéméride
    P('=' * 78)
    P('1. SOLEIL — date : 30/04/1524 julien = 10/05/1524 grégorien, JD(0h UT) = %.1f' % JD_G)
    dec0, _ = sun_eq(JD_G + 0.5)
    P('   déclinaison à midi ≈ %.3f°, équation du temps ≈ %+.1f min (temps solaire vrai ; lon %.3f E ⇒ midi moyen local = 12h − %.0f min UT)' % (dec0, EOT, 6.03, 6.03 * 4))
    P('   Heures = temps solaire VRAI local (pas d\'heure légale en 1524).')
    P('   Hauteurs/azimuts : hauteur géométrique vraie du centre ; azimut depuis le nord, sens horaire.')
    P()
    ST = {}
    for o in ORIG:
        ST[o] = solar_times(o)
    st = ST['RP']
    P('   Lever/coucher théoriques (horizon plat, bord sup.) : lever %s (az %.1f°)  coucher %s (az %.1f°)  jour = %.2f h' % (
        hms(st['rise0']), sun_alt_az(st['rise0'])[1], hms(st['set0']), sun_alt_az(st['set0'])[1], st['set0'] - st['rise0']))
    P('   Horizon réel depuis RP (angle d\'élévation max ; distance de l\'obstacle) :')
    for a in (50, 56, 60, 64, 70, 76, 80, 90, 100, 110, 120):
        if a in EAZ:
            h, d = horizon('RP', a); P(f'     az {a:3d}° : {h:5.2f}°  à {d} m')
    for a in (240, 250, 260, 270, 280, 290, 300, 310):
        h, d = horizon('RP', a); P(f'     az {a:3d}° : {h:5.2f}°  à {d} m')
    for o in ('RP',):
        s = ST[o]
        rA = s['riseA']; sA = s['setA']
        P('   Lever APPARENT depuis %s (bord sup. du soleil franchit le relief) : %s, az %.1f°, hauteur vraie %.2f°' % (
            o, hms(rA), sun_alt_az(rA)[1], sun_alt_az(rA)[0]))
        P('   Coucher APPARENT depuis %s : %s, az %.1f°, hauteur vraie %.2f°   → jour apparent = %.2f h' % (
            o, hms(sA), sun_alt_az(sA)[1], sun_alt_az(sA)[0], sA - rA))
    P()
    # liste des directions (modèle, rang, sous-moment) pour chaque origine ; même soleil (TA ≈ RP à 82 m)
    DIRS = []   # (model, rank, sub, t, hsun, az)
    P('   Directions solaires (même soleil pour RP et TA : 82 m d\'écart, parallaxe nulle) :')
    P('   %-48s %-4s %-8s %-7s %-7s %-8s %s' % ('modèle', 'rang', 'moment', 'heure', 'haut.', 'azimut', 'soleil visible au-dessus du relief RP ?'))
    for (mod, lab), lst in ST['RP']['M'].items():
        for sub, t in lst:
            h, a = sun_alt_az(t)
            if h < 0:
                vis = 'NON (sous l\'horizon)'
            else:
                a_r = a
                hz = hor_interp('RP', a_r) if (a_r % 360 >= 40 and a_r <= 125) or (a_r >= 234 and a_r <= 320) else None
                vis = 'oui (horizon %.1f°)' % hz if hz is not None and (h + refr(h)) > hz else ('NON (masqué, horizon %.1f°)' % hz if hz is not None else 'hors plage horizon calculée')
            P('   %-48s %-4s %-8s %-7s %6.2f° %7.2f°  %s' % (mod, lab, sub, hms(t), h, a, vis))
            if h >= 0: DIRS.append((mod, lab, sub, t, h, a))
    P()

    # ------------------------------------------------ 2. jonctions qualifiées
    P('=' * 78)
    P('2. JONCTIONS QUALIFIÉES (nœuds de degré>=3 des tronçons Chemin/Sentier/Route empierrée BD TOPO)')
    P('   critères : <=60 m d\'un tronçon hydrographique ; aucun bâtiment à <50 m ; visible depuis l\'origine ; dans %d m' % RMAX)
    hyd = load('troncon_hydrographique.geojson')
    hg = [g for g, p in hyd]; hp = [p for g, p in hyd]
    htree = STRtree(hg)
    bl = load('batiment.geojson'); bg = [g for g, p in bl]; btree = STRtree(bg)
    cand = [j for j in Jn if min(j['dRP'], j['dTA']) <= RMAX]
    for j in cand:
        p = Point(j['x'], j['y'])
        i = htree.nearest(p); j['dh'] = p.distance(hg[i]); j['hname'] = hp[i].get('cpx_toponyme_de_cours_d_eau') or hp[i].get('nature')
        j['hnat'] = hp[i].get('nature')
        i = btree.nearest(p); j['db'] = p.distance(bg[i])
    base = [j for j in cand if j['dh'] <= 60 and j['db'] >= 50]
    P(f'   jonctions dans {RMAX:.0f} m (RP ou TA) : {len(cand)} ; ruisseau<=60 m et bâtiment>=50 m : {len(base)}')
    # visibilité
    allp = []
    for j in base:
        for o in ORIG:
            if j['d' + o] <= RMAX: allp += vis_pts(ORIG[o], j['la'], j['lo'])
    prefetch(allp, 'visibilité')
    for j in base:
        for o in ORIG:
            for h in (2, 12):
                j[f'v{o}{h}'] = visible_ext(ORIG[o], j['la'], j['lo'], h_obs=h)[0] if j['d' + o] <= RMAX else None
    Q = {}
    for o in ORIG:
        Q[o] = [j for j in base if j['d' + o] <= RMAX and j[f'v{o}2']]
        P(f'   visibles depuis {o} (observateur à 2 m) : {len(Q[o])}  ; (observateur à 12 m : {sum(1 for j in base if j["d"+o] <= RMAX and j[f"v{o}12"])})')
    for o in ORIG:
        P(f'   --- qualifiées depuis {o} (h_obs 2 m) : lat, lon, dist, azimut, ruisseau(dist), bât(dist), degré')
        for j in sorted(Q[o], key=lambda j: j['a' + o]):
            P('     %.5f, %.5f  %5.0f m  az %6.1f°  %s (%.0f m)  bât %.0f m  deg %d' % (j['la'], j['lo'], j['d' + o], j['a' + o], j['hname'], j['dh'], j['db'], j['deg']))
    P()

    # ------------------------------------------------ 3. comptes par direction + contrôle
    P('=' * 78)
    P('3. JONCTIONS QUALIFIÉES SUR CHAQUE DIRECTION SOLAIRE (cône ±%.1f°, ≤%d m) ET CONTRÔLE' % (TOL0, RMAX))
    def count(o, a, tol=TOL0, rmin=0, rmax=RMAX):
        return [j for j in Q[o] if angdiff(j['a' + o], a) <= tol and rmin <= j['d' + o] <= rmax]
    ctrl_all = {}; ctrl_E = {}; ctrl_W = {}
    rnd_all = [random.uniform(0, 360) for _ in range(200)]
    rnd_E = [random.uniform(40, 125) for _ in range(200)]
    rnd_W = [random.uniform(234, 320) for _ in range(200)]
    for o in ORIG:
        for tol in TOLS:
            ctrl_all[o, tol] = [len(count(o, a, tol)) for a in rnd_all]
            ctrl_E[o, tol] = [len(count(o, a, tol)) for a in rnd_E]
            ctrl_W[o, tol] = [len(count(o, a, tol)) for a in rnd_W]
    mean = lambda l: sum(l) / len(l)
    P('   CONTRÔLE (200 azimuts aléatoires, cône identique) : moyenne de jonctions qualifiées par direction')
    for o in ORIG:
        for tol in TOLS:
            P('     origine %s cône ±%.1f° : tout azimut 0-360 : %.2f (max %d, part de directions à 0 jonction %.0f%%) | azimuts E 40-125 : %.2f | azimuts O 234-320 : %.2f' % (
                o, tol, mean(ctrl_all[o, tol]), max(ctrl_all[o, tol]), 100 * sum(1 for c in ctrl_all[o, tol] if c == 0) / 200,
                mean(ctrl_E[o, tol]), mean(ctrl_W[o, tol])))
    P()
    P('   DIRECTIONS SOLAIRES : nb de jonctions qualifiées (cône ±%.1f° / ±%.1f°) ; si >0, détail' % (TOLS[0], TOL0))
    hit = []
    for o in ORIG:
        P(f'   -- origine {o}')
        for (mod, lab, sub, t, h, a) in DIRS:
            c1 = count(o, a, TOLS[0]); c3 = count(o, a, TOL0); c5 = count(o, a, TOLS[2])
            ctrl = ctrl_E if a < 180 else ctrl_W
            pct = 100 * sum(1 for c in ctrl[o, TOL0] if c >= len(c3)) / 200
            P('     %-44s %-3s %-7s %s az %6.2f° : ±1.5°:%d  ±3°:%d  ±5°:%d   (contrôle ±3° même secteur : moy %.2f ; P(ctrl>=obs)=%.0f%%)' % (
                mod[:44], lab, sub, hms(t), a, len(c1), len(c3), len(c5), mean(ctrl[o, TOL0]), pct))
            for j in c3:
                hit.append((o, mod, lab, sub, a, j))
    P()
    P('   Détail des jonctions trouvées dans un cône ±3° d\'une direction solaire :')
    seen = {}
    for o, mod, lab, sub, a, j in hit:
        k = (o, round(j['la'], 5), round(j['lo'], 5))
        seen.setdefault(k, []).append((mod[:2], lab, sub, a))
    for k, v in sorted(seen.items(), key=lambda kv: (kv[0][0], kv[0][1])):
        j = [jj for (oo, mm, ll, ss, aa, jj) in hit if (oo, round(jj['la'], 5), round(jj['lo'], 5)) == k][0]
        mods = sorted({(m, l, s) for m, l, s, a in v})
        P('     [%s] %.5f, %.5f  %4.0f m  az %6.1f°  ruisseau %s (%.0f m)  <- %s' % (k[0], k[1], k[2], j['d' + k[0]], j['a' + k[0]], j['hname'], j['dh'],
          '; '.join(f'{m} {l} {s}' for m, l, s in mods[:6]) + (' …' if len(mods) > 6 else '')))
    P()

    # ------------------------------------------------ 4. éclairement
    P('=' * 78)
    P('4. ÉCLAIREMENT DU RUISSEAU AU LEVER APPARENT (soleil rasant) ET VISIBLE DEPUIS RP')
    rA = ST['RP']['riseA']; hA, AA = app_upper(rA)
    hv, Av = sun_alt_az(rA)
    P('   lever apparent RP : %s, azimut %.1f°, bord sup. apparent %.2f° (centre vrai %.2f°)' % (hms(rA), Av, hA, hv))
    # échantillons de ruisseau dans 2.5 km, tous les 50 m
    samples = []
    for (g, p) in hyd:
        L = g.length
        if L == 0: continue
        n = max(1, int(L / 50))
        for k in range(n + 1):
            pt = g.interpolate(min(L, k * 50.0))
            la, lo = inv(pt.x, pt.y)
            if hav(RP, (la, lo)) <= RMAX:
                samples.append((la, lo, p.get('cpx_toponyme_de_cours_d_eau') or p.get('nature'), p.get('nature')))
    P(f'   échantillons de cours d\'eau (50 m) dans {RMAX:.0f} m : {len(samples)}')
    prefetch([q for s in samples for q in vis_pts(RP, s[0], s[1])], 'vis ruisseau')
    vs = [s for s in samples if visible_ext(RP, s[0], s[1], h_obs=2, h_tgt=0.5)[0]]
    P(f'   visibles depuis RP (obs 2 m, cible 0,5 m) : {len(vs)}')
    # moments testés : lever apparent + quelques minutes après
    moments = [('lever apparent', rA), ('lever apparent +10 min', rA + 1 / 6), ('lever apparent +30 min', rA + 0.5)]
    for lab, t in moments:
        hh, aa = app_upper(t)
        prefetch([dest((s[0], s[1]), aa, d) for s in vs for d in LITD], 'éclairement ' + lab)
    results = {}
    for lab, t in moments:
        hh, aa = app_upper(t)
        L = [(s, lit(s[0], s[1], aa, hh)[0]) for s in vs]
        nunk = sum(1 for s, l in L if l is None)
        if nunk: P('       (%d échantillons ignorés : altitude d origine introuvable)' % nunk)
        L = [(s, l) for s, l in L if l is not None]
        results[lab] = L
        names = Counter(s[2] for s, l in L if l)
        P('   %s (%s, az %.1f°, haut. bord sup. %.2f°) : %d/%d échantillons visibles éclairés' % (lab, hms(t), aa, hh, sum(1 for s, l in L if l), len(L)))
        for nm, c in names.most_common(8):
            P('       %-34s %d éch. éclairés (~%d m)' % (nm, c, c * 50))
        # points éclairés : emprise
        lp = [s for s, l in L if l]
        if lp:
            P('       éclairés — bornes : lat %.5f–%.5f, lon %.5f–%.5f ; dist RP %.0f–%.0f m ; az RP %.0f–%.0f°' % (
                min(s[0] for s in lp), max(s[0] for s in lp), min(s[1] for s in lp), max(s[1] for s in lp),
                min(hav(RP, (s[0], s[1])) for s in lp), max(hav(RP, (s[0], s[1])) for s in lp),
                min(az(RP, (s[0], s[1])) for s in lp), max(az(RP, (s[0], s[1])) for s in lp)))
    # jonctions qualifiées dont le ruisseau est éclairé au lever apparent
    P('   Jonctions qualifiées depuis RP dont le cours d\'eau (<=60 m) est éclairé au lever apparent :')
    hh, aa = app_upper(rA)
    for j in sorted(Q['RP'], key=lambda j: j['aRP']):
        i = htree.nearest(Point(j['x'], j['y'])); pt = hg[i].interpolate(hg[i].project(Point(j['x'], j['y'])))
        la, lo = inv(pt.x, pt.y)
        prefetch([dest((la, lo), aa, d) for d in LITD], 'lit j')
        l, ang = lit(la, lo, aa, hh)
        P('     %.5f, %.5f %5.0f m az %6.1f°  ruisseau (%.0f m) éclairé au lever apparent : %s (horizon vers soleil %s vs soleil %.1f°)' % (j['la'], j['lo'], j['dRP'], j['aRP'], j['dh'], 'INCONNU (altitude manquante)' if l is None else ('OUI' if l else 'non'), 'n/a' if ang is None else '%.1f°' % ang, hh))
    P()

    # ------------------------------------------------ 5. triangle 3e / 11e
    P('=' * 78)
    P('5. TRIANGLE : droites RP→soleil 3e heure et RP→soleil 11e heure, deux points à 1850 m l\'un de l\'autre')
    rng = random.Random(SEED)
    TOLB = 2.0; DMAX = 3000.0; DT = 18.5
    allJ = [j for j in Jn if j['dRP'] <= DMAX or j['dTA'] <= DMAX]
    for j in allJ:
        pass
    def pairs(o, a3, a11, tol=TOLB):
        A3 = [j for j in J if hav(ORIG[o], (j['la'], j['lo'])) <= DMAX and angdiff(az(ORIG[o], (j['la'], j['lo'])), a3) <= tol] if False else None
    JJ = {o: [] for o in ORIG}
    for o in ORIG:
        for j in J:
            d = hav(ORIG[o], (j['la'], j['lo']))
            if 100 <= d <= DMAX:
                JJ[o].append((j, d, az(ORIG[o], (j['la'], j['lo']))))
    def pairs(o, a3, a11, tol=TOLB):
        s3 = [(j, d) for j, d, a in JJ[o] if angdiff(a, a3) <= tol]
        s11 = [(j, d) for j, d, a in JJ[o] if angdiff(a, a11) <= tol]
        res = []
        for j3, d3 in s3:
            for j11, d11 in s11:
                dd = math.hypot(j3['x'] - j11['x'], j3['y'] - j11['y'])
                if abs(dd - 1850) <= DT: res.append((j3, d3, j11, d11, dd))
        return res
    P('   (jonctions de chemins quelconques, 100–3000 m, cône ±%.1f° ; paire à 1850 ± %.1f m ; aucune exigence ruisseau/visibilité ici)' % (TOLB, DT))
    # directions appariées
    pairlist = []
    for (mod, lab), lst in ST['RP']['M'].items():
        if lab != '3e' or mod.startswith('E3'): continue
        l11 = ST['RP']['M'][(mod, '11e')]
        for (sub, t3), (sub2, t11) in zip(lst, l11):
            a3 = sun_alt_az(t3)[1]; a11 = sun_alt_az(t11)[1]
            pairlist.append((mod, sub, t3, t11, a3, a11))
    for o in ORIG:
        P(f'   -- origine {o}')
        for mod, sub, t3, t11, a3, a11 in pairlist:
            th = (a11 - a3) % 360
            pr = pairs(o, a3, a11)
            ctrl = []
            for _ in range(200):
                phi = rng.uniform(0, 360)
                ctrl.append(len(pairs(o, a3 + phi, a11 + phi)))
            pc = 100 * sum(1 for c in ctrl if c >= len(pr)) / 200
            P('     %-44s %-6s 3e %s az %6.2f° / 11e %s az %6.2f° (écart %.1f°) : %d paires ; contrôle (200 rotations) moy %.2f, max %d ; P(ctrl>=obs)=%.0f%%' % (
                mod[:44], sub, hms(t3), a3, hms(t11), a11, th, len(pr), mean(ctrl), max(ctrl), pc))
            for j3, d3, j11, d11, dd in pr[:6]:
                la3, lo3 = j3['la'], j3['lo']; la11, lo11 = j11['la'], j11['lo']
                P('        3e: %.5f,%.5f (%4.0f m)  11e: %.5f,%.5f (%4.0f m)  séparation %.1f m  [ruisseau 3e %.0f m / 11e %.0f m]' % (
                    la3, lo3, d3, la11, lo11, d11, dd, j3.get('dh', float('nan')), j11.get('dh', float('nan'))))
    P()
    P('   Table analytique (loi des cosinus) : distances d3, d11 avec |P3P11| = 1850 m pour l\'écart angulaire du milieu T1')
    mod, sub, t3, t11, a3, a11 = [p for p in pairlist if p[0].startswith('T1') and p[1] == 'milieu'][0]
    th = math.radians((a11 - a3) % 360)
    P('   écart angulaire %.2f° ; d3 -> d11 :' % math.degrees(th))
    for d3 in (200, 500, 800, 1000, 1500, 2000, 2500):
        # d11² - 2 d3 cos(th) d11 + d3² - 1850² = 0
        b = -2 * d3 * math.cos(th); c = d3 * d3 - 1850 ** 2
        disc = b * b - 4 * c
        sols = [(-b + s * math.sqrt(disc)) / 2 for s in (1, -1)] if disc >= 0 else []
        P('     d3=%4d m -> d11 = %s' % (d3, ', '.join('%.0f m' % s for s in sols if s > 0)))
    json.dump(_cache, open(CACHE, 'w'))

if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'run')
