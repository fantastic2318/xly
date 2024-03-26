import os

import pytest
import yaml

from interFace2.Conf.Setting import DATA_PATH
from interFace2.Utils.ApiExecute import execute_api
from interFace2.Utils.yamlparse import read_caseinfo

caseinfos = read_caseinfo(os.path.join(DATA_PATH, 'add_cat.yaml'))
@pytest.mark.parametrize('caseinfo', caseinfos)
def test_demo1(caseinfo):
    #with open(os.path.join(DATA_PATH, 'TestData/add_cat.yaml'), "r", encoding='utf-8') as yamlfile:
        # api_data = yaml.safe_load(yamlfile)
        # print(type(caseinfo))
        # print(caseinfo)
        # 执行请求
        execute_api(caseinfo)

if __name__ == '__main__':
    pytest.main(['-s', 'test_add.py'])