# -*- coding: utf-8 -*-
"""T12D — full FAQ for translation / 'Dieu sut' / 'favorable' / author identity."""
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
targets = ["anglaise","n'est pas traduit","est rest","Dieu sut","favorable","montrer favorable",
           "Etienne","Picand","Unsolved","auteur du","identité","auteur des énigmes","qui est l'auteur",
           "Naga","Elixir","Contremarque","Destrier","Fatum","autre chasse","chasses"]
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
