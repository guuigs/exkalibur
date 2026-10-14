# É12 — Pistes vivantes et protocole d'itération (06/10/2026)

**Fichier de pilotage unique de l'É12.** On l'ouvre à chaque séance, on y met à jour les fiches, on le commite. Le détail des tests passés reste dans les autres fichiers (`PISTES_ECARTEES.md` en premier).

---

## 0. Socle : ce qu'on tient pour acquis

| Élément | Valeur | Confiance | Ce qui ferait tout revoir |
|---|---|---|---|
| Départ | Esplanade / enceinte de la **tour d'Avalon** (Saint-Maximin), sur la droite de l'É11 (+1,1 km après Bayard). Accès libre toute l'année | 75 % | une réponse de l'auteur qui situe le rempart ailleurs |
| Narrateur | **Bayard** (un millénaire après Arthur, mort sous une arquebuse = « actes lâches », « sans reproche » = pur, statue, rues, enseigné à l'école) | 65 % | voir piste **N3** : FAQ07-050 et l'annonce du 04/06 distinguent « le dernier chevalier » et « le narrateur » |
| Jour dernier | 30/04/1524 (azimuts 63,7° / 68,6° / 73,9°) | 60 % | lecture 8e jour / Pâques (déjà discutée) |
| Coffre | domaine public, loin de tout bâtiment (≥ 100 m), fauteuil avec accompagnateur, **hors Pontcharra** | règle | — |
| Clairière | = jonction de vrais chemins = « l'endroit apparu », visible à l'œil nu du rempart, proche du rempart, mais le rempart n'est pas l'un des chemins | FAQ | — |

## Décisions de Guilhem (à respecter)
- 07/10 : **« à senestre » n'est plus un filtre** : l'eau peut être à gauche OU à droite du chemin suivi.
- 06/10 : l'**épée reste essentielle** (seules les balises de Pontcharra et le calque sont abandonnés).
- Sous-agents sur `deepseek-flash`.

## 1. Contraintes dures sur les 3e et 11e (lettre de la FAQ)

C1 même nature (06-009) · C2 un seul de chaque (06-216) · C3 deux points à pointer sur une carte (05-074, 07-063) · C4 1 850 m ±18 m en ligne droite (05-172, 07-120) · C5 pas visibles sur Maps, et « se voient-ils des remparts ? » est une **mauvaise question** (06-227) · C6 trouvables de chez soi (04-114) · C7 pieds nus : pas d'écharde sur la 3e, écharde possible sur le 11e (07-068) · C8 on marche surtout sur l'un des deux (06-247) · C9 le 13e existe et mène ailleurs (06-133) · C10 les 8e et 16e seraient « incorrects » (FAQ8) · C11 pas un ensemble de 52 (07-156) · C12 pas un chevalier (07-065) · C13 ordre différent du « numéro un » d'Ultima Cena (04-051) · C14 l'enl. 11 place « une partie », confirme « l'un des deux » (07-239, 04-186) · C15 se positionnent par rapport au point de départ (07-120, 07-180) · C16 le 11e ne « prête pas à sourire » (FAQ8).
Plus : un joueur a identifié leur **nature** (06-259), personne leur **position** (06-109, 07-236). Ils « prennent tout leur sens » à l'arrivée de l'É11 (05-196). Ils « rapprochent grandement du trésor » (05-068). Le ciel indique où aller, « c'est là » qu'ils servent (06-166). Le **premier paragraphe** est lié à la suite « d'un point de vue spatial et topographique » (06-069).

**Grille de score** : toute piste est notée sur C1–C16. Une piste n'est candidate que si C7, C14 et C15 passent.

---

## 2. Pistes vivantes, classées

Format de chaque fiche : **Idée** · **Pour** · **Contre** · **Ce qui la tue** · **Prochain test** · **Statut**.

### N1 — « 3e = étape intermédiaire, 11e = destination finale » 🆕 (lecture de FAQ03-293)
- **Idée.** L'auteur : « on aurait pu dire … la troisième et la onzième **à la destination finale**, ou seulement **deux étapes, une intermédiaire plus la destination finale. Il n'y a que deux étapes.** » On a toujours traité les 3e/11e comme une paire symétrique. Lecture littérale : la 3e est une étape intermédiaire, le **11e est la destination finale** (la zone de la clairière).
- **Pour.** C'est cohérent avec plusieurs réponses :
  - l'écharde possible sur le 11e : zone boisée, souche (C7) ;
  - on marche surtout sur l'un des deux : là où l'on fait les derniers pas (C8) ;
  - l'enl. 11 (chemin vers un bois) confirme « l'un des deux » (C14) ;
  - « ils rapprochent grandement du trésor » (05-068).
- **Contre.** « Même nature » (C1) oblige la 3e et le 11e à être deux objets du même type, l'un en route, l'autre à l'arrivée. Leur nature reste inconnue.
- **Ce qui la tue.** Une réponse de la FAQ où le 11e serait loin du coffre.
- **Prochain test.** Inverser le crible : partir des deux zones finales survivantes (J16, Le Mouret) et chercher, à 1 850 m ±18 m, une **3e** non boisée, marchable, posée par rapport au rempart. Le ciel donne la direction (06-166). Points calculés sur les trois azimuts du jour dernier, depuis la tour :
  - J16 : 45.43607, 6.05174 (63,7°) · 45.43485, 6.05278 (68,6°) · 45.43345, 6.05376 (73,9°), soit 1,82 à 1,87 km de la tour ;
  - Le Mouret : 45.43650, 6.05298 · 45.43547, 6.05503 · 45.43414, 6.05715.

  Ces six points tombent dans le secteur du **Couvet** (candidat gardé en réserve, 45.434748, 6.059095). Il faut regarder ce qui s'y trouve (pont, gué, dalle, croix de pierre, passage) avant de conclure, puis appliquer le test du hasard (azimuts tirés au sort).
- **Statut.** 🔴 06/10 : mécanisme de placement **mort** (6 points en terrain agricole ouvert, rien à 60 m ; hasard 25,7 %, `R0610_N1_inverse.md`). La **lecture** (11e = zone finale boisée, 3e = étape) reste utilisable comme contrainte de nature.

### N2 — Le narrateur, sous-exploité en fin de jeu 🆕 (FAQ07-030, 05-182, 06-192)
- **Idée.** FAQ07-030 : « des éléments physiques **de même nature** ayant un lien avec les **écrits du narrateur** dans la zone finale ? → **Oui**. Une dizaine ont identifié le narrateur mais **quasiment aucun ne s'en sert**. Il y a un lien **fort et évident**, extrêmement utile en fin de jeu. » FAQ05-182 : sans le narrateur, la dernière énigme est « presque impossible ». FAQ06-192 : il faut exploiter sa **biographie réelle**.
- **Pour.** « De même nature » est le mot exact de 06-009 (les 3e et 11e). C'est le plus fort indice textuel jamais relevé sur la nature des 3e/11e.
- **Contre.** Le sens d'« écrits du narrateur » est ambigu : le parchemin lui-même, ses mots gravés, ou des textes biographiques (le *Loyal Serviteur*, 1527, en chapitres).
- **Ce qui la tue.** Rien de « même nature » lié à Bayard dans 3 km de la tour.
- **Prochain test.**
  1. Inventorier tout ce qui porte la parole ou le nom de Bayard autour de la tour : plaques, stèles, panneaux du sentier « Sur les traces du chevalier Bayard », bornes du parcours Pontcharra (61-70), devises gravées, croix, rue Bayard, statue.
  2. Lister les **chapitres III et XI** du *Loyal Serviteur* (« La très joyeuse… histoire… du bon chevalier sans paour et sans reprouche », Gallica). On ne cherche pas des « chapitres III et XI » abstraits (déjà écartés) mais les **lieux** qu'ils citent, et leur écart (1 850 m ?).
  3. Faire de même avec les éventuels écrits propres de Bayard (lettres, devise).
- **Statut.** 🟠 06/10 : aucune paire d'objets liés à Bayard à 1 850 m ; chapitres III/XI du *Loyal Serviteur* hors zone (Savoie, Naples). Le lien « fort et évident » = le sentier « Sur les traces du chevalier Bayard » qui part du pied de la tour vers le château natal. Reste : positions des panneaux du sentier (absentes du web). `R0610_N2N3_narrateur.md`.

### N3 — Contrôle de l'identité du narrateur 🆕
- **Idée.** Avant d'exploiter N2, confronter Bayard au profil complet de la FAQ, soit 40 réponses relevées le 06/10 :
  - homme réel, de premier ordre, lien très fort avec le mythe arthurien (07-140) ;
  - métier commun, encore pratiqué de façon modernisée (06-051, 07-081) ;
  - portrait au pinceau (06-159) ; statue (07-265) ; rues (07-047) ; enseigné à l'école (07-211) ;
  - a donné sa vie pour sa cause, a subi des actes lâches (06-128, 07-119) ;
  - descendance (07-029) ; manuscrit qu'il aurait pu faire imprimer de son vivant (05-057) ;
  - « un millénaire a passé » est la clé de son identification (06-024) ;
  - « le combat d'une vie lui a coûté sa gardienne de lumière » (05-104) ; jour de honte → jour de gloire tiré de sa biographie (06-048).
- **Points faibles de Bayard.** « Gardienne de lumière », « jour de honte », et l'annonce du 04/06 qui nomme « le dernier chevalier, le narrateur » comme deux trouvailles distinctes.
- **Prochain test.** Remplir la grille pour Bayard et pour 2 ou 3 autres candidats, sans parti pris.
- **Statut.** ✅ 06/10 : Bayard confirmé (~29/30 critères contre Du Guesclin, René d'Anjou, Jacques Cœur, Saint Louis). Gardienne de lumière = la dame aimée (Loyal Serviteur ch. XIII) ; devise *Accipit ut det* (la lune reçoit la lumière pour la rendre).

### T1 — Jonction J16 (45.42684, 6.03200, Route du Vivier, marais d'Avalon)
- **Pour.** Elle survit au crible « depuis chez soi », est vue du rempart, avec de l'eau à gauche sur la branche du marais.
- **Contre.** Aucune grande roche sur cette branche ; le lien avec les 3e/11e ne vient que de la croix PATERNOSTER, écartée.
- **Prochain test.** Branche est vers le Rebouchet et Le Châtelard (seuls rochers compatibles) ; BD Forêt (hêtres) ; cadastre de 1838 (« la Roche », « le Chêne »).
- **Statut.** 🔴 07/10 (refait, géoréférence corrigée et contrôlée, `R0610_J16_est_v2.md`) : branche est = eau à **dextre** (l'« eau à senestre » du 06/10 venait du bug) ; bras NE = eau à senestre mais aucune roche ; bras O = rien ; 6 points de fouille, 0 survivant. — Historique : ⚠️ le test du 06/10 était INVALIDE — bug de géoréférence dans `r0610_j16est_roches.py` (NY=2500 pour une mosaïque de 3 000 lignes : analyse décalée de 500 m vers le nord, coordonnées publiées fausses). À refaire. Ancien statut : 🔴 06/10 (branche est) : eau à gauche ✓, grande roche réelle (45.42485, 6.03198 ; 2,3 m, 17 m du Rebouchet, 222 m de J16) ✓, mais **0/66** points de fouille valables (64 en bois privé, 2 en berge à 27-36°). `R0610_J16_est.md`.

### T2 — Le Mouret (45.42243, 6.04030) — **piste principale retenue le 07/10**
- **MAC (3e/11e)** : seules les listes **Mt 10 / Mc 3**, sens « à droite du Christ », donnent 11e = **Simon le Zélote** (scie de l'enl. 12, FAQ06-238) sans attribut en bois sur la 3e (Jacques/Jean) → écharde cohérente (07-068). Canon romain et rangée de Léonard mettent André (croix en X, bois) en 3e → éliminés.
- **Géométrie (cercle r = 1 068 m centré au rempart, corde 3→11 = 1 850 m)** : 3e = 45.43802, 6.03463 (⚠️ **commune de Pontcharra**, à re-vérifier) ; 11e = **45.42184, 6.04019**, à **8 m d'une source BD TOPO** et 66 m du carrefour du Mouret, corde à 17 m du carrefour ; 13e (Christ) tombe à 25 m du bâti → « ne mène pas au bon endroit » ✓. Grille **C1–C16 : 15 ✅ / 1 ⚠️ / 0 ❌**.
- **Hasard** : fenêtre d'orientation **unique** A = 89,8–93,4° (= aube de Pâques) où la 11e est ≤ 100 m d'une jonction visible avec eau → **P ≈ 1 %** ; mais fragile (bâti à 105 m ; à ≥ 150 m, P = 0 %) et placebo à centres aléatoires 1,79 %.
- **L4 (variante « bloc sous les arbres ») : MORTE (07/10)** — la bande « non cadastrée » du coffre 45.424709, 6.041016 est un **corridor de cours d'eau** (fond de ravin boisé, en V, 30 m de tout chemin) → lit **privé**, pas une emprise publique ; roche C = **pente forestière 35-49° sous canopée**, aucun affleurement sur ortho HR, 5 m **au-dessus** de l'eau (ne barre pas) ; le Rebouchet est à **dextre** depuis J2 (78 % du tracé) ; « arrivé à ce chemin-là » jamais satisfait (2 208 runs, 0) ; coffre seulement au pas 0,75 m ; non vu du rempart ; 11/39 roches du secteur font aussi bien → sous le bruit. `R0710_L4_emprise.md`, `R0710_L4_variante.md`.
- **Vérification (07/10, demande de Guilhem) : L6 n'est PAS en bord de rivière.** Distance mesurée (BD TOPO, Lambert 93) : coffre L6 à **235 m** du Ruisseau de Rebouchet, sa roche à **256 m** ; J2 à 65 m ; 11e (MA) à 220 m ; alors que **roche C (L4) est à 6,2 m** du Rebouchet. Près de L6, le LiDAR ne montre que de **faux talwegs de 0,6 à 1 m** (fossés/ornières, MNH 0 = nu) — pas de lit. **Donc « suivre les eaux jusqu'à la grande roche » ne marche PAS au Mouret : l'eau est là où échoue le domaine public (L4) et le domaine public est là où il n'y a pas d'eau (L6).**
- **Contre-épreuve sur L6** : même méthode appliquée à 45.42033, 6.04254 → bande **plate (676-678 m), nue (MNH 0), à 0,3 m d'un chemin cartographié** = vrai chemin. L6 gagne du crédit.
- **Leçons de données** : ne plus utiliser **RGE ALTI** pour l'altitude ici (lissé, -19 m dans le ravin) ; le Rebouchet BD TOPO est mal placé (~12 m) dans le bois ; **« non cadastré » ne vaut public que si la bande est plate, nue et alignée sur un chemin**.
- **MB (fin différente)** : le public au Mouret = **bandes de chemin seules** (2,34 ha, médiane 4 m) ; le Rebouchet est **non domanial** (lit privé). Fin retenue : roche-bloc 45.420245, 6.042310 (parcelle B0292 privée) → 10 pas N + 10 pas E (pas 1,0 m) tombe **sur le chemin** → 8 pas → coffre **45.42033, 6.04254, NON CADASTRÉ (emprise de chemin, donc public)**, pente 6,2°, bâti 103 m. Variante L4 (roche C) : 45.42471, 6.04102, public/plat/isolé, eau cartographiée, roche sous canopée.
- **Hasard MB** : tomber sur du public est banal (58–75 % des croisements ; 7,6 % pour la chaîne complète) → **aucune valeur de preuve**. Le Mouret reste à 0–5 sur 118 croisements témoins.
- **Faiblesse de fond inchangée** : le déroulé « roche → coffre » échoue (0/1 199 variantes, `R0710_M1`), la liste d'apôtres n'est pas confirmée par l'auteur (03-007, FAQ8), roche ≠ source (03-082), carrefour non vu du rempart.
- Fichiers : `R0710_MA_mouret_3e11e.md`, `R0710_MB_mouret_fin.md`, cartes `images_travail/r0710_MB_*.jpg`.
- **07/10 (M1, 1 199 variantes : départ, pas, nord, souche, jour, 2e roche, eau des deux côtés)** : 🔴 0 survivant hors bruit ; la « roche » de 99 m² n'est pas une roche nue (sous les arbres). **Arrêter le Mouret.** `R0710_M1_mouret_variantes.md`.
- **07/10 (v2)** : **meilleur ajustement textuel de toute la zone** — bras NE (cap 41°) : eau à senestre (le ruisseau se rapproche à 11 m) jusqu'à une **grande roche de 99 m² dans le lit** (45.42399, 6.04271 ; Δz 2,3 m). Mais les 12 points de fouille tombent en parcelles privées B0595/B0636, pente 30-52°, maisons à 22-42 m → 0 survivant.
- **Pour.** Croisement, sources, sentier qui longe l'eau à gauche.
- **Contre.** La fouille tomberait en bois privé (domaine public non sûr), sur des pentes de 40 à 100 %.
- **Statut.** 🟠 bloquée sauf preuve de parcelle publique.

### T3 — Le Couvet (45.434748, 6.059095)
- **Pour.** Cap 73° (lever du 30/04), 2 280 m ; c'est **là que tombe N1**.
- **Contre.** Maisons à 45 m ; la Burge est intermittente.
- **Statut.** 🟠 réserve. À rouvrir si N1 donne une 3e nette.

### D1 — L'épée et le calice (FAQ07-048, FAQ8 « rôle crucial à toute fin du jeu », 02-123, 03-032)
- **Idée.** Comprendre pourquoi l'épée, sous cette forme, est sur toutes les enluminures, et pourquoi telle face est montrée. Le calice tenu par les pattes des dragons est « crucial en fin de chasse ».
- **Contre.** Pas de calque (04-169) ; pas d'épée à tracer après l'É11 (FAQ8).
- **Prochain test.** Lier le calice à « la coupe du charpentier » et au premier paragraphe : « L'épée, évidemment… Tombée par trois fois… revenue là où elle n'avait jamais cessé d'être », que 06-069 dit relié spatialement à la suite.
- **Statut.** 🟠 06/10 : 3 mécanismes testés, négatifs (toponymes « épée », fissure = horizon p = 0,95, tracés passant près de la tour). Acquis : « revenue là où elle n'avait jamais cessé d'être » ≈ « encore dans son rocher » (É1) = la grande roche (50 %) ; la face peinte est probablement le **revers** de l'épée réelle (non photographié publiquement). **Rouverte (Guilhem : l'épée reste essentielle).** Revers = face B : deux dragons + **pommes** + calice (`R0610_epee_deux_faces.md`). Vague épée 06/10 (`R0610_E1/E2/E3_*.md`) : le calice de la garde = la coupe de l'enl. 9 = la coupe du charpentier (le but) ; le pommeau donne les cardinaux (10 pas N / E) mais pas le « jour dernier » (8 faces, pas de 45°) ; l'épée n'est ni un tracé ni une série ≥ 13 ; FAQ8 : l'épée = « dernière clé » et il faut « une dernière intuition cruciale pour trouver la clairière ». Lecture retenue (faible) : l'épée se lit pommeau→garde→lame→pointe = astre→jonction→eaux→roche. Légende vérifiée : l'épée retourne toujours **à l'eau** (Girflet/Bedivere, 3e jet), jamais à la pierre. `R0610_D1_epee_calice.md`.

### D2 — Ponceaux et planches le long des **chemins** (et non des ruisseaux)
- **Idée.** 3e = franchissement en pierre, 11e = passerelle en bois (écharde) ; ils sont absents d'OSM et de la BD TOPO standard.
- **Statut.** 🔴 06/10 : 73 franchissements chemin × ruisseau dans 3 km, aucun chemin n'en a plus de 5 → pas de 11e. `R0610_sentier_Bayard.md`.

### V — Lac du Vernay (Chapareillan, demande de Guilhem, 06/10)
- **Pour.** Contour de l'étang peint tourné de 110° (IoU 0,84-0,87) ; lac **public** (commune de Chapareillan, AL 0105) ; hors Pontcharra ; « lac » de la Dame du Lac ; depuis la rive, tour d'Avalon (132°) et église de Pontcharra (133°) dans la même direction.
- **Contre.** Invisible depuis tous les remparts candidats (cachés de 16 à 28 m, LiDAR MNT+MNH) → FAQ05-155 ; « coupe » reportée en bois privé ; 3,2 km (« pas loin ») ; panorama de l'enl. 9 non spécifique (4 plans d'eau voisins identiques, Vivier et Mirande corrèlent mieux) ; pas de paire 3e/11e.
- **Statut.** 🟠 06/10 : faible. Seule réserve : canopée d'été (LiDAR en feuilles ?) depuis le sommet de la tour. `R0610_V1_vernay_terrain.md`, `R0610_V2_vernay_panorama.md`.

### F1 — Fils de Jacob (3e = Lévi, 11e = Joseph) · F2 — Zodiaque (3e Gémeaux, 11e Verseau, enl. 11 « Verseau : oui » sur Discord)
- **Statut.** 🟠 nature plausible, aucun placement (5 essais pour F1, test du rattachement aux enluminures non propre pour F2). À garder comme **lecture de nature**, à combiner avec N1 ou N2 si un placement apparaît.

---

### C — Chaîne complète sur toutes les jonctions (07/10)
- 324 croisements ≤ 2,5 km hors Pontcharra → 179 « visibles » → 91 suivent un cours d'eau (gauche ou droite) → 17 avec roche-signature sur la branche → 168 points de fouille → **0 survivant** (y compris pente jusqu'à 20°). 0 aussi pour 1 000 tours fictives : la dernière étape ne discrimine pas. 19 quasi-manques (un seul filtre en échec), listés dans `R0710_C_chaine_toutes_jonctions.md` §4.
- ⚠️ Bug relevé : dans `r0610_C_lib.py`, `r0610_j16est2_lib.py`, `r0610_R_*.py`, `CANOPY = MNH − MNT` alors que le MNH IGN est **déjà une hauteur** (0-50 m) → (1) la visibilité de la chaîne C est calculée **sans les arbres** (le « 179 visibles » est surestimé ; l'entonnoir ne peut que diminuer, le 0 final tient) ; (2) le filtre « roche nue » n'agit pas. Les scripts V1 (Vernay), t29, t31 font bien `MNT + MNH`.
- Sous-produit : roche nue de 109 m² (45.43612, 6.03680) avec 46 points plats isolés : **commune de Pontcharra, non cadastré (lit du Rebouchet/Bréda)** → exclue par la règle de Guilhem.

### S — Ciel depuis le rempart (07/10)
- 🔴 6 règles posées avant le terrain (rayon du lever, première lumière/ombres portées, paires d'astres à 1 850 m, Gémeaux/Verseau, ruisseau aligné sur le lever, points à 1 850 m sur azimuts d'astres) : toutes négatives (hasard 17-21 %). Au 30/04/1524 julien : Vénus = étoile du **soir** (lever 05:42 après le Soleil) ; au matin : Lune (croissant 13 %), Mars (az 66,3°), Jupiter ; Soleil az 62,8° (astro) / 67,2° (horizon réel). Depuis le rempart, seules 3 jonctions et 16 points d'eau passent les filtres durs ; aucun n'est sur un azimut céleste. Le secteur visible est dans l'ombre au lever. `R0710_S_ciel.md`.
- Piste suivante proposée : le ciel de l'enl. 9 comme **code à 6 signes** (confirmateur de fin, 06-067), et **remettre en cause le point de départ** (variable la plus lourde).

### D — Départ remis en cause (07/10)
- Arrivée É11 recalculée : **45.423918, 6.020085**, 99 m après le château Bayard (« dépasser très finement » reproduit) ; incertitude ±2,6 km le long de la ligne (D(É10) ±0,5 %), ±450 m en travers.
- Chemins de rempart sur la ligne : château Bayard (privé, sur RDV → échec 06-020, 0 croisement visible) et **tour d'Avalon (public 12/12)**. Autres (Beauregard, Le Clément, Augustins, Maximy, Fayet) privés ; Fort Barraux et La Buissière **non testés** (hors couverture LiDAR).
- Bug canopée corrigé : croisements visibles depuis la tour ≤ 29 (9 depuis le chemin de rempart) au lieu de 179 ; **0 survivant partout** (tour, 1 000 départs fictifs, alternatifs). `R0710_D_depart_alternatif.md`.
- Reste : étendre le LiDAR à l'ouest (Fort Barraux, La Buissière) ; hauteur réelle du chemin de ronde de la tour.

### K — Ciel de l'enl. 9 comme code (07/10)
- 🔴 6 signes = loup (+ glyphe) · étoile · arc-en-ciel · **âne** + émeraude · diamant + ancre · croissant (8 objets). **Correction : le « crâne de bovin » des anciens relevés est une tête d'âne** (05-097, 07-143). Aucune lecture (astro, zodiaque, constellations, chrétien, chimie, toponymes) ne donne série, date ou nom ; le ciel est un confirmateur (06-067). `R0710_K_code_ciel_enl9.md`.

### V — Visibilité depuis le vrai chemin de rempart (07/10)
- Terrasse sommitale ~20 × 30 m, mur/chemin de ronde actuel **3,1 m** (LiDAR) ; enceinte de 1339 (112 m, rempart 15 m) arasée. Croisements visibles ≤ 2,5 km hors Pontcharra : sol esplanade 0 ; haut du mur 9 ; pourtour complet 21 ; sommet de tour 29.
- Chaîne : 3 croisements visibles portent une roche → 36 points → **0 survivant**, de +3 m à +41 m d'œil. Un quasi-manque : 45.437471, 6.005180 (public, pente 1,9°, mais maisons à 47 m), cap 287°, 2 221 m. `R0710_V_visibilite_rempart.md`.

### INV — Recherche inverse du triplet (eau + chemin public + roche), 07/10
- Règle posée avant : eau cartographiée (BD TOPO perméable ou **intermittent** + OSM) ≤ 10 m, bande publique de chemin ≤ 10 m, roche-signature (LRM ≥ 1,5 m, canopée **MNH < 3 m**, ≥ 10 m²) ≤ 30 m.
- **Le triplet existe et pullule** : 8 894 cellules / 49 amas (3,5 ha) ; aux seuils serrés (5/5/10) 625 cellules / 31 amas ; après filtres public + bâti ≥ 100 m + pente ≤ 12° : **519 cellules / 31 amas**, dont **12 hors Pontcharra**. **Hasard** : eau décalée → 4 300 points (×2 seulement) ; thème témoin (courbes de niveau) → ×7. **Banal.**
- **Aucune « grande roche » (LRM ≥ 2,5 m ET ≥ 50 m²) dans un contexte eau + chemin public ≤ 2,5 km** → 0. Les 109 amas LRM ≥ 2,5 m / ≥ 50 m² du secteur sont hors de ce contexte (pentes 30-57°, privé, invisibles).
- **Vérification complémentaire (07/10)** : 535 amas rocheux (3 seuils) recoupés avec les rasters INV → les meilleurs compromis : **45.42277, 6.03437** (Saint-Maximin, **non cadastré**, eau 10,6 m, chemin public 0 m, pente 4,8°, 727 m de la tour, blob 22-30 m², LRM 2,03) et **45.41165, 6.01496** (2,3 km, pente 47°) ; **aucun n'est visible du rempart** (blocage +13 à +16 m, même du sommet de la tour).
- Meilleur candidat de l'inverse : 45.43951, 6.05305 (Laissaud, Les Gorges, Bréda) — public, plat 0,6°, isolé 189 m, roche **dans le lit**, chemin à 3 m — mais roche de 16 m², 2,1 km, non vue.
- **Conclusion** : la coïncidence eau + chemin + roche n'est pas rare, et **aucun point de la zone ne réunit à la fois visibilité du rempart, platitude, domaine public, eau cartographiée et roche imposante**. `R0710_INV_triplet.md`.

## 3. Mortes (ne pas relancer)
Voir `PISTES_ECARTEES.md`. En résumé :
- les **cryptos du texte** (FAQ8 : « la décrypter, non ») ;
- les **séries locales numérotées** (T4 06/10 : bornes, milliaires, croix, parcours de 9 ou 10 étapes) ;
- les constellations, la rose des vents, les calques de l'épée ;
- Machrie Moor, les chemins de croix, les ponts BD TOPO ;
- le SATOR et la croix PATERNOSTER comme mécanisme, le tarot, Hercule ;
- Pontcharra.

## 4. Protocole d'itération (à suivre à chaque séance)
1. **Relire** ce fichier, puis `PISTES_ECARTEES.md`.
2. **Écrire la règle avant de regarder la carte** : quelle nature, quel ordre, quel ancrage, quelle direction. Zéro paramètre ajusté après coup.
3. **Noter la piste sur C1–C16.** Si C7, C14 ou C15 échoue, on arrête.
4. **Calculer** (script `outils_scratch/rXXXX_*.py`) et **faire le test du hasard** : même règle avec des ancres, des caps ou des rangs tirés au sort, 1 000 tirages. Seuil : ≤ 2 % (5 % au plus).
5. **Contrôle terrain depuis chez soi** : vue du rempart, croisement réel, eau à gauche, roche, domaine public (cadastre + personnes morales), maisons à ≥ 100 m, hors Pontcharra.
6. **Mettre à jour** la fiche ici (Statut + date) ; si la piste meurt, une ligne dans `PISTES_ECARTEES.md`.
7. **Commit** avec un message « É12 : <piste> — <verdict> ».

Une piste est **fiable** quand elle passe 2 à 5, plus un contrôle indépendant (un second calcul ou une relecture par un autre agent).

## 5. Ordre de travail recommandé
1. **N1** (une séance) : regarder les six points du secteur du Couvet sur orthophoto + BD TOPO, puis faire le test du hasard.
2. **N3 puis N2** (une séance) : grille du narrateur, puis chapitres III et XI du *Loyal Serviteur* sur Gallica et objets liés à Bayard autour de la tour.
3. **D1** si N1 et N2 ne donnent rien.
4. **T1** (branche est de J16) en tâche de fond.

## 6. Journal des itérations
| Date | Piste | Résultat | Fichier |
|---|---|---|---|
| 06/10 | T1–T5 (départ, texte, FAQ, séries, enluminures) | départ confirmé ; le reste négatif ou faible | `R0610_T*.md` |
| 06/10 | parcours Bayard Pontcharra, bornes royales, Verseau | négatifs | `PISTES_ECARTEES.md` |
| 07/10 | Recherche inverse eau+chemin+roche | triplet banal (49 amas) ; aucune grande roche dans ce contexte ; aucun candidat visible du rempart | `R0710_INV_triplet.md` |
| 07/10 | L4 creusée (emprise + contrôle indépendant) | **L4 morte** (corridor de ruisseau privé, roche = pente boisée, eau à dextre, clause non tenue) ; **L6 créditée** (chemin plat et nu) | `R0710_L4_emprise.md`, `R0710_L4_variante.md` |
| 07/10 | Mouret A (3e/11e) + B (fin différente) | 11e = Simon à 8 m de la source du Mouret (15/16 contraintes, hasard ≈ 1 % mais fragile) ; fin publique trouvée 45.42033, 6.04254 (hasard banal) ; 3e en Pontcharra | `R0710_MA_*`, `R0710_MB_*` |
| 07/10 | Visibilité depuis le vrai rempart (mur 3,1 m) | 0 survivant ; 1 quasi-manque (maisons à 47 m) | `R0710_V_*` |
| 07/10 | Départ alternatif ; code du ciel enl. 9 | tour d'Avalon reste le seul départ public sur la ligne ; 0 survivant ; ciel = confirmateur | `R0710_D_*`, `R0710_K_*` |
| 07/10 | Ciel depuis le rempart (6 règles) | rien (hasard 17-21 %) | `R0710_S_ciel.md` |
| 07/10 | Mouret variantes (M1) ; chaîne C sur toutes les jonctions | 0 survivant partout ; Mouret arrêté ; bug canopée relevé | `R0710_M1_*`, `R0710_C_*` |
| 07/10 | P311 cadastre/voirie ; nature de la roche + inventaire ; J16/Mouret refaits (bug corrigé) | 3e/11e administratifs : rien ; roche = bloc qui barre le ruisseau (60 %), 29 → 7 publiques → 0 complète ; J16 0/6, Mouret NE = meilleur texte mais 0/12 | `R0610_P311_*`, `R0610_R_nature_roche.md`, `R0610_J16_est_v2.md` |
| 06/10 nuit | Vernay (terrain + panorama) ; épée E1-E3 | Vernay public mais invisible du rempart, panorama non spécifique ; épée = clé de lecture, sans coordonnée | `R0610_V1_*`, `R0610_V2_*`, `R0610_E1/E2/E3_*` |
| 06/10 nuit | revers de l'épée (Discord + Atelier Thibaud) ; balises Pontcharra abandonnées | face B = dragons + pommes + calice ; rien de placable | `R0610_epee_deux_faces.md` |
| 06/10 soir | J16 est, sentier Bayard + ponceaux, épée/calice | tous négatifs ; roche réelle au Rebouchet mais coffre impossible | `R0610_J16_est.md`, `R0610_sentier_Bayard.md`, `R0610_D1_epee_calice.md` |
| 06/10 | consolidation + N1, N2, N3 | N1 mort (hasard 25,7 %) ; N3 Bayard confirmé ; N2 sans paire à 1 850 m | `R0610_N1_inverse.md`, `R0610_N2N3_narrateur.md` |
