#!/usr/bin/python
# -*-coding:GBK -*-
import os
import sys
import unittest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Permission(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    def camera_permission(self):
        allow = self.poco("com.android.permissioncontroller:id/permission_allow_button")
        if len(allow) == 1:
            allow_text = self.poco("com.android.permissioncontroller:id/permission_allow_button").get_text()
            permission_message = self.poco(name="com.android.permissioncontroller:id/permission_message").get_text()
            print(permission_message + "==>" + allow_text)
            allow.click()
        else:
            print("����ȷ��ϵͳȨ��")

    # ��Ƭ��Դ
    def source_pic(self, source):
        if source == 1:
            self.poco(name="com.rh.hjz:id/tv_camera").click()
            print("ѡ������")
        elif source == 2:
            self.poco(name="com.rh.hjz:id/tv_images").click()
            print("ѡ�����")
        else:
            print("��ѡ����Դ")


if __name__ == "__main__":
    unittest.main()
