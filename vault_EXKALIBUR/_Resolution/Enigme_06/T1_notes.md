# T1 — ordre de lecture / Pater (notes)

## REPRISE
**Verdict : PAS TROUVÉ.** Toutes les pistes « Pater → lettres → lieu(x) en C » testées sont au niveau du hasard.

**(1) Fait + résultat** (scripts dans `calculs/`, sorties `.out.txt`)
- Positions relues sur `hd/R4G_panneau_x3.png` : identiques au BRIEF (rouges (3,0)(1,3)(1,5)(3,5)(0,6)(3,6)(4,3) ; bleus illustrés (0,0)(6,0)(1,1), unis (3,1)(4,2)(5,3)(5,5)). Le rond rouge hors plateau ressemble à « 5 » sur ce rendu (brief : S). Pas de zoom `region`.
- `T1_lib.py` : plateau, ~400 parcours (lignes/colonnes/boustrophédon, anneaux, rayons, spirales, 8 départs, 2 sens, ext↔int, + anneaux à départ/sens indépendants), sous-ensembles (R, B, R+B, vides, illustrés, unis…) ± S ± T, index multiset (hash) de noms en C : 35 k communes FR, GeoNames GB/IE/ES/PT/AD/FR, liste curée B, ~55 noms latins. Données dans `calculs/T1data/`.
- **run1** (`T1_run1.py`) : 21 phrases (Pater lat/fr/en/es/it/pt/cy/br, courtes/longues, fenêtres de 24) × parcours × sous-ensembles → 1 nom en C exact. Réel vs hasard (30 plateaux aléatoires) : communes 2245 vs 1984±269 ; geo_all 5840 vs 5776 ; curated 17 vs 40 → bruit.
- **run2** (`T1_run2.py`, événements distincts, 25 plateaux) : curated 121 vs 122±45 ; latin 53 vs 81±22 ; communes 4221 vs 4456±1144 → aucun signal. Hits « jolis » (Clisson, Créteil, Coutances, Chartres, Cistercium, Cantium, Canossa) incohérents entre eux.
- **run3** (`T1_run3.py`, César 0–25) : 872 vs 803±161 (6 plateaux) → bruit.
- **run4** (`T1_run4.py`, numéro de case = rang de lettre dans le Pater complet lat/fr/en, ou Harold/Libera) : 51 vs 57±13 (30 plateaux) → bruit.
- **run5** (`T1_run5.py`) : sur les phrases de 24 lettres, rouges ET bleus donnant chacun un nom en C (même parcours), ou R+B(+S,T) = 2 noms en C : **0 hit** (réel et hasard).
- 24 lettres = 24 cases est impossible pour un seul lieu (aucun toponyme en C de 24 lettres) ; seuls des sous-ensembles sont testables.

**(2) En cours** : rien.

**(3) Prochaines étapes (non faites)**
1. « 7 cieux planétaires » (Lune, Mercure, Vénus, Soleil, Mars, Jupiter, Saturne) ↔ 7 rouges / 7 bleus : non testé.
2. Décomposition en 3–4 noms (4 C) : non testé (seulement 2 noms).
3. Identifier les figures illustrées (0,0)(6,0)(1,1) sur HD avant tout mécanisme lettre.

**(4) Écartées** : lecture Pater (lat/fr/en…) × parcours naturels → anagramme d'un lieu en C ; César ; rang de lettre ; 2 noms sur R+B. Raison : bruit ≈ hasard (chiffres ci-dessus).
