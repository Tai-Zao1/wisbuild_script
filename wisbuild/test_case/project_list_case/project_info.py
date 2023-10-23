#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "项目列表用例"

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
        项目信息查询
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().clearapp()  # 杀死并启动APP
            StartAPP().test1_tv_agree()  # 登录时确认指引
            UserLogin().test1_login('19730000000', 288371)  # 登录页面输入手机号验证码
            List().proj_info("环荣", '在建', '住宅')
        finally:
            Tool().test2loggin_html()  # 生成测试报告

    def run_script_case2(devices):
        """
        切换项目
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().stopapp()  # 终止并启动APP
            Worker_stats().project()
            List().change_proj()
        finally:
            Tool().test2loggin_html()  # 生成测试报告

    def run_script_case3(devices):
        """
        项目状态筛选
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().stopapp()  # 终止并启动APP
            Worker_stats().project()
            Filter().status("筹备")
        finally:
            Tool().test2loggin_html()  # 生成测试报告

    def run_script_case4(devices):
        """
        项目类型筛选
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().stopapp()  # 终止并启动APP
            Worker_stats().project()
            Filter().type("道路")
        finally:
            Tool().test2loggin_html()  # 生成测试报告





if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.run_script_case1)
    devicestest().parallel(Verified.run_script_case2)
    devicestest().parallel(Verified.run_script_case1)
    devicestest().parallel(Verified.run_script_case4)