#!/user/bin/python
# -*- encoding=GBK -*-

__author__ = "�۽�פ"
__title__ = "��֯�ܹ�"

import os
import sys
from airtest.core.api import *
import time
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Company(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ��˾����
    def company_name(self, company_name):
        name = self.poco(name='com.rh.hjz:id/tv_name')
        companyName = name.get_text()
        if company_name not in companyName:
            print("��˾�����жϴ���")
        else:
            name.click()
        return companyName

    # ��˾����
    def company_detail(self, companyName):
        detail_name = self.poco(name="com.rh.hjz:id/tv_company_name").get_text()
        assert_true(companyName == detail_name)
        # ���������Ա���ж��Ƿ���Խ���Ա������
        self.poco(name='com.rh.hjz:id/tv_role_name').click()
        employee_info = self.poco(name='com.rh.hjz:id/recycler_list')
        if employee_info.exists():
            self.poco(name="com.rh.hjz:id/iv_back").click()
        else:
            print("����鿴������ԱԱ���������")
        print('��˾���ڵأ�' + self.poco(name='com.rh.hjz:id/tv_area_value').get_text())
        print('��˾��ҵ���ͣ�' + self.poco(name='com.rh.hjz:id/tv_profession_value').get_text())

    # �˳���ҵ
    def company_exit(self, status):
        self.poco(name="com.rh.hjz:id/bt_exit").click()
        if status == 1:
            tv_confirm = self.poco(name='com.rh.hjz:id/tv_confirm')
            tv_confirm.click()
            print('�����' + tv_confirm.get_text())
        else:
            tv_cancel = self.poco(name='com.rh.hjz:id/tv_cancel')
            tv_cancel.click()
            print('�����' + tv_cancel.get_text())

    # ��֯�ܹ�
    def organization(self):
        organization_name = self.poco(name= 'com.rh.hjz:id/tv_organization_name')
        assert_true(organization_name.exists())
        organization_name.click()
        print('������룺'+organization_name.get_text())
