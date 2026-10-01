"""Bibliotheque geodesique + Web Mercator pour l'enigme 1 (Exkalibur).
Toutes les distances en km. R = 6371.0088 (orthodromie) et 6378137 (Web Mercator, EPSG:3857).
"""
import math

R_KM = 6371.0088
R_MERC = 6378137.0  # Web Mercator (Google My Maps)


def rad(d):
    return math.radians(d)


def deg(r):
    return math.degrees(r)


def vec(lat, lon):
    la, lo = rad(lat), rad(lon)
    return (math.cos(la) * math.cos(lo), math.cos(la) * math.sin(lo), math.sin(la))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def norm(a):
    n = math.sqrt(dot(a, a))
    return tuple(x / n for x in a)


def hav(p, q):
    """distance orthodromique (lat,lon) -> km"""
    p1, p2 = rad(p[0]), rad(q[0])
    dp, dl = p2 - p1, rad(q[1] - p[1])
    return 2 * R_KM * math.asin(math.sqrt(math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2))


def bearing(p, q):
    """cap initial (lat,lon)->(lat,lon), degres 0-360"""
    p1, p2 = rad(p[0]), rad(q[0])
    dl = rad(q[1] - p[1])
    return (deg(math.atan2(math.sin(dl) * math.cos(p2), math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl))) + 360) % 360


def dest(p, brg, d_km):
    """point a d_km de p au cap brg (orthodromie)"""
    d = d_km / R_KM
    p1, l1 = rad(p[0]), rad(p[1])
    b = rad(brg)
    p2 = math.asin(math.sin(p1) * math.cos(d) + math.cos(p1) * math.sin(d) * math.cos(b))
    l2 = l1 + math.atan2(math.sin(b) * math.sin(d) * math.cos(p1), math.cos(d) - math.sin(p1) * math.sin(p2))
    return (deg(p2), (deg(l2) + 540) % 360 - 180)


def interp_gc(p, q, f):
    """point a la fraction f (0..1) de l'arc orthodromique p->q (interpolation spherique)"""
    a, b = vec(*p), vec(*q)
    om = math.acos(max(-1, min(1, dot(a, b))))
    if om == 0:
        return p
    s = math.sin(om)
    v = tuple((math.sin((1 - f) * om) * x + math.sin(f * om) * y) / s for x, y in zip(a, b))
    return (deg(math.asin(v[2])), deg(math.atan2(v[1], v[0])))


def cross_track(p, a, b):
    """distance signee (km) de p au grand cercle a-b ; + = a gauche du sens a->b"""
    n = norm(cross(vec(*a), vec(*b)))
    return R_KM * math.asin(max(-1, min(1, dot(vec(*p), n))))


def along_track(p, a, b):
    """distance (km) le long de a->b du pied de p (projection orthogonale sur le grand cercle)"""
    n = norm(cross(vec(*a), vec(*b)))
    proj = norm(cross(n, cross(vec(*p), n)))
    if dot(proj, vec(*a)) < 0:
        proj = tuple(-x for x in proj)
    return R_KM * math.acos(max(-1, min(1, dot(vec(*a), proj))))


def gc_intersection(a1, a2, b1, b2):
    """intersection de 2 grands cercles (a1a2) et (b1b2) : renvoie les 2 points antipodaux"""
    n1, n2 = cross(vec(*a1), vec(*a2)), cross(vec(*b1), vec(*b2))
    x = cross(n1, n2)
    if math.sqrt(dot(x, x)) < 1e-12:
        return None
    x = norm(x)
    p = (deg(math.asin(x[2])), deg(math.atan2(x[1], x[0])))
    q = (-p[0], (p[1] + 360) % 360 - 180)
    return p, q


def vertex_gc(a, b):
    """vertex (point de latitude extreme) du grand cercle a-b, cote a->b"""
    n = norm(cross(vec(*a), vec(*b)))
    v = norm(cross(n, (0, 0, 1)))
    if dot(v, vec(*a)) < 0:
        v = tuple(-x for x in v)
    return (deg(math.asin(v[2])), deg(math.atan2(v[1], v[0])))


# ---------- Web Mercator (EPSG:3857), celle de Google My Maps ----------
def m(lat, lon):
    """(lat,lon) -> (x,y) Web Mercator en metres"""
    x = R_MERC * rad(lon)
    y = R_MERC * math.log(math.tan(math.pi / 4 + rad(lat) / 2))
    return (x, y)


def mi(x, y):
    """(x,y) Web Mercator -> (lat,lon)"""
    lon = deg(x / R_MERC)
    lat = deg(2 * math.atan(math.exp(y / R_MERC)) - math.pi / 2)
    return (lat, lon)


def merc_line_inter(p1, p2, q1, q2):
    """intersection de 2 droites tracees DROITES sur une carte Web Mercator"""
    (x1, y1), (x2, y2) = m(*p1), m(*p2)
    (x3, y3), (x4, y4) = m(*q1), m(*q2)
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(d) < 1e-9:
        return None
    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / d
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / d
    return mi(px, py)


def merc_interp(p, q, f):
    """point a la fraction f le long du segment DROIT sur une carte Web Mercator"""
    (x1, y1), (x2, y2) = m(*p), m(*q)
    return mi(x1 + f * (x2 - x1), y1 + f * (y2 - y1))


def merc_dist_ground(p, q):
    """distance 'au sol' estimee de la droite Mercator p-q : longueur du segment en metres equatoriaux * cos(lat moyen)"""
    (x1, y1), (x2, y2) = m(*p), m(*q)
    d = math.hypot(x2 - x1, y2 - y1)
    return d * math.cos(rad((p[0] + q[0]) / 2)) / 1000.0


def merc_cross_track(p, a, b):
    """distance (km, signee) de p a la droite Mercator a-b, ramenee au sol via cos(lat)"""
    (xa, ya), (xb, yb) = m(*a), m(*b)
    (xp, yp) = m(*p)
    num = (xb - xa) * (ya - yp) - (xa - xp) * (yb - ya)
    den = math.hypot(xb - xa, yb - ya)
    return (num / den) * math.cos(rad(p[0])) / 1000.0


def merc_bearing(p, q):
    """cap de la droite Mercator p->q (le cap du segment de carte)"""
    (x1, y1), (x2, y2) = m(*p), m(*q)
    return (deg(math.atan2(x2 - x1, y2 - y1)) + 360) % 360


def rhumb_dist(p, q):
    """distance loxodromique (a cap constant) km"""
    p1, p2 = rad(p[0]), rad(q[0])
    dl = rad(abs(q[1] - p[1]))
    dpsi = math.log(math.tan(math.pi / 4 + p2 / 2) / math.tan(math.pi / 4 + p1 / 2))
    if abs(dl) > math.pi:
        dl = 2 * math.pi - dl
    qm = math.cos(p1)
    dphi = p2 - p1
    return math.sqrt(dphi ** 2 + qm ** 2 * dl ** 2) * R_KM if False else R_KM * math.hypot(dphi, dpsi) if abs(dpsi) >= abs(dphi) or True else 0


def rhumb_dist2(p, q):
    p1, p2 = rad(p[0]), rad(q[0])
    dl = rad(q[1] - p[1])
    dpsi = math.log(math.tan(math.pi / 4 + p2 / 2) / math.tan(math.pi / 4 + p1 / 2))
    return R_KM * math.hypot(dl, dpsi)  # variante "plate carree en psi" (proche loxodrome)
