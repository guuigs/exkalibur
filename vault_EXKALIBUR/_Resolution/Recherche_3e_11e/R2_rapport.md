# R2 : séries religieuses et Passion (troisième et onzième), 03/10/2026

Famille : chemin de croix, apôtres, mystères du rosaire, heures, psaumes, Pater noster, béatitudes, commandements, sept douleurs, et aussi chartreux et saint Hugues.
Scripts et données : `scratchpad/R2/` (`getosm.py`, `parse.py`, `wfs.py`, `wd.py`, `cat.py`, `tests.py`, `chain.py` ; `relig_objs.json` = 574 objets religieux dédoublonnés dans 16 km).

## 0. Sources interrogées (toutes dans un rayon d'environ 15-16 km autour de la tour 45.42887, 6.03101)
| Source | Couverture | Résultat brut |
|---|---|---|
| **API OSM /map** : 48 tuiles de 0,05°, 5,84-6,24 E / 45,29-45,59 N (522 Mo, 1,51 M nœuds) | complète, **première fois sans Overpass** | 124 `wayside_cross`, 103 `man_made=cross`, 17 `wayside_shrine`, 145 lieux de culte ; **0 chemin de croix**, **0 objet `station`/`Via Crucis`**, 0 relation de pèlerinage (seule la *Via Sancti Martini*, départ à Pontcharra) |
| BD TOPO WFS `construction_ponctuelle` (Croix/Calvaire/Clocher), `batiment` (Chapelle/Église), `zone_d_activite` (Culte chrétien), `toponymie`, `lieu_dit_non_habite` (bbox 32 × 32 km) | complète | 433 croix (dont 25 oratoires et 21 vierges), 1 calvaire, 116 clochers, 204 églises et chapelles, 5 908 toponymes |
| Wikidata SPARQL (`wikibase:around`, 16 km) | OK | 997 items, 74 églises, 29 chapelles ; **aucun item « chemin de croix »** |
| Cadastre (`lieux_dits_bruts.json`) | environ 9 km | voir § 3 |
| Web (chemins de croix et calvaires des communes voisines, Myans, Saint-Hugon, tour d'Avalon, désert de Chartreuse) | — | aucun chemin de croix en plein air dans la zone ; l'inventaire Auvergne-Rhône-Alpes est bloqué par un anti-robot ; l'API POP ne répond pas |

## 1. Grille C1-C12 par série
Légende : ✓ compatible, ✗ contredit, ? indéterminé. « Objet » = existe-t-il deux objets réels à 1 850 m ± 1 % dans 15 km (C3) ?

| Série (3e / 11e / 13e) | C1 | C2 | C3 objet | C4 | C5 | C6 | C7 | C8 | C9 | C10 | C11 | C12 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Chemin de croix** (3 = 1re chute / 11 = clouage / 13 = descente de croix ; 14 stations) | ✓ | ✓ | ✗ aucun chemin de croix en plein air | ✓ croix de bois | ? | ✓ | ✓ pas de 16e | ✓ | ✓ | ✓ (porteur de croix « III » enl. 5, croix de l'enl. 11) | ? | ✓ | **VIVANTE comme nature, sans objet réel** |
| Apôtres, Mt 10 (Jacques / Simon / Matthias ou Paul) | ✓ | ✓ | ✗ aucun Simon | ✓ scie | ? | ✓ | ✓ | ✓ | ✓ | ✓ ? (personnages de bord) | ? | ✓ | FAIBLE (pas d'objet) |
| Apôtres, Mc 3 (Jean / Simon) | ✓ | ✓ | ✗ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | FAIBLE |
| Apôtres, Lc 6 et Ac 1 (Jacques / Jude Thaddée) | ✓ | ✓ | ✗ aucun Jude | ✓ massue ou hallebarde | ? | ✓ | ✓ | ✓ | ✓ | ? (médaillon du Christ = attribut de Jude) | ? | ✓ | FAIBLE |
| Apôtres, Canon romain *Communicantes* et litanies (André / Simon / Lin) — texte d'environ 1 500 ans, cf. FAQ8 NRP | ✓ | ✓ | ✗ | ✓ | ? | ✓ | ✓ | ✓ | ✓ | ? | ? | ✓ | FAIBLE |
| Mystères du rosaire, 15 (Nativité / Résurrection) ou 20 (Nativité / Agonie) | ✓ | ✓ | ✗ aucun sanctuaire de la Nativité ; « Chemin du Rosaire » = simple rue à 13,9 km | ? (crèche en bois pour la 3e ?) | ? | ✓ | ✓ (15) / ? (20) | ✓ | ✓ | ? | ? | ✓ | FAIBLE |
| Heures canoniques (7-8 offices) | — | — | — | — | — | ✗ **pas de 11e** | — | — | — | — | — | — | **ÉCARTÉE (sûr)** : pas de 11e ; FAQ06-133 suppose un 13e |
| Heures du jour (12 ; Mc 15,25 « 3e heure » ; Mt 20 « ouvriers de la 11e heure ») | ✓ | ✓ | ✗ | ? | ? | ✗ pas de 13e heure | ✓ | ✓ | ? | ? | ? | ✓ | **ÉCARTÉE (C6, FAQ06-133 : « aurait-on pu aller jusqu'au 13e ? Oui, tout à fait »)** |
| Psaumes (150 ; Ps 42/41 « comme une biche ») | ✓ | ✓ | ✗ ce ne sont pas des lieux | ? | ? | ✓ | ✓ | ✓ | ? | ? | ? | ✓ | FAIBLE |
| Pater noster, 7 demandes | — | — | — | — | — | ✗ pas de 11e | — | — | — | — | — | — | **ÉCARTÉE (sûr, pas de 11e)** |
| Pater noster, mots latins (qui / **regnum** / fiat) | ✓ | ✓ | ✗ abstrait | ? | ? | ✓ | ✓ | ✓ | ? | ? | ? | ✓ | FAIBLE |
| PATERNOSTER, lettres (T / R) | ✓ | ✗ (T et R deux fois chacun) | ✗ | ? | ? | ✗ 11 lettres (13 seulement avec A…O) | ✓ | ✓ | ✓ | ✓ **(enl. 11)** | ? | ✓ | FAIBLE comme série 3e/11e (voir § 4) |
| Béatitudes (8 ou 9 en Mt, 4 en Lc) | — | — | — | — | — | ✗ | — | — | — | — | — | — | **ÉCARTÉE (sûr, pas de 11e)** |
| Dix commandements | — | — | — | — | — | ✗ | — | — | — | — | — | — | **ÉCARTÉE (sûr, pas de 11e)** |
| Sept douleurs de Notre-Dame, 7 paroles du Christ, 7 sacrements, 7 péchés, 7 jours, 10 plaies | — | — | — | — | — | ✗ | — | — | — | — | — | — | **ÉCARTÉES (sûr, pas de 11e)** |
| Fils de Jacob, 12 (Lévi / Joseph) ou 13 avec Dina (Lévi / Dina / Benjamin) ; la coupe de Joseph (Gn 44) | ✓ | ✓ | ✗ | ? | ? | ✓ seulement avec Dina | ✓ | ✓ | ? | ? | ? | ✓ | FAIBLE (curiosité : « coupe ») |
| Règle de saint Benoît (vers 530, environ 1 500 ans ; ch. 11 = vigiles du dimanche, « dernière veille ») | ✓ | ✓ | ✗ ce sont des chapitres | ? | ? | ✓ | ✓ | ✓ | ? | ? | ? | ✓ | FAIBLE |
| Chartreux : limites du désert de la Grande Chartreuse (16 dans la bulle de 1184, 67 en 1540 ; croix gravées dans la roche **ou dans les arbres**, oratoires) | ✓ | ✓ | ? liste non trouvée ; limites à **15-20 km et plus** (oratoire de Nerfont / Nère Fontaine à 17,0 km) | ✓ (arbre = bois, roche = pas d'écharde) | ? | ✓ | ✓ | ✓ | ? | ? | ✗ ? loin de la tour | ✓ | FAIBLE, à garder en réserve (voir § 5) |
| Parcours thématique de Saint-Maximin (9 étapes, de la tour à l'étang du Vivier) | — | — | — | — | — | ✗ pas de 11e | — | — | — | — | — | — | **ÉCARTÉ (sûr, 9 étapes)** |

Rappels utiles. **FAQ04-115** (« vous allez directement de la troisième à la onzième, mais ça va vous amener à passer par des étapes intermédiaires ») est l'appui le plus fort pour une série ordonnée et parcourue, comme des stations. **FAQ06-227** (« se voient-ils sur Maps ? des remparts ? » : « vous n'avez pas encore correctement identifié ce que peuvent être les 3e et 11e ») et **FAQ05-074** (« pas visibles sur Maps », mais deux points à pointer) vont contre des objets cartographiés. Cela concorde avec le négatif de terrain ci-dessous.

## 2. Objets réels : chemin de croix et stations (C3)
- **Aucun chemin de croix en plein air dans 15 km** (OSM complet, BD TOPO, Wikidata, web). Les chemins de croix connus sont à l'intérieur des églises (stations espacées de quelques mètres, incompatibles avec 1 850 m).
- **Test de chaîne** : pour les 43 paires de croix à 1 850 m ± 1 %, on compte les croix présentes dans un couloir de 300 m entre les deux. Un chemin de croix devrait en contenir environ 7 (stations 4 à 10). Maximum observé : **4** (vignoble de Saint-Jeoire-Prieuré, à 12 km). Densité maximale : 12 croix dans 1 km, 23 dans 2 km (villages). **Aucune signature de chemin de croix.**
- **Taux de hasard** (paires à 1 850 m ± 1 % comparées aux couronnes témoins 1 500-2 200 m de même largeur) : croix-croix **43 contre 44,7 ± 6,4 (× 0,96)** ; églises et chapelles **7 contre 6,6 ± 2,1** ; clochers **3 contre 2,4 ± 1,3** ; paires dont au moins une extrémité est à moins de 4 km de la tour **8 contre 6,2 ± 3,4**. **Aucun signal.**
- **Depuis les départs** : aucun objet religieux à 1 831-1 869 m de la tour ni de la Rue du Rempart (0 observé, 0,2 attendu). Depuis le carrefour Le Vivier : **1 objet**, une **croix en bois** (OSM n9196370724, `material=wood`, **45.44309, 6.04621**) à **1 834 m (−0,9 %), cap 31°**.
- **Seule paire « 3e sans bois / 11e en bois »** près de la tour : croix sans matériau connu (OSM n9122972149, **45.45860, 6.05489**) ↔ croix en bois (45.44309, 6.04621) : **1 853 m (+0,15 %)**. Hasard : 9 croix en bois × 358 autres croix donnent **2,1 paires attendues pour 3 observées**. Ni l'une ni l'autre n'est visible depuis le sommet de la tour (viewshed LiDAR) et rien ne les numérote. **Non retenue** (bruit de densité), notée pour mémoire.
- **Toponymes de stations** (15 km) : 13e station (Pietà) = **chapelle Notre-Dame de Pitié** (45.39843, 5.96286 ; 6,3 km) et église de la Compassion-de-Notre-Dame (Sainte-Marie-du-Mont ; 7,2 km) ; 12e (Golgotha) = « Les 3 croix » à Goncelin (45.34024, 5.98018 ; 10,6 km), le calvaire BD TOPO (45.53977, 6.00504 ; 12,5 km) et le Passage du Calvaire à La Rochette (8,6 km) ; 14e = lieu-dit « les Tombeaux » (13,5 km) ; Croix des Rameaux (45.45317, 6.07039 ; 4,1 km). **Aucun toponyme de 3e station (chute) ni de 11e station (clou, clouage).**

## 3. Objets réels : apôtres (dédicaces et lieux-dits)
- Dédicaces à des apôtres dans 16 km : Saint-Pierre (Villaroux 4,7 km ; Saint-Pierre-d'Allevard 6,1 ; Soucy 9,5 ; Chignin 10,5 ; Apremont 11,6 ; La Thuile 11,8 ; Coise 13,7 ; Entremont 13,9), Saint-Barthélemy (Sainte-Marie-d'Alloix 7,1), Saint-André (Montagnole 15,6), Saints-Pierre-et-Paul (Villard-Léger 14,1), ancien hôpital Saint-Jacques (La Buissière 4,6). Les « Saint-Jean » sont tous **Jean-Baptiste**, pas l'apôtre. **Aucun Saint-Simon, aucun Saint-Jude ou Thaddée, aucun Saint-Matthias.**
- Lieux-dits du cadastre (nouveaux) : **PLAN SIMON** (Saint-Vincent-de-Mercuze, 45.3746, 5.94575 ; 9,0 km), **JACQUEMIÈRE** (Sainte-Marie-d'Alloix, 45.38439, 5.96897), **LE SOUILLET ET CROIX-SAINT-ANDRÉ** (Saint-Maximin, 45.41769, 6.05824 ; 2,5 km), « Croix de Saint-André » (BD TOPO, 45.4953, 5.98099), PRÉ JEAN VIEUX (2,1 km), PRÉ THOMASSET.
- Paires 3e ↔ 11e : Jacquemière ↔ Plan Simon = **2 115 m (+14 %)**, hors tolérance même avec un centroïde à ± 150 m ; hôpital Saint-Jacques ↔ Plan Simon 4 577 m ; Croix-Saint-André ↔ Plan Simon 10,0 km. **Aucune paire à 1 850 m ± 1 %.** Aucune voie de Compostelle à moins de 30 km.
- **Observation sur les enluminures, à faire vérifier par Guilhem** (montage `apotres.jpg`) : le personnage au **couteau** porte le livre **« VI »** (enl. 10). C'est l'iconographie de **Barthélemy**, qui est **6e dans Mt 10, Mc 3 et Lc 6** (7e dans Ac 1). Le personnage aux **clés** (Pierre, 1er partout) porte un livre ; si c'est bien le « I » de l'enl. 4, deux rangs sur deux concordent. Le « III » (porteur de croix, enl. 5) ne correspond ni à Jacques ni à Jean (3e selon les listes), sauf à y voir Philippe (5e). Les deux livres « II » se contredisent. Statut : coïncidence possible ; elle vaut un recadrage HD (quel numéro pour quel personnage).

## 4. PATERNOSTER et la croix de l'enluminure 11 (rappel, non géographique)
La croix de 11 pierres par bras avec le N au centre reproduit exactement le PATERNOSTER croisé : R à distance 1 du centre (à gauche et au-dessus) et R au bout de chaque bras (droite et bas, distance 5). Cela confirme la lecture SATOR → PATERNOSTER de l'enl. 11 (T15). Comme série des 3e/11e (T / R), elle bute sur C2 (deux T et deux R) et sur C6 (11 lettres). La projection « 231 m par pierre » a déjà été testée (fontaine des Bruns, hameau bâti : non retenue).

## 5. Chartreux et saint Hugues
- **FAITS** : la tour d'Avalon a été construite en 1895 par les chartreux sur le donjon. Une **chapelle Saint-Hugues** (Hugues de Lincoln, chartreux) la flanque au sud ; elle abrite aujourd'hui une maquette du bourg médiéval. OSM nomme **« Place Saint-Hugues d'Avallon »** au pied de la tour (32 m) et **« Église Saint-Hugues »** l'église de Pontcharra (45.43333, 6.02319 ; 786 m ; Wikidata : Saint-Blaise). La **chartreuse de Saint-Hugon** (Arvillard, 45.41974, 6.14371 ; 8,9 km), fondée en 1172-1173, est dédiée à saint Hugues de Grenoble, avec la forêt domaniale de Saint-Hugon et un bois « Saint-Bruno » (10,7 km).
- **Aucune croix numérotée, aucune station ni aucun chemin « de saint Hugues »** trouvé dans 15 km.
- **Piste en réserve (HYPOTHÈSE)** : les limites du « désert » chartreux, une liste ordonnée (16 limites en 1184, 67 en 1540) marquée par des **croix gravées dans la roche ou dans les arbres**. Cela colle de façon élégante à C4 : roche, pas d'écharde ; arbre, écharde possible. Les limites de la Grande Chartreuse sont toutefois à 15-20 km et plus de la tour (oratoire de Nerfont / Nère Fontaine : 45.39389, 5.81937, à 17,0 km), et je n'ai pas trouvé la liste ordonnée de 1184. Pour le désert de Saint-Hugon (vallée du Bens, à 7-12 km à l'est), aucune liste n'a été trouvée. À tester seulement si la liste de 1184 est trouvée (cartulaire de Chartreuse).
- Hors famille, à signaler : le lieu-dit **« LES HUITS ET LES TREIZES »** (Pontcharra, 45.43068, 6.01174 ; 1,5 km à l'ouest de la tour) cite 8 et 13, les deux rangs que nomme la FAQ (8e/16e ; « le 13e ne vous mènerait pas… »). Il s'agit probablement de redevances (huitain, treizain). Origine non trouvée. À transmettre à l'agent « numérotations, cadastre ».

## 6. Conclusion
- Écartées pour de bon (absence de 11e, ou de 13e d'après FAQ06-133) : heures canoniques, heures du jour, 7 demandes du Pater, béatitudes, commandements, sept douleurs, septénaires, plaies, parcours de Saint-Maximin.
- La plus vivante comme nature reste le **chemin de croix** (C4, C6, C7, FAQ04-115 et « Tombée par trois fois »). Elle n'a **aucun support physique** dans 15 km : pas de chemin de croix en plein air, pas de chaîne de croix, taux de paires égal au hasard. Si c'est la bonne série, les stations ne sont pas des objets cartographiés (FAQ06-227, FAQ05-074) : elles doivent se construire, par exemple avec un gabarit tiré des enluminures.
- Apôtres : aucune paire réelle (pas de Simon ni de Jude dans 16 km). La coïncidence « VI = Barthélemy » est à vérifier sur les originaux.
