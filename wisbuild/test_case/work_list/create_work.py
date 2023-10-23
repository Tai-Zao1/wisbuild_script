#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "新用户个人详情"

import threading
from wisbuild_script.wisbuild.page_object.work.recruitment_list.create_work_page import Create_work
from wisbuild_script.wisbuild.page_object.work.work_list.work_page import Work
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

        StartAPP().screenon()
        StartAPP().clearapp()  # 清除缓存启动APP
        StartAPP().test1_tv_agree()  # 登录时确认指引

    def create_work(devices):
        """
        招工信息展示
        :param devices:
        :return:
        """
        Verified().login()
        Tool().test1loggin(devices)  # 获取设备信息
        try:
            UserLogin().test1_login('16500000001', 288371)  # 登录页面输入手机号验证码
            StartAPP().test3_permission()
            StartAPP().test2_update_app()
            Work().menu_work()
            Work().find_work()
            Create_work().create_entrance(3)
            Create_work().publish_work('新泾家苑', '工地小工/杂工/拆除工/打磨/学徒')
            Create_work().c_info()
            Create_work().other_tag('人员构成', '个人')
            Create_work().other_tag('人数', '1-2人')
            Create_work().other_tag('工资', '元/天', 200)
            Create_work().other_tag('结算方式', '日结')
            Create_work().other_tag('熟练度', '中工')
            Create_work().other_tag('熟练度', '小工')
            Create_work().other_tag('福利', '包住')
            Create_work().other_tag('福利', '包吃')
            Create_work().other_tag('福利', '社保')
            Create_work().other_tag('其他要求', '会用智能手机')
            Create_work().other_tag('其他要求', '技术好')
            Create_work().other_tag('其他要求', '二把刀勿扰')
            Create_work().tag_confirm()
            Create_work().publish()
        finally:
            Tool().test2loggin_html()  # 生成测试报告


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest

    devicestest().parallel(Verified.create_work)
