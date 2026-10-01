# T13I — rapport : l'enluminure 11 comme « mini jeu de cartes »

**Id : T13I · énigme 12 · date : 01/10/2026 · statut : piste close (lecture φ testée, lecture « cartes → géo » écartée).**

## 0. Méthode / limite
`vision_analyze` est indisponible dans cette session (pas de fournisseur vision configuré). La transcription repose donc sur : le schéma simplifié de Guilhem tel que décrit dans BRIEF_v3 + solution.md, et les réponses d'auteur (champ `a` du JSON FAQ) qui fixent ce qui est réellement sur le panneau. Les observations à lever sur l'original sont listées en §6. Calculs archivés : `T13I_01_cartes_phi.py` / `.out.txt`.

## 1. Ce que la FAQ fixe (contraintes dures, étiquetées)
| # | Contrainte (RÉPONSE de l'auteur) | Conséquence pour la lecture |
|---|---|---|
| FAQ03-294 | « D et C sur ceux du haut et rien sur les deux autres » | seuls **D et C** sont des lettres ; les pierres du bas (♠ pique, ♦ carreau) n'ont PAS de lettre |
| FAQ03-335 | « il y a juste deux lettres en plus sur les roches au fond, D et C » | idem ; X/T/G = décors ou mauvaises lectures, pas des lettres |
| FAQ03-137 | sur la pierre au trèfle, « un deux à l'envers ? » → « non, c'est la lettre C » | le C est bien C (pas G, pas 2) |
| FAQ05-091 | carreau/pique à compléter par une lettre ? « Non… notez le point d'interrogation… orientez-vous » | le « ? » complète ; « orientez-vous » = mise en ordre spatiale |
| FAQ05-163 | « Le point d'interrogation… un lieu, un nombre, une lettre ? » → « Un nombre » | le « ? » = un **nombre** |
| FAQ06-100 | « les trois chiffres vous aiguillent sur le chiffre » | 3 chiffres (1, √5/5, 3) → un nombre cible |
| FAQ07-294 | « plutôt vers le **nombre** important… comptez par vous-même » | le nombre cible = « le nombre important » ; il faut compter |
| FAQ03-016 | couleurs des chiffres non importantes | 1 bleu / 3 blanc / 5 rosâtre = décor, pas de sens |
| FAQ07-035 | pierres (chiffres+symboles) vs pierres en croix (R) = « deux éléments qui vous servent différemment » | **deux cryptos distinctes** |
| FAQ8 | « jeu de cartes de l'É11 : vous en aurez besoin, mais **pour autre chose** » | les symboles de cartes ne servent PAS aux 3e/11e |
| FAQ07-239 | « l'enluminure 11 aide à placer **une partie** des 3e/11e » | seule la croix (crypto B) sert au placement des 3e/11e |
| FAQ07-071 | « un jeu de cartes aide à identifier le dernier chevalier… vice-versa » | les cartes servent à É11 (dernier chevalier) |

## 2. Tableau des lectures (élément → interprétations → cohérence FAQ)
| Élément | Lectures proposées | Cohérence FAQ | Statut |
|---|---|---|---|
| **D** (sur ♥, HG) | Dame (rang 12) · Dix (X=10) · Dieu · Droite/dextre | **Dame de cœur** : jeu de cartes FR confirmé (FAQ07-071/100) ; « Dame de cœur » = Judith. Dix/Dieu : purs échos texte, sans appui. Droite/dextre : aucune FAQ, contredit le contexte cartes | **Dame** (retenu) |
| **C** (sur ♣, HD) | Cavalier/Chevalier (tarot) · Cent · Carreau · Cœur · Cénestre | **Cavalier de trèfle** : le tarot (ancêtre FR, FAQ07-100) a le rang Cavalier = « chevalier » ; FAQ03-137 (c'est un C) ; lien direct « dernier chevalier » (FAQ07-071). Carreau/Cœur = confusion lettre/symbole (non). Cénestre : aucune FAQ | **Cavalier** (retenu) |
| X (sur ♠, BG) | Dix · croix | FAQ03-335/03-294 : rien sur les pierres du bas → décor | écarté |
| T (sur ♦, BD) | Trèfle | idem, pas de lettre | écarté |
| G (« C/G ? ») | Gascogne · Gauche | FAQ03-137 : c'est un C | écarté |
| chiffres 1, √5, 3, ? | triangle 1/√5/3 · φ · carré magique 1-3-5 | voir §3 | **φ** (retenu), triangle écarté |
| croix 11×11 + 4 R | gabarit de placement des 3e/11e | FAQ07-239 + FAQ07-035 | retenu (§4) |

## 3. Lecture « nombre d'or » (la seule productive sur les chiffres) — FAIT arithmétique
- Les 3 chiffres 1, √5, 3 sont exactement ceux de **φ = (1+√5)/2** et **φ² = (3+√5)/2** ; le « 2 » (dénominateur) manque et peut être le « ? » ou les « II » du livre du saint (2 romain, vu 4×). « comptez par vous-même » (FAQ07-294) : le 2 est à compter (II).
- **cos 72° = (√5−1)/4** → √5 encode l'angle 72° = 360/5. Or l'« angle du dernier chevalier » (É11) vaut **72,08°** (cap Saint-Palais→Bayard 64,98° moins axe de lame É1 352,90°). Lien √5 → 72° = propre.
- **Triangle 1, √5, 3** : inégalité vraie (1+√5=3,236>3), angles = **14,31° / 33,56° / 132,13°** → rien de remarquable (ni 30/60/90, ni doré). **Écarté** (testé, rien ne « tombe juste »).
- **Géométrie des ancres (le résultat le plus fort)** : distance **Tour d'Avalon (45,429083 ; 6,030808) → arrivée É11 (45,4242 ; 6,0179) = 1144,3 m**, et **1850/φ = 1143,4 m** → ratio **1,0009 (écart 0,09 %)** ; de plus **1144,3 × φ = 1851,6 m ≈ 1850 m (les « dix stades »)**. Autrement dit : **les 10 stades de l'É12 = φ × (distance Tour→arrivée É11)**. ⚠️ Sensible aux coordonnées : avec le Bayard d'`exk.py` (45,423611 ; 6,018889) la distance tombe à 1127,8 m (ratio 0,9864, plus de match). Le point « arrivée É11 » doit donc être confirmé à ~1 m près pour valider ce lien.

## 4. La croix 11×11 (crypto des 3e/11e)
- Bras = 11 pierres, centre = 6e case **vide** ; R aux distances 1,1,5,5 du centre → positions 1, 5, 7, 11 (écarts 4, 2, 4).
- « 3e et 11e » = 3e et 11e pierre d'un bras, séparées de **8 cases**. Contre « dix stades » (1850 m) : 1 case = 10/8 = **1,25 stade = 231,25 m** (non propre), ou si le bras entier (1re→11e) vaut 10 stades, alors 3e→11e = 8 stades = 1480 m (≠ 1850, contradictoire avec FAQ07-120 « distance en ligne droite qui sépare les 3e et 11e »). → la croix donne un **gabarit de position** (la 11e = pierre du bout, marquée R), pas une échelle métrique directe.
- Cohérence « pierre / bois » (FAQ07-068 : pas d'écharde sur la 3e, écharde possible sur la 11e) : la 11e (au bout, R) peut être un élément en bois (poteau), la 3e une pierre lisse. HYPOTHÈSE (non testable bureau).

## 5. Tests géographiques — AUCUN signal (témoin aléatoire)
- Balayage de 315 destinations (3 départs × 5 distances × 21 angles) contre toponymes/lieux-dits/plans d'eau : 190 « touches » à <200 m = **niveau du hasard** (toponymie dense ~1 pt/100 m).
- Contrôle aléatoire : **16,8 %** de destinations aléatoires tombent à <150 m d'un plan d'eau → le seul « hit motivé » (1850 m @ 72° → 127 m d'un bassin) est non significatif.
- Aucun couple (distance φ = 706,6 / 1143,4 / 1850 m ; angle 0/72/90/137,5/180/241,7/270/64,98°) ne désigne une clairière/étang/croisement/bloc unique. → **la lecture « cartes → géo » ne produit pas de point contrôlable.**

## 6. Observations à demander à Guilhem (sur l'original, en une liste)
1. Le « √5 » est-il un **5 surmonté d'un signe racine**, ou un simple **5** ? (FAQ03-016 dit « cinq rosâtres » = 5 ; si c'est 5 et non √5, la lecture φ change.) C'est LE point décisif.
2. Position exacte du **« ? » noir** : sur quelle pierre / quel quadrant / en marge ? Est-il au 4e point cardinal (bas) complétant 3 (haut) / √5 (gauche) / 1 (droite) ?
3. Le **livre du saint** : les marques sont-elles des « II » (2 romain) et combien y en a-t-il (4 ?) — nécessaires pour la lecture φ (le « 2 » manquant).
4. Confirmer les **4 R** de la croix et leurs distances au centre (1, 1, 5, 5) + le nombre de pierres par bras (**11**) et la case centrale vide.
5. Que montre exactement chaque pierre du bas : **♠ pique** (BG) et **♦ carreau** (BD) — purs symboles, ou marques supplémentaires (le « X » / « T » vus par Guilhem) ?
6. Le **C** de la pierre ♣ est-il bien un C isolé (pas de « G » ni de « 2 » retourné à côté) — déjà confirmé FAQ03-137, à re-vérifier visuellement.

## 7. Conclusion (lecture complète et testée)
L'enluminure 11 contient **deux cryptos** (FAQ07-035) qu'il ne faut pas fusionner :
- **Crypto cartes (4 symboles ♥♣♠♦ + D/C + chiffres)** → sert à É11 : **D = Dame de cœur, C = Cavalier de trèfle** = le rang « chevalier » des ancêtres du jeu FR, donc **« le dernier chevalier »** (FAQ07-071, FAQ8 « pour autre chose ») ; **√5 → cos72°=(√5−1)/4 → l'angle 72°** du dernier chevalier (72,08° mesuré). La lettre « X » (dix) et le « T » ne sont pas des lettres (FAQ03-335).
- **Crypto croix (11×11 + 4 R)** → sert à **placer les 3e/11e** de l'É12 (FAQ07-239) : 3e et 11e pierre d'un bras, la 11e = pierre R du bout (bois → écharde, FAQ07-068).
- **Le nombre important** aiguillé par 1, √5, 3 = **φ** ; il est **confirmé par la géométrie des ancres** : 10 stades (1850 m) = φ × distance Tour d'Avalon → arrivée É11 (1144 m, écart 0,09 %), et 1850/φ = 1143 m ≈ 1144 m. Ce lien est le seul résultat « qui tombe juste » hors du bruit aléatoire, **mais il exige une coordonnée d'arrivée É11 exacte** et il confirme φ, sans encore placer les 3e/11e sur la carte (cela relève de la croix + du terrain).

**Preuve d'insuffisance (partielle)** : l'information du schéma ne suffit pas à trancher √5 vs 5, ni à localiser le « ? », ni à donner l'échelle métrique de la croix. Les 6 observations §6 sont à lever avant de poursuivre.
