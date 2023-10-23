#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "��Ŀ�б��ѯ"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Detail(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    def proj_basic_info(self):
        proj_name = self.poco(name="com.rh.hjz:id/tv_project_name").get_text()
        proj_type = self.poco(name="com.rh.hjz:id/tv_type").get_text()
        proj_state = self.poco(name="com.rh.hjz:id/tv_state").get_text()
        print(
            "��ǰ��Ŀ���ƣ�" + proj_name +
            "\n��Ŀ���ͣ�" + proj_type +
            "\n��Ŀ״̬��" + proj_state
        )

    #   ��Ŀ�ſ�
    def proj_view(self, contor_value, tv_area_value, structure_value, all_time_value, date_value):
        """
        contor_value���ܰ�����
        tv_area_value����Ŀ���
        structure_value����Ŀ�ṹ
        all_time_value����Ŀ����
        date_value������ʱ��
        """
        proj_area = self.poco(name="com.rh.hjz:id/tv_area_title")
        while proj_area.exists() != True:
            swipe([600, 1100], [600, 600])
        else:
            print("��ȫ��չʾ����Ŀ�ſ�")
        contor_value1 = self.poco(name="com.rh.hjz:id/tv_contractor_value").get_text()
        self.assertIn(contor_value, contor_value1, "�ܰ����Գɹ�")
        print(contor_value + " in " + contor_value1)
        area_value1 = self.poco(name="com.rh.hjz:id/tv_area_value").get_text()
        self.assertIn(tv_area_value, area_value1, "��Ŀ������Գɹ�")
        print(tv_area_value + " in " + area_value1)
        structure_value1 = self.poco(name="com.rh.hjz:id/tv_structure_value").get_text()
        self.assertIn(structure_value, structure_value1, "��Ŀ�ṹ���Գɹ�")
        print(structure_value + " in " + structure_value1)
        type_value = self.poco(name="com.rh.hjz:id/tv_type").get_text()
        type_value1 = self.poco(name="com.rh.hjz:id/tv_type_value").get_text()
        self.assertIn(type_value, type_value1, "��Ŀ�����Գɹ�")
        print(type_value + " in " + type_value1)
        all_time_value1 = self.poco(name="com.rh.hjz:id/tv_all_time_value").get_text()
        self.assertIn(all_time_value, all_time_value1, "��Ŀ���ڶ��Գɹ�")
        print(all_time_value + " in " + all_time_value1)
        date_value1 = self.poco(name="com.rh.hjz:id/tv_date_value").get_text()
        self.assertIn(date_value, date_value1, "��Ŀ����ʱ����Գɹ�")
        print(date_value + " in " + date_value1)
        state = self.poco(name="com.rh.hjz:id/tv_state").get_text()
        state_value = self.poco(name="com.rh.hjz:id/tv_state_value").get_text()
        self.assertIn(state, state_value, "��Ŀ��չ���Գɹ�")
        print(state + " in " + state_value)

    #   ��Ŀ���ڵ�
    def area(self, location_value, address_value):
        title = self.poco(name="com.rh.hjz:id/tv_title")
        while title.exists() == True:
            swipe([600, 1100], [600, 600])
        else:
            print("��ȫ��չʾ����Ŀ���ڵ�")
        location_value1 = self.poco(name="com.rh.hjz:id/tv_area_location_value").get_text()
        self.assertIn(location_value, location_value1, "����λ�ö��Գɹ�")
        print(location_value + " in " + location_value1)
        address_value1 = self.poco(name="com.rh.hjz:id/tv_address_value").get_text()
        self.assertIn(address_value, address_value1, "��Ŀ��ַ���Գɹ�")
        print(address_value + " in " + address_value1)


if __name__ == "__main__":
    unittest.main()
