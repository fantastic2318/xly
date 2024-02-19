import os

from PythonTest.Mix_fra.Scripts import excel_obj
from PythonTest.Mix_fra.Scripts.add_contacts import add_contact
from PythonTest.Mix_fra.Util.generate_method import generate_func
from PythonTest.Mix_fra.Util.read_excel import ExcelParse
from PythonTest.Mix_fra.settings.config import testDataPath

from PythonTest.Mix_fra.Action.elementsAction import *


def test_loginandContractsAndSend():
    """
    测试 登录--》 添加联系人---》发送邮件
    :return:
    """

    excel_obj.load_workbook(os.path.join(testDataPath, "163mixFra.xlsx"))

    case_sheet = excel_obj.get_sheet_by_name("case")

    case_nums = excel_obj.get_rows_nums(case_sheet)

    for i in range(2, case_nums+1):

        # 判断case是否要执行
        if excel_obj.get_cell_value(i, 7, case_sheet).lower() == 'y':
            # 获取测试用例名
            case_name = excel_obj.get_cell_value(i, 2, case_sheet)
            # 获取框架名
            frame_mode = excel_obj.get_cell_value(i, 4, case_sheet)

            step_sheet_name = excel_obj.get_cell_value(i, 6, case_sheet)
            # 数据类型
            if frame_mode == "data":
                data_sheet_name = excel_obj.get_cell_value(i, 5, case_sheet)
                data_source_sheet = excel_obj.get_sheet_by_name(data_sheet_name)
                step_sheet = excel_obj.get_sheet_by_name(step_sheet_name)
                print(i, data_sheet_name, data_source_sheet)
                result = add_contact(excel_obj, data_source_sheet, step_sheet)

                if result == "pass":
                    print(f"执行{case_name}成功")
                    excel_obj.write_cell(i, 8, 'pass', os.path.join(testDataPath, '163mixFra.xlsx'), case_sheet)
                else:
                    print(f"执行{case_name}失败")
                    excel_obj.write_cell(i, 8, 'fail', os.path.join(testDataPath, '163mixFra.xlsx'), case_sheet)
            # 关键字驱动
            elif frame_mode == "keyword":

                step_sheet = excel_obj.get_sheet_by_name(step_sheet_name)

                step_nums = excel_obj.get_rows_nums(step_sheet)

                success_step_nums = 0
                for j in range(2, step_nums+1):
                    step_desc = excel_obj.get_cell_value(j, 1, step_sheet)
                    location_type = excel_obj.get_cell_value(j, 2, step_sheet)
                    location_express = excel_obj.get_cell_value(j, 3, step_sheet)
                    action = excel_obj.get_cell_value(j, 4, step_sheet)
                    test_data = excel_obj.get_cell_value(j, 5, step_sheet)
                    print(j, location_type, location_express, action, test_data)
                    method_express = generate_func(location_type, location_express, action, test_data)
                    try:
                        print(f'开始执行-{step_desc}--{method_express}')
                        eval(method_express)
                    except Exception as e:
                        print(f'执行{step_desc} 发生异常 {e}')
                        excel_obj.write_cell(i, 8, 'fail', os.path.join(testDataPath, '163mixFra.xlsx'), case_sheet)
                        continue
                    else:
                        print(f'执行{step_desc}成功')
                        success_step_nums += 1
                if success_step_nums + 1 == step_nums:
                    print(f'{case_name}执行成功')
                    excel_obj.write_cell(i, 8, 'pass', os.path.join(testDataPath, '163mixFra.xlsx'), case_sheet)


if __name__ == "__main__":
    test_loginandContractsAndSend()
