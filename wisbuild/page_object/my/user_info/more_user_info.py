#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "更多个人设置"

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

    # 更多个人信息入口
    def entrance(self):
        more_entrance = self.poco(name="com.rh.hjz:id/tv_content")[3]
        more_entrance.click()

    # 修改籍贯
    def hometown(self, province_name, city_name):
        hometown = self.poco(name="com.rh.hjz:id/tv_content")[0]
        self.poco(name="com.rh.hjz:id/tv_title", text="籍贯").click()
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
        self.poco(name='com.rh.hjz:id/tv_right', text='完成').click()
        print("修改用户籍贯结束，籍贯信息：" + hometown.get_text())

    # 修改入行时间
    def entry_time(self):
        self.poco(name="com.rh.hjz:id/tv_title", text="入行时间").click()


if __name__ == '__main__':
    unittest.main()
