"""
1、给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。
如 nums = [2,7,11,15], target = 9
输出:[0,1]
⽤两种⽅法实现(实在想不不出，至少实现一种)
"""


def twoSum(nums, target):
    dict1 = {}
    for i, v in enumerate(nums):
        diff = target - v
        if diff in dict1:
            return [dict1[diff], i]
        else:
            dict1[v] = i


print(twoSum([2, 7, 11, 15], 9))

# 第二种想了很久  后来百度一下 是二分法
def twoSum_v2(nums,target):
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum > target:
            right -= 1
        else:
            left += 1
print(twoSum_v2([2, 7, 11, 15], 9))
"""
2、从字符串里提取单词，例如”my name is cc“，将单词放到列表⾥， 不要用 split ⽅方法
"""
def getWord(str1):
    startIndex = 0
    endIndex = 0
    list1 = []
    while startIndex < len(str1):
        if str1[startIndex] != ' ':
            startIndex += 1
        else:
            list1.append(str1[endIndex: startIndex])
            startIndex += 1
            endIndex = startIndex
    list1.append(str1[endIndex:startIndex])
    return list1


#print(getWord('my name is cc'))

"""
3、⽣生成矩阵
已知两个列列表
  lst_1 = [1, 2, 3, 4]
  lst_2 = ['a', 'b', 'c', 'd']
将两个列列表交叉相乘 得到
  [['1a', '2a', '3a', '4a'],
   ['1b', '2b', '3b', '4b'],
   ['1c', '2c', '3c', '4c'],
   ['1d', '2d', '3d', '4d']]
"""
def getVector(lst_1, lst_2):

    vector = [[str(j)+i for j in lst_1] for i in lst_2]
    return vector

#print(getVector([1, 2, 3, 4],['a', 'b', 'c', 'd']))

"""
4.比较版本号，给一个["2.1.0", "1.5", "2", "1.1.999.1.2.3", "0.10.0"] 要求从小到大排序


"""
def sortVersion(list1):
    for i in range(len(list1)-1, -1, -1):
        for j in range(0, i):
            if list1[i] < list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
    return list1


print(sortVersion(["2.1.0", "1.5", "2", "1.1.999.1.2.3", "0.10.0"]))

"""
完成163邮箱从登录到发送邮件的线性代码
"""
import time
from selenium import webdriver
path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(executable_path=path)
driver.get('http://mail.163.com')
time.sleep(3)
# 根据tag name(input  span iframe )查找
tmp_iframe = driver.find_element('tag name', 'iframe')
# 切换到iframe中
driver.switch_to.frame(tmp_iframe)
time.sleep(2)
driver.find_element('name','email').send_keys('fantastic2318')
driver.find_element('name','password').send_keys('fantastic12306')
driver.find_element('id', 'dologin').click()
time.sleep(5)
# 写信
driver.refresh()
driver.find_element('xpath', '/html/body/div[1]/nav/div[1]/ul/li[2]/span[2]').click()
time.sleep(3)
driver.find_element('class name', 'nui-editableAddr-ipt').send_keys('764904579@qq.com')
# driver.find_element('class name', 'nui-ipt-input').send_keys('测试')
# find_element && find_elements
driver.find_elements('class name', 'nui-ipt-input')[2].send_keys('你吃饭了没')
driver.switch_to.frame(driver.find_element('class name', 'APP-editor-iframe'))
driver.find_element('class name', 'nui-scroll').send_keys('你吃饭了么')
driver.switch_to.default_content()
driver.find_element('xpath', '/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]').click()
