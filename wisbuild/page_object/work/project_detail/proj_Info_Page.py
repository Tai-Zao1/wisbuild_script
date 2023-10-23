#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "项目列表查询"

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
            "当前项目名称：" + proj_name +
            "\n项目类型：" + proj_type +
            "\n项目状态：" + proj_state
        )

    #   项目概况
    def proj_view(self, contor_value, tv_area_value, structure_value, all_time_value, date_value):
        """
        contor_value；总包名称
        tv_area_value：项目面积
        structure_value：项目结构
        all_time_value：项目工期
        date_value：开工时间
        """
        proj_area = self.poco(name="com.rh.hjz:id/tv_area_title")
        while proj_area.exists() != True:
            swipe([600, 1100], [600, 600])
        else:
            print("已全部展示出项目概况")
        contor_value1 = self.poco(name="com.rh.hjz:id/tv_contractor_value").get_text()
        self.assertIn(contor_value, contor_value1, "总包断言成功")
        print(contor_value + " in " + contor_value1)
        area_value1 = self.poco(name="com.rh.hjz:id/tv_area_value").get_text()
        self.assertIn(tv_area_value, area_value1, "项目面积断言成功")
        print(tv_area_value + " in " + area_value1)
        structure_value1 = self.poco(name="com.rh.hjz:id/tv_structure_value").get_text()
        self.assertIn(structure_value, structure_value1, "项目结构断言成功")
        print(structure_value + " in " + structure_value1)
        type_value = self.poco(name="com.rh.hjz:id/tv_type").get_text()
        type_value1 = self.poco(name="com.rh.hjz:id/tv_type_value").get_text()
        self.assertIn(type_value, type_value1, "项目类别断言成功")
        print(type_value + " in " + type_value1)
        all_time_value1 = self.poco(name="com.rh.hjz:id/tv_all_time_value").get_text()
        self.assertIn(all_time_value, all_time_value1, "项目工期断言成功")
        print(all_time_value + " in " + all_time_value1)
        date_value1 = self.poco(name="com.rh.hjz:id/tv_date_value").get_text()
        self.assertIn(date_value, date_value1, "项目开工时间断言成功")
        print(date_value + " in " + date_value1)
        state = self.poco(name="com.rh.hjz:id/tv_state").get_text()
        state_value = self.poco(name="com.rh.hjz:id/tv_state_value").get_text()
        self.assertIn(state, state_value, "项目进展断言成功")
        print(state + " in " + state_value)

    #   项目所在地
    def area(self, location_value, address_value):
        title = self.poco(name="com.rh.hjz:id/tv_title")
        while title.exists() == True:
            swipe([600, 1100], [600, 600])
        else:
            print("已全部展示出项目所在地")
        location_value1 = self.poco(name="com.rh.hjz:id/tv_area_location_value").get_text()
        self.assertIn(location_value, location_value1, "所在位置断言成功")
        print(location_value + " in " + location_value1)
        address_value1 = self.poco(name="com.rh.hjz:id/tv_address_value").get_text()
        self.assertIn(address_value, address_value1, "项目地址断言成功")
        print(address_value + " in " + address_value1)


if __name__ == "__main__":
    unittest.main()
