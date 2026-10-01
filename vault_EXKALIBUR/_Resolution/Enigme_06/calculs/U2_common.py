"""U2 : listes de noms (preux, dieux, boissons), index de lieux en C (hash multiset), helpers numpy."""
import sys, os, json, pickle, random
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from T1_lib import norm, hword, HL, load_names, name_hash_sets
sys.stdout.reconfigure(encoding="utf-8")
HERE=os.path.dirname(os.path.abspath(__file__)); D=os.path.join(HERE,"U2data")
PREUX=['Hector','Alexandre','Alexander','Cesar','Caesar','Jules Cesar','Josue','Joshua','Josué','David','Judas Maccabee','Maccabee','Judas','Arthur','Charlemagne','Charles','Carolus','Godefroy','Godefroi','Godfrey','Bouillon','Godefroy de Bouillon','Roland','Lancelot','Gauvain','Perceval','Galaad']
NINE=['Hector','Alexandre','Cesar','Josue','David','Judas','Arthur','Charlemagne','Godefroy']
BACCH=['Bacchus','Dionysos','Dionysus','Liber','Liber Pater','Libera','Ceres','Silene','Silenus','Ganymede','Hebe','Soma','Sucellus','Dagda','Aegir','Osiris','Noe','Comus','Oenotria','Pan','Vin','Baccus','Bromios','Lyaeus','Evohe','Iacchus','Sabazios','Methe','Mead','Hydromel','Kvasir','Ninkasi','Hathor','Shiva','Hapi']
PLAN=['Lune','Mercure','Venus','Soleil','Mars','Jupiter','Saturne','Luna','Sol','Mercurius','Venus','Iuppiter','Saturnus','Moon','Mercury','Sun','Saturn','Dianus','Diane','Helios','Selene','Hermes','Aphrodite','Ares','Zeus','Cronos','Kronos','Apollon','Artemis']
DRINKS_CUR=['Cognac','Calvados','Chartreuse','Champagne','Cidre','Cervoise','Claret','Cassis','Chablis','Cahors','Cava','Cointreau','Chianti','Cointreau','Cachaca','Calisay','Cynar','Campari','Curacao','Cuba Libre','Cappuccino','Cafe','Chocolat','Chouchen','Chinon','Chambertin','Chateauneuf','Corton','Cremant','Cerveza','Cerveja','Cider','Cream','Cocktail','Coca','Cola','Coffee','Cocoa','Clairette','Cahors','Corbieres','Cotes','Cointreau','Caipirinha','Cosmopolitan','Cuvee','Cordial','Claret','Cask','Cuvée','Vin','Wine','Vino','Bière','Biere','Beer','Ale','Mead','Hydromel','Whisky','Whiskey','Gin','Rhum','Rum','Vodka','Eau','Lait','The','Tea','Sake','Porto','Port','Sherry','Xeres','Jerez','Rioja','Medoc','Bordeaux','Bourgogne','Sancerre','Sauternes','Armagnac','Pastis','Absinthe','Pommeau','Poire','Perry','Stout','Porter','Guinness','Jameson','Poitin','Poteen','Sangria','Tequila','Mojito','Pineau','Cahors','Muscadet','Banyuls','Madere','Madeira','Vinho','Verde','Ginjinha','Orujo','Anis','Licor','Aguardiente','Agua','Ponche','Txakoli','Cava','Sidra','Garnacha','Tempranillo','Albarino','Monastrell','Chartreux','Benedictine','Cluny']
def load_list(name):
    p=os.path.join(D,name+".json"); return json.load(open(p,encoding="utf-8")) if os.path.exists(p) else []
def places_hashes():
    p=os.path.join(D,"places.pkl")
    if os.path.exists(p): return pickle.load(open(p,"rb"))
    sets=load_names(); H={}
    for sn,d in sets.items():
        for n,disp in d.items():
            if len(n)>=4: H.setdefault(int(hword(n)),[]).append((n,disp[0],sn))
    pickle.dump(H,open(p,"wb")); return H
def hw(names,minlen=2):
    out={}
    for x in names:
        n=norm(x)
        if len(n)>=minlen: out.setdefault(n,x)
    return out
