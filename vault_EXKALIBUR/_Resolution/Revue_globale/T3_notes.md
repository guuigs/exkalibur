# T3 notes

## REPRISE
- Fait : lecture brief
- En cours : lecture solutions
- Prochaines : E1..E11 par script/FAQ
- Écarté : -

## REPRISE (2)
- Fait : lecture brief, solutions, graphe ; T3_faq_zones.py -> .out.txt lancé (FAQ par zone)
- En cours : lecture FAQ par zone puis calculs (É1 lieues, jour dernier, É11 angle), puis narrateur (#NARRATEUR)
- [É1 FAIT] T3_e1_lieues.py/.out.txt : Foix = 53,68 km (indép. du point de mesure ±0,1 km), cap 274,8° (« Couchant » ✓). 12,08 lieues communes (4,444) MAIS 10,74 lieues de 5,0 km, 11,00 de 4,88 (Bourbonnais), 11,12 de 4,828. Lieue implicite 4,88–5,11 km. FAQ01-002 « à vous de déterminer la valeur », FAQ02-155 « pas exactement onze ». Autres candidats à 10,5–10,99 : Lordat (4,44 km), Tarascon (5 km) mais cap/cathares moins bons. Garde León→Foix ∥ SC→Lorient : écart 7,67° (meilleur des 8 candidats, mais marginal). Verdict : inchangée→renforcée légèrement (moyenne).
- [Jour dernier FAIT] T3_jour_dernier.py/.out.txt : lever/coucher à Avalon (45.4288N 6.0308E) : 30/04/1524 JULIEN (=10/05 grég., déc +17,60°) → lever 63,66° / coucher 296,34° ; 30/04/1524 grégorien proleptique → 67,97°/292,03° ; 30/04/2026 → 67,78°/292,22°. Colomb † 20/05/1506 → 57,3°; J.Cœur † 25/11/1456 → 121,8°; solstice été 54,4°; équinoxe 89,4°.
  TROUVAILLE : lever à SAINT-PALAIS le 30/04/1524 julien = 64,69° (64,97° avec horizon -0,567°) vs angle É11 64,99° ! Base rate : 4 j/365 (1,1 %) à ±0,35°. => l'« angle du dernier chevalier » = azimut du lever du soleil le jour de la mort de Bayard (hypothèse, moyenne). Cohérent avec « jour dernier » (É12) = même date, azimuth Avalon 63,66° (julien).
- [FAIT] E5 (FAQ: « enluminure dix » = soleil+pierres+chevalier couronné=R5D ; « enluminure cinq » = nappe+barque+cornemuse=R3G donne « solution intermédiaire » = É10) ; E7 ; E8 (Lincoln/Avalon/wiki) ; E9 narrateur (FAQ 223 items) ; E6 figure C (T3_figure_C_666.py) ; E10/E11 (T3_c6_e11angle, T3_e11_rhumb_soleil). PROCHAINE ÉTAPE : écrire T3_rapport.md (tout est calculé), puis TERMINÉ.

## REPRISE (final) — TERMINÉ
- Fait : toutes les zones (É1, É2, É5, É6, É7, É8, É9 narrateur, jour dernier, É10, É11). Rapport : T3_rapport.md.
- Trouvailles : lever du soleil à Saint-Palais le 30/04/1524 julien = 64,69° (≈ angle É11 64,99°) — hypothèse moyenne-faible ; Hugues d'Avalon né à Saint-Maximin (tour d'Avalon 1895) ; É2 Alexandrie affaiblie (genre) ; É5 R3G porte É10 (« enluminure cinq »), R5D = « enluminure dix » ; « Ligne 8 » = rectangle parisien du KML É1.
- Écarté : formules nombre×constante pour 64,99° ; Marignan comme jour dernier (88°).
