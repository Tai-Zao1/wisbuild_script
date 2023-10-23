#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "工人统计页面"

import sys
import re
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

class Worker_stats(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    #   进入项目列表
    def project(self):
        project_name = self.poco(name="com.rh.hjz:id/tv_project")
        print("当前已切换项目"+project_name.get_text())
        project_name.click()
        sleep(2)
        next_page = self.poco(text="项目列表").exists()
        if  next_page == True:
            print("进入项目列表")
            current_proj = self.poco(name="com.rh.hjz:id/tv_project_name")[0].get_text()
            assert_equal(current_proj,project_name.get_text(),"当前已切换项目不成立")
        else:
            print("操作失败")

    #   工人统计模块日期切换
    def choose_day(self, data):     # -1:更多, 30:本月, 7:近七天, 1:昨天
        if data == -1:
            day = self.poco(name="com.rh.hjz:id/tv_more")
            day.click()
            print("当前选中日期"+day.get_text())
        elif data == 30:
            day_30 = self.poco(name="com.rh.hjz:id/day_30")
            day_30.click()
            print("当前选中日期"+day_30.get_text())
        elif data == 7:
            day_7 = self.poco(name="com.rh.hjz:id/day_7")
            day_7.click()
            print("当前选中日期"+day_7)
        elif data == 1:
            day_1 = self.poco(name="com.rh.hjz:id/tv_yesterday")
            day_1.click()
            print("当前选中日期"+day_1)
        else:
            print("默认日期 本月")

    #   工人统计模块薪资
    def worker_salary(self):
        need_salary_text = self.poco(name="com.rh.hjz:id/tv_title").get_text()
        need_salary = self.poco(name="com.rh.hjz:id/tv_all_salary").get_text()
        print(need_salary_text + ":" + need_salary)
        eff_att_day = self.poco(name="com.rh.hjz:id/tv_arrival").get_text()
        eff_att_value = self.poco(name="com.rh.hjz:id/tv_arrival_value").get_text()
        print(eff_att_day + ":" + eff_att_value)
        surplus_salary = self.poco(name="com.rh.hjz:id/tv_surplus_salary").get_text()
        surplus_salary_value = self.poco(name="com.rh.hjz:id/tv_surplus_salary_value").get_text()
        print(surplus_salary + ":"+surplus_salary_value)






if __name__ == "__main__":
    unittest.main()
