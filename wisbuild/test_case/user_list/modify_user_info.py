#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "修改用户信息"

import threading

from wisbuild_script.wisbuild.page_object.my.user_info.more_user_info import More_user_info
from wisbuild_script.wisbuild.page_object.my.user_info.my_Page import My_page
from wisbuild_script.wisbuild.page_object.my.user_info.user_info_Page import User_info_page
from wisbuild_script.wisbuild.tool.Generate_log import *
from wisbuild_script.wisbuild.page_object.login.login_Page.start_APP import *
from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
from wisbuild_script.wisbuild.tool.upload_pic import Upload_pic

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

    def md_user_info(devives):
        """
        修改个人信息
        :param devices:
        :return:
        """
        Verified().login()
        Tool().test1loggin(devives)
        try:
            UserLogin().test1_login("16500000001", "288371")
            StartAPP().test3_permission()
            StartAPP().test2_update_app()
            My_page().my()
            My_page().user_info()
            User_info_page().header(
                r"F:\wisbuild_automation\wisbuild_script\wisbuild\image\header_image.png")  # 在相册选择头像
            Upload_pic().crop()  # 更换头像
            User_info_page().nickname()  # 修改昵称
            User_info_page().work_type("装修木工,固定工,泥瓦工")  # 修改工种
            More_user_info().entrance()
            More_user_info().hometown('江苏', '苏州')
        finally:
            Tool().test2loggin_html()  # 生成测试报告


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest

    devicestest().parallel(Verified.login)
