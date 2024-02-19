# 选择排序
# 求一个列表第二大的元素
# 模块 一个.py文件就是一个模块
# python 引入文件时、寻找文件会有一个默认的路径
# 导入时主要作用于定义变量和函数 不是每次导入都会执行函数 导入一次和导入多次效果相同、但是第二次导入就不会执行函数
import sys
#print(sys.path)

import pprint
#pprint.pprint(sys.path)
sys.path.append('/Users/wufan/Project/pythonProject')
pprint.pprint(sys.path)
from math import sin
from math import *  # 导入这个包里的所有内容
from math import cos as c  # 给方法重命名
c(6)
import haha
print(dir(haha)) # 模块加载时 会有自己创建一些属性（变量） __name__ 属性
# 这个模块是被自己执行（__name__ == __main__） 还是被调用执行
# 模块被别人调用、__name__ 为调用者的模块名
haha.show_message()

import os # 系统相关库
print(os.getcwd()) # 脚本所在的目录路径
#os.mkdir("aa") # 默认在当前路径创建一个文件夹 可以指定文件夹
#os.rmdir('') # 删除文件夹
"""
os.listdir() # 列出当前文件夹下所有文件夹和路径
os.rename()  # 修改路径下文件的名字
os.remove()  # 移除文件
print(os.path.abspath())  # 返回当前路径在系统中的绝对路径
os.path.join() # 连接两个路径
"""



import time
#time.sleep(3)
print(time.asctime())   # 获取当前时间 不传时间  默认显示当前时间 str
time.time()   # 获取当前时间戳 float
print(time.localtime(time.time()))  # 转换成本地时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.strptime('2023-12-03 08:56:00', '%Y-%m-%d %H:%M:%S'))


import random
r = random.choice([1,5,6,3,2,9,0]) # 在序列中随机抽取一个数
ret = random.sample([1,5,6,3,2,9,0],3)  # 在序列中随机抽取多个数
print(ret)
random.shuffle([1,5,6,3,2,9,0]) # 随意打乱顺序 返回原列表
# 生成随机数
random.randint(10,20) # 范围内10-20的随机整数
random.randrange(1,7,2) # 可以指定步长
random.random() # 1-0 随机


class A:
    def __init__(self, a, b, c):
        self.c = 100
        self._a = 10 # 约定俗成的私有变量
        self.__b = 20 # 真正的私有变量

    def get_b(self):
        return self.__b


# 私有变量 _ __
# 公有变量
a = A(100,2,3)
# a._a
# 在类的外部调用私有属性
a.get_b()
# a._A.__b 这种可以执行调用私有变量


# 进程 线程
"""
进程：正在运行的存续实体 一个进程包括了很多线程 
线程：程序执行的最小单元

并发：一个CPU 对应 三个用户执行 
并行：三个CPU 对应 三个用户执行

GIL锁 （Global Interpreter Lock） 全局解释器锁
pyhton支持多个线程、   Python解释器 ：某一个时间点 只有一个线程在解释器运行  伪多线程  类似并发概念
thread threading Queue  多线程模块
"""

from threading import Thread
import threading
def func(n):
    print(f'{threading.current_thread()}-task:{n}')
    time.sleep(2)
    print(f'{threading.current_thread()}已结束')



class Myclass(Thread):

    def __init__(self, func, arg):
        Thread.__init__(self)
        self.func = func
        self.args = arg

    def run(self):
        self.func(self.args)


# 通过类创建线程
t1 = Myclass(func,'线程1')
t2 = Myclass(func, '线程2')





# 通过函数创建线程
# t1 = Thread(target=func,args=('线程1',))  # 通过Thread类创建线程实例
# t2 = Thread(target=func,args=('线程2',))  # 通过Thread类创建线程实例

start_time = time.time()
threads = []
for i in range(20):
    t = Thread(target=func, args=(f'线程{i}',))
    t.setDaemon(True)  # 守护线程
    t.start()
    threads.append(t)
    #t.join() # 主线程等待子线程结束后才会运行主线程功能

for i in threads:
    i.join()

print(f"{threading.current_thread()}总共耗时:{time.time()-start_time} ")
print(f"{threading.current_thread()}已结束")
# 整个程序是一个总线程 总线程不会等到子线程全部执行完再去向下执行 而是 总线程直接向下执行
#t1.start()
#t2.start()





# 守护线程  是为主线程服务的













