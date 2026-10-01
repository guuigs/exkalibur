# BRIEF commun — vague 1 (01/10/2026) — énigme 12 Exkalibur

Tu es un sous-agent. Tu ne peux pas poser de questions à l'utilisateur. Réponds en français. Tu écris UNIQUEMENT dans `C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/` (fichiers préfixés par ton Id) ; fichiers lourds dans `C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/`. N'écris jamais dans les notes de l'utilisateur. Ne poste jamais sur Discord. Pas de navigateur disponible (Chrome fermé) : utilise Python (urllib avec User-Agent « Mozilla/5.0 (research script) », API Wikipedia/Commons, miroir Overpass `https://overpass.openstreetmap.fr/api/interpreter` en POST, IGN data.geopf.fr) et `web_extract`.

## Sauvegarde continue
Crée `<Id>_notes.md` au 1er appel, avec un en-tête `## REPRISE` (Fait / En cours / Prochaines étapes / Écarté), mis à jour après chaque piste. Si le fichier existe, tu es une reprise : lis-le d'abord. Budget ≈ 40 appels. Rends un rapport `<Id>_rapport.md` + un résumé de 12 lignes.

## Règles de méthode
- Sépare FAIT / HYPOTHÈSE / INTUITION avec une confiance. Ne dis « 95 % » que si un décompte ou un contrôle le justifie.
- Chaque contrainte que tu utilises est étiquetée : TEXTE de l'énigme, RÉPONSE de l'auteur (champ `a` du JSON FAQ), ou question de joueur (champ `q`, la réponse de l'auteur étant seule valide).
- Toute citation du texte de l'énigme doit être trouvée mot pour mot dans le texte ci-dessous.
- Tout calcul par script archivé avec sa sortie ; teste toujours contre un témoin aléatoire (autres distances, autres points) : à ±1 % beaucoup de chaînes « tombent juste ».
- Ne reprends pas les pistes écartées (liste ci-dessous) sauf pour une raison nouvelle écrite.
- Une idée n'est retenue que si un OBJET RÉEL existe sur le terrain ou dans les données.

## Texte de l'énigme 12 (Ad vitam aeternam), verbatim
> Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. Le roi avait rejoint les fées, et laissé son épée aux portes d'Avalon. L'épée, évidemment. L'épée, depuis toujours ! Là était la dernière clé de la quête du Graal. Tombée par trois fois, elle était revenue là où elle n'avait jamais cessé d'être.
> Tout commence et tout s'achève. J'entends le chant retentir. J'ai fait une dernière veille au chemin de rempart, et l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau.
> Dans la clairière, à la jonction des chemins, j'ai suivi à senestre les eaux enchantées jusqu'à la grande roche, puis fis dix pas au nord, autant à l'est. Arrivé à la souche-majesté, je fis huit derniers pas, et ma boussole suivait le jour dernier.
> Là, tu trouveras la coupe du charpentier.

## Données et chemins
- FAQ officielle de l'auteur (dict, ~10 000 entrées `{q, a, theme}`) : `.../_Resolution/Communaute/faq_officielle_auteur.json` (clés FAQ0x-yyy). Transcription vidéo FAQ 8 (texte brut nettoyé) : `C:/Users/Admin/AppData/Local/hermes/cache/scratch/faq8.txt`.
- Dossier de travail : `.../_Resolution/Enigme_12/solution.md` (état + rétractations), `PLAN_ACTION.md`, `Revue_globale/00_SYNTHESE.md`, `Enigme_11/solution.md`, `Enigme_10/solution.md`, `00 - Solutions validées.md` (racine EXKALIBUR).
- Helpers : `exec(open(r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py",encoding="utf-8").read())` (hav, brg, faq()…).
- IGN local (GeoJSON BD TOPO, 12 km autour de la tour) : `C:/Users/Admin/AppData/Local/hermes/cache/scratch/ign/*.geojson` (toponymie_12km, troncon_hydrographique_12km, troncon_de_route, zone_de_vegetation, batiment, foret_publique_12km, construction_ponctuelle_12km…).
- LiDAR HD MNT 2 m : `.../exk_e12/mnt_1500_2.npy` (2000×2000, lignes = nord→sud, méta `lidar_meta_1500.json` BB=[45.4107,6.00518,45.44689,6.05638]), accumulation `acc_1500_2.npy`, D8 `d8_1500_2.npy`, viewshed tour 3 km `viewshed_tower_3000.npy`, bâtiments `bldg_la.npy/bldg_lo.npy`, nœuds du réseau pédestre OSM `reseau_gresivaudan_noeuds.json`.

## Faits acquis (nœuds)
- É1-É11 résolues. É10 : Machrie Moor (Arran), distance Eilean Donan→Machrie Moor = 193,13 km. É11 : Saint-Palais ×π (606,74 km, cap 64,99°) → **château Bayard à ~50 m** (45.4242, 6.0179). Tour d'Avalon = 45.429083, 6.030808 (1,08 km plus loin sur la même droite ; consensus Discord, non prouvé). Aucun « chemin de rempart » cartographié à proximité (IGN/OSM) ; Fort Barraux (45.4356, 5.9871) a de vrais remparts (écart 1,8 km).
- « Jour dernier » = 30/04/1524 (mort de Bayard), validé par l'utilisateur ; 8 derniers pas ≈ 12 m, donc **hors sujet pour une zone de 50 m**.
- 10 stades romains = 1 850 m (1 832–1 868 m à ±1 %).

## Réponses de l'auteur à utiliser (verbatim abrégé, `a`)
- FAQ04-115 : « Vous allez directement de la troisième à la onzième, mais ça va vous amener, vous verrez, à passer par des **étapes intermédiaires**. »
- FAQ07-120 : « Il y a bien une distance en **ligne droite** qui sépare les 3e et 11e. Toute la question, c'est de savoir quels sont ces 3e et 11e et comment les positionner par rapport à un point de départ. »
- FAQ06-166 : « Le chemin de rempart est un point de départ… après, c'est l'astre glorieux qui vous indique où aller. C'est là que les 3e et 11e seront utiles pour résoudre cette énigme. »
- FAQ07-180 : « Ne soyez pas obnubilé par la direction de l'astre glorieux… Ce qui compte, c'est de vraiment identifier les 3e et 11e et de voir ce que vous en faites avec la distance, le point de départ qui vous est donné. »
- FAQ07-152 : « l'astre glorieux… une relation avec le ciel pour trouver la direction et pour trouver l'endroit où vous allez arriver depuis le rempart. » ; FAQ8 : « l'astre glorieux vous guide en tout dernier lieu » ; « faut-il lever la tête vers le ciel pour trouver le jour dernier ? Non. »
- FAQ07-133 : 3e/11e « d'une aide plus que précieuse » pour identifier la clairière. FAQ05-068 : « vous rapprochent grandement du trésor ». FAQ07-281 : ne servent pas de confirmateur du tracé de l'ultime traversée, « quelque chose de plus important ».
- FAQ06-009 : même nature. FAQ06-216 : un seul de chaque. FAQ06-133 : le 13e « ne vous mènerait pas au bon endroit » (série ≥ 13). FAQ8 : 8e/16e « non, sinon ça aurait été incorrect » (les rangs comptent). FAQ04-114 / FAQ8 : trouvables de chez soi. FAQ07-063 : deux points à placer, respectivement 3e et 11e. FAQ05-074 : pas visibles sur Maps malgré la mesure, mais on pointe deux points. FAQ06-227 : question « se voient sur Maps ? » → « vous n'avez pas encore correctement identifié ce que peuvent être les 3e et 11e ». FAQ07-187 : visibles sur Maps ? NRP. FAQ07-156 : pas « un ensemble de 52 sur le chemin des remparts ». FAQ06-247 : « il faudra marcher surtout sur l'une des deux ». FAQ07-068 : pieds nus, pas d'écharde sur la 3e, « sur le onzième, oui, c'est possible » (réponse à une question de joueur, pas dans le texte). FAQ07-239 : l'enluminure 11 aide à en placer « une partie ». FAQ05-093 : visibles sur les enluminures = « l'une des clés ». FAQ04-027 : « Les enluminures, la carte ou les énigmes… Tout est codé et vous permet de trouver les 3e et 11e. » FAQ8 : l'ordre qui les définit = liste universelle (mois, apôtres, zodiaque) ? → NRP ; matériaux différents ? → NRP ; texte ancien de 1 500 ans ? → NRP ; « l'essai », la boussole de la carte : non ; l'énigme É12 « lever la tête… non » ; FAQ8 : « une dernière idée, une dernière intuition qui sera cruciale pour trouver la clairière » ; FAQ8 : l'endroit sur l'île au sud d'Omnia aide à décoder l'enluminure 11 (« oui, tout à fait »), E11 = « carte rudimentaire » (oui), pierres à chiffres et pierres à symboles = deux cryptos distinctes, jeu de cartes de l'E11 « vous en aurez besoin, mais pour autre chose ».
- Terrain : FAQ06-025 chemin de rempart ≠ chemin de la jonction « même s'ils sont très proches » ; FAQ06-005 jonction = croisement de sentiers au sens premier ; FAQ05-155 « l'endroit est dans le champ de vision » depuis le rempart ; FAQ06-090 pieds mouillés possibles avant la roche, pas après ; FAQ8 grande roche « bloque vraiment le chemin » ; FAQ05-107 coffre éloigné de tout bâtiment ; domaine public, ni monument historique, ni zone protégée (FAQ8 : forêt publique autorisée).

## Pistes déjà écartées (ne pas refaire sans raison nouvelle)
Pierre Tombante (cascade cachée par la crête) ; paires de ponts/croix/passerelles BD TOPO à 1 850 m (niveau du hasard) ; paires de toponymes à prénom d'apôtre à 1 850 m (0) ; chemin de croix extérieur près de la tour (aucun, OSM) ; zones « Chêne-Roche-Vivier / Pierre Gros / Corbassière » (coïncidences de noms, bâtiments à < 90 m) ; raisonnement « agrégation cryptographique É11 » (rejeté par l'utilisateur) ; Machrie Moor 3/11 pris tels quels à ~190 m (échelle) — à ré-examiner seulement par T12-B.
