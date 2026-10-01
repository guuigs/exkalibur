"""Solveur B / É6 — 3) recherche combinatoire de chaînes de 4 C (A-B-C-D, ordre quelconque, sens indifférent, sans lieu répété)
dont la longueur orthodromique totale est à ±1 % de D.
Pool A : liste curatée (solveurB_C_coords.json : Wikipedia en + carte Guilhem) + compléments Wikipedia (Conques, Les Andelys, Caldicot).
Pool B : geonames cities15000 (toutes villes > 15 000 hab. dont le nom commence par C), FR+GB+BE+CH+ES+IT+DE+LU+NL ; source geonames.org (CC-BY).
Cibles D : Tour->Battle->X pour X in {Sainte-Chapelle, Notre-Dame, Vincennes, Saint-Denis, Chartres ...}.
"""
import sys, json, itertools, time
import numpy as np
sys.path.insert(0, "."); from solveurB_geo import *
T = (51.5081124, -0.0759493); B = wiki_coords(["Battle Abbey"])["Battle Abbey"][:2]
X = wiki_coords(["Sainte-Chapelle", "Notre-Dame de Paris", "Sainte-Chapelle de Vincennes", "Saint-Denis Basilica", "Chartres Cathedral"])
def D_of(x): return hav(T, B) + hav(B, x[:2])
TARGETS = {"Sainte-Chapelle": D_of(X["Sainte-Chapelle"]), "Notre-Dame": D_of(X["Notre-Dame de Paris"]),
           "Sainte-Chapelle de Vincennes": D_of(X["Sainte-Chapelle de Vincennes"]), "Saint-Denis": D_of(X["Saint-Denis Basilica"]),
           "Chartres": D_of(X["Chartres Cathedral"]) }
print("Cibles D (km):", {k: round(v, 2) for k, v in TARGETS.items()})

def load_poolA():
    d = json.load(open("solveurB_C_coords.json", encoding="utf-8"))
    extra = wiki_coords(["Conques-en-Rouergue", "Les Andelys", "Caldicot"])
    d["Conques"] = [extra["Conques-en-Rouergue"][0], extra["Conques-en-Rouergue"][1], "Conques-en-Rouergue", "Ste Foy"]
    d["Château-Gaillard (Les Andelys)"] = [extra["Les Andelys"][0], extra["Les Andelys"][1], "Les Andelys", "château"]
    d["Caldicot"] = [extra["Caldicot"][0], extra["Caldicot"][1], "Caldicot", "château"]
    for k in ("Caister", "Camlann", "Chalon", "Cambrai2", "Colchester2", "Clunia2", "Cambrai/Compiègne", "Canterbury (ville)", "Chertsey2", "Cîteaux-Vougeot"):
        d.pop(k, None)
    # dédoublonnage par coordonnées (<1 km)
    keep = {}
    for k, v in d.items():
        if all(hav(v[:2], w[:2]) > 1.0 for w in keep.values()): keep[k] = v
    return keep

def load_poolB(countries=("FR", "GB", "BE", "CH", "ES", "IT", "DE", "LU", "NL")):
    out = {}
    for line in open("solveurB_cities15000.tsv", encoding="utf-8"):
        f = line.split("\t")
        if f[8] in countries and f[1].upper().startswith("C"):
            out[f"{f[1]} ({f[8]})"] = [float(f[4]), float(f[5]), "geonames", f[14]]
    return out

def dist_matrix(P):
    n = len(P); la = np.radians([p[0] for p in P]); lo = np.radians([p[1] for p in P])
    dla = la[:, None]-la[None, :]; dlo = lo[:, None]-lo[None, :]
    h = np.sin(dla/2)**2 + np.cos(la)[:, None]*np.cos(la)[None, :]*np.sin(dlo/2)**2
    return 2*R*np.arcsin(np.sqrt(h))

def chains_in_tol(names, P, lo, hi, collect=True):
    """toutes chaînes a-b-c-d (4 lieux distincts, dédoublonnées par sens) avec lo <= L <= hi. Renvoie liste (L, a,b,c,d)."""
    n = len(P); M = dist_matrix(P); res = []; cnt = 0
    for b in range(n):
        for c in range(n):
            if b == c: continue
            mid = M[b, c]
            if mid > hi: continue
            # a et d : dist(a,b)+mid+dist(c,d) in [lo,hi]
            s = lo - mid; e = hi - mid
            ab = M[:, b][:, None]; cd = M[c, :][None, :]
            tot = ab + cd
            ok = (tot >= s) & (tot <= e)
            ok[b, :] = False; ok[c, :] = False; ok[:, b] = False; ok[:, c] = False
            np.fill_diagonal(ok, False)
            ia, id_ = np.nonzero(ok)
            if not collect:
                cnt += len(ia); continue
            for a, d in zip(ia, id_):
                if (a, b, c, d) < (d, c, b, a):   # évite le doublon inverse
                    res.append((float(ab[a, 0] + mid + cd[0, d]), a, b, c, d))
    return res if collect else cnt // 2

if __name__ == "__main__":
    for label, pool in (("A (curée)", load_poolA()), ("B (geonames C, 9 pays)", load_poolB())):
        names = list(pool); P = [pool[k] for k in names]
        print(f"\n===== Pool {label} : {len(names)} lieux (paires-chaînes non ordonnées ≈ {len(names)**4//2:,})")
        for tn, D in TARGETS.items():
            t0 = time.time(); r = chains_in_tol(names, P, D*0.99, D*1.01, collect=label.startswith('A'))
            nr = len(r) if label.startswith('A') else r
            print(f"D={D:7.2f} ({tn:28s}) ±1 % -> {nr:7d} chaînes  ({time.time()-t0:.1f}s)")
            if label.startswith("A") and tn in ("Sainte-Chapelle", "Notre-Dame"):
                r.sort(key=lambda t: abs(t[0]-D))
                json.dump([[round(t[0], 2)] + [names[i] for i in t[1:]] for t in r], open(f"solveurB_chaines_A_{tn.replace(' ', '_')}.json", "w", encoding="utf-8"), ensure_ascii=False)
