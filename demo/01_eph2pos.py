"""
利用星历参数(这里是PRN1卫星的星历)计算出GPS卫星在某一时刻的空间位置
参考: 《GPS原理与接收机设计》P61
"""

import sys
import os
import numpy as np
sys.path.append("..")
from rtkcmn import Eph, rCST

def ephinit(filename, eph):
    with open(filename, "rt") as feph:
        for line in feph:
            key = line.split(" ")[0]
            value = line.split(" ")[-1]

            # 01_demo暂未使用星历参数：
            # iode: 星历数据龄期
            # iodc: 指星钟数据龄期
            # f0~f3: 分别为卫星钟差(s)、卫星漂移(s/s)、卫星漂移速度(s/s^2)
            # toc: 卫星钟参考时间、对应年月日时分秒
            # week: GPS周数，与toe一同表示时间
            # sva: 卫星精度
            # health: 卫星健康状况
            # fit: 星历参数采用的拟合间隔
            # tgd: 群波延时
            # 当使用单频接收机时，用Tgd改正所观测的结果，以减小电离层效应影响提高定位精度；
            # 当采用双频接收机时，就不必要采用这个时延差改正，该值包含在定位计算的过程中。

            # 01_demo已使用的星历参数：
            # toe: 星历参考时间
            # sqrtA: 根号长半径
            # e: 偏心率
            # io 轨道倾角
            # OMG0: 轨道升交点赤经
            # omg: 近地点角距
            # M0: 平近点角
            # deln: 平均角速度校正值
            # idot: 轨道倾角校正值
            # OMGd: 轨道升交点赤经校正值
            # cuc: 升交点角距余弦调和校正
            # cus: 升交点角距正弦调和校正
            # crc: 轨道半径余弦调和校正
            # crs: 轨道半径正弦调和校正
            # cic: 轨道倾角余弦调和校正
            # cis: 轨道倾角正弦调和校正
            
            if key == "toe":
                eph.toe = float(value)
            elif key == "sqrtA":
                sqrtA = float(value)
                eph.A = np.power(sqrtA, 2)
            elif key == "e":
                eph.e = float(value)
            elif key == "i0":
                eph.i0 = float(value)  
            elif key == "OMG0":
                eph.OMG0 = float(value)
            elif key == "omg":
                eph.omg = float(value)
            elif key == "M0":
                eph.M0 = float(value)
            elif key == "deln":
                eph.deln = float(value)
            elif key == "idot":
                eph.idot = float(value)
            elif key == "OMGd":
                eph.OMGd = float(value)
            elif key == "cuc":
                eph.cuc = float(value)
            elif key == "cus":
                eph.cus = float(value)
            elif key == "crc":
                eph.crc = float(value)
            elif key == "crs":
                eph.crs = float(value)
            elif key == "cic":
                eph.cic = float(value)
            elif key == "cis":
                eph.cis = float(value)

def eph2pos(time, eph):
    """ learn: calculate sat postition """

    """ step 01 """
    # 计算规划时间tk
    tw = 604800
    tk = time - eph.toe
    if tk>tw:
        tk -= tw
    elif tk<-tw:
        tk += tw
    
    """ step 02 """
    # 计算卫星的平均角速度n
    mu = rCST.MU_GPS
    n0 = np.sqrt(mu / eph.A**3)
    n = n0 + eph.deln

    """ step 03 """
    # 计算信号发射时刻的平近点角Mk
    pi = rCST.PI
    Mk = eph.M0 + n*tk
    if Mk<0:
        Mk += 2*pi
    elif Mk>2*pi:
        Mk -= 2*pi

    """ step 04 """
    # 计算信号发射时刻的偏近点角Ek
    # 通常3次就能迭代出相对准确的值
    Ek, E = Mk, 0
    for _ in range(30):
        if abs(E - Ek) < 1e-13:
            break
        E = Ek
        Ek = Mk + eph.e*np.sin(Ek)
    
    """ step 05 """
    # 计算信号发射时刻的偏近点角vk
    cosv = (np.cos(Ek) - eph.e) / (1 - eph.e * np.cos(Ek))
    sinv = np.sqrt(1 - eph.e**2) * np.sin(Ek) / (1 - eph.e*np.cos(Ek))
    vk = np.arctan2(sinv, cosv)

    """ step 06 """
    # 计算信号发射时刻的升交点角距PHIk
    PHIk = vk + eph.omg

    """ step 07 """
    # 计算摄动校正后的升交点角距delta_uk、卫星矢距长度delta_rk和倾角delta_ik
    delta_uk = eph.cus*np.sin(2*PHIk) + eph.cuc*np.cos(2*PHIk)
    delta_rk = eph.crs*np.sin(2*PHIk) + eph.crc*np.cos(2*PHIk)
    delta_ik = eph.cis*np.sin(2*PHIk) + eph.cic*np.cos(2*PHIk)

    """ step 08 """
    # 计算摄动校正后的升交点角距delta_uk、卫星矢距长度delta_rk和
    uk = PHIk + delta_uk
    rk = eph.A * (1- eph.e*np.cos(Ek)) + delta_rk
    ik = eph.i0 + eph.idot*tk + delta_ik

    """ step 09 """
    # 计算信号发射时刻卫星在轨道平面的位置xk' yk'
    xd = rk * np.cos(uk)
    yd = rk * np.sin(uk)
    
    """ step 10 """
    # 计算信号发射时刻的升交点赤经OMGk
    OMGe = rCST.OMGE
    OMGk = eph.OMG0 + (eph.OMGd - OMGe)*tk - OMGe*eph.toe

    """ step 11 """
    # 计算卫星在WGS-84地心地固直角坐标系中的坐标(xk, yk, zk)
    xk = xd*np.cos(OMGk) - yd*np.cos(ik)*np.sin(OMGk)
    yk = xd*np.sin(OMGk) + yd*np.cos(ik)*np.cos(OMGk)
    zk = yd*np.sin(ik)
    
    return [xk, yk, zk]
    

if __name__ == "__main__":
    eph = Eph(1) # G01
    time = 239050.7223 # 假设星历的星期数与当前时间的星期数相等
    curdir = os.path.abspath(os.path.join(os.getcwd(), "../data"))
    ephinit(curdir + "/01_ephG01.txt", eph)
    rs = eph2pos(time, eph)
    print(rs)