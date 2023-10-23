#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "认证通过未加入项目统计页面"

import sys
import re
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Certified(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 当前日期
    def page_element(self):
        mydate = re.sub("-", '.', time.strftime('%Y-%m-%d', time.localtime(time.time())))
        print('当前日期：' + mydate)
        data = self.poco(name="com.rh.hjz:id/tv_date_time").get_text()
        if mydate in data:
            print(mydate + " in " + data)
        else:
            print(mydate + " not in " + data)
        print(self.poco(name="com.rh.hjz:id/tv_pre_real_name").get_text())
        print(self.poco(name="com.rh.hjz:id/tv_nums").get_text())

    def bottom_join(self):
        by_project = self.poco(name="com.rh.hjz:id/by_project").get_text()
        if by_project == "按项目加入":
            print("按钮文案" + by_project)
        bottom_join_child = self.poco(name="com.rh.hjz:id/bottom_join").child(name="android.widget.TextView").get_text()
        if bottom_join_child == "天天开工 ，洗手领钱":
            print("按钮描述：" + bottom_join_child)
        bottom_join = self.poco(name="com.rh.hjz:id/bottom_join")
        bottom_join.click()
        proj_list = self.poco(name="com.rh.hjz:id/recycler")
        if len(proj_list) == 1:
            print("进入项目列表")


if __name__ == "__main__":
    unittest.main()
