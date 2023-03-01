import sys
import os
sys.path.append("..")
from rtcm import read_file
from rtkcmn import Obs


if __name__ == "__main__":
    curdir = os.path.abspath(os.path.join(os.getcwd(), "../data"))
    rtcmfile = curdir + "/05_rtcm.log"

    rtcm = []

    read_file(rtcmfile, rtcm)
    print(rtcm[0])