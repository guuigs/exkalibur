"""Solveur B / É6 — 1) lectures (a) axe prolongé et (b) ligne brisée Tour->Battle->X ; 2) D pour chaque candidat « lieu très Sainte ».
Coordonnées : Tour de Londres = carte Guilhem ; Battle = Wikipedia 'Battle Abbey' (50.915, 0.4858) ; autres = Wikipedia en (API) via cache."""
import sys; sys.path.insert(0, ".")
from solveurB_geo import *
T = (51.5081124, -0.0759493)   # carte Guilhem
BATTLE_ABBEY = wiki_coords(["Battle Abbey"])["Battle Abbey"][:2]
BATTLE_TOWN  = wiki_coords(["Battle, East Sussex"])["Battle, East Sussex"][:2]
BATTLE_ALT   = (50.9143, 0.4870)  # valeur de geo_e6.py
print("== Axe Tour -> Battle (3 géocodages de Battle)")
for n, B in (("Battle Abbey (Wikipedia)", BATTLE_ABBEY), ("Battle ville (Wikipedia)", BATTLE_TOWN), ("geo_e6.py", BATTLE_ALT)):
    print(f"{n:28s} {B}  d={hav(T,B):.2f} km cap={cap(T,B):.3f}°")
B = BATTLE_ABBEY; AX = cap(T, B)

cand = {  # titre Wikipedia en : nature
 "Sainte-Chapelle": "Paris, île de la Cité, Passion",
 "Notre-Dame de Paris": "Paris, île de la Cité",
 "Sainte-Chapelle de Vincennes": "Vincennes",
 "Saint-Denis Basilica": "nécropole royale",
 "Sainte-Baume": "massif, grotte Marie-Madeleine",
 "Saintes, Charente-Maritime": "Saintes",
 "Chartres Cathedral": "voile de la Vierge",
 "Vézelay Abbey": "Ste-Madeleine, prêche 2e croisade",
 "Mont-Saint-Michel": "île / Michel",
 "Lindisfarne": "Holy Island (île sainte, île à marée)",
 "Iona": "île sainte celtique",
 "Rosslyn Chapel": "Rose-line, mythe Templier/Graal",
 "Glastonbury Abbey": "Avalon / Graal",
 "Canterbury Cathedral": "Becket",
 "Reims Cathedral": "sacre des rois",
 "Sens Cathedral": "Sens", "Auxerre Cathedral": "Auxerre",
 "Fontainebleau": "Fontainebleau", "Sainte-Marie-de-la-Mer": "Saintes-Maries-de-la-Mer",
 "Saintes-Maries-de-la-Mer": "Saintes-Maries (Marie-Madeleine, Sara)",
 "Amiens Cathedral": "Amiens (tête de saint Jean-Baptiste)",
 "Rouen Cathedral": "Rouen", "Cluny Abbey": "(C, exclu par FAQ03-099 si C)",
 "Sainte-Anne-d'Auray": "pèlerinage breton", "Sainte-Anne-de-Beaupré": "hors-jeu",
 "Jerusalem": "Jérusalem, Saint-Sépulcre", "Church of the Holy Sepulchre": "Saint-Sépulcre",
 "Rome": "Rome", "Santiago de Compostela Cathedral": "Compostelle",
 "Avalon": "?",
}
co = wiki_coords(list(cand))
print("\n== D candidats (a) point sur l'axe prolongé ; (b) polyligne Tour->Battle->X")
print(f"{'lieu':34s} {'d(T,X)':>8s} {'T-B-X':>8s} {'écart/axe':>9s} {'abscisse':>8s}  cap(T,X)")
rows = []
for t, nat in cand.items():
    v = co[t]
    if not v: print(f"{t:34s} PAS DE COORD"); continue
    X = v[:2]; d = hav(T, X); pb = hav(T, B)+hav(B, X)
    print(f"{t:34s} {d:8.2f} {pb:8.2f} {xtrack(T,B,X):+9.2f} {along(T,B,X):8.1f}  {cap(T,X):.2f}   ({nat}; {v[0]:.4f},{v[1]:.4f})")
print("\n== (a) Lecture 'axe prolongé' : écart latéral (km) de l'axe Tour->Battle au lieu X, et écart D si D=T-X")
print("   Si X est à 1,9 km de l'axe, la précision annoncée (0,42 km) dépend de l'axe choisi : Battle est à 0,42 km de la droite T-SC,")
print("   mais SC est à ~%.2f km de la droite T-Battle (rapport des distances 342/77)." % xtrack(T, B, co['Sainte-Chapelle'][:2]))
print("\n== Points de l'axe prolongé à distance D de la Tour")
for D in (300, 320, 341.6, 345.2, 360, 380, 400, 429, 450, 500, 550, 600):
    la, lo = dest(T, AX, D); print(f"D={D:6.1f}  {la:.4f}, {lo:.4f}")
