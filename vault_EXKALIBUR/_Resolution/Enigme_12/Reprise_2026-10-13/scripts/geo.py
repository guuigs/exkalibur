from geographiclib.geodesic import Geodesic
G=Geodesic.WGS84
def inv(a,b):
    r=G.Inverse(a[0],a[1],b[0],b[1]); return r['s12']/1000, r['azi1']%360
def direct(a,az,km):
    r=G.Direct(a[0],a[1],az,km*1000); return (r['lat2'],r['lon2'])
def xtrack(a,az,p):
    # cross-track distance (km) and along-track of p wrt geodesic from a at az (approx, spherical)
    import math
    d,az2=inv(a,p); R=6371.0
    dx=math.asin(math.sin(d/R)*math.sin(math.radians(az2-az)))*R
    at=math.acos(max(-1,min(1,math.cos(d/R)/math.cos(dx/R))))*R
    return dx,at
