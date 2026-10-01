# Piste 2b : lettrines E3 (ruines, 2 tours) et C11 (tour + mur crénelé) : fortifications réelles autour d'Avalon/Bayard; couples à 1,85 km ±1 %
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
import json,itertools,collections,re,urllib.parse
print("TA",TA,"CB",CB,"d(TA,CB)=%.3f km"%hav(TA,CB))
# 1. initiales
tit=["Amis aventuriers(intro)","In principio","Terra incognita","Ecce Homo","Rex dei gratia","Lux in tenebris","Libera nos a malo","Sub rosa","Ultima cena","Noli me tangere","Omnia vincit amor","Consummatum est","Ad vitam aeternam"]
print("Initiales:", "".join(t[0] for t in tit[1:]), "| 3e (Ecce Homo)=E, 11e (Consummatum est)=C ; en comptant l'intro : 3e=T, 11e=O")
# 2. natures dans IGN
for layer in ("construction_ponctuelle","batiment","zone_d_activite_ou_d_interet","toponymie","lieu_dit_non_habite"):
    try: fs=load(layer)
    except Exception as e: print(layer,"ERR",e); continue
    c=collections.Counter()
    for f in fs:
        p=f["properties"]; c[str(p.get("nature") or p.get("categorie") or "")]+=1
    print(layer,len(fs),dict(c.most_common(25)))
