import sys,json,re
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
items=faq()
Z={
'E1':[r'lieue',r'11 lieues',r'Foix',r'Rennes-le-Ch',r'quillon',r'Couchant'],
'E2':[r'Alexandri',r'charade',r'neuvième',r'9e mot',r'TROIANOVA|Troia'],
'E5':[r'panneau',r'R5R|R3G|R5G',r'Winchester',r'décimale'],
'E6':[r'plateau',r'lettre.*C\b|6 C|six C|5e C|sixième C|cinquième C',r'Ligne 8|ligne 8|huit'],
'E7':[r'balance',r'jument',r'lance',r'\brose\b'],
'E8':[r'Tibère|numéro 1|numéro un',r'Lincoln',r'Hugues',r'pétale',r'Avalon'],
'JOURDER':[r'jour dernier',r'30 avril|1524|julien|grégorien|solstice|équinoxe'],
'E10':[r'compte-les|compter|Compte',r'Machrie|Arran|Fingal',r'\b1, ?3, ?5|chiffres?.*pierre'],
'E11':[r'angle',r'64|Montsalvage',r'1f|π|pi\b',r'dernier chevalier|Bayard']}
for z,ks in Z.items():
    print('\n=====',z)
    seen=set()
    for it in items:
        t=it.get('q','')+' '+str(it.get('a',''))
        if any(re.search(k,t,re.I) for k in ks):
            r=it.get('ref')
            if r in seen: continue
            seen.add(r)
            print(r,'|',it.get('theme'),'|Q:',it['q'][:220].replace('\n',' '),'|A:',str(it['a'])[:260].replace('\n',' '))
