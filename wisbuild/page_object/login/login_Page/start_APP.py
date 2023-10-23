#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��APP���ҽ�����ҳ"


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

    # ɱ��������APP
    def clearapp(self):
        clear_app("com.rh.hjz")
        start_app("com.rh.hjz")
        time.sleep(2)

    # ��ֹĿ��Ӧ�����豸�ϵ�����
    def stopapp(self):
        stop_app("com.rh.hjz")
        start_app("com.rh.hjz")
        time.sleep(2)

    # �ж��豸�Ƿ����Ļ
    def screenon(self):
        android = Android()
        if not android.is_screenon():
            wake()
        else:
            print('�豸��Ļ�Ѵ�')

    # ͬ��Э��
    def test1_tv_agree(self):
        # �ȵ����ͬ��
        self.poco(name="com.rh.hjz:id/tv_unagree").click()
        # ���ȥͬ��
        self.poco(name="com.rh.hjz:id/tv_agree", text="ȥͬ��").click()
        # ͬ��Э��
        self.poco(name="com.rh.hjz:id/tv_agree").click()
        sleep(0.5)

    # ��ͬ��Э��
    def test1_tv_unagree(self):
        # �ȵ����ͬ��
        self.poco(name="com.rh.hjz:id/tv_unagree").click()
        # ��ͬ��Э��
        self.poco(name="com.rh.hjz:id/tv_unagree", text="�˳�Ӧ��").click()
        sleep(0.5)

    # ����������������
    def test2_update_app(self):
        up = self.poco(name="com.rh.hjz:id/tv_update")  # ���°�ť
        if len(up) == 1:
            if str(up.get_text()) == "��������":
                self.poco(name="com.rh.hjz:id/iv_cancel").click()  # �رո��°�ť
                print("�н���������ȡ������")
            else:
                up.click()
                print("��ǿ������,���и���")
        else:
            print("���°汾��������")

    def test3_permission(self):
        permission_allow = self.poco(textMatches=".*����.*", touchable=True)
        if len(permission_allow) == 1:
            permission_allow.click()
            print("Ȩ������")
        else:
            return


if __name__ == '__main__':
    unittest.main()
