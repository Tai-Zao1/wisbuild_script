#!/usr/bin/python
# -*-coding:GBK -*-
import os
import random
import sys
import unittest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class createPhone(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    #   拍照功能
    def moblie(self):
        for k in range(100):
            prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139"
                , "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                       "186", "187", "188", "189", "172", "176", "185"]

            phone = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
            return phone

if __name__ == "__main__":
    unittest.main()
