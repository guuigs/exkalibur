# T3 — agent « histoire & thème » (É6 Libera nos a malo)

## REPRISE
**(1) Faits + résultats**
- **Itinéraire Urbain II 1095-96** (sources : fr.wikipedia « 1095 », « 1096 », Urbain_II, Concile_de_Clermont_(1095) ; sophiahistorica.com ; catholic.com ; Persée Crozet 1937 et Becker 1997 = seulement résumés accessibles) : 5 août 1095 Valence (cathédrale) → 15 août Le Puy → 18 août La Chaise-Dieu → 23 août Romans → 11 sept. **Cluny** (consacre l'autel le 25 oct.) → Autun → Souvigny (début nov.) → **Clermont** (concile 18-27 nov.) → déc. Limoges → 10 fév. 1096 Angers → Le Mans, Tours, Poitiers, Saintes, Bordeaux → 24 mai Toulouse (Saint-Sernin) → **Carcassonne** → 28 juin Maguelone → juillet Nîmes. C attestés : **Chaise-Dieu, Cluny, Clermont, Carcassonne** (+ Chinon/Cormery non attestés). Cahors/Conques/Cadouin/Cîteaux/Clairvaux : **aucune source de passage**.
- **Hugues de Payns 1127-29** (fr.wikipedia Hugues_de_Payns, Concile_de_Troyes_(1129)) : envoyé en Occident 1127 ; Champagne (Barbonne, don de Thibaud II) → Anjou, Normandie, Angleterre, Flandre → retour en Champagne ; concile de **Troyes 13 janv. 1129** ; retour en Terre sainte fin 1129. Aucun C attesté sauf Champagne/Troyes (pas C). Étapes précises non documentées → pas de chaîne en C propre.
- **Chaînes a priori** (script `calculs/T3_chaines.py` / `T3_chaines2.py`, sorties `.out.txt`, coords solveurB_C_coords.json, haversine R=6371,0088) :
  | chaîne (ordre) | L km | écart /341,6 | lame |
  |---|---|---|---|
  | Chaise-Dieu>Cluny>Clermont>Carcassonne (chrono Urbain II) | 577,2 | +69 % | non |
  | Cluny>Clermont>Carcassonne (3 C) | 432,7 | +27 % | non |
  | Cluny>Clermont>Cîteaux>Clairvaux (chrono fondations) | 471,9 | +38 % | non |
  | Cluny>Clermont>Cadouin (3 C) | 345,2 | +1,06 % | non |
  | Chinon>Caen>Canterbury>Cassel>Clairvaux (Templiers 1127-29) | 934 | — | — |
  | **Clairvaux>Cîteaux>Cluny>Clermont** (seule permutation ±1 % des 4 C Cluny/Clermont/Cîteaux/Clairvaux) | 340,99 | −0,18 % | non |
  Aucune permutation des 4 C d'Urbain II n'approche 341,6 (min 468,8 km).
- **Test du hasard** (T3_chaines.py, 4 lieux en C tirés parmi 67 lieux de France, N=30 000) : P(une chaîne d'ordre fixé tombe à ±1 % de 341,6) = **0,063 %** ; P(au moins un ordre parmi 12 tombe à ±1 %) = 0,74 % ; P(le plus court chemin tombe à ±1 %) = 0,23 %. Combiné aux résultats B08 (noyau 19 lieux : 3 chaînes ±1 % contre médiane 2 pour D aléatoire ; noyau 43 lieux : 132 contre médiane 238) : **aucun excès** de touches pour un choix « thématique » — le hit Clermont-Cluny-Cîteaux-Clairvaux est au niveau du hasard (dès qu'on a ~20 lieux plausibles, on attend ~3 chaînes).

**(2) En cours** : rien.
**(3) Prochaines étapes** : (a) l'ordre gagnant Clairvaux>Cîteaux>Cluny>Clermont n'est pas chronologique ; seule justification narrative possible : « de Bernard/Templiers vers Urbain II/croisade » (remonter aux origines, ou sens Clermont 1095 → Cluny → Cîteaux → Clairvaux = croisade → Templiers via Bernard). Cîteaux n'est **pas** justifié par le texte ni par l'enluminure → sélection ad hoc. (b) Si un autre agent trouve le vrai mécanisme (anagrammes des pions), tester ses 4 C avec `T3_chaines.py::length/crosses`. (c) Non testé : Cormery (« Cormaricus ») — pas de lien Urbain II/Templiers trouvé ; Carcassonne (écu C rouge de la carte) : test seul, chaînes Carcassonne-Clermont-Cluny trop longues (432 km, 3 C) ; avec 4e C il faudrait des jambes très courtes (impossible : Carcassonne–Clermont = 291 km, il reste 50 km pour 2 jambes → un 4e C à ≈ ≤ 50 km de Clermont/Carcassonne (ex. Cahors/Conques ne collent pas)).
**(4) Écartées** : chaîne chronologique Urbain II (577 km) ; chaîne 3 C Cluny-Clermont-Carcassonne (433 km) ; chaîne Templiers 1127-29 (aucun C attesté, 934 km) ; ordre chronologique Cluny→Clermont→Cîteaux→Clairvaux (472 km) ; aucune ne colle à D.

## Liste justifiée des candidats C (thème → lieu → statut)
- **Clermont** (concile/appel 1095 ; texte « porter la guerre très loin ») : très fort. **Cluny** (Urbain II ex-prieur, autel 1095 ; 3 clochers de l'enluminure ; texte « Sépulcre… ») : fort. **Carcassonne** (passage d'Urbain II 1096 ; C rouge de la carte ; épée d'É1 forgée là) : moyen. **La Chaise-Dieu** (Urbain II 18/8/1095, litige avec Cluny) : faible. **Clairvaux** (Bernard, Règle templière, lien Troyes 1129) : moyen. **Troyes** (concile 1129) et Payns : non C. **Cîteaux, Cadouin (Suaire rapporté de croisade), Cahors, Conques** : sélection non ancrée dans le texte (piste joueurs).
- Graal/coupe de Vie : pas de C évident sans mécanisme (Corbenic, Camelot ? — non testé).

## Conclusion (confiance : moyenne)
Aucun ordre « évident » (chronologique ou itinéraire) des lieux historiquement attestés en C (Urbain II, Templiers) ne donne D = 341,6/342,0 km. Le seul groupe ±1 % (Clermont-Cluny-Cîteaux-Clairvaux, 340,99) est au niveau du hasard, sans justification de Cîteaux avant la mesure, et son ordre n'est pas chronologique. La distance seule ne valide rien ; T3 n'a **pas** de déclic. Lame d'épée : aucune chaîne testée ne la croise.

## Rappel acquis (solveurs B)
- Sans a-priori, 132 chaînes/1,48 M à ±1 % de 341,6 ; contrôle D aléatoire : médiane 238.
