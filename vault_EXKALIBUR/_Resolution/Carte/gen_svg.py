"""Régénère Carte/traces_valides.svg (visible dans Obsidian) depuis exkalibur_traces_valides.kml.
Relancer après chaque ajout au KML : python Carte/gen_svg.py"""
import re, math, os
D = os.path.dirname(os.path.abspath(__file__))
kml = open(os.path.join(D, "exkalibur_traces_valides.kml"), encoding="utf-8").read()
pms = re.findall(r"<Placemark><name>(.*?)</name>.*?<coordinates>(.*?)</coordinates>", kml, re.S)
LON0, LON1, LAT0, LAT1 = -10.5, 9.0, 37.0, 59.0
W = 900
def xy(lo, la):
    y = math.log(math.tan(math.pi/4+math.radians(la)/2))
    y0 = math.log(math.tan(math.pi/4+math.radians(LAT0)/2)); y1 = math.log(math.tan(math.pi/4+math.radians(LAT1)/2))
    H = W*(y1-y0)/math.radians(LON1-LON0)
    return (lo-LON0)/(LON1-LON0)*W, (y1-y)/(y1-y0)*H, H
H = xy(0, 45)[2]
COL = {"É1": "#8b1a1a", "É4": "#6b4e16", "É5": "#555", "É6": "#1f4e8c", "É7": "#2e7d32", "É8": "#b8860b", "É9": "#7b1fa2", "É10": "#c2185b", "É11": "#ef6c00", "É12": "#2e7d32"}
def col(n):
    for k, c in sorted(COL.items(), key=lambda kc: -len(kc[0])):
        if n.startswith(k) or f"({k}" in n: return c
    return "#333"
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H:.0f}" font-family="Georgia, serif" font-size="10">',
       f'<rect width="{W}" height="{H:.0f}" fill="#f5efe0" stroke="#8a7a5a"/>']
for la in range(40, 59, 5):
    y = xy(0, la)[1]; out.append(f'<line x1="0" x2="{W}" y1="{y:.1f}" y2="{y:.1f}" stroke="#e0d6c0"/><text x="4" y="{y-2:.1f}" fill="#a09070">{la}°N</text>')
for lo in range(-10, 10, 5):
    x = xy(lo, 45)[0]; out.append(f'<line y1="0" y2="{H:.0f}" x1="{x:.1f}" x2="{x:.1f}" stroke="#e0d6c0"/>')
lines, pts = [], []
for n, c in pms:
    cs = [tuple(map(float, p.split(",")[:2])) for p in c.split()]
    (lines if len(cs) > 1 else pts).append((n, cs))
for n, cs in lines:
    d = " ".join(f"{xy(lo, la)[0]:.1f},{xy(lo, la)[1]:.1f}" for lo, la in cs)
    dash = ' stroke-dasharray="5,3"' if "probable" in n or "réserve" in n else ""
    out.append(f'<polyline points="{d}" fill="none" stroke="{col(n)}" stroke-width="2"{dash}><title>{n}</title></polyline>')
for n, cs in pts:
    x, y, _ = xy(*cs[0]); lab = re.sub(r"\s*\[.*?\]", "", n.split(" (")[0])[:34]
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="3" fill="{col(n)}"><title>{n}</title></circle><text x="{x+4:.1f}" y="{y-3:.1f}" fill="#222">{lab}</text>')
ly = 16
for k, c in COL.items():
    out.append(f'<rect x="{W-70}" y="{ly-8}" width="10" height="10" fill="{c}"/><text x="{W-56}" y="{ly}">{k}</text>'); ly += 14
out.append(f'<text x="{W-70}" y="{ly+4}" fill="#555">- - probable</text></svg>')
open(os.path.join(D, "traces_valides.svg"), "w", encoding="utf-8").write("\n".join(out))
print(f"{len(lines)} tracés, {len(pts)} points → traces_valides.svg")
