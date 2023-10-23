#!/usr/bin/python
# -*- encoding=GBK -*-
__author__ = "�۽�פ"
__title__ = "�����й�"

import json
import sys
from airtest.core.api import *
import unittest
import logging

from wisbuild_script.wisbuild.page_object.work.project_list.proj_filter_Page import Filter
from wisbuild_script.wisbuild.tool.permission import Permission

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)


class Create_work(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    # �й������ϴ�ͼƬ
    def create_entrance(self, amount):
        create_ent = self.poco(name='com.rh.hjz:id/iv_camera')
        create_ent.click()
        Permission().camera_permission()
        img = self.poco(name='com.rh.hjz:id/tvCheck')
        i = 0
        while i <= amount - 1:
            img[i].click()
            i += 1
            content = self.poco(name="com.rh.hjz:id/tv_content")
            btnOk = self.poco(name='com.rh.hjz:id/btnOk')
            if content.exists():
                print(content.get_text())
                btnOk.click()
                break
        header_confirm = Template(r"F:\wisbuild_automation\wisbuild_script\wisbuild\image\header_confirm.png")
        touch(header_confirm)
        sleep(5)

    #   �й���Ϣ�ı������
    def publish_work(self, address, work_level_2):
        weak_hint = "�������й���Ϣ..."
        text_input = self.poco(name="com.rh.hjz:id/et_input").get_text()
        assert (weak_hint in text_input)
        city_name = Create_work().work_city(address)
        # print(city_name)
        Create_work().work_type(work_level_2)
        work_list_name = Create_work().c_info_worklevel3()
        print()
        # work_list_name2 = ",".join(work_list_name)
        # print(work_list_name2)
        input_text_case = city_name + '��Ƹ' + '��'.join(work_list_name)
        print(input_text_case)
        # confirm = self.poco(name='com.rh.hjz:id/tv_right', text='ȷ��')
        # confirm.click()
        text_input = self.poco(name="com.rh.hjz:id/et_input").get_text()
        assert (input_text_case in text_input)

    #   ���ֵ���
    def work_city(self, address):
        work_city_ent = self.poco(name='com.rh.hjz:id/tv_left', text='��������')
        work_city_ent.click()
        search = self.poco(name='com.rh.hjz:id/tv_search')
        sleep(3)
        search.click()
        self.poco(name='com.rh.hjz:id/et_search').set_text(address)
        i = 1
        while i <= 3:
            address_name = self.poco(name='com.rh.hjz:id/tv_title')
            if address_name.exists():
                if address in address_name.get_text():
                    address_name.click()
                    break
                else:
                    pass
            else:
                sleep(3)
                print("��ַδ���س������ȴ�" + str(i) + '��')
                i += 1
        else:
            raise SyntaxError('ɸѡ�й���ַ�쳣,�ȴ�������'+ str(i))
        city = self.poco(name='com.rh.hjz:id/tv_left').sibling('com.rh.hjz:id/tv_content')
        city.wait_for_appearance()
        city_name = city.get_text()
        print("��ѡ��ַ����ʡ�У�" + city_name)
        return city_name

    #   ���蹤��
    def work_type(self, work_level_2):
        work_type_ent = self.poco(name='com.rh.hjz:id/tv_left', text='���蹤��')
        work_type_ent.click()
        Filter().level2work(work_level_2)

    #   ������Ϣ���
    def c_info(self):
        c_info_ent = self.poco(name='com.rh.hjz:id/tv_left', text='������Ϣ').sibling('com.rh.hjz:id/tv_right')
        c_info_ent.click()

    #   ��ȡ����������������������
    def c_info_worklevel3(self):
        weak_hint = '��8�� �Ǳ���'
        c_info_text = self.poco(name='com.rh.hjz:id/tv_right')
        assert (weak_hint in c_info_text.get_text())
        c_info_text.click()
        #   ��ȡ���ֱ�ǩ
        work_level2 = self.poco(name='com.rh.hjz:id/tv_work_level').get_text()
        work_tag = self.poco(name='com.rh.hjz:id/rv_list')[0]
        work_list = work_tag.offspring('com.rh.hjz:id/tv_text_tag')
        work_list_name = []
        i = 0
        while i < len(work_list):
            work_level3 = work_tag.offspring('com.rh.hjz:id/tv_text_tag')[i].get_text()
            # print(work_level3)
            i += 1
            work_list_name.append(work_level3)
        self.poco(name='com.rh.hjz:id/tv_right', text='ȷ��').click()
        return work_list_name

    #   �����й���ǩ��ע�⣺��ѡ���ٴε��ã�
    def other_tag(self, tag_type, pres_tag, amount=None):
        """
        tag_type:��Ա���ɡ����������ʡ����㷽ʽ�����ڡ������ȡ�����������Ҫ��
        pres_tag��������Ӧ��ǩ��
        """
        staff_comp = self.poco(name="com.rh.hjz:id/tv_title", text=tag_type)
        staff_comp = staff_comp.sibling("com.rh.hjz:id/rv_list").child("com.rh.hjz:id/cst_cons")
        while not staff_comp.exists():
            swipe([500, 2000], [500, 1000])
        staff_comp_tag = staff_comp.child("com.rh.hjz:id/tv_text_tag", text=pres_tag)
        staff_comp_tag.click()
        if tag_type == '����':
            if pres_tag != '����':
                work_amount = self.poco(name='com.rh.hjz:id/et_input')
                work_amount.click()
                work_amount.set_text(amount)
        else:
            pass


    #   ��ǩȷ��
    def tag_confirm(self):
        tag_confirm = self.poco(name='com.rh.hjz:id/tv_right', text='ȷ��')
        tag_confirm.click()

    #   �й�����
    def publish(self):
        self.poco(name='com.rh.hjz:id/tv_publish').click()
        rule = self.poco(name='com.rh.hjz:id/li_cancel')
        if rule.exists():
            self.poco(name='com.rh.hjz:id/tv_agree').click()
        else:
            print('��ȷ�Ϲ��������ٴ�ȷ��')


if __name__ == '__main__':
    unittest.main()
