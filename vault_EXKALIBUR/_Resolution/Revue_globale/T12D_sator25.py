# -*- coding: utf-8 -*-
"""T12D — carré 5x5 de 'Dieu sut se montrer favorable' + anagrammes ciblés + comptages."""
import re, unicodedata, itertools, collections

def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

# 1) 'Dieu sut se montrer favorable' = 25 lettres ?
p = "Dieu sut se montrer favorable"
pl = [c for c in strip_acc(p.lower()) if c.isalpha()]
print("1) '", p, "' ->", len(pl), "lettres :", "".join(pl))
assert len(pl) == 25
# carré 5x5
sq = [pl[i*5:(i+1)*5] for i in range(5)]
print("Carré 5x5 (lignes):")
for r in sq: print("   ", " ".join(r))
print("Colonnes:")
for c in range(5): print("   ", " ".join(sq[r][c] for r in range(5)))
print("Diag principale:", " ".join(sq[i][i] for i in range(5)))
print("Diag anti     :", " ".join(sq[i][4-i] for i in range(5)))
print("Boustrophedon :", "".join("".join(r) if i%2==0 else "".join(reversed(r)) for i,r in enumerate(sq)))
print("Spirale (lecture SATOR) :", end=" ")
# spirale centre->ext? faire simple : lecture en colimaçon depuis l'extérieur
mat = [list(r) for r in sq]
res = []
while mat:
    res += mat.pop(0)
    if mat and mat[0]:
        for row in mat: res.append(row.pop())
    if mat:
        res += mat.pop()[::-1]
    if mat and mat[0]:
        for row in mat[::-1]: res.append(row.pop(0))
print("".join(res))

# 2) anagrammes ciblés
print("\n2) Anagrammes ciblés")
def letters(s):
    return "".join(sorted(c for c in strip_acc(s.lower()) if c.isalpha()))
def can_make(bag, target):
    b = collections.Counter(bag); t = collections.Counter(target)
    return all(b[k] >= v for k,v in t.items())
bag = pl
for w in ["avalon","breba","breda","isere","grenoble","lune","etoile","soleil","roche",
          "souche","epee","coupe","graal","bois","foret","champ","stade","rempart",
          "majeste","roche","ruisseau","sentier","chemin","bayard","tintagel","ecce homo"]:
    print(f"   '{w}' dans le sac ? {can_make(bag, w)}")

# 3) comptages de lettres des phrases clés
print("\n3) Comptages")
for s in ["dix stades romains","separaient","les troisieme et onzieme",
          "la coupe du charpentier","souche majeste","astre glorieux","jour dernier",
          "Dieu sut se montrer favorable"]:
    ll = [c for c in strip_acc(s.lower()) if c.isalpha()]
    print(f"   {s!r:32} = {len(ll)} lettres")

# 4) texte entier : nb de phrases, mots, lettres
TEXTE = open(r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/T12D_analyse_texte.py",encoding="utf-8").read()
# (déjà calculé) — vérif 138 mots, 12 phrases
print("\n4) Rappel : 12 phrases, 138 mots, 651 lettres (calculé précédemment)")

# 5) les 12 titres -> acrostiche + découpage
TITRES = ["In Principio","Terra incognita","Ecce Homo","Rex dei gratia","Lux in tenebris",
          "Libera nos a malo","Sub rosa","Ultima cena","Noli me tangere","Omnia vincit amor",
          "Consummatum est","Ad vitam aeternam"]
init = [t.strip()[0] for t in TITRES]
print("5) Acrostiche titres =", "".join(init))
print("   ITER =", "iter" in "".join(init).lower(), "(latin : chemin/route/voyage)")
print("   reste après ITER =", "".join(init)[4:])
