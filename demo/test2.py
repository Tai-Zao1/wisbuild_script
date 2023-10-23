# batVoltage = 3955  # 电压
# gpsLongitude = 121028568  # 经度
# gpsLatitude = 31232281  # 纬度
#
# electric = (batVoltage - 3400) / (4350 - 3400) * 100  # 电量百分比
# long1 = str(gpsLongitude)[:3]
# long2 = str(gpsLongitude)[3:]
# lat1 = str(gpsLatitude)[:2]
# lat2 = str(gpsLatitude)[2:]
# gpslong = int(long1) + int(long2) / 10000 / 60
# gpslat = int(lat1) + int(lat2) / 10000 / 60
# print(electric, gpslong, gpslat)



import random
for i in range(38):
    print(random.randint(5000,20000))