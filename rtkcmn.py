import sys
import numpy as np
from numpy import sin, cos, arctan2, arcsin, floor
from numpy.linalg import norm

gpst0 = [1980, 1, 6, 0, 0, 0]
ion_default = np.array([ # 2004/1/1
    [0.1118E-07,-0.7451E-08,-0.5961E-07, 0.1192E-06],
    [0.1167E+06,-0.2294E+06,-0.1311E+06, 0.1049E+07]])
# troposhere model
nmf_coef = np.array([
    [1.2769934E-3, 1.2683230E-3, 1.2465397E-3, 1.2196049E-3, 1.2045996E-3],
    [2.9153695E-3, 2.9152299E-3, 2.9288445E-3, 2.9022565E-3, 2.9024912E-3],
    [62.610505E-3, 62.837393E-3, 63.721774E-3, 63.824265E-3, 64.258455E-3],
    [0.0000000E-0, 1.2709626E-5, 2.6523662E-5, 3.4000452E-5, 4.1202191E-5],
    [0.0000000E-0, 2.1414979E-5, 3.0160779E-5, 7.2562722E-5, 11.723375E-5],
    [0.0000000E-0, 9.0128400E-5, 4.3497037E-5, 84.795348E-5, 170.37206E-5],
    [5.8021897E-4, 5.6794847E-4, 5.8118019E-4, 5.9727542E-4, 6.1641693E-4],
    [1.4275268E-3, 1.5138625E-3, 1.4572752E-3, 1.5007428E-3, 1.7599082E-3],
    [4.3472961E-2, 4.6729510E-2, 4.3908931E-2, 4.4626982E-2, 5.4736038E-2]])
nmf_aht = [2.53E-5, 5.49E-3, 1.14E-3] # height correction
gps_freq = {
    "L1": 1.57542e9,
    "L2": 1.22760e9,
    "L5": 1.17645e9,
}
dfreq_glo = [0.56250E6, 0.43750E6]  # L1, L2
glo_freq = {
    
}
gal_freq = {
    
}
bds2_freq = {
    
}
bds3_freq = {
    
}


class rCST():
    """ class for constants """
    PI = 3.1415926535898
    CLIGHT = 299792458.0
    MU_GPS = 3.9860050E14
    MU_GAL = 3.986004418E14
    MU_GLO = 3.9860044E14
    MU_CMP = 3.986004418E14
    # GME = 3.986004415E+14
    # GMS = 1.327124E+20
    # GMM = 4.902801E+12
    OMGE = 7.2921151467E-5
    OMGE_GAL = 7.2921151467E-5
    OMGE_GLO = 7.292115E-5
    OMGE_CMP = 7.292115E-5
    RE_WGS84 = 6378137.0
    # RE_GLO = 6378136.0
    FE_WGS84 = (1.0/298.257223563)
    # J2_GLO = 1.0826257E-3  # 2nd zonal harmonic of geopot
    # AU = 149597870691.0
    D2R = PI/180
    R2D = 180/PI
    # AS2R = D2R/3600.0
    # DAY_SEC = 86400.0
    # CENTURY_SEC = DAY_SEC*36525.0


class uGNSS():
    """ class for GNSS constants """
    GPS = 0
    GLO = 1
    GAL = 2
    BDS = 3

    # sat type
    # GEO  = 1
    # IGSO = 2
    # MEO  = 3

    # SBS = ?
    # QZS = ?
    # IRN = ?
    # GPSMAX = 32
    # GALMAX = 36
    # QZSMAX = 10
    # GLOMAX = 27
    # BDSMAX = 63
    # SBSMAX = 24
    # IRNMAX = 10
    # NONE = -1
    # MAXSAT = GPSMAX + GALMAX + GLOMAX + BDSMAX

class rSIG():
    """ class to define signals """
    NONE = 0
    L1C = 1
    L1X = 2
    L1W = 3
    L2C = 4
    L2L = 5
    L2X = 6
    L2W = 7
    L5Q = 8
    L5X = 9
    L7Q = 10
    L7X = 11
    SIGMAX = 16


class Obs():
    """ observation data record """

    def __init__(self):
        self.t = gtime_t()
        self.nsat = 0
        self.P = []
        self.L = []
        self.S = []
        self.D = []
        # self.lli = []
        # self.Lstd = []
        # self.Pstd = []
        self.sat = []


class Eph():
    """ class to define GPS/GAL/QZS/CMP ephemeris """
    prn = 0
    sys = 0
    iode = 0
    iodc = 0
    f0 = 0.0
    f1 = 0.0
    f2 = 0.0
    toc = 0
    toe = 0
    # tot = 0
    week = 0
    crs = 0.0
    crc = 0.0
    cus = 0.0
    cus = 0.0
    cis = 0.0
    cic = 0.0
    e = 0.0
    i0 = 0.0
    A = 0.0
    deln = 0.0
    M0 = 0.0
    OMG0 = 0.0
    OMGd = 0.0
    omg = 0.0
    idot = 0.0
    tgd = [0.0, 0.0]
    sva = 0
    health = 0
    fit = 0
    toes = 0

    def __init__(self, sat=0):
        self.sat = sat

def satazel(pos, e):
    """ calculate az/el from LOS vector in ECEF (e) """
    if pos[2] > -rCST.RE_WGS84 + 1:
        enu = ecef2enu(pos, e)
        az = arctan2(enu[0], enu[1]) if np.dot(enu, enu) > 1e-12 else 0
        az = az if az > 0 else az + 2 * np.pi
        el = arcsin(enu[2])
        return az, el
    else:
        return 0, np.pi / 2

def time2doy(t):
    """ convert time to epoch """
    ep = time2epoch(t)
    ep[1] = ep[2] = 1.0
    ep[3] = ep[4] = ep[5] = 0.0
    return timediff(t, epoch2time(ep))/86400+1

def ionmodel(t, pos, az, el, ion=None):
    """ klobuchar model of ionosphere delay estimation """
    psi = 0.0137 / (el / np.pi + 0.11) - 0.022
    phi = pos[0] / np.pi + psi * cos(az)
    phi = np.max((-0.416, np.min((0.416, phi))))
    lam = pos[1]/np.pi + psi * sin(az) / cos(phi * np.pi)
    phi += 0.064 * cos((lam - 1.617) * np.pi)
    _, tow = time2gpst(t)
    tt = 43200.0 * lam + tow  # local time
    tt -= np.floor(tt / 86400) * 86400
    f = 1.0 + 16.0 * np.power(0.53 - el/np.pi, 3.0)  # slant factor

    h = [1, phi, phi**2, phi**3]
    amp = np.dot(h, ion[0, :])
    per = np.dot(h, ion[1, :])
    amp = max(amp, 0)
    per = max(per, 72000.0)
    x = 2.0 * np.pi * (tt - 50400.0) / per
    if np.abs(x) < 1.57:
        v = 5e-9 + amp * (1.0 + x * x * (-0.5 + x * x / 24.0))
    else:
        v = 5e-9
    diono = rCST.CLIGHT * f * v
    return diono

def interpc(coef, lat):
    """ linear interpolation (lat step=15) """
    i = int(lat / 15.0)
    if i < 1:
        return coef[:, 0]
    if i > 4:
        return coef[:, 4]
    d = lat / 15.0 - i
    return coef[:, i-1] * (1.0 - d) + coef[:, i] * d

def tropmodel(t, pos, el, humi):
    """ saastamonien tropospheric delay model """
    temp0  = 15 # temparature at sea level
    if pos[2] < -100 or pos[2] > 1e4 or el <= 0:
        return 0, 0, 0
    hgt = max(pos[2], 0)
    # standard atmosphere
    pres = 1013.25 * np.power(1 - 2.2557e-5 * hgt, 5.2568)
    temp = temp0 - 6.5e-3 * hgt + 273.16
    e = 6.108 * humi * np.exp((17.15 * temp - 4684.0) / (temp - 38.45))
    # saastamoinen model
    z = np.pi / 2.0 - el
    trop_hs = 0.0022768 * pres / (1.0 - 0.00266 * np.cos(2 * pos[0]) - 
              0.00028e-3 * hgt) / np.cos(z)
    trop_wet = 0.002277 * (1255.0 / temp+0.05) * e / np.cos(z)
    return trop_hs, trop_wet, z

def mapf(el, a, b, c):
    """ simple tropospheric mapping function """
    sinel = np.sin(el)
    return (1.0 + a / (1.0 + b / (1.0 + c))) / (sinel + (a / (sinel + b / (sinel + c))))

def tropmapf(t, pos, el):
    """ tropospheric mapping function Neil (NMF)  """
    if pos[2] < -1e3 or pos[2] > 20e3 or el <= 0.0:
        return 0.0, 0.0
    
    aht = nmf_aht
    lat = np.rad2deg(pos[0])
    # year from doy 28, add half a year for southern latitudes
    y = (time2doy(t) - 28.0) / 365.25
    y += 0.5 if lat < 0 else 0
    cosy = np.cos(2.0 * np.pi * y)
    c = interpc(nmf_coef, np.abs(lat))
    ah = c[0:3] - c[3:6] * cosy
    aw = c[6:9]
    # ellipsoidal height is used instead of height above sea level
    dm = (1.0 / np.sin(el) - mapf(el, aht[0], aht[1], aht[2])) * pos[2] * 1e-3
    mapfh = mapf(el, ah[0], ah[1], ah[2]) + dm
    mapfw = mapf(el, aw[0], aw[1], aw[2])
   
    return mapfh, mapfw

# gtime将gps时间分为了整数位和小数位，可能是为了考虑数据存储方便，因为小数点可能非常靠后
class gtime_t():
    """ class to define the time """
    def __init__(self, time=0, sec=0.0):
        self.time = time
        self.sec = sec

def timediff(t1: gtime_t, t2: gtime_t):
    """ return time difference """
    dt = t1.time - t2.time
    dt += (t1.sec - t2.sec)
    return dt

def timeadd(t: gtime_t, sec: float):
    """ return time added with sec """
    import copy
    tr = copy.deepcopy(t)
    tr.sec += sec
    tt = floor(tr.sec)
    tr.time += int(tt)
    tr.sec -= tt
    return tr

def epoch2time(ep):
    """ calculate time from epoch """
    doy = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    time = gtime_t()
    year = int(ep[0])
    mon = int(ep[1])
    day = int(ep[2])

    if year < 1970 or year > 2099 or mon < 1 or mon > 12:
        return time
    days = (year-1970)*365+(year-1969)//4+doy[mon-1]+day-2
    if year % 4 == 0 and mon >= 3:
        days += 1
    sec = int(ep[5])
    time.time = days*86400+int(ep[3])*3600+int(ep[4])*60+sec
    time.sec = ep[5]-sec
    return time

def time2epoch(t):
    """ convert time to epoch """
    mday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31,
            30, 31, 31, 30, 31, 30, 31, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31,
            30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    days = int(t.time/86400)
    sec = int(t.time-days*86400)
    day = days % 1461
    for mon in range(48):
        if day >= mday[mon]:
            day -= mday[mon]
        else:
            break
    ep = [0, 0, 0, 0, 0, 0]
    ep[0] = 1970+days//1461*4+mon//12
    ep[1] = mon % 12+1
    ep[2] = day+1
    ep[3] = sec//3600
    ep[4] = sec % 3600//60
    ep[5] = sec % 60+t.sec
    return ep

def timediff(t1: gtime_t, t2: gtime_t):
    """ return time difference """
    dt = t1.time - t2.time
    dt += (t1.sec - t2.sec)
    return dt

def gpst2time(week, tow):
    """ convert to time from gps-time """
    t = epoch2time(gpst0)
    if tow < -1e9 or tow > 1e9:
        tow = 0.0
    t.time += 86400*7*week+int(tow)
    t.sec = tow-int(tow)
    return t

def time2gpst(t: gtime_t):
    """ convert to gps-time from time """
    t0 = epoch2time(gpst0)
    sec = t.time-t0.time
    week = int(sec/(86400*7))
    tow = sec-week*86400*7+t.sec
    return week, tow

def geodist(rs, rr):
    """ geometric distance ----------------------------------------------------------
    * compute geometric distance and receiver-to-satellite unit vector
    * args   : double *rs       I   satellite position (ecef at transmission) (m)
    *          double *rr       I   receiver position (ecef at reception) (m)
    *          double *e        O   line-of-sight vector (ecef)
    * return : geometric distance (m) (0>:error/no satellite position)
    * notes  : distance includes sagnac effect correction """
    e = rs - rr
    r = norm(e)
    e /= r
    # 这里需要考虑地球自转的影响
    r += rCST.OMGE * (rs[0] * rr[1] -rs[1] * rr[0]) / rCST.CLIGHT
    return r, e


def xyz2enu(pos):
    """ return ECEF to ENU conversion matrix from LLH 
        pos is LLH
    """
    sp = sin(pos[0])
    cp = cos(pos[0])
    sl = sin(pos[1])
    cl = cos(pos[1])
    E = np.array([[-sl, cl, 0],
                  [-sp*cl, -sp*sl, cp],
                  [cp*cl, cp*sl, sp]])
    return E

def ecef2pos(r):
    """  ECEF to LLH position conversion """
    pos = np.zeros(3)
    e2 = rCST.FE_WGS84*(2-rCST.FE_WGS84)
    r2 = r[0]**2+r[1]**2
    v = rCST.RE_WGS84
    z = r[2]
    zk = 0
    while abs(z - zk) >= 1e-4:
        zk = z
        sinp = z / np.sqrt(r2+z**2)
        v = rCST.RE_WGS84 / np.sqrt(1 - e2 * sinp**2)
        z = r[2] + v * e2 * sinp
    pos[0] = np.arctan(z / np.sqrt(r2)) if r2 > 1e-12 else np.pi / 2 * np.sign(r[2])
    pos[1] = np.arctan2(r[1], r[0]) if r2 > 1e-12 else 0
    pos[2] = np.sqrt(r2 + z**2) - v
    return pos

def ecef2enu(pos, r):
    """ relative ECEF to ENU conversion """
    E = xyz2enu(pos)
    e = E @ r
    return e

trace_level = 5

def trace(level, msg):
    if level <= trace_level:
        sys.stderr.write('%d %s' % (level, msg))
        
def tracemat(level, msg, mat, fmt='.6f'):
    if level > trace_level:
        return
    fmt = '{:' + fmt + '}'
    if len(mat.shape) == 1 or mat.shape[1] == 1:
        trace(level, msg)
        sys.stderr.write(' '.join(map(fmt.format, mat)))
        sys.stderr.write('\n')
    else:
        trace(level, msg + '\n')
        for row in mat:
            sys.stderr.write(' '.join(map(fmt.format, row)))
            sys.stderr.write('\n')
    
def tracelevel(level):
    global trace_level
    trace_level = level
