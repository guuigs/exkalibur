# Pont entre les deux branches de travail (14/10/2026)

Le dépôt a deux lignes de travail sur l'É12 qui ne se connaissent pas :

| Branche | Point de départ | Période | Fil conducteur |
|---|---|---|---|
| `claude/awesome-lamport-raceuj` (celle-ci, session cloud) | commit `b9e02ea` du 01/10 | 13-14/10 | textes d'abord : *Roman de la Rose* III/XI, Pâques 1524, pré A |
| `claude/happy-feynman-p7xsyy` (poste Windows) | même base | 06-11/10 | FAQ8, narrateur, terrain LiDAR, cadastre, audits |

La session cloud est partie du 01/10 sans voir le travail du 06 au 11/10. Ce fichier liste ce que l'autre branche avait déjà établi et qui touche le TODO d'ici. Rien n'est fusionné (trop de fichiers divergents) : on lit l'autre branche avec `git show origin/claude/happy-feynman-p7xsyy:<chemin>`.

## Acquis de `happy-feynman` utiles ici

| Sujet | Résultat | Fichier (branche happy-feynman) | Effet sur le TODO d'ici |
|---|---|---|---|
| Narrateur | **Bayard confirmé** (~29/30 critères FAQ ; la « gardienne de lumière » = sa dame, *Loyal Serviteur* ch. XIII) | `Enigme_12/R0610_N2N3_narrateur.md` | conforte E1 / jour dernier = 30/04/1524 |
| Règle de Guilhem sur Pontcharra | exclue **seulement comme ville** (« ville, zones d'activités, gare ») ; ses forêts restent permises | `Enigme_12/00_PISTES_VIVANTES.md` | à appliquer ici aussi |
| « à senestre » | Guilhem : **pas un filtre** (l'eau peut être à gauche ou à droite) | idem | adoucit la discussion V1/V2 du § 7.3 de `TEXTES_direction.md` |
| Contraintes éliminatoires | domaine public (DGFiP groupes 1-4), loin du bâti, hors ENS / Natura 2000 / réserves, **toujours appliquées en premier** | `Enigme_12/R1110_audit_et_inverse.md`, `R1110_PUB_rapport.md` | le pré A ne les passe pas (voir `R1410_controle_eliminatoire_preA.md`) |
| Inventaire du domaine public (8 km) | 5 311 parcelles publiques ; **à < 3 km aucun secteur public boisé + ruisseau + plat + loin du bâti hors Pontcharra** ; le côté est (levant) est privé | `Enigme_12/R1110_PUB_rapport.md` | même vide que le § 4 de `R1410_…` |
| Lac du Vernay | parcelle communale de Chapareillan (AL 105, 18,6 ha), le bassin peint colle après rotation de 110°, mais caché du rempart par la canopée | `Enigme_12/R0610_V1_vernay*` | piste « contour du bassin » (E19) déjà testée sur le Vernay |
| Audit des vagues DeepSeek | bug `CANOPY = MNH − MNT`, seuils inventés (bâti ≥ 100 m, pente ≤ 12°) : leurs « 0 survivant » ne sont pas des éliminations | `Enigme_12/R1110_audit_et_inverse.md` | ne pas reprendre leurs verdicts |
| FAQ8 relue | « une fois au départ de l'É12, vous pouvez oublier l'enl. 11 » ; « le dernier chevalier n'est pas un point précis à positionner » ; « l'épée est la dernière clé », « dernière intuition cruciale pour trouver la clairière » | `Enigme_12/00_PISTES_VIVANTES.md` | **E22 (enl. 11 comme carte) est à rétrograder** |
| Épée réelle | face B peinte = deux dragons ailés + pommes + calice ; pierre du pommeau à trois ♦ | `images_travail/discord_epee/`, `00_PISTES_VIVANTES.md` | sert l'item E6 du TODO |
| Pistes mortes du 06-11/10 | séries numérotées locales (13 types), balisage Bayard de Pontcharra, bornes royales, numéros de parcelles 3/11, chemins de croix extérieurs ≤ 10 km, J16, Le Mouret, Lônes, Mollettes, sentiers LiDAR (2 860 jonctions, niveau du hasard) | `PISTES_ECARTEES.md` | ne pas refaire |

## Ce que cette branche apporte et que l'autre n'avait pas
- 3e/11e = chap. III et XI du *Roman de la Rose*, vers 1524 ; lecture pascale (R2) ; visibilité au sol depuis la butte (seul le pré A à l'est) ; ciel de l'enl. 9 = émaux héraldiques ; croissant décroissant = aube du 30/04 ou du 01/05/1524.
- Le pré A, lui, tombe sur les contraintes éliminatoires (fichier `R1410_controle_eliminatoire_preA.md`).
