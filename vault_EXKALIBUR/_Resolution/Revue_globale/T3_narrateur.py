import re
exec(open(r'C:/Users/Admin/AppData/Local/hermes/cache/scratch/exk_e12/exk.py',encoding='utf-8').read())
items=faq()
N=[it for it in items if 'NARRATEUR' in str(it.get('theme','')).upper()]
M=[it for it in items if it not in N and re.search(r'narrateur|narratrice',it.get('q','')+str(it.get('a','')),re.I)]
print('theme NARRATEUR:',len(N),'| autres items mentionnant narrateur:',len(M))
seen=set()
def show(L):
    for it in sorted(L,key=lambda x:x.get('ref','')):
        r=it.get('ref')
        if r in seen: continue
        seen.add(r)
        print(r,'|Q:',it['q'][:230].replace('\n',' '),'|A:',str(it['a'])[:300].replace('\n',' '))
print('##### THEME #NARRATEUR'); show(N)
print('\n##### AUTRES (mention narrateur)'); show(M)
