#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "我的页面"

from wisbuild_script.wisbuild.page_object.login.login_Page.login import *
from wisbuild_script.wisbuild.page_object.my.user_info.user_setting_Page import *
import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# noinspection PyTypeChecker
class My_page(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 我的菜单
    def my(self):
        self.poco(name="com.rh.hjz:id/menu_mine").click()

    # 进入个人信息
    def user_info(self):
        self.poco(name="com.rh.hjz:id/iv_avatar").parent().click()  # 点击头像控件所在父级
        user_info = self.poco(name="com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("个人信息" in user_info)
        except ValueError:
            print("未进入个人信息")

    # 进入钱包
    def wallet(self):
        self.poco(name="com.rh.hjz:id/tv_title", text='钱包').click()
        wallet = self.poco(name="com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("我的钱包" in wallet)
        except ValueError:
            print("进入钱包失败")

    # 进入证件管理
    def documents(self):
        self.poco(name="com.rh.hjz:id/tv_title", text='证件').click()
        documents = self.poco(name="com.rh.hjz:id/tv_my_certificate").get_text()
        try:
            assert ("我的证件" in documents)
        except ValueError:
            print("进入证件失败")

    # 进入设备管理
    def equipment(self):
        self.poco(name="com.rh.hjz:id/tv_title", text='设备').click()
        equipment = self.poco(name="com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("设备管理" in equipment)
        except ValueError:
            print("进入设备管理失败")

    # 进入紧急联系人
    def emergency_contact(self):
        self.poco(name="com.rh.hjz:id/tv_title", text="紧急联系人").click()
        emergency_contact = self.poco(name="紧急联系人").get_text()
        try:
            assert ("紧急联系人" in emergency_contact)
        except ValueError:
            print("进入联系人列表失败")

    # 设置
    def set(self):
        self.poco(name="com.rh.hjz:id/tv_title", text="设置").click()
        set_up = self.poco(name="com.rh.hjz:id/constraint_title").child("com.rh.hjz:id/tv_title").get_text()
        try:
            assert ("设置" in set_up)
        except ValueError:
            print("进入设置页面失败")

    # 用户信息
    def new_user_info(self):  # user_type: 0 无数据用户，1 完整数据用户
        work_type = self.poco(name="com.rh.hjz:id/tv_type").get_text()
        certified = self.poco(name="com.rh.hjz:id/tv_certified").get_text()
        username = self.poco(name="com.rh.hjz:id/tv_name").get_text()
        user_heard = Template(r"\wisbuild_automation\wisbuild_script\wisbuild\page_object\my\image\iv_avatar.png")
        if "暂无" in work_type:
            print(work_type)
            if "未实名认证" in certified:
                print(certified)
                if assert_exists(user_heard, "断言用户头像"):
                    print("用户昵称：" + username)
                    print("该用户为新用户")
        else:
            User_setting_page().sign_out()
            UserLogin().test1_login('13100000000', 288371)
            My_page().my()
            My_page().new_user_info()


if __name__ == '__main__':
    unittest.main()
