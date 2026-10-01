import re, html, json, subprocess, sys, os
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
def fetch(term):
    url = "https://faq.unsolvedhunts.com/?chasse=exkalibur&search=" + term.replace(' ', '+')
    r = subprocess.run(["curl", "-s", "-m", "60", "-A", UA, "-G", "--data-urlencode", "chasse=exkalibur",
                        "--data-urlencode", "search=" + term, "https://faq.unsolvedhunts.com/"],
                       capture_output=True)
    return r.stdout.decode("utf-8", "ignore")
def clean(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', s or ''))).strip()
def parse(t):
    items = []
    blocks = re.split(r'<div class="result-item"', t)
    for b in blocks[1:]:
        ref = re.search(r'id="result-(FAQ\d+-\d+)"', b)
        if not ref: continue
        theme = re.search(r'class="thematique">(.*?)</span>', b, re.S)
        q = re.search(r'<strong>\s*Question\s*:?\s*</strong>(.*?)</p>', b, re.S | re.I)
        a = re.search(r'<strong>\s*R[ée]ponse\s*:?\s*</strong>(.*?)</p>', b, re.S | re.I)
        items.append({"ref": ref.group(1), "theme": clean(theme.group(1) if theme else ''),
                      "q": clean(q.group(1) if q else ''), "a": clean(a.group(1) if a else '')})
    return items
if __name__ == "__main__":
    allitems = {}
    terms = sys.argv[1:]
    for term in terms:
        t = fetch(term)
        n = 0
        for it in parse(t):
            if it['ref'] not in allitems:
                allitems[it['ref']] = it
                n += 1
        print(f"{term!r}: page={len(t)} nouveaux={n} total={len(allitems)}", file=sys.stderr)
    out = "faq_exkalibur.json"
    if os.path.exists(out):
        old = json.load(open(out, encoding='utf-8'))
        old.update(allitems); allitems = old
    json.dump(allitems, open(out, "w", encoding='utf-8'), ensure_ascii=False, indent=1)
    print("TOTAL", len(allitems))
    from collections import Counter
    c = Counter(k.split('-')[0] for k in allitems)
    print(sorted(c.items()))
