"""Solveur B / É6 — 4) piste de Guilhem : Cluny / Clermont / Cadouin + 4e C. Quel 4e C, quel ordre, donnerait ≈ D ?
Coordonnées Cluny, Clermont, Cadouin : carte Guilhem ; 4e C : pool A (curé) + pool B (geonames C) de solveurB_05_chaines.py.
Résultats : (i) borne inférieure géométrique ; (ii) 4e C candidats ordre par ordre ; (iii) même test avec Carnac (É5) parmi les 4 ; (iv) 5 C avec Carnac."""
import sys, json, itertools
sys.path.insert(0, "."); from solveurB_geo import *
from solveurB_05_chaines import load_poolA, load_poolB, TARGETS
G = {"Cluny": (46.4348054, 4.6585012), "Clermont": (45.7787583, 3.0858573), "Cadouin": (44.8114955, 0.8737598)}
CARNAC = (47.5918383, -3.0835991)
print("== (i) Distances entre les 3 C de Guilhem")
for a, b in itertools.combinations(G, 2): print(f"{a}-{b}: {hav(G[a], G[b]):.2f} km")
lo = hav(G["Cluny"], G["Cadouin"])
print(f"\nInégalité triangulaire : toute chaîne contenant Cluny ET Cadouin est >= {lo:.2f} km (= la chaîne à 3 C, Clermont étant quasi sur la droite).")
for tn, D in TARGETS.items():
    print(f"  cible {tn:30s} D={D:7.2f}  D*1,01={D*1.01:7.2f}  -> {'INCOMPATIBLE' if lo > D*1.01 else 'compatible'} (marge {D*1.01-lo:+.2f} km ; écart relatif de {lo:.2f} à D : {100*(lo/D-1):+.2f} %)")
print("  Sensibilité : un décalage de 1 km sur Cluny ou Cadouin (abbaye vs bourg) suffit à changer la conclusion pour Sainte-Chapelle -> non-discriminant.")

pool = {**load_poolA(), **load_poolB()}
pool = {k: v for k, v in pool.items() if k not in G and all(hav(v[:2], g) > 3 for g in G.values())}
print(f"\n== (ii) 4e C parmi {len(pool)} lieux (ordre libre) ; on garde les chaînes 4 C dans ±1 % de chaque D")
res = {}
for tn, D in TARGETS.items():
    rows = []
    for nm, v in pool.items():
        X = v[:2]
        for perm in itertools.permutations(list(G) + ["X"]):
            pts = [G[p] if p != "X" else X for p in perm]
            L = sum(hav(pts[i], pts[i+1]) for i in range(3))
            if abs(L/D-1) <= 0.01 and perm[0] < perm[-1]:
                rows.append((round(L, 2), round(100*(L/D-1), 2), nm, " - ".join(p if p != "X" else nm for p in perm)))
    rows.sort(key=lambda r: abs(r[1]))
    res[tn] = rows
    print(f"\n-- D={D:.2f} ({tn}) : {len(rows)} solutions (4e C, ordre) dans ±1 %")
    for r in rows[:15]: print(f"   L={r[0]:7.2f} ({r[1]:+.2f} %)  {r[3]}")
json.dump(res, open("solveurB_07_guilhem4e.json", "w", encoding="utf-8"), ensure_ascii=False)

print("\n== (iii) Carnac (É5) comme un des 4 C, avec deux des trois C de Guilhem + 1 libre — ou 3 C Guilhem + Carnac (= 4 C)")
for perm in itertools.permutations(list(G) + ["Carnac"]):
    pts = [G[p] if p != "Carnac" else CARNAC for p in perm]
    L = sum(hav(pts[i], pts[i+1]) for i in range(3))
    if perm[0] < perm[-1]:
        print(f"   {' - '.join(perm):40s} L={L:8.2f}   écart à D(SC)={100*(L/TARGETS['Sainte-Chapelle']-1):+.1f} %")
print("== (iv) 5 C = Carnac + 3 C Guilhem + 1 : non testé ici (le texte dit 4 C ; FAQ03-259 : « ça ne veut pas dire qu'il n'y en a que quatre dans le jeu »).")
