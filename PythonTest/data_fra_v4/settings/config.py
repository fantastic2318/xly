import os

# .ini文件路径，当前文件的目录的绝对路径的父目录的父目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试数据文件
testDataPath = os.path.join(BASE_DIR, 'TestData/163mail.xlsx')
#print(eleLocationPath)

# 日志文件路径

logfilePath = os.path.join(BASE_DIR, 'Logfile')

# 添加测试用例路径
testCasePath = os.path.join(BASE_DIR, 'Scripts')

# 测试报告路径
testReportPath = os.path.join(BASE_DIR, 'Reports')