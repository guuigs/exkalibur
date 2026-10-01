# T4 A4: autour de "PIERRE GROS" et "LE CHENE LA ROCHE ET LE VIVIER" (cadastre + BD TOPO)
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import gzip
u="https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/38/38426/cadastre-38426-lieux_dits.json.gz"
j=json.loads(gzip.decompress(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=90).read()))
for f in j["features"]:
    c=cen(f["geometry"]); d=hav(TA,c)
    if d<1.2: print("LD %.2f km %3.0f° %-40s %s pts=%d"%(d,brg(TA,c),f["properties"]["nom"],f["geometry"]["type"],len(_pts(f["geometry"]))))
P=(45.43208,6.03398); V=(45.42827,6.03232)
print("tour->PierreGros %.0f m brg %.0f ; tour->Chene Roche Vivier %.0f m"%(hav(TA,P)*1000,brg(TA,P),hav(TA,V)*1000))
print("Pierre Gros -> Vivier %.0f m"%(hav(P,V)*1000))
# hydro, sentiers, detail autour de chaque point (<=500 m)
for L in ["troncon_hydrographique_12km","detail_hydrographique_12km","surface_hydrographique_12km","plan_d_eau_12km","detail_orographique_12km","toponymie_12km","construction_ponctuelle_12km","lieu_dit_non_habite_12km"]:
    try: F=load(L)
    except Exception as e: print(L,"absent"); continue
    for f in F:
        g=f["geometry"]; pts=_pts(g)
        dm=min(hav(P,(q[1],q[0])) for q in pts)
        if dm<=0.5:
            p=f["properties"]; print(L,"%.0f m"%(dm*1000),{k:p[k] for k in p if k in("toponyme","nature","nom_1","graphie","cleabs","etat_de_l_objet","persistance","nom_collaboratif","toponyme_1") and p[k]})
