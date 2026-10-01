# -*- coding: utf-8 -*-
"""T12D — recherche par mots-clés dans la FAQ auteur + faq8.txt."""
import json, re, os, unicodedata

Z = r"C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/"
def strip_acc(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")

# ---- charger FAQ ----
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
print("NB entrées FAQ =", len(items))

# clés d'un item
sample = items[0]
print("clés item:", list(sample.keys()), "| exemple:", {k: (str(v)[:40]) for k,v in sample.items()})

KW = ["coupe","charpentier","stade","stades","palindrome","acrostiche","anagramme",
      "double lecture","double sens","initiales","traduit","traduction","coupe du",
      "souche","majeste","astre","clairiere","troisieme et onzieme","troisième et onzième",
      "dix stades","romains","enlum","lettrine"]
for kw in KW:
    kwn = strip_acc(kw.lower())
    hits = []
    for it in items:
        q = strip_acc(str(it.get("q",""))).lower()
        a = strip_acc(str(it.get("a",""))).lower()
        key = str(it.get("theme",""))+"|"+list(it.keys())[0] if "theme" in it else ""
        if kwn in q or kwn in a:
            hits.append((it.get("q",""), it.get("a","")))
    print(f"\n### {kw!r} -> {len(hits)} entrée(s)")
    for q,a in hits[:12]:
        print(f"  Q: {str(q)[:120]}")
        print(f"  A: {str(a)[:160]}")

# ---- faq8.txt : chercher 'coupe', 'stade', 'charpentier', 'palindrome' ----
print("\n\n===== FAQ8.TXT =====")
raw = open(r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/faq8.txt", encoding="utf-8").read()
for kw in ["coupe","charpentier","stade","palindrome","traduit","acrostiche","anagramme","majesté","majeste","souche"]:
    kwn = strip_acc(kw.lower())
    r = strip_acc(raw.lower())
    idxs = [m.start() for m in re.finditer(re.escape(kwn), r)]
    print(f"\n### faq8 {kw!r} -> {len(idxs)} occurrence(s)")
    for i in idxs[:6]:
        print("   ...", raw[max(0,i-120):i+160].replace("\n"," "), "...")
