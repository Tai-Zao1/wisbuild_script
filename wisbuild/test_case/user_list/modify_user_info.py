#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "�޸��û���Ϣ"

import threading

from wisbuild_script.wisbuild.page_object.my.user_info.more_user_info import More_user_info
from wisbuild_script.wisbuild.page_object.my.user_info.my_Page import My_page
from wisbuild_script.wisbuild.page_object.my.user_info.user_info_Page import User_info_page
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import *
from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
from wisbuild_script.wisbuild.tool.upload_pic import Upload_pic

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

    def md_user_info(devives):
        """
        �޸ĸ�����Ϣ
        :param devices:
        :return:
        """
        Verified().login()
        Tool().test1loggin(devives)
        try:
            UserLogin().test1_login("16500000001", "288371")
            StartAPP().test3_permission()
            StartAPP().test2_update_app()
            My_page().my()
            My_page().user_info()
            User_info_page().header(
                r"F:\wisbuild_automation\wisbuild_script\wisbuild\image\header_image.png")  # �����ѡ��ͷ��
            Upload_pic().crop()  # ����ͷ��
            User_info_page().nickname()  # �޸��ǳ�
            User_info_page().work_type("װ��ľ��,�̶���,���߹�")  # �޸Ĺ���
            More_user_info().entrance()
            More_user_info().hometown('����', '����')
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest

    devicestest().parallel(Verified.login)
