#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "待认证页面"

import os
import sys
import re
import time
from airtest.core.api import *
import unittest
import logging
from wisbuild_script.wisbuild.tool.permission import Permission
from wisbuild_script.wisbuild.tool.Camera import Camera

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class Certified(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 当前日期
    def tv_date_time(self):
        mydate = re.sub("-", '.', time.strftime('%Y-%m-%d', time.localtime(time.time())))
        print('当前日期：' + mydate)
        data = self.poco(name="com.rh.hjz:id/tv_date_time").get_text()
        if mydate in data:
            print(mydate + "in" + data)
        else:
            print(mydate + "not in " + data)

    # 实名认证按钮
    def Verified_button(self):
        tv_verified = self.poco(name="com.rh.hjz:id/tv_auth")
        if len(tv_verified) == 1:
            print("该用户未实名认证")
            tv_verified.click()
        else:
            print("该用户已实名认证，无需认证")

    #   选择工种
    def work_type(self, work_name):
        self.poco(text=work_name).click()
        print("选择的工种是" + work_name)
        self.poco(name="com.rh.hjz:id/tv_next").click()

    #   人脸拍照
    def bar_title(self):
        self.poco(name="com.rh.hjz:id/tv_know").click()
        self.poco(name="com.rh.hjz:id/bg_scan").click()
        Permission().camera_permission()
        Camera().Camera()

    #   上传身份证
    def Id_card_bottun(self, Idtype):
        if Idtype == "人像面":
            self.poco(name="com.rh.hjz:id/iv_cid_1").click()
            Permission().source_window(2)
            Permission().camera_permission()
            Camera().Id_card(Idtype)
        elif Idtype == "国徽面":
            self.poco(name="com.rh.hjz:id/iv_cid_2").click()
            Permission().source_window(2)
            Permission().camera_permission()
            Camera().Id_card(Idtype)
        else:
            print("没有该类型")

    def tv_next_bottun(self):
        self.poco(name="com.rh.hjz:id/tv_next").click()
        real_name = self.poco(name="com.rh.hjz:id/tv_pre_real_name").get_text()
        if real_name == "认证通过":
            print("认证通过")
        else:
            print("认证失败")


if __name__ == "__main__":
    unittest.main()
