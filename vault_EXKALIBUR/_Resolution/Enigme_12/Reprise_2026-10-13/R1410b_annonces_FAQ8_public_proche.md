# É12 : suite du 14/10 au soir — annonces officielles, FAQ8 relue pour le modèle des 3e/11e, entonnoir public à courte portée

## 1. Discord (lecture seule, 14/10)

### Annonces officielles de l'auteur (`#les-annonces`) — [OFFICIEL]
| Date | Contenu utile |
|---|---|
| 04/06/2026 | 95 % des éléments trouvés ; « plusieurs dizaines » ont le chemin de rempart ; **3 équipes à 90-95 %, « toutes à moins de 150 m du coffre dans l'une ou plusieurs de leurs résolutions »** ; une proposition de solution par mail et par semaine au plus. |
| **02/07/2026** | Un joueur arrêté en train de creuser sur un terrain privé. **« Menez vos recherches en excluant strictement les propriétés privées, monuments historiques, bâtis en tout genre. Le coffre ne s'y trouvera pas. »** Outils conseillés : France Cadastre, carte Koumoul des parcelles des personnes morales (MAJIC), Géoportail + calques des forêts publiques. |
| 22/07/2026 | Pause des FAQ ; « soyez très précis, notamment sur l'énigme 12 ». |
| 01/10/2026 | FAQ de rentrée reportée ; « nombre de chasseurs très proches » ; « soyez précis sur vos derniers déplacements ». |

→ L'annonce du 02/07 fait du contrôle « public / pas de bâti / pas de monument » une **règle officielle**, avec la même méthode que la nôtre (cadastre + personnes morales). Le contrôle du pré A (`R1410_controle_eliminatoire_preA.md`) est donc exactement ce que l'auteur demande.

### Salon `#ad-vitam-aeternam`, 04-13/10 — [COMMUNAUTÉ]
- Personne n'annonce les 3e/11e (« Quelqu'un a progressé sur les troisième et onzième ? » reste sans réponse le 04/10).
- Un « progressivomètre » (questionnaire de l'auteur sur l'avancement) circule ; des joueurs disent y avoir mis leurs solutions et attendre « la quinzaine ». Ce n'est pas un validateur.
- Discussion du 13/10 : pour les 10 pas, « le nord donné par l'épée » (axe de l'épée sur la carte ≈ 352-353°, pommeau = nord). Hypothèse de joueurs, rien de plus.

## 2. FAQ8 : les esquives qui touchent le modèle « 3e/11e »
Relues dans la transcription (`Communaute/FAQ8_2026-06-04_transcription_auto.pdf`). Une esquive n'est pas un oui, mais elle marque une question que l'auteur refuse de démentir.
- « À peine débarqué sur un chemin de rempart, je trouve **directement dix stades romains entre deux points très particuliers**. Est-ce normal ou suis-je sur une fausse piste ? » → « Là-dessus, je ne pourrai pas vous répondre. »
- « Les remparts, dans leur intégralité, forment-ils un **ensemble beaucoup plus vaste** ? » → pas de réponse. « Peut-on faire **le tour complet** des remparts ? » → pas de réponse. « Les remparts appartiennent-ils à **un château précis** ? » → pas de réponse.
- « Les **titres des énigmes** sont-ils une clé pour un élément crucial ? » → « Oui, ils n'ont pas été choisis au hasard. » (titre 3 = *Ecce Homo*, titre 11 = *Consummatum est* : déjà noté au README § H, à garder).
- FAQ06-166 : « La dernière ronde se fait-elle en partant de la zone définie par les 3e/11e ? » → « **Pas exactement.** Le chemin de rempart est un point de départ […] c'est l'astre glorieux qui vous indique où aller. C'est là que les 3e/11e seront utiles. »

### Modèle M2 (écrit avant toute carte, pour la prochaine séance)
Les 3e et 11e sont **deux points trouvés à partir du rempart**, à 10 stades l'un de l'autre (07-120 « les positionner par rapport à un point de départ »), et c'est **le segment 3e → 11e, avec le ciel**, qui désigne la clairière (07-133), pas un cercle de 10 stades centré sur le départ. Conséquences testables :
- l'endroit n'a pas à être à 1 850 m du rempart (cohérent avec 06-244 « le coffre n'est pas loin du rempart » et 06-025 « chemins très proches ») ;
- « on marche surtout sur l'une des deux » (06-247) : la clairière pourrait être **sur le 11e** (bois possible : passerelle, platelage, pont de bois) ;
- le 3e (« la troisième », pierre) pourrait être au rempart ou très près.
Test à faire : lister les objets de même nature, dénombrables par rang depuis le rempart, dont le 3e et le 11e sont à 1 850 m ± 1 %, **puis** appliquer d'abord le filtre public / bâti / monument.

## 3. Entonnoir « public d'abord » à courte portée (≤ 1,6 km de l'esplanade)
Règle posée avant : toutes les parcelles publiques (DGFiP groupes 1-4) ≥ 300 m², sans seuil de bâti inventé ; on mesure la distance au ruisseau (BD TOPO, écoulement naturel), au bâti, la part boisée. Script `scripts/public_proche.py`, sortie `scripts/public_proche.out.txt`. **188 parcelles**, dont 35 à ≤ 60 m d'un ruisseau.

Hors Pontcharra-ville et hors parcelles collées aux maisons, il reste trois groupes :

| Groupe | Où | Ce que c'est | Contre |
|---|---|---|---|
| **S1** Saint-Maximin B 1735, 1736, 2667, 2669 | 45.4177, 6.0338 ; 1 260 m, cap 168° | **petite clairière communale en forêt**, croisée de deux chemins, un ruisseau intermittent sans nom y **prend naissance** et descend vers le nord-ouest | bâti à 44-91 m (maisons de 7-9 m à l'est) ; **pente ≈ 19°** (fauteuil, 03-112, difficile) ; cap 168° sans lecture textuelle |
| **B1** Pontcharra AH 344, 345, 351, 370, 371, 379, 72 | 45.4375-45.4386, 6.043-6.047 ; 1 260-1 590 m, caps 44-51° | bois de berge communal le long du **Bréda**, au bord de la route | le Bréda est un torrent, pas un « ruisseau » ; route collée ; FAQ06-180 met en garde contre les grands cours d'eau |
| **É1** Saint-Maximin B 1969, 1315 | lieu-dit « Le Chêne, la Roche et le Vivier », 120 m de la tour | l'**étang d'Avalon** (vivier médiéval) est communal | Espace naturel sensible (zone protégée exclue, FAQ8) ; maisons à 7-37 m des parcelles. Déjà classé « repère, pas zone du coffre » le 01/10 |

Aucun des trois ne passe proprement toutes les contraintes. S1 est le seul qui a la forme de la scène (clairière, jonction, ruisseau, communal) : **piste faible**, à garder comme exemple de ce que l'entonnoir peut sortir, pas comme candidat.

## 4. Où en est-on
- Contrainte officielle confirmée : public, pas de bâti, pas de monument (annonce du 02/07).
- Avec le modèle « cercle de 10 stades autour du départ », **aucun lieu ne passe** (pré A compris).
- Prochaine étape : tester M2 (§ 2), en appliquant le filtre public en premier.
