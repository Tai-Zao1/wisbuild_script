#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "���û���������"

import threading
from wisbuild_script.wisbuild.page_object.work.recruitment_list.to_hire_page import To_hire
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

    def run_script_case1(devices):
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
            To_hire().title()
            To_hire().work_info('�Զ�������')
            To_hire().work_level_2('�깤/�ڹ�/��/�罬��/����')
            To_hire().work_tags('11-20�� | �깤�� | ���� | �� | С�� | ��ס | ���� | �籣 | �Ͳ� | ���²��� | ���������ֻ� | ������ | רҵʦ�� | ���ѵ�����')
            To_hire().city_name('����')
            To_hire().publish_user('ƻ��13', '����')
        finally:
            Tool().test2loggin_html()  # ���ɲ��Ա���


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.run_script_case1)
