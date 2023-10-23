#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "�ҵ�ҳ��"

from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
from wisbuild_script.wisbuild.page_object.my.user_info.user_setting_Page import *
import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# noinspection PyTypeChecker
class My_page(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        unittest.TestCase.__init__(self)
        self.poco = poco

    # �ҵĲ˵�
    def my(self):
        self.poco(name="com.rh.hjz:id/menu_mine").click()

    # ���������Ϣ
    def user_info(self):
        self.poco(name="com.rh.hjz:id/iv_avatar").parent().click()  # ���ͷ��ؼ����ڸ���
        user_info = self.poco(name="com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("������Ϣ" in user_info)
        except ValueError:
            print("δ���������Ϣ")

    # ����Ǯ��
    def wallet(self):
        self.poco(name="com.rh.hjz:id/tv_title", text='Ǯ��').click()
        wallet = self.poco(name="com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("�ҵ�Ǯ��" in wallet)
        except ValueError:
            print("����Ǯ��ʧ��")

    # ����֤������
    def documents(self):
        self.poco(name="com.rh.hjz:id/tv_title", text='֤��').click()
        documents = self.poco(name="com.rh.hjz:id/tv_my_certificate").get_text()
        try:
            assert ("�ҵ�֤��" in documents)
        except ValueError:
            print("����֤��ʧ��")

    # �����豸����
    def equipment(self):
        self.poco(name="com.rh.hjz:id/tv_title", text='�豸').click()
        equipment = self.poco(name="com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("�豸����" in equipment)
        except ValueError:
            print("�����豸����ʧ��")

    # ���������ϵ��
    def emergency_contact(self):
        self.poco(name="com.rh.hjz:id/tv_title", text="������ϵ��").click()
        emergency_contact = self.poco(name="������ϵ��").get_text()
        try:
            assert ("������ϵ��" in emergency_contact)
        except ValueError:
            print("������ϵ���б�ʧ��")

    # ����
    def set(self):
        self.poco(name="com.rh.hjz:id/tv_title", text="����").click()
        set_up = self.poco(name="com.rh.hjz:id/constraint_title").child("com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("����" in set_up)
        except ValueError:
            print("��������ҳ��ʧ��")

    # �û���Ϣ
    def new_user_info(self):  # user_type: 0 �������û���1 ���������û�
        work_type = self.poco(name="com.rh.hjz:id/tv_type").get_text()
        certified = self.poco(name="com.rh.hjz:id/tv_certified").get_text()
        username = self.poco(name="com.rh.hjz:id/tv_name").get_text()
        user_heard = Template(r"\wisbuild_automation\wisbuild_script\wisbuild\page_object\my\image\iv_avatar.png")
        if "����" in work_type:
            print(work_type)
            if "δʵ����֤" in certified:
                print(certified)
                if assert_exists(user_heard, "�����û�ͷ��"):
                    print("�û��ǳƣ�" + username)
                    print("���û�Ϊ���û�")
        else:
            User_setting_page().sign_out()
            UserLogin().test1_login('13100000000', 288371)
            My_page().my()
            My_page().new_user_info()


if __name__ == '__main__':
    unittest.main()
