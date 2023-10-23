#!/usr/bin/python
# -*-coding:GBK -*-
import os
import sys
from multiprocessing.context import Process
from airtest.core.android.adb import ADB
import unittest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class devicestest(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    def get_devices(self):
        '''获取设备'''
        devicesList = ADB().devices()
        print(devicesList)
        return devicesList

    def parallel(self, case):
        dev = []
        for i in devicestest().get_devices():
            dev.append(Process(target=case, args=(i[0],)))
        for p in dev:
            p.start()
        for p in dev:
            p.join()


if __name__ == "__main__":
    unittest.main()
