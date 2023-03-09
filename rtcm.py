from pyrtcm import RTCMReader
from rtkcmn import uGNSS, rCST, \
                   trace

RANGE_MS = rCST.CLIGHT*0.001

class MSM_h():
    rtype = 0
    staid = 0
    tow = 0
    sync = 0
    iod = 0                     # issue of data station
    clk_str = 0                 # clock steering indicator
    clk_ext = 0                 # external clock indicator
    smooth = 0                  # divergence free smoothing indicator
    tint_s = 0                  # soothing interval
    nsat = 0                    # number of satellites
    sats = [0]*64;              # satellites
    nsig = 0                    # number of signals
    usigs = [0]*32;             # signals
    cellmask = [0]*nsat*nsig;   # cell mask

class RTCM():        #/* RTCM control struct type */
    staid = 0 # int staid;          /* station id */
    stah = 0 # int stah;           /* station health */
    seqno = 0 # int seqno;          /* sequence number for rtcm 2 or iods msm */
    outtype = 0 # int outtype;        /* output message type */
    time = 0 # gtime_t time;       /* message time */
    time_s = 0 # gtime_t time_s;     /* message start time */
    obs = 0 # obs_t obs;          /* observation data (uncorrected) */
    nav = 0 # nav_t nav;          /* satellite ephemerides */
    sta = 0 # sta_t sta;          /* station parameters */
    dgps = 0 # dgps_t *dgps;       /* output of dgps corrections */
    ssr = 0 # ssr_t ssr[MAXSAT];  /* output of ssr corrections */
    msg = 0 # char msg[128];      /* special message */
    msgtype = 0 # char msgtype[256];  /* last message type */
    msmtype = 0 # char msmtype[6][128]; /* msm signal types */
    obsflag = 0 # int obsflag;        /* obs data complete flag (1:ok,0:not complete) */
    ephsat = 0 # int ephsat;         /* update satellite of ephemeris */
    cp = 0 # double cp[MAXSAT][NFREQ+NEXOBS]; /* carrier-phase measurement */
    lock = 0 # unsigned short lock[MAXSAT][NFREQ+NEXOBS]; /* lock time */
    loss = 0 # unsigned short loss[MAXSAT][NFREQ+NEXOBS]; /* loss of lock count */
    lltime = 0 # gtime_t lltime[MAXSAT][NFREQ+NEXOBS]; /* last lock time */
    nbyte = 0 # int nbyte;          /* number of bytes in message buffer */ 
    nbit = 0 # int nbit;           /* number of bits in word buffer */ 
    len = 0 # int len;            /* message length (bytes) */
    buff = 0 # unsigned char buff[1200]; /* message buffer */
    nmsg3 = 0 # unsigned int nmsg3[300]; /* message count of RTCM 3 (1-299:1001-1299,0:ohter) */
    opt = 0 # char opt[256];      /* RTCM dependent options */


def read_file(filename, obs, nav):
    stream = open(filename, 'rb')
    rtr = RTCMReader(stream)
    for (_, parsed_rtcm) in rtr:
        decode_rtcm(parsed_rtcm, obs, nav)
    stream.close()

def read_socket():
    pass

def read_serial():
    pass

def decode_rtcm(rtcm, obs, nav):
    # 1001: ret=decode_type1001(rtcm)  /* not supported */
    if rtcm.DF002 == 1001:
        pass
    # 1002: ret=decode_type1002(rtcm)  /* not supported */
    elif rtcm.DF002 == 1002:
        pass
    # 1003: ret=decode_type1003(rtcm)  /* not supported */
    elif rtcm.DF002 == 1003:
        pass
    # 1004: ret=decode_type1004(rtcm)  /* not supported */
    elif rtcm.DF002 == 1004:
        pass
    # 1005: ret=decode_type1005(rtcm)  /* not supported */
    elif rtcm.DF002 == 1005:
        pass
    # 1006: ret=decode_type1006(rtcm)  /* not supported */
    elif rtcm.DF002 == 1006:
        pass
    # 1007: ret=decode_type1007(rtcm)  /* not supported */
    elif rtcm.DF002 == 1007:
        pass
    # 1008: ret=decode_type1008(rtcm)  /* not supported */
    elif rtcm.DF002 == 1008:
        pass
    # 1009: ret=decode_type1009(rtcm)  /* not supported */
    elif rtcm.DF002 == 1009:
        pass
    # 1010: ret=decode_type1010(rtcm)  /* not supported */
    elif rtcm.DF002 == 1010:
        pass
    # 1011: ret=decode_type1011(rtcm)  /* not supported */
    elif rtcm.DF002 == 1011:
        pass
    # 1012: ret=decode_type1012(rtcm)  /* not supported */
    elif rtcm.DF002 == 1012:
        pass
    # 1013: ret=decode_type1013(rtcm)  /* not supported */
    elif rtcm.DF002 == 1013:
        pass
    # 1019: ret=decode_type1019(rtcm)  /* not supported */
    elif rtcm.DF002 == 1019:
        pass
    # 1020: ret=decode_type1020(rtcm)  /* not supported */
    elif rtcm.DF002 == 1020:
        pass
    # 1021: ret=decode_type1021(rtcm)  /* not supported */
    elif rtcm.DF002 == 1021:
        pass
    # 1022: ret=decode_type1022(rtcm)  /* not supported */
    elif rtcm.DF002 == 1022:
        pass
    # 1023: ret=decode_type1023(rtcm)  /* not supported */
    elif rtcm.DF002 == 1023:
        pass
    # 1024: ret=decode_type1024(rtcm)  /* not supported */
    elif rtcm.DF002 == 1024:
        pass
    # 1025: ret=decode_type1025(rtcm)  /* not supported */
    elif rtcm.DF002 == 1025:
        pass
    # 1026: ret=decode_type1026(rtcm)  /* not supported */
    elif rtcm.DF002 == 1026:
        pass
    # 1027: ret=decode_type1027(rtcm)  /* not supported */
    elif rtcm.DF002 == 1027:
        pass
    # 1030: ret=decode_type1030(rtcm)  /* not supported */
    elif rtcm.DF002 == 1030:
        pass
    # 1031: ret=decode_type1031(rtcm)  /* not supported */
    elif rtcm.DF002 == 1031:
        pass
    # 1032: ret=decode_type1032(rtcm)  /* not supported */
    elif rtcm.DF002 == 1032:
        pass
    # 1033: ret=decode_type1033(rtcm)  /* not supported */
    elif rtcm.DF002 == 1033:
        pass
    # 1034: ret=decode_type1034(rtcm)  /* not supported */
    elif rtcm.DF002 == 1034:
        pass
    # 1035: ret=decode_type1035(rtcm)  /* not supported */
    elif rtcm.DF002 == 1035:
        pass
    # 1037: ret=decode_type1037(rtcm)  /* not supported */
    elif rtcm.DF002 == 1037:
        pass
    # 1038: ret=decode_type1038(rtcm)  /* not supported */
    elif rtcm.DF002 == 1038:
        pass
    # 1039: ret=decode_type1039(rtcm)  /* not supported */
    elif rtcm.DF002 == 1039:
        pass
    # 1044: ret=decode_type1044(rtcm)  /* not supported */
    elif rtcm.DF002 == 1044:
        pass
    # 1045: ret=decode_type1045(rtcm)  /* not supported */
    elif rtcm.DF002 == 1045:
        pass
    # 1046: ret=decode_type1046(rtcm)  /* not supported */
    elif rtcm.DF002 == 1046:
        pass
    # 1042: ret=decode_type1042(rtcm)  /* not supported */
    elif rtcm.DF002 == 1042:
        pass
    # 1062: ret=decode_ssr6(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1062:
        pass
    # 1063: ret=decode_ssr1(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1063:
        pass
    # 1064: ret=decode_ssr2(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1064:
        pass
    # 1065: ret=decode_ssr3(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1065:
        pass
    # 1066: ret=decode_ssr4(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1003:
        pass
    # 1067: ret=decode_ssr5(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1067:
        pass
    # 1068: ret=decode_ssr6(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1068:
        pass
    # 1071: ret=decode_msm0(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1071:
        pass
    # 1072: ret=decode_msm0(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1072:
        pass
    # 1073: ret=decode_msm0(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1073:
        pass
    # 1074: ret=decode_msm4(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1074:
        pass
    # 1075: ret=decode_msm5(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1075:
        pass
    # 1076: ret=decode_msm6(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1076:
        pass
    # 1077: ret=decode_msm7(rtcm,SYS_GPS)
    elif rtcm.DF002 == 1077:
        ret = decode_msm7(rtcm, uGNSS.GPS)
    # 1081: ret=decode_msm0(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1081:
        pass
    # 1082: ret=decode_msm0(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1082:
        pass
    # 1083: ret=decode_msm0(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1083:
        pass
    # 1084: ret=decode_msm4(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1084:
        pass
    # 1085: ret=decode_msm5(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1085:
        pass
    # 1086: ret=decode_msm6(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1086:
        pass
    # 1087: ret=decode_msm7(rtcm,SYS_GLO)  /* not supported */
    elif rtcm.DF002 == 1087:
        pass
    # 1091: ret=decode_msm0(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1091:
        pass
    # 1092: ret=decode_msm0(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1092:
        pass
    # 1093: ret=decode_msm0(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1093:
        pass
    # 1094: ret=decode_msm4(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1094:
        pass
    # 1095: ret=decode_msm5(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1095:
        pass
    # 1096: ret=decode_msm6(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1096:
        pass
    # 1097: ret=decode_msm7(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1097:
        pass
    # 1101: ret=decode_msm0(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1101:
        pass
    # 1102: ret=decode_msm0(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1102:
        pass
    # 1103: ret=decode_msm0(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1103:
        pass
    # 1104: ret=decode_msm4(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1104:
        pass
    # 1105: ret=decode_msm5(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1105:
        pass
    # 1106: ret=decode_msm6(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1106:
        pass
    # 1107: ret=decode_msm7(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1107:
        pass
    # 1111: ret=decode_msm0(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1111:
        pass
    # 1112: ret=decode_msm0(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1112:
        pass
    # 1113: ret=decode_msm0(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1113:
        pass
    # 1114: ret=decode_msm4(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1114:
        pass
    # 1115: ret=decode_msm5(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1115:
        pass
    # 1116: ret=decode_msm6(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1116:
        pass
    # 1117: ret=decode_msm7(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1117:
        pass
    # 1121: ret=decode_msm0(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1121:
        pass
    # 1122: ret=decode_msm0(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1122:
        pass
    # 1123: ret=decode_msm0(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1123:
        pass
    # 1124: ret=decode_msm4(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1124:
        pass
    # 1125: ret=decode_msm5(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1125:
        pass
    # 1126: ret=decode_msm6(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1126:
        pass
    # 1127: ret=decode_msm7(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1127:
        pass
    # 1230: ret=decode_type1230(rtcm)  /* not supported */
    elif rtcm.DF002 == 1230:
        pass
    else:
        pass

def decode_msm_header(rtcm, sys, header):
    header.rtype = rtcm.DF002      # RTCM类型
    header.staid = rtcm.DF003      # 基准站ID
    # 注意这里的历元时间暂未考虑周数，不确定其影响
    if sys == uGNSS.GLO:
        pass
    elif sys == uGNSS.BDS:
        # refering: http://www.bdsytime.com/jishuzhichi2/20210524_73.html
        tow = rtcm.GNSSEpoch
        tow += 14 # BDT -> GPST
    elif sys == uGNSS.GPS or sys ==uGNSS.GAL:
        tow = rtcm.GNSSEpoch
    else:
        pass
    header.tow = tow
    header.sync = rtcm.DF393       # MSM多信息标志
    header.iods = rtcm.DF409       # 数据期号
    header.clk_str = rtcm.DF411    # 锁定引导标志
    header.clk_ext = rtcm.DF412    # 扩展锁定标志
    header.smooth = rtcm.DF417     # GNSS平滑类型标志
    header.tint_s = rtcm.DF418     # GNSS平滑区间
    header.nsat = rtcm.NSat        # GNSS卫星数目
    header.sats_mask = rtcm.DF394  # GNSS卫星掩码
    header.nsig = rtcm.NSig        # GNSS信号数目
    header.sigs_mask = rtcm.DF395  # GNSS信号掩码
    header.cell_mask = rtcm.DF396  # Cell标志组

def decode_msm7(rtcm, sys):
    header = MSM_h()
    r = [0.0]*64
    rr = [0.0]*64
    pr = [0.0]*64
    cp = [0.0]*64
    rrf = [0.0]*64
    cnr = [0.0]*64
    ex = [0] * 64
    half = [0] * 64

    # decode msm header
    decode_msm_header(rtcm, sys, header)
    
    ''' decode satellite data '''
    # range
    for i in range(0, header.nsat):
        rng = getattr(rtcm, f"DF406_{i+1:02}")
        if rng != 255:
            r[i] = rng * RANGE_MS

    # extended info
    for i in range(0, header.nsat):
        ex[i] = rtcm.GNSSSpecific_01

    print(r)

    # for (j=0;j<h.nsat;j++) {
    #     rng_m=getbitu(rtcm->buff,i,10); i+=10;
    #     if (r[j]!=0.0) r[j]+=rng_m*P2_10*RANGE_MS;
    # }
    # for (j=0;j<h.nsat;j++) { /* phaserangerate */
    #     rate =getbits(rtcm->buff,i,14); i+=14;
    #     if (rate!=-8192) rr[j]=rate*1.0;
    # }


    return 0