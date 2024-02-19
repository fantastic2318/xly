import requests
url = 'http://httpbin.org/get'
'''
get请求无参数
'''
res = requests.get(url, timeout=5)
print(res.text)
print(res.encoding)
print(res.content) # 二进制形式返回内容
print(res.json()) # 返回内容转换成json格式
print(res.status_code == requests.codes.ok)  # 内置状态校验
print(res.headers)
print(res.cookies)

'''
get请求有参数
'''
payload = {
    'username': 'admin',
    'password': '<PASSWORD>'
}
res2 = requests.get(url, params=payload)
print(res2.text)

'''
请求头传值
'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
}
payload = {
    'username': 'admin',
    'password': '<PASSWORD>'
}
res3 = requests.get(url, params=payload, headers=headers)
print(res3.text)

'''
post请求,带headers
'''
post_url = 'http://httpbin.org/post'
res4 = requests.post(post_url, headers=headers)
print(res4)

'''
post请求 以表单形式传入数据
'''
print('post请求 以表单形式传入数据'+'*'*30)
form_data = {
    'username': 'admin',
    'password': '123'
}
res5 = requests.post(post_url, data=form_data, headers=headers)
print(res5.text)
'''
post请求 以json形式传入数据
'''
print('post请求 以json形式传入数据'+'*'*30)
json_data = {
    'username': 'admin',
    'password': '345'
}
res6 = requests.post(url=post_url, json=json_data, headers=headers)
print(res6.text)

'''
post请求 带headers ,http://ssssd?name=sdf 入参展示在外面的post请求(query_string)
'''
data = {'gender': 'M', 'nation': 'China'}
res7 = requests.post(url=post_url, headers=headers, params=data)
print(res7.text)

'''
post请求 带headers ,同时出现form json
'''
print('post请求 带headers ,同时出现form json'+'---'*10)
data = {'gender': 'M', 'nation': 'China'}
res8 = requests.post(url=post_url, headers=headers, json=json_data, data=form_data)
print(res8.text)

'''
文件上传
'''
# files = {
#     'file': open('http_introduce.md', 'rb')
# }
# res9 = requests.post(url=post_url, files=files)
# print(res9.text)

'''
带cookies发送服务器
'''

url_cookies = 'http://httpbin.org/cookies'
cookies = {'name': 'cc'}
res10 = requests.post(url=url_cookies, cookies=cookies)
print(res10.text)