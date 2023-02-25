from pyproj import CRS
from pyproj import Transformer
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

plot_title = 'rtkpy single'

crs_WGS84 = CRS.from_epsg(4326)        # WGS84地理坐标系
crs_ECEF = CRS.from_epsg(4328)         # ECEF地心地固坐标系
crs_WebMercator = CRS.from_epsg(3857)  # Web墨卡托投影坐标系


def ECEFToWGS84(x, y, z):
    transformer = Transformer.from_crs(crs_ECEF, crs_WGS84)
    lat, lon, alt = transformer.transform(x, y, z)
    return lat, lon, alt

def ECEFToWebMercator(x, y, z):
    transformer = Transformer.from_crs(crs_ECEF, crs_WebMercator)
    web_x, web_y, web_z = transformer.transform(x, y, z)
    return web_x, web_y, web_z

def WGS84ToWebMercator(lat, lon, alt):
    transformer = Transformer.from_crs(crs_WGS84, crs_WebMercator)
    web_x, web_y, web_z = transformer.transform(lat, lon, alt)
    return web_x, web_y, web_z

if __name__ == '__main__':
    trace_x = []
    trace_y = []
    first_x = 0
    first_x = 0

    file = open('temp.txt')
    for index, line in enumerate(file.readlines()):
        curLine = line.strip().split(" ")
        web_pos = WGS84ToWebMercator(curLine[0], curLine[1], curLine[2])
        if(len(trace_x) == 0):
            first_x = web_pos[0]
            first_y = web_pos[1]
            trace_x.append(0)
            trace_y.append(0)
        else:
            trace_x.append(web_pos[0] - first_x)
            trace_y.append(web_pos[1] - first_y)

    # x_major_locator=MultipleLocator(locator_dis)
    # y_major_locator=MultipleLocator(locator_dis)
    # ax=plt.gca()
    # ax.xaxis.set_major_locator(x_major_locator)
    # ax.yaxis.set_major_locator(y_major_locator)
    # plt.xlim(xlim_tuple)
    # plt.ylim(ylim_tuple)

    plt.plot(trace_x, trace_y, "or")
    plt.xlabel('m')
    plt.ylabel('m')
    plt.title(plot_title)
    plt.show()