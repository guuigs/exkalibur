"""Helper de recherche web de secours (web_search casse, ddg.py HTML casse).
Tente plusieurs moteurs en HTML simple + l'API Wikipedia francaise.
usage: python 00_websearch.py s "requete"   |   python 00_websearch.py f URL   |   python 00_websearch.py w "titre wiki"
"""
import sys, re, html, json, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
      "Accept-Language": "fr-FR,fr;q=0.9,en;q=0.8"}

def get(url, data=None, timeout=25):
    req = urllib.request.Request(url, data=data, headers=UA)
    return urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8", "ignore")

def strip(t):
    t = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", t)
    t = re.sub(r"(?s)<br\s*/?>|</p>|</div>|</li>|</h\d>|</tr>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    t = re.sub(r"[ \t]+", " ", t)
    return re.sub(r"\n\s*\n+", "\n", t).strip()

def searx_like(q):
    """lite.duckduckgo.com (POST) puis bing puis mojeek : renvoient des liens en clair."""
    out = []
    try:
        t = get("https://lite.duckduckgo.com/lite/", urllib.parse.urlencode({"q": q}).encode())
        for m in re.finditer(r'<a[^>]+class="result-link"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
            out.append((strip(m.group(2)), html.unescape(m.group(1)), ""))
        for m in re.finditer(r'<td[^>]*class="result-snippet"[^>]*>(.*?)</td>', t, re.S):
            if out and len(out) - 1 < 50:
                pass
        sn = [strip(m.group(1)) for m in re.finditer(r'class="result-snippet"[^>]*>(.*?)</td>', t, re.S)]
        out = [(a, b, sn[i] if i < len(sn) else "") for i, (a, b, _) in enumerate(out)]
    except Exception as e:
        print("  [lite.ddg ERR]", e)
    if out:
        return out
    try:
        t = get("https://www.bing.com/search?q=" + urllib.parse.quote(q) + "&setlang=fr")
        for m in re.finditer(r'<li class="b_algo".*?<h2><a[^>]+href="([^"]+)"[^>]*>(.*?)</a></h2>(.*?)</li>', t, re.S):
            out.append((strip(m.group(2)), html.unescape(m.group(1)), strip(m.group(3))[:250]))
    except Exception as e:
        print("  [bing ERR]", e)
    if out:
        return out
    try:
        t = get("https://www.mojeek.com/search?q=" + urllib.parse.quote(q))
        for m in re.finditer(r'<a class="ob"[^>]+href="([^"]+)"[^>]*>(.*?)</a>.*?<p class="s">(.*?)</p>', t, re.S):
            out.append((strip(m.group(2)), html.unescape(m.group(1)), strip(m.group(3))[:250]))
    except Exception as e:
        print("  [mojeek ERR]", e)
    return out

def wiki(title, lang="fr"):
    u = f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&format=json&redirects=1&titles=" + urllib.parse.quote(title)
    d = json.loads(get(u))
    for pid, pg in d["query"]["pages"].items():
        return pg.get("title", "?"), pg.get("extract", "")
    return "?", ""

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if sys.argv[1] == "s":
        for q in sys.argv[2:]:
            print("=== " + q)
            for t, u, s in searx_like(q)[:8]:
                print(f"- {t}\n  {u}\n  {s[:300]}")
    elif sys.argv[1] == "f":
        for u in sys.argv[2:]:
            print("=== " + u)
            try:
                print(strip(get(u))[:6000])
            except Exception as e:
                print("ERR", e)
    elif sys.argv[1] == "w":
        for t in sys.argv[2:]:
            ti, ex = wiki(t)
            print(f"===== {ti} ({len(ex)} car.)")
            print(ex[:6000])
