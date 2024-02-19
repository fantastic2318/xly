import os

from action_fra.Util.generate_method import generate_func
from action_fra.Util.read_excel import ExcelParse
from action_fra.settings.config import testDataPath
from action_fra.Action.elementsAction import *

excel_par = ExcelParse()
file_path = os.path.join(testDataPath, "163mail.xlsx")
excel_par.load_workbook(file_path)


def test_run():
    """
    测试登录场景
    :return:
    """
    excel_par.get_sheet_by_name('index')
    # 获取测试场景
    row_nums = excel_par.get_rows_nums()

    for i in range(2, row_nums+1):

        if excel_par.get_cell_value(i, 5) == 'y':
            case_step_sheet = excel_par.get_cell_value(i, 4)
            excel_par.get_sheet_by_name(case_step_sheet)
            # 拿到步骤数
            steps_nums = excel_par.get_rows_nums()

            # 记录成功步骤数（如果成功步骤数==最大步骤数，则认为该场景执行成功，一旦某一步骤抛出异常则认为场景执行失败）
            success_steps = 0
            for j in range(2, steps_nums+1):
                step_desc = excel_par.get_cell_value(j, 1)
                location_type = excel_par.get_cell_value(j, 2)
                location_express = excel_par.get_cell_value(j, 3)
                action = excel_par.get_cell_value(j, 4)
                test_data = excel_par.get_cell_value(j, 5)
                print(f'{step_desc}-{location_type}-{location_express}-{action}-{test_data}')
                # 函数表达式 通过Excel中的步骤构建函数表达式
                method_express = generate_func(location_type, location_express, action, test_data)
                # 识别字符串种的表达式
                try:
                   eval(method_express)
                except Exception as e:
                    excel_par.get_sheet_by_name("index")
                    excel_par.write_cell(i, 6, "error", file_path, excel_par.sheet)
                    break
                else:
                    success_steps += 1
                if success_steps == steps_nums - 1:
                    # 表示用例场景成功执行、则写入成功
                    excel_par.get_sheet_by_name("index")
                    excel_par.write_cell(i, 6, "pass", file_path, excel_par.sheet)
                else:
                    # 写入失败
                    pass


if __name__ == "__main__":
    test_run()