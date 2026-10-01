"""É8 Ultima cena : test du chaînage communautaire, avec balayage des unités et des points de départ.
Chaîne : pétales de la « fleur de Patmos » (rose de l'Apocalypse, Sainte-Chapelle) = 18 ; numéro 1 = Tibère († 37 apr. J.-C.)
 → 18 × 37 = 666 (nombre de la Bête, Ap 13,18 ; « deux monstres » = les deux bêtes d'Ap 13) → au carré : 443 556 unités.
Trajet : depuis « l'île sainte », à vol d'oiseau (FAQ03-011), en direction de Jérusalem (FAQ04-145 : une seule Jérusalem),
on s'arrête « en cours de chemin » (FAQ03-153) sur l'humble serviteur du Graal.
Test : pour chaque (départ, unité), on calcule le point d'arrivée et la distance aux candidats (Payns, Mergey, Troyes...).
Nul : on remplace 666 par tous les produits p × a (p de 5 à 24 pétales, a de 1 à 1400) et on regarde combien tombent à ≤ 2 km de Payns."""
import math, sys
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
def dest(a, t, d):
    la1, lo1 = rad(a); t = math.radians(t); dr = d/R
    la2 = math.asin(math.sin(la1)*math.cos(dr)+math.cos(la1)*math.sin(dr)*math.cos(t))
    lo2 = lo1+math.atan2(math.sin(t)*math.sin(dr)*math.cos(la1), math.cos(dr)-math.sin(la1)*math.sin(la2))
    return math.degrees(la2), math.degrees(lo2)
JER = (31.7780, 35.2354)            # Saint-Sépulcre, Jérusalem
DEP = {
 "Île de la Cité (centre)": (48.8547, 2.3470),
 "Sainte-Chapelle": (48.855375, 2.3449609),
 "Notre-Dame de Paris": (48.8530, 2.3499),
 "Île Saint-Louis": (48.8517, 2.3567),
 "Westminster (Thorney Island)": (51.4993695, -0.1272993),
 "Lindisfarne (Holy Island)": (55.6690, -1.8010),
}
CAND = {"Payns (église)": (48.3833, 3.9750), "Payns (commanderie / musée Hugues de Payns)": (48.3806, 3.9670),
        "Mergey": (48.3547, 4.0122), "Troyes (cathédrale)": (48.2990, 4.0786), "Clairvaux": (48.1467, 4.7883)}
UNITS = {"pied romain 0,2957 m": 0.2957, "pied anglais 0,3048 m": 0.3048, "pied du roi 0,32484 m": 0.32484,
         "coudée 0,444 m": 0.444, "pas simple 0,74 m": 0.74, "pas commun 0,812 m": 0.812, "pas romain double 1,4786 m": 1.4786}
N = (18*37)**2
print(f"18 × 37 = {18*37} ; au carré = {N:,} unités".replace(",", " "))
print("\n== Départ × unité → point d'arrivée (cap vers Jérusalem) ; candidats à ≤ 10 km")
for dn, d0 in DEP.items():
    t = brg(d0, JER)
    for un, u in UNITS.items():
        dkm = N*u/1000; X = dest(d0, t, dkm)
        near = sorted((hav(X, c), cn) for cn, c in CAND.items())
        hits = [f"{cn} {dd:.2f} km" for dd, cn in near if dd <= 10]
        if hits: print(f"  {dn:28s} | {un:26s} | {dkm:7.2f} km, cap {t:6.2f}° → {X[0]:.4f},{X[1]:.4f} | {'; '.join(hits)}")
# Nul : autres produits p×a, départ Île de la Cité, pied du roi
d0 = DEP["Île de la Cité (centre)"]; t = brg(d0, JER); P = CAND["Payns (église)"]
tot = hit = 0
for u in UNITS.values():
    for p in range(5, 25):
        for a in range(1, 1401):
            dkm = (p*a)**2*u/1000
            if dkm > 3000: break
            tot += 1
            if hav(dest(d0, t, dkm), P) <= 2: hit += 1
print(f"\n== Nul : {tot} combinaisons (pétales 5-24 × année 1-1400 × 7 unités), départ Île de la Cité → {hit} à ≤ 2 km de Payns ({100*hit/tot:.3f} %)")
print(f"   Écart de Payns à la droite Cité → Jérusalem : {abs(math.asin(math.sin(hav(d0,P)/R)*math.sin(math.radians(brg(d0,P)-t)))*R):.2f} km ; distance Cité → Payns {hav(d0,P):.2f} km")
