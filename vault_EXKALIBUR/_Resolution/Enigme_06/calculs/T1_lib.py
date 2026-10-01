"""T1 lib : plateau (24 pts), parcours, phrases, index de noms en C (hash multiset additif)."""
import sys, json, re, zipfile, unicodedata, itertools, os
import numpy as np
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "T1data")

def norm(s, fold=False):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).upper()
    s = re.sub(r"[^A-Z]", "", s.replace("Œ", "OE").replace("Æ", "AE"))
    if fold: s = s.replace("J", "I").replace("V", "U").replace("W", "U")
    return s

# ---------- plateau ----------
def ring_pt(r, k):
    a, b = r, 6 - r
    return [(a, a), (3, a), (b, a), (b, 3), (b, b), (3, b), (a, b), (a, 3)][k]
CELLS = [ring_pt(r, k) for r in range(3) for k in range(8)]  # idx = 8*r + k
IDX = {c: i for i, c in enumerate(CELLS)}
RED = [(3,0),(1,3),(1,5),(3,5),(0,6),(3,6),(4,3)]
BLUE_ILL = [(0,0),(6,0),(1,1)]
BLUE_PLAIN = [(3,1),(4,2),(5,3),(5,5)]
def board_masks(red=RED, bill=BLUE_ILL, bpl=BLUE_PLAIN):
    R = np.zeros(24, np.int64); Bi = np.zeros(24, np.int64); Bp = np.zeros(24, np.int64)
    for c in red: R[IDX[c]] = 1
    for c in bill: Bi[IDX[c]] = 1
    for c in bpl: Bp[IDX[c]] = 1
    return R, Bi, Bp
def subsets(R, Bi, Bp):
    """retourne dict nom -> (masque 24, nbS, nbT) ; S rouge hors plateau, T bleu hors plateau"""
    B = Bi + Bp; E = 1 - R - B
    base = {"R": R, "B": B, "RB": R + B, "E": E, "RE": R + E, "BE": B + E, "Bill": Bi, "Bpl": Bp, "RBpl": R + Bp, "Rbill": R + Bi}
    out = {}
    for n, m in base.items():
        for s, t in [(0,0),(1,0),(0,1),(1,1)]:
            out[f"{n}" + ("+S" if s else "") + ("+T" if t else "")] = (m, s, t)
    return out

# ---------- parcours ----------
def all_traversals():
    T = {}
    # lignes / colonnes
    for axis in (0, 1):
        for lo in (0, 1):
            for io in (0, 1):
                for bou in (0, 1):
                    order = []
                    ys = sorted({c[1 - axis] for c in CELLS}, reverse=bool(lo))
                    for li, y in enumerate(ys):
                        line = sorted([i for i, c in enumerate(CELLS) if c[1 - axis] == y], key=lambda i: CELLS[i][axis])
                        d = io ^ (li % 2 if bou else 0)
                        if d: line = line[::-1]
                        order += line
                    T[f"{'ligne' if axis==0 else 'col'}_l{lo}_i{io}_b{bou}"] = order
    # anneaux (même départ)
    for rev_rings in (0, 1):
        rings = [0, 1, 2][::-1] if rev_rings else [0, 1, 2]
        for mode in ("cw", "ccw", "alt_cw", "alt_ccw"):
            for s in range(8):
                order = []
                for j, r in enumerate(rings):
                    d = 1 if mode.endswith("cw") and not mode.endswith("ccw") else -1
                    if mode.startswith("alt") and j % 2: d = -d
                    order += [8 * r + (s + d * m) % 8 for m in range(8)]
                T[f"anneau_{'int-ext' if rev_rings else 'ext-int'}_{mode}_s{s}"] = order
    # rayons
    for rev in (0, 1):
        for mode in ("ei", "ie", "alt"):
            for s in range(8):
                order = []
                for m in range(8):
                    k = (s + (-m if rev else m)) % 8
                    rr = [0, 1, 2] if mode == "ei" else [2, 1, 0] if mode == "ie" else ([0, 1, 2] if m % 2 == 0 else [2, 1, 0])
                    order += [8 * r + k for r in rr]
                T[f"rayon_{'ccw' if rev else 'cw'}_{mode}_s{s}"] = order
    # spirale "réelle" : anneau ext cw, puis le suivant démarre au point suivant, etc.
    for d in (1, -1):
        for s in range(8):
            for rev_rings in (0, 1):
                rings = [2, 1, 0] if rev_rings else [0, 1, 2]
                order = []; cur = s
                for r in rings:
                    order += [8 * r + (cur + d * m) % 8 for m in range(8)]
                    cur = (cur + d * 8) % 8  # revient au départ : même index ; variantes ci-dessous
                T[f"spirale_d{d}_s{s}_r{rev_rings}"] = order
    # sens inverse de chacun
    T.update({k + "_REV": v[::-1] for k, v in list(T.items())})
    return T
def tier2_traversals():
    """anneaux : départ+sens indépendants par anneau ; ordre des anneaux ext-int / int-ext"""
    out = []
    for rings in ([0, 1, 2], [2, 1, 0]):
        for cfg in itertools.product(range(16), repeat=3):
            order = []
            for r, c in zip(rings, cfg):
                s, d = c % 8, (1 if c < 8 else -1)
                order += [8 * r + (s + d * m) % 8 for m in range(8)]
            out.append(order)
    return out

def order_to_pos(orders):
    """orders: liste de listes (ordre de visite). retourne P[t, cell] = position de la cellule dans le parcours"""
    P = np.zeros((len(orders), 24), np.int64)
    for t, o in enumerate(orders):
        assert sorted(o) == list(range(24)), t
        for p, c in enumerate(o): P[t, c] = p
    return P

# ---------- hash multiset ----------
rng = np.random.default_rng(20260930)
HL = rng.integers(-2**62, 2**62, size=26, dtype=np.int64)
def hword(w):
    h = np.int64(0)
    for ch in w: h = h + HL[ord(ch) - 65]
    return h
def hletters(arr):  # arr = str -> np array of hashes
    return np.array([HL[ord(c) - 65] for c in arr], np.int64)

# ---------- noms ----------
def load_names():
    """retourne dict set_name -> dict norm -> [display,...] (uniquement noms commençant par C)"""
    sets = {"curated": {}, "communes": {}, "geo_big": {}, "geo_all": {}, "latin": {}}
    def add(s, disp):
        n = norm(disp)
        if len(n) >= 3 and n[0] == "C":
            sets[s].setdefault(n, []).append(disp)
    cj = json.load(open(os.path.join(HERE, "solveurB_C_coords.json"), encoding="utf-8"))
    for k in cj: add("curated", k)
    for c in json.load(open(os.path.join(DATA, "communes.json"), encoding="utf-8")):
        add("communes", c["nom"])
    LAT = ["Cluniacum","Cistercium","Claravallis","Carnutum","Compendium","Cantuaria","Camelot","Camulodunum","Corinium","Cadomum",
           "Caesarea","Constantinopolis","Colonia","Corduba","Compostella","Carcassio","Cabillonum","Cenomanum","Cameracum","Caletum",
           "Carnacum","Clarus Mons","Claromontensis","Cadurcum","Conchae","Cadunium","Cormaricum","Canossa","Cassinum","Corbeia",
           "Carlisle","Carduel","Caerleon","Caerleon-on-Usk","Camlann","Cornubia","Cambria","Cantium","Calagurris","Caledonia",
           "Compostela","Cabo","Cabo Finisterre","Coimbra","Conimbriga","Calatrava","Covadonga","Castella","Cataluña","Cadiz","Carthago"]
    for x in LAT: add("latin", x)
    for cc in ["GB", "IE", "ES", "PT", "AD", "FR"]:
        z = zipfile.ZipFile(os.path.join(DATA, cc + ".zip"))
        with z.open(cc + ".txt") as f:
            for line in f:
                p = line.decode("utf-8").split("\t")
                fc, fcode, pop = p[6], p[7], int(p[14] or 0)
                ok_all = fc == "P" or (fc == "S" and fcode in ("ABBY","CSTL","CTHDRL","CH","MSTY","PRY","MNMT","HSTS","TMPL","CVNT","CHNT"))
                if not ok_all: continue
                for nm in {p[1], p[2]}:
                    add("geo_all", nm)
                    if pop >= 2000 and cc != "FR": add("geo_big", nm)
                    if pop >= 2000 and cc == "FR": add("geo_big", nm)
    return sets
def name_hash_sets(sets, minlen=4, fold=False):
    out = {}
    for sn, d in sets.items():
        H = {}
        for n, disp in d.items():
            nn = norm(n, fold) if fold else n
            if len(nn) < minlen: continue
            H.setdefault(int(hword(nn)), []).append((nn, disp[0]))
        out[sn] = H
    return out
