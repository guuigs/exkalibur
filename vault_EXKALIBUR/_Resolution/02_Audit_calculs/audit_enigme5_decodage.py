"""Audit Phase 0 : test de la piste 'Table ronde de Winchester' (Enigme 5, 1re ligne de code).
Hypothese testee : 'a.b' = chevalier n°a (liste des 24 noms peints sur la Table de Winchester,
graphie telle que notee par Guilhem), lettre n°b. Deux variantes : espaces comptes / ignores.
ATTENTION : la liste et sa graphie viennent des notes de Guilhem, pas d'une photo de la table ;
l'ordre officiel des noms sur la table reste a verifier (source primaire).
"""
import sys
sys.stdout.reconfigure(encoding="utf-8")
KNIGHTS = ["galahallt", "launcelot deulake", "gauen", "pcyvale", "lyonell", "trystram delyens",
           "garethe", "bedwere", "blubrys", "lacotemale tayle", "lucane", "plomyd", "lamorak",
           "bors de ganys", "safer", "pelleus", "kay", "ectorde marys", "dagonet", "degore",
           "brumear", "lybyus dyscovy", "alynore", "mordrede"]
# NB : Guilhem a note 'Iyonell' (I majuscule) ; lu ici comme 'lyonell' (l minuscule), a verifier.
CODE = "6.4 - 2.9 - 1.2 - 5.4 - 23.7 - 14.9 - 1.1 - 24.6 - 9.7"
pairs = [tuple(map(int, p.strip().split("."))) for p in CODE.split("-")]
assert len(KNIGHTS) == 24
for label, prep in [("espaces ignores", lambda s: s.replace(" ", "")), ("espaces comptes", lambda s: s)]:
    out = []
    for k, l in pairs:
        name = prep(KNIGHTS[k - 1])
        out.append(name[l - 1] if l <= len(name) else "?")
    print(f"{label}: {''.join(out).upper()}   detail: " + ", ".join(f"{k}.{l}->{KNIGHTS[k-1]!r}" for k, l in pairs))
