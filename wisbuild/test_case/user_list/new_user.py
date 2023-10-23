#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "新用户个人详情"

import threading
from wisbuild_script.wisbuild.page_object.my.user_info.my_Page import My_page
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import *
from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
from wisbuild_script.wisbuild.page_object.my.user_info.user_info_Page import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Verified(threading.Thread):
    def login(self):
        """
        初始化登录
        :param devices:
        :return:
        """
        wake()
        StartAPP().clearapp()  # 清除缓存启动APP
        StartAPP().test1_tv_agree()  # 登录时确认指引

    def run_script_case1(devices):
        """
        新用户个人信息
        :param devices:
        :return:
        """
        Verified().login()
        Tool().test1loggin(devices)  # 获取设备信息
        try:
            UserLogin().test1_login('', 288371)  # 登录页面输入手机号验证码
            StartAPP().test3_permission()
            StartAPP().test2_update_app()
            My_page().my()
            My_page().new_user_info()
        finally:
            Tool().test2loggin_html()  # 生成测试报告


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.login)

