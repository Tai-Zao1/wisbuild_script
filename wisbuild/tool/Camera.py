#!/usr/bin/python
# -*-coding:GBK -*-
import os
import sys
import unittest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Camera(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    #   拍照功能
    def Camera(self):
        photograph_button = self.poco(name="com.rh.hjz:id/capture_layout").child("android.view.View")[1]
        photograph_button.click()
        confirm_button = self.poco(name="com.rh.hjz:id/capture_layout").child("android.view.View")[1]
        confirm_button.click()
        self.poco(name="com.rh.hjz:id/menu_crop").click()

    #   选择照片
    def Id_card(self, type):
        self.poco(name="com.rh.hjz:id/ps_tv_title").click()
        self.poco(textMatches="证件.*").click()
        if type == "人像面":
            self.poco(name="com.rh.hjz:id/tvCheck")[-1].click()
        elif type == "国徽面":
            self.poco(name="com.rh.hjz:id/tvCheck")[-2].click()
        elif type == "银行卡":
            self.poco(name="com.rh.hjz:id/tvCheck")[-3].click()
        else:
            print("没有记录该照片类型")
        self.poco(name="com.rh.hjz:id/ps_tv_complete").click()
        self.poco(name="com.rh.hjz:id/menu_crop").click()
        if type == "人像面":
            self.poco(name="com.rh.hjz:id/iv_retry_update_1").wait_for_appearance()
            print("人像面上传成功")
        elif type == "国徽面":
            self.poco(name="com.rh.hjz:id/iv_retry_update_2").wait_for_appearance()
            print("国徽面上传成功")

if __name__ == "__main__":
    unittest.main()
