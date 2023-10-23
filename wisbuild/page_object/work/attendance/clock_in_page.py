#!/usr/bin/python
# -*- encoding = GBK -*-
__author__ = "慧建驻"
__tittle__ = '打卡页面'

import unittest


class attendance(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco
        unittest.TestCase.__init__(self)
        self.poco = poco
