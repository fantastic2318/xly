import os.path

from interFace2.Conf.Setting import DATA_PATH
from interFace2.Utils.ApiExecute import execute_api_flow
from interFace2.Utils.yamlparse import read_full_case


def test_flow():
    caseinfo = read_full_case(os.path.join(DATA_PATH, 'flow.yaml'))
    execute_api_flow(caseinfo)