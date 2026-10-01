# -*- coding: utf-8 -*-
"""T12D — extraire les réponses COMPLÈTES des FAQ clés."""
import json, unicodedata
Z = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/"
def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

d = json.load(open(Z + "Communaute/faq_officielle_auteur.json", encoding="utf-8"))
items = []
def walk(o):
    if isinstance(o, dict):
        if "q" in o: items.append(o)
        else:
            for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(d)

# rechercher des sous-chaînes dans q
targets = [
    "aurait-on pu écrire", "séparer le troisième", "en ligne droite", "treizième",
    "genre", "masculin", "féminin", "une étape", "deux étapes", "intermédiaire",
    "palindrome", "anagramme", "pont virgule", "point virgule",
    "traduite en deux", "en quatre mots", "philosophie de vie",
    "coupe de charpentier", "coupe du charpentier", "anachronisme",
    "nom du lieu", "département", "arrondissement", "étage", "stade de foot",
    "amphithéâtre", "stade romain", "étape du tour", "ligne de bus",
]
seen = set()
for t in targets:
    tn = strip_acc(t.lower())
    for it in items:
        qn = strip_acc(str(it.get("q",""))).lower()
        an = strip_acc(str(it.get("a",""))).lower()
        if tn in qn or tn in an:
            ref = it.get("ref","?")
            if ref in seen: continue
            seen.add(ref)
            print(f"\n--- {ref} [{it.get('theme','')}] ---")
            print("Q:", str(it.get("q","")))
            print("A:", str(it.get("a","")))
