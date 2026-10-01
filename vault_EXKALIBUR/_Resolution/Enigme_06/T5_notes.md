# T5 — Veille rumeurs & FAQ transverse des C (É6 « Libera nos a malo »)

## REPRISE (à jour : TERMINÉ — FAQ complète ; web épuisé, 0 rumeur trouvée)
1. **Requêtes faites** (≈17/30) :
   - FAQ : extraction complète (`Communaute/extract_C.py` → `_C_raw.json` ; tri → `Communaute/faq_C_transverse.md`, 46 entrées + contexte).
   - Moteurs texte morts : DDG HTML (page vide), Bing HTML (pas de résultats parsables), Brave (429), Firecrawl `web_search`/`web_extract` (403), r.jina.ai (401 « bad network reputation »), `browser_exec` (daemon ne démarre pas), reddit.com (page « Blocked »), zarquos (réponse vide).
   - **YouTube via curl + `scratch/yt.py` FONCTIONNE** : 9 requêtes (« Exkalibur énigme 6 Libera nos a malo », « …solution énigme », « …4 C avant-dernier C théorie », « …Cluny Cîteaux Clairvaux », « …joueurs avancement », « …tiktok théorie », « …treasure hunt solution riddle », « Exkalibur Sainte-Chapelle », « Exkalibur Ultima Forsan »). Résultat : **uniquement** vidéos officielles (FAQ#1–7 UNSOLVED HUNTS ; « Un indice décisif » Puy du Fou 31/10/2025 ; making-of de l'épée), presse/TV (TV Vendée Actu ×2, Ameland lancement 22/05/2025), présentations de jeu (Ludovox « Ludochrono », CKanKonJoue TQTYmPGGqc0 — description = simple présentation, aucune solution). **Aucune vidéo de solution/théorie, aucune chaîne de chasseur traitant É6 ou les C.**
2. **Conclusion web** : [RUMEUR] = néant public. Cohérent avec la veille du 29/09 (`veille_2026-09-29.md` l.197 : aucun fil de théories hors Discord, qui est fermé).
3. **Restant possible (non fait, faible espoir)** : commentaires publics YouTube des vidéos FAQ#3/#4/#6/#7 (nécessite l'API de commentaires, non accessible sans clé/JS) ; relire les FAQ vidéo YouTube (transcripts) si l'auteur y dit plus que la base texte ; accès Discord (interdit).
4. **Sources mortes** : voir point 1 ; Facebook/Discord fermés (aucun compte créé).

## [OFFICIEL] Synthèse FAQ des C (réf. = `faq_officielle_auteur.json`)
### Nombre et nature
- Libera nos a malo : **4 C à identifier dans l'énigme** (03-092, 03-259). « Ça ne veut pas dire qu'il n'y en a que quatre dans le jeu » (03-259).
- **Total des C** : 4 (Libera) + **avant-dernier C** (trouvé dans/à partir de Noli me tangere : « vous avez trouvé tous les C jusqu'à l'avant-dernier. Donc il en reste deux », 03-061) + **dernier C** = « sixième et dernier C » (question 06-252 reprise par l'auteur sans correction ; 07-193 « mes 5 C » : ne les relie pas à la gardienne de lumière). → **6 C au total** (4 + avant-dernier = 5e + dernier = 6e). Le chiffre « 6 » vient d'une formulation de joueur que l'auteur n'a pas corrigée ; 05-035 « l'avant-dernier C est-il le 5e ? » → NRP. **Niveau : probable, pas explicitement confirmé.**
- **Nature des 4 C** : « Est-ce que les quatre C sont de même nature ? » → **« Je ne répondrais pas »** (03-084) = non éliminant. Le jeu du moulin : nature ni confirmée ni infirmée (03-085, 03-326) ; il ne dit pas comment on les trouve.
- **Chaque C est-il un lieu ?** Les C sont posés « sur Google Maps » (03-279), on les relie (03-101) → ce sont des **points géographiques** (fait implicite fort). « Vous pouvez sûrement **boire** à chaque fois [qu'on passe sur un C], mais pas croquer de pomme » (07-280) : réponse joueuse/ludique, à lire comme allusion à l'eau (source, fontaine, rivière ? cf. « eaux enchantées » d'Ad Vitam) — [PISTE, non éliminant]. Le dernier et l'avant-dernier C font exception (pas de « boire » vs pomme : la question les exclut).
- Nature du « dernier C » : « Le dernier C est-il toujours un C aujourd'hui ? » → **Oui** (07-058) ; ce n'est pas Montsalvage (07-271) ; les C n'aident pas à trouver Montsalvage (07-230) ; la tour d'Ultima Cena n'est pas un C (06-072) ; le « lieu très sainte » n'est **pas** un des 4 C (03-099).
- La cloche de l'enluminure 12 **n'est pas un 5e C** (06-169, 06-240 : « la cloche n'est pas indicative d'un C mais va vous aider en ce qu'elle est accolée au bâtiment ») ; elle aide à trouver la tour (04-170), l'animal rouge est un mâle (06-273). NB : 04-181 (« oui » à « la cloche a-t-elle une importance, un 5e C ? ») est un « Oui » à l'importance, contredit/précisé ensuite → ne pas en tirer un C.
- Enluminure 11 : lettres **D et C** sur les rochers du fond (03-137, 03-294, 03-335) ; à ne pas confondre avec les C-lieux (lettre C, autre usage).

### Ordre / usage / distance
- « Il y a **un ordre évident** pour les relier » (03-101) ; placer les C **dans l'ordre, sans aller-retour** (03-279). Genre masculin de « les C » : pas une erreur (03-100).
- **07-038 (usage final « visuel »)** : « je vous les donne dans un certain ordre… parfois on suit l'ordre dans lequel on les trouve pour obtenir le résultat d'un décryptage… à la fin, **peut-être visuellement en tout cas, ça va vous donner une indication supplémentaire** » → la **figure formée par tous les C** compte (forme, direction, alignement).
- **Distance** : « parcours la même distance **que** les quatre C » (03-047, 03-062) = longueur de la chaîne des 4 C. **07-160** : s'intéresser à la distance des 4 C hors Libera/Noli est justifié, « elle vous sera utile à plusieurs reprises ».
- **Non-croisement (07-166)** : relier tous les C (4 C, avant-dernier, dernier) → **ne croise pas la lame** de l'épée d'É1 (« Il ne me semble pas »). Contrainte de forme sur toute la chaîne. Tolérance 1 % (02-277).
- Liens Noli : le narrateur se rend à l'avant-dernier C mais « réellement, non » (06-056) ; l'avant-dernier C ne donne pas le château de la gardienne de lumière (07-200) ; le dernier C ne s'a pas encore quand on cherche le nom de Dieu (07-181), aide pour Consummatum Est (07-178), est un point de passage qu'on **traverse** (06-252) et confirme le bon chemin (06-071). L'ultime traversée peut dépasser très finement le lieu du dernier chevalier (07-256).
- Les C ne servent pas à trouver Montsalvage (07-230).

### Éliminations / non-éliminations (ce que l'auteur a REFUSÉ de dire)
| Question | Réponse | Effet |
|---|---|---|
| Les 4 C de même nature ? | Je ne répondrais pas (03-084) | aucun |
| Les 4 C dans le même pays ? (→ autres C aussi ?) | **NRP** (05-100) | aucun ; pas de contrainte pays |
| Lieu très sainte = un des 4 C ? | **Non** (03-099) | élimine Sainte-Chapelle (ou tout lieu final) comme C |
| Tour d'Ultima Cena = C ? | Non (06-072) | élimine |
| Dernier C = Montsalvage ? | Non (07-271) | élimine |
| Dernier C aide à trouver Montsalvage / les C ? | Non (07-230) | découplage |
| Chaîne de tous les C croise la lame ? | Il ne me semble pas (07-166) | **contrainte géométrique** |
| Lien Libera ↔ vagues de la carte ? | Non (03-107) | élimine |
| Libera donne des indices pour identifier le narrateur ? | Pas vraiment (04-089) | – |
| Le dernier C est représenté en enluminure 12 ? | ne peut répondre (07-252) | aucun |

### Anagrammes (Libera) — 04-189, 03-058, 04-185
Anagrammes exactes ; identifient « le lieu sans problème. Pas forcément que le lieu d'ailleurs ». Non exploité dans les C par l'auteur (pas de lien dit).

## [RUMEUR]
- **Aucune rumeur publique retrouvée** (YouTube/presse/TV : seulement contenus officiels ou de présentation ; autres moteurs inaccessibles, cf. REPRISE). Les hypothèses de chaînes (Clermont–Cluny–Cîteaux–Clairvaux 340,99 km ; Clermont–Cadouin–Cahors–Conques 341,87 km) viennent du calcul des solveurs précédents, **pas** d'une source publique.
- [RUMEUR-interne, joueur dans la FAQ] Q 06-252 « sixième et dernier C » → hypothèse de 6 C ; Q 07-280 « boire à chaque fois » → l'auteur suggère une relation avec la boisson/eau à chaque C (allusion, pas une définition).

## Pistes à tester (issues de la FAQ, à confier aux autres agents)
1. **Figure « visuelle » finale** des 6 C (07-038) : alignement, polygone, direction → tester chaque chaîne candidate de 4 C prolongée par avant-dernier et dernier C.
2. **Non-croisement de la lame** (07-166) : filtre géométrique pour candidats 4 C (nécessite les coordonnées du tracé É1 : épée León–Foix–Valence–Urquhart).
3. « Boire à chaque C » (07-280) : chercher si des lieux à eau/fontaine/source/abbaye à puits conviennent (sans conclure).
4. Distance D (chaîne 4 C) réutilisée « à plusieurs reprises » (07-160) → chercher où d'autres énigmes (Noli, Consummatum Est : « même distance… ») la réemploient ; c'est un test de cohérence pour la valeur D.
