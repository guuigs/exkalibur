# T17A : inventaire des maillons et anneaux dorés, et recherche de la règle de décodage

Sous-agent T17A, 03/10/2026. Sources : IMG_4334 (planche entière, environ 600 px par panneau) et IMG_4335 à 4345 (gros plans), remis à l'endroit et agrandis avec Pillow (×2 à ×7). Les recadrages utiles sont dans `images_travail/t17a_*.jpg`.
Numérotation : celle de l'auteur, dans l'ordre de lecture (enl.1 = R1G, enl.2 = R1D, enl.3 = R2G, enl.4 = R2D, etc.). FAQ02-306 (poignée, enl.4) et FAQ06-176 (biche, enl.3) la confirment.
**FAIT** = vu sur la photo. **HYP** = interprétation.

**Verdict : je n'ai pas trouvé de règle qui produise un mot ou un nombre sans choix arbitraire.**
Trois acquis :
1. un inventaire corrigé de 12 groupes de maillons, dont **4 nouveaux** par rapport à T15D : les 2 rinceaux des coins hauts, et 2 maillons (pas 1) pour le soldat et pour Mercure ;
2. une **contrainte officielle jusqu'ici négligée** (FAQ8), qui élimine toutes les règles du type « nom de l'élément + nombre » ;
3. deux pistes qui sortent de l'inventaire : la bague de l'épée est l'**anneau de Silchester (Vyne Ring)**, et la chaîne d'or associée à l'écu rouge et à l'**émeraude** évoque les **armes de la Navarre** (Montsalvage = Saint-Palais).

---

## 1. Inventaire (FAIT, confiance par compte)

Un « maillon » est ici un anneau doré qui s'enchaîne à un autre ou qui pend à un élément. Convention de dessin observée sur toute la planche : les maillons alternent **de face** (ovale ou rond ouvert) et **de chant** (simple bande droite). Une bande droite qui passe dans la main et se prolonge par un « U » compte donc pour **2 maillons**. C'est ce qui corrige les comptes du soldat et de Mercure.

| # | Où | Élément porteur | Compte | Forme | Confiance | Recadrage |
|---|---|---|---|---|---|---|
| 1 | Bordure haute (au-dessus de l'enl.1) | **Cheval noir**, au cou | **5** (4 nets + 1 partiel à gauche, derrière l'encolure) | ovale plat, rond central, ovale, ovale ouvert | moyenne (4 ou 5) | `t17a_e1_cheval_noir.jpg` |
| 2 | Enl.1 | **Clé de Pierre** | **2 maillons d'or** sous un **anneau d'argent** (3 anneaux si on compte l'argent) | ovales allongés pendants | haute | `t17a_e1_cle_pierre.jpg` |
| 3 | Enl.1, rinceau du coin haut gauche (sous le médaillon) | rinceau du cadre | **2** anneaux entrelacés, qui pendent d'une volute | ovales | haute (**nouveau**) | `t17a_e1_rinceau_gauche.jpg` |
| 4 | Enl.2, rinceau du coin haut droit (sous le médaillon), symétrique du n°3 | rinceau du cadre | **2** anneaux entrelacés | ovales | haute (**nouveau**) | `t17a_e2_rinceau_droit.jpg` |
| 5 | Enl.3 | **Biche**, au cou | **3** | petit ovale, anneau rond, ovale allongé | haute | `t17a_e3_biche.jpg` |
| 6 | Enl.4 | **Poignée rouge de la porte verte** (écurie) | **2** | ovales, sous le bouton | haute (officiel : FAQ02-306 « deux chaînons dorés », FAQ02-210 « double anneau ») | `t17a_e4_poignee_porte.jpg` |
| 7 | Bout droit de la garde de l'épée centrale, dans l'enl.4 (FAQ03-220, FAQ03-375) | **Épée** (quillon droit) | **2 maillons + 1 bague** : un maillon passé autour du quillon, un ovale, puis une **bague** épaisse à chaton rectangulaire gravé et à jonc inscrit | ovales + bague | haute pour 2+1 ; 2 ou 3 selon qu'on compte la bague | `t17a_e4_garde_epee.jpg`, `t17a_e4_bague_vyne.jpg` |
| 8 | Enl.7 (planche seule) | **Mercure** (main gauche) | **2** (un de chant entre les doigts, un rond dessous). La clé de la main droite est en argent, à anneau double : je ne la compte pas | rond + bande | moyenne (1 ou 2) | `t17a_e7_mercure.jpg` |
| 9 | Enl.7 (planche seule) | **Vierge** (main gauche baissée) | **2** probablement, d'un or plus sombre | ovales | faible à moyenne (2 ou 3) | `t17a_e7_vierge.jpg` |
| 10 | Enl.9 | **Soldat romain** (main droite) | **2** : une bande droite de chant, tenue entre le pouce et l'index et visible au-dessus des doigts, plus un « U » de face dessous | bande + U | moyenne à haute (corrige le « 1 » de T15D) | `t17a_e9_soldat.jpg` |
| 11 | Enl.11 | **Dragon blanc**, à la patte | **2** anneaux entrelacés, en bracelet au-dessus des griffes | ronds | moyenne à haute | `t17a_e11_dragon.jpg` |
| 12 | Cadre bas, entre l'enl.11 et l'enl.12 | **Couronne fleurdelisée**, sur le bandeau | **7** en guirlande (3 à gauche, 1 au centre, 3 à droite) ; la boucle centrale pourrait aussi compter pour 2 | ovales ; anneau central | moyenne (7 ± 1) | `t17a_couronne_cadre.jpg` |

### Panneaux sans maillon d'or (vérifiés au gros plan)
Ces vérifications valent pour IMG_4334 et les gros plans. Pour l'enl.8, je n'ai que la planche.
- **Enl.5** : bannière Matheson (ceinture à boucle, pas de chaîne), ancre d'or sous la barque, cornemuseur (ceinture), saint à la croix.
- **Enl.6** : balance (fléau sans chaînes), médaillon de Jude, chevalier couronné, trophée de cerf.
- **Enl.8** (confiance moyenne, planche seule) : couronne « AAAA » flottante, gourde du saint, géant à 3 têtes.
- **Enl.10** : harnais bleu à pendeloques (pas d'or), Merlin, saint au « VI ».
- **Enl.12** : sanglier, tour aux 2 yeux, saint à la scie.
- **Cadre bas** des enl.11 et 12 : les cercles des rinceaux (« ooC ») sont des volutes fermées, pas des maillons.

### Éléments écartés ou à part
- Les **4 cloches** de l'enl.7 pendent à un **pointillé**, pas à une chaîne.
- Les cercles isolés des rinceaux près des médaillons des coins sont des volutes décoratives, pas des maillons.
- Le parchemin des textes (FullSizeRender) n'a **pas de chaîne d'or visible** : rubans, fleurs de lys, portraits.
- Dans le ciel de l'enl.9, l'**émeraude** est un ovale vert facetté en étoile au-dessus de la tête d'âne. Ce n'est pas un maillon, mais elle compte pour la piste Navarre (§3).

### Totaux (avec leur fourchette)
- Multiset principal : {5, 2, 2, 2, 3, 2, 3, 2, 2, 2, 2, 7}.
- Total : **34** avec les rinceaux et la bague ; **30** sans les rinceaux ; **27 à 36** en cumulant toutes les incertitudes.
- 9 groupes sur 12 valent 2 ou 3. Les seuls nombres qui sortent du lot sont le **5** (cheval) et le **7** (couronne).

---

## 2. Contrainte officielle décisive (FAQ8, transcription `faq8f.txt`)
- Question : si les maillons avaient été placés ailleurs, auraient-ils dû rester associés à leur élément d'origine ? Réponse : « je ne comprends pas ce que vous entendez par élément d'origine, mais **ils auraient pu en effet être placés ailleurs, sans que ça change quoi que ce soit** ».
- « J'ai du mal à compter les maillons… rédhibitoire ? » Réponse : « Non… **pas grave si vous êtes à un ou deux près**, vous finirez par comprendre de quoi il s'agit. »
- « Crypto des anneaux… » Réponse : « **précieux pour la résolution de la onzième ou de la douzième** énigme… encore peu découvert ».
- Autres réponses utiles :
  - FAQ8 : anneaux liés à Montsalvage ? « je ne pourrais pas répondre » ;
  - FAQ07-226 : d'abord Montsalvage ou d'abord l'« énigme des chaînons » ? « compliqué de répondre » ;
  - FAQ07-209 : combiner les chaînons pour obtenir un mot, résolution « plus imagée » ? « vous avez de bonnes intuitions » ;
  - FAQ07-282 : les chaînons ne confirment pas le narrateur.

**Conséquences logiques** :
- (a) **L'élément porteur et le panneau ne comptent pas.** Toute règle « n-ième lettre du nom de l'élément » ou « indice dans le texte de l'énigme du panneau » est donc contraire à la FAQ.
- (b) Le résultat **tolère une erreur de ±1 ou 2** sur le comptage. Il ne peut donc pas s'agir d'une lecture lettre par lettre où chaque unité compte. Ce qui reste plausible :
  - un **total** qui évoque quelque chose de connu ;
  - une **forme** de suite que l'on reconnaît (« plus imagée ») ;
  - ou un **symbole** que l'on reconnaît, plus que l'on ne le calcule.

---

## 3. Règles testées (script `scratchpad/rings/rules.py`)

| Règle | Résultat | Verdict |
|---|---|---|
| n-ième lettre du nom de l'élément, dans l'ordre de la planche (CHEVAL→A, CLÉ→L ou PIERRE→I, BICHE→C, PORTE→O, ÉPÉE→E, MERCURE→E, VIERGE→I, SOLDAT→O, DRAGON→R, COURONNE→N) | « A L C O E E I O R N », aucun mot ; en anagramme avec synonymes et ±1, **33 des 50 mots cibles sont formables** (NAVARRE, AVALON, TERRAIL, ISÈRE, TAPON, PONT, CHÊNE…) | **bruit pur**, et contraire à FAQ8 (a) |
| Nombre → lettre (A=1) | E B B B C B C B B B B G | rien |
| Total | 30 à 34 selon le périmètre (27 à 36 au pire). Échos possibles : 30 deniers (« le prix de la trahison », É9) ; 33 (âge du Christ, *Consummatum est*) | rien d'unique ; aucun des deux ne sert à l'É11 ou l'É12 de façon calculable |
| Suite reconnaissable (Fibonacci 1-1-2-3-5-8, ou nombres premiers 2-3-5-7) | Tentante avec les comptes de T15D (1, 1, 2, 3, 5, 7). Mais au gros plan le soldat et Mercure ont **2** maillons, pas 1, et il y a **neuf groupes de 2** | **affaiblie**. Elle reste seulement compatible avec « à un ou deux près ». Si c'était φ, cela rejoindrait T13I (1, √5 et 3 sur l'enl.11 ; 72° = angle lame/route de l'É11), mais je ne le démontre pas |
| Total → angle de l'É11 (cap 65°) | Au cap exact de **65,00°**, D·π depuis Saint-Palais arrive à **120 m du château Bayard** (lame + 72,00° : 0,98 km). Mais le total ne vaut pas 65, et une erreur de 2° décalerait l'arrivée de 21 km | non |
| Comptes → rangs « troisième et onzième » | Les 2 premiers panneaux totalisent **11** maillons (cheval 5 + clé 2 + 2 rinceaux) et le 3e (biche) en a **3**. C'est une coïncidence curieuse, mais elle dépend du périmètre (sans les rinceaux : 7) | anecdotique |

---

## 4. Deux pistes qui sortent de l'inventaire (HYP, à valider par Guilhem)

### 4a. La bague de l'épée = l'anneau de Silchester (Vyne Ring) : confiance moyenne à haute
- **FAIT** (photo) : la 3e pièce de la chaîne de la garde est une **bague** épaisse, avec un **chaton rectangulaire gravé** et des lettres sur le jonc.
- Le **Vyne Ring** (anneau de Senicianus) est une bague d'or romaine trouvée **près de Silchester** avant 1786. Il a un **chaton carré** gravé d'une **Vénus** (« VE / NVS ») et un jonc à 10 facettes inscrit « **SENICIANE VIVAS IIN DE** ». Il passe pour avoir inspiré l'Anneau unique de Tolkien.
- Cela explique trois réponses de la FAQ :
  - FAQ02-243 : la bague a un motif à identifier, qui donne « un élément de confirmation très important » ;
  - FAQ03-220 et FAQ03-375 : l'anneau est « présent dans l'enluminure quatre » (*Rex dei gratia*, « quérir l'**anneau du sacre**, à 181 milia » = **Silchester**) ;
  - FAQ03-069 : un « anneau en or » anachronique, découvert bien plus tard.
- On peut aussi rapprocher la **Vénus** de Milo posée sur la White Tower (enl.2).
- **Portée** : cette pièce **confirme l'É4** (déjà validée). Elle ne sert pas directement à l'É11 ou l'É12.

### 4b. Chaîne d'or + écu de gueules + émeraude = armes de la Navarre : confiance moyenne
- Les armes de la Navarre sont « **de gueules aux chaînes d'or** posées en orle, en croix et en sautoir, chargées en cœur d'une **émeraude** ». Selon la légende, ce sont les chaînes de Las Navas de Tolosa (1212), rompues par **Sanche** VII le Fort.
- Sur la planche, plusieurs éléments vont dans ce sens :
  - le cheval du frontispice porte la **chaîne d'or la plus longue** (5 maillons), juste à côté de l'**écu rouge plein**. L'indice officiel dit « l'écu de Montsalvage se dresse à dextre du cheval », et le rouge plein est l'écu ancien de la Navarre ;
  - le ciel de l'enl.9 montre une **émeraude** au-dessus d'une **tête d'âne**. HYP faible : l'âne de **Sancho** ;
  - la couronne fleurdelisée du cadre bas porte elle aussi une guirlande de maillons. HYP : « roi de France **et de Navarre** ».
- Cette lecture colle aux deux contraintes FAQ8 : la place exacte des maillons n'a pas d'importance, et une erreur d'un ou deux ne gêne pas, car on reconnaît un **emblème** plus qu'on ne calcule un nombre. Elle colle aussi à « plus imagée » (FAQ07-209), à « sans beaucoup de prérequis » (FAQ05-166), à « précieux pour la onzième » (Montsalvage = **Saint-Palais**, capitale de la Basse-Navarre) et au refus de répondre sur le lien anneaux / Montsalvage (FAQ8, FAQ07-226).
- **Faiblesse** : elle n'explique pas pourquoi l'auteur insiste sur le **nombre** de maillons par élément (FAQ06-205, FAQ06-176). Elle ne donne ni l'angle de l'É11, ni rien pour l'É12.

---

## 5. Conclusion
- **Inventaire** : 12 groupes, environ **30 à 34 maillons d'or**. Les comptes sont fiables à ±1, sauf pour la Vierge et la couronne. Les recadrages sont dans `images_travail/t17a_*.jpg`.
- **Aucune règle de décodage trouvée** ne donne un lieu, un nom de ruisseau, un nom de clairière, les 3e/11e de l'É12, une unité ou une direction **sans choix arbitraire**. Les règles « élément + nombre » sont exclues par l'auteur lui-même (FAQ8).
- **Le plus solide** :
  - (1) la bague = **Vyne Ring de Silchester** (confirme l'É4) ;
  - (2) la lecture **chaînes d'or + émeraude = Navarre** pour Montsalvage. C'est un « crypto imagé » qui tolère les erreurs de comptage. Elle aide l'É11 (le départ), pas encore l'É12.
- **À faire** :
  - photo de près de l'**enl.7** (Mercure, Vierge) et de l'**enl.8**, absentes des gros plans ;
  - recompter la **couronne** (7 ou 8 décide entre Fibonacci et nombres premiers) ;
  - lire les lettres gravées sur la bague, à comparer avec « SENICIANE VIVAS IIN DE » et « VENVS ».
