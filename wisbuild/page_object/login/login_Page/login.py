#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��½ҳ��"

import os
import sys
from airtest.core.api import *
import time
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from wisbuild_script.wisbuild.tool.Mobile_Phone import createPhone

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class UserLogin(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ��½
    def test1_login(self, mobile=None, code=None):  # type :1 = ���̣߳��Զ���ȡ�� ��2 =���̣߳��ֶ������˺����룩
        time.sleep(5)
        login_text = \
            self.poco(name="com.rh.hjz:id/tv_explain").attr("text")
        assert_equal(login_text, "��¼���ɲ鿴���ڼ�¼���������㣬��Ŀ��̬״̬����Ϣ����ʱ�������½���", '�жϵ�¼ҳ������')
        code_login = self.poco(name="com.rh.hjz:id/tv_mobile_code_login")
        if len(code_login) == 1:
            print("δ��¼->���е�¼����")
            if str(mobile) != "":
                self.poco(name="com.rh.hjz:id/et_mobile").set_text(mobile)
                print("�����ֻ���:" + str(mobile))
            else:
                mobile1= str(createPhone().moblie())
                self.poco(name="com.rh.hjz:id/et_mobile").set_text(mobile1)
                print("��������ֻ���:" + str(mobile1))
            self.poco(name="com.rh.hjz:id/et_verify_code").set_text(code)
            print("������֤�룺" + str(code))
            agreement_button = self.poco(name="com.rh.hjz:id/tv_agreement_explain")
            if len(agreement_button) == 1:
                self.poco(name="com.rh.hjz:id/ck_agree").click()
                print("���ȷ��Э��")
            else:
                print("��ȷ��Э��")
            self.poco(name="com.rh.hjz:id/tv_mobile_login").click()
            snapshot(msg="��¼��ͼ")
            print("�����¼��ť")
        else:
            print("�ѵ�¼->����Ҫ�ٴε�¼")


if __name__ == '__main__':
    unittest.main()
