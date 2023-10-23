# coding: utf-8
# python计算两个经纬度之间的距离
import math
from math import pi

# lat lon - > distance
# 计算经纬度之间的距离，单位为千米

EARTH_REDIUS = 6378.137


def rad(d):
    return d * pi / 180.0


def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.asin(
        math.sqrt(math.pow(math.sin(a / 2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b / 2), 2)))
    s = s * EARTH_REDIUS
    return s


if __name__ == '__main__':
    ret = getDistance(32.125421,118.964891,31.391163, 121.057778)
    print(ret)


