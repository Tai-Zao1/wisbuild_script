#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��Ŀ�б�����"

import logging
import threading
from wisbuild_script.wisbuild.page_object.login.login_Page.login import UserLogin
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import StartAPP
from wisbuild_script.wisbuild.page_object.statistics.stats_Page.worker_stats_Page import Worker_stats
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.work.project_list.proj_list_Page import List
from wisbuild_script.wisbuild.page_object.work.project_list.proj_filter_Page import Filter


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Verified(threading.Thread):
    def run_script_case1(devices):
        """
        ��Ŀ��Ϣ��ѯ
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().clearapp()  # ɱ��������APP
            StartAPP().test1_tv_agree()  # ��¼ʱȷ��ָ��
            UserLogin().test1_login('19730000000', 288371)  # ��¼ҳ�������ֻ�����֤��
            List().proj_info("����", '�ڽ�', 'סլ')
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���

    def run_script_case2(devices):
        """
        �л���Ŀ
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().stopapp()  # ��ֹ������APP
            Worker_stats().project()
            List().change_proj()
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���

    def run_script_case3(devices):
        """
        ��Ŀ״̬ɸѡ
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().stopapp()  # ��ֹ������APP
            Worker_stats().project()
            Filter().status("�ﱸ")
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���

    def run_script_case4(devices):
        """
        ��Ŀ����ɸѡ
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().stopapp()  # ��ֹ������APP
            Worker_stats().project()
            Filter().type("��·")
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���





if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.run_script_case1)
    devicestest().parallel(Verified.run_script_case2)
    devicestest().parallel(Verified.run_script_case1)
    devicestest().parallel(Verified.run_script_case4)