"""É7 Sub rosa : vérification du tracé de la « nouvelle garde » (consensus Discord) + test du hasard.
Chaîne logique testée :
  - « Bayeux Evad. Ecfv » = initiales de la tapisserie de Bayeux, scène 18 : « Et Venerunt Ad Dol. Et Conan Fuga Vertit »,
    suivie du mot « REDNES » (Rennes) : c'est la « complétion » (FAQ03-256 : pas de traduction, une complétion).
  - « la déroute devant le Conquérant » = la fuite de Conan devant Guillaume, de Dol vers Rennes.
  - « Depuis le lieu très saint » = Sainte-Chapelle (acquis en É6) ; « suis la déroute » = passe par Rennes (FAQ03-095).
  - Tracé en droite prolongée (FAQ04-026) ; « à travers les bois » = Brocéliande (Paimpont) ; « s'achève à l'Orient » = Lorient.
Mesures : écart de Paimpont et de Lorient à la droite SC → Rennes (orthodromie, R = 6371,0088 km) ;
nul : on tire des « points de déroute » au hasard (communes FR à 250-400 km de SC, secteur ouest) et on compte
combien de droites passent à ≤ 1 km d'une forêt légendaire ET à ≤ 1 km d'une commune au nom « Orient »/est."""
import math, json, random, sys
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088
def rad(p): return math.radians(p[0]), math.radians(p[1])
def hav(a, b):
    la1, lo1 = rad(a); la2, lo2 = rad(b)
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def brg(a, b):
    la1, lo1 = rad(a); la2, lo2 = rad(b)
    y = math.sin(lo2-lo1)*math.cos(la2); x = math.cos(la1)*math.sin(la2)-math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return math.degrees(math.atan2(y, x)) % 360
def xtrack(a, b, p):
    """distance signée (km) de p au grand cercle a->b, et distance le long de la droite"""
    d13 = hav(a, p)/R; t13 = math.radians(brg(a, p)); t12 = math.radians(brg(a, b))
    xt = math.asin(math.sin(d13)*math.sin(t13-t12))*R
    at = math.acos(max(-1, min(1, math.cos(d13*1)/math.cos(xt/R))))*R
    return xt, at
SC = (48.855375, 2.3449609)          # Sainte-Chapelle
P = {
 "Dol-de-Bretagne (cathédrale)": (48.5496, -1.7575),
 "Rennes (cathédrale)": (48.1117, -1.6836),
 "Dinan (château)": (48.4526, -2.0472),
 "Paimpont (abbaye, Brocéliande)": (48.0213, -2.1712),
 "Paimpont (centre commune)": (48.0327, -2.1793),
 "Val sans Retour (Tréhorenteuc)": (47.9951, -2.2862),
 "Lorient (centre)": (47.7494, -3.3799),
 "Lorient (Enclos du port, arsenal)": (47.7485, -3.3530),
 "Forêt d'Orient (lac, Aube)": (48.2640, 4.3310),
}
print("== Droites depuis la Sainte-Chapelle")
for via in ["Rennes (cathédrale)", "Dol-de-Bretagne (cathédrale)", "Dinan (château)"]:
    print(f"\n-- SC → {via} (cap {brg(SC, P[via]):.2f}°, {hav(SC, P[via]):.1f} km)")
    for n, p in P.items():
        if n == via: continue
        xt, at = xtrack(SC, P[via], p)
        if at > 0 and abs(xt) < 30: print(f"   {n:38s} écart {xt:+7.2f} km, à {at:6.1f} km de SC")
# ---- test du hasard
random.seed(7)
com = json.load(open(r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Enigme_06/calculs/T1data/communes.json", encoding="utf-8"))
pts = [((c["centre"]["coordinates"][1], c["centre"]["coordinates"][0]), c["nom"]) for c in com if c.get("centre")]
brocs = [P["Paimpont (abbaye, Brocéliande)"], P["Val sans Retour (Tréhorenteuc)"]]
lor = P["Lorient (centre)"]
cand = [p for p, n in pts if 150 < hav(SC, p) < 400 and p[1] < 0.5]   # « points de déroute » plausibles à l'ouest
N = len(cand); hit_b = hit_l = hit_both = 0
for p in cand:
    xb = min(abs(xtrack(SC, p, b)[0]) for b in brocs)
    xl, al = xtrack(SC, p, lor)
    hb = xb <= 1.0; hl = abs(xl) <= 1.0 and al > 0
    hit_b += hb; hit_l += hl; hit_both += (hb and hl)
print(f"\n== Nul : {N} communes à l'ouest de SC (150-400 km) prises comme « point de déroute »")
print(f"   droite à ≤ 1 km de Brocéliande : {hit_b} ({100*hit_b/N:.2f} %)")
print(f"   droite à ≤ 1 km de Lorient     : {hit_l} ({100*hit_l/N:.2f} %)")
print(f"   les deux                       : {hit_both} ({100*hit_both/N:.3f} %)")
print("   → Rennes est imposé par le texte (complétion REDNES), il n'est pas choisi après coup.")
# ---- relation avec la garde d'É1 (León → Foix) et la lame (Urquhart → Valence)
L1, F1 = (42.5994383, -5.5671632), (42.965574, 1.604881)
U, V = (57.3241399, -4.4420013), (39.4752858, -0.3754667)
g_new = brg(SC, lor); g_old = brg(L1, F1); lame = brg(U, V)
print(f"\n== Géométrie de l'épée : cap nouvelle garde SC→Lorient {g_new:.1f}° ; ancienne garde León→Foix {g_old:.1f}° ; lame Urquhart→Valence {lame:.1f}°")
def ang(a, b):
    d = abs(a-b) % 180; return min(d, 180-d)
print(f"   angle nouvelle garde / ancienne garde : {ang(g_new, g_old):.1f}° ; nouvelle garde / lame : {ang(g_new, lame):.1f}°")
xt, at = xtrack(U, V, SC); print(f"   la Sainte-Chapelle est à {xt:+.1f} km de l'axe de la lame")
print(f"   longueur SC → Lorient : {hav(SC, lor):.1f} km ; longueur León → Foix : {hav(L1, F1):.1f} km")
