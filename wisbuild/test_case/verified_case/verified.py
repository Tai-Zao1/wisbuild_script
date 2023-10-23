#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "ʵ����֤����"

import threading

from wisbuild_script.wisbuild.page_object.login.login_Page.login import UserLogin
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import StartAPP
from wisbuild_script.wisbuild.page_object.statistics.certification_Page.tobe_certified_Page import Certified
from wisbuild_script.wisbuild.tool.Generate_log import *
import logging
from airtest.core.api import wake

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Verified(threading.Thread):

    def run_script_case1(devices):
        """
        ʵ����֤ͨ��
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().clearapp()  # ɱ��������APP
            StartAPP().test1_tv_agree()  # ��¼ʱȷ��ָ��
            UserLogin().test1_login("", 288371)  # ��¼ҳ�������ֻ�����֤��
            Certified().tv_date_time()
            Certified().Verified_button()
            Certified().work_type("�ֽ")
            Certified().bar_title()
            Certified().Id_card_bottun("������")
            Certified().Id_card_bottun("������")
            Certified().tv_next_bottun()
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest

    devicestest().parallel(Verified.run_script_case1)
