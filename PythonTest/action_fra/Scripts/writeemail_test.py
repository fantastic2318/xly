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
    测试写信场景
    :return:
    """
    excel_par.get_sheet_by_name("index")
    row_nums = excel_par.get_rows_nums()
    success_steps = 0
    for i in range(2, row_nums+1):
        if excel_par.get_cell_value(i, 4) == "writeemail" and excel_par.get_cell_value(i, 5) == 'y':
            case_sheet = excel_par.get_sheet_by_name("writeemail")
            steps_nums = excel_par.get_rows_nums()
            #print(excel_par.get_rows_nums())
            for j in range(2, steps_nums+1):
                step_desc = excel_par.get_cell_value(j, 1)
                location_type = excel_par.get_cell_value(j, 2)
                location_express = excel_par.get_cell_value(j, 3)
                test_action = excel_par.get_cell_value(j, 4)
                test_data = excel_par.get_cell_value(j, 5)
                #print(f'{step_desc}-{location_type}-{location_express}-{test_action}-{test_data}')
                express_method = generate_func(location_type, location_express, test_action, test_data)
                try:
                    eval(express_method)
                except Exception as e:
                    excel_par.get_sheet_by_name("index")
                    excel_par.write_cell(i, 6, 'error', file_path, excel_par.sheet)
                else:
                    success_steps += 1
                if success_steps == steps_nums-1:
                   excel_par.write_cell(i, 6, 'pass', file_path, excel_par.sheet)


if __name__ == "__main__":
    test_run()