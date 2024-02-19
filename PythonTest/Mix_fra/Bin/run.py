import time

import gitlab
import schedule



from PythonTest.Mix_fra.Scripts.test_flow import test_loginandContractsAndSend
from PythonTest.Mix_fra.Util.generate_report import generate_report
from PythonTest.Mix_fra.Util.send_email import SendEmail
from PythonTest.Mix_fra.settings.config import GIT_URL, private_token, LAST_COMMIT_ID


def execute_case():
    """
    执行测试用例
    :return:
    """
    #test_loginandContractsAndSend()
    content = generate_report()
    email = SendEmail()
    now = time.strftime("%Y-%m-%d")
    email.send_email(f"陈信宏为什么开会唱歌自动化测试标题-{now}", content)


def job1():
    print("")


def job2():
    print("")


def job3(name):
    print(f"{name}运行")


def check_commit():
    """
    用来判断 项目是否有新的提交
    :return:
    """
    git_client = gitlab.Gitlab(GIT_URL, private_token)
    projects = git_client.projects
    print(projects.get(1))
    project = projects.get(1)
    print(project.commits.list(all=True)[0])

    last_commit_id = project.commits.list(all=True)[0].get_id()

    with open(LAST_COMMIT_ID, 'r') as file:
        store_commit_id = file.read()

    if store_commit_id != last_commit_id:
        print('项目有新的提交')
        execute_case()
        with open(LAST_COMMIT_ID, 'w') as file:
            file.write(last_commit_id)
    else:
        pass


if __name__ == "__main__":
    execute_case()
    # schedule.every(1).minutes.do(job1)
    # schedule.every().day.at("14:33").do(job2)
    # print(schedule.get_jobs()) # 获取多有任务
    #
    # # 带参数的形式
    # schedule.every(10).seconds.do(job3, name="任务3")
    # schedule.every(1).to(5).seconds.do() # 每1~5秒运行一次
    # schedule.every().hour.do()   # 每小时
    # schedule.every().day.at('00:00').do()
    # schedule.every().monday.at() # 每周一
    # schedule.every().minute.at(':45') # 每分钟45秒执行
    # print(schedule.get_jobs()) # 获取所有任务

    # schedule.every().day.at('14:47').do(execute_case)
    # while True:
    #     schedule.run_pending()  # 运行 所有可执行的任务