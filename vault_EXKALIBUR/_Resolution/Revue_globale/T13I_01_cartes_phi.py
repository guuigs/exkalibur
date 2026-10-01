# T13I_01_cartes_phi.py — énigme 12, piste T13-I (enluminure 11 = mini jeu de cartes)
# Archive des calculs : triangle 1/√5/3, nombre d'or, croix 11x11, jeu de cartes, géo (départs candidats).
# Sortie : T13I_01_cartes_phi.out.txt
import math, json
R = 6371.0088

def hav(a,b):
    la1,lo1,la2,lo2 = map(math.radians, (*a,*b))
    h = math.sin((la2-la1)/2)**2 + math.cos(la1)*math.cos(la2)*math.sin((lo2-lo1)/2)**2
    return 2*R*math.asin(math.sqrt(h))*1000

def brg(a,b):
    la1,lo1,la2,lo2 = map(math.radians, (*a,*b))
    y=math.sin(lo2-lo1)*math.cos(la2); x=math.cos(la1)*math.sin(la2)-math.sin(la1)*math.cos(la2)*math.cos(lo2-lo1)
    return (math.degrees(math.atan2(y,x))+360)%360

def dest(a,brg_d,dist_m):
    la1,lo1=map(math.radians,a); b=math.radians(brg_d); d=dist_m/1000
    la2=math.asin(math.sin(la1)*math.cos(d/R)+math.cos(la1)*math.sin(d/R)*math.cos(b))
    lo2=lo1+math.atan2(math.sin(b)*math.sin(d/R)*math.cos(la1), math.cos(d/R)-math.sin(la1)*math.sin(la2))
    return (math.degrees(la2), math.degrees(lo2))

phi = (1+math.sqrt(5))/2
print("phi =", phi, " phi^2 =", phi**2, " sqrt5 =", math.sqrt(5))
print("cos(72deg) = %.6f ; (sqrt5-1)/4 = %.6f" % (math.cos(math.radians(72)), (math.sqrt(5)-1)/4))
print("angle d'or = 360/phi^2 =", 360/phi**2)

print("\n-- Triangle 1, sqrt5, 3 --")
s = sorted([1, math.sqrt(5), 3]); a,b,c = s
print("sides:", [round(x,4) for x in s], "ineq:", a+b, ">", c, "->", a+b>c)
A = math.degrees(math.acos((b*b+c*c-a*a)/(2*b*c)))
B = math.degrees(math.acos((a*a+c*c-b*b)/(2*a*c)))
C = math.degrees(math.acos((a*a+b*b-c*c)/(2*a*b)))
print("angles: %.3f %.3f %.3f (sum %.3f)" % (A,B,C,A+B+C))
print("triangle droit 1,2,sqrt5 : angle opp 2 = atan2(2,1) = %.4f deg" % math.degrees(math.atan2(2,1)))

print("\n-- Croix 11x11 --")
print("bras = 11 pierres, centre = 6e (vide). R aux distances 1,1,5,5 du centre -> positions 1,5,7,11")
print("3e et 11e : positions 3 et 11, separes de 8 cases")
print("10 stades separent 3e/11e -> 1 case = 10/8 = 1.25 stade =", 1850/8, "m")
print("si 1re->11e = 10 stades -> 1 case = 1 stade ; 3->11 = 8 stades =", 8*185, "m")

print("\n-- Jeu de cartes (rangs) --")
print("52 cartes: As=1,2..10, Valet=11, Dame=12, Roi=13  -> 3='trois', 11='Valet'")
print("32 (piquet): 7..10,V,D,R,As -> pas de '3'")
print("tarot mineur: As=1..10, Valet=11, Cavalier=12, Dame=13, Roi=14 -> 11=Valet, 12=Cavalier(=chevalier)")
print("valets FR: trefle=Lancelot, coeur=La Hire, carreau=Hector, pique=Ogier/Hogier")
print("dames FR: coeur=Judith, carreau=Rachel, pique=Pallas, trefle=Argine")
print("rois FR: coeur=Charlemagne, carreau=Cesar, pique=David, trefle=Alexandre")

print("\n-- Anchors --")
TA_brief = (45.429083, 6.030808)   # tour d'Avalon (brief vague3)
RR_brief = (45.42977, 6.03118)     # rue du rempart
BA_brief = (45.4242, 6.0179)       # arrivee exacte E11 (brief)
CB_exk   = (45.423611, 6.018889)   # chateau Bayard (exk.py)
for name,coord in [("TourAvalon(brief)",TA_brief),("TourAvalon(exk.py)",(45.4288,6.03078)),
                   ("RueRempart(brief)",RR_brief),("Bayard(exk.py)",CB_exk)]:
    d = hav(coord, BA_brief)
    print("%-20s -> arriveeE11: %8.1f m   d/(1850/phi)=%.4f   d*phi=%7.1f" % (name, d, d/(1850/phi), d*phi))

print("\n-- Anchors vs 10 stades --")
print("1850/phi = %.2f m ; 1850/phi^2 = %.2f m ; 1850*phi = %.2f m" % (1850/phi, 1850/phi**2, 1850*phi))
print("Tour(brief)->arriveeE11 = %.1f m ; x phi = %.1f m (10 stades = 1850)" % (hav(TA_brief,BA_brief), hav(TA_brief,BA_brief)*phi))

print("\n-- E11 angle du dernier chevalier --")
SP = (43.3284, -1.0333)  # Saint-Palais
print("cap SP->Bayard = %.2f deg ; axe lame E1 = 352.90 -> angle = %.2f deg (vs 72 = 360/5)" %
      (brg(SP, BA_brief), (brg(SP,BA_brief)-352.90+360)%360))
