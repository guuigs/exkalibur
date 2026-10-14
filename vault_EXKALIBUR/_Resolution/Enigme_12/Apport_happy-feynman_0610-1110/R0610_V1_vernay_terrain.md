# R0610_V1 — Étude terrain « depuis chez soi » du Lac du Vernay (Chapareillan, 38075)

**Date** : 06/10/2026 — **Statut** : partiel → complété. **Verdict : RIEN de fiable** (échec de la contrainte décisive FAQ 05-155).

Données réutilisées : cadastre Etalab 38075, DGFiP « parcelles des personnes morales » dépt 38 (situation 2025), LiDAR HD (MNT+MNH, 1 m, LAMB93, fenêtre 6×3 km), BD TOPO (WFS), OSM (Overpass). Scripts : `outils_scratch/r0610_V1_*.py`. Carte : `images_travail/r0610_V1_vernay_carte.jpg`.

---

## 1. PROPRIÉTÉ (Mission 1) — fusion cadastre + DGFiP pm

| Élément | Parcelle | Superficie | Propriétaire | Statut |
|---|---|---|---|---|
| **Lac du Vernay** | AL 0105 | 186 378 m² | **COMMUNE DE CHAPAREILLAN** | **PUBLIC** |
| Chute d'eau (report enl. 9) | AL 0093 | 4 526 m² | COMMUNE DE CHAPAREILLAN | PUBLIC |
| Coupe (report enl. 9) | AL 0003 | 17 457 m² | « PROPRIÉTAIRES DU BND 075 AL0003 » (bois) | **PRIVÉ** |

Parcelles à ≤ 400 m du lac : **262** — **52 PUBLIC (37,8 ha)**, 40 privées pers. morale (28,2 ha), 170 particuliers (62,3 ha).
Grands publics proches : AL 0105 (lac, 18,6 ha), AL 0096 (7,0 ha), AK 0160 / AL 0106 / AL 0080 (Département de l'Isère), AL 0107 (Syndicat mixte des bassins hydrauliques).
Privés proches : **AREA** (corridor A41 : AL 0111 = 7,3 ha + AL 0108/0109/0112/0113…), SERVETTE 37 (ZC), COTAGNIER (AL 0023-0035, ZC 0046…).

> **Correction d'un fait antérieur** : le lac n'est **pas** privé (l'hypothèse « Granulats Vicat / non public » est fausse) — il est **communal**, cohérent avec la mention AAPPMA « accessible aux pêcheurs ». La marge ouest (chute) est communale ; en revanche la **coupe** (la « grande roche » du texte) est en **bois privé**.

## 2. VISIBILITÉ réciproque (Mission 2) — LiDAR MNT+MNH (canopée)

Cible : rive ouest/sud-ouest et surface du lac (≈ 252 m d'altitude). Résultat : **0 point visible depuis tous les remparts candidats**.

| Observateur (hauteur œil) | Lac (centre) | Rive O (chute) | Cause du blocage |
|---|---|---|---|
| Sommet tour d'Avalon (+33 m, alt. 439 m) | caché +16 m | caché +19,5 m | canopée à ~2 925 m |
| Esplanade tour (+1,7 m) | caché | caché | canopée |
| Rue du Rempart (+1,7 m) | caché | caché | canopée |
| **Fort Barraux** (remparts, +8 m) | — | **caché +26 m** (relief, 930 m) | relief |
| Château Bayard (+5 m) | caché +28 m | caché | relief + canopée |

Les **5 clairières/croisements** du pourtour sont aussi **cachés de +20 à +22 m** depuis le sommet de la tour (bande forestière intermédiaire sur la pente descendant vers l'Isère).

> **ÉCHEC de FAQ 05-155** (« l'endroit est dans le champ de vision depuis le chemin de rempart ») : ni le lac, ni la rive, ni les clairières ne sont visibles à l'œil nu depuis le rempart le plus haut (sommet de la tour).

## 3. TERRAIN autour du lac (Mission 3, ≤ 400 m)

- **Croisements (≥3 voies)** : 13. Principaux : **(45.44753, 5.99907)** 5 voies, lac+186 m, clairière (MNH 0), domaine public (chemin non cadastré) ; **(45.45044, 6.00340)** 4 voies, lac+19 m ; (45.44757, 6.00289) en AL 112 **AREA (privé)**.
- **Clairières** (MNH<2 m) 36 % ; forêt (MNH≥10 m) 48 % ; **pente médiane 4,8°** (fauteuil OK), max 73°, 17 % >20°.
- **Roches/relief** (fenêtre 5 m ≥1 m) : 29,6 % des cellules (gravière rugueuse, pas une « roche isolée » nette).
- **Bâti** le plus proche : **293 m** (≥100 m satisfait). Souches : non détectables au LiDAR (canopée).
- **Arrivées d'eau** : écoulement naturel à **117 m** (rive ouest, 45.44747/5.99731), buse 118 m, canal 136 m, ruisseau 198 m.

## 4. DÉROULÉ du texte (Mission 4)

Depuis les croisements en clairière : « eaux à senestre » = ruisseau ouest (117 m) plausible ; « grande roche » = la **coupe (AL 3, PRIVÉ)** ; puis 10 pas N + 10 pas E + 8 pas (cap 63,7/68,6/73,9°).
Filtre (public + bâti ≥100 m + pente) : les points de fouille retombent **hors parcelles publiques** pour la plupart des croisements testés (public=False), pentes 0–31°. **Aucun croisement ne donne un parcours complet sur domaine public** (la roche-coupe est privée, et la plupart des fouilles débouchent en parcelles privées AREA/COTAGNIER/SERVETTE).

## 5. 3e / 11e à 1 850 m ±1 % (Mission 5)

- Seules 2 paires de même nature : « Le Bréda » (rivière) ↔ « Plan d'eau des Lônes » (étang, 0,77 km du lac) à 1,864 km — **hétérogène (rivière ≠ plan d'eau)** ; 2 ponts anonymes à 1,863 km (à 1,94 km du lac).
- Distances remarquables : Fort Barraux **1,72 km** du lac ; Château Bayard 1,94 km ; Tour d'Avalon 3,22 km. Aucune à 1 850 ±1 %.
- ⇒ **RIEN de fiable** (cohérent avec PISTES_ECARTEES ligne 16 : « 108 paires contre 71 au hasard », niveau du bruit). Test de hasard : 2 paires trouvées ≈ attendu par hasard sur ~40 éléments.

## 6. VERDICT

**RIEN de fiable** pour le Lac du Vernay comme zone finale. Point positif unique : **le lac est bien public (communal)**, ce qui lève l'incertitude de propriété. Mais la contrainte décisive **FAQ 05-155 (visibilité depuis le chemin de rempart) échoue totalement** (lac, rive et clairières cachés de 16–28 m par relief/canopée depuis tous les remparts candidats, y compris le sommet de la tour à 33 m). S'y ajoutent : la « coupe »/grande roche en **bois privé**, la distance 3,2 km (contre « pas loin »/« tout près »), l'absence de paire 3e/11e à 1 850 m, et le grand lac de l'enluminure (presqu'île, cygnes, aqueduc) qui ne correspond pas à une gravière.

**Recommandation** : ne pas creuser au Vernay ; conserver comme acquis le caractère **public** du lac (utile si une autre piste reconverge vers lui). Prochaine étape : revenir aux candidats proches de la tour (≤1 km) visibles du sommet, en réutilisant la méthode de visibilité canopée ici validée.

## Fichiers produits
- Rapport : `vault_EXKALIBUR/_Resolution/Enigme_12/R0610_V1_vernay_terrain.md`
- Carte : `images_travail/r0610_V1_vernay_carte.jpg`
- Données : `donnees_travail/r0610_V1_vernay/` (mnt.npy, mnh.npy, lidar_meta.json, wfs_*.json, osm_v1.json, cadastre-38075-*.json.gz, pm_38.csv, parcelles_400m.json, geoms.json)
- Scripts : `outils_scratch/r0610_V1_fetch_lidar.py`, `_fetch_wfs.py`, `_fetch_osm.py`, `_propriete2.py`, `_visibilite.py`, `_profil.py`, `_terrain2.py`, `_derouler.py`, `_pointscles.py`, `_paires1850.py`, `_carte.py`, `_reperes.py`, `_geoms.py`
