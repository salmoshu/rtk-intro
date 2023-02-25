"""
假设有一组GPS的单频观测数据和星历数据, 基于此数据进行伪距单点定位
1. 这里暂未考虑电离层、对流层误差校正
"""

import sys
import os
import numpy as np
sys.path.append("..")
from rtkcmn import Obs, Eph, rSIG, rCST, uGNSS, \
                   epoch2time, gpst2time, timeadd, timediff, \
                   geodist, satazel, ecef2pos
from ephemeris import eph2pos

class Obs_ex():
    ver = 0.0
    nsig = 0
    nband = 0
    pos = np.array([0, 0, 0])
    sig_tbl = {'1C': rSIG.L1C, '1X': rSIG.L1X, '1W': rSIG.L1W,
               '2W': rSIG.L2W, '2C': rSIG.L2C, '2X': rSIG.L2X,
               '5Q': rSIG.L5Q, '5X': rSIG.L5X, '7Q': rSIG.L7Q,
               '7X': rSIG.L7X} 
    sigid = np.ones((1, rSIG.SIGMAX*3), dtype=int) * rSIG.NONE
    typeid = np.ones((1, rSIG.SIGMAX*3), dtype=int) * rSIG.NONE
    obslist = []

class Eph_ex():
    ver = 0.0
    eph = []
    ephlist = []
    def flt(self, u, c=-1):
        if c >= 0:
            u = u[19*c+4:19*(c+1)+4]
        try:
            return float(u.replace("D", "E"))
        except:
            return 0

class Sol():
    rr = np.zeros(3)
    # """" class for solution """  
    # def __init__(self):
    #     self.rr = np.zeros(3)

def decode_obs(obsfile, obsx):
    fobs = open(obsfile, 'rt')
    # HEADER
    for line in fobs:
        if line[60:73] == 'END OF HEADER':
            break
        if line[60:80] == 'RINEX VERSION / TYPE':
            obsx.ver = float(line[4:10])
            if obsx.ver < 3.02:
                return -1
        elif line[60:79] == 'APPROX POSITION XYZ':
            obsx.pos = np.array([float(line[0:14]),
                            float(line[14:28]),
                            float(line[28:42])])
        elif line[60:79] == 'SYS / # / OBS TYPES':
            # 假设只有GPS
            sys = uGNSS.GPS
            obsx.nsig = int(line[3:6])
            s = line[7:7+4*13]
            for k in range(obsx.nsig):
                sig = s[4*k:3+4*k]
                if sig[1:3] not in obsx.sig_tbl:
                    continue
                if sig[0] == 'C':
                    obsx.typeid[sys][k] = 0
                elif sig[0] == 'L':
                    obsx.typeid[sys][k] = 1
                elif sig[0] == 'S':
                    obsx.typeid[sys][k] = 2
                elif sig[0] == 'D':
                    obsx.typeid[sys][k] = 3
                else:
                    continue
                obsx.sigid[sys][k] = obsx.sig_tbl[sig[1:3]]
            obsx.nband = len(np.where(obsx.typeid[sys]==1)[0])

    # DATA
    for line in fobs:
        if line == '':
            break
        if line[0] != '>':
            continue
        obs = Obs()
        nsat = int(line[32:35])
        year = int(line[2:6])
        month = int(line[7:9])
        day = int(line[10:12])
        hour = int(line[13:15])
        minute = int(line[16:18])
        sec = float(line[19:29])
        obs.nsat = nsat
        obs.t = epoch2time([year, month, day, hour, minute, sec])
        obs.P = np.zeros((nsat, obsx.nband))
        obs.L = np.zeros((nsat, obsx.nband))
        obs.D = np.zeros((nsat, obsx.nband))
        obs.S = np.zeros((nsat, obsx.nband))
        # obs.lli = np.zeros((nsat, obsx.nband), dtype=int)
        # obs.Pstd = np.zeros((nsat, obsx.nband), dtype=int)
        # obs.Lstd = np.zeros((nsat, obsx.nband), dtype=int)
        # obs.mag = np.zeros((nsat, obsx.nband))
        obs.sat = np.zeros(nsat, dtype=int)
        n = 0
        for k in range(nsat):
            line = fobs.readline()
            prn = int(line[1:3])

            for i in range(obsx.nsig):
                obs_ = line[16*i+4:16*i+17].strip()
                if obs_ == '' or obsx.sigid[sys][i] == 0:
                    continue
                try:
                    obsval = float(obs_)
                except:
                    obsval = 0

                f = i // (obsx.nsig // obsx.nband) # 单频时f始终为0
                obs.sat[n] = prn
                if obsx.typeid[sys][i] == 0:  # code
                    obs.P[n, f] = obsval
                    # Pstd = line[16*i+18]
                    # obs.Pstd[n, f] = int(Pstd) if Pstd != " " else 0
                elif obsx.typeid[sys][i] == 1:  # carrier
                    obs.L[n, f] = obsval
                    # lli = line[16*i+17]
                    # obs.lli[n, f] = int(lli) if lli != " " else 0
                    # Lstd = line[16*i+18]
                    # obs.Lstd[n, f] = int(Lstd) if Lstd != " " else 0
                elif obsx.typeid[sys][i] == 2:  # C/No
                    obs.S[n, f] = obsval
                elif obsx.typeid[sys][i] == 3:  # Doppler
                    obs.D[n, f] = obsval
            n += 1
        obs.P = obs.P[:n, :]
        obs.L = obs.L[:n, :]
        # obs.Pstd = obs.Pstd[:n, :]
        # obs.Lstd = obs.Lstd[:n, :]
        obs.D = obs.D[:n, :]
        obs.S = obs.S[:n, :]
        # obs.lli = obs.lli[:n, :]
        # obs.mag = obs.mag[:n, :]
        obs.sat = obs.sat[:n]

        obsx.obslist.append(obs)

    fobs.close()

def decode_eph(ephfile, ephx):
    """decode RINEX Navigation message from file """
    feph = open(ephfile, 'rt')
    ephx.eph = []
    for line in feph:
        if line[60:73] == 'END OF HEADER':
            break
        elif line[60:80] == 'RINEX VERSION / TYPE':
            ephx.ver = float(line[4:10])
            if ephx.ver < 3.02:
                return -1
        elif line[60:76] == 'IONOSPHERIC CORR': # 假设只存在GPS
            if line[0:4] == 'GPSA':
                for k in range(4):
                    ephx.ion[0, k] = ephx.flt(line[5+k*12:5+(k+1)*12])
            if line[0:4] == 'GPSB':
                for k in range(4):
                    ephx.ion[1, k] = ephx.flt(line[5+k*12:5+(k+1)*12])

    for line in feph:
        prn = int(line[1:3])
        sat = prn
        year = int(line[4:8])
        month = int(line[9:11])
        day = int(line[12:14])
        hour = int(line[15:17])
        minute = int(line[18:20])
        sec = int(line[21:23])
        toc = epoch2time([year, month, day, hour, minute, sec])

        # 假设不考虑除GPS的其他星座
        eph = Eph(sat)
        eph.toc = toc
        eph.f0 = ephx.flt(line, 1)
        eph.f1 = ephx.flt(line, 2)
        eph.f2 = ephx.flt(line, 3)

        line = feph.readline() #3:6
        eph.iode = int(ephx.flt(line, 0)) 
        eph.crs = ephx.flt(line, 1)
        eph.deln = ephx.flt(line, 2)
        eph.M0 = ephx.flt(line, 3)

        line = feph.readline() #7:10
        eph.cuc = ephx.flt(line, 0)
        eph.e = ephx.flt(line, 1)
        eph.cus = ephx.flt(line, 2)
        sqrtA = ephx.flt(line, 3)
        eph.A = sqrtA**2

        line = feph.readline() #11:14
        eph.toes = int(ephx.flt(line, 0))
        eph.cic = ephx.flt(line, 1)
        eph.OMG0 = ephx.flt(line, 2)
        eph.cis = ephx.flt(line, 3)

        line = feph.readline() #15:18
        eph.i0 = ephx.flt(line, 0)
        eph.crc = ephx.flt(line, 1)
        eph.omg = ephx.flt(line, 2)
        eph.OMGd = ephx.flt(line, 3)

        line = feph.readline() #19:22
        eph.idot = ephx.flt(line, 0)
        eph.code = int(ephx.flt(line, 1))  # source for GAL NAV type
        eph.week = int(ephx.flt(line, 2))

        line = feph.readline() #23:26
        eph.sva = ephx.flt(line, 0)
        eph.svh = int(ephx.flt(line, 1))
        tgd = np.zeros(2)
        tgd[0] = float(ephx.flt(line, 2))
        eph.iodc = int(ephx.flt(line, 3))
        eph.tgd = tgd

        line = feph.readline() #27:30
        tot = int(ephx.flt(line, 0))
        if len(line) >= 42:
            eph.fit = int(ephx.flt(line, 1))

        eph.toe = gpst2time(eph.week, eph.toes)
        eph.tot = gpst2time(eph.week, tot)

        ephx.ephlist.append(eph) # 假设只考虑一组星历数据

    feph.close()

def Gunit(rs, X, k):
    return - (rs[k] - X[k, 0]) / np.sqrt((rs[0]-X[0, 0])**2 + (rs[1]-X[1, 0])**2 + (rs[2]-X[2, 0])**2)

def bunit(p, rs, X):
    return p - ( np.sqrt((rs[0]-X[0, 0])**2 + (rs[1]-X[1, 0])**2 + (rs[2]-X[2, 0])**2) + X[3, 0] )

def pntpos(itr, obs, ephlist, X):
    """ single-point positioning ----------------------------------------------------
    * compute receiver position, velocity, clock bias by single-point positioning
    * with pseudorange and doppler observables
    """

    G = np.zeros((obs.nsat, 4))
    b = np.zeros((obs.nsat, 1))
    dion = dtrp = 0
    rr = Sol.rr

    for _ in range(10): # 只考虑10次迭代
        for i, sat in enumerate(obs.sat):
            """ 1. 卫星空间位置解算"""
            for eph in ephlist:
                if eph.sat == sat:

                    pr = obs.P[i,0]
                    t = timeadd(obs.t, -pr / rCST.CLIGHT)

                    t1 = ts = timediff(t, eph.toc)
                    for _ in range(2):
                        t1 = ts - (eph.f0 + eph.f1 * t1 + eph.f2 * t1**2)
                    dt = eph.f0 + eph.f1*t1 + eph.f2 * t1**2

                    # # tk = dtadjust(obs.t, eph.toc)
                    # # dt = eph.f0 + eph.f1 * tk + eph.f2 * tk**2
                    t = timeadd(t, -dt)
                    rs, dts, _ = eph2pos(t, eph) # 这里存在重复计算，先忽略

                    # TGD
                    # 这里暂不考虑GLO
                    break
            """ 2. 数据准备与初始解的设置 """
            # 伪距校正 Pc = P + dtm -Im -Tm
            rs = np.array(rs)
            r, e = geodist(rs, rr)
            if r < 0:
                continue
            pos = ecef2pos(rr)
            az, el = satazel(pos, e)

            if el < 10 * rCST.D2R:
                continue

            if obs.S[i,[0]] < 35:
                continue

            if itr == 0:
                dion = dtrp = 0
            else:
                dion = dtrp = 0

            Pr = obs.P[i, 0] - eph.tgd[0] * rCST.CLIGHT
            dts -= eph.tgd[0]
            P1 = Pr + dts*rCST.CLIGHT - dion - dtrp
            # print(np.sqrt((rs[0]-X[0, 0])**2 + (rs[1]-X[1, 0])**2 + (rs[2]-X[2, 0])**2))
            # G1 = np.array([[Gunit(rs, X, 0), Gunit(rs, X, 1), Gunit(rs, X, 2), 1]])
            G1 = -e
            b1 = P1 - r - X[3, 0]
            # b1 = np.array([bunit(P1, rs, X)])

            """ 3. 非线性方程组线性化 """
            if obs.nsat < 4:
                return -1
            else:
                G[i, 0:3] = G1
                G[i, 3] = 1
                # G[i, :] = G1
                b[i, 0] = b1

        """ 4. 最小二乘法 """
        dx = np.linalg.inv(G.T @ G) @ G.T @ b
        X += dx

        rr = [X[0, 0], X[1, 0], X[2, 0]]

        if np.linalg.norm(dx) <= 1e-4:
            break
    return [X[0, 0], X[1, 0], X[2, 0]]


def postpos(obsx, ephx):
    
    X = np.zeros((4, 1))
    for i, obs in enumerate(obsx.obslist):
        rr = pntpos(i, obs, ephx.ephlist, X) # 假设只考虑一组星历
        Sol.rr = rr
        if i == 0:
            continue
        D2R = rCST.D2R
        llh = ecef2pos(rr)
        print(llh[0]/D2R, llh[1]/D2R, llh[2])

if __name__ == "__main__":
    curdir = os.path.abspath(os.path.join(os.getcwd(), "../data"))

    # 参考经纬度: 31.17930441 121.40605141
    obsfile = curdir + "/02_rover_log.obs"
    ephfile = curdir + "/02_rover_log.nav"
    obsx = Obs_ex() # obsx存储有关obs的额外信息
    ephx = Eph_ex() # ephx存储有关eph的额外信息

    decode_obs(obsfile, obsx)
    decode_eph(ephfile, ephx)

    postpos(obsx, ephx)    