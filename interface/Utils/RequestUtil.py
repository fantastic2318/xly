import requests

#接口请求测试 就是对数据的测试
def send_request(url, method,headers=None,params=None,content_type=None):
    '''
    接口发送请求
    '''
    try:
        result = None
        if method.lower() == 'get':
            result = requests.get(url,headers=headers,params=params)
        elif method.lower == 'post':
            if content_type == 'application/json':
                result = requests.post(url=url, json=params, headers=headers)
            else:# 提交表单 方式
                result = requests.post(url=url, data=params, headers=headers)
        else:
            print('http method not supported')
        return result
    except Exception as e:
        print(f'http 请求报错{e}')


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/cat_list'
    method = 'get'
    headers = {'Content-Type': 'application/json'}
    result = send_request(url=url,method=method,headers=headers)
    print(result.json())
