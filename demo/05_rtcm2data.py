import sys
import os
sys.path.append("..")
from rtcm import read_file
from rtkcmn import Obs, \
                   tracelevel

trace_level = 5
if trace_level > 0:
    trcfile = os.path.join("./", 'test.trace')
    sys.stderr = open(trcfile, "w")
tracelevel(5)

if __name__ == "__main__":
    curdir = os.path.abspath(os.path.join(os.getcwd(), "../data"))
    rtcmfile = curdir + "/05_rtcm.log"

    obs = None
    nav = None

    read_file(rtcmfile, obs, nav)