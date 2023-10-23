#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "登陆页面"

import os
import sys
from airtest.core.api import *
import time
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from wisbuild_script.wisbuild.tool.Mobile_Phone import createPhone

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class UserLogin(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 登陆
    def test1_login(self, mobile=None, code=None):  # type :1 = 多线程（自动获取） ；2 =单线程（手动输入账号密码）
        time.sleep(5)
        login_text = \
            self.poco(name="com.rh.hjz:id/tv_explain").attr("text")
        assert_equal(login_text, "登录即可查看考勤记录，工作核算，项目动态状态等信息，随时掌握最新进度", '判断登录页面描述')
        code_login = self.poco(name="com.rh.hjz:id/tv_mobile_code_login")
        if len(code_login) == 1:
            print("未登录->进行登录步骤")
            if str(mobile) != "":
                self.poco(name="com.rh.hjz:id/et_mobile").set_text(mobile)
                print("输入手机号:" + str(mobile))
            else:
                mobile1= str(createPhone().moblie())
                self.poco(name="com.rh.hjz:id/et_mobile").set_text(mobile1)
                print("输入随机手机号:" + str(mobile1))
            self.poco(name="com.rh.hjz:id/et_verify_code").set_text(code)
            print("输入验证码：" + str(code))
            agreement_button = self.poco(name="com.rh.hjz:id/tv_agreement_explain")
            if len(agreement_button) == 1:
                self.poco(name="com.rh.hjz:id/ck_agree").click()
                print("点击确认协议")
            else:
                print("已确认协议")
            self.poco(name="com.rh.hjz:id/tv_mobile_login").click()
            snapshot(msg="登录截图")
            print("点击登录按钮")
        else:
            print("已登录->不需要再次登录")


if __name__ == '__main__':
    unittest.main()
