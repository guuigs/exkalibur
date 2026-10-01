"""É10 Omnia vincit amor : vérification indépendante de la lecture communautaire (Machrie Moor / Eilean Donan).
Chaîne testée :
  1. « Rome et Amour. Nomme-les. » → ROMA + AMOR (palindrome : « l'une autour de l'Amour, l'autre autour de Rome », qui tournoient et « reviennent »).
  2. « Respecte la règle à la lettre, et prononce le nom de la Terre du 10e père (_) » → Règle du Temple (Hugues de Payns, É8) ;
     10e « père » cité au concile de Troyes (1129) = évêque de Châlons → C (FAQ05-011 : lieu de son « travail »).
  3. « Prononce enfin le nom de Dieu. Garde ses trois premières lettres (___) » → IEH (IEHOVA, forme latine de YHWH ; FAQ05-085 : pas en français).
  4. Anagramme des 12 lettres → un endroit sur l'île au sud (FAQ05-098), « celles qui entourent le roi » (FAQ07-224).
  5. Château de la gardienne = au nord de l'île (FAQ05-159) ; crypto de l'enluminure (FAQ06-113) : bannière « FAC ET SPERA » = devise du clan Matheson,
     fondateur légendaire d'Eilean Donan (Wikipedia).
  6. Distance île → gardienne, à vol d'oiseau (FAQ06-172), réutilisée dans Consummatum est (FAQ03-224)."""
import math, sys
from collections import Counter
sys.stdout.reconfigure(encoding="utf-8")
R = 6371.0088
def hav(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    h = math.sin((la2-la1)/2)**2+math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))
def brg(a, b):
    la1, lo1, la2, lo2 = map(math.radians, (*a, *b))
    y = math.sin(lo2-lo1)*math.cos(la2); x = math.cos(la1)*math.sin(la2)-math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return math.degrees(math.atan2(y, x)) % 360
L = lambda s: Counter(c for c in s.upper() if c.isalpha())
print("== 1-4. Anagramme")
pool = L("ROMA") + L("AMOR") + L("C") + L("IEH")
for cible in ["MACHAIRE MOOR", "MACHRIE MOOR", "AM MACHAIRE"]:
    t = L(cible); print(f"  {cible:14s} : {'EXACTE' if t == pool else 'non'}  (manque {dict(t - pool)}, reste {dict(pool - t)})")
print("  Variante « lettres communes » ROMA seul + C + IEH :", "EXACTE" if L("ROMACIEH") == L("MACHRIEMOOR") else "non")
print("  Variante « JEH » (Jehovah) :", "EXACTE" if L("ROMAAMORCJEH") == L("MACHAIREMOOR") else "non")
print("\n== 2. 10e « père » au concile de Troyes (ordre de la liste Wikipédia FR « Concile de Troyes (1129) »)")
peres = ["légat Matthieu d'Albano", "archev. Reims", "archev. Sens", "év. Chartres", "év. Soissons", "év. Troyes", "év. Orléans",
         "év. Auxerre", "év. Meaux", "év. Châlons-sur-Marne", "év. Laon", "év. Beauvais", "év. Paris"]
for i, p in enumerate(peres[:11], 1): print(f"  {i:2d}. {p}" + ("   ← 10e : terre = CHÂLONS → C" if i == 10 else ""))
print("  NB : ordre à confirmer sur le texte latin du prologue de la Règle (la liste Wikipédia peut différer).")
print("\n== 5-6. Géographie")
MM = (55.540829, -5.313655)    # Machrie Moor Stone Circles (Wikipedia)
ED = (57.27402778, -5.51611111)  # Eilean Donan (Wikipedia)
d = hav(ED, MM)
print(f"  Eilean Donan → Machrie Moor : {d:.2f} km, cap {brg(ED, MM):.1f}° (sud = 180°) ; île d'Arran au sud du château : {'oui' if 150 < brg(ED, MM) < 210 else 'non'}")
print("\n== « Compte-les » (objets non vivants près du roi, FAQ07-053 ; sert plus tard, FAQ07-151) : candidats, Wikipedia")
for k, n in [("cercles de pierres visibles (MM1-5 + MM11)", 6), ("MM5 « Fingal's Cauldron Seat » (siège du roi Fingal) : 8 + 15 blocs", 23),
             ("MM5 cercle intérieur", 8), ("MM5 cercle extérieur", 15), ("MM4 : blocs de granite", 4)]:
    print(f"  {n:3d}  {k}")
