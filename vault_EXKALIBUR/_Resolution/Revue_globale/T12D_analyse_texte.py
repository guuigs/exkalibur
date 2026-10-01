# -*- coding: utf-8 -*-
"""T12D — analyse formelle du texte de l'énigme 12."""
import re, unicodedata, itertools, collections

TEXTE = """Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. Le roi avait rejoint les fées, et laissé son épée aux portes d'Avalon. L'épée, évidemment. L'épée, depuis toujours ! Là était la dernière clé de la quête du Graal. Tombée par trois fois, elle était revenue là où elle n'avait jamais cessé d'être. Tout commence et tout s'achève. J'entends le chant retentir. J'ai fait une dernière veille au chemin de rempart, et l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau. Dans la clairière, à la jonction des chemins, j'ai suivi à senestre les eaux enchantées jusqu'à la grande roche, puis fis dix pas au nord, autant à l'est. Arrivé à la souche-majesté, je fis huit derniers pas, et ma boussole suivait le jour dernier. Là, tu trouveras la coupe du charpentier."""

TITRE = "Ad vitam aeternam"
TITRES = ["In Principio","Terra incognita","Ecce Homo","Rex dei gratia","Lux in tenebris",
          "Libera nos a malo","Sub rosa","Ultima cena","Noli me tangere","Omnia vincit amor",
          "Consummatum est","Ad vitam aeternam"]

def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

# phrases : découpage sur . ! ? (le point d'abréviation n'existe pas ici)
phrases_raw = re.split(r"(?<=[.!?])\s+", TEXTE.strip())
print("=== NB DE PHRASES ===", len(phrases_raw))
for i,p in enumerate(phrases_raw,1):
    print(f"  P{i:02d} [{len(p)} car.] {p}")

mots = re.findall(r"[A-Za-zÀ-ÿœŒ'’-]+", TEXTE)
mots_lc = [m.lower() for m in mots]
print("\n=== NB DE MOTS (tout le texte) ===", len(mots))
print("  mot 3  =", mots[2], " | mot 11 =", mots[10])

lettres = [c for c in TEXTE if c.isalpha()]
print("=== NB DE LETTRES ===", len(lettres))
print("  lettre 3  =", lettres[2], " | lettre 11 =", lettres[10])

# initiales de phrases
init_phrases = [p.strip()[0] for p in phrases_raw if p.strip()]
print("\n=== ACROSTICHE (initiales des phrases) ===", " ".join(init_phrases))

# initiales des mots
init_mots = [m[0] for m in mots]
print("=== INITIALES DES MOTS ===", " ".join(init_mots))
# finales des mots
fin_mots = [m[-1] for m in mots]
print("=== FINALES DES MOTS ====", " ".join(fin_mots))

# mots par phrase, 3e et 11e mot de chaque phrase
print("\n=== MOTS PAR PHRASE + 3e/11e mot ===")
for i,p in enumerate(phrases_raw,1):
    mm = re.findall(r"[A-Za-zÀ-ÿœŒ'’-]+", p)
    m3 = mm[2] if len(mm)>=3 else "-"
    m11 = mm[10] if len(mm)>=11 else "-"
    print(f"  P{i:02d} ({len(mm):2d} mots) | 3e={m3!r} 11e={m11!r}")

# lettres par phrase
print("\n=== LETTRES PAR PHRASE ===")
for i,p in enumerate(phrases_raw,1):
    ll = [c for c in p if c.isalpha()]
    print(f"  P{i:02d} : {len(ll)} lettres")

# 12 titres
print("\n=== TITRES : initiales, 3e et 11e ===")
for i,t in enumerate(TITRES,1):
    t_let = strip_acc(t).replace(" ","").replace("-","")
    m = t_let
    print(f"  T{i:02d} [{len(m):2d} lettres] {t!r:28} -> {m} | 3e={m[2] if len(m)>=3 else '-'} 11e={m[10] if len(m)>=11 else '-'}")
init_titres = [t.strip()[0] for t in TITRES]
print("  INITIALES TITRES:", " ".join(init_titres), " =>", "".join(init_titres))
print("  3e titre =", TITRES[2], "| 11e titre =", TITRES[10])

# palindromes
def is_pal(s):
    s = strip_acc(s.lower())
    s = "".join(c for c in s if c.isalpha())
    return len(s)>=3 and s==s[::-1]
print("\n=== MOTS PALINDROMES ===", [m for m in mots if is_pal(m)])

# anagrammes de phrases clés
print("\n=== ANAGRAMMES (lettres triées) ===")
groupes = ["Dieu sut se montrer favorable","dix stades romains","la coupe du charpentier",
           "souche majeste","souche-majesté","astre glorieux","jour dernier",
           "troisieme et onzieme","les troisieme et onzieme","Ad vitam aeternam",
           "derniere cle de la quete du Graal"]
for g in groupes:
    g2 = strip_acc(g.lower())
    g2 = "".join(c for c in g2 if c.isalpha())
    srt = "".join(sorted(g2))
    print(f"  {g!r:38} -> {srt}")

# décompte des lettres du titre
print("\n=== TITRE lettre à lettre ===")
t2 = strip_acc(TITRE.lower()).replace(" ","")
for i,c in enumerate(t2,1):
    print(f"  {i:2d} {c}")

# fréquence des lettres du texte
print("\n=== FRÉQUENCE LETTRES (texte) ===")
cnt = collections.Counter(c.lower() for c in lettres)
print("  ", " ".join(f"{k}:{v}" for k,v in sorted(cnt.items())))

# 'dix stades romains' -> 10 unités ; test rangs 3/11 sur des séquences
print("\n=== RANGS 3/11 SUR DIVERSES SÉQUENCES ===")
seqs = {
 "mots": mots, "lettres": lettres, "phrases": phrases_raw,
 "titres": TITRES, "initiales_titres": init_titres,
}
for name, seq in seqs.items():
    a3 = seq[2] if len(seq)>=3 else None
    a11 = seq[10] if len(seq)>=11 else None
    print(f"  {name:18} : 3e={a3!r}  11e={a11!r}")

# mots en position 3 et 11, et ce qui les sépare (distance en mots)
print("\n=== ENTRE mot 3 et mot 11 (comptage) ===")
print("  mots[3:11] =", mots[3:11])
print("  écart indices =", 11-3)
