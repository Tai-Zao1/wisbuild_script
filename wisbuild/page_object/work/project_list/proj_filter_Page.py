#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "筛选控件"

import sys
import re
from airtest.core.api import *
import unittest
import logging

from wisbuild_script.wisbuild.tool.work_type import Work_type

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Filter(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 地区查询目前只支持二级地区全部
    def area(self, city_name):
        area = self.poco(name="com.rh.hjz:id/tv_area")
        area.click()
        city = self.poco(name="com.rh.hjz:id/tv_name", text=city_name).exists()
        while city != True:
            city = self.poco(name="com.rh.hjz:id/tv_name", text=city_name).exists()
            swipe([200, 900], [200, 500])
        else:
            print("找到该元素")
            #   点击输入元素
            self.poco(text=city_name).click()
            self.poco(text="全部").click()

    #   状态查询
    def status(self, status_name):
        self.poco(name="com.rh.hjz:id/tv_state").click()
        self.poco(text=status_name).click()
        for proj_process in self.poco(name="com.rh.hjz:id/tv_project_process"):
            assert_equal(proj_process.get_text(), status_name, "筛选状态正确")
            name = proj_process.sibling("com.rh.hjz:id/tv_project_name")
            print(name.get_text() + ": state" + proj_process.get_text())

    #   类型查询
    def type(self, typename):
        self.poco(name="com.rh.hjz:id/tv_type").click()
        self.poco(text=typename).click()
        for proj_type in self.poco(name="com.rh.hjz:id/tv_project_type"):
            assert_equal(typename, proj_type.get_text(), "筛选状态正确")
            name = proj_type.sibling("com.rh.hjz:id/tv_project_name")
            print(name.get_text() + ": type" + proj_type.get_text())

    # 二级工种筛选
    def level2work(self, levelwork_name):
        levelwork_name = levelwork_name
        levelwork = self.poco(name='com.rh.hjz:id/tv_name', textMatches='.*' + levelwork_name + '.*')
        while not levelwork.exists():
            swipe([700, 2000], [700, 1000])
        else:
            levelwork.click()
            self.poco(name="com.rh.hjz:id/tv_right", text="确认").click()

    # 人员筛选
    def tv_tag(self, i):
        tv_tag_list = ['全部', '未填写', '个人', '班组', '劳务', '分包']
        tv_tag = self.poco(name='com.rh.hjz:id/tv_tag')
        tv_tag.click()
        tag_name = self.poco(name='com.rh.hjz:id/tv_item', text=tv_tag_list[i])
        tag_name.click()

    def tv_sort(self, i):
        tv_sort_list = ['最新发布', '距离最近']
        tv_sort = self.poco(name='com.rh.hjz:id/tv_sort')
        tv_sort.click()
        sort_name = self.poco(name="com.rh.hjz:id/tv_item", text=tv_sort_list[i])
        sort_name.click()


if __name__ == "__main__":
    unittest.main()
