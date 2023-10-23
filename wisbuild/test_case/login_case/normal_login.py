#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��¼����"

import sys
sys.path.append('F:/wisbuild_automation')

import threading
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import *
from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
import logging
from airtest.core.api import wake


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Login(threading.Thread):

    def run_script_case1(devices):
        """
        ��ȷ�ֻ�����ȷ��֤��
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)     # ��ȡ�豸��Ϣ
            wake()
            StartAPP().clearapp()       # ɱ��������APP
            StartAPP().test1_tv_agree()     # ��¼ʱȷ��ָ��
            UserLogin().test1_login(19720000001, 288371)     # ��¼ҳ�������ֻ�����֤��
        finally:
            Tool().test2loggin_html()       # ���ɲ��Ա���

    def run_error_code(devices):
        """
        ��ȷ�ֻ��Ŵ�����֤��
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)     # ��ȡ�豸��Ϣ
            wake()
            StartAPP().clearapp()       # ɱ��������APP
            StartAPP().test1_tv_agree()     # ��¼ʱȷ��ָ��
            UserLogin().test1_login(19720000001, 111111)     # ��¼ҳ�������ֻ�����֤��
        finally:
            Tool().test2loggin_html()       # ���ɲ��Ա���

    def run_error_mobile(devices):
        """
        �����ֻ��Ŵ�������
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)     # ��ȡ�豸��Ϣ
            wake()
            StartAPP().clearapp()       # ɱ��������APP
            StartAPP().test1_tv_agree()     # ��¼ʱȷ��ָ��
            UserLogin().test1_login(10000000000, 111111)     # ��¼ҳ�������ֻ�����֤��
        finally:
            Tool().test2loggin_html()       # ���ɲ��Ա���


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Login.run_script_case1)
    devicestest().parallel(Login.run_error_code)
    devicestest().parallel(Login.run_error_mobile)
