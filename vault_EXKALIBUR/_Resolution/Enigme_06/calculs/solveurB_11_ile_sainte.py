"""Solveur B / É6 — 11) PISTE « ÎLE SAINTE ». La FAQ (tags ULTIMACENA) traite « lieu très sainte » comme « île très sainte / île Sainte » de Ultima cena
(FAQ03-070, 03-288, 03-099, 03-108 ; FAQ03-275 : l'île Sainte est identifiée dans une énigme précédente ; FAQ04-049 : PAS dans Sub rosa ; FAQ04-012 : « toujours une île, à ce jour, oui »).
=> le lieu très Sainte est peut-être une ÎLE. Test : îles/lieux insulaires saints candidats : distance à l'axe Tour->Battle prolongé, abscisse (= D en lecture (a)),
D en lecture (b) polyligne Tour->Battle->X, et écart au cap. Coordonnées Wikipedia (en), cache."""
import sys, time
sys.path.insert(0, "."); from solveurB_geo import *
T = (51.5081124, -0.0759493); B = wiki_coords(["Battle Abbey"])["Battle Abbey"][:2]
titles = ["Île de la Cité", "Lindisfarne", "Iona", "Bardsey Island", "Holy Island, Anglesey", "Mont-Saint-Michel", "Île Saint-Honorat", "Île Sainte-Marguerite (Cannes)", "Île de Sein",
          "Île de Bréhat", "Glastonbury Tor", "Isle of Man", "Skellig Michael", "Île de Groix", "Belle Île", "Île de Batz", "Jersey", "Guernsey", "Lérins Islands",
          "Corsica", "Malta", "Cyprus", "Patmos", "Sainte-Marie, Réunion", "Sainte-Hélène", "Île Saint-Louis", "Bonifacio, Corse-du-Sud", "Île Tibérine", "Sainte-Croix (Switzerland)",
          "Avalon", "Isle of Avalon", "Ynys Enlli", "Île de Ré", "Île d'Yeu", "Île d'Oléron", "Île de Porquerolles", "Île de Port-Cros", "Île du Levant"]
res = wiki_coords(titles[:20]); time.sleep(3); res.update(wiki_coords(titles[20:]))
print(f"Axe Tour->Battle : cap {cap(T,B):.3f}° ; Battle à {hav(T,B):.2f} km\n")
print(f"{'lieu':34s} {'coord':>18s} {'écart axe':>10s} {'abscisse=D(a)':>13s} {'D(b) T-B-X':>10s} {'d(T,X)':>8s}")
rows = []
for t in titles:
    v = res[t]
    if not v: print(f"{t:34s} (pas de coordonnées)"); continue
    X = v[:2]; xt = xtrack(T, B, X); al = along(T, B, X)
    rows.append((abs(xt), t, X, xt, al))
for a_, t, X, xt, al in sorted(rows):
    print(f"{t:34s} {X[0]:8.3f},{X[1]:8.3f} {xt:+10.1f} {al:13.1f} {hav(T,B)+hav(B,X):10.1f} {hav(T,X):8.1f}")
print("\nLecture: un lieu sur l'axe prolongé apparaît avec écart ~0 (< 2 km). Les autres ne sont atteignables qu'en lecture (b) (ligne brisée) avec un cap libre depuis Battle.")
print("Points de l'axe prolongé à quelques distances (pour repérage d'îles/ports côtiers) :")
for D in (342, 500, 800, 1000, 1100, 1200, 1300, 1500, 1700, 2000, 2500, 3000, 3600):
    la, lo = dest(T, cap(T, B), D); print(f"   D={D:5d}  {la:7.3f}, {lo:7.3f}")
