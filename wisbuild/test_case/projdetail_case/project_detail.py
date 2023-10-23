#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��Ŀ�б�����"

import threading


from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import *
from wisbuild_script.wisbuild.page_object.statistics.stats_Page.worker_stats_Page import *
from wisbuild_script.wisbuild.page_object.work.project_detail.proj_Info_Page import *
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.work.project_list.proj_list_Page import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Verified(threading.Thread):
    def run_script_case1(devices):
        """
        ��Ŀ����
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().clearapp()  # �����������APP
            StartAPP().test1_tv_agree()  # ��¼ʱȷ��ָ��
            UserLogin().test1_login('19730000000', 288371)  # ��¼ҳ�������ֻ�����֤��
            Worker_stats().project()
            List().proj_detail("����")
            Detail().proj_basic_info()
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���

    def run_script_case2(devices):
        """
        ��Ŀ�ſ�
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().stopapp()  # �رս��̺�����APP
            Worker_stats().project()
            List().proj_detail("����")
            Detail().proj_basic_info()
            Detail().proj_view("��������", "10��ƽ", "�ֻ�", "36����", "2022-03-31")
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���

    def run_script_case3(devices):
        """
        ��Ŀλ��
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
            wake()
            StartAPP().stopapp()  # �رս��̺�����APP
            Worker_stats().project()
            List().proj_detail("����")
            Detail().proj_basic_info()
            Detail().area("�Ϻ���-�Ϻ�-������","��������ϼ��·888Ū")
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.run_script_case1)
    devicestest().parallel(Verified.run_script_case2)
    devicestest().parallel(Verified.run_script_case3)