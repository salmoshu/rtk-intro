"""
将01_demo中的eph2pos进行了完善，并将其封装到了ephemeris.py中
更新内容：
1. 对于其中的gps时间描述，整数位和小数位进行了分开描述，主要是为了存储及计算方便
2. 对于eph2pos中的步骤4，增加了多次迭代和迭代满足的条件
3. 增加了四大星座的解算
4. 增加了北斗GEO卫星的解算
5. 增加了钟差
6. 预留了星历ura方差
"""

import sys
import os
import numpy as np
sys.path.append("..")
from rtkcmn import Eph, gtime_t, uGNSS
from ephemeris import eph2pos

def ephinit(filename, eph):
    with open(filename, "rt") as feph:
        for line in feph:
            key = line.split(" ")[0]
            value = line.split(" ")[-1]
            
            if key == "toe":
                eph.toes = float(value)
                eph.toe = gtime_t()
                eph.toe.time = int(eph.toes)
                eph.toe.sec = eph.toes - eph.toe.time
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

if __name__ == "__main__":
    eph = Eph(1) # G01
    eph.sys = uGNSS.GPS
    eph.toc = gtime_t(0, 0) # 占位，避免求取dt时报错
    eph.sva = 0 # 占位，避免求取var时报错
    time = gtime_t(239050, 0.7223) # 假设为同一周

    curdir = os.path.abspath(os.path.join(os.getcwd(), "../data"))
    ephinit(curdir + "/01_ephG01.txt", eph)
    rs, _, _ = eph2pos(time, eph)
    print(rs)