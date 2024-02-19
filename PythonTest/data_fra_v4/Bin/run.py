import time
import unittest
import TestRunner
from TestRunner import SMTP

from data_fra_v4.settings.config import testCasePath, testReportPath

"""
整个框架从此处开始运行
"""
if __name__ == "__main__":
    suit = unittest.TestSuite()
    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    loader = unittest.TestLoader()  # 装载测试用例
    suit.addTests(loader.discover(testCasePath))
    report_file = testReportPath + "/"+now+'_report.html'
    with(open(report_file, 'wb')) as fp:
        runner = TestRunner.HTMLTestRunner(
            stream=fp,
            title="陈信宏开会为什么会唱歌测试报告",
            description="仅供测试"
        )
        runner.run(suit)

    smtp = SMTP(user="fantastic2318@163.com", password="GOENZBIJLFZKBJCJ", host='smtp.163.com')
    smtp.sender(to='1552599101@qq.com', subject='陈信宏开会为什么唱歌-12.24课后作业', contents='陈信宏开会为什么唱歌-12.24课后作业', attachments=report_file)
