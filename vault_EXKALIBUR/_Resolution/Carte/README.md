# Carte de travail de Guilhem (Google My Maps)

- Source : `networklink_original.kml`, qui pointe vers My Maps `mid=1YL85n1pv617HK_eEI2LSSEwwebiAk9Q`. Contenu téléchargé le 29/09/2026 dans `carte_guilhem_mymaps.kml`.
- Extraction : `extraire_kml.py` → `carte_guilhem_objets.json` et `extraire_kml.out.txt`.
- ⚠️ Ce **n'est pas** la carte au trésor officielle : c'est le travail de Guilhem, à traiter comme des **hypothèses** et à auditer comme ses notes.
- Pour rafraîchir la copie après des modifications dans My Maps : relancer `curl "https://www.google.com/maps/d/kml?forcekml=1&mid=1YL85n1pv617HK_eEI2LSSEwwebiAk9Q"`, puis `extraire_kml.py`.

## Contenu (29/09/2026)
| Dossier | Objets | Lecture |
|---|---|---|
| Epée – énigme 1 | León, Foix, Valence, Urquhart ; **Ligne 5** Urquhart→Valence (axe lame + poignée, **sans Lombrives**) ; **Ligne 6** León→Foix (garde) ; **Ligne 8** : rectangle à Paris (48,83–48,87 N ; 2,29–2,35 E) | Ligne 8 : origine inconnue, sans doute un essai ou une erreur. **À demander à Guilhem.** |
| Enigme 2 | Tour de Londres | = solution É2 |
| Enigme 3 | Tintagel ; Ligne 3 Tintagel→Silchester→Westminster | Chemin royal de l'énigme 4 |
| Enigme 4 | Westminster, Silchester | |
| Enigme 5 | Stonehenge, alignements du Ménec (Carnac) | |
| Enigme 6 | Hastings (la ville, pas Battle Abbey) | Cf. audit : le champ de bataille est à Battle |
| **Enigme 7** | Clermont, abbaye de Cluny, cloître de Cadouin, Sainte-Chapelle, forêt de Brocéliande ; lignes Cluny→Clermont→Cadouin, Tour de Londres→Sainte-Chapelle, « Garde brocéliande » Brocéliande→Sainte-Chapelle | Clermont, Cluny, Cadouin, (Sainte-)Chapelle : ce sont peut-être **les « 4 C » de l'énigme 6**. « Garde brocéliande » répondrait à l'énigme 7 (« trace la nouvelle garde… les bois qui mènent à la cité de l'Autre Monde »). |
