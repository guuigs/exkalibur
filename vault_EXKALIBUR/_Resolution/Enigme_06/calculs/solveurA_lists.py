import unicodedata,json,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
def norm(s):
    s=unicodedata.normalize('NFD',s.upper()).replace('Œ','OE').replace('Æ','AE')
    return ''.join(c for c in s if 'A'<=c<='Z')
def key(s): return ''.join(sorted(norm(s)))
# ---- lieux commençant par C (communes FR + geonames cities15000 avec noms alternatifs)
places={}
for n,lat,lon,pop in json.load(open('communes.json',encoding='utf-8')):
    if norm(n)[:1]=='C': places.setdefault(norm(n),(n,'FR',pop))
for line in open('cities15000.txt',encoding='utf-8'):
    f=line.split('\t')
    cands=[f[1],f[2]]+f[3].split(',')
    for a in cands:
        if a and norm(a)[:1]=='C' and len(norm(a))>=4 and a.isascii()==False or (a and norm(a)[:1]=='C' and len(norm(a))>=4):
            k=norm(a)
            if k not in places: places[k]=(a,f[8],int(f[14] or 0))
curated=['Cluny','Clermont','Clermont-Ferrand','Cadouin','Conques','Citeaux','Clairvaux','Chartres','Compostelle','Canterbury','Cantorbery','Constantinople','Cesaree','Chypre','Carcassonne','Cambrai','Corbie','Cordoue','Cologne','Chinon','Camelot','Carduel','Caerleon','Carlisle','Cardiff','Colchester','Chichester','Chester','Cambridge','Crecy','Carnac','Chalon','Cahors','Compiegne','Cornouailles','Cornwall','Caen','Cadbury','Camlann','Camlan','Cuenca','Coimbra','Cordoba','Calatrava','Cesarea','Clairmont','Clermont','Cerdagne','Cerdanya','Castelnaudary','Chateaudun','Chastel','Celestine','Cyprus','Chalcedoine','Cesar','Charlemagne','Cambridge','Carthage','Corinthe','Crete','Cythere','Cydnus','Canterbury','Camelford','Cirencester','Caistor','Calais','Colombey','Chaource','Chaumont','Cite','Cerne','Chalice','Cornwall','Chepstow','Caerwent','Caerphilly','Carmarthen','Conwy','Caernarfon','Carreg','Cheddar','Cadiz','Cartagena','Ceuta','Cairo','Caire','Cesenatico','Capharnaum','Calvaire','Canaan','Cana','Carmel','Cedron','Cenacle']
for c in curated: places.setdefault(norm(c),(c,'CUR',0))
print(len(places),'lieux en C')
byk=collections.defaultdict(list)
for k,(n,cc,p) in places.items(): byk[''.join(sorted(k))].append((n,cc,p))
# ---- noms de personnages/dieux
LISTS={
'preux':['Hector','Alexandre','Cesar','Josue','David','Judas Maccabee','Judas Macchabee','Maccabee','Arthur','Charlemagne','Godefroy de Bouillon','Godefroy','Bouillon','Godefroi'],
'grec':['Zeus','Hera','Poseidon','Demeter','Hestia','Hades','Athena','Apollon','Artemis','Ares','Aphrodite','Hephaistos','Hermes','Dionysos','Cronos','Kronos','Rhea','Ouranos','Uranus','Gaia','Gea','Pan','Eros','Nyx','Erebe','Chaos','Thanatos','Hypnos','Hecate','Persephone','Helios','Selene','Eos','Atlas','Prometheus','Nemesis','Tyche','Iris','Hebe','Eole','Triton','Nereus','Thetis','Titan','Oceanos','Ocean','Themis','Mnemosyne','Phoebe','Cybele','Asclepios','Heracles','Herakles','Hercule','Perseus','Orion','Caelus','Coeus','Crios','Hyperion','Japet','Iapetos','Thea','Tethys','Cerbere','Charon','Cerberus','Chiron','Circe','Calypso','Castor','Pollux','Cassandre','Clio','Calliope','Cyclope'],
'romain':['Jupiter','Junon','Neptune','Ceres','Vesta','Pluton','Minerve','Apollon','Diane','Mars','Venus','Vulcain','Mercure','Bacchus','Saturne','Ops','Uranus','Caelus','Coelus','Terra','Tellus','Janus','Faune','Flore','Aurore','Sol','Luna','Lune','Soleil','Cupidon','Amour','Psyche','Fortuna','Victoria','Bellone','Proserpine','Hercule','Quirinus','Silvain','Cybele','Vertumne','Pomone','Libitina','Dispater','Dis Pater','Iuppiter','Iovis','Diespiter','Juppiter','Ceres','Comus','Consus','Carmenta','Cardea','Concordia'],
'nordique':['Odin','Thor','Loki','Freya','Freyja','Frigg','Tyr','Baldr','Balder','Heimdall','Njord','Frey','Freyr','Bragi','Idunn','Sif','Hel','Ymir','Vidar','Vali','Ull','Forseti','Hod','Skadi','Aegir','Ran','Jord','Mani','Sol','Fenrir','Odhin','Wotan','Woden','Donar','Wodan','Tiw','Frige'],
'egypte':['Ra','Re','Amon','Amon-Ra','Osiris','Isis','Horus','Seth','Set','Anubis','Thot','Thoth','Hathor','Bastet','Sekhmet','Ptah','Nout','Geb','Shou','Tefnout','Nephtys','Sobek','Apis','Aton','Atoum','Maat','Khnoum','Khonsou','Min','Bes'],
'celte':['Lug','Lugh','Taranis','Teutates','Esus','Belenos','Cernunnos','Epona','Ogmios','Dagda','Brigit','Morrigan','Nuada','Danu','Lir','Manannan','Cernunos','Sucellus','Nantosuelta','Rosmerta','Camulos','Toutatis','Belisama','Maponos','Grannus','Sirona','Nodens','Ceridwen','Arawn','Rhiannon','Bran','Cocidius','Cathubodua','Coventina'],
'planetes':['Soleil','Lune','Mars','Mercure','Jupiter','Venus','Saturne','Uranus','Neptune','Pluton','Terre'],
'jours':['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'],
'jours_lat':['Dies Lunae','Dies Martis','Dies Mercurii','Dies Iovis','Dies Veneris','Dies Saturni','Dies Solis'],
'zodiaque':['Belier','Taureau','Gemeaux','Cancer','Lion','Vierge','Balance','Scorpion','Sagittaire','Capricorne','Verseau','Poissons'],
'templiers':['Hugues de Payns','Payens','Godefroi de Saint-Omer','Bernard de Clairvaux','Jacques de Molay','Molay','Templier','Temple','Hospitaliers','Baudouin','Urbain','Urbain II','Eudes de Chatillon','Pierre lErmite','Raymond de Saint-Gilles','Bohemond','Tancrede','Godefroy'],
'saintpere':['Pater Noster','Notre Pere','Pere','Cieux','Ciel','Caelum','Pater','Libera nos a malo','Amen'],
}
