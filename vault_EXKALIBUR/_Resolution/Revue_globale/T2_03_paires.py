# Piste 2b/5 : objets 'Tour, donjon', 'Château', 'Chapelle', 'Clocher', 'Eglise', 'Monument' (IGN) ; couples à 1,85/1,776/1,92 km ±1 % ; test du hasard
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import json,itertools,random,statistics
def cent(g):
    import itertools
    t=g["type"];c=g["coordinates"]
    pts=[]
    def rec(x):
        if isinstance(x[0],(int,float)): pts.append(x)
        else:
            for y in x: rec(y)
    rec(c); return (sum(p[1] for p in pts)/len(pts), sum(p[0] for p in pts)/len(pts))
objs=[]
for f in load("batiment"):
    n=f["properties"].get("nature")
    if n in("Tour, donjon","Château","Chapelle","Eglise"): objs.append((n,f["properties"].get("cleabs"),cent(f["geometry"])))
for f in load("construction_ponctuelle"):
    n=f["properties"].get("nature")
    if n in("Clocher","Croix"): objs.append((n,f["properties"].get("cleabs"),(f["geometry"]["coordinates"][1],f["geometry"]["coordinates"][0])))
for f in load("zone_d_activite_ou_d_interet"):
    n=f["properties"].get("categorie") or f["properties"].get("nature")
    if n in("Monument","Culte chrétien"): objs.append(("Z:"+str(n),f["properties"].get("toponyme") or f["properties"].get("cleabs"),cent(f["geometry"])))
print("objets:",len(objs))
for n in ("Tour, donjon","Château"):
    for o in objs:
        if o[0]==n: print(n,o[1],"%.5f %.5f"%o[2],"d_TA=%.2f d_CB=%.2f"%(hav(TA,o[2]),hav(CB,o[2])))
wins={"185":(1.8315,1.8685),"177.6":(1.7582,1.7938),"192":(1.9008,1.9392)}
for lab,(lo,hi) in wins.items():
    print("\n== fenêtre",lab)
    for kind in (("Tour, donjon","Château","Clocher","Chapelle","Eglise"),):
        S=[o for o in objs if o[0] in kind]
        pairs=[(hav(a[2],b[2]),a,b) for a,b in itertools.combinations(S,2)]
        ok=[p for p in pairs if lo<=p[0]<=hi]
        print("objets fortif/religieux:",len(S),"paires:",len(pairs),"dans fenêtre:",len(ok),"=> taux %.3f"%(len(ok)/len(pairs)))
        for d,a,b in ok: print("  %.4f"%d,a[0],a[1],"|",b[0],b[1])
    # paires impliquant la tour d'Avalon (point TA) et CB avec tous objets
    for ref,name in ((TA,"TA"),(CB,"CB")):
        hits=[(hav(ref,o[2]),o) for o in objs if lo<=hav(ref,o[2])<=hi]
        print(" objets à la fenêtre de",name,":",[(round(d,3),o[0],o[1]) for d,o in hits])
# base rate : anneau de 37 m à 1,85 km autour d'un point, aire / aire du carré 9x9
import math
for lab,(lo,hi) in wins.items():
    ring=math.pi*(hi**2-lo**2); print(lab,"aire anneau %.3f km2 ; fraction du carré 81 km2 = %.4f"%(ring,ring/81))
