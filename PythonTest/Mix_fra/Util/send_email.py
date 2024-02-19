import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from PythonTest.Mix_fra.settings.config import EmailConfig


class SendEmail:
    """
    发送测试报告邮件
    """
    def __init__(self):
        self.server = EmailConfig['SMTP_SERVER']
        self.port = EmailConfig['PORT']
        self._from = EmailConfig['FROM']
        self._to = EmailConfig['TO']
        self.password = EmailConfig['PASSWORD']
        self.smtp = smtplib.SMTP_SSL(self.server, self.port)
        self.smtp.login(self._from, self.password)

    def send_email(self, title, content):
        """
        发送邮件（不是附件形式）、打开邮件直接看见
        :param title:
        :param content:
        :return:
        """
        msg = MIMEMultipart()

        email_text = MIMEText(content, 'html', 'utf-8')
        msg.attach(email_text)

        msg['Subject'] = Header(title, 'utf-8')
        msg['From'] = self._from
        msg['TO'] = ''.join(self._to)

        # 发送邮件
        print('start send email...')
        self.smtp.sendmail(self._from, self._to, msg.as_string())
        self.smtp.quit()
        print("send end.....")


if __name__ == '__main__':
    email = SendEmail()
    email.send_email("这是手工制作的邮件标题", '爱你')
