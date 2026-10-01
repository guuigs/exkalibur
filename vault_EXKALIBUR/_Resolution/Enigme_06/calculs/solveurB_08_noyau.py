"""Solveur B / É6 — 3b) chaînes de 4 C dans ±1 % de D, restreintes à une liste « noyau » thématique (croisade / Urbain II / Templiers / Arthur / chasse),
avec filtre FAQ07-166 (la chaîne ne croise pas la lame de l'épée É1 = Ligne 5 Urquhart->Valence de la carte de Guilhem) et exclusion de Carnac
(Carnac = C n°1 de É5, les 4 C de É6 sont « à identifier dans cette énigme » FAQ03-092 -> on teste avec ET sans Carnac).
Test du hasard : fraction de toutes les chaînes possibles (n*(n-1)*(n-2)*(n-3)/2) qui tombent dans ±1 % de D, pour D « tiré au hasard » entre 200 et 500 km (contrôle)."""
import sys, json, itertools, random
import numpy as np
sys.path.insert(0, "."); from solveurB_geo import *
from solveurB_05_chaines import load_poolA, TARGETS, dist_matrix
pool = load_poolA()
CORE = ["Clermont", "Cluny", "Cadouin", "Cîteaux", "Clairvaux", "Chartres", "Conques", "Compostelle", "Canterbury", "Caerleon", "Cadbury Castle (Camelot)",
        "Carcassonne", "Caen", "Chinon", "Cahors", "Carlisle", "Colchester", "Cologne", "Constantinople (Sainte-Sophie)", "Chester", "Cambrai", "Chichester",
        "Caernarfon", "Cardiff", "Charroux", "Cressing Temple", "Chartreuse", "Chaource", "Cassino", "Canossa", "Camelford (Camlann)", "Carmarthen",
        "Cerne Abbas", "Corbie", "Compiègne", "Chelles", "Crécy", "Cassel", "Cherbourg", "Calais", "Cambridge", "Champmol", "Clairefontaine"]
CORE = [c for c in CORE if c in pool]
URQ, VAL = (57.3241399, -4.4420013), (39.4752858, -0.3754667)
def seg_cross(p1, p2, q1, q2):
    """intersection de segments dans le plan (lon, lat) — suffisant à l'échelle de la France/GB"""
    def o(a, b, c): return (b[1]-a[1])*(c[0]-b[0]) - (b[0]-a[0])*(c[1]-b[1])
    a, b, c, d = (p1[1], p1[0]), (p2[1], p2[0]), (q1[1], q1[0]), (q2[1], q2[0])
    o1, o2, o3, o4 = o(a, b, c), o(a, b, d), o(c, d, a), o(c, d, b)
    return (o1*o2 < 0) and (o3*o4 < 0)
def crosses_blade(pts): return any(seg_cross(pts[i], pts[i+1], URQ, VAL) for i in range(len(pts)-1))
def run(names, tag):
    P = [pool[n][:2] for n in names]; n = len(names); M = dist_matrix(P)
    tot = n*(n-1)*(n-2)*(n-3)//2
    print(f"\n######## {tag} : {n} lieux, {tot:,} chaînes possibles")
    L4 = M[:, :, None, None] + M[None, :, :, None] + M[None, None, :, :]      # L4[a,b,c,d]
    I = np.indices((n, n, n, n)); a, b, c, d = I
    valid = (a != b) & (a != c) & (a != d) & (b != c) & (b != d) & (c != d) & (a < d)   # a<d : un sens par chaîne
    Lv = L4[valid]; idx = np.stack([a[valid], b[valid], c[valid], d[valid]], 1)
    out = {}
    for tn, D in TARGETS.items():
        m = (Lv >= D*0.99) & (Lv <= D*1.01)
        rows = [(float(l), *map(int, ix)) for l, ix in zip(Lv[m], idx[m])]
        nb = sum(1 for r in rows if not crosses_blade([P[i] for i in r[1:]]))
        print(f"D={D:7.2f} ({tn:28s}): {len(rows):5d} chaînes dans ±1 % ({100*len(rows)/tot:.2f} % du total) ; sans croiser la lame : {nb}")
        out[tn] = rows
    rnd = random.Random(6); fr = []
    for _ in range(40):
        D = rnd.uniform(200, 500); fr.append(int(np.count_nonzero((Lv >= D*0.99) & (Lv <= D*1.01))))
    print(f"CONTRÔLE : 40 valeurs D aléatoires dans [200, 500] km -> nombre de chaînes ±1 % : min {min(fr)}, médiane {int(np.median(fr))}, max {max(fr)}")
    return out, names, M, P
if __name__ == "__main__":
    o1, names, M, P = run(CORE, "noyau thématique AVEC Carnac absent (44 lieux max)")
    names2 = [c for c in CORE if c in ("Clermont", "Cluny", "Cadouin", "Cîteaux", "Clairvaux", "Chartres", "Conques", "Compostelle", "Canterbury", "Caerleon",
              "Cadbury Castle (Camelot)", "Carcassonne", "Caen", "Chinon", "Cahors", "Carlisle", "Colchester", "Cologne", "Constantinople (Sainte-Sophie)")]
    o2, names2, M2, P2 = run(names2, "noyau restreint (19 lieux : liste des joueurs / consigne)")
    for tn in ("Sainte-Chapelle", "Notre-Dame"):
        print(f"\n--- chaînes du noyau restreint dans ±1 % de D({tn})")
        for L, a, b, c, d in sorted(o2[tn], key=lambda r: abs(r[0]-TARGETS[tn])):
            pts = [P2[i] for i in (a, b, c, d)]
            print(f"   L={L:7.2f} ({100*(L/TARGETS[tn]-1):+.2f} %) {'[CROISE LAME]' if crosses_blade(pts) else '             '} {names2[a]} - {names2[b]} - {names2[c]} - {names2[d]}")
    json.dump({tn: [[round(L, 2)] + [names2[i] for i in r] for L, *r in o2[tn]] for tn in o2}, open("solveurB_08_noyau.json", "w", encoding="utf-8"), ensure_ascii=False)
