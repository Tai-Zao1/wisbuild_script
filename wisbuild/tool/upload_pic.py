#!/usr/bin/python
# -*-coding:GBK -*-
import sys
import unittest
from airtest.core.api import *

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


class Upload_pic(unittest.TestCase):
    def __init__(self):
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        poco = AndroidUiautomationPoco()
        unittest.TestCase.__init__(self)
        self.poco = poco

    #   ѡ��ͷ��ͼƬ
    def pic(self, filename_url):
        new_header_image = Template(filename_url)
        while not exists(new_header_image):
            swipe([500, 500], [500, 1900])
        else:
            touch(new_header_image)
        # ȷ�ϰ�ť��û�пؼ�name��ͼƬ header_confirm
        header_confirm = Template(r"F:\wisbuild_automation\wisbuild_script\wisbuild\image\header_confirm.png")
        ps_selected = self.poco(name="com.rh.hjz:id/ps_tv_selected")
        if ps_selected.exists():
            ps_selected.click()
            print("����Ԥ��ģʽ")
        touch(header_confirm)

    #   �ü�
    def crop(self):
        crop = self.poco(name="com.rh.hjz:id/toolbar_title").get_text()
        print("����" + crop)
        proportion = self.poco(name="android.widget.TextView", text="1:1")
        proportion.click()
        self.poco(name="com.rh.hjz:id/menu_crop").click()
        print("�ü��ɹ�")


if __name__ == '__main__':
    unittest.main()
