#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "我的页面"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class User_setting_page(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco
        from wisbuild_script.wisbuild.page_object.my.user_info.userInfo_Page import User
        User().set()

    # 退出登录
    def sign_out(self):
        self.poco(name="com.rh.hjz:id/tv_logout").click()
        code_login_text = self.poco(name="com.rh.hjz:id/tv_mobile_code_login")
        if len(code_login_text) == 1:
            print("退出登录成功")
        else:
            print("退出登录失败")


if __name__ == '__main__':
    unittest.main()
