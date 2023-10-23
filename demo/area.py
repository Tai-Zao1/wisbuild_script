import math
def  ConvertToRadian(input):
    return input * math.pi / 180
def CalculatePolygonArea0(data):
    area = 0
    arr = data.split(';')
    arr_len = len(arr)
    if arr_len < 3:
        return 0.0
    temp = []
    for i in range(0, arr_len):
        temp.append([float(x) for x in arr[i].split(',')])
    for i in range(0, arr_len):
        area += ConvertToRadian(temp[(i + 1) % arr_len][0] - temp[(i) % arr_len][0]) * (2 + math.sin(ConvertToRadian(temp[(i) % arr_len][1])) + math.sin(ConvertToRadian(temp[(i + 1) % arr_len][1])))
    area = area * 6378137.0 * 6378137.0 / 2.0
    return round(math.fabs(area),6)
if (__name__ == "__main__"):
    data = "121.0471520864411,31.386706995286254;121.04787245877561,31.386691977694678;121.04786412369027,31.3874473474171;121.04715275596361,31.387462177763332"

    print(CalculatePolygonArea0(data))