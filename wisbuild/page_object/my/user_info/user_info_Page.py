#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��������"

import sys
import datetime
from airtest.core.api import *
import unittest
import logging

from wisbuild_script.wisbuild.tool.permission import Permission
from wisbuild_script.wisbuild.tool.upload_pic import Upload_pic
from wisbuild_script.wisbuild.tool.work_type import Work_type

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class User_info_page(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # �޸�ͷ��
    def header(self, filename_url):
        header = self.poco(name="com.rh.hjz:id/constraint_image")
        header.click()
        cancel = self.poco(name="com.rh.hjz:id/tv_cancel")
        cancel.click()
        tittle = self.poco(name="com.rh.hjz:id/tv_title", text="����ͷ��")
        if len(tittle) == 1:
            print("�������ͷ��ҳ��")
        right = self.poco(name="com.rh.hjz:id/iv_right")
        right.click()
        md_md_content_layout = self.poco(name="com.rh.hjz:id/md_content_layout")
        if len(md_md_content_layout) == 1:
            print("�޸�ͷ��")
        Permission().source_pic(2)  # ���ֻ������ѡ��
        Permission().camera_permission()  # ȷ��Ȩ��
        Upload_pic().pic(filename_url)  # ѡ��ͷ���ļ�

    # �޸��û��ǳ�
    def nickname(self):
        nickname = self.poco(name="com.rh.hjz:id/tv_content")[0]
        print("��ǰ�û��ǳƣ�" + nickname.get_text())
        nickname.click()
        title = self.poco(name="com.rh.hjz:id/tv_title", text="�ǳ�����")
        if title.exists():
            delete = self.poco(name="com.rh.hjz:id/iv_cancel")
            delete.click()
            nickname2 = self.poco(name="com.rh.hjz:id/et_name")
            now = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d')
            nickname2.set_text("�Զ����޸�" + now)
            self.poco(name="com.rh.hjz:id/tv_right").click()
        else:
            print("δ����༭ҳ��")

    # �޸��û�����
    def work_type(self, work_type1):
        work_type = self.poco(name="com.rh.hjz:id/tv_content")[1]
        if work_type.get_text() == "����":
            work_type.click()
            # ֱ����ѡ��������
            Work_type().update_work_type("����, ���Ṥ, �̶���")
        else:
            work_type.click()
            choose = self.poco(name="com.rh.hjz:id/rv_choose_list")
            c_list = choose.offspring("com.rh.hjz:id/tv_name")
            # ɾ����ѡ����
            for x in c_list:
                c_name = choose.offspring("com.rh.hjz:id/tv_name").get_text()
                delete = c_list.sibling("com.rh.hjz:id/iv_remove")[0]
                delete.click()
                print("ɾ��ԭ���֣�" + c_name)
            # �޸��û�����
            Work_type().update_work_type(work_type1)



if __name__ == '__main__':
    unittest.main()
