# É12 *Ad vitam aeternam* : fiche de reprise (état au 14/10/2026)

Cette fiche sert à reprendre le travail sur un autre ordinateur, seul ou avec Claude. Elle résume la méthode, les règles, l'état de chaque élément de l'énigme et ce qui reste à faire.

Pour le détail, voir :
- `Enigme_12/Reprise_2026-10-13/TEXTES_direction.md` (§ 1 à 10) ;
- `Enigme_12/Reprise_2026-10-13/LISTES_enigme_et_FAQ.md` (les deux listes) ;
- `Enigme_12/Reprise_2026-10-13/README.md` (historique complet) ;
- `00_ETAT.md` (état général de la chasse).

---

## 1. Où on en est (en 8 lignes)

1. **É1 à É11 validées.** L'É11 arrive au **château Bayard** (Pontcharra), à 14 m près. Bayard est « le dernier chevalier » et, très probablement, le narrateur.
2. **Départ de l'É12** : le chemin de rempart de la **tour d'Avalon** (Saint-Maximin, Isère). C'est fortement supposé par les textes et la FAQ, **pas validé à 100 %**. Comme le lieu doit être accessible toute l'année (06-020), on part du **sommet de la butte, au sol** (esplanade ou rue du Rempart), pas du haut du donjon.
3. **3e et 11e** : chapitres III (la porte du verger) et XI (la fontaine de Narcisse) du *Roman de la Rose*, trad. Marteau. C'est la seule lecture qui passe toutes les contraintes dures de la FAQ. Le vers d'ouverture, « Dieu sut se montrer favorable », est le **vers 1524** de cette édition, l'année de la mort de Bayard.
4. **10 stades** = 1 850 m ± 1 % (1 831,5 à 1 868,5 m).
5. **Direction** : la lecture « lever du soleil le jour de la mort de Bayard » (R1) échoue sur la carte. La lecture « matin de Pâques 1524 » (R2, Veillée pascale), combinée à la visibilité depuis le sol de la butte, désigne **le pré A** (45.43057, 6.05462). C'est le **seul lieu visible vers le levant à 10 stades**.
6. Le **ruisseau du Tapon** longe le pré A. Le *Roman* (« je suivis le courant ») dit qu'on **descend**, l'eau à gauche, donc sur la rive droite.
7. **Jonction, grande roche, souche-majesté** : impossibles à voir à distance. Le LiDAR ne montre aucune roche près du pré A.
8. **Ciel de l'enluminure 9** : pas décodé. Les pierres sont des couleurs du blason (émeraude = vert, diamant = noir). Le croissant correspond au matin du 30/04/1524. Bayard est mort un samedi.

**Statut honnête : pas encore trouvé.** Le pré A est le meilleur candidat de clairière, sans être démontré.

---

## 2. Règles de travail (à respecter, toujours)

| Règle | Détail |
|---|---|
| **Aucune vérification sur place, jamais** | Tout se fait à distance : textes, FAQ, cartes IGN, LiDAR, cadastre, OSM |
| Images dans le dépôt | Uniquement des cartes tirées de données IGN (et les photos du jeu déjà présentes). **Pas de photos de tiers** |
| Notes de Guilhem | En **lecture seule**. On travaille dans `_Resolution/` |
| Contenu de l'énigme | **Ne jamais inventer** : textes recopiés mot à mot depuis les photos HD (IMG_4347 à 4359) |
| Discord | Lecture seule |
| Conclusions | Préférer « pas encore trouvé » à une fausse certitude |
| Indications vagues du narrateur | « tout près », « très proches », « dans le champ de vision » : **jamais chiffrées**. Elles servent à départager, jamais à exclure |
| Ordre de travail | **Les textes d'abord, la carte ensuite** |
| Objectif fixé par Guilhem | Une zone de **± 50 m** pour le coffre, avec **au moins 95 % de confiance** |

---

## 3. La méthode (le cycle à suivre pour chaque piste)

1. **Lire les textes** : l'énigme, l'intro « Amis aventuriers », les FAQ mot pour mot (`Communaute/faq_officielle_auteur.json` et la FAQ8). Lister les lectures possibles avec leurs appuis et leurs faiblesses.
2. **Écrire la règle avant le test** (pré-enregistrement). Par exemple : « la direction est le lever du soleil du jour X, vu du point Y ». **Commiter la règle avant de regarder la carte.** Sinon, on trouve toujours quelque chose a posteriori.
3. **Passer la piste à la grille** de `LISTES_enigme_et_FAQ.md` § 3 :
   1. nature des 3e/11e ;
   2. règle de placement ;
   3. une jonction dans une clairière, visible du rempart ;
   4. un ruisseau gardé à gauche jusqu'à une roche mouillée qui barre le passage ;
   5. domaine public, praticable en fauteuil avec aide ;
   6. le hasard.

   **Une piste qui échoue au point 4 n'est pas sauvée par les points 1 à 3.**
4. **Tester sur la carte** : IGN LiDAR HD (MNT et MNS), BD TOPO, OSM, cadastre, orthophoto.
5. **Faire un témoin au hasard** : combien de points tirés au hasard passeraient les mêmes filtres ? Une coïncidence à 25 % ne prouve rien.
6. **Consigner** dans `TEXTES_direction.md`, résumer dans `00_ETAT.md`, puis commit et push.

Codes des filtres FAQ (dans `LISTES_enigme_et_FAQ.md` § 2) :
- **D** = contrainte dure, élimine ;
- **Q** = indication qualitative, départage seulement ;
- **M** = consigne de méthode ;
- **R** = réponse qui écarte une idée ;
- **A** = ambigu, ne sert pas de filtre.

---

## 4. Tableau d'évaluation de l'énigme (mis à jour le 14/10)

Légende : ✅ acquis · 🟡 lecture solide, non validée · 🔴 ouvert

| # | Texte | Lecture actuelle | Statut |
|---|---|---|---|
| E1 | « Dieu sut se montrer favorable » | Vers 1524 du *Roman de la Rose* (Marteau, chap. XI) = année de la mort de Bayard ; « confirmateur de la zone » (07-088) | ✅ |
| E2 | « dix stades romains » | 1 850 m ± 1 %, en ligne droite | ✅ |
| E3 | « les troisième et onzième » | Chap. III (porte) et XI (fontaine) du *Roman de la Rose*. Règle de placement : voir E11 | 🟡 |
| E4-E5 | « Le roi avait rejoint les fées… aux portes d'Avalon » | Tour d'Avalon, Saint-Maximin | 🟡 (supposé, non validé) |
| E6 | « L'épée… la dernière clé » | « Une dernière intuition cruciale pour trouver la clairière » (FAQ8) : non trouvée. Le pommeau de l'épée réelle porte N-E-S-O | 🔴 |
| E7 | « Tombée par trois fois… » | Ouvert (Girflet ou Bedivere qui jette l'épée ? les trois chutes du Christ ?) | 🔴 |
| E8 | « Tout commence et tout s'achève » | Alpha et oméga ; cierge pascal (*Principium et Finis*) ; « dernier jour = premier jour » (07-107) | 🟡 |
| E9 | « J'entends le chant retentir » | *Exsultet* de la Veillée pascale (lecture R2) | 🟡 |
| E10 | « dernière veille au chemin de rempart » | Sommet de la butte d'Avalon, au sol (esplanade 45.42891, 6.03112 ou rue du Rempart). **Note : `LISTES` § 1 dit encore « sommet du donjon », c'est périmé** | 🟡 |
| E11 | « l'endroit m'est apparu au matin, illuminé par l'astre glorieux » | R2 : lever du soleil de Pâques 1524 (80-91°) → le pré A, seul lieu visible à 10 stades vers l'est. R1 (lever du 30/04/1524) échoue | 🟡 |
| E12 | « Dans la clairière, à la jonction des chemins » | Pré A ; trois jonctions candidates (§ 5 ci-dessous) | 🔴 |
| E13 | « j'ai suivi à senestre les eaux enchantées » | Le Tapon, en descendant, sur la rive droite (l'eau à gauche) | 🟡 |
| E14 | « jusqu'à la grande roche » | Rien de visible au LiDAR 0,5 m le long du Tapon. FAQ8 : la roche est mouillée et elle a peut-être un nom (pas de réponse) | 🔴 |
| E15 | « dix pas au nord, autant à l'est » | Mécanique, une fois la roche trouvée | — |
| E16 | « la souche-majesté » | On peut s'y asseoir (07-167). Mécanique | — |
| E17 | « huit derniers pas… le jour dernier » | 4 candidats, **à trancher** (§ 6 ci-dessous) | 🔴 |
| E18 | « la coupe du charpentier » | Le trésor, c'est la coupe de l'enluminure 9 (07-005) | ✅ |
| E19 | Bassin de l'enl. 9 (« contour de ces eaux », 07-052) | Comparé aux 41 plans d'eau de la BD TOPO à moins de 3 km : aucun ne ressemble. Lecture : la fontaine de Narcisse | 🔴 |
| E20 | Premier plan de l'enl. 9 | La scène finale : roche fendue, cascade, bassin, tronc couché, coupe | 🟡 |
| E21 | Ciel de l'enl. 9 | Voir § 7 ci-dessous | 🔴 |
| E22 | Enluminure 11 | « Carte rudimentaire » (FAQ8) ; aide à placer une partie des 3e/11e (07-239). Non exploitée | 🔴 |

### 4.1 Les lectures des 3e/11e passées à la grille
| Lecture | Un 13e existe (06-133) | Écharde sur le 11e, pas sur la 3e (07-068) | Suite ruisseau + roche | Verdict |
|---|---|---|---|---|
| **Chap. III et XI du *Roman de la Rose*** | ✓ (le chap. XIII a servi à l'É7) | ✓ | pré A + Tapon, roche non vue | **en tête** |
| Portes de la Jérusalem céleste | ✗ (12 portes) | ? | ✗ | rétrogradée |
| Fêtes des apôtres | ✗ | ? | non testée | fragile |
| Heures romaines | ✗ (12 heures) | ? | non testée | bute sur le 13e |
| Chemin de croix (14 stations) | ✓ | ✓ | pas de règle de placement | passe les D, inutilisable |

### 4.2 Les lectures de « au matin… l'astre glorieux »
| # | Lecture | Résultat sur la carte |
|---|---|---|
| R1 | Lever du soleil le 30/04/1524 julien (mort de Bayard), 63,7° depuis le haut de la tour | ✗ : rien de convenable à 10 stades, que l'on parte de la tour, du château Bayard ou de la rue du Rempart |
| **R2** | **Lever du soleil de Pâques 1524 (27/03 julien)**, de 80° à 91° : Veillée pascale, *Exsultet*, *Principium et Finis* | ✓ **pré A**, seul lieu visible depuis le sol de la butte |
| R3 | Simplement l'est (88-92°) | ✗ depuis la tour ; depuis le sol, la fenêtre ne contient pas le pré A (83-86°) |
| R4 | L'épée remise en place : axe des quillons de l'É1 (León → Foix), 83,6° (fenêtre 81,6-85,6°) | ✗ depuis le haut de la tour ; **depuis le sol, la fenêtre contient aussi le pré A** : deux lectures (R2 et R4) convergent. À noter dans `TEXTES_direction.md` |
| R5 | La droite de l'É11 prolongée | passe à 26,5 m de la jonction du Couvat (P3), mais une telle coïncidence arrive environ 24 fois sur 100 au hasard |

---

## 5. Coordonnées utiles (WGS84)

| Point | Lat, lon | Remarque |
|---|---|---|
| Donjon d'Avalon (sol) | 45.428888, 6.031015 | sommet de la tour à 437,6 m |
| Esplanade (table d'orientation) | 45.42891, 6.03112 | point de vue retenu |
| Rue du Rempart (BAN) | 45.429772, 6.03118 | voie publique, sentier du PDIPR |
| Château Bayard | 45.423611, 6.018889 | arrivée de l'É11 ; privé |
| **Pré A** (centre) | **45.43057, 6.05462** | 83-86° depuis l'esplanade ; traversé par une ligne à haute tension |
| J2, angle nord-ouest du pré A (3 pistes) | 45.43105, 6.05343 | jonction candidate |
| A1, angle sud-est (la piste entre en forêt) | 45.43010, 6.05463 | jonction candidate |
| J, passage du Tapon | 45.43054, 6.05309 | jonction candidate |
| Cabane au bout de la piste | 45.43021, 6.05380 | ce n'est pas une roche |
| R1, ravin du Tapon | 45.42944, 6.05466 | 1 848 m, 88,1° |
| P3, jonction du Couvat | 45.43288, 6.05406 | droite de l'É11 à 26,5 m |
| Lieu-dit « Tire Loup » | ~45.42638, 6.05388 | le loup du ciel ? |

---

## 6. Le « jour dernier » (8 derniers pas) : candidats à trancher

| Lecture | Direction | Appuis | Contre |
|---|---|---|---|
| Azimut du lever du soleil le 30/04/1524 | ~64° (environ 61° magnétique) | date validée par Guilhem | FAQ8 : « faut-il lever la tête vers le ciel pour trouver le jour dernier ? → Non » |
| Samedi (Bayard meurt un samedi, 7e jour) → VII sur la boussole de la carte | ouest (270°) | calcul du jour ; samedi = Saturne = sable = diamant (l'ancre du ciel) | la règle de lecture de la boussole n'est pas confirmée |
| Dimanche, « dernier jour = premier jour » (07-107) → I | nord (0°) | l'auteur prend lui-même l'exemple du nord (03-027 : « si vous commencez au nord ») | pourrait n'être qu'un exemple |
| VIII, dernier chiffre de la boussole | nord-ouest (315°) | « dernier » | rien d'autre |

La boussole de la carte est graduée de **I à VIII** dans le sens horaire (I = N, III = E, V = S, VII = O). Ce remplacement des directions par des chiffres romains « est vraiment important » (01-117). Il existe « une aide » pour s'en servir (07-110).

---

## 7. Ciel de l'enluminure 9 : état des lectures

Dessins, de gauche à droite : loup + glyphe (☿ manuscrit ?), étoile à 5 branches (forme de l'étoile de Bethléem), arc-en-ciel à 6 bandes, âne + émeraude, ancre + diamant, puis, derrière l'arbre, un croissant doré **décroissant**.

| Lecture | Ce qui colle | Ce qui manque | Statut |
|---|---|---|---|
| **Couleurs du blason** (pierre ou planète → couleur) | émeraude = sinople, diamant = sable, ☿ = pourpre, lune = argent. Répond à « un seul élément », « les astres aident », « héraldique », « code universel » | ce que désignent « âne de sinople », « ancre de sable » | **la clé la plus probable** |
| Parcours final de l'É12 | âne dans le vert = clairière, ancre noire = roche, arbre = souche, croissant doré = coupe | ne donne aucune position | plausible |
| Jours de la semaine (planète → jour) | ancre + diamant = Saturne = samedi = jour de la mort de Bayard | une chance sur sept par hasard | à creuser avec E17 |
| Éléments chimiques | W, Ir, Be, C, Se | rien pour l'âne ni l'ancre | faible |
| Douze tribus | Zabulon (ancre + diamant) | l'âne d'Issacar a le saphir, pas l'émeraude | partielle |
| Lieux-dits autour du pré A | Tire Loup | rien d'autre | écartée |
| Semaine sainte | tout colle | c'est une histoire, ce qu'exclut 07-134 | écartée |

---

## 8. TODO (par priorité)

- [ ] **Trancher le « jour dernier »** (§ 6) par les textes et la FAQ, en écrivant la règle avant de regarder la carte.
- [x] ~~**Choisir la jonction du pré A**~~ → **sans objet** : le pré A échoue aux contraintes éliminatoires (14/10 soir, voir l'encadré ci-dessous).
- [ ] **NOUVEAU (priorité 1) : revoir le modèle « 3e = départ, 11e = endroit à 10 stades »**. Modèle M2 écrit le 14/10 (`R1410b_annonces_FAQ8_public_proche.md` § 2) : les 3e/11e sont deux points à 10 stades l'un de l'autre, trouvés depuis le rempart, et c'est leur segment + le ciel qui désigne la clairière (le coffre « pas loin du rempart », 06-244). À tester en appliquant d'abord le filtre public / bâti / monument (règle officielle du 02/07).
- [ ] **NOUVEAU : forêts communales de Saint-Maximin à l'est** (A 409-411, A 173 ; 2,3-2,7 km, caps 84-89°, donc dans la fenêtre de Pâques R2) : seules terres publiques boisées vers le levant. Chercher une règle textuelle qui y mène avant de les regarder de près.
- [ ] **E22 à rétrograder** : FAQ8 « une fois au départ de l'É12, vous pouvez oublier l'enluminure 11 ».

> **Mise à jour du 14/10 au soir (poste Windows)** — `Enigme_12/Reprise_2026-10-13/R1410_controle_eliminatoire_preA.md` et `PONT_branches.md`.
> - **Le pré A échoue aux contraintes éliminatoires** (domaine public, loin du bâti) : la rive droite du Tapon devant le pré est privée ; les seules parcelles communales de la rive entourent un **réservoir d'eau** (la « cabane » = BD TOPO `reservoir`, probable périmètre de captage). J2 est à 18 m d'une grange.
> - Sur **tout** l'anneau des 10 stades, le domaine public loin du bâti ne touche que des champs (nord), une zone d'activités (ouest) et une forêt communale à 145° (croupe à 850 m, jonction de 3 chemins à 1 834 m, mais ruisseau à 384 m et aucune lecture du texte ne donne ce cap).
> - Même conclusion que l'entonnoir cadastral du 11/10 de l'autre branche (copié dans `Enigme_12/Apport_happy-feynman_0610-1110/`). **Une hypothèse de la chaîne est fausse** : d'abord « l'endroit est à 10 stades du départ », puis le départ, puis la visibilité prise au sens strict.
- [ ] **Ciel de l'enl. 9** : chercher ce que désignent « âne de sinople » et « ancre de sable » dans la zone (armoiries de seigneurs locaux : Avalon, Alleman, Terrail ; bornes ou croix armoriées ; *Armorial du Dauphiné*).
- [x] **Discord (lecture seule)** : lu le 14/10 (`R1410b_…` § 1). Rien sur les 3e/11e ; l'annonce officielle du 02/07 impose d'exclure privé, monuments et tout bâti. Personne ne lit les pierres comme des émaux (recherches « sinople », « émaux », « ancre diamant » : rien sur l'enl. 9 dans ce sens ; des joueurs ont essayé pierres de naissance → jours de la semaine, juin 2025).
- [ ] **E6, l'épée « dernière clé »** : la face représentée sur la planche, les pattes de dragon qui enserrent le calice (07-048), le pommeau N-E-S-O.
- [ ] **E22, l'enluminure 11** comme « carte rudimentaire » pour placer les 3e/11e (07-239).
- [ ] **E7, « tombée par trois fois »** : identifier l'épisode.
- [ ] **E19, contour du bassin** : le comparer à des formes plus larges (lacs connus, contour d'une commune, d'une parcelle), pas seulement aux plans d'eau proches.
- [x] Mettre à jour `LISTES_enigme_et_FAQ.md` § 1 (E10 : la butte au sol, pas le haut du donjon). Fait le 14/10.
- [ ] **Décision de Guilhem** : envoyer ou non à l'auteur une capture vue du ciel du pré A et la description du parcours (07-078 l'autorise ; FAQ8 : une solution par mois est lue en détail). **Avis du 14/10 : ne pas l'envoyer en l'état**, le pré A ne passe pas « domaine public / loin des bâtiments » ; ce serait griller l'envoi du mois.

---

## 9. Reprendre les calculs sur un autre ordinateur

**Prérequis** : Python 3 avec `numpy`, `pillow` et `shapely` (`pip install numpy pillow shapely`), plus `curl`. Les données IGN sont publiques et sans clé (`data.geopf.fr`).

**Scripts** (dans `Enigme_12/Reprise_2026-10-13/scripts/`). Pour les trois premiers, se placer dans un dossier de données vide, par exemple `~/exk_data/dem` :

| Script | Rôle |
|---|---|
| `getdem.py` | MNT 2 m (RGE ALTI) autour de la tour → `dem2m.npy` et `.json` (~28 Mo) |
| `getmns.py` | MNS LiDAR HD 2 m (arbres et bâtiments) → `mns2m.npy` et `.json` |
| `getbig.py` | MNT 20 m sur 25 km, pour l'horizon lointain → `big20m.npy` et `.json` |
| `get05.py LAYER OUT lat lon demi-côté` | LiDAR 0,5 m local, par exemple autour du pré A |
| `wfs.py COUCHE lat_min lon_min lat_max lon_max sortie.json` | BD TOPO, par exemple `BDTOPO_V3:troncon_de_route 45.39 5.97 45.47 6.09 troncon_de_route.json` (idem `troncon_hydrographique`, `batiment`, `zone_de_vegetation`) |
| `ring_all.py DEM CALC [dmin dmax]` et `ring_center.py` (variable `CENTER="lat,lon"`) | jonctions de chemins dans l'anneau de 10 stades. `CALC` doit contenir `troncon_de_route.json` et `osm.json` |
| `viewshed_point.py DEM` (variables `VIEW="lat,lon"`, `EYEH=1.7`, `OBST=mns`) | ce qu'on voit depuis un point au sol |
| `los_scan.py` | ligne de vue entre un point et des cibles |
| `horizon_lib.py` | horizon réel et premier rayon de soleil pour une date |
| `lune_1524.py DEM [H_esplanade.npz]` | phase et lever de la lune en 1524, vus de l'esplanade |
| `emprunts_rdlr.py` | emprunts au *Roman de la Rose* (Gutenberg 16816) |

**Données légères déjà dans le dépôt** (`Enigme_12/Reprise_2026-10-13/data/`) :
- `osm_zone_avalon.json` : chemins et cours d'eau OSM. Overpass était bloqué dans l'environnement de Claude. À copier sous le nom `osm.json` dans le dossier CALC.
- `lieux_dits_saint_maximin_38426.json` : lieux-dits du cadastre (Etalab).
- `H_esplanade.npz`, `H_top_mnt.npz`, `horizon_pts_mnt.npz` : horizons réels déjà calculés (esplanade, haut de la tour).

Les gros fichiers (MNT/MNS de 28 Mo, champs de vision de 70 Mo) ne sont pas dans le dépôt : on les régénère avec les scripts ci-dessus.

**Avec Claude**, un bon message de départ :
> « Lis `vault_EXKALIBUR/_Resolution/TODO_REPRISE_E12.md`, puis `Enigme_12/Reprise_2026-10-13/TEXTES_direction.md`. Respecte les règles du § 2 et la méthode du § 3. Reprends le TODO au premier point non coché. »
