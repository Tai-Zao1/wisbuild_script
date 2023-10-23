#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "招工列表"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class To_hire(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 点击招工标题
    def title(self):
        title = self.poco(name="com.rh.hjz:id/tb_ly").offspring(name="招工")
        title.click()
        print('点击招工title')

    # 招工列表招工tag
    def work_info(self, work_name):
        global work_name2
        work_name2 = self.poco(name='com.rh.hjz:id/tv_project_name', textMatches='.*' + work_name + '.*')
        while not work_name2.exists():
            print('未找到招工尝试滑动查找')
            swipe([500, 1800], [500, 1000])
            time.sleep(2)
        else:
            print('找到该招工信息：' + work_name2.get_text())
        return work_name2

    #   招工二级工种信息
    def work_level_2(self, work_level):
        work_level2 = work_name2.sibling('com.rh.hjz:id/tv_level_2')
        while not work_level2.exists():
            print("招工信息未展示全，继续滑动")
            swipe([500, 1800], [500, 1000])
        else:
            assert (work_level in work_level2.get_text())
            print("该招工所需工种：" + work_level2.get_text())

    #   招工信息标签
    def work_tags(self, work_tag):
        work_tag2 = work_name2.sibling('com.rh.hjz:id/tv_project_tag')

        if not work_tag2.exists():
            print("未找到对应tag")
        else:
            assert (work_tag in work_tag2.get_text())
            print("该招工标签：" + work_tag2.get_text())

    #  项目所在城市
    def city_name(self, city):
        city_name = work_name2.sibling('com.rh.hjz:id/tv_location')
        while not city_name.exists():
            print("招工信息未展示全，继续滑动")
            swipe([500, 1800], [500, 1000])
        if city in city_name:
            print("该招工所在城市：" + city_name.get_text())
        data = work_name2.sibling('com.rh.hjz:id/tv_date')
        print('该招工发布日期：' + data.get_text())

    #   招工发布者用户信息
    def publish_user(self, userName, userTag):
        publish_info = work_name2.sibling('android.view.ViewGroup')
        publish_user_name = publish_info.child('com.rh.hjz:id/tv_publish_user_name').get_text()
        user_tag = publish_info.child('com.rh.hjz:id/tv_user_tag').get_text()
        assert (userName in publish_user_name)
        print("该招工发布者：" + publish_user_name)
        assert (userTag in user_tag)
        print('该招工人员类型' + user_tag)
