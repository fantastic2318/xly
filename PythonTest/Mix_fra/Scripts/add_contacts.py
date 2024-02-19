import os
import time

from PythonTest.Mix_fra.Action import elementsAction
from PythonTest.Mix_fra.Action.elementsAction import *
from PythonTest.Mix_fra.Util.generate_method import generate_func
from PythonTest.Mix_fra.Util.read_excel import ExcelParse
from PythonTest.Mix_fra.settings.config import testDataPath
from PythonTest.Mix_fra.Action import *


def add_contact(excel, data_sheet, step_sheet):
    """
    添加联系人
    :param excel:
    :param data_sheet:
    :return:
    """
    # 步骤行数
    step_row_nums = excel.get_rows_nums(step_sheet)
    # 数据行数
    data_row_nums = excel.get_rows_nums(data_sheet)
    # 需要执行的行数
    need_record = 0
    # 成功的行数
    sucess_record = 0

    for i in range(2, data_row_nums+1):
        # 判断是否需要执行
        if excel.get_cell_value(i, 6, data_sheet).lower() == "y":
            need_record += 1
            name = excel.get_cell_value(i, 1, data_sheet)
            email = excel.get_cell_value(i, 2, data_sheet)
            is_star = excel.get_cell_value(i, 3, data_sheet)
            phone = excel.get_cell_value(i, 4, data_sheet)
            remarks = excel.get_cell_value(i, 5, data_sheet)
            success_step = 0
            for j in range(2, step_row_nums+1):
                step_desc = excel.get_cell_value(j, 1, step_sheet)
                location_type = excel.get_cell_value(j, 2, step_sheet)
                location_express = excel.get_cell_value(j, 3, step_sheet)
                key_word = excel.get_cell_value(j, 4, step_sheet)
                operate_value = excel.get_cell_value(j, 5, step_sheet)
                # 将关键字sheet中value和数据sheet中数据联系
                # backup 候补定位方式
                backup_location_express = excel.get_cell_value(j, 6, step_sheet)

                # 判断operate_value是否为规定的变量 ${}
                if isinstance(operate_value, str) and "${" in operate_value and '}' in operate_value:
                    # ${email}-->email
                    operate_value = eval(operate_value[2:operate_value.index('}')])
                # operate_value 一定为data_sheet中的列值
                # 组装对应方法

                method_express = generate_func(location_type, location_express, key_word, operate_value)
                if operate_value != 'N':
                    # 不是星标为N的步骤 则执行
                    try:
                        eval(method_express)
                    except TimeoutError as e:
                        print(f"执行{step_desc}失败, 尝试用backup定位方式")
                        backup_method_express = generate_func(location_type, backup_location_express, key_word, operate_value)
                        try:
                            eval(backup_method_express)
                        except Exception as e:
                            print(f'执行{step_desc} 候补失败')
                            continue
                        else:
                            success_step += 1
                            print(f"执行{step_desc} 候补成功")
                    else:# 原本定位方式成功
                        success_step += 1
                        print(f"执行{step_desc}成功")
                else:  # 如果是星标不为N 则不执行
                    success_step += 1
            if success_step + 1 == step_row_nums:
                sucess_record += 1
                excel.write_cell(i, 7, 'pass', os.path.join(testDataPath, '163mixFra.xlsx'), data_sheet)
            else:
                excel.write_cell(i, 7, 'fail', os.path.join(testDataPath, '163mixFra.xlsx'), data_sheet)
    if sucess_record == need_record:
        return "pass"
    else:
        return "fail"



# if __name__ == "__main__":
#     from selenium import webdriver
#     path = "/usr/local/bin/chromedriver"
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get('http://mail.163.com')
#     driver.maximize_window()
#     i_frame = driver.find_element('tag name', 'iframe')
#     driver.switch_to.frame(i_frame)
#     driver.find_element('name', 'email').send_keys('fantastic2318')
#     driver.find_element('name', 'password').send_keys('fantastic12306')
#     driver.find_element('id', 'dologin').click()
#     time.sleep(10)
#     driver.refresh()
#     elementsAction.driver = driver
#     excel_obj = ExcelParse()
#     excel_obj.load_workbook(os.path.join(testDataPath, '163mixFra.xlsx'))
#     data_sheet = excel_obj.get_sheet_by_name("contacts_data")
#     step_sheet = excel_obj.get_sheet_by_name("add_contacts")
#     add_contact(excel_obj, data_sheet, step_sheet)
