#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��Ŀ�б�ҳ��"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class List(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # �л���Ŀ
    def change_proj(self):
        change_name = self.poco(name="com.rh.hjz:id/tv_change")
        if change_name.exists() == True:
            toggle_proj = change_name.sibling('com.rh.hjz:id/tv_project_name').get_text()
            print("���л���Ŀ��" + toggle_proj)
            change_name[0].click()
            sleep(2)
            home_proj = self.poco(name="com.rh.hjz:id/tv_project").get_text()
            if home_proj == toggle_proj:
                print("�л��ɹ�")
            else:
                print("�л�ʧ��")
        else:
            print("û�п��л���Ŀ")

    # �ж���Ŀ��Ϣ
    def proj_info(self, projname, proj_state, proj_type):
        proj_name = self.poco(textMatches=projname + ".*")
        proj_state1 = proj_name.sibling("com.rh.hjz:id/tv_project_process").get_text()
        assert_equal(proj_state, proj_state1, "��Ŀ״̬������")
        print("��Ŀ״̬����")
        proj_type1 = proj_name.sibling("com.rh.hjz:id/tv_project_type").get_text()
        assert_equal(proj_type, proj_type1, "��Ŀ���Ͳ�����")
        print("��Ŀ���ͳ���")

    # ���������Ŀ����
    def proj_detail(self, projname):
        proj_name = self.poco(textMatches=".*" + projname + ".*")
        while proj_name.exists() == False:
            swipe([600, 1500], [600, 500])
        else:
            proj_name.click()
            print("������Ŀ����: "+proj_name.get_text())


if __name__ == "__main__":
    unittest.main()
