from rtkcmn import timediff, rCST, uGNSS
import numpy as np

def dtadjust(t1, t2, tw=604800):
    """ calculate delta time considering week-rollover """
    dt = timediff(t1, t2)
    if dt > tw:
        dt -= tw
    elif dt < -tw:
        dt += tw
    return dt

def eph2pos(time, eph):
    """ broadcast ephemeris to satellite position and clock bias -------------
    * compute satellite position and clock with broadcast ephemeris (gps,
    * galileo, beidou)
    * args   : gtime_t time     I   time (gpst)
    *          eph_t eph        I   broadcast ephemeris
    * return : rs               O   satellite position (ecef) {x,y,z} (m)
    *          dts              O   satellite clock bias (s)
    *          var              O   satellite position and clock variance (m^2)
    * notes  : none  """

    """ 计算卫星位置rs """
    if eph.sys == uGNSS.GAL:
        mu = rCST.MU_GAL
        OMGe = rCST.OMGE_GAL
    elif eph.sys == uGNSS.BDS:
        mu = rCST.MU_CMP
        OMGe = rCST.OMGE_CMP
    else: # GPS
        mu = rCST.MU_GPS
        OMGe = rCST.OMGE

    # 01. 计算规划时间tk
    tk = dtadjust(time, eph.toe)

    # 02. 计算卫星的平均角速度n
    n0 = np.sqrt(mu / eph.A**3)
    n = n0 + eph.deln

    # 03. 计算信号发射时刻的平近点角Mk
    pi = rCST.PI
    Mk = eph.M0 + n*tk
    if Mk<0:
        Mk += 2*pi
    elif Mk>2*pi:
        Mk -= 2*pi

    # 04. 计算信号发射时刻的偏近点角Ek
    # 假设3次能够迭代出相对准确的值
    Ek, E = Mk, 0
    for _ in range(30):
        if abs(E - Ek) < 1e-13:
            break
        E = Ek
        Ek = Mk + eph.e*np.sin(Ek)

    # 05. 计算信号发射时刻的偏近点角vk
    cosv = (np.cos(Ek) - eph.e) / (1 - eph.e * np.cos(Ek))
    sinv = np.sqrt(1 - eph.e**2) * np.sin(Ek) / (1 - eph.e*np.cos(Ek))
    vk = np.arctan2(sinv, cosv)

    # 06. 计算信号发射时刻的升交点角距PHIk
    PHIk = vk + eph.omg

    # 07. 计算摄动校正后的升交点角距delta_uk、卫星矢距长度delta_rk和倾角delta_ik
    delta_uk = eph.cus*np.sin(2*PHIk) + eph.cuc*np.cos(2*PHIk)
    delta_rk = eph.crs*np.sin(2*PHIk) + eph.crc*np.cos(2*PHIk)
    delta_ik = eph.cis*np.sin(2*PHIk) + eph.cic*np.cos(2*PHIk)

    # 08. 计算摄动校正后的升交点角距delta_uk、卫星矢距长度delta_rk和
    uk = PHIk + delta_uk
    rk = eph.A * (1- eph.e*np.cos(Ek)) + delta_rk
    ik = eph.i0 + eph.idot*tk + delta_ik
    sini = np.sin(ik)
    cosi = np.cos(ik)

    # 09. 计算信号发射时刻卫星在轨道平面的位置xk' yk'
    xd = rk * np.cos(uk)
    yd = rk * np.sin(uk)

    if eph.sys == uGNSS.BDS and (eph.prn <= 5 or eph.prn >=59):
        # 参考文件：《北斗系统空间信号接口控制文件B31》星历参数用户算法部分 P33
        # 10_1. 计算信号发射时刻的升交点赤经OMGk (BDS GEO)
        # BDS GEO sat PRN: 01 02 03 04 05 59 60 61 （until 2023/02/16）
        OMGk = eph.OMG0 + eph.OMGd - OMGe*eph.toes

        # 11_1. 计算卫星在WGS-84地心地固直角坐标系中的坐标(xk, yk, zk) (BDS GEO)
        sinO = np.sin(OMGk)
        cosO = np.cos(OMGk)
        xg = xd*cosO - yd*cosi*sinO
        yg = xd*sinO + yd*cosi*cosO
        zg = yd*sini
        sino = np.sin(OMGe*tk)
        coso = np.cos(OMGe*tk)
        sin_5 = -0.0871557427476582 # sin(-5.0 deg)
        cos_5 = 0.9961946980917456  # cos(-5.0 deg)
        xk = xg*coso + yg*sino*cos_5 + zg*sino*sin_5
        yk = -xg*sino+yg*coso*cos_5+zg*coso*sin_5
        zk = -yg*sin_5+zg*cos_5
    else:
        # 10_2. 计算信号发射时刻的升交点赤经OMGk
        OMGk = eph.OMG0 + (eph.OMGd - OMGe)*tk - OMGe*eph.toes

        # 11_2. 计算卫星在WGS-84地心地固直角坐标系中的坐标(xk, yk, zk)
        sinO = np.sin(OMGk)
        cosO = np.cos(OMGk)
        xk = xd*cosO - yd*cosi*sinO
        yk = xd*sinO + yd*cosi*cosO
        zk = yd*sini

    rs = [xk, yk, zk]
    
    """ 计算卫星钟差dts """
    # 这里未考虑tdg
    tk = dtadjust(time, eph.toc)
    dts = eph.f0 + eph.f1 * tk + eph.f2 * tk**2
    
    # relativity correctio
    dts -= 2 *np.sqrt(mu * eph.A) * eph.e * np.sin(Ek) / rCST.CLIGHT**2

    var = 0

    return rs, dts, var
