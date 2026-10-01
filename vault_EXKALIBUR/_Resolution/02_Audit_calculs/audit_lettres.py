"""Audit Phase 0 : controles 'lettres' sur les pistes existantes (enigmes 2 et 3).
Objectif : verifier si les reponses notees par Guilhem produisent un motif de lettres,
et tester une variante (Octave au lieu d'Auguste, Odyssee au lieu d'Homere).
"""
import sys, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
def norm(s): return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").upper()

print("## Enigme 2 - initiales de la charade")
guilhem = ["Troie", "Richard", "Auguste", "Icare", "Alexandre", "Noé", "Homère", "Vercingétorix", "Auguste"]
variante = ["Troie", "Richard", "Octave", "Icare", "Alexandre", "Noé", "Odyssée", "Vercingétorix", "A?"]
for label, L in [("reponses Guilhem", guilhem), ("variante O/O", variante)]:
    print(f"- {label}: {''.join(norm(w)[0] for w in L)}")
print("  cible testee : TROIANOVA (Troia Nova, nom de Londres chez Geoffroy de Monmouth)")
print("  NB : 'Ma septieme, epopee' est au feminin -> une epopee (Odyssee), pas un poete (Homere).")
print("  NB : 'premier de l'Empire de Rome' -> Octave (Auguste = titre pris en -27).")

print("\n## Enigme 3 - carre / place forte en 8 lettres")
couples = [("Tristan", "Iseult"), ("Lancelot", "Guenièvre")]
init = "".join(norm(a)[0] + norm(b)[0] for a, b in couples)
target = "TINTAGEL"
rest = list(target)
for c in init: rest.remove(c)
print(f"- initiales des couples : {init} ; place forte : {target} ({len(target)} lettres)")
print(f"- lettres de {target} non couvertes par {init} : {''.join(rest)} (= les 'NTAE' de Guilhem)")
print("  -> le mecanisme 'Complete le carre' n'est PAS encore explique : 4 lettres restent orphelines.")
