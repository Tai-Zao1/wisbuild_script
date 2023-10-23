#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "�й��б�"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class To_hire(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # ����й�����
    def title(self):
        title = self.poco(name="com.rh.hjz:id/tb_ly").offspring(name="�й�")
        title.click()
        print('����й�title')

    # �й��б��й�tag
    def work_info(self, work_name):
        global work_name2
        work_name2 = self.poco(name='com.rh.hjz:id/tv_project_name', textMatches='.*' + work_name + '.*')
        while not work_name2.exists():
            print('δ�ҵ��й����Ի�������')
            swipe([500, 1800], [500, 1000])
            time.sleep(2)
        else:
            print('�ҵ����й���Ϣ��' + work_name2.get_text())
        return work_name2

    #   �й�����������Ϣ
    def work_level_2(self, work_level):
        work_level2 = work_name2.sibling('com.rh.hjz:id/tv_level_2')
        while not work_level2.exists():
            print("�й���Ϣδչʾȫ����������")
            swipe([500, 1800], [500, 1000])
        else:
            assert (work_level in work_level2.get_text())
            print("���й����蹤�֣�" + work_level2.get_text())

    #   �й���Ϣ��ǩ
    def work_tags(self, work_tag):
        work_tag2 = work_name2.sibling('com.rh.hjz:id/tv_project_tag')

        if not work_tag2.exists():
            print("δ�ҵ���Ӧtag")
        else:
            assert (work_tag in work_tag2.get_text())
            print("���й���ǩ��" + work_tag2.get_text())

    #  ��Ŀ���ڳ���
    def city_name(self, city):
        city_name = work_name2.sibling('com.rh.hjz:id/tv_location')
        while not city_name.exists():
            print("�й���Ϣδչʾȫ����������")
            swipe([500, 1800], [500, 1000])
        if city in city_name:
            print("���й����ڳ��У�" + city_name.get_text())
        data = work_name2.sibling('com.rh.hjz:id/tv_date')
        print('���й��������ڣ�' + data.get_text())

    #   �й��������û���Ϣ
    def publish_user(self, userName, userTag):
        publish_info = work_name2.sibling('android.view.ViewGroup')
        publish_user_name = publish_info.child('com.rh.hjz:id/tv_publish_user_name').get_text()
        user_tag = publish_info.child('com.rh.hjz:id/tv_user_tag').get_text()
        assert (userName in publish_user_name)
        print("���й������ߣ�" + publish_user_name)
        assert (userTag in user_tag)
        print('���й���Ա����' + user_tag)
