# T12F — Rapport : le crypto de 25 lettres (piste F)

Id = T12F. Question : exploiter « Dieu sut se montrer favorable » (25 lettres) comme
anagramme / palindrome / mesure numérique / Vigenère / SATOR, chaque résultat testé
contre un témoin (200 phrases françaises aléatoires de 25 lettres).

Méthode : scripts archivés `T12F_*.py` + `.out.txt` (scratch `exk_e12/`). Lexique
français 323 417 mots (raw.github an-array-of-french-words), toponymes IGN 2 859 noms
(toponymie_12km, cours_d_eau, troncon_hydro, lieu_dit_non_habite, foret_publique).
Témoin : 200 fenêtres de 25 lettres tirées de texte français reconstitué (lexique).

**Lettres (25) :** D I E U S U T S E M O N T R E R F A V O R A B L E
Multiset : A×2, B, D, E×4, F, I, L, M, N, O×2, R×3, S×2, T×2, U×2, V.
**Absentes : C, G, H, J, K, P, Q, W, X, Y, Z** → impossible de former : Hugues d'Avalon
(G,H), Bayard (Y), Lincoln (C), Glastonbury (G,Y), Pontcharra (P,C,H), Saint-Maximin (X),
Chartreux (C,H,X), chemin/château/roche/souche/épée/coupe (C,H,P).

---

## 1. CE QUI SURVIT

### 1.1 La phrase épelle « AVALON » (et « MERLIN », mais pas les deux) — FAIT fort
- « avalon » est formable à partir des 25 lettres : **A,V,A,L,O** viennent de
  « fa**v**o**ra**b**l**e » (« avalo ») + **N** de « m**o**n**t**rer ». Lecture propre :
  le dernier mot donne AVALO, le précédent donne le N → **AVALON**.
- « merlin » est aussi formable, mais **pas simultanément** : Avalon et Merlin exigent
  chacun l'unique **L** et l'unique **N** du sac. La phrase choisit donc l'un des deux.
- **Avalon est le nom de la zone finale** : toponyme IGN « avalon » à **145 m** de la tour
  (45.42997, 6.03217), 1 285 m du château Bayard. La tour d'Avalon (45.429083, 6.030808)
  porte ce nom. C'est cohérent avec FAQ07-088 « confirmateur crucial de la zone finale ».
- « tour d'avalon » (11 lettres, `tourdavalon`) est lui aussi formable intégralement.

### 1.2 Témoin : « avalon » n'est pas banal à former (signal modéré)
- « avalon » est formable dans **12/200 = 6 %** des fenêtres françaises aléatoires.
- Les 16 mots-thème testés (avalon, merlin, isère, savoie, ruisseau, sentier, forêt,
  étoile, lune, stade, bois, astre, montrer, favorable, dieu) sont **tous** formables par
  la phrase ; les témoins n'en forment en moyenne que 4,5 (max 12). Réel = 16 > max témoin.
- Toponymes IGN (≥4 lettres) formables à <3 km de la tour : **22** (témoin : moy 7,2,
  max 22, 2/200 fenêtres ≥ 22 → ~99e centile). Parmi eux « avalon » (145 m), « labruta »
  (385 m), « lebreda » (629 m), « merlin » (2 457 m).
- Conclusion : le chiffre est suggestif mais NON décisif seul (6 % de faux positifs).
  C'est le fait **qualitatif** qui pèse : phrase laissée en français volontairement
  (FAQ07-218/04-182) + elle épelle exactement le nom de la zone (Avalon).

---

## 2. CE QUI EST TUÉ (avec raison)

### 2.1 Anagrammes exactes en 2-3 mots → bruit pur (TUÉ)
- 2 mots exacts (25 lettres) : **2** solutions — « boulevardiers + fomentateurs »,
  « désobstruerait + roman-fleuve ». Témoin : moyenne **9,6** (max 380) → la phrase en a
  MOINS que le hasard ; et les 2 sont des mots français anodins. Aucun toponyme.
- 3 mots avec un mot « signifiant » : **15 854** partitions → pur bruit de dictionnaire.
- Sous-ensembles 15-25 lettres, 1-3 mots : aucun assemblage nommant un lieu réel.

### 2.2 Palindromes cachés → rien (TUÉ)
- Palindromes français de 5 lettres formables : radar, rever, rotor, sonos, solos, semes,
  tarat, seves, sanas, etete, talat, senes, salas (7 lettres : « retater » seulement).
- « R … R » (indice utilisateur) → radar / rever / rotor : aucun message. Le narrateur
  fait des palindromes (FAQ8), mais ils ne sont pas dans ces 25 lettres.

### 2.3 La phrase comme mesure numérique → aucun mapping propre (TUÉ)
- A1Z26 : somme 308 ; par mot dieu=39, sut=60, se=24, montrer=103, favorable=82.
- Longueurs de mots : **4-3-2-7-9** (Dieu=4, sut=3, se=2, montrer=7, favorable=9) — et
  NON « 5-3-2-7-6-7 / 4-3-2-7-6-7 » comme posé dans le brief (favorable = 9 lettres, pas 6).
  Concaténation = « 43279 ».
- Lettres « romaines » présentes : M=1000, L=50, I=1, V=5, D=500 → somme 1556. DIEU →
  D=500 seulement (I, U ne sont pas des chiffres romains).
- Aucun de ces nombres (308, 39/60/24/103/82, 43279, 1556) ne correspond aux constantes
  connues : 1 850 m (10 stades), 607 km, cap ~65°, 45.429/6.031, 12 m.

### 2.4 Vigenère / César → illisible (TUÉ)
- César 1-25 : seul ROT13 donne la sous-chaîne « geres » (bruit).
- Vigenère (déchiffrement) avec AMOR, ROMA, MACHAIRE, MOOR, EXKALIBUR, AVALON, BAYARD,
  ULTIMA, SATOR, GRAAL, ITER, NAGA, OR : aucune sortie ne contient un mot français ≥4.
  Tout est du charabia.

### 2.5 SATOR → pas de mot-message net (TUÉ, un seul écho faible)
- Commun : **16 lettres** (A×2, E×4, N, O×2, R×3, S×2, T×2).
- Lettres de la phrase ABSENTES du SATOR (9) : **B D F I L M U U V** → mots français :
  film, imbu, muid (anodins) ; latin « fluvium » (rivière) = étirement non retenu.
- Lettres du SATOR ABSENTES de la phrase (9) : **A A O O P P R T T** → mots français :
  **apporta**, apport, **tarot**, porta, tort, topo… « tarot » est le seul écho thématique
  (piste cartes/tarot de T12D), mais 9 lettres s'anagramment en des dizaines de mots :
  non significatif sans décompte propre.

---

## 3. Vérification géographique (tâche 6)

Tout élément qui nomme un lieu a été vérifié dans les données IGN autour de la tour
(45.429083, 6.030808) et du château Bayard (45.4242, 6.0179) :

| Nom formable | Distance tour | Distance Bayard | Nature IGN |
|---|---|---|---|
| **avalon** | **145 m** | 1 285 m | toponymie (le nom de la zone) |
| labruta | 385 m | 1 527 m | toponymie |
| lebreda | 629 m | 1 652 m | toponymie (Breda) |
| merlin | 2 457 m | 3 504 m | toponymie (lieu-dit) |

« isère », « savoie » sont des noms de région/département, pas des lieux ponctuels locaux.
Aucun autre toponyme formable ne colle aux distances/caps connus (1 850 m, 65°).

---

## Bilan
Le crypto de 25 lettres confirme **Avalon** : le dernier mot « favorable » fournit AVALO,
le mot « montrer » fournit le N manquant, et « avalon » est un toponyme IGN réel à 145 m de
la tour — exactement la zone finale. C'est un **confirmateur**, pas un code à déchiffrer en
un autre lieu. Tout le reste (anagrammes exactes, palindromes, A1Z26/gematria, Vigenère,
SATOR) est du bruit : soit sous le niveau du hasard, soit sans mapping propre, soit sans mot
signifiant. Les nombres avancés dans le brief (longueurs 5-3-2-7-6-7) sont corrigés en
4-3-2-7-9.
