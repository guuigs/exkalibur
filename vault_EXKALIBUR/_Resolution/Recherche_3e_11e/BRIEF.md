# BRIEF commun — recherche « troisième et onzième » (É12 Exkalibur), 03/10/2026

## Contexte
Énigme 12 (Ad vitam aeternam) : « Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. » Départ = « chemin de rempart » (tour d'Avalon / Rue du Rempart, Saint-Maximin, Isère : tour 45.4288723, 6.03101275 ; Rue du Rempart 45.42977, 6.03118 ; carrefour Le Vivier 45.42898, 6.03404). Lire : `vault_EXKALIBUR/00 - Solutions validées.md`, `vault_EXKALIBUR/_Resolution/Enigme_12/solution.md` (tout, surtout la fin), `vault_EXKALIBUR/_Resolution/Revue_globale/FAQ_E12_complet.md`. FAQ complète : `vault_EXKALIBUR/_Resolution/Communaute/faq_officielle_auteur.json` ; FAQ8 : `/tmp/claude-0/-home-user-exkalibur/459ce361-0706-50f5-a5c3-fb8740ef9d66/scratchpad/faq8f.txt`.

## Données / outils disponibles (réseau ouvert : IGN data.geopf.fr WMS/WFS, api.openstreetmap.org/api/0.6/map (bbox ≤ 0,25 deg², ≤ 50 000 nœuds), Wikipedia, web ; Overpass BLOQUÉ)
- OSM brut déjà parsé du secteur 5,99-6,09 E / 45,40-45,45 N : `/tmp/claude-0/-home-user-exkalibur/459ce361-0706-50f5-a5c3-fb8740ef9d66/scratchpad/osm.json` (clés nodes/ways/pois). Pour plus loin : télécharger d'autres tuiles via l'API OSM /map.
- BD TOPO (Lambert 93) : `.../scratchpad/wfs_*.json` (batiment, troncon_de_route, troncon_hydrographique, toponymie, detail_hydrographique, construction_ponctuelle, zone_de_vegetation…). Script WFS : `outils_scratch/fetch_wfs2.py`.
- LiDAR 1 m (MNT, MNH) mosaïque 7×7 km : `.../scratchpad/mnt.npy`, `mnh.npy` (origine L93 X0=933000, Y0=6482000, 7000×7000, nord en haut) ; viewshed depuis le sommet de la tour : `viewsheds.npz` (grille 2 m).
- Lieux-dits cadastre : `vault_EXKALIBUR/_Resolution/Revue_globale/T11_roches_web/lieux_dits_bruts.json`.
- Python : numpy, scipy, pyproj, shapely, PIL installés. Travailler dans un sous-dossier du scratchpad à ton nom.

## GRILLE D'ÉLIMINATION (réponses de l'AUTEUR seulement — une hypothèse qui en viole une est « ÉCARTÉE (sûr) »)
C1 Même nature (FAQ06-009 « oui tout à fait »). Matériaux différents : pas de réponse (donc permis).
C2 Un seul de chaque (FAQ06-216).
C3 Deux POINTS à placer sur une carte (FAQ05-074, FAQ07-063), séparés de 10 stades = 1 850 m ±1 % (stade 185 m ; fenêtre 1 831-1 869 m ; tolérer 177,6-192 m/stade en variante) EN LIGNE DROITE (FAQ07-120).
C4 Pieds nus : pas d'écharde sur la 3e ; écharde possible sur le 11e (FAQ07-068) → le 11e comporte du bois (ou équivalent).
C5 On marche surtout sur l'un des deux (FAQ06-247).
C6 « Le treizième ne vous mènerait pas au bon endroit » ; on aurait pu aller jusqu'au 13e (FAQ06-133) → la série a ≥ 13 éléments (ou le 13e existe).
C7 « 3e et 11e auraient-ils pu être 8e et 16e ? Non, sinon incorrect » (FAQ8) → les rangs comptent, pas seulement l'écart 8.
C8 Pas liés à un chevalier (FAQ07-065). Pas un ensemble de 52 sur le chemin de rempart (FAQ07-156). La boussole de la carte n'aide pas (FAQ8) ; « l'essai » n'aide pas (FAQ8).
C9 Difficiles à trouver (FAQ06-292) ; personne n'a nature+position (FAQ06-109) ; un joueur a trouvé la nature (FAQ06-259) ; trouvables de chez soi (FAQ04-114), « une fois la zone trouvée » (FAQ8).
C10 Visibles sur les enluminures = « l'une des clés » (FAQ05-093) ; « tout est codé » dans enluminures/carte/énigmes (FAQ04-027) ; l'enluminure 11 aide à placer « une partie » (FAQ07-239) ; le visuel 11 est confirmateur « pour l'un d'entre eux » (FAQ04-186).
C11 Ils servent, avec la distance et le point de départ, à trouver la clairière (FAQ07-120/133/180, FAQ06-166) ; ils « rapprochent grandement du trésor » (FAQ05-068). La clairière (jonction de chemins) est visible à l'œil nu depuis le rempart et proche.
C12 Genre : l'auteur dit « la troisième » et « le onzième » (FAQ07-068) et accepte les deux genres (FAQ03-293).
Indices faibles (non éliminatoires) : liste « universelle » (mois, apôtres, zodiaque…) → NRP ; texte de 1 500 ans → NRP ; « série culturellement reconnaissable ou construite par la chasse » → NRP ; « la découverte du onzième peut prêter à sourire ? non ».
Corrections de Guilhem (font foi) : enl. 11 = croix de 11 pierres dans chaque sens (21 au total), 4 R ; pierres chiffrées 1, 3, 5 et une 4e pierre avec un signe lu « 2 inversé » (peut-être 11, « presque plutôt 21 ») = le « point d'interrogation » de l'auteur ; le « V » devant le 5 est un brin d'herbe ; livres numérotés : enl.4 I, enl.2 II, enl.5 III (personnage portant une grande croix latine), enl.10 VI, enl.11 (ermite à la lance) II.

## Livrable
`vault_EXKALIBUR/_Resolution/Recherche_3e_11e/<ID>_rapport.md` : tableau hypothèse × critères C1-C12 (✓/✗/?), verdict ÉCARTÉE (sûr, avec la contrainte violée citée) / FAIBLE / VIVANTE ; pour les vivantes, paires concrètes de points (coordonnées) à 1 850 m ±1 %, avec taux de hasard (même test sur positions/permutations témoins). Ne JAMAIS écarter sur une intuition : seulement sur une réponse de l'auteur ou un fait vérifié. Résumé final 300 mots max. Pas de git commit.
