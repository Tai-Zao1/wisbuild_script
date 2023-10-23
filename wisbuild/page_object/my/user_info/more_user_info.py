#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "�����������"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class More_user_info(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ���������Ϣ���
    def entrance(self):
        more_entrance = self.poco(name="com.rh.hjz:id/tv_content")[3]
        more_entrance.click()

    # �޸ļ���
    def hometown(self, province_name, city_name):
        hometown = self.poco(name="com.rh.hjz:id/tv_content")[0]
        self.poco(name="com.rh.hjz:id/tv_title", text="����").click()
        province = self.poco(textMatches='.?' + province_name + '.?')
        while not province.exists():
            swipe([600, 2000], [600, 500])
        else:
            province.click()
            city = self.poco(textMatches='.?' + city_name + '.?')
            while not city.exists():
                swipe([600, 2000], [600, 500])
            else:
                city.click()
        self.poco(name='com.rh.hjz:id/tv_right', text='���').click()
        print("�޸��û����������������Ϣ��" + hometown.get_text())

    # �޸�����ʱ��
    def entry_time(self):
        self.poco(name="com.rh.hjz:id/tv_title", text="����ʱ��").click()


if __name__ == '__main__':
    unittest.main()
