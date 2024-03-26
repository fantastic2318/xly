import copy
import os

import yaml
from yamlinclude import YamlIncludeConstructor

from interFace2.Conf.Setting import DATA_PATH


def read_caseinfo(yaml_path):
    """
    获取caseinfo数据[]
    """
    caseinfos = []
    with open(yaml_path, 'r', encoding='utf-8') as yamlfile:
        caseinfo = yaml.safe_load(yamlfile)

    ddts = caseinfo.get('ddts', [])
    if len(ddts) > 0:
        caseinfo.pop('ddts')

        # 没有多种场景
    if len(ddts) == 0:
        caseinfos.append(caseinfo)

    else:
        for ddt in ddts:
            new_case = copy.deepcopy(caseinfo)
            context = new_case.get('context', {})
            # 将ddt 中的数据 放到了 context 中，
            ddt.update(context)
            new_case.update({'context': ddt})
            caseinfos.append(new_case)
    return caseinfos


YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader)
def read_full_case(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
    return data


if __name__ == "__main__":
    # with open("../TestData/cat_add.yaml", "r") as ymlfile:
    #     data = yaml.load(ymlfile, Loader=yaml.Loader)
    #     print(type(data))
    #     print(data)
    # print(read_caseinfo(os.path.join(DATA_PATH, 'add_cat.yaml')))
    print(read_full_case(os.path.join(DATA_PATH, 'flow.yaml')))
    # string.Template 用于特定字符串的置换 前提是关键字打好标记 默认的替换符为b '$'
    # from string import Template
    # s = 'hello $world'
    # t = Template(s)
    # data = t.substitute({'world': '世界'})
    # print(data)