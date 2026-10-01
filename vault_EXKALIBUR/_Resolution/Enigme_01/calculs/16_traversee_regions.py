"""Enigme 1 - la lame traverse-t-elle vraiment Guyenne, Anjou, Bretagne, Cornouailles,
pays de Galles, mur d'Hadrien (puis Loch Nis) ?

Test 1 (quantitatif) : distance minimale de chaque 'ancre' de region a la ligne, et
 rang de passage le long de la ligne (globe = orthodromie, carte = droite Web Mercator).
Test 2 (objectif) : echantillonnage de la ligne + geocodage inverse OSM Nominatim
 (pays / region administrative) -> sequence reelle des territoires traverses.
"""
import json, math, os, sys, time, urllib.request, urllib.parse
from importlib import import_module
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.stdout.reconfigure(encoding="utf-8")
G = import_module("00_geo")

U = (57.3241399, -4.4420013)      # Chateau d'Urquhart
LO = (42.8232161, 1.616311)       # Grotte de Lombrives
V = (39.4752858, -0.3754667)      # Cathedrale de Valence
RLC = (42.9272475, 2.2627453)

ANCRES = [
    ("Guyenne: Bordeaux", 44.8378, -0.5792), ("Guyenne: Perigueux", 45.1841, 0.7213), ("Guyenne: Agen", 44.2024, 0.6200),
    ("Anjou: Angers", 47.4712, -0.5517), ("Anjou: Saumur", 47.2597, -0.0780),
    ("Bretagne: Rennes", 48.1147, -1.6794), ("Bretagne: Brest", 48.3904, -4.4861), ("Bretagne: St-Malo", 48.6493, -2.0257),
    ("Bretagne: Quimper", 47.9960, -4.1024),
    ("Cornouailles: Truro", 50.2632, -5.0514), ("Cornouailles: Bodmin", 50.4715, -4.6695),
    ("Cornouailles: Land's End", 50.0657, -5.7134), ("Cornouailles: Tintagel", 50.6673, -4.7585),
    ("Galles: Cardiff", 51.4816, -3.1791), ("Galles: Aberystwyth", 52.4143, -4.0836),
    ("Galles: Caernarfon", 53.1399, -4.2732), ("Galles: St Davids", 51.8819, -5.2660),
    ("Mur d'Hadrien: Bowness", 54.9504, -3.2264), ("Mur d'Hadrien: Carlisle", 54.8924, -2.9329),
    ("Mur d'Hadrien: Housesteads", 55.0125, -2.3134), ("Mur d'Hadrien: Newcastle", 54.9783, -1.6178),
    ("Ecosse: Edimbourg", 55.9533, -3.1883), ("Ecosse: Inverness", 57.4778, -4.2247),
    ("Angleterre: Londres", 51.5074, -0.1278), ("Angleterre: Plymouth", 50.3755, -4.1427),
    ("Irlande: Dublin", 53.3498, -6.2603), ("Manche: I. de Wight", 50.6930, -1.3040),
]

def analyse(nom, A, B, mode):
    print("\n" + "=" * 96)
    print(f"### {nom}  ({mode})")
    lg = G.hav(A,B) if mode=='globe' else (G.merc_dist_ground(A,B) if mode=='carte' else 'n/a')
    print(f"  A={A}  B={B}  | longueur {lg}")
    rows = []
    for n, la, lo in ANCRES:
        p = (la, lo)
        if mode == "globe":
            d = G.cross_track(p, A, B); at = G.along_track(p, A, B)
        elif mode == "plate":
            # projection equirectangulaire : x = lon, y = lat ; ecart perpendiculaire DESSINE (en degres)
            # converti en "km de carte" par 111,32 km/degre (ce que mesure une regle sur la carte).
            den = math.hypot(B[1] - A[1], B[0] - A[0])
            d = (((B[1] - A[1]) * (A[0] - p[0]) - (A[1] - p[1]) * (B[0] - A[0])) / den) * 111.320
            at = ((p[1] - A[1]) * (B[1] - A[1]) + (p[0] - A[0]) * (B[0] - A[0])) / den / den * G.hav(A, B)
        else:
            d = G.merc_cross_track(p, A, B)
            # rang de passage : on projette sur le segment Mercator
            (x1, y1), (x2, y2), (xp, yp) = G.m(*A), G.m(*B), G.m(*p)
            at = ((xp - x1) * (x2 - x1) + (yp - y1) * (y2 - y1)) / math.hypot(x2 - x1, y2 - y1) / 1000.0
        rows.append((at, abs(d), n, d))
    rows.sort()
    for at, ad, n, d in rows:
        flag = "TRAVERSE" if ad < 60 else ("a proximite" if ad < 120 else "")
        print(f"    {n:28s} ecart {d:8.1f} km | rang {at:7.0f} km le long de la ligne  {flag}")

print("Sources des ancres : coordonnees OSM/Wikipedia des villes de reference.")
print("Critere 'TRAVERSE' : ecart perpendiculaire < 60 km (largeur typique d'une province historique).")

analyse("Lame pour la ligne de Guilhem (Ligne 5) : Urquhart -> Valence", U, V, "globe")
analyse("Lame pour la ligne de Guilhem (Ligne 5) : Urquhart -> Valence", U, V, "carte")
analyse("Lame 'nee a Lombrives' : Urquhart -> Lombrives", U, LO, "globe")
analyse("Lame 'nee a Lombrives' : Urquhart -> Lombrives", U, LO, "carte")
analyse("Lame (Ligne 5) : Urquhart -> Valence", U, V, "plate")
analyse("Lame 'nee a Lombrives' : Urquhart -> Lombrives", U, LO, "plate")

# ---- geocodage inverse : sequence objective des territoires ----
CACHE = os.path.join(HERE, "reverse_cache.json")
cache = json.load(open(CACHE, encoding="utf-8")) if os.path.exists(CACHE) else {}
def rev(p):
    k = f"{p[0]:.3f},{p[1]:.3f}"
    if k in cache:
        return cache[k]
    u = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&zoom=8&lat=%f&lon=%f" % p
    try:
        d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "exkalibur-audit/1.0"}), timeout=30).read().decode())
        a = d.get("address", {})
        r = (a.get("country", "?"), a.get("state", a.get("region", "")), a.get("county", ""), d.get("name", ""))
    except Exception as e:
        r = ("ERR", str(e)[:40], "", "")
    cache[k] = r; time.sleep(1.05)
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
    return r

if "--rev" in sys.argv:
    print("\n\n" + "#" * 96)
    print("### SEQUENCE DES TERRITOIRES TRAVERSES (geocodage inverse OSM, zoom=8)")
    for nom, A, B, mode in [("Urquhart->Valence", U, V, "globe"), ("Urquhart->Valence", U, V, "carte"),
                            ("Urquhart->Lombrives", U, LO, "globe"), ("Urquhart->Lombrives", U, LO, "carte"),
                            ("Urquhart->Valence", U, V, "plate"), ("Urquhart->Lombrives", U, LO, "plate")]:
        print(f"\n--- {nom} ({mode}) : {40} points")
        seen = []
        for i in range(31):
            f = i / 30
            p = G.interp_gc(A, B, f) if mode == "globe" else (G.merc_interp(A, B, f) if mode == "carte" else (A[0] + f * (B[0] - A[0]), A[1] + f * (B[1] - A[1])))
            c, st, co, nm = rev(p)
            lab = f"{c} / {st} / {co}" + (f" ({nm})" if nm else "")
            if not seen or seen[-1][1] != lab:
                seen.append((f, lab, p))
                print(f"   f={f:4.2f} {p[0]:7.3f},{p[1]:7.3f}  {lab}")
    json.dump(cache, open(CACHE, "w", encoding="utf-8"), ensure_ascii=False)
