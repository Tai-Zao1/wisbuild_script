#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "慧建驻"
__title__ = "新用户个人详情"

import threading
from wisbuild_script.wisbuild.page_object.work.recruitment_list.to_hire_page import To_hire
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

    def run_script_case1(devices):
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
            To_hire().title()
            To_hire().work_info('自动化测试')
            To_hire().work_level_2('钻工/炮工/矿工/喷浆手/爆破')
            To_hire().work_tags('11-20人 | 完工结 | 长期 | 大工 | 小工 | 包住 | 包吃 | 社保 | 餐补 | 高温补贴 | 会用智能手机 | 技术好 | 专业师傅 | 二把刀勿扰')
            To_hire().city_name('苏州')
            To_hire().publish_user('苹果13', '班组')
        finally:
            Tool().test2loggin_html()  # 生成测试报告


if __name__ == "__main__":
    from wisbuild_script.wisbuild.tool.phone_devices import devicestest
    devicestest().parallel(Verified.run_script_case1)
