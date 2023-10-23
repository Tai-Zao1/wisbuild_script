#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "工作菜单"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Work(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 工作菜单
    def menu_work(self):
        menu_work = self.poco(name='com.rh.hjz:id/menu_work')
        menu_work.click()

    # 找工作
    def find_work(self):
        find_work = self.poco(name='com.rh.hjz:id/tv_left', text='找工作')
        find_work.click()

    # 考勤
    def attendance(self):
        attendance = self.poco(name='com.rh.hjz:id/tv_left', text='考勤')
        attendance.click()

    # OA审批
    def oa_approval(self):
        oa_approval = self.poco(name='com.rh.hjz:id/tv_left', text='OA审批')
        oa_approval.click()


if __name__ == "__main__":
    unittest.main()
