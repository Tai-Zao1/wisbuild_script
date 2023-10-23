#!/usr/bin/python
# -*-coding:GBK -*-
import sys
import unittest
from airtest.core.api import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Work_type(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    #   �޸��û�����
    def update_work_type(self, work_list1):  # work_list �û����֣�����������м䶺�ŷָ�
        work_list = work_list1.replace(' ', '').split(',')
        aa = self.poco(name="com.rh.hjz:id/rv_right_type")
        two_work_type = aa.offspring("com.rh.hjz:id/tv_name")
        bb = len(work_list)
        i = 0
        a = 1
        while a <= bb:

            three_work_type = aa.offspring("com.rh.hjz:id/cst_bg").offspring("com.rh.hjz:id/tv_name")

            two_work_type[i].click()
            # print("-----" + two_work_type[i].get_text()+ '==>���')

            cc = len(list(three_work_type))
            for x in range(cc):
                # print("xֵ" +str(x))
                work_type_name = three_work_type[x].get_text()
                # print("----------" + work_type_name)
                if work_type_name in work_list:
                    print("�����" + work_type_name)
                    three_work_type[x].click()

                    a += 1
                    time.sleep(2)
                x += 1
            else:
                two_work_type[i].click()
                print("�ر�"+two_work_type[i].get_text())
                i += 1
                # two_work_type[i].click()
                # print('��'+two_work_type[i].get_text())
                # print('aֵ:'+str(a))
                # print('xֵ:' + str(x))
        # ѡ���ֽ��������ȷ��
        affirm = self.poco(name="com.rh.hjz:id/tv_affirm")
        affirm.click()
        print("�޸Ĺ��ֽ���")


if __name__ == '__main__':
    unittest.main()
