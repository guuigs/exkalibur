"""Solveur B / É6 — géocodage de la liste LARGE de lieux en C (Wikipedia en, API MediaWiki, coordonnées primaires).
Sortie : solveurB_C_coords.json {nom_affiché: [lat, lon, titre_wikipedia, thème]} + solveurB_03_liste_C.out.txt"""
import sys, json; sys.path.insert(0, "."); from solveurB_geo import *
# (nom affiché, titre Wikipedia en, thème)
L = [
 # --- déjà vus dans la chasse / carte de Guilhem (coord. carte Guilhem prioritaires, voir plus bas)
 ("Carnac", "Carnac", "chasse É5"), ("Clermont", "Clermont-Ferrand Cathedral", "Urbain II 1095"), ("Cluny", "Cluny Abbey", "Urbain II"),
 ("Cadouin", "Cadouin Abbey", "Suaire, croisade"),
 # --- ordres religieux / croisade / Templiers
 ("Cîteaux", "Cîteaux Abbey", "cistercien"), ("Clairvaux", "Clairvaux Abbey", "Bernard, Templiers"),
 ("Chartres", "Chartres Cathedral", "voile de la Vierge"), ("Conques", "Conques Abbey", "Ste Foy, pèlerinage"),
 ("Cahors", "Cahors Cathedral", "cathédrale"), ("Carcassonne", "Carcassonne", "cité, Templiers"),
 ("Caen", "Abbaye aux Hommes", "Guillaume le Conquérant"), ("Chinon", "Château de Chinon", "Templiers, Plantagenêt"),
 ("Cambrai", "Cambrai Cathedral", "cathédrale"), ("Châlons-en-Champagne", "Châlons-en-Champagne", "Champagne"),
 ("Charroux", "Charroux Abbey", "abbaye"), ("Compiègne", "Compiègne", "roi"), ("Corbie", "Corbie Abbey", "abbaye"),
 ("Combourg", "Combourg", "Bretagne"), ("Cognac", "Cognac, Charente", "Charente"), ("Coutances", "Coutances Cathedral", "cathédrale"),
 ("Cherbourg", "Cherbourg-en-Cotentin", "port"), ("Clisson", "Clisson", "château"), ("Cerisy", "Cerisy Abbey", "abbaye normande"),
 ("Chalon-sur-Saône", "Chalon-sur-Saône", "ville"), ("Château-Gaillard", "Château Gaillard", "château"),
 ("Chauvigny", "Chauvigny", "château"), ("Cléry-Saint-André", "Cléry-Saint-André", "basilique"), ("Chambord", "Château de Chambord", "château"),
 ("Cassel", "Cassel, Nord", "bataille"), ("Crécy", "Crécy-en-Ponthieu", "champ de bataille"), ("Compostelle", "Santiago de Compostela Cathedral", "pèlerinage"),
 ("Clunia", "Clunia", "site"), ("Chaumont", "Chaumont, Haute-Marne", "ville"), ("Clamecy", "Clamecy, Nièvre", "ville"),
 ("Chambéry", "Chambéry", "ville"), ("Clermont-en-Beauvaisis", "Clermont, Oise", "homonyme Clermont"),
 ("Colmar", "Colmar", "ville"), ("Chalon", "Chalon-sur-Saône", "doublon"), ("Chenonceau", "Château de Chenonceau", "château"),
 ("Cluses", "Cluses", "ville"), ("Cîteaux-Vougeot", "Clos de Vougeot", "cistercien"), ("Cormery", "Cormery", "abbaye"),
 ("Cassis", "Cassis", "ville"), ("Cannes", "Cannes", "ville"), ("Calais", "Calais", "port"), ("Cambrai2", "Cambrai", "ville"),
 ("Chelles", "Chelles, Seine-et-Marne", "Sainte-Bathilde"), ("Choisy", "Choisy-le-Roi", "banlieue Paris"), ("Créteil", "Créteil", "banlieue Paris"),
 ("Clichy", "Clichy, Hauts-de-Seine", "banlieue Paris"), ("Courbevoie", "Courbevoie", "banlieue Paris"), ("Chantilly", "Chantilly, Oise", "château"),
 ("Clairefontaine", "Clairefontaine-en-Yvelines", "village"), ("Cergy", "Cergy", "ville"), ("Chevreuse", "Chevreuse", "château"),
 ("Chaource", "Chaource", "Sépulcre (mise au tombeau)"), ("Champmol", "Chartreuse de Champmol", "chartreuse"), ("Chartreuse", "Grande Chartreuse", "Chartreux"),
 ("Cambremer", "Cambremer", "village"), ("Cerisy-la-Salle", "Cerisy-la-Salle", "village"), ("Cabourg", "Cabourg", "plage"),
 ("Carentan", "Carentan-les-Marais", "ville"), ("Condé-sur-Noireau", "Condé-en-Normandie", "ville"),
 # --- Angleterre / pays de Galles / Écosse
 ("Canterbury", "Canterbury Cathedral", "Becket"), ("Caerleon", "Caerleon", "Arthur, Camelot gallois"), ("Cadbury Castle (Camelot)", "Cadbury Castle, Somerset", "Camelot"),
 ("Carlisle", "Carlisle Cathedral", "Carduel arthurien"), ("Colchester", "Colchester Castle", "Camulodunum"), ("Chester", "Chester Cathedral", "Deva"),
 ("Chichester", "Chichester Cathedral", "cathédrale"), ("Cambridge", "Cambridge", "ville"), ("Camelford (Camlann)", "Camelford", "Camlann"),
 ("Caernarfon", "Caernarfon Castle", "château"), ("Conwy", "Conwy Castle", "château"), ("Corfe", "Corfe Castle", "château"),
 ("Cardiff", "Cardiff Castle", "château"), ("Carmarthen", "Carmarthen", "Myrddin/Merlin"), ("Chepstow", "Chepstow Castle", "Normands"),
 ("Cressing Temple", "Cressing Temple", "Templiers"), ("Canterbury St Augustine", "St Augustine's Abbey", "abbaye"),
 ("Castle Rising", "Castle Rising", "château"), ("Caister", "Caister Castle", "château"), ("Chelmsford", "Chelmsford", "ville"),
 ("Cirencester", "Cirencester", "Corinium"), ("Carisbrooke", "Carisbrooke Castle", "château"), ("Carew", "Carew Castle", "château"),
 ("Cerne Abbas", "Cerne Abbas", "géant"), ("Colchester2", "Colchester", "ville"), ("Chatham", "Chatham, Kent", "ville"),
 ("Camber Castle", "Camber Castle", "château"), ("Chertsey", "Chertsey Abbey", "abbaye"), ("Cranbrook", "Cranbrook, Kent", "ville"),
 ("Canterbury (ville)", "Canterbury", "ville"), ("Crowborough", "Crowborough", "ville"), ("Crawley", "Crawley", "ville"),
 ("Croydon", "Croydon", "banlieue Londres"), ("Cheam", "Cheam", "banlieue Londres"), ("Chertsey2", "Chertsey", "ville"),
 ("Camlann", "Battle of Camlann", "bataille arthurienne"), ("Caldicot", "Caldicot Castle", "château"),
 # --- Europe / Orient
 ("Cologne", "Cologne Cathedral", "Rois mages"), ("Constantinople (Sainte-Sophie)", "Hagia Sophia", "croisade"), ("Cordoue", "Mosque–Cathedral of Córdoba", "Espagne"),
 ("Cuenca", "Cuenca, Spain", "Espagne"), ("Covadonga", "Covadonga", "Reconquista"), ("Calatrava", "Calatrava la Vieja", "ordre militaire"),
 ("Cassino", "Monte Cassino", "abbaye"), ("Canossa", "Canossa Castle", "Grégoire VII"), ("Cefalù", "Cefalù Cathedral", "Normands"),
 ("Caesarea", "Caesarea Maritima", "croisade"), ("Cairo", "Cairo", "Égypte"), ("Clunia2", "Clunia", "doublon"),
 ("Cadix", "Cádiz", "Espagne"), ("Ceuta", "Ceuta", "Espagne"), ("Copenhague", "Copenhagen", "Danemark"),
 ("Cambrai/Compiègne", "Compiègne", "doublon"),
]
names = {}
for n, t, th in L:
    if t in [v[1] for v in names.values()]: continue   # dédoublonnage par titre
    names[n] = (t, th)
fr = wiki_coords(sorted({t for t, _ in names.values()}), "en")
out = {}; miss = []
for n, (t, th) in names.items():
    v = fr[t]
    if v: out[n] = [v[0], v[1], v[2], th]
    else: miss.append((n, t))
# coordonnées de la carte de Guilhem (prioritaires pour les 3 C du joueur)
GUIL = {"Clermont": (45.7787583, 3.0858573), "Cluny": (46.4348054, 4.6585012), "Cadouin": (44.8114955, 0.8737598)}
for n, (la, lo) in GUIL.items():
    if n in out: out[n][0], out[n][1] = la, lo; out[n][2] += " [coord carte Guilhem]"
# Carnac : alignements du Ménec (carte Guilhem) = -3.0835991, 47.5918383
out["Carnac"] = [47.5918383, -3.0835991, "Alignements du Ménec [carte Guilhem]", "chasse É5"]
json.dump(out, open("solveurB_C_coords.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(f"{len(out)} lieux géocodés ; manquants ({len(miss)}) : {miss}")
for n, v in out.items(): print(f"{n:32s} {v[0]:9.4f} {v[1]:9.4f}  {v[2]}")
