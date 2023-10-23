#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "实名认证流程"

import threading

from wisbuild_script.wisbuild.page_object.login.login_Page.login import UserLogin
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import StartAPP
from wisbuild_script.wisbuild.page_object.statistics.certification_Page.tobe_certified_Page import Certified
from wisbuild_script.wisbuild.tool.Generate_log import *
import logging
from airtest.core.api import wake

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Verified(threading.Thread):

    def run_script_case1(devices):
        """
        实名认证通过
        :param devices:
        :return:
        """
        try:
            Tool().test1loggin(devices)  # 获取设备信息
            wake()
            StartAPP().clearapp()  # 杀死并启动APP
            StartAPP().test1_tv_agree()  # 登录时确认指引
            UserLogin().test1_login("", 288371)  # 登录页面输入手机号验证码
            Certified().tv_date_time()
            Certified().Verified_button()
            Certified().work_type("钢筋工")
            Certified().bar_title()
            Certified().Id_card_bottun("人像面")
            Certified().Id_card_bottun("国徽面")
            Certified().tv_next_bottun()
        finally:
            Tool().test2loggin_html()  # 生成测试报告


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest

    devicestest().parallel(Verified.run_script_case1)
