import sys
import os
sys.path.append("..")
from rtcm import read_file
from rtkcmn import Obs


if __name__ == "__main__":
    curdir = os.path.abspath(os.path.join(os.getcwd(), "../data"))
    rtcmfile = curdir + "/05_rtcm.log"

    obs = None
    nav = None

    read_file(rtcmfile, obs, nav)
    # print(rtcm[0])