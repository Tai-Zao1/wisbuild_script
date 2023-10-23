#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "�����˵�"

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

    # �����˵�
    def menu_work(self):
        menu_work = self.poco(name='com.rh.hjz:id/menu_work')
        menu_work.click()

    # �ҹ���
    def find_work(self):
        find_work = self.poco(name='com.rh.hjz:id/tv_left', text='�ҹ���')
        find_work.click()

    # ����
    def attendance(self):
        attendance = self.poco(name='com.rh.hjz:id/tv_left', text='����')
        attendance.click()

    # OA����
    def oa_approval(self):
        oa_approval = self.poco(name='com.rh.hjz:id/tv_left', text='OA����')
        oa_approval.click()


if __name__ == "__main__":
    unittest.main()
