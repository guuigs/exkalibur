"""Cherche les emprunts mot pour mot des 12 énigmes (+ intro) au Roman de la Rose, trad. Marteau, tome I (Gutenberg 16816).
Usage : python3 emprunts_rdlr.py <pg16816.txt> <"00 - Solutions validées.md">
Le texte Gutenberg complet se télécharge sur https://www.gutenberg.org/cache/epub/16816/pg16816.txt
Sortie : pour chaque énigme, les séquences de N mots (N=4 puis 6) présentes dans le livre, avec la ligne du livre."""
import re, sys, unicodedata, bisect
book_path, sol_path = sys.argv[1], sys.argv[2]
src = open(sol_path, encoding='utf-8').read()
enig = {}
for s in re.split(r'\n## ', src):
    m = re.match(r'(\d+)\. ', s)
    if m: enig[int(m.group(1))] = ' '.join(l[1:].strip() for l in s.split('\n') if l.startswith('>'))
def norm(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
    return re.findall(r"[a-z]+", s)
book = open(book_path, encoding='utf-8').read(); lines = book.split('\n')
pos = []; wc = 0
for l in lines: pos.append(wc); wc += len(norm(l))
bw = norm(book)
stop = set('de la le les et a en un une des du que qui il elle se ne pas son sa ses au aux par pour sur dans est etait l d n s j qu'.split())
for N in (4, 6):
    idx = {}
    for i in range(len(bw) - N): idx.setdefault(tuple(bw[i:i+N]), []).append(i)
    print('=== N = %d mots' % N)
    for k in sorted(enig):
        w = norm(enig[k]); hits = []
        for i in range(len(w) - N):
            g = tuple(w[i:i+N])
            if sum(1 for x in g if x not in stop) < 2: continue
            if g in idx: hits.append((' '.join(g), len(idx[g]), bisect.bisect_right(pos, idx[g][0])))
        print('É%d' % k, hits)
