# T4 notes
## REPRISE
- Fait: rien (démarrage). Brief lu.
- En cours: lecture SYNTHESE/T1/T2
- Prochaines: A) blocs erratiques / roches (OSM, BD TOPO, cadastre) ; B) parcelles ONF (WFS capacités)
- Écarté: (rien)

### MàJ après A3 (cadastre)
- FAIT: cadastre lieux-dits: "PIERRE GROS" (45.43208,6.03398) 0,44 km NE de la tour; "LE CHENE LA ROCHE ET LE VIVIER" 0,13 km ESE; "LE ROCHAT" 1,42 km S; ROCHE MORTE 3,07 km SSW (Pontcharra); "PIRRE GROSSE" 5,7 km E. BD TOPO: Lycée Pierre de Terrail (Bayard = Pierre Terrail) 1,39 km.
- Overpass: api.de donne 406 sans Accept, 504 sinon (surcharge). Script T4_A2_osm.py à relancer.
- WFS caps: pas de couche ONF parcelles; seules BDTOPO_V3:foret_publique, BDFORETV1 (resu_bdv1_shape), ObsForets..., forêts "monterritoire". 
- FAIT (A4): lieu-dit cadastral "LE CHENE LA ROCHE ET LE VIVIER" à 134 m ESE de la tour (vivier = étang à poissons ; chêne ; roche) + "AVALON" (lieu-dit, 90 m N) + "PIERRE GROS" 442 m NE. À explorer: géométrie, ruisseau, propriété.
- Overpass down (504) – réessayer une fois en fin.
- FAIT (B1): SOURCE TROUVÉE: WFS ONF http://ws.carmencarto.fr/WFS/105/ONF_Forets, couche PARC_PUBL_FR (GML 3.1.1, WFS 1.1.0, BBOX lat,lon,lat,lon,EPSG:4326). Attributs: iidtn_frt (id forêt), llib_frt (nom), ccod_prf (code parcelle, ex "K" = LETTRE!). Forêt communale de Saint-Maximin = F19836X (parcelle 'K' vue à 45.41,6.048).
- Suite: T4_B2_parcelles_all.py: tout télécharger (±10 km), lister codes par forêt, calcul 3→11.
## REPRISE
- Fait: A1 (BD TOPO), A3 (cadastre), A4; B1 source ONF OK. Overpass HS (504).
- En cours: B2 téléchargement parcelles + calcul.
- Suite: rapport, test hasard; A: lecture métaphorique; relance Overpass.
- Écarté: rien encore
- FAIT (B2): 505 parcelles ONF dans ±10km (t4_parc_onf.json). Saint-Maximin = 16 parcelles LETTRES A–P (3e=C, 11e=K); Pontcharra A–V; Moutaret A–J (10 seulement, pas de K); Barraux A–N; Ste-Marie-du-Mont A–E; Glapigneux 1–9. Numériques: Chapareillan 1–28, Allevard 1–35, Saint-Hugon, etc. Calcul 3→11 à faire: T4_B3.

## REPRISE (final)
- Fait: A1-A6, B1-B3, T4_rapport.md écrit.
- Piste vivante: lieu-dit cadastral LE CHENE LA ROCHE ET LE VIVIER (15 m de la tour, retenue 10318 m2).
- Écarté: parcelles ONF (244 paires, bruit 1,2 pourcent; Saint-Maximin = lettres A-P; C->K = 2022/1786 m).
- Non fait: Overpass (HS), scieries/ponts en bois, LiDAR.
