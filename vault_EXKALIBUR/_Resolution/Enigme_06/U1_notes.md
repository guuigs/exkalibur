# U1 notes — « boire à chaque C » (FAQ07-280)
## REPRISE
**Fait** (tout dans `calculs/U1_*`, .out.txt joints) :
1. Pool 83 lieux en C liés à une boisson (vin W, spiritueux S, bière/cidre B, eau E, Graal G, monastère M ; 6 pays), coords Wikipedia : `U1_pool.py`, `U1_coords.json`. 9 sans coord (Corbières, Clos de Vougeot, Cambus, Cooley, Cariñena, Cigales, Cangas-Narcea, Campo de Borja, Colares) → Cariñena/Cigales/Cambus toujours absents ; à compléter à la main si on veut.
2. Balayage exhaustif 73 lieux, 1 088 430 quadruplets × 6 ordres a priori (N>S, S>N, O>E, E>O, alpha, alpha inverse) : **1030 hits ±1 % de 341,61/342,01 (0,016 %)** ; 66 « purs » (même famille) : `U1_chaines.py`, `U1_hits.json`. Hasard T3 (111 lieux C) : 0,074 %.
   Chaînes « pures » les plus propres (ordre évident, non croisé) : **Chablis > Chassagne > Condrieu > Cornas 340,39** (vins, N>S = O>E = alpha) ; Cheverny>Chablis>Reims/Champagne (le « C » de Reims est faux) ; Cardhu>Cragganmore>Campbeltown>Coleraine 341,19 (whisky, **croise la lame** → écartée).
3. Familles curées (F1 vins/spiritueux FR, F2 eaux FR, F3 whisky/bière UK-IE, F4 Graal, F5 Ibérie, F6 moines-boisson, F7 emblématiques) : `U1_familles.py`. Hits vs hasard (D aléatoire 250-450) : F1 4 vs 2,6 ; F2 0 vs 0,5 ; F3 2 vs 1,3 (croise lame) ; F4 0 ; F5 0 ; F6 4 vs 0,8 (mais F6 construite en sachant que Clairvaux>Cîteaux>Cluny>Clermont 341,02 marche → biais post-hoc) ; F7 0. **Rien au-dessus du hasard, sauf F6 contaminé.**
4. Ordre « repas » (apéritif→digestif) sur 10 boissons emblématiques : 0/210 : `U1_repas.py`.
5. Ibérie NO (Graal de Galice O Cebreiro + Compostelle, Cambados/albariño, Covadonga, Cangas de Onís, Cudillero) : 5 hits vs 2,0 hasard (Cangas de Onís>Covadonga>Compostelle>Cambados 341,54 !) mais pool bricolé, aucune justification thématique de 4 ; `U1_regions.py`.
6. Lecture « exception » (2 premiers C = boisson, 2 derniers = Normandie/pommes-cidre) : 0 hit / 24 024 chaînes vs 2,0 attendus : `U1_regions.py`.
7. FAQ : recherche mots-clés (boire/vin/eau/coupe/pomme) dans faq_officielle_auteur.json : rien de plus sur les C-boisson (FAQ03-225 : gourde du barbu, É8, sans rapport).
**Conclusion** : la contrainte « boisson » ne réduit pas assez le pool : la distance ±1 % laisse des dizaines de chaînes plausibles à chaque famille, au niveau du hasard. Aucune identification.

## Interprétations non testées (intuition, confiance faible)
- **Lecture plateau** : « pomme rouge, grise ou jaune » = pions ? rouges = sphères (pommes !), bleus = tuiles ; « boire » = bleu/eau. Le joueur demande si à chaque C il peut « croquer » = capturer un pion rouge ? Réponse « non, mais boire » ≈ les C correspondraient à des cases/pions bleus (eau), pas rouges. Or FAQ03-265 : identifier ce que sont les pions bleus « très utile ». Piste : les 4 C = 4 des 7 pions bleus (à identifier sur photo macro (0,0),(6,0),(1,1) illustrés).
- « À l'exception du dernier et avant-dernier C » : les 2 derniers C seraient autres que boisson (potentiellement pommes). Non résolu.
- Avalon = « île des pommes » : les 2 derniers C pourraient être arthuriens.

**En cours** : rien.
**Prochaines étapes** : (a) obtenir macro des pions bleus ; (b) ajouter anagrammes (FAQ04-189) sur noms de boissons (multisets) ; (c) si un lieu est identifié par autre voie, tester les chaînes avec lui comme point fixe.
**Écarté** : pools larges de boissons + distance seule (0,016 % ≈ quelques centaines de chaînes, indiscernable du hasard) ; ordre repas ; Normandie-cidre ; whisky (croise la lame).
