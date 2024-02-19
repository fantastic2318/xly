import os
import time

from PythonTest.Mix_fra.Util.read_excel import ExcelParse
from PythonTest.Mix_fra.settings.config import testDataPath, template_path, testReportPath


def generate_report():
    """
    生成测试报告
    :return:
    """
    test_count = 0 # 用例总数
    pass_count = 0
    fail_count = 0
    skip_count = 0
    excel_obj = ExcelParse()
    excel_obj.load_workbook(os.path.join(testDataPath, '163mixFra.xlsx'))
    data_sheet = excel_obj.get_sheet_by_name('case')
    rows_nums = excel_obj.get_rows_nums(data_sheet)
    test_count = rows_nums - 1
    content = ''
    # 拼接 $test_result 内容 ，之后 替换就行
    for i in range(2, rows_nums+1):
        # 添加一行
        content += "\n<tr height='40'>" # 添加一行
        content += f'\n<td width="7%">{i-1}</td>' # id
        # Case Name
        content += f'\n<td widt="15%">{excel_obj.get_cell_value(i, 2, data_sheet)}</td>'
        # 是否执行
        content += f'\n<td widt="7%">{excel_obj.get_cell_value(i, 7, data_sheet)}</td>'
        if excel_obj.get_cell_value(i, 7, data_sheet) == 'n':
            skip_count += 1
            content += f'\n<td width="10%">SKIP</td>' # 测试结果列
        else: # 需要执行
            content += f'\n<td width="10%">{excel_obj.get_cell_value(i, 8, data_sheet)}</td>'

        # 测试时间
        content += f'\n<td width="10%">{excel_obj.get_cell_value(i, 9, data_sheet)}</td>'
        # Test Log
        content += f'\n<td width="12%">{"to be added"}</td>'
        # error msg
        content += f'\n<td width="15%">{"to be added"}</td>'
        # test screen
        content += f'\n<td width="20%">{"to be added"}</td>'

        content += '\n</tr>'
        if excel_obj.get_cell_value(i, 8, data_sheet) == "pass":
            pass_count += 1
        elif excel_obj.get_cell_value(i,8, data_sheet) == "fail":
            fail_count += 1


    percent = str(round(pass_count/(test_count - skip_count), 4) * 100) if pass_count != 0 else '0'
    with open(template_path, encoding='utf-8') as file:
        template = file.read()

    now = time.strftime('%Y%m%d_%H%M%S')
    template = template.replace('$test-date', time.strftime('%Y%m%d'))
    template = template.replace('$test-version', '1.0v')

    template = template.replace('$pass-count', str(pass_count))

    template = template.replace('$fail-count', str(fail_count))

    template = template.replace('$skip-count', str(skip_count))
    template = template.replace('$percent', percent)
    template = template.replace('$report-time', now)

    template = template.replace('$test-result', content)


    # html报告
    # filename = testReportPath + '/' + time.strftime(f'{now}.html')
    # with open(filename, mode='w', encoding='utf-8') as file:
    #     file.write(template)
    return template


if __name__ == "__main__":
    generate_report()