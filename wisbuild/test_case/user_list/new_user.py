#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "���û���������"

import threading
from wisbuild_script.wisbuild.page_object.my.user_info.my_Page import My_page
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import *
from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
from wisbuild_script.wisbuild.page_object.my.user_info.user_info_Page import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Verified(threading.Thread):
    def login(self):
        """
        ��ʼ����¼
        :param devices:
        :return:
        """
        wake()
        StartAPP().clearapp()  # �����������APP
        StartAPP().test1_tv_agree()  # ��¼ʱȷ��ָ��

    def run_script_case1(devices):
        """
        ���û�������Ϣ
        :param devices:
        :return:
        """
        Verified().login()
        Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
        try:
            UserLogin().test1_login('', 288371)  # ��¼ҳ�������ֻ�����֤��
            StartAPP().test3_permission()
            StartAPP().test2_update_app()
            My_page().my()
            My_page().new_user_info()
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.login)

