# T4 B1: parcelles forestières ONF (WFS carmencarto PARC_PUBL_FR, GML) autour de la tour
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
W=r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/'
base="http://ws.carmencarto.fr/WFS/105/ONF_Forets"
d=0.02
tests={
 "latlon4326":f"SRSNAME=EPSG:4326&BBOX={TA[0]-d},{TA[1]-d},{TA[0]+d},{TA[1]+d},EPSG:4326",
 "urn4326":f"SRSNAME=urn:ogc:def:crs:EPSG::4326&BBOX={TA[0]-d},{TA[1]-d},{TA[0]+d},{TA[1]+d},urn:ogc:def:crs:EPSG::4326",
 "lonlat_nocrs":f"BBOX={TA[1]-d},{TA[0]-d},{TA[1]+d},{TA[0]+d}",
}
for k,p in tests.items():
    u=f"{base}?SERVICE=WFS&VERSION=1.1.0&REQUEST=GetFeature&TYPENAME=PARC_PUBL_FR&MAXFEATURES=3&{p}"
    try:
        t=get(u,120); print("##",k,len(t)); print(t[600:2600] if len(t)>800 else t[-200:])
    except Exception as e: print(k,"ERR",e)
