#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "打开APP并且进入首页"


import sys
from airtest.core.api import *
import unittest
import logging
from airtest.core.android import Android
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)



logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class StartAPP(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 杀死并启动APP
    def clearapp(self):
        clear_app("com.rh.hjz")
        start_app("com.rh.hjz")
        time.sleep(2)

    # 终止目标应用在设备上的运行
    def stopapp(self):
        stop_app("com.rh.hjz")
        start_app("com.rh.hjz")
        time.sleep(2)

    # 判断设备是否打开屏幕
    def screenon(self):
        android = Android()
        if not android.is_screenon():
            wake()
        else:
            print('设备屏幕已打开')

    # 同意协议
    def test1_tv_agree(self):
        # 先点击不同意
        self.poco(name="com.rh.hjz:id/tv_unagree").click()
        # 点击去同意
        self.poco(name="com.rh.hjz:id/tv_agree", text="去同意").click()
        # 同意协议
        self.poco(name="com.rh.hjz:id/tv_agree").click()
        sleep(0.5)

    # 不同意协议
    def test1_tv_unagree(self):
        # 先点击不同意
        self.poco(name="com.rh.hjz:id/tv_unagree").click()
        # 不同意协议
        self.poco(name="com.rh.hjz:id/tv_unagree", text="退出应用").click()
        sleep(0.5)

    # 处理升级弹窗问题
    def test2_update_app(self):
        up = self.poco(name="com.rh.hjz:id/tv_update")  # 更新按钮
        if len(up) == 1:
            if str(up.get_text()) == "立即更新":
                self.poco(name="com.rh.hjz:id/iv_cancel").click()  # 关闭更新按钮
                print("有建议升级，取消更新")
            else:
                up.click()
                print("有强制升级,进行更新")
        else:
            print("无新版本更新升级")

    def test3_permission(self):
        permission_allow = self.poco(textMatches=".*允许.*", touchable=True)
        if len(permission_allow) == 1:
            permission_allow.click()
            print("权限允许")
        else:
            return


if __name__ == '__main__':
    unittest.main()
