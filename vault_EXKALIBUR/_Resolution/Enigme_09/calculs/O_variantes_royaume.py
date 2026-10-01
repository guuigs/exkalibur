"""É9 Noli me tangere — VARIANTES du « royaume » (demande de Guilhem : sans la ligne Carnac → Stonehenge de l'É5).
Pour chaque lecture (garde, royaume) on calcule la croisée, puis deux règles de sortie :
  (a) « vers l'Est » strict : 340,9 km plein Est (loxodromie, cap 90°), communes en C à ≤ 5 km du point ;
  (b) « vers l'Est » large : anneau 340,9 km ± 1 %, cap 45-135°, en listant les lieux C « notables » (liste fixée AVANT calcul)
      + le nombre total de communes en C dans l'anneau (le bruit de fond).
Coordonnées des communes : base officielle (T1data/communes.json, centres), aucune coordonnée inventée pour les lieux notables."""
import json, math, sys
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088; D4C = 340.9
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2); x = math.cos(la1)*math.sin(la2)-math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return math.degrees(math.atan2(y, x)) % 360
def v(p):
    la, lo = map(math.radians, p); return (math.cos(la)*math.cos(lo), math.cos(la)*math.sin(lo), math.sin(la))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def norm(a): n = math.sqrt(sum(x*x for x in a)); return tuple(x/n for x in a)
def ll(u): return (math.degrees(math.asin(u[2])), math.degrees(math.atan2(u[1], u[0])))
def inter(a1, a2, b1, b2):
    x = norm(cross(norm(cross(v(a1), v(a2))), norm(cross(v(b1), v(b2)))))
    c, c2 = ll(x), ll(tuple(-t for t in x))
    return c if hav(c, a1) < hav(c2, a1) else c2
def on_seg(p, a, b, tol=1.0): return hav(a, p)+hav(p, b)-hav(a, b) < tol
def gc_at_lon(a, b, lon):
    # point du grand cercle (a,b) à une longitude donnée
    n = norm(cross(v(a), v(b))); lo = math.radians(lon)
    lat = math.atan(-(n[0]*math.cos(lo)+n[1]*math.sin(lo))/n[2]); return (math.degrees(lat), lon)
def east_rhumb(p, d):
    return (p[0], p[1]+math.degrees(d/(R*math.cos(math.radians(p[0])))))
P = {"SteChapelle": (48.855375, 2.3449609), "Rennes": (48.1117, -1.6836), "Lorient": (47.7494, -3.3799),
     "León": (42.5994383, -5.5671632), "Foix": (42.965574, 1.604881), "Urquhart": (57.3241399, -4.4420013),
     "Valence": (39.4752858, -0.3754667), "Tintagel": (50.6672813, -4.7585053), "Silchester": (51.3538459, -1.1005385),
     "Westminster": (51.4993695, -0.1272993), "Tour": (51.5081124, -0.0759493), "Battle": (50.9143, 0.487),
     "Carnac": (47.5918383, -3.0835991), "Stonehenge": (51.178882, -1.826215)}
# ---- croisées candidates (royaume ≠ ligne É5), chacune avec sa justification textuelle
CRO = {}
CRO["B. garde É7 × lame É1 (croisée de l'épée : garde/lame, à Brocéliande)"] = inter(P["SteChapelle"], P["Lorient"], P["Urquhart"], P["Valence"])
CRO["C. garde É7 × chemin du Conquérant É6 (il devient roi : Tour→Battle→Sainte-Chapelle) = Sainte-Chapelle"] = P["SteChapelle"]
CRO["D. garde É7 × frontière du royaume de Bretagne (Bretagne/Maine, lon ≈ −1,02 ; ± 3 km)"] = gc_at_lon(P["SteChapelle"], P["Rennes"], -1.02)
CRO["E. garde É1 × lame É1 (croisée d'origine de l'épée, Pyrénées)"] = inter(P["León"], P["Foix"], P["Urquhart"], P["Valence"])
CRO["F. garde É1 × royaume É5 (contrôle)"] = inter(P["León"], P["Foix"], P["Carnac"], P["Stonehenge"])
CRO["G. garde É7 × chemin royal É4 prolongé (Tintagel–Silchester)"] = inter(P["SteChapelle"], P["Lorient"], P["Tintagel"], P["Silchester"])
CRO["H. garde É7 × chemin royal É4 prolongé (Silchester–Westminster)"] = inter(P["SteChapelle"], P["Lorient"], P["Silchester"], P["Westminster"])
CRO["A. RÉFÉRENCE garde É7 × royaume É5 (Carnac–Stonehenge)"] = inter(P["SteChapelle"], P["Lorient"], P["Carnac"], P["Stonehenge"])
com = json.load(open(r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Enigme_06/calculs/T1data/communes.json", encoding="utf-8"))
# Clé = « nom (département) » : plusieurs communes portent le même nom (ex. Chambord 27/41, Cravant 45/89).
pts = {f'{c["nom"]} ({c["code"][:2]})': (c["centre"]["coordinates"][1], c["centre"]["coordinates"][0]) for c in com if c.get("centre")}
Cpts = {n: p for n, p in pts.items() if n.upper().startswith(("C", "Ç"))}
base = lambda k: k.rsplit(" (", 1)[0]
# lieux C notables, liste figée avant calcul (noms de communes exacts de la base)
NOTABLE = ["Chartres", "Chambord", "Chinon", "Chaumont-sur-Loire", "Cheverny", "Châteaudun", "Cléry-Saint-André", "Cormery",
           "Candes-Saint-Martin", "Chauvigny", "Charroux", "Conques", "Carcassonne", "Cahors", "Cluny", "Clermont-Ferrand",
           "Chalon-sur-Saône", "Châlons-en-Champagne", "Compiègne", "Coucy-le-Château-Auffrique", "Chantilly", "Caen", "Cherbourg-en-Cotentin",
           "Colmar", "Chaumont", "Cîteaux", "Clairvaux-les-Lacs", "Collioure", "Céret", "Cadillac", "Cognac", "Chenonceaux",
           "Châteauroux", "Châtellerault", "Cunault", "Chaource", "Crécy-en-Ponthieu", "Coutances", "Conches-en-Ouche", "Caudebec-en-Caux",
           "Courtenay", "Chablis", "Cravant", "Corbeil-Essonnes", "Carnac", "Carhaix-Plouguer", "Combourg", "Cancale"]
miss = [n for n in NOTABLE if not any(base(k) == n for k in pts)]
print("Notables absents de la base :", miss or "aucun")
for lab, X in sorted(CRO.items()):
    inEU = 35 < X[0] < 60 and -12 < X[1] < 10
    print(f"\n=== {lab}\n    croisée {X[0]:.4f}, {X[1]:.4f}" + ("" if inEU else "  → HORS ZONE DE JEU (pas de croisement réel) : ÉCARTÉ"))
    if not inEU: continue
    near = sorted((hav(X, p), n) for n, p in pts.items())[:2]
    print(f"    commune la plus proche : {near[0][1]} ({near[0][0]:.1f} km)")
    E = east_rhumb(X, D4C)
    ce = sorted((hav(E, p), n) for n, p in Cpts.items())[:3]
    print(f"    (a) plein Est 340,9 km → {E[0]:.4f}, {E[1]:.4f} ; C les plus proches : " + " ; ".join(f"{n} {d:.1f} km" for d, n in ce))
    ring = [(n, hav(X, p), brg(X, p)) for n, p in Cpts.items() if abs(hav(X, p)-D4C) <= 0.01*D4C and 45 <= brg(X, p) <= 135]
    nb = [(n, d, b) for n, d, b in ring if base(n) in NOTABLE]
    print(f"    (b) anneau ±1 %, cap 45-135° : {len(ring)} communes en C ; notables : " +
          (" ; ".join(f"{n} {d:.1f} km cap {b:.0f}°" for n, d, b in sorted(nb, key=lambda t: t[2])) or "aucun"))
    near2 = sorted(((abs(hav(X, pts[k])-D4C), k, hav(X, pts[k]), brg(X, pts[k])) for k in pts if base(k) in NOTABLE))[:3]
    print("        notables les plus proches de 340,9 km (tout cap) : " + " ; ".join(f"{n} {d:.1f} km cap {b:.0f}°" for _, n, d, b in near2))
