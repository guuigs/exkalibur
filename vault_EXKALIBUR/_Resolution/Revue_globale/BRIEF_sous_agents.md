# BRIEF sous-agents : revue globale des zones d'ombre (Exkalibur), 30/09/2026

## Le jeu
Chasse au trésor **Exkalibur** (Puy du Fou / Unsolved Hunts, auteur Étienne Picand). 12 énigmes, 12 enluminures et une carte.
Le coffre est **enterré à environ 40 cm** sur **domaine public** (ni terrain privé, ni monument historique, ni bâtiment, accès gratuit), dans l'un de ces pays : PT, ES, AD, FR, UK, IE.
- Il est **validé au pile-poil** uniquement.
- Les énigmes 1 à 11 ont été résolues par la communauté (annonce du 04/06/2026). Le coffre n'est **pas trouvé** au 30/09/2026.

## Règles (strictes)
- Les notes de Guilhem sont en **LECTURE SEULE** : tu écris **uniquement** dans `C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/`, avec **ton préfixe** (T1_, T2_, T3_).
- Les fichiers lourds (données, images de travail) vont dans `C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/`.
- **N'invente jamais** le contenu d'une énigme ou d'une image. Sépare **FAIT / HYPOTHÈSE / INTUITION**, chacun avec une confiance. Cite la source : réf. FAQ (`FAQ06-102`), URL, ou fichier.
- **Calculs par script uniquement**, archivés avec leur sortie `.out.txt` dans `Revue_globale/`.
- **Test du hasard obligatoire** : avec ±1 %, une distance de 1,85 km tombe « juste » par hasard dans une zone habitée. Compte les candidats possibles, et ne garde un candidat que si **un indice indépendant** le désigne.
- **INTERDIT** :
  - Discord, sous toutes ses formes : c'est l'orchestrateur qui le lit ;
  - poster quoi que ce soit, créer un compte, utiliser un identifiant ;
  - toute action hors lecture web / API publique et écriture dans ton dossier.
- Préfère « pas trouvé » à une solution séduisante. Garde au moins 3 pistes vivantes, et **écris la raison de chaque abandon**.
- Langue : français.

## Sauvegarde continue (limite d'usage Claude : ta session PEUT être coupée)
- Crée `Revue_globale/<préfixe>notes.md` **dès ton premier appel**. Mets-le à jour **après chaque piste**, sous un en-tête `## REPRISE` qui contient : Fait / En cours / Prochaines étapes / Écarté.
- Si ce fichier existe déjà, tu es une **REPRISE** : lis REPRISE et ne refais pas ce qui est fait.
- Budget : environ **35 appels d'outils**. Termine par un résumé de 15 lignes maximum.

## Sources à disposition
- **FAQ officielle de l'auteur** (JSON, environ 2 000 Q/R) : `_Resolution/Communaute/faq_officielle_auteur.json`.
  - Items `{ref, theme, q, a}` imbriqués. Parcours récursif : tout dict qui a `q` est un item.
  - Recherche par **mots concrets** dans `q` + `a`, pas seulement par thème.
- **Helpers Python** : `exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())`.
  - Fournit `hav`, `brg`, `cen`, `load`, `faq()`, `wfs(layer,bbox)` et `get(url)`.
  - Le User-Agent est déjà réglé : urllib fonctionne. Web : API Wikipedia via `get`.
- **IGN BD TOPO v3** (WFS public, sans clé) : `wfs("BDTOPO_V3:<couche>", (latmin, lonmin, latmax, lonmax))`.
  - Déjà téléchargé en GeoJSON pour un carré de ±4,5 km autour de (45.4262, 6.0248) : `C:/Users/Admin/AppData/Local/hermes/cache/scratch/ign/<couche>.geojson`.
  - Couches : troncon_de_route (dont les chemins et sentiers, champ `nature`), troncon_hydrographique, cours_d_eau, detail_orographique, toponymie, lieu_dit_non_habite, zone_de_vegetation, construction_ponctuelle (dont les croix), plan_d_eau, detail_hydrographique, surface_hydrographique, foret_publique, haie, batiment, zone_d_activite_ou_d_interet, ligne_orographique.
  - Autres services publics utilisables :
    - altitude : `https://data.geopf.fr/altimetrie/1.0/calcul/alti/rest/elevation.json?lon=..&lat=..&resource=ign_rge_alti_wld` ;
    - lieux-dits cadastraux : `https://cadastre.data.gouv.fr/bundler/cadastre-etalab/communes/<INSEE>/geojson/lieux_dits` ;
    - monuments historiques : API Mérimée / data.culture.gouv.fr.
- **Photos HD** : `_Resolution/Sources/photos_HD_2026-09-29/` (voir `INDEX.md`).
  - IMG_4334 : planche des 12 enluminures.
  - IMG_4342 : **R5G = « enluminure 9 » de l'auteur** (guerrier romain, ciel à symboles, étang aux poissons et aux cygnes, rocher rayonnant, coupe). La photo est tournée de 90°.
  - IMG_4345 : R6G = enluminure 11 (chemin de pierres en croix, 4 pierres à cartes, dragon blanc à 3 têtes, ermite, 3 croix).
  - IMG_4344 : R6D = enluminure 12 (tour rouge à l'œil, cloche, sanglier rouge, Jésus seul à table, charpentier à la scie, porte à triangle d'or, pont).
  - IMG_4333 : carte officielle.
  - Textes : IMG_4358 et 4359.
  - Recadrage et rotation avec PIL. Pour regarder une image, utilise ton outil de vision sur le fichier.
- Solutions déjà établies : `EXKALIBUR/00 - Solutions validées.md` (texte intégral + TL;DR des 12 énigmes), `_Resolution/GRAPHE_INDICES.md`, `_Resolution/Enigme_XX/solution.md`.

## État de la fin de jeu (énigme 12, *Ad vitam aeternam*)
Texte exact (IMG_4359) :
> Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. Le roi avait rejoint les fées, et laissé son épée aux portes d'Avalon. L'épée, évidemment. L'épée, depuis toujours ! Là était la dernière clé de la quête du Graal. Tombée par trois fois, elle était revenue là où elle n'avait jamais cessé d'être.
> Tout commence et tout s'achève. J'entends le chant retentir. J'ai fait une dernière veille au chemin de rempart, et l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau.
> Dans la clairière, à la jonction des chemins, j'ai suivi à senestre les eaux enchantées jusqu'à la grande roche, puis fis dix pas au nord, autant à l'est. Arrivé à la souche-majesté, je fis huit derniers pas, et ma boussole suivait le jour dernier.
> Là, tu trouveras la coupe du charpentier.

**Enchaînement probable.** L'énigme 11 va de Saint-Palais (64) au château Bayard (Pontcharra, 38), soit 606,6 km = D·π, avec D = 193,13 km (énigme 10). Cette droite, prolongée de 1,07 km, passe par la **tour d'Avalon** (Saint-Maximin, 38 ; 45.4288, 6.0308 ; inscrite MH). Hypothèse de travail : **chemin de rempart = tour d'Avalon**, rumeur Discord majoritaire (FAQ07-257 : 7 joueurs ont trouvé les remparts).
- ⚠️ Alternative à tester : le **fort Barraux** (4 km à l'ouest, remparts, chemin de ronde), ou un autre rempart visible.
- Narrateur probable : **Bayard** (né au château Bayard ; « dernier chevalier » ; † 30/04/1524 à la Sesia).

**Contraintes FAQ (FAIT) :**
- *Chemin de rempart*
  - Point précis (FAQ07-268), accessible toute l'année (FAQ06-020). Pas maritime (FAQ07-023).
  - Même lieu que l'arrivée de l'énigme 11 (FAQ06-193). Le coffre n'en est pas loin (FAQ06-244).
  - Le rempart peut être trouvé sans Montsalvage (FAQ07-202).
- *Troisième / onzième*
  - 10 stades romains à ±1 % (FAQ05-172), en ligne droite (FAQ07-120). Même nature (FAQ06-009), un seul de chaque (FAQ06-216).
  - Difficiles à trouver (FAQ06-292). La nature a été identifiée par un joueur (FAQ06-259), mais pas leur position (FAQ06-109, FAQ07-236).
  - Pieds nus : pas d'écharde sur la troisième, écharde possible sur le onzième (FAQ07-068). Il faut marcher surtout sur l'un des deux (FAQ06-247).
  - Le 13e ne mènerait pas au bon endroit (FAQ06-133). On va directement de la 3e à la 11e, mais on passe par des étapes intermédiaires (FAQ04-115).
  - Pas lié à un chevalier (FAQ07-065). Pas un ensemble de 52 (FAQ07-156). Pas de couleurs (FAQ07-244).
  - L'enluminure 11 aide à en placer une partie (FAQ07-239). Enluminures, carte ou énigmes le codent (FAQ04-027).
  - Ce sont « une aide plus que précieuse » pour trouver la clairière une fois la « direction de l'astre » comprise (FAQ07-133). L'astre, c'est « le ciel qui vous guide », pas une direction au sens strict (FAQ07-132, 07-152, 07-180).
- *Clairière*
  - Clairière = jonction des chemins = « l'endroit m'est apparu » (FAQ05-165). Point précis (FAQ03-083, 06-230).
  - Toujours une clairière aujourd'hui (FAQ03-274). Visible depuis le rempart. Personne ne l'a trouvée (FAQ06-102).
  - Le chemin de rempart n'est pas l'un des chemins de la jonction, mais ils sont très proches (FAQ06-025).
- *Eaux enchantées*
  - Eaux enchantées = le ruisseau (FAQ03-152). On les suit à gauche jusqu'à la grande roche, qui bloque le passage (FAQ06-195).
  - Elles coulent jusqu'à la roche et au-delà (FAQ03-082). On risque de se mouiller avant la roche, pas après (FAQ06-090).
  - Il faut aller sur place pour les voir (FAQ06-060). « Féeriques » (FAQ06-284).
- *Grande roche et souche*
  - Grande roche « très difficile à manquer » (FAQ03-211), difficile à toucher sans se mouiller (FAQ06-180). Pas visible sur Maps selon l'auteur (FAQ07-126).
  - Souche-majesté : appellation « très concrète » (FAQ05-008), non visible sur Maps (FAQ07-078).
- *Pas*
  - 10 pas au N, 10 à l'E, puis 8 depuis la souche, dans la direction du « jour dernier ». C'est un jour, pas un moment de la journée (FAQ07-186). Boussole réelle.
  - Même pas partout ; mesure « de pèlerin », « restez simple » (FAQ06-152).
- *Enluminure 9 (R5G)*
  - Sa coupe **est** la coupe du charpentier (FAQ07-005).
  - « Intéressez-vous au **contour de ces eaux** (étang aux 2 poissons et 2 cygnes) » (FAQ07-052). Identifier correctement le **bassin** rapproche grandement de la résolution (FAQ03-308).
  - Ce qu'on voit dans l'enluminure 9 sert à localiser l'objectif, et les éléments alentour aident (FAQ07-196).
  - Ciel : loup, étoile, arc-en-ciel, âne + émeraude (verte), diamant + ancre, croissant de lune.
    - Lecture de gauche à droite (FAQ05-019) ; les paires se décodent ensemble (FAQ07-143) ; « code universel », mêmes dessins dans toutes les langues (FAQ06-138).
    - Ils servent à « identifier un élément crucial » et à un « déclic en fin de jeu » (FAQ07-134, 07-198). À interpréter une fois la zone finale trouvée (FAQ06-067). C'est une des voies de passage de la fin (FAQ06-184).
- *Enluminure 11 (R6G)*
  - Les 4 pierres portent des symboles de cartes (carreau, cœur, trèfle, pique), des lettres D et C sur celles du fond, et des chiffres 1, 3, 5 plus un point d'interrogation (= un nombre, FAQ05-163 ; « orientez-vous », FAQ05-091).
  - La croix de pierres porte des R. Ce sont deux cryptos distincts (FAQ07-035). « N'oubliez pas l'épée » (FAQ05-101). Noms classiques des figures de cartes (FAQ07-106).
- *Enluminure 12 (R6D)* : la cloche aide à trouver la tour, parce qu'elle est accolée au bâtiment (FAQ06-240). Avec *Ultima cena*, deux éléments à identifier puis concaténer donnent « quelque chose de très précieux » (FAQ07-019).
- *Lettrines* : « dans leur ensemble, elles sont à suivre pour trouver quelque chose » (FAQ06-270).

## Premier relevé IGN autour de la tour d'Avalon (FAIT, BD TOPO)
- Toponymes : « Tire-Loup » (bois, 1,6 km, cap 98°), Ruisseau de Rebouchet (0,9 km, S), Ruisseau de Tapon (1,8 km, E), Ruisseau de la Burge, le Ratier (sommet, 0,8 km NE).
- Plans d'eau : Plan d'eau des Lônes (2,7 km), Étangs du Maupas (3,6 km, SO), Bassin du Cheylas.
- Forêts publiques : Saint-Maximin (1,8 km E), Pontcharra, Moutaret, Glapigneux.
- Croix : 0,38 km (cap 55°), 0,55 km (95°), 0,92 km (204°), 1,28 km (82°), 1,47 km (3°).
- Aucun chemin de croix balisé dans OSM à moins de 12 km.
