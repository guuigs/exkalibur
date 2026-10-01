import json,re,sys
sys.stdout.reconfigure(encoding="utf-8")
d=json.load(open("faq_officielle_auteur.json",encoding="utf-8"))
th=re.compile(r"#C$|LIBERANOSAMALO|NOLIMETANGERE|DERNIERC|AVANTDERNIERC",re.I)
rC=re.compile(r"(?<![A-Za-zÀ-ÿ0-9'’])C(?![A-Za-zÀ-ÿ0-9'’])(?!\s+['’])")
rC2=re.compile(r"(?<![A-Za-zÀ-ÿ0-9'’])C(?=\s*[,.?;:)]|\s+(?:et|ou|de|du|en|est|sont|que|qui|dans|entre|pour|avant|final)\b)")
kw=re.compile(r"quatre\s+C\b|\b4\s*C\b|\b4C\b|\b[3-6]\s*C\b|avant[- ]dernier|dernier\s+C|(cinqui|sixi|troisi|deuxi|premi)[eè]me\s+C|cloche|3-C|Noli me tangere|m[êe]me distance|les\s+C\b|des\s+C\b|ces\s+C\b|chaque\s+C\b|tous\s+les\s+C|autres?\s+C\b|(un|le|ce|ton|mon|notre|nos|tes|mes|au)\s+C\b",re.I)
out=[]
for r,e in d.items():
    t=e["q"]+" "+e["a"]
    why=[]
    if th.search(e["theme"]): why.append("theme")
    if rC.search(t) and (rC2.search(t) or kw.search(t)): why.append("C")
    if kw.search(t): why.append("kw")
    if why: out.append((r,e,why))
out.sort(key=lambda x:x[0])
json.dump(out,open("_C_raw.json","w",encoding="utf-8"),ensure_ascii=False)
print(len(out))
from collections import Counter
print(Counter(e["theme"] for r,e,w in out).most_common(15))
