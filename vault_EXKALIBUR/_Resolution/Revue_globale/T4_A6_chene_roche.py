# T4 A6: le lieu-dit "LE CHENE LA ROCHE ET LE VIVIER" : géométrie, hydro proche, taux de hasard
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import gzip
from shapely.geometry import Polygon, Point
kx=111320*math.cos(math.radians(45.43)); ky=110574
def xy(p): return ((p[0]-TA[1])*kx,(p[1]-TA[0])*ky)
allld=[]
for code in ['38426','38314','73151','38439','38078','38418','73276','38417','38075','38163','73294','73021','38100','38062','38466','73082','73141','73215','73324','38006']:
    try:
        u=f"https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/{code[:2]}/{code}/cadastre-{code}-lieux_dits.json.gz"
        j=json.loads(gzip.decompress(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=90).read()))
        allld+= [(f["properties"]["nom"],f["geometry"]) for f in j["features"]]
    except Exception as e: print(code,"ERR",e)
print("lieux-dits chargés:",len(allld))
T=Point(0,0)
for nm,g in allld:
    if nm.startswith("LE CHENE LA ROCHE"):
        ring=g["coordinates"][0]; P=Polygon([xy(p) for p in ring])
        print(nm,"aire %.2f ha ; distance tour->polygone %.0f m ; bbox(m)"%(P.area/1e4,P.distance(T)),[round(v) for v in P.bounds], "centroïde",[round(v) for v in (P.centroid.x,P.centroid.y)])
        cc=cen(g); print("  centroïde lat,lon %.5f,%.5f"%cc)
        Pg=P
# hydro BD TOPO proche du polygone
for L in ["troncon_hydrographique_12km","surface_hydrographique_12km","detail_hydrographique_12km","plan_d_eau_12km"]:
    for f in load(L):
        pts=_pts(f["geometry"]); 
        dm=min(Pg.distance(Point(xy(q))) for q in pts)
        if dm<=300: p=f["properties"]; print(L,"%.0f m"%dm,p.get("nature"),p.get("toponyme") or p.get("nom_1") or "",p.get("persistance",""))
# taux de hasard: lieux-dits 'roche|pierre|rocher|roc' à <= 134 m d'un point tiré au hasard dans la zone
RX=re.compile(r"\bROCHE|PIERRE|ROCHER|\bROC\b|ROCS|CAILLOU|BLOC",re.I)
K=[nm for nm,g in allld if RX.search(nm)]; print("lieux-dits roche/pierre dans 20 communes:",len(K),"/",len(allld))
d=[hav(TA,cen(g)) for nm,g in allld if RX.search(nm)]
print("à <=0.5 km de la tour:",sum(1 for x in d if x<=.5),"; à <=7.5 km:",sum(1 for x in d if x<=7.5))
A=math.pi*7.5**2; dens=sum(1 for x in d if x<=7.5)/A
print("densité %.3f /km² ; proba d'en avoir ≥1 à <=0.134 km (hasard) = %.2f %% ; à <=0.5 km = %.1f %%"%(dens,100*(1-math.exp(-dens*math.pi*.134**2)),100*(1-math.exp(-dens*math.pi*.5**2))))
ch=[(hav(TA,cen(g)),nm) for nm,g in allld if re.search(r"CHENE|VIVIER",nm) ]
ch.sort(); print("lieux-dits CHENE/VIVIER (plus proches):",[(round(a,2),b) for a,b in ch[:8]])
