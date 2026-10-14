"""Ligne de vue sol -> cible sur le MNS LiDAR 2 m (arbres et bâtiments compris).
visible(vlat, vlon, lats, lons, eye=1.7, th=1.7, near=6) renvoie un booléen par cible.
Données : dossier DEM (variable d'environnement) contenant dem2m.npy/json et mns2m.npy."""
import numpy as np, json, math, os
SP=os.environ.get('DEM', '.')
M=json.load(open(SP+'/dem2m.json')); DTM=np.load(SP+'/dem2m.npy').astype(float); MNS=np.load(SP+'/mns2m.npy').astype(float)
LA1,LO0,DLAT,DLON=M['LA1'],M['LO0'],M['DLAT'],M['DLON']
T=(45.428888,6.031015); KY=111132.0; KX=math.cos(math.radians(T[0]))*111320.0
def idx(lat,lon): return (LA1-lat)/DLAT-0.5,(lon-LO0)/DLON-0.5
def bil(Z,fi,fj):
    i0=np.clip(np.floor(fi).astype(int),0,Z.shape[0]-2); j0=np.clip(np.floor(fj).astype(int),0,Z.shape[1]-2); di=fi-i0; dj=fj-j0
    return Z[i0,j0]*(1-di)*(1-dj)+Z[i0+1,j0]*di*(1-dj)+Z[i0,j0+1]*(1-di)*dj+Z[i0+1,j0+1]*di*dj
def visible(vlat,vlon,tl,to,eye=1.7,th=1.7,near=6):
    """tl,to: arrays of target lat/lon. returns bool array"""
    zv=bil(DTM,*map(np.atleast_1d,idx(vlat,vlon)))[0]+eye
    dx=(to-vlon)*KX; dy=(tl-vlat)*KY; D=np.hypot(dx,dy)
    n=int(D.max()/2)+2; f=np.linspace(0,1,n)[None,:]
    la=vlat+dy[:,None]/KY*f; lo=vlon+dx[:,None]/KX*f; r=D[:,None]*f
    fi,fj=idx(la,lo); s=bil(MNS,fi,fj)-(0.87*r**2/12742000.0)
    zt=bil(DTM,*idx(tl,to))-(0.87*D**2/12742000.0)+th
    ang_t=(zt-zv)/D
    with np.errstate(divide='ignore',invalid='ignore'):
        a=(s-zv)/r
    mask=(r<near)|(r>D[:,None]-4)
    a[mask]=-np.inf
    return a.max(1)<=ang_t
