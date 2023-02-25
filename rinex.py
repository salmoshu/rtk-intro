def flt(u):
    """ scientific notation string to float """
    try:
        return float(u.replace("D", "E"))
    except:
        return 0