#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "���û���������"

import threading
from wisbuild_script.wisbuild.page_object.work.recruitment_list.create_work_page import Create_work
from wisbuild_script.wisbuild.page_object.work.work_list.work_page import Work
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

        StartAPP().screenon()
        StartAPP().clearapp()  # �����������APP
        StartAPP().test1_tv_agree()  # ��¼ʱȷ��ָ��

    def create_work(devices):
        """
        �й���Ϣչʾ
        :param devices:
        :return:
        """
        Verified().login()
        Tool().test1loggin(devices)  # ��ȡ�豸��Ϣ
        try:
            UserLogin().test1_login('16500000001', 288371)  # ��¼ҳ�������ֻ�����֤��
            StartAPP().test3_permission()
            StartAPP().test2_update_app()
            Work().menu_work()
            Work().find_work()
            Create_work().create_entrance(3)
            Create_work().publish_work('������Է', '����С��/�ӹ�/�����/��ĥ/ѧͽ')
            Create_work().c_info()
            Create_work().other_tag('��Ա����', '����')
            Create_work().other_tag('����', '1-2��')
            Create_work().other_tag('����', 'Ԫ/��', 200)
            Create_work().other_tag('���㷽ʽ', '�ս�')
            Create_work().other_tag('������', '�й�')
            Create_work().other_tag('������', 'С��')
            Create_work().other_tag('����', '��ס')
            Create_work().other_tag('����', '����')
            Create_work().other_tag('����', '�籣')
            Create_work().other_tag('����Ҫ��', '���������ֻ�')
            Create_work().other_tag('����Ҫ��', '������')
            Create_work().other_tag('����Ҫ��', '���ѵ�����')
            Create_work().tag_confirm()
            Create_work().publish()
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest

    devicestest().parallel(Verified.create_work)
