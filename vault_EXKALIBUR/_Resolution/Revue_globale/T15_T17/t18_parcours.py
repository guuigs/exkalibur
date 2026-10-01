# T18 — Parcours à postes numérotés autour de la tour d'Avalon : test « d(3e, 11e) = 1850 m ± 18 m »
# Données d'entrée = valeurs lues dans les fiches/PDF cités dans T18_parcours.md (aucune coordonnée de poste inventée).
import math, itertools, json, random
TA=(45.429083,6.030808)
def hav(a,b,c,d):
    R=6371008.8;p=math.pi/180
    x=math.sin((c-a)*p/2)**2+math.cos(a*p)*math.cos(c*p)*math.sin((d-b)*p/2)**2
    return 2*R*math.asin(math.sqrt(x))
TARGET,TOL=1850,18

# (nom, nb postes, longueur boucle km, lat, lon du départ/centre, source de la distance à la tour)
P=[
 ("Parcours patrimoine Saint-Maximin (PDF Apidae)",9,5.2,45.42911,6.03086),
 ("CO patrimoine Bayard Pontcharra/St-Maximin",10,5.0,45.433749,6.01339),
 ("Parcours santé patrimoine Pontcharra (Isère Outdoor)",11,6.7,45.432275,6.020483),
 ("Parcours thématique Barraux (10 étapes)",10,6.5,45.433704,5.977339),
 ("Parcours thématique Chapareillan (8 étapes)",8,None,45.4585,5.9455),
 ("Sentier forestier Plateau de la Puce, Chapareillan",40,2.3,45.455468,5.949346),
 ("CO patrimoine Allevard village",11,2.5,45.394305,6.075117),
 ("CO ludique Lac de la Mirande, Allevard",11,1.5,45.406998,6.084817),
 ("Randonnée des Hameaux (OSM rel. 2825942)",4,5.0,45.4294,6.0308),
]
print("%-55s %4s %6s %8s  %s"%("parcours","N","L km","d_tour m","borne : 3→11 possible ≥ 1850-18 ?"))
for n,N,L,la,lo in P:
    dt=hav(la,lo,*TA)
    if N<11: v="impossible : pas de 11e poste"
    elif L is None: v="n/a"
    else:
        # borne haute grossière : chemin 3→11 = 8 intervalles ≈ 8/N de la boucle (postes ~équi-répartis) ; la droite ≤ chemin
        seg=8*L*1000/N
        v="chemin 3→11 ≈ %d m (8/%d de %.1f km) -> %s"%(seg,N,L,"exclu (≪1832)" if seg<TARGET-TOL else "non exclu (estimation grossière ; emprise carte ≲ 0,7 km => exclu en pratique pour Allevard)")
    print("%-55s %4d %6s %8d  %s"%(n,N,L,dt,v))

# --- Seul parcours avec positions approximatives (géoréf. du plan sur la trace GPX officielle) : santé Pontcharra
# positions issues de t18_sp_geo.py (± ~30 m, lecture visuelle des pastilles sur le plan)
SP={1:(45.43253,6.02008),2:(45.43661,6.01863),3:(45.43757,6.01632),4:(45.44082,6.01123),5:(45.44298,6.00832),6:(45.44388,6.00721),
    7:(45.45143,6.01029),8:(45.4459,6.01529),9:(45.43643,6.02136),10:(45.43066,6.02384),11:(45.43132,6.02226)}
print("\nSanté Pontcharra (11 bornes, positions APPROXIMATIVES) : d(3,11) = %d m ; d(i,i+8) = %s"%(
    hav(*SP[3],*SP[11]), [round(hav(*SP[i],*SP[i+8])) for i in (1,2,3)]))
allp=[hav(*SP[i],*SP[j]) for i,j in itertools.combinations(SP,2)]
hit=sum(abs(d-TARGET)<=TOL for d in allp)
print("Toutes paires (%d) : min %d  max %d  médiane %d ; paires dans 1850±18 : %d"%(len(allp),min(allp),max(allp),sorted(allp)[len(allp)//2],hit))
# contrôle : proba qu'une distance aléatoire tombe dans ±18 m, pour des distances uniformes sur [0, 2539] (étendue observée)
random.seed(1);M=200000
base=[hav(*SP[random.choice(list(SP))],*SP[random.choice(list(SP))]) for _ in range(M)]
print("Contrôle : fenêtre ±18 m sur distances 0–%d m : %.2f %% par hasard (≈ 36/%d)"%(max(allp),100*36/max(allp),max(allp)))
print("Paires > 1832 m : %d ; d(3,11)=%d m => rejeté (écart %d m)."%(sum(d>TARGET-TOL for d in allp),hav(*SP[3],*SP[11]),1850-hav(*SP[3],*SP[11])))
