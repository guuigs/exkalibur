# -*- coding: utf-8 -*-
"""T12-B (suite) : tests numeriques systematiques vs nombres de la chasse."""
import math, itertools

sites = {
 "MM1": (191200, 632390), "MM2": (191140, 632410), "MM3": (191020, 632440),
 "MM4": (191000, 632350), "MM5": (190870, 632340), "MM6": (190730, 632370),
 "MM7": (190630, 632530), "MM8": (190570, 632370), "MM9": (190500, 632400),
 "MM10":(190060, 632650), "MM11":(191210, 632420), "MM12":(191000, 632400),
 "Bally":(192440, 632250),
}
def d(a,b):
    return math.hypot(sites[a][0]-sites[b][0], sites[a][1]-sites[b][1])
def brg(a,b):  # from N clockwise
    e1,n1=sites[a]; e2,n2=sites[b]
    return (math.degrees(math.atan2(e2-e1, n2-n1)) + 360) % 360

keys = list(sites.keys())
print("### DISTANCES ~ 185 m (1 stade, +/-1% = 183-187) :")
for i,j in itertools.combinations(keys,2):
    x=d(i,j)
    if 183 <= x <= 187: print(f"  {i}-{j} = {x:.1f} m")
print("### DISTANCES ~ 1850 m (+/-1% = 1832-1868) :")
for i,j in itertools.combinations(keys,2):
    x=d(i,j)
    if 1832 <= x <= 1868: print(f"  {i}-{j} = {x:.0f} m")
print("### BEARINGS ~ 64.99 / 72.09 / 352.90 deg (+/-0.6) :")
for i,j in itertools.permutations(keys,2):
    b=brg(i,j)
    for t in (64.99, 72.09, 352.90, 25.01, 17.09):
        if abs(b-t) < 0.6: print(f"  {i}->{j} = {b:.2f} deg (~{t})")

# comptages de pierres par site
counts = {"MM1":11, "MM2":3, "MM3":9, "MM4":4, "MM5":23, "MM6":2, "MM7":1,
          "MM8":1, "MM9":1, "MM10":12, "MM11":10, "MM12":12, "Bally":3}
print()
print("### Comptages de pierres :", counts)
print("### Recherche cible 1850 par arithmetique simple sur les comptages :")
for k,v in counts.items():
    for f in [10,11,12,13,23,80.43,185/10]:
        pass
# produits/sommes simples
vals = list(counts.values())
print("  somme des comptages =", sum(vals))
print("  23 x 80.43 = %.1f ;  23 x 10 = %d ;  23 x 8 = %d ; 23 x 15 = %d" % (23*80.43, 23*10, 23*8, 23*15))
print("  11 (MM1) x 168.2 = %.0f ; 10 (MM11) x 185 = %d ; 9 (MM3) x 205.6 = %.0f" % (11*168.2, 10*185, 9*205.6))
print("  12 (MM12) x 154.2 = %.0f" % (12*154.2))

# lettres D=500 C=100 X=10 (romains) : combinaisons
print()
print("### Lecture romaine D=500, C=100, X=10 :")
print("  D+C+X = 610 ;  D+C = 600 ; D-C = 400 ; D/X = 50 ; C/X = 10 ; D/C = 5")
print("  DCX = 610 ; si '?'=I(1) -> DCXI=611 ; si '?'=V(5) -> 615 ; si '?'=L(50) -> 660")
print("  610 vs 606.74 km (E11 D.pi) : ecart %.2f %%" % (100*abs(610-606.74)/606.74))
print("  610 vs 607.69 km (StPalais->TdA) : ecart %.2f %%" % (100*abs(610-607.69)/607.69))

# lecture cartes : valet=11, dame=12, roi=13
print()
print("### Lecture cartes (valet=11, dame=12, roi=13) :")
print("  D=Dame=12 ; si C=Cavalier=11 (jeu ancien) ; X=10 (dix) ; '?'=9 -> suite 12,11,10,9")
print("  ranks possibles 12,11,10,9 -> somme=42 ; moyenne=10.5")

# distance MM3-MM11 : 1 stade ? verifier vs 185 et vs les 'pas'
d311 = d("MM3","MM11")
print()
print("### MM3 <-> MM11 = %.1f m  (185 m = 1 stade -> ratio %.3f)" % (d311, d311/185))
print("  10 x 185 = %d m ; 10 x 191 = %d m" % (1850, 10*191))

# le '?' : 1,3,5 -> suite impaire -> 7 ; MM7 = pierre levee 1.6m
print()
print("### si '?'=7 (suite impaire 1,3,5,7) -> MM7 :")
for k in ["MM1","MM3","MM5"]:
    print(f"  {k} <-> MM7 = {d(k,'MM7'):.0f} m")
