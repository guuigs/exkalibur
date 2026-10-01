"""Extraction ciblée de la FAQ officielle de l'auteur (faq.unsolvedhunts.com) : tout ce qui touche l'énigme 6
(Libera nos a malo) et ses liens (4 C, tour krak, champ de bataille, lieu très sainte, partie, enluminure 6).
Sortie : Enigme_06/faq_e6.md (citations exactes, référence FAQxx-nnn)."""
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "faq_officielle_auteur.json"), encoding="utf-8"))
THEMES = {"#LIBERANOSAMALO", "#C", "#ENLUMINURE6"}
PAT = re.compile(r"libera|quatre c|4 c|\bles c\b|\bdes c\b|\bun c\b|\bdeux c\b|krak|champ de bataille|hastings|"
                 r"tr[èe]s sainte|recueillir|preux contre dieux|observe la partie|la partie|commencera le p[èe]re|"
                 r"finiront les cieux|enluminure 6|sixi[èe]me [ée]nigme|[ée]nigme 6|[ée]nigme six|clermont|urbain|"
                 r"croisade|s[ée]pulcre|coupe de vie|enchanteur|forces occultes|m[êe]me distance", re.I)
rows = [v for k, v in sorted(d.items()) if v["theme"] in THEMES or PAT.search(v["q"] + " " + v["a"])]
out = os.path.join(HERE, "..", "Enigme_06", "faq_e6.md")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", encoding="utf-8") as f:
    f.write("# FAQ officielle de l'auteur : extraits liés à l'énigme 6\n\n")
    f.write("Source : https://faq.unsolvedhunts.com/?chasse=exkalibur (récupérée le 29/09/2026). "
            "Q = question d'un joueur (hypothèse), R = réponse de l'auteur [OFFICIEL].\n\n")
    for v in rows:
        f.write(f"- **{v['ref']}** `{v['theme']}` — Q : {v['q']}\n  - R : {v['a']}\n")
print(len(rows), "entrées ->", os.path.normpath(out))
