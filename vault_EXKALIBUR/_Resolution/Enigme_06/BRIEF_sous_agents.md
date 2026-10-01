# BRIEF COMMUN — Énigme 6 « Libera nos a malo » (à lire par chaque sous-agent)

Chasse au trésor **Exkalibur** (Puy du Fou / Unsolved Hunts, auteur Étienne Picand). 12 énigmes + 12 enluminures + 1 carte. Coffre enterré dans l'un de 6 pays (PT, ES, AD, FR, UK, IE).
Dossier : `C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/` (noté `R/`). **Lecture seule**, sauf ton fichier de notes et tes scripts (voir ta tâche).
Python : `python` = 3.11 ; mets `sys.stdout.reconfigure(encoding="utf-8")`. Terminal = bash (git-bash) sous Windows, chemins `C:/...`.
Recherche web : l'outil `web_search` est en panne (Firecrawl 403). Utilise plutôt `python C:/Users/Admin/AppData/Local/hermes/cache/scratch/ddg.py s "requête"` (DuckDuckGo) et `python .../ddg.py f URL` (lecture d'une page), ou `curl`. `web_extract` peut marcher.

## Acquis (faits, ne pas re-vérifier)
- É1 : épée León–Foix–Valence–Urquhart. É2 : Londres / **Tour de Londres** = « tour-krak ». É3 : Tintagel. É4 : Tintagel → Silchester → Westminster. É5 : Stonehenge + **Carnac** (1er « C » du jeu : l'énigme 5 finit par un code « …3-C » = CARNAC).
- **Mode « shark »** : une résolution **officiellement validée** (auteur, FAQ) = fait. Une **rumeur** de joueur = piste marquée [RUMEUR], jamais un fait.

## Texte exact (photo HD `R/Enigme_06/hd/texte_E6_IMG4353.jpg`)
> *Libera nos a malo*
> « Il est des forces occultes en ce monde, dit le roi, qui ne dorment jamais. Nous autres, pauvres chevaliers, avons une mission : les combattre. C'est à jamais notre devoir. » Sur ces dires, le roi fit convier l'enchanteur, et celui-ci les avertit : « preux chevaliers, un avenir m'est apparu, et cet avenir est funeste. Le Sépulcre court un grand danger. Il vous faudra porter la guerre très loin de vos terres, pour protéger la coupe de Vie. Vous en serez les dépositaires. Voilà votre quête, qui ne connaîtra pas de fin. »
> Observe la partie, preux contre dieux. Commencera le Père, et finiront les cieux.
> Tu as les 4 C, relie-les une à une. Depuis la tour-Krak, en passant par le champ de bataille, parcours la même distance jusqu'à te recueillir dans ce lieu très Sainte.

Énigme suivante (É7, *Sub rosa*, liée par le « lieu très saint ») : « Bayeux Evad. Ecfv / Parti au combat, et blessé d'un coup de lance, le roi la récupéra, non sans l'avoir essuyée, et l'offrit à sa dame après le combat. "Vous êtes blessé mon roi ?" Mais non, le trait qui l'a percé, goutte de sang n'avait versé. Depuis le lieu très saint, suis la déroute devant le Conquérant, et trace la nouvelle garde. Elle s'achève à l'Orient, à travers les bois qui mènent à la cité de l'Autre Monde. »

## Enluminure de l'énigme (panneau rangée 4 gauche = « enluminure 7 » dans la numérotation de l'auteur)
Images : `R/Enigme_06/hd/R4G_panneau_IMG4334.png` (600×410, net) et `R4G_panneau_x3.png` (agrandi) ; `R4G_cloches_x3.png` ; planche entière `R/Sources/photos_HD_2026-09-29/IMG_4334.JPEG`. Utilise `vision_analyze` avec `region` pour zoomer.
- **Plateau** : 3 carrés concentriques + médianes = **24 intersections** (géométrie du jeu du moulin ; l'auteur refuse de confirmer ce nom). Cercle **« 10 »** au centre.
  - Coordonnées 7×7 (col, ligne ; ligne 0 = haut). Points : extérieur (0,0)(3,0)(6,0)(6,3)(6,6)(3,6)(0,6)(0,3) ; moyen (1,1)(3,1)(5,1)(5,3)(5,5)(3,5)(1,5)(1,3) ; intérieur (2,2)(3,2)(4,2)(4,3)(4,4)(3,4)(2,4)(2,3).
  - **Rouges (sphères), 7** : (3,0)(1,3)(1,5)(3,5)(0,6)(3,6)(4,3).
  - **Bleus (tuiles), 7** : (0,0)(6,0)(1,1) **illustrés** ; (3,1)(4,2)(5,3)(5,5) unis. Positions à revérifier sur l'image HD.
  - **Hors plateau** : rouge « **S** » (lu S, non 5) et bleu « **T** » sur un pied, près de l'ange.
- Au-dessus : **3 clochers** (tour carrée, clocher octogonal, flèche). Sous eux, le mot hébreu **אמן (« Amen »)**.
- **Pape** mitré, à gauche. **Ange** (Gabriel) et **Vierge** (Annonciation), à droite. **Personnage roux au casque ailé** tenant un anneau et une tige.
- « **HAROLD REX INTERFECTUS EST** » vertical. « **MLXVI** » entouré de **4 cloches** dorées **reliées par un pointillé**. Livre jaune au sol.

## Contraintes officielles (FAQ de l'auteur : `R/Enigme_06/faq_e6.md`, base complète `R/Communaute/faq_officielle_auteur.json`)
- Les 4 C sont **à identifier dans cette énigme** (FAQ03-092). Il y a d'autres C ailleurs dans le jeu.
- « Dans Libera, le jeu donne-t-il des anagrammes exacts ? » → « Oui. L'anagramme vous permet en effet de correctement identifier le lieu sans problème. **Pas forcément que le lieu** d'ailleurs. » (FAQ04-189). Anagrammes parfaites, selon la langue et la prononciation (FAQ03-058, 04-185).
- « Observe la partie » : seulement l'observer, pas la jouer (FAQ03-332). Le jeu du moulin n'est ni confirmé ni infirmé (FAQ03-326).
- Identifier à quoi ou à qui correspond chacun des pions bleus (question sur les pions non illustrés) : « ça pourrait vous être très utile » (FAQ03-265).
- Les lettres des pions S et T ne sont pas remplaçables (FAQ03-354). Le T n'est pas relié au T de « EST » (FAQ03-233). Les couleurs auraient pu être autres (FAQ03-257). Les 3 clochers auraient pu être ailleurs (FAQ03-272).
- Il y a un **ordre évident** pour relier les C (FAQ03-101) ; on peut les placer dans l'ordre, sans aller-retour (FAQ03-279).
- « Parcours la même distance » = la même distance **que** les 4 C (longueur de la chaîne, FAQ03-047). Cette distance resservira (FAQ07-160).
- Le lieu très Sainte **n'est pas** un des C (FAQ03-099). C'est le même lieu que le « lieu très saint » de Sub rosa (FAQ03-005). Le « e » de Sainte est une aide volontaire (FAQ03-070, 03-288).
- Tour-krak = Tour de Londres (FAQ04-010). « Champ de bataille » = « le lieu qui porte le nom du champ de bataille » (FAQ03-038), donc probablement la ville de **Battle** (Senlac, 1066).
- La chaîne de tous les C ne croise pas la lame de l'épée d'É1 (FAQ07-166). Tolérance : >1 % d'écart = très mauvais signe (FAQ02-277).
- L'auteur déconseille l'IA et Google Lens pour identifier les modèles des figures : l'enlumineuse s'inspire parfois de modèles sans rapport (FAQ03-030, 03-119).

## Déjà établi par les solveurs précédents (ne pas refaire)
- Tour de Londres → Battle → Sainte-Chapelle : **D = 341,6 km**, trois points quasi alignés. Mais l'alignement **ne prouve rien** : l'axe Londres→Battle pointe de toute façon sur le centre de Paris (`calculs/solveurB_06c_*`).
- La contrainte de distance seule **ne discrimine pas** : des dizaines de chaînes de 4 C tombent dans ±1 % (`solveurB_08`, `solveurA_chaine`). Chaînes repérées : Clermont–Cluny–Cîteaux–Clairvaux 340,99 km (ordre = plus court chemin) ; Clermont–Cadouin–Cahors–Conques 341,87 km. **Rien n'est validé.**
- Solveur A (`solveurA_notes.md`) : ont échoué, au niveau du hasard, les lectures position → alphabet 23/24/26, les anagrammes de 31 phrases, preux × dieux et les ensembles de dieux. Il travaillait sur la photo basse définition.

## Sauvegarde continue (OBLIGATOIRE — la session peut être coupée à tout moment)
- Crée `R/Enigme_06/<prefixe>_notes.md` **dès ton 1er appel**, et mets-le à jour **après chaque piste testée**.
- En tête, une section `## REPRISE` toujours à jour : **Fait** (1 ligne par piste : résultat + script), **En cours**, **Prochaines étapes** (précises, actionnables), **Écarté** (+ raison).
- Si ce fichier existe déjà, tu es une **reprise** : lis `## REPRISE`, ne refais rien de ce qui est marqué Fait, et continue les Prochaines étapes.

## Règles de travail
- Tout calcul par du **code**, archivé dans `R/Enigme_06/calculs/` avec **ton préfixe** (script + `.out.txt`). Aucune anagramme « vue à l'œil » : compare des multisets de lettres.
- **Test du hasard obligatoire** pour tout hit : la même méthode sur des entrées quelconques donne-t-elle autant ?
- Sépare fait / hypothèse / intuition, avec un niveau de confiance. Préfère « pas trouvé » à une construction ad hoc.
- **Budget** : vise 40 appels d'outils au maximum, et reste concis (l'usage Claude est limité).
- Sortie : ton fichier `R/Enigme_06/<prefixe>_notes.md`, puis une réponse finale de 12 lignes maximum.
