# Piste 0 : valeur du stade romain et fenêtre ±1 % pour 10 stades
for nom,s in [("stade romain 185 m (1/8 de mille romain de 1480 m) - VALEUR RETENUE",185.0),("variante 177,6 m (stade attique/olympique)",177.6),("variante 192 m (stade olympique ~192,27 m)",192.0)]:
    d=10*s
    print(f"{nom}: 10 stades = {d:.0f} m ; fenêtre ±1 % = [{d*0.99:.1f} ; {d*1.01:.1f}] m (largeur {d*0.02:.1f} m)")
print("Union des 3 fenêtres:",1776*.99,"->",1920*1.01)
# Aire de l'anneau de recherche autour d'un point A pour 1 850 m ±1 % : 
import math
for d in (1850,1776,1920):
    print(d,"anneau: aire km2 =",round(math.pi*((d*1.01/1000)**2-(d*.99/1000)**2),4),"; largeur",round(d*.02),"m")
