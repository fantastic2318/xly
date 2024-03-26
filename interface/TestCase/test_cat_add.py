import pytest

from interface.Utils.ExcelUtil import get_row_values
from interface.Utils.RequestUtil import send_request

params = get_row_values('data.xlsx', 'add', 1)
params_values = get_row_values('data.xlsx', 'add')
@pytest.parametrize(params,params_values)
def test_add(project, module, caseid, casename, description, url, method, header, param, contenttype):
    param = eval(param) if param else param
    request = send_request(url=url, method=method,headers=header, params=param,content_type=contenttype)
    print(request.text)