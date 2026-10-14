# BRIEF commun — sous-agents É12 (06/10/2026). À lire en entier avant toute action.

Langue : FRANÇAIS pour tout (rapports, notes, résumé final). Ton : factuel, sobre, « pas encore trouvé » plutôt qu'une zone séduisante.

## Le jeu
Chasse au trésor « Exkalibur » (Unsolved Hunts / Puy du Fou, auteur Arthur Pendragon / « Étienne »). 12 énigmes, 1 à 11 résolues par nous (validées par Guilhem, pas par l'auteur). Il reste l'**énigme 12 « Ad vitam aeternam »** : trouver un petit coffre enterré (~40 cm de profondeur), précision « pile-poil » au mètre.
Dépôt : `C:/Users/Admin/Projects/exkalibur` (branche `claude/happy-feynman-p7xsyy`). Dossier de travail : `vault_EXKALIBUR/_Resolution/`. Outils/scripts : `outils_scratch/`, données : `donnees_travail/`, images : `images_travail/`. Photos HD des enluminures et du parchemin : `C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Sources/photos_HD_2026-09-29/` (INDEX.md). Planche numérotée : `images_travail/PLANCHE_enluminures_numerotees.jpg`.

## Texte de l'É12 (verbatim)
> Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. Le roi avait rejoint les fées, et laissé son épée aux portes d'Avalon. L'épée, évidemment. L'épée, depuis toujours ! Là était la dernière clé de la quête du Graal. Tombée par trois fois, elle était revenue là où elle n'avait jamais cessé d'être.
> Tout commence et tout s'achève. J'entends le chant retentir. J'ai fait une dernière veille au chemin de rempart, et l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau.
> Dans la clairière, à la jonction des chemins, j'ai suivi à senestre les eaux enchantées jusqu'à la grande roche, puis fis dix pas au nord, autant à l'est. Arrivé à la souche-majesté, je fis huit derniers pas, et ma boussole suivait le jour dernier.
> Là, tu trouveras la coupe du charpentier.

## État acquis (à NE PAS refaire)
- Départ = arrivée de l'É11 (Saint-Palais → château Bayard, D×π à ~50 m ; prolongé de ~1 km : tour d'Avalon, Saint-Maximin, Isère). « Chemin de rempart » = chemin d'un mur ou d'une tour (FAQ8), point précis, accessible toute l'année. Probable, non validé officiellement.
- 3e et 11e : deux points de même nature, distants de 10 stades (1 850 m ±1 %) en ligne droite, trouvables de chez soi sur carte mais « pas visibles sur Maps » ; pas d'écharde sur le 3e, possible sur le 11e ; le 13e existe mais mène ailleurs ; 8e/16e « incorrects » (les rangs comptent). Personne ne les a identifiés (FAQ, Discord au 04/10 : « quelqu'un a progressé sur les 3e et 11e ? » sans réponse).
- Jour dernier retenu : 30/04/1524 (azimuts 63,7° / 68,6° / 73,9°). Coffre sur domaine public, loin de tout bâtiment (≥ 100 m), accessible en fauteuil avec accompagnateur ; **zone dans Pontcharra interdite** (décision de Guilhem).
- L'organisateur (01/10) : « fin de chasse très ouverte, nombre de chasseurs très proches, cela se jouera sur des détails » ; 3 équipes à < 150 m du coffre (juin).
- **Registre des pistes déjà écartées : `Enigme_12/PISTES_ECARTEES.md` — le lire AVANT d'inventer. Contraintes FAQ verbatim : `Enigme_12/FAQ_CRITIQUES_E12.md`. Synthèse : `Enigme_12/00_SYNTHESE_E12.md`. FAQ complète (1 852 Q/R, JSON) : `vault_EXKALIBUR/_Resolution/Communaute/faq_officielle_auteur.json` + `outils_scratch/faq8.txt`.**
- Déjà écartés (liste courte) : Machrie Moor, chemins de croix, ponts, pylônes, bornes, constellations posées sur la carte, rose des vents, SATOR, tarot/cartes, apôtres en table/rangée, Hercule, calque de l'épée, fils de Jacob (5 placements), croix PATERNOSTER comme mécanisme, heures solaires 3/11.

## Règles de travail (Guilhem)
1. Pas de visite sur place, pas de demande de photos à Guilhem. Aucune action hors vault, web et dépôt GitHub. Discord : lecture seule, et les sous-agents n'y touchent pas.
2. Jamais de secret/mot de passe dans un fichier ou un message.
3. On n'invente JAMAIS le contenu d'une énigme ni une citation. Fait / hypothèse / intuition, avec un niveau de confiance.
4. **Test du hasard obligatoire** : toute coïncidence (anagramme, distance, alignement, correspondance de lieu) doit être comparée à une référence aléatoire (tirage de contrôle, miroir, décalage, autre ancre) avec un décompte. Une piste n'est dite « fiable » que si elle (a) dérive d'une règle posée AVANT de regarder le terrain, sans paramètre libre ajusté, (b) tient TOUTES les contraintes FAQ_CRITIQUES, (c) a un hasard ≤ 2 % et (d) est contrôlée de façon indépendante.
5. Ne pas se rabattre sur du bruit : si rien ne tient, le dire clairement. « Rien de fiable » est une réponse acceptable et attendue la plupart du temps.
6. Les scripts vont dans `outils_scratch/` (préfixe `r0610_`), les rapports dans `vault_EXKALIBUR/_Resolution/Enigme_12/R0610_<ID>_<sujet>.md`. Ne pas modifier les autres fichiers. Pas de commit (l'orchestrateur le fait).
7. Réponse finale : ≤ 300 mots, avec (i) verdict (FIABLE / PISTE FAIBLE / RIEN), (ii) chemin absolu du rapport, (iii) 3 faits les plus importants, (iv) ce que tu recommandes de tester ensuite. Les résumés d'enfants sont des auto-déclarations : fournis des chemins vérifiables.
8. Réseau : web_search / web_extract (Firecrawl) sont disponibles. Pas de navigateur partagé. Python : `python3`.
