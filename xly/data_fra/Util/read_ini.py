# -*- coding: utf-8 -*- 
# @Time : 2023-12-17 13:52 
# @Author : kunp
# @File : read_ini.py 
# @Software: PyCharm

import configparser

from data_fra.Settings.Config import eleLocationPath


class IniParaseFile:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(eleLocationPath)


    def getSection(self, section_name):
        """
        获取  section_name 这个节的所有的参数值（键值对）
        """
        option_dict = dict(self.cf.items(section_name))
        return option_dict


    def getOpitonVaule(self, sction_name, option_name):
        """
        获取某个节中具体的某个参数的值
        """
        return self.cf.get(sction_name, option_name)


if __name__ == '__main__':
    ini_par = IniParaseFile()
    print(ini_par.getSection("163mail_login"))
    # print(ini_par.getOpitonVaule('163mail_login', 'login_page.loginbutton'))
