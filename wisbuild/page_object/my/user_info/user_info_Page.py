#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "个人中心"

import sys
import datetime
from airtest.core.api import *
import unittest
import logging

from wisbuild_script.wisbuild.tool.permission import Permission
from wisbuild_script.wisbuild.tool.upload_pic import Upload_pic
from wisbuild_script.wisbuild.tool.work_type import Work_type

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


# noinspection PyTypeChecker
class User_info_page(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 修改头像
    def header(self, filename_url):
        header = self.poco(name="com.rh.hjz:id/constraint_image")
        header.click()
        cancel = self.poco(name="com.rh.hjz:id/tv_cancel")
        cancel.click()
        tittle = self.poco(name="com.rh.hjz:id/tv_title", text="个人头像")
        if len(tittle) == 1:
            print("进入个人头像页面")
        right = self.poco(name="com.rh.hjz:id/iv_right")
        right.click()
        md_md_content_layout = self.poco(name="com.rh.hjz:id/md_content_layout")
        if len(md_md_content_layout) == 1:
            print("修改头像")
        Permission().source_pic(2)  # 从手机相册中选择
        Permission().camera_permission()  # 确认权限
        Upload_pic().pic(filename_url)  # 选择头像文件

    # 修改用户昵称
    def nickname(self):
        nickname = self.poco(name="com.rh.hjz:id/tv_content")[0]
        print("当前用户昵称：" + nickname.get_text())
        nickname.click()
        title = self.poco(name="com.rh.hjz:id/tv_title", text="昵称设置")
        if title.exists():
            delete = self.poco(name="com.rh.hjz:id/iv_cancel")
            delete.click()
            nickname2 = self.poco(name="com.rh.hjz:id/et_name")
            now = datetime.datetime.strftime(datetime.datetime.now(), '%m-%d')
            nickname2.set_text("自动化修改" + now)
            self.poco(name="com.rh.hjz:id/tv_right").click()
        else:
            print("未进入编辑页面")

    # 修改用户工种
    def work_type(self, work_type1):
        work_type = self.poco(name="com.rh.hjz:id/tv_content")[1]
        if work_type.get_text() == "暂无":
            work_type.click()
            # 直接走选择工种流程
            Work_type().update_work_type("开槽, 油漆工, 固定工")
        else:
            work_type.click()
            choose = self.poco(name="com.rh.hjz:id/rv_choose_list")
            c_list = choose.offspring("com.rh.hjz:id/tv_name")
            # 删除已选工种
            for x in c_list:
                c_name = choose.offspring("com.rh.hjz:id/tv_name").get_text()
                delete = c_list.sibling("com.rh.hjz:id/iv_remove")[0]
                delete.click()
                print("删除原工种：" + c_name)
            # 修改用户工种
            Work_type().update_work_type(work_type1)



if __name__ == '__main__':
    unittest.main()
