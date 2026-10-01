"""Audit Phase 0 : Enigme 5, 2e ligne de code '9 - 1 - 7x9 - 1&2 - 3 - C'.
Hypothese testee (issue de la note de Guilhem '3,14159265358') : chaque nombre = rang d'une DECIMALE de pi
('table parfaitement ronde, a la decimale pres' ; 'eureka' = Archimede). 'x' = produit, '&' = concatenation,
puis A=1..Z=26. 'C' est laisse tel quel.
+ geometrie de l'epee (Enigme 1) : alignement pommeau/poignee/pointe.
"""
import json, math, os, sys
sys.stdout.reconfigure(encoding="utf-8")
DEC = "14159265358979323846"  # decimales de pi (source : constante mathematique, 20 premieres)
d = lambda i: int(DEC[i - 1])
L = lambda n: chr(64 + n)
steps = [("9", d(9)), ("1", d(1)), ("7x9", d(7) * d(9)), ("1&2", int(f"{d(1)}{d(2)}")), ("3", d(3))]
out = ""
for tok, n in steps:
    out += L(n); print(f"{tok:>4} -> {n:>2} -> {L(n)}")
out += "C"; print(f"   C -> C\nMot : {out}")
# Test du hasard : meme regle avec les chiffres de e et de sqrt(2)
for name, s in {"e": "71828182845904523536", "sqrt2": "41421356237309504880"}.items():
    g = lambda i: int(s[i - 1])
    vals = [g(9), g(1), g(7) * g(9), int(f"{g(1)}{g(2)}"), g(3)]
    print(f"controle {name}: {vals} -> " + "".join(L(v) if 1 <= v <= 26 else "?" for v in vals) + "C")

print("\n## Enigme 1 - axe de l'epee")
HERE = os.path.dirname(os.path.abspath(__file__))
C = json.load(open(os.path.join(HERE, "coords.json"), encoding="utf-8"))
R = 6371.0088
def vec(p):
    la, lo = math.radians(p["lat"]), math.radians(p["lon"])
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))
def cross(a, b): return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])
def dot(a, b): return sum(x*y for x, y in zip(a, b))
def norm(a): n = math.sqrt(dot(a, a)); return tuple(x/n for x in a)
def xtrack(p, a, b):  # distance de p au grand cercle (a,b), km (signe = cote)
    n = norm(cross(vec(a), vec(b))); return R * math.asin(dot(vec(p), n))
V, Lo, U = C["Cathédrale de Valence"], C["Grotte de Lombrives"], C["Château d'Urquhart"]
print(f"- Ecart de Lombrives a l'axe Valence->Urquhart : {xtrack(Lo, V, U):.1f} km")
for q in ["Château de Foix", "Château de Montségur"]:
    n1 = norm(cross(vec(C["Cathédrale de León"]), vec(C[q]))); n2 = norm(cross(vec(V), vec(U)))
    x = norm(cross(n1, n2))
    if dot(x, vec(Lo)) < 0: x = tuple(-c for c in x)
    lat, lon = math.degrees(math.asin(x[2])), math.degrees(math.atan2(x[1], x[0]))
    print(f"- Intersection garde (Leon->{q}) x axe (Valence->Urquhart) : {lat:.4f}, {lon:.4f}")
