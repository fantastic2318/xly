import os

# .ini文件路径，当前文件的目录的绝对路径的父目录的父目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试数据文件
testDataPath = os.path.join(BASE_DIR, 'TestData')
#print(eleLocationPath)

# 日志文件路径

logfilePath = os.path.join(BASE_DIR, 'Logfile')

# 添加测试用例路径
testCasePath = os.path.join(BASE_DIR, 'Scripts')

# 测试报告路径
testReportPath = os.path.join(BASE_DIR, 'Reports')

# 测试报告模板路径
template_path = os.path.join(BASE_DIR, 'Template/template.html')

# 邮箱配置
EmailConfig = {
    "SMTP_SERVER": 'smtp.163.com',
    "PORT": 465,
    "FROM": "fantastic2318@163.com",
    "TO": ['1552599101@qq.com'],
    "PASSWORD": "GOENZBIJLFZKBJCJ"  # 授权码
}

# gitLab配置
GIT_URL = ""
private_token = ""
LAST_COMMIT_ID = os.path.join(BASE_DIR, "settings/last_commit_id.txt")
