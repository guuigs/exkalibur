import re
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
items=faq()
Z={
'E9 honte/gloire/trahison':[r'jour de honte|jour de gloire|prix de la trahison|trahison|deniers|Judas|Marignan|Bayard|Colomb|Jacques C'],
'E8 tour/Lincoln/Avalon/Hugues':[r'Lincoln|Hugues|Payns|plus haute tour|Avalon|Dean|Bishop|Glastonbury'],
'E6 6C / figure / ligne 8':[r'sixième C|6e C|6 C|six C|dernier C|cinquième C|5e C|avant-dernier|figure visuelle|relier|reli[ée]s? une à une|ligne 8|Ligne huit'],
'E5 panneau / enlum 5':[r'enluminure (5|cinq)\b|enluminure 10|dixième enluminure|table ronde'],
'E2 alexandrie':[r'Alexandri|neuvième|mon dernier|Octave|Auguste|lauriers'],
'E7 juments/lance/rose/balance':[r'jument|balance|goutte de sang|lance|Sub rosa|SUBROSA'],
'E10 compte':[r'aïeux|cairn|Machrie|Fingal|Arran|gardienne de lumière|Eilean|Donan'],
'E11 angle/1f':[r"1f|π|\bpi\b|parfaitement|rayon|angle du dernier|lever du soleil|azimut|boussole|jour dernier"],
}
for z,ks in Z.items():
    print('\n=====',z); seen=set()
    for it in sorted(items,key=lambda x:x.get('ref','')):
        t=it.get('q','')+' '+str(it.get('a',''))
        if any(re.search(k,t,re.I) for k in ks):
            r=it.get('ref')
            if r in seen: continue
            seen.add(r)
            print(r,'|Q:',it['q'][:200].replace('\n',' '),'|A:',str(it['a'])[:240].replace('\n',' '))
