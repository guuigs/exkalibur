# Helper Discord LECTURE SEULE : recherche avec garde-fou de focus (jamais de frappe dans la zone de message).
# Usage dans browser_exec : exec(open(r"C:/Users/Admin/AppData/Local/hermes/cache/scratch/discord_search_safe.py", encoding="utf-8").read())
import time
def _focus_ok():
    # Le champ de recherche est lui aussi un éditeur Slate : on l'identifie par son label, et on exclut la zone de message.
    return js("""(() => { const a=document.activeElement; if(!a) return false;
      if(a.closest('[class*="channelTextArea"]')||a.closest('form')) return false;
      return a.getAttribute('role')==='combobox' && /Rechercher/i.test(a.getAttribute('aria-label')||''); })()""")
def _focus_search():
    # 1) focus JS direct (fiable quand la liste de résultats/suggestions est ouverte ; un clic peut atterrir sur un <li>)
    js("""(() => { const e=document.querySelector('[role="combobox"][aria-label*="Rechercher"]'); if(e && !e.closest('[class*="channelTextArea"]')) e.focus(); })()"""); time.sleep(0.3)
    if _focus_ok(): return True
    r = js("""(() => { const e=[...document.querySelectorAll('[role="combobox"], [aria-label]')].find(x=>/Rechercher/i.test(x.getAttribute('aria-label')||'') && !x.closest('[class*="channelTextArea"]')); if(!e) return null; const b=e.getBoundingClientRect(); return [b.x+b.width/2,b.y+b.height/2]; })()""")
    if not r: return False
    click_at_xy(r[0], r[1]); time.sleep(0.6)
    return _focus_ok()
def _key(k, code, vk, mod=0):
    cdp("Input.dispatchKeyEvent", type="keyDown", modifiers=mod, key=k, code=code, windowsVirtualKeyCode=vk)
    cdp("Input.dispatchKeyEvent", type="keyUp", modifiers=mod, key=k, code=code, windowsVirtualKeyCode=vk)
def composer_empty():
    t = js("""(() => { const e=document.querySelector('[class*="channelTextArea"] [role="textbox"]'); return e? e.innerText : ''; })()""") or ''
    return t.replace('\ufeff','').strip() == ''
def _search_text():
    t = (js("""(() => { const e=document.querySelector('[role="combobox"][aria-label*="Rechercher"]'); return e? e.innerText : ''; })()""") or '')
    t = t.replace('\ufeff','').replace('Rechercher Exkalibur','').strip()   # le placeholder fait partie du innerText
    return t
def _clear_search():
    # Ctrl+A ne sélectionne pas tout dans ce champ : on efface caractère par caractère (End puis Backspace), avec contrôle.
    for _ in range(6):
        n = len(_search_text())
        if n == 0: return True
        if not _focus_ok() and not _focus_search(): return False
        _key("End","End",35)
        for _ in range(n + 5): _key("Backspace","Backspace",8)
        time.sleep(0.3)
    return len(_search_text()) == 0
def srch(q, wait=6):
    if not composer_empty(): raise RuntimeError("Zone de message non vide : STOP")
    if not _focus_search(): return ["FOCUS_KO"]
    if not _clear_search(): return ["CLEAR_KO"]
    if not _focus_ok() and not _focus_search(): return ["FOCUS_PERDU"]
    cdp("Input.insertText", text=q); time.sleep(1.0)
    if _search_text() != q: return ["TEXTE_INATTENDU:" + _search_text()]
    if not composer_empty(): return ["COMPOSER_NON_VIDE"]
    if not _focus_ok() and not _focus_search(): return ["FOCUS_PERDU_AVANT_ENTREE"]
    _key("Enter","Enter",13)
    time.sleep(wait)
    js("""(() => document.querySelectorAll('[class*="spoilerContent"][aria-expanded="false"]').forEach(e=>e.click()))()"""); time.sleep(0.5)
    return js("""(() => [...document.querySelectorAll('[class*="searchResult"]')].map(e=>e.innerText.replace(/\\n+/g,' ⏎ ')))()""") or []
