#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "项目列表页面"

import sys
from airtest.core.api import *
import unittest
import logging

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class List(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # 切换项目
    def change_proj(self):
        change_name = self.poco(name="com.rh.hjz:id/tv_change")
        if change_name.exists() == True:
            toggle_proj = change_name.sibling('com.rh.hjz:id/tv_project_name').get_text()
            print("可切换项目：" + toggle_proj)
            change_name[0].click()
            sleep(2)
            home_proj = self.poco(name="com.rh.hjz:id/tv_project").get_text()
            if home_proj == toggle_proj:
                print("切换成功")
            else:
                print("切换失败")
        else:
            print("没有可切换项目")

    # 判断项目信息
    def proj_info(self, projname, proj_state, proj_type):
        proj_name = self.poco(textMatches=projname + ".*")
        proj_state1 = proj_name.sibling("com.rh.hjz:id/tv_project_process").get_text()
        assert_equal(proj_state, proj_state1, "项目状态不成立")
        print("项目状态成立")
        proj_type1 = proj_name.sibling("com.rh.hjz:id/tv_project_type").get_text()
        assert_equal(proj_type, proj_type1, "项目类型不成立")
        print("项目类型成立")

    # 点击进入项目详情
    def proj_detail(self, projname):
        proj_name = self.poco(textMatches=".*" + projname + ".*")
        while proj_name.exists() == False:
            swipe([600, 1500], [600, 500])
        else:
            proj_name.click()
            print("进入项目详情: "+proj_name.get_text())


if __name__ == "__main__":
    unittest.main()
