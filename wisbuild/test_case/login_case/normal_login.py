#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "登录流程"

import sys
sys.path.append('F:/wisbuild_automation')

import threading
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import *
from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
import logging
from airtest.core.api import wake


curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Login(threading.Thread):

    def run_script_case1(devices):
        """
        正确手机号正确验证码
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)     # 获取设备信息
            wake()
            StartAPP().clearapp()       # 杀死并启动APP
            StartAPP().test1_tv_agree()     # 登录时确认指引
            UserLogin().test1_login(19720000001, 288371)     # 登录页面输入手机号验证码
        finally:
            Tool().test2loggin_html()       # 生成测试报告

    def run_error_code(devices):
        """
        正确手机号错误验证码
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)     # 获取设备信息
            wake()
            StartAPP().clearapp()       # 杀死并启动APP
            StartAPP().test1_tv_agree()     # 登录时确认指引
            UserLogin().test1_login(19720000001, 111111)     # 登录页面输入手机号验证码
        finally:
            Tool().test2loggin_html()       # 生成测试报告

    def run_error_mobile(devices):
        """
        错误手机号错误密码
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)     # 获取设备信息
            wake()
            StartAPP().clearapp()       # 杀死并启动APP
            StartAPP().test1_tv_agree()     # 登录时确认指引
            UserLogin().test1_login(10000000000, 111111)     # 登录页面输入手机号验证码
        finally:
            Tool().test2loggin_html()       # 生成测试报告


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Login.run_script_case1)
    devicestest().parallel(Login.run_error_code)
    devicestest().parallel(Login.run_error_mobile)
