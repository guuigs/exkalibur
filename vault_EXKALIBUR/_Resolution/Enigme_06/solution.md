# Énigme 6 — Libera nos a malo : SOLUTION (mode shark, 30/09/2026)

**Statut : ✅ VALIDÉE (mode shark)**, sur trois appuis indépendants :
1. **[OFFICIEL]** annonce de l'auteur du 04/06/2026 : « l'entièreté des énigmes 1 à 11 » est résolue par la communauté.
2. **[COMMUNAUTÉ, consensus]** Discord officiel : « Les solutions les plus "communes" : 4C : Cîteaux, Cluny, Clairvaux, Clermont ; 5e C : Chartres ; le 6e : top secret » (Merlin, 19/06/2026). Mécanisme (PtitNours, 30/04/2026) : « pour les bleus ACDEINUTX anagramme de **ND CITEAUX**, pour les rouges ARUCALIVX anagramme de **CLAIRVAUX** ». Clermont et Cluny s'obtiennent autrement : « jeu du moulin de l'enluminure 7, en t'aidant d'un indice trouvé enluminure 3 et du bâtiment en haut à gauche » (Mircé, 26/07/2026 ; les 3 clochers = Cluny).
3. **[NOS CALCULS]** `calculs/O_verif_solution_communaute.py` :
   - les deux anagrammes sont **exactes** ;
   - chaîne **Clairvaux → Cîteaux → Cluny → Clermont** (ordre nord → sud) = **340,94 km** (115,46 + 83,99 + 141,49) ;
   - D = Tour de Londres → Battle → Sainte-Chapelle = **341,60 km**, soit un écart de **−0,19 %** (tolérance officielle de 1 %) ;
   - point d'arrivée à L depuis la Tour via Battle : **0,68 km de la Sainte-Chapelle** (1,07 km de Notre-Dame).

## Solution
- **Les 4 C** : **Clairvaux, Cîteaux (Notre-Dame de Cîteaux), Cluny, Clermont**, reliés dans cet ordre (nord → sud, « relie-les une à une »).
  - Thème : 1re croisade et Templiers. Urbain II, ancien moine de Cluny, prêche à Clermont en 1095. Bernard de Clairvaux, cistercien issu de Cîteaux, fait reconnaître les « pauvres chevaliers » (Templiers). La Vierge = ND de Cîteaux ; le pape = Urbain II ; les 3 clochers = Cluny.
- **Tour-krak** = Tour de Londres ; **champ de bataille** = Battle (Hastings 1066, « HAROLD REX INTERFECTUS EST », MLXVI).
- **Distance** = longueur des 4 C ≈ **341 km** ; elle resservira (Noli me tangere : « la même distance que les 4 C »).
- **Lieu très Sainte** = **Sainte-Chapelle** (Paris) ; le « e » de Sainte et la majuscule reprennent le nom officiel. C'est le même lieu que le « lieu très saint » de Sub rosa (É7).

## Ce qui n'est PAS reproduit par nous (limite honnête)
- Le **détail du mécanisme de lecture** du plateau, c'est-à-dire l'ordre exact qui associe les 24 cases aux lettres (clé « Commencera le Père, et finiront les cieux » = Pater noster en latin + « Amen » en hébreu, d'après le Discord). Mes tests de parcours avec un alphabet à 24 lettres ne redonnent pas ACDEINUTX/ARUCALIVX : il y a probablement une étape de plus (lettres du Pater, cases vides, pions hors plateau). Sans impact sur la solution, confirmée par ailleurs.
- La forme des 4 cloches (U à angles droits) ne colle pas avec les angles réels de la chaîne (virages d'environ 35°). Sur le Discord, un joueur conseille de faire « un petit quart de tour » : c'est un confirmateur approximatif, pas une contrainte.

## Pour la suite (transverse)
- 5e C probable = **Chartres** [RUMEUR consensuelle] ; 6e C : secret. Les 6 C reliés forment une figure (FAQ 8).
- Sainte-Chapelle = point de départ de Sub rosa (É7).
