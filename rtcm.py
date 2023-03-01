from pyrtcm import RTCMReader
from rtkcmn import uGNSS

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
    # 1057: ret=decode_ssr1(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1057:
        pass
    # 1058: ret=decode_ssr2(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1058:
        pass
    # 1059: ret=decode_ssr3(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1059:
        pass
    # 1060: ret=decode_ssr4(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1060:
        pass
    # 1061: ret=decode_ssr5(rtcm,SYS_GPS)  /* not supported */
    elif rtcm.DF002 == 1061:
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
    # 1240: ret=decode_ssr1(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1240:
        pass
    # 1241: ret=decode_ssr2(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1241:
        pass
    # 1242: ret=decode_ssr3(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1242:
        pass
    # 1243: ret=decode_ssr4(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1243:
        pass
    # 1244: ret=decode_ssr5(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1244:
        pass
    # 1245: ret=decode_ssr6(rtcm,SYS_GAL)  /* not supported */
    elif rtcm.DF002 == 1245:
        pass
    # 1246: ret=decode_ssr1(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1246:
        pass
    # 1247: ret=decode_ssr2(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1247:
        pass
    # 1248: ret=decode_ssr3(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1248:
        pass
    # 1249: ret=decode_ssr4(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1249:
        pass
    # 1250: ret=decode_ssr5(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1250:
        pass
    # 1251: ret=decode_ssr6(rtcm,SYS_QZS)  /* not supported */
    elif rtcm.DF002 == 1251:
        pass
    # 1252: ret=decode_ssr1(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1252:
        pass
    # 1253: ret=decode_ssr2(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1253:
        pass
    # 1254: ret=decode_ssr3(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1254:
        pass
    # 1255: ret=decode_ssr4(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1255:
        pass
    # 1256: ret=decode_ssr5(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1256:
        pass
    # 1257: ret=decode_ssr6(rtcm,SYS_SBS)  /* not supported */
    elif rtcm.DF002 == 1257:
        pass
    # 1258: ret=decode_ssr1(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1258:
        pass
    # 1259: ret=decode_ssr2(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1259:
        pass
    # 1260: ret=decode_ssr3(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1260:
        pass
    # 1261: ret=decode_ssr4(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1261:
        pass
    # 1262: ret=decode_ssr5(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1262:
        pass
    # 1263: ret=decode_ssr6(rtcm,SYS_CMP)  /* not supported */
    elif rtcm.DF002 == 1263:
        pass
    else:
        pass

def decode_msm7(rtcm, sys):
    print(rtcm)
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

    staid = rtcm.DF003      # 基准站ID
    sync = rtcm.DF393       # MSM多信息标志
    iods = rtcm.DF409       # 数据期号
    _ = rtcm.DF001_7        # 预留
    clk_str = rtcm.DF411    # 锁定引导标志
    clk_ext = rtcm.DF412    # 扩展锁定标志
    smooth = rtcm.DF417     # GNSS平滑类型标志
    tint_s = rtcm.DF418     # GNSS平滑区间
    
    nsat = rtcm.NSat        # 
    sats_mask = rtcm.DF394  # GNSS卫星掩码
    nsig = rtcm.NSig        # 
    sigs_mask = rtcm.DF395  # GNSS信号掩码
    cell_mask = rtcm.DF396  