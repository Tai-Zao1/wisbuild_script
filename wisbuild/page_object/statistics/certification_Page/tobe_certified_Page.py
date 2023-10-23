#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "����֤ҳ��"

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

    # ��ǰ����
    def tv_date_time(self):
        mydate = re.sub("-", '.', time.strftime('%Y-%m-%d', time.localtime(time.time())))
        print('��ǰ���ڣ�' + mydate)
        data = self.poco(name="com.rh.hjz:id/tv_date_time").get_text()
        if mydate in data:
            print(mydate + "in" + data)
        else:
            print(mydate + "not in " + data)

    # ʵ����֤��ť
    def Verified_button(self):
        tv_verified = self.poco(name="com.rh.hjz:id/tv_auth")
        if len(tv_verified) == 1:
            print("���û�δʵ����֤")
            tv_verified.click()
        else:
            print("���û���ʵ����֤��������֤")

    #   ѡ����
    def work_type(self, work_name):
        self.poco(text=work_name).click()
        print("ѡ��Ĺ�����" + work_name)
        self.poco(name="com.rh.hjz:id/tv_next").click()

    #   ��������
    def bar_title(self):
        self.poco(name="com.rh.hjz:id/tv_know").click()
        self.poco(name="com.rh.hjz:id/bg_scan").click()
        Permission().camera_permission()
        Camera().Camera()

    #   �ϴ����֤
    def Id_card_bottun(self, Idtype):
        if Idtype == "������":
            self.poco(name="com.rh.hjz:id/iv_cid_1").click()
            Permission().source_window(2)
            Permission().camera_permission()
            Camera().Id_card(Idtype)
        elif Idtype == "������":
            self.poco(name="com.rh.hjz:id/iv_cid_2").click()
            Permission().source_window(2)
            Permission().camera_permission()
            Camera().Id_card(Idtype)
        else:
            print("û�и�����")

    def tv_next_bottun(self):
        self.poco(name="com.rh.hjz:id/tv_next").click()
        real_name = self.poco(name="com.rh.hjz:id/tv_pre_real_name").get_text()
        if real_name == "��֤ͨ��":
            print("��֤ͨ��")
        else:
            print("��֤ʧ��")


if __name__ == "__main__":
    unittest.main()
