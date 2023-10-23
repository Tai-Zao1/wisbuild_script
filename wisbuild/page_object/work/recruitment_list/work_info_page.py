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

    def work_name(self):
        name = self.poco(name='com.rh.hjz:id/tv_project_name').get_text()
        print("招工标题：" + name)
        data = self.poco(name='com.rh.hjz:id/tv_date').get_text()
        print("发布时间：" + data)
        work_level2 = self.poco(name='com.rh.hjz:id/tv_sub_title').get_text()
        print("招工需要二级工种" + work_level2)
        proj_des = self.poco(name='com.rh.hjz:id/rv_list')
        proj_des_tag = proj_des.offspring('com.rh.hjz:id/tv_tag')
        # print(proj_des_tag.get_text())
        # print(len(proj_des_tag))
        # print(proj_des_tag.exists())
        if proj_des_tag.exists():
            i = 0
            while i < len(proj_des_tag):
                print('描述：' + proj_des_tag[i].get_text())
                i += 1
        else:
            raise SyntaxError('没有发现招工描述内容')
        address = self.poco(name='com.rh.hjz:id/tv_location').get_text()
        distance = self.poco(name='com.rh.hjz:id/tv_distance').get_text()
        print('招工所在地址：' + address + ',距离'+distance)
