import json
import re
from string import Template

import jsonpath
import requests


class Mytemplate(Template):
    delimiter = '!'

def execute_api_flow(caseinfo):
    context = caseinfo['context']
    for step in caseinfo.get('steps', []):
        step.update({'context':context})
        execute_api(step)

def execute_api(caseinfo):
    '''
    接口执行
    '''
    context = caseinfo['context']
    # 针对每个参数 进行变量渲染
    for key in caseinfo.keys():
        target = caseinfo.get(key)
        s = Mytemplate(json.dumps(target)) # 将可能是字典形式的值转化为字符串
        value = s.substitute(context)
        obj = json.loads(value)
        caseinfo.update({key: obj})


    print(f'请求信息为：{caseinfo}')

    # 发起请求操作
    response = requests.request(url=caseinfo.get('url', None),
                                 method=caseinfo.get('method', None),
                                 headers=caseinfo.get('headers', None),
                                 json=caseinfo.get('json', None),
                                params=caseinfo.get('params', None),
                                data=caseinfo.get('data', None),
                                cookies=caseinfo.get('cookies', None)
                                )

    print(f'接口返回{response.json()}')
   # 断言
    for assert_option in caseinfo.get('assert_options', []):
        target_value = None
        # 以jsonpath的形式取值
        if assert_option.get('target').startswith('$.'):
            target_value = jsonpath.jsonpath(response.json(), assert_option['target'])
        # 以正则表达式的形式取值
        else:
            parttern = re.compile(assert_option['target'])
            target_value = re.findall(parttern, response.text)[0]
        if assert_option['type'] == 'exits': #存在
            assert_result = target_value[0] != False
        elif assert_option['type'] == 'contails': # 包含
            assert_result = assert_option['value'] in target_value[0]
        elif assert_option['type'] == 'equals':
            assert_result = str(target_value[0]) == assert_option['value']

        assert assert_result, '断言不通过' + assert_option['errorMsg'] + '实际为'+ assert_option['value']
    # 提取变量
    for extract_option in caseinfo.get('extract_options', []):
        target_value = None
        # jsonpath 表达式
        if extract_option['target'].startswith('$.'):
            target_value = jsonpath.jsonpath(response.json(), extract_option['target'])[0]
        # 正则表达式提取
        else:
            pattern = re.compile(extract_option['target'])
            target_value = re.findall(pattern, response.text)[0]
        # 更新context
        context.update(
            {
                extract_option['varname']: target_value
            }
        )


    print(f'响应内容:{response.json()}')



