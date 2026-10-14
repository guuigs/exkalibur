# R0610_E2 — Modèle complet de l'épée d'après la FAQ + hypothèses combinées épée ↔ 3e/11e ↔ clairière

**Statut : PARTIEL (état tôt le 06/10).** Sources : `Communaute/faq_officielle_auteur.json` (1 852 Q/R), `outils_scratch/faq8.txt` (transcription auto), `R0610_D1_epee_calice.md`, `R0610_epee_deux_faces.md`, `R0610_T3_faq.md` (grille C1–C16), `00_PISTES_VIVANTES.md`, `PISTES_ECARTEES.md`.

---

## 1. L'épée dans la FAQ — classement (EST / N'EST PAS / SERT À)

Références = clés JSON `FAQnn-iii` ou `FAQ8`. Verbatim entre guillemets.

### 1a. Ce qu'elle EST (nature, forme, composition)

| Élément | Verbatim / fait | Réf |
|---|---|---|
| Objet matériel + objet illustré | « l'épée réelle est publique et fait partie intégrante du jeu » ; « les deux » (réelle + illustrée) utiles | FAQ8 |
| Fabriquée « sur mesure » | « l'épée Exkalibur a-t-elle été fabriquée avec un cahier des charges en rapport avec les énigmes ? **Oui.** » ; indices directement sur l'épée : « Oui » ; épée physique nécessaire à certaines énigmes : « Oui, tout à fait » | 02-017, 02-014, 02-085 |
| **Pommeau réel** | 8 segments, inscription **N, E, S, O** « dans le sens des aiguilles d'une montre, en débutant par l'inscription du haut » | 05-092 |
| **Pommeau réel = rose des vents** | « la version originale et forgée de l'épée comporte quant à elle **une rose des vents** » | FAQ8 |
| **Pommeau peint** | « ~52 traits » (joueurs) / « 8 segments subdivisés… au moins une cinquantaine » (auteur) ; « important de relever **pourquoi cette épée, sous cette forme, est présente sur l'ensemble des enluminures** » | FAQ8, 02-123 |
| **Pommeau peint, pierre centrale** | spinelle rouge (réel) ; peint = disque rouge + **3 losanges blancs** (2 en haut, 1 en bas, pointe vers la lame) | obs. `r0610_D1_pommeau_zoom.jpg` |
| **La face compte** | « très important de voir que c'est **un côté précis** de l'épée qui a été représenté, ça vous sera très utile » ; FAQ8 « Non, je parle de **la face de l'épée**, en effet » (pas la garde en haut) | 03-032, FAQ8 |
| **Face B = face peinte** | ricasso = **deux dragons ailés affrontés + pommes + entrelacs** ; garde = **calice entre pattes de dragons** ; (face A réelle = croix celtique + épis + triquetra) | `R0610_epee_deux_faces.md` |
| **Calice au centre de la garde** | « ces doigts ne sont pas des doigts, il s'agit des **pattes des dragons qui enserrent le calice** et c'est **un élément crucial en fin de chasse** » | 07-048 |
| **Calice = coupe du charpentier** | « [la coupe tenue au milieu de l'épée géante par les dragons] représentait **la même chose que celle représentée sur l'enluminure neuf**… oui » ; or la coupe de l'enl. 9 = « la coupe du charpentier » : « Je vous confirme que c'est le cas » | FAQ8, 07-005 |
| **Fissure de la lame** | « la fissure vous donne un élément, en effet » ; seule la **forme** compte (placée ailleurs : « Oui » ; tournée de 180° : « Oui, tout à fait ») | FAQ8, 03-059, 06-161 |
| Fourreau | devise « C'est à jamais » (Puy du Fou) | obs. |
| Ricasso réel (face A) | croix celtique + épis + « ARTHURUS PENDRAGON » ; **« pas représenté sur l'enluminure… n'a pas d'importance »** | 03-194 |
| « revenue là où elle n'a jamais cessé d'être » | métaphore ; « elle est encore dans son rocher » (un « s », SON) ; « pas de rocher à trouver… **à ce stade du jeu en tout cas** » | 01-097, 01-137, 06-210 |

### 1b. Ce qu'elle N'EST PAS (négations nettes)

| Négation | Verbatim | Réf |
|---|---|---|
| **Pas un tracé / pas de calque de l'épée** | « l'épée… vous n'avez **pas besoin de faire un calque de l'épée** » | 04-169 |
| **Pas d'épée à tracer en fin de jeu** | « ai-je raison de vouloir tracer une épée en sortant de Consumatum Est ? **Non, vous n'aurez pas besoin de tracer une épée** » | FAQ8 |
| Pas de « plusieurs tracés » | « pour l'instant, vous n'avez pas plusieurs tracés à faire » | 01-245 |
| Dimensions sans importance | « les dimensions de l'épée… importantes ? **Non** » | 03-151 |
| Placement pommeau/quillons/pointe sur des enl. précises sans importance | « le pommeau sur l'enl. 1, les quillons sur 3-4, la pointe sur 12 : important ? **Non** » | 06-289 |
| Pas courbée, poignée/lame alignées | « elle ne peut pas être courbée » ; « elles sont alignées » | 01-169, 01-053 |
| Pas enterrée | « ce n'est pas l'épée qui a été enterrée… elle attendra son vainqueur » | 01-024 |
| Pas indispensable pour Montsalvage | « utiliser l'épée est-elle indispensable pour trouver Montsalvage ? **Non, pas nécessairement** » | 07-219 |
| Dragon ≠ serpent | « un dragon peut-il désigner un serpent ? **Non** » | 03-250 |
| Eaux enchantées ≠ dragons | « les eaux enchantées peuvent-elles rappeler des dragons ? **Pas vraiment** » | 06-147 |
| La fissure ≠ profil d'horizon | testé : corrélation rampe vs horizon, **p = 0,955** (niveau du hasard) | `R0610_D1` §5 M2 |
| « voir trois fois le même astre » inutile | « je ne pense pas que ça va vous être utile de voir trois fois le même astre » | FAQ8 |

### 1c. À QUOI elle sert (fonction)

| Fonction | Verbatim | Réf |
|---|---|---|
| Capitale | « l'épée est **capitale** dans le jeu. Ce sera à vous d'en déterminer le sens exact » | 01-155 |
| **La dernière clé** | « une fois que l'épée est retournée là où elle n'a jamais cessé d'être, son pommeau a-t-il encore un rôle ? **L'épée est la dernière clé.** … pommeau, garde, ricasso, lame… **rôle crucial à jouer à toute fin du jeu** » | FAQ8 |
| **→ trouver la clairière** | « là était la dernière clé : un code, deux clés ? — Il y a **une dernière idée, une dernière intuition cruciale pour trouver la clairière** » | FAQ8 |
| 1er paragraphe = lien spatial | « le 1er paragraphe est-il lié à la suite ? … **d'un point de vue spatial et topographique : Oui** » ; « la 1re phrase est cruciale et agit comme **confirmateur** » | 06-069, 07-088 |
| Calice = le but | la coupe du charpentier (trésor) est représentée **au centre de la garde** | FAQ8 + 07-005 |
| Lien enl. 11 | « dans l'enl. 11, doit-on jouer aux cartes pour résoudre le crypto ? … **N'oubliez pas l'épée dans tout cela** » ; « le jeu de cartes de l'enl. 11 : vous en aurez besoin, mais **pour autre chose** » | 05-101, FAQ8 |
| Boussole ? | « l'épée est-elle une boussole pour le jeu ? — l'épée est capitale… sens exact à déterminer » (ni oui ni non) | 01-155 |
| Épée réelle utile en É12 | « l'épée réelle avec le triquetra et le dragon était-elle utile dans Ad vitam æternam ? **Oui, l'épée est très utile** » | FAQ8 |

**Synthèse 1 :** l'épée est une **clé de lecture**, pas un tracé ni un calque. Elle fournit (a) une **boussole/rose des vents** (pommeau), (b) le **but** (calice = coupe du charpentier), (c) une **face** à identifier (revers B), (d) un **ordre structurel** pommeau → garde → lame → pointe. Elle ne fournit **pas** de série ≥ 13 ni de coordonnée.

---

## 2. Superposition / calque / astres / ciel de l'enl. 9 / symboles

### 2a. Le passage-charnière de FAQ8 (verbatim, adjacents)

> « Euh, les différents **astres présents dans les Enluminures** peuvent-ils nous aider à comprendre **les symboles dans le ciel de l'Enluminure neuf** ? — Hmm, **oui, tout à fait**. »
> « utiliser un **logiciel de superposition d'images** est-il nécessaire dans la chasse ? — **Excellente question.** Et sans aller jusqu'au logiciel, vous pourriez en effet utiliser **un calque**. »

Lecture : l'auteur enchaîne **astres → symboles du ciel enl. 9** (oui) puis **superposition → calque** (excellente question). Le « calque » (objet physique, papier) sert à superposer **deux images**, probablement pour mettre en relation **les astres des enluminures** et **le ciel de l'enl. 9**.

### 2b. Corpus complet astres / ciel / symboles (enl. 9)

| Thème | Verbatim | Réf |
|---|---|---|
| Astres demandés par l'auteur | « j'ai en effet demandé à **représenter certains astres** sur les enluminures » | 07-185 |
| Astres enl. 1 et 3 | « le point clé dans ces astres est davantage **la couleur** que les cratères » | 06-063 |
| Ciel important | « les ciels ont-ils une importance ? **Oui, le ciel est important** » ; « le ciel a toute sa place… **se tourner vers le ciel** » | 03-214, 03-033 |
| Ciel sur la carte | « puis-je apercevoir une partie du ciel sur la carte ? **Oui** » | 06-151 |
| Ciel étoilé Omnia | « gardez bien **le ciel en tête**, il n'est pas là pour rien » | 06-066 |
| **6 symboles du ciel enl. 9** | loup, étoile, arc-en-ciel, âne, ancre, **croissant de lune** (6e, à droite de l'arbre) | 05-097, 05-183, 06-258 |
| Pas un rébus phonétique | « il ne s'agira pas d'un rébus phonétique » (lecture étymologique/héraldique/historique à creuser) | 06-059 |
| Pas une histoire, mais un élément | « ils ne vous racontent pas une histoire mais vous permettent d'**identifier un élément crucial** » | 07-134 |
| Déclic fin de jeu | « ça peut vous aider à avoir **un déclic en fin de jeu** » ; « interpréter correctement les 6 dessins **une fois la zone finale trouvée** » | 07-198, 06-067 |
| Paires décodées ensemble | « les signes qui vont par deux… **décodés ensemble**… identifier à chaque fois **une seule chose** » (ancre+diamant ; âne+émeraude) | 07-143 |
| Code universel | « c'est un **code universel**, mêmes dessins dans toutes les langues » | 06-138 |
| Distinct du reste de l'enl. 9 | « la charade du ciel… rapport avec les autres éléments de l'enl. 9 ? **Non, pas vraiment** » | 06-222 |
| Lien pers. rouge / ciel ? | « lien entre les personnages en rouge de l'enl. 9 et les symboles du ciel ? **Non** » | FAQ8 |

### 2c. Superposition / calque : ce qui est autorisé vs refusé

| Autorisé | Verbatim | Réf |
|---|---|---|
| **Un calque (papier)** | « sans aller jusqu'au logiciel, vous pourriez utiliser **un calque** » | FAQ8 |
| Papier calque « très utile » ? | « j'ai vu que beaucoup de joueurs l'avaient tenté, **je ne répondrai pas** » | 03-106 |
| Calquer un rapporteur pour un angle | « impressions de My Maps sur lesquelles **vous calquez un rapporteur**… vous aurez besoin de **calculer un angle** » | 07-141, FAQ8 |

| Refusé / non-réponse | Verbatim | Réf |
|---|---|---|
| **Calque de l'épée** | « pas besoin de faire **un calque de l'épée** » | 04-169 |
| Tracer une épée après É11 | « non, vous n'aurez pas besoin de tracer une épée » | FAQ8 |
| Superposer un élément d'enluminure sur un autre | « je ne peux pas répondre » | 02-333 |
| Superposer des constellations sur la carte | « bonne question, je ne peux pas y répondre » | FAQ8 |
| Superposer = méthodologie | « loin d'une **simple superposition de repères**… identifier un fil rouge, la structure » | 02-211 |

**Synthèse 2 :** le **calque** est autorisé (et même suggéré) mais **jamais de l'épée**. L'objet du calque est le plus probablement **le ciel de l'enl. 9** (6 symboles = « astres »), à relier aux **astres** semés dans les autres enluminures (FAQ8 « oui, tout à fait »), pour « identifier un élément crucial » → « déclic en fin de jeu ». Le lien **épée ↔ calque** est : le **pommeau réel porte une rose des vents** (instrument d'orientation) et l'enl. 11 demande « **orientez-vous** pour compléter ».

---

## 3. Par partie de l'épée : série ≥ 13 ? objet « même nature » ? instrument ?

Rappel des contraintes 3e/11e (grille C1–C16, `R0610_T3_faq` §4) : **même nature** (C1), **un seul de chaque** (C2), **série ordonnée ≥ 13** (C9 : « le 13e existe et mène ailleurs » ; C10 : « 8e/16e incorrects »), **bois vs pierre** (C7 écharde), **marchable** (C8).

| Partie de l'épée | Contenu (observé + FAQ) | Série ≥ 13 ? | Objet « même nature » que 3e/11e ? | Instrument ? |
|---|---|---|---|---|
| **Pommeau** (8 faces N/E/S/O + 3 losanges + ~52 traits) | 8 faces cardinales (05-092) ; rose des vents (FAQ8) ; ~52 traits peints (02-123, FAQ8) ; **3 losanges blancs** | 8 < 13 ; 52 = cartes mais « pas un ensemble de 52 » (07-156) → **non** | non (ni pierre ni bois, non marchable) | **boussole / rose des vents** (FAQ8) ; rapporteur/angle (FAQ8) |
| **Garde / calice** | quillons à têtes de dragon ; **calice entre pattes de dragons** (07-048) = coupe du charpentier (FAQ8, 07-005) | non | le **calice = coupe = le but** (pas un 3e/11e) | non (symbole du but) |
| **Ricasso face B** | **2 dragons ailés + pommes + entrelacs** | non (2 dragons, pas ≥13) | non | non (thème : Hespérides/Avalon) |
| **Lame / fissure** | fissure = « un élément » (FAQ8), seule la **forme** compte (03-059, 06-161) | non (test horizon p=0,955) | non | « **règle/échelle** » possible (la fissure comme profil/échelle), **non confirmé** |
| **Pointe** | pointe sur enl. 12 (tour rouge = Lincoln = Hugues d'Avalon) | non | non | non |

**Synthèse 3 :** **aucune partie de l'épée n'est une série ordonnée ≥ 13.** L'épée n'est donc **pas la source des 3e/11e** : c'est une **clé** (boussole + but + ordre + face) qui sert à **décoder/positionner** la série (les 3e/11e), cohérent avec « la dernière clé » / « dernière intuition pour trouver la clairière » (FAQ8). La série ≥ 13 doit venir d'ailleurs (enl. 11, écrits du narrateur, terrain). Les deux seuls éléments « numériques » de l'épée (8 faces, 52 traits) sont **trop petits** ou **explicitement exclus** (07-156).

---

## 4. Hypothèses combinées épée ↔ 3e/11e ↔ clairière

Notation : ✓ satisfait, ✗ échoue, ~ partiel/incertain, — sans objet. Contre FAQ04-169/FAQ8 noté en dernière colonne.

### H1 — Le pommeau = boussole des huit derniers pas (« jour dernier » sans lever la tête)
Le pommeau réel porte une **rose des vents N/E/S/O** (FAQ8 + 05-092). « ma boussole suivait le jour dernier » (texte) ; « faut-il lever la tête pour trouver le jour dernier ? **Non** » (FAQ8) ; « huit derniers pas suivant votre boussole » (04-139) ; « j'avais une boussole avec moi » (06-282).
- **Ce qu'elle dit :** la boussole du texte = le pommeau (rose des vents) ; elle oriente les **8 derniers pas** selon le « jour dernier » (30/04/1524, azimut 63,7–73,9°), et les **10 pas N + 10 pas E** selon les **cardinaux**.
- **Score C1–C16 :** ne fournit pas la nature des 3e/11e → C1–C14 ~/— ; C15 ✓ (positionne par rapport au départ/rempart) ; C16 —.
- **Contre 04-169/FAQ8 :** **compatible** (pas de calque, pas de tracé ; « boussole » n'est pas un tracé). Aucune contradiction.
- **Confiance :** lecture 40 % ; instrument concret, mais **ne résout pas les 3e/11e** (c'est le mécanisme des derniers pas, après la clairière).

### H2 — La face B inverse E/O pour les derniers déplacements
La face peinte est le **revers** (dragons + pommes + calice, `R0610_epee_deux_faces.md`). Vu du revers, la rose des vents du pommeau est **retournée** (E à gauche, O à droite). Si on lit la boussole sur la face B (la face « utile », 03-032/FAQ8), « dix pas à l'est » devient « dix pas à l'**ouest** » et le « jour dernier » devient son **miroir** (180° − azimut).
- **Ce qu'elle dit :** un renversement miroir des déplacements finaux (ou des 3e/11e par rapport au départ).
- **Score C1–C16 :** — (mécanisme de marche final, pas une série).
- **Contre 04-169/FAQ8 :** compatible, mais **spéculatif** (aucun texte ne demande d'inverser E/O) ; « la face compte » (03-032) est un appui faible.
- **Confiance :** 15 %.

### H3 — Les 3 losanges (♦) du pommeau ↔ la pierre « carreau + ? » de l'enl. 11 (« orientez-vous pour compléter »)
Le pommeau peint porte **3 losanges** ; l'enl. 11 a une roche au symbole **« losange, carreau »** (FAQ8 « il s'agit du symbole d'un losange, carreau ») avec un **point d'interrogation** à compléter (05-091 : « notez bien le **point d'interrogation** sur l'enl. 11. Et "**orientez-vous**" pour compléter »). « N'oubliez pas l'épée » (05-101) + « le jeu de cartes de l'enl. 11 : vous en aurez besoin **pour autre chose** » (FAQ8).
- **Ce qu'elle dit :** le pommeau (rose des vents + 3 losanges = « carreau » + le « 3 ») est la **clé de la crypto de l'enl. 11**, dont la relecture en É12 (« autre chose ») sert à **placer les 3e/11e** (C14 : l'enl. 11 « place une partie »).
- **Score C1–C16 :** C14 ✓ (lien direct avec l'enl. 11) ; C7 ✗ (les cartes/pierres ne donnent pas d'écharde) ; C11 ✓-cohérent (pas 52 : les 3 losanges ≠ 52 cartes) ; le reste ~/—.
- **Contre 04-169/FAQ8 :** compatible (aucun calque de l'épée ; on ne trace pas l'épée).
- **Confiance :** 25 % comme **pont épée → enl. 11 → 3e/11e**, mais **pas de placement géométrique** dérivé. C'est une piste d'**É11** (angle sans dérivation), pas une coordonnée d'É12.

### H4 — L'épée = carte d'ordre du dernier tronçon (pommeau = astre, garde = jonction + calice = coupe, lame = eaux, pointe = roche)
La structure de l'épée **reproduit l'ordre du texte** : pommeau (astre glorieux / boussole) → **garde** (croisée = « jonction des chemins » ; **calice au centre = la coupe du charpentier**, le but) → **lame + fissure** (les eaux enchantées, « le trait glorieux ») → **pointe** (grande roche). Le 1er paragraphe est « lié spatialement et topographiquement » (06-069) ; le calice = coupe = « ce que vous cherchez » (07-196).
- **Ce qu'elle dit :** l'épée est une **mnémonique/ordre de lecture**, pas un tracé. Le calice au centre de la garde dit que **le but (coupe) est à la jonction des chemins** (la clairière) — cohérent avec « trouver la coupe du charpentier » à la clairière.
- **Score C1–C16 :** C15 ✓ (ordre relatif au départ) ; C16 ✓ ; le reste — (aucune série/coordonnée).
- **Contre 04-169/FAQ8 :** **compatible** (on ne calque pas, on lit l'ordre ; le calice = coupe est confirmé par FAQ8 + 07-005). Aucune contradiction.
- **Confiance :** lecture 35 % (déjà notée 25 % dans `R0610_D1` §4 ; **renforcée** par la confirmation FAQ8 « calice = coupe de l'enl. 9 »).

### H5 — Superposition par calque : astres des enluminures → ciel de l'enl. 9 → position des 3e/11e
FAQ8 enchaîne « astres des enluminures aident à comprendre les symboles du ciel de l'enl. 9 : **oui** » puis « superposition d'images → **un calque** ». Le calque sert donc à **superposer** les 6 symboles-astres du ciel de l'enl. 9 sur **autre chose** (la carte ? l'enl. 11 ?), pour « identifier un élément crucial » (07-134) et avoir « un déclic en fin de jeu » (07-198).
- **Ce qu'elle dit :** une **superposition d'images** (pas de l'épée) positionne les 3e/11e. L'épée n'intervient que par son **pommeau-rose des vents** (« orientez-vous »).
- **Score C1–C16 :** C14 ~ (enl. 11 = support possible) ; le reste —. Aucune contrainte C1–C8 satisfaite par elle-même.
- **Contre 04-169/FAQ8 :** **compatible** (04-169 n'interdit que le calque *de l'épée* ; FAQ8 *encourage* un calque). Mais l'objet superposé et la cible sont **inconnus**.
- **Confiance :** 15 % (direction valable, contenu vide).

**Classement :** H4 > H1 > H3 > H5 > H2. H4 + H1 se combinent naturellement (l'ordre structurel + l'instrument boussole). H3 est le seul à relier directement l'épée à l'enl. 11 (donc à C14), mais sans géométrie.

---

## 5. Meilleure hypothèse — règle de test et exécution

**Meilleure : H4 (combinée H1)** — *« L'épée est une clé de lecture d'ordre : pommeau = boussole/astre (N/E/S/O + rose des vents) → garde = jonction, calice central = coupe du charpentier (le but) → lame/fissure = eaux enchantées → pointe = grande roche ; le pommeau-boussole oriente les déplacements finaux. »*

### Règle de test (écrite avant calcul)

1. **Entrées :** les azimuts du « jour dernier » (30/04/1524 : 63,7° / 68,6° / 73,9°, acquis) ; les pas du texte (10 N, 10 E, 8 derniers) ; le pommeau à 8 faces (pas de 45°).
2. **Calcul :**
   - (a) l'ordre épée pommeau→garde→lame→pointe doit correspondre à l'ordre texte astre→jonction→eaux→roche (test de correspondance, qualitatif) ;
   - (b) le **vecteur d'approche finale** = 10 pas N + 10 pas E + 8 pas à l'azimut θ du jour dernier (et son miroir « face B ») ;
   - (c) l'azimut du jour dernier doit pouvoir être **lu sur le pommeau** (8 faces = grille 45°).
3. **Critère de succès :** (a) ordre cohérent ; (b) vecteur final ~15–32 m de la souche, cap ≈ 53,5° (ou 67,9° miroir) — compatible « pile-poil » et « tout près de la jonction » ; (c) l'azimut jour-dernier **coïncide avec une face** du pommeau.
4. **Test du hasard :** pour (c), comparer l'écart azimut↔face la plus proche à un tirage aléatoire d'azimuts (1 000) — le pommeau « encode » l'azimut seulement si l'écart réel est ≤ tolérance typique (≤ ~5°).

### Exécution (calculs faits, `outils_scratch` / session Python)

**(a) Ordre — cohérent.** pommeau (astre/boussole) → garde-croisée (jonction) → lame-fissure (eaux/« trait glorieux ») → pointe (roche) = ordre exact du texte (astre → jonction → eaux → roche). ✓ (qualitatif, non falsifié).

**(b) Vecteur d'approche finale (de la souche au coffre).**

| Pas | azimut θ | offset Est | offset Nord | distance | cap |
|---|---|---|---|---|---|
| 0,70 m (pas français) | 68,6° (jour dernier) | 12,2 m | 9,0 m | **15,2 m** | 53,5° |
| 0,70 m | 111,4° (miroir face B) | 12,2 m | 5,0 m | 13,2 m | 67,9° |
| 1,48 m (passus romain) | 68,6° | 25,8 m | 19,1 m | **32,1 m** | 53,5° |
| 1,48 m | 111,4° | 25,8 m | 10,5 m | 27,9 m | 67,9° |

Le coffre est à **15–32 m** de la souche (selon l'unité de pas, que l'auteur laisse « libre », 04-163), cap ~53,5° (jour dernier) ou ~67,9° (miroir face B). Cohérent avec « tout près » (05-051) et la précision « pile-poil ».

**(c) Le pommeau N'ENCODE PAS l'azimut du jour dernier.** Écarts azimut ↔ face la plus proche (grille 45°) : 63,7°→45° (**18,7°**), 68,6°→90° (**21,4°**), 73,9°→90° (**16,1°**). Les trois écarts (16–21°) dépassent largement toute tolérance de lecture (~5°) ; un azimut au hasard est en moyenne à 11,25° d'une face (uniforme 0–22,5°). **Le pommeau à 8 faces ne peut pas être la source du « jour dernier » (63,7–73,9°), même à 16 points (pas de 22,5° : écarts ≥ 7,4°).**

**Conclusion du test :** H4 tient comme **ordre de lecture** (a ✓, b ✓ cohérent), mais **H1 est réfutée dans sa version « pommeau = source de l'azimut »** : le pommeau (8 faces, rose des vents à 8/16 points) donne les **cardinaux** (les 10 pas N + 10 pas E), tandis que le « jour dernier » (63,7–73,9°) provient de **l'astre glorieux** — ce que confirme FAQ8 : « l'astre glorieux vous guide **en tout dernier lieu** » et « faut-il lever la tête pour trouver le jour dernier ? **Non** » (= on le **calcule**, on ne le lit pas sur le pommeau ni dans le ciel). Le pommeau-boussole est donc le **référentiel N/E/S/O**, pas la valeur de l'azimut.

---

## 6. Verdict et suite

- **Verdict global : PISTE FAIBLE (lecture), RIEN de géométriquement fiable issu de l'épée seule.** L'épée est confirmée « dernière clé » (FAQ8) = **clé de lecture** (ordre + boussole + but + face), **pas un tracé ni une série ≥ 13**. Elle ne peut pas, à elle seule, fournir les 3e/11e : la série ≥ 13 est ailleurs (enl. 11, écrits du narrateur).
- **Acquis nouveaux ce jour (vs `R0610_D1`) :**
  1. **Le calice de la garde = la coupe de l'enl. 9 = la coupe du charpentier** (FAQ8 + 07-005) → le **but est dessiné au centre de la garde** = « à la jonction des chemins » (la clairière). Renforce H4.
  2. **Le pommeau réel porte une rose des vents** (FAQ8) → la « boussole » du texte est matériellement sur l'épée (H1), mais **elle donne les cardinaux, pas l'azimut jour-dernier** (réfuté ci-dessus, écarts 16–21°).
  3. **FAQ8 enchaîne « astres → ciel enl. 9 : oui » puis « superposition → un calque »** → le calque autorisé porte sur les **astres/ciel**, jamais sur l'épée (04-169).
- **À tester ensuite (ordre) :** (1) lire l'azimut « jour dernier » comme un **angle à calculer au rapporteur** (FAQ8 « vous aurez besoin de calculer un angle »), pas une face du pommeau ; (2) exploiter **H3** : reprendre la crypto de l'enl. 11 (« n'oubliez pas l'épée », 3 losanges ↔ carreau « ? », « orientez-vous ») pour « l'autre chose » de l'É12 ; (3) identifier l'**objet exact du calque** (ciel enl. 9 → carte ?) ; (4) chercher la série ≥ 13 dans les **écrits du narrateur** (N2) ou le **terrain** (ponceaux le long des chemins).

---

## 7. Faits vérifiables (chemins)

- Corpus épée : 182 entrées FAQ touchées ; Q/R clés : 01-155, 02-014/017/085/123, 03-032/151/194/260, 04-169/180, 05-092/101, 06-161/289, 07-005/048/212/219, FAQ8 (dernière clé, rose des vents, calice=coupe, face, fissure, calque, astres→ciel enl. 9).
- Corpus ciel/astres/calque : 03-033/106/214, 05-095/097/183, 06-059/063/066/067/138/151/222/258, 07-134/143/185/198, 02-333, FAQ8.
- Grille C1–C16 : `R0610_T3_faq.md` §4.
- Revers de l'épée : `R0610_epee_deux_faces.md`. Tests géométriques déjà faits : `R0610_D1_epee_calice.md` §5 (toponymes, horizon p=0,955, tracés ≥ 270 km).
