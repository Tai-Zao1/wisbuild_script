#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "项目列表用例"

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
        项目详情
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().clearapp()  # 清除缓存启动APP
            StartAPP().test1_tv_agree()  # 登录时确认指引
            UserLogin().test1_login('19730000000', 288371)  # 登录页面输入手机号验证码
            Worker_stats().project()
            List().proj_detail("环荣")
            Detail().proj_basic_info()
        finally:
            Tool().test2loggin_html()  # 生成测试报告

    def run_script_case2(devices):
        """
        项目概况
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().stopapp()  # 关闭进程后启动APP
            Worker_stats().project()
            List().proj_detail("环荣")
            Detail().proj_basic_info()
            Detail().proj_view("龙海建设", "10万平", "钢混", "36个月", "2022-03-31")
        finally:
            Tool().test2loggin_html()  # 生成测试报告

    def run_script_case3(devices):
        """
        项目位置
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().stopapp()  # 关闭进程后启动APP
            Worker_stats().project()
            List().proj_detail("环荣")
            Detail().proj_basic_info()
            Detail().area("上海市-上海-长宁区","长宁区仙霞西路888弄")
        finally:
            Tool().test2loggin_html()  # 生成测试报告


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.run_script_case1)
    devicestest().parallel(Verified.run_script_case2)
    devicestest().parallel(Verified.run_script_case3)