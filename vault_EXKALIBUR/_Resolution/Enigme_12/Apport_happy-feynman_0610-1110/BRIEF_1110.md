# BRIEF commun — sous-agents É12, vague du 11/10/2026. À lire en entier avant toute action.

Langue : FRANÇAIS. Ton factuel. « Rien de fiable » est une réponse acceptée.

## Le jeu
Chasse « Exkalibur » (Unsolved Hunts / Puy du Fou, auteur Étienne). Énigmes 1-11 résolues (validées par Guilhem). Reste l'É12 « Ad vitam aeternam » : petit coffre enterré, « pile-poil ». Personne ne l'a trouvé (Discord au 11/10). Personne n'a identifié les **3e et 11e** (verrou principal, FAQ06-109, 07-236).

Dépôt : `C:/Users/Admin/Projects/exkalibur` (branche `claude/happy-feynman-p7xsyy`). Travail : `vault_EXKALIBUR/_Resolution/`. Python avec numpy/scipy/shapely/pyproj/PIL : `C:/Users/Admin/Projects/exkalibur/.venv-exk/Scripts/python.exe`. Librairie terrain : `outils_scratch/r0610_C_lib.py` (mosaïque LiDAR 1 m 6×6 km autour de la tour, L93 ; ATTENTION : sa variable CANOPY est fausse — utiliser `L.MNH` directement, c'est déjà une hauteur 0-50 m ; DSM = MNT + MNH). Données BD TOPO/OSM : `donnees_travail/r0610_R_roches/`, `donnees_travail/r0610_C/` (jonctions.json : clés « lat » et « lon » INVERSÉES). Photos HD : `C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Sources/photos_HD_2026-09-29/` (+ INDEX.md ; IMG_4334 = planche des 12 enluminures, IMG_4333 = carte officielle, IMG_4342 = enl. 9 à tourner de −90°, IMG_4345 = enl. 11).

## Texte de l'É12 (verbatim)
> Dieu sut se montrer favorable ; dix stades romains séparaient les troisième et onzième. Le roi avait rejoint les fées, et laissé son épée aux portes d'Avalon. L'épée, évidemment. L'épée, depuis toujours ! Là était la dernière clé de la quête du Graal. Tombée par trois fois, elle était revenue là où elle n'avait jamais cessé d'être.
> Tout commence et tout s'achève. J'entends le chant retentir. J'ai fait une dernière veille au chemin de rempart, et l'endroit m'est apparu au matin, illuminé par l'astre glorieux qui magnifiait le ruisseau.
> Dans la clairière, à la jonction des chemins, j'ai suivi à senestre les eaux enchantées jusqu'à la grande roche, puis fis dix pas au nord, autant à l'est. Arrivé à la souche-majesté, je fis huit derniers pas, et ma boussole suivait le jour dernier.
> Là, tu trouveras la coupe du charpentier.

## Acquis (ne pas refaire)
- Départ : chemin de rempart près de la **tour d'Avalon** (Saint-Maximin, 38 ; tour 45.4288, 6.03078 ; Rue du Rempart 45.42977, 6.03118). Droite É11 Saint-Palais → Grande Chartreuse → château Bayard (82 m). ~65-70 %.
- Narrateur = **Bayard** (mort le 30/04/1524 = « jour dernier », lever ≈ 63,7°). Hugues d'Avalon (chartreux, évêque de Lincoln) né à Avalon.
- Pontcharra (commune 38314) exclu par décision de Guilhem pour la zone du coffre.
- Pistes mortes : `Enigme_12/PISTES_ECARTEES.md` + `references` « exkalibur-e12-tests » résumées dans `Enigme_12/R1110_audit_et_inverse.md`. LIRE AVANT D'INVENTER. Notamment morts : ponts/croix/bornes/pylônes/parcelles/PR routiers/sentiers patrimoine (9 étapes)/réseau points-nœuds (nommés), Machrie Moor, chemin de croix, constellations, apôtres-table, Hercule, SATOR/PATERNOSTER, heures solaires, chapitres III/XI (Loyal Serviteur, Roman de la Rose).

## Contraintes de l'auteur sur les 3e et 11e (FAQ ; texte complet : `Revue_globale/FAQ_E12_complet.md`, FAQ8 : `C:/Users/Admin/AppData/Local/hermes/cache/scratch/faq8.txt`, base JSON 1 852 Q/R : `Communaute/faq_officielle_auteur.json`)
C1 même nature (06-009) · C2 un seul de chaque (06-216) · C3 deux points à pointer sur une carte (05-074, 07-063) · C4 1 850 m ±1 % en ligne droite (05-172, 07-120) · C5 pas visibles sur Maps (05-074) · C6 trouvables de chez soi (04-114, FAQ8) · C7 pieds nus : pas d'écharde sur la 3e, possible sur le 11e (07-068) · C8 « il faudra marcher surtout sur l'une des deux » (06-247) · C9 « aurait-on pu aller jusqu'au 13e ? oui, mais le 13e ne vous mènerait pas au bon endroit » (06-133) · C10 « auraient-ils pu être les 8e et 16e ? non, sinon ça aurait été incorrect » (FAQ8) · C11 pas un ensemble de 52 (07-156) · C12 ne mènent pas à un chevalier (07-065) · C13 l'ordre qui les définit ≠ celui du « numéro un » d'Ultima Cena (04-051) · C14 « vous allez directement de la 3e à la 11e mais ça va vous amener à passer par des étapes intermédiaires » (04-115) · C15 « toute la question : quels sont ces 3e et 11e et comment les positionner par rapport à un point de départ » (07-120) ; « identifiez les 3e/11e et voyez ce que vous en faites avec la distance, le point de départ » (07-180) · C16 « les enluminures, la carte ou les énigmes : tout est codé et vous permet de trouver les 3e et 11e » (04-027) · C17 un joueur a identifié leur nature (06-259) · C18 « le ciel vous indique où aller, c'est là que les 3e et 11e seront utiles » (06-166) ; ils servent à identifier la clairière (07-133) · C19 « difficiles à trouver » (06-292) · C20 liste universellement connue (mois, apôtres, zodiaque) ? → « je ne pourrais pas répondre » (FAQ8, esquive) · matériaux différents ? → esquive (FAQ8).
Autres : clairière restée clairière (03-274), point précis (06-230), jonction = croisement de sentiers au sens premier (06-005), le chemin de rempart n'est pas l'un des chemins mais « très proche » (06-025), l'endroit est « dans le champ de vision » du rempart (05-155), roche « très difficile à manquer », mouillée, barre le passage (03-211, 06-195), coffre loin de tout bâtiment (05-107), domaine public.

## Règle de fiabilité (obligatoire)
Une piste est FIABLE seulement si (a) la règle est posée AVANT de regarder la carte, sans paramètre ajusté ; (b) elle tient C1-C20 ; (c) test du hasard par décompte (1 000 tirages ou contrôle équivalent) ≤ 2 % ; (d) chaque citation est vérifiée verbatim. Sinon : PISTE FAIBLE ou RIEN. Distinguer fait / hypothèse / intuition.

## Sauvegarde continue (obligatoire)
Crée `vault_EXKALIBUR/_Resolution/Enigme_12/R1110_<PREFIXE>_notes.md` au 1er appel, mets-le à jour après CHAQUE piste, avec un en-tête `## REPRISE` (Fait / En cours / Prochaines étapes / Écarté). S'il existe déjà, tu es une REPRISE : lis-le et ne refais pas ce qui est fait. Scripts : `outils_scratch/r1110_<prefixe>_*.py`. Rapport final : `Enigme_12/R1110_<PREFIXE>_rapport.md`.

## Règles
Pas de message à personne, pas de post Discord, pas de visite terrain, pas de commit. Web : web_search / web_extract (Firecrawl). Pas de navigateur partagé. Jamais d'invention de contenu ou de citation.

## Réponse finale (≤ 300 mots)
(i) verdict FIABLE / PISTE FAIBLE / RIEN ; (ii) chemin absolu du rapport ; (iii) les 3 faits les plus importants ; (iv) candidats éventuels (nature des 3e/11e, coordonnées) avec le score C1-C20 et le hasard ; (v) prochain test recommandé.
