# T4 B3: distance 3e -> 11e parcelle (numérotée ou lettre) par forêt ; test du hasard (k,k+8)
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
from collections import defaultdict
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
F=json.load(open(W+'t4_parc_onf.json',encoding='utf-8'))
la0=45.43; kx=111320*math.cos(math.radians(la0)); ky=110574
def xy(p): return ((p[0]-TA[1])*kx,(p[1]-TA[0])*ky)
G=defaultdict(dict)
for f in F:
    polys=[Polygon([xy(p) for p in r]).buffer(0) for r in f["rings"] if len(r)>3]
    if not polys: continue
    # rings exterior seulement (les trous sont rares) -> union
    g=unary_union(polys)
    k=f["code"]; fo=f["nom"]
    G[fo][k]=unary_union([G[fo][k],g]) if k in G[fo] else g
def order(code):
    if code.isdigit(): return int(code)
    if len(code)==1 and code.isalpha(): return ord(code.upper())-64
    return None
LO,HI=1831.5,1868.5  # 10 stades de 185 m +-1 %
def metr(a,b):
    return a.centroid.distance(b.centroid), a.distance(b)
rows=[]; allpairs=[]
for fo,d in G.items():
    od={order(c):(c,g) for c,g in d.items() if order(c) is not None}
    for k in sorted(od):
        if k+8 in od:
            a,b=od[k][1],od[k+8][1]; dc,de=metr(a,b)
            inwin_c=LO<=dc<=HI; inwin_e=LO<=de<=HI
            allpairs.append((fo,k,od[k][0],od[k+8][0],dc,de,inwin_c,inwin_e))
print("Stade 185 m -> fenêtre [%.1f ; %.1f] m"%(LO,HI))
print("\n== Paires (3e,11e) par forêt (ordre 3 et 11 ; lettres: C=3, K=11)")
for r in allpairs:
    if r[1]==3: print("%-55s %s->%s  centroïdes %7.0f m | bords %7.0f m %s%s"%(r[0],r[2],r[3],r[4],r[5],"  <== CENTROIDE DANS LA FENÊTRE" if r[6] else "","  <== BORDS" if r[7] else ""))
n=len(allpairs); nc=sum(1 for r in allpairs if r[6]); ne=sum(1 for r in allpairs if r[7])
print("\n== Test du hasard: toutes paires (k,k+8), toutes forêts: n=%d ; centroïde dans fenêtre: %d (%.1f %%) ; bords: %d (%.1f %%)"%(n,nc,100*nc/n,ne,100*ne/n))
for r in allpairs:
    if r[6] or r[7]: print("  HIT %-50s %s->%s (rangs %d->%d) c=%.0f e=%.0f"%(r[0],r[2],r[3],r[1],r[1]+8,r[4],r[5]))
# Saint-Maximin / Pontcharra : toutes distances entre parcelles (contexte)
for fo in ["Forêt communale de Saint-Maximin","Forêt communale de Pontcharra","Forêt communale du Moutaret","Forêt communale de Chapareillan","Forêt communale de Barraux"]:
    d=G[fo]; print("\n--",fo,"centroïdes (cap/dist depuis tour)")
    for c in sorted(d,key=lambda c:(order(c) or 99)):
        g=d[c].centroid; print("   %s  %5.0f m E, %5.0f m N  (tour->centroïde %.0f m) aire %.1f ha"%(c,g.x,g.y,math.hypot(g.x,g.y),d[c].area/1e4))
