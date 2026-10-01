# T1 tache 5 : genere T1_candidats.kml et T1_rapport.md a partir des JSON produits par les scripts T1_*
import json, math
from xml.sax.saxutils import escape
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
D=r'C:/Users/Admin/Guilhem workspace/EXKALIBUR/_Resolution/Revue_globale/'
tour=json.load(open(D+'T1_tour_jonctions.json',encoding='utf-8')); fort=json.load(open(D+'T1_fort_jonctions.json',encoding='utf-8'))
top=tour[:10]; topf=fort[:6]
tp=json.load(open(D+'T1_toponymes.json',encoding='utf-8')); bs=json.load(open(D+'T1_bassin_scores.json',encoding='utf-8'))
FORT=(45.4358,5.98723)
def flt(r): return ' '.join(k for k,v in (('trouée',r['trouee']),('eau≤150m',r['eau']),('public',r['pub']),('vue',r['vis']),('versant-E',r['est'])) if v) or '-'
def n_ok(r): return sum(bool(r[k]) for k in ('trouee','eau','pub','vis','est'))
pm=[]
def P(name,lat,lon,desc): pm.append('<Placemark><name>%s</name><description>%s</description><Point><coordinates>%.6f,%.6f,0</coordinates></Point></Placemark>'%(escape(name),escape(desc),lon,lat))
P("Tour d'Avalon (origine rempart, hypothèse)",TA[0],TA[1],'45.4288, 6.0308')
P("Fort Barraux (alternative rempart)",FORT[0],FORT[1],'Wikipedia 45.4358, 5.98723')
for i,r in enumerate(top,1):
    P('T%02d jonction (tour) %d/5'%(i,n_ok(r)),r['lat'],r['lon'],'score %.2f ; %.0f m cap %.0f ; %s ; filtres : %s ; ruisseau à %d m (%s), coule vers %.0f ; ruisseau vu depuis la jonction au cap %.0f ; alt %s m'%(r['score'],r['d'],r['cap'],'/'.join(r['nat']),flt(r),r['dh'],r.get('ruis_nom') or r.get('ruis'),r['flow_cap'],r['ruis_dir_depuis_jonction'],r.get('z')))
for i,r in enumerate(topf,1):
    P('F%02d jonction (fort) %d/5'%(i,n_ok(r)),r['lat'],r['lon'],'score %.2f ; %.0f m cap %.0f ; %s ; filtres : %s ; ruisseau à %d m, coule vers %.0f'%(r['score'],r['d'],r['cap'],'/'.join(r['nat']),flt(r),r['dh'],r['flow_cap']))
for r in bs:
    if r.get('nom'): P('Bassin IGN : %s (IoU %.2f)'%(r['nom'],r['iou']),r['lat'],r['lon'],'%.1f km cap %.0f, aire %d m2 ; ressemblance non probante'%(r['dist'],r['cap'],r['aire']))
seen=set()
for r in tp:
    if r['terme'] in('fontaine','âne','clairière','fée','chant','roche','loup','avalon','arc-en-ciel','rempart','bayard') and 'nature, sans nom' not in r['nom'] and (r['nom'].lower(),r['terme']) not in seen and r['d']<=4 and 'école' not in r['nom'].lower():
        seen.add((r['nom'].lower(),r['terme'])); P('Topo %s : %s'%(r['terme'],r['nom']),r['lat'],r['lon'],'%.2f km cap %.0f (%s)'%(r['d'],r['cap'],r['src']))
open(D+'T1_candidats.kml','w',encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>T1 candidats Exkalibur</name>'+''.join(pm)+'</Document></kml>')
N=len(tour); c=lambda k:sum(bool(r[k]) for r in tour)
pr={k:c(k)/N for k in ('trouee','eau','pub','vis','est')}
exp=N*math.prod(pr.values())
L=[]
L.append('# T1 : rapport terrain IGN (bassin, clairière, toponymes, fort Barraux)\n')
L.append('Date : 30/09/2026. Scripts : `T1_bassin2.py`, `T1_clairiere.py`, `T1_toponymes.py`, `T1_livrables.py` (sorties `.out.txt`). Sources : BD TOPO v3 (GeoJSON en cache), altimétrie IGN RGE ALTI, cadastre Etalab (lieux-dits), photo IMG_4342.\n')
L.append("""## Verdict
- **Bassin de l'enluminure 9 : aucune ressemblance forte** avec un plan d'eau IGN à ≤ 6 km de la tour (Maupas 0,83 ; Cheylas 0,60 ; Lônes 0,48 ; 18 surfaces sur 62 dépassent 0,80). Le contour est un blob trop générique. Confiance dans « non identifié » : haute ; confiance dans une identification quelconque : très faible (< 5 %).
- **Clairière** : sur 217 jonctions de chemins à ≤ 2,5 km de la tour, **aucune ne cumule** les 5 filtres. Le meilleur candidat n'a que 3 ou 4 filtres et aucun indice indépendant ne le désigne.
- **Toponymes** : « Avalon » (lieu-dit cadastral, 90 m de la tour), « Tire-Loup » (1,6 km E), « Château Bayard » (1,1 km) ; rien pour étoile, émeraude, diamant, ancre, lune, souche, charpentier, coupe.
- **Fort Barraux** : 0 jonction avec trouée, 0 en domaine public ; eau+vue+versant est = 4 jonctions sur le flanc ouest. Piste vivante, non favorite.
- **Bilan : pas de solution.** Filtres trop lâches, ou clairière trop petite pour la BD TOPO.
""")
L.append("## 1. Bassin (enluminure 9)\n")
L.append("""**FAIT** (recadrage HD de IMG_4342 tournée de 90° ; contrôle `T1_bassin_trace_controle.png`) :
- Étang bleu allongé (rapport petit/grand axe ≈ 0,58), extrémité gauche en pointe émoussée, lobe large à droite, bord haut légèrement creusé là où tombe une fine cascade issue du rocher rayonnant : le ruisseau **alimente** l'étang, aucune sortie visible. 2 poissons.
- Les **2 cygnes** sont sur le grand lac pâle de l'arrière-plan, pas dans l'étang.
- Rocher jaune-gris à rayons dorés portant la coupe ; grand arbre à fruits jaunes à droite.
- Horizon, de gauche à droite : chaîne bleutée ; butte grise avec petite tour/bâtiment blanc ; village orange à toits pointus et clochers ; longue muraille orange à arcades et créneaux ; montagnes roses et bleues.
""")
L.append("**Comparaison IGN** (62 surfaces d'eau hors cours d'eau à ≤ 6 km, IoU invariant aux rotations ±20° et symétries ; planche `T1_bassin_planche.png`) :\n\n| Plan d'eau IGN | Distance / cap | IoU |\n|---|---|---|")
for r in bs[:5]: L.append('| %s %s (%s) | %.1f km / %.0f° | %.2f |'%(r['nature'],r['id'][-8:],r['pers'],r['dist'],r['cap'],r['iou']))
for r in bs:
    if r.get('nom'): L.append('| **%s** | %.1f km / %.0f° | %.2f |'%(r['nom'],r['dist'],r['cap'],r['iou']))
L.append("""
**Test du hasard** : médiane IoU 0,74 ; 29/62 ≥ 0,75 ; 18/62 ≥ 0,80. Un blob quelconque « colle » à ~0,7, donc la forme seule ne prouve rien. **Abandon de la piste « forme » : non discriminante.** Piste restante : l'arrière-plan (grand lac, muraille orange, butte à tour blanche) est peut-être la vue depuis le site.
""")
L.append("## 2. Clairière : jonctions (tour d'Avalon, rayon 2,5 km)\n")
L.append("""Méthode : nœuds à ≥ 3 branches de `troncon_de_route` (Sentier/Chemin/Route empierrée). **Trouée** = hors forêt/bois (`zone_de_vegetation`), < 15 % de forêt à 20 m et ≥ 35 % entre 25 et 90 m. **Eau** = tronçon hydro « Ecoulement naturel » ≤ 150 m. **Public** = dans une `foret_publique` (proxy, pas le cadastre). **Vue** = ligne de vue terrain seul, tour +8 m vers point +1,7 m (RGE ALTI, sans végétation ni bâti). **Versant est** = pente ≥ 4 % et descente au cap 45–135°.
""")
L.append('**Test du hasard** (%d jonctions) :\n\n| Filtre | Passent | Part |\n|---|---|---|'%N)
for k,lab in (('trouee','trouée'),('eau','ruisseau ≤ 150 m'),('pub','forêt publique'),('vis','vue depuis la tour'),('est','versant est')): L.append('| %s | %d | %.1f %% |'%(lab,c(k),100*pr[k]))
L.append('\nCombinés : trouée+eau = 2 ; trouée+eau+vue = 2 ; eau+public+vue = 4 ; eau+vue+est = 1 ; **les 5 ensemble = 0**. Espérance par hasard (indépendance) ≈ %.4f. Avec des filtres aussi lâches (eau 46 %%, vue 26 %%), un candidat à 3 filtres n\'informe pas.\n'%exp)
L.append('**Top 10** (score = nb de filtres + bonus proximité − distance/10 km) :\n\n| # | Lat, Lon | Dist/cap | Nature | Filtres | Ruisseau (dist ; flux ; cap du ruisseau depuis la jonction) | Score |\n|---|---|---|---|---|---|---|')
for i,r in enumerate(top,1):
    L.append('| T%02d | %.5f, %.5f | %.0f m / %.0f° | %s | %s (%d/5) | %d m ; %s ; coule vers %.0f° ; ruisseau au %.0f° | %.2f |'%(i,r['lat'],r['lon'],r['d'],r['cap'],'/'.join(r['nat']),flt(r),n_ok(r),r['dh'],r.get('ruis_nom') or 'sans nom',r['flow_cap'],r['ruis_dir_depuis_jonction'],r['score']))
L.append("""
**Lecture.** T05 (45.41512, 6.02803, Ruisseau de la Perrière, 1,5 km au sud) est la seule vraie trouée avec ruisseau nommé du top, avec vue théorique marginale (dégagement 7 m) ; le ruisseau coule vers l'ONO (293°) et passe à 23 m. Son versant regarde l'ouest, pas l'est. T10 a un versant est net (44 %) mais hors trouée et sur l'Isère. T01–T04 sont en forêt publique avec vue théorique (le relief seul ; la forêt gênera). **Aucun n'est retenu.** La direction d'écoulement est celle du tronçon BD TOPO au point le plus proche (sens de saisie corrigé si « Sens inverse »).
""")
L.append("## 3. Toponymes (≤ 5,5 km ; distance et cap depuis la tour)\n\n| Terme | Toponyme | Dist | Cap | Source |\n|---|---|---|---|---|")
seen=set()
for r in tp:
    if 'nature, sans nom' in r['nom'] or r['d']>5.5 or 'école' in r['nom'].lower(): continue
    k=(r['terme'],r['nom'].lower())
    if k in seen: continue
    seen.add(k); L.append('| %s | %s | %.2f km | %.0f° | %s |'%(r['terme'],r['nom'],r['d'],r['cap'],r['src']))
L.append("""
Les ~52 « Fontaine » sans nom de `detail_hydrographique` ne sont pas listées : les plus proches sont à 0,91 km (166°), 0,92 km (204°), 1,11 km (358°), 1,15 km (87° et 264°). **Aucun** toponyme pour émeraude, diamant, ancre, étoile, lune, souche, charpentier, coupe, dame ; « Chante-Merle » (1,87 km, 59°) évoque « chant » ; « Le Cret du Mur » (2,56 km, 184°) et « Mollard Billard et les Murailles » (3,8 km, 132°) évoquent le rempart ; « Tire-Loup » (1,6 km, 98°) évoque le loup ; « Le Fayet » (4,55 km, 255°) n'a qu'une étymologie (hêtre), pas le sens de fée. Les noms « âne » sont des faux positifs (Granier, Buganière). **Test du hasard** : 3 067 noms dans 6,5 km ; « roche » ou « loup » y sont banals ; seul « Avalon » est indépendant (et déjà connu). Tire-Loup : HYPOTHÈSE faible.
""")
L.append("## 4. Alternative : fort Barraux (45.4358, 5.98723 ; ~3,5 km cap 283° de la tour)\n")
L.append("Rayon 1,5 km, 32 jonctions : trouée 0, eau 7, public 0, vue 5, versant est 5 ; eau+vue+est = 4. Meilleurs (aucun n'a la trouée) :\n\n| # | Lat, Lon | Dist du fort | Nature | Filtres | Flux |\n|---|---|---|---|---|---|")
for i,r in enumerate(topf[:4],1): L.append('| F%02d | %.5f, %.5f | %.0f m / %.0f° | %s | %s | ruisseau à %d m, coule vers %.0f° |'%(i,r['lat'],r['lon'],r['d'],r['cap'],'/'.join(r['nat']),flt(r),r['dh'],r['flow_cap']))
L.append("""
Les 4 premiers sont sur le versant est de la montagne à l'ouest du fort (descente vers l'est, ruisseau à quelques mètres, vue théorique sur le relief). Cohérent avec « l'astre du matin sur le ruisseau », mais sans trouée dans la BD TOPO et hors forêt publique dans les données. **Non retenu, piste vivante.** Le fort est un monument historique : c'est le chemin de rempart, pas le lieu du coffre.
""")
L.append("""## À vérifier sur place ou ensuite
- La vraie clairière peut être absente de la BD TOPO (trouée < 30 m, sous-bois) : contrôler l'orthophoto IGN ou le LiDAR HD (MNH) pour chaque candidat, T05 d'abord.
- Visibilité réelle depuis la tour : refaire avec le MNS LiDAR (végétation et bâti), pas le MNT.
- Chercher sur place un ruisseau qui coule à gauche jusqu'à une roche qui bloque le passage (absent de BD TOPO).
- Domaine public : vérifier au cadastre parcellaire (non fait ici).
- Le chemin de rempart précis : FAQ06-025 dit qu'il n'est pas l'un des chemins de la jonction, mais très proche.
- L'arrière-plan de l'enluminure 9 (lac, muraille orange crénelée, butte à tour blanche) : à comparer avec des panoramas de la vallée.
""")
L.append("## Fichiers\n`T1_candidats.kml`, `T1_bassin_planche.png`, `T1_bassin_trace_controle.png`, `T1_bassin_scores.json`, `T1_tour_jonctions.json`, `T1_fort_jonctions.json`, `T1_toponymes.json`, `T1_*.out.txt`, `T1_notes.md`.\n")
open(D+'T1_rapport.md','w',encoding='utf-8').write('\n'.join(L))
print(N,pr,exp)
