import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail(object):
    def __init__(self):
        self.smtp_server = "smtp.163.com"
        self.usermail = "137*******6@163.com"
        self.password = "********"
        self.receives = ["840*****0@qq.com"]
        self.subject = "Slot自动化测试报告"
        self.content = "<html><h1>叮咚，您有新的外卖订单，请注意查收!</h1></html>"
        self.report = os.path.dirname(os.path.dirname(__file__)) + "/report/"

    def send_mail(self, latest_report):
        # 三种方式打开文件
        # f = open(latest_report, 'rb')
        # mail_content = f.read()
        # f.close()

        # msg = MIMEText(open(latest_report, "rb").read(), "html", "utf-8")

        with open(latest_report, 'rb') as f:
            mail_content = f.read()

        html = os.path.split(latest_report)[1]

        # 定义附件格式
        try:
            att = MIMEText(mail_content, "html", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            att["Content-Disposition"] = "attachment;filename='%s'" % html
        except Exception:
            print("附件无法携带")
            raise

        # 定义头部信息
        try:
            msg = MIMEMultipart()
            msg.attach(MIMEText(self.content, "html", "utf-8"))
            msg["Subject"] = Header(self.subject, "utf-8")
            msg["From"] = self.usermail
            msg["To"] = ",".join(self.receives)
            msg.attach(att)
        except Exception:
            print("头部定义错误")
            raise

        try:
            print("外卖正在配送中...")
            smtp = smtplib.SMTP_SSL(self.smtp_server, 465)
            smtp.helo(self.smtp_server)
            smtp.ehlo(self.smtp_server)
            smtp.login(self.usermail, self.password)
            smtp.sendmail(self.usermail, self.receives, msg.as_string())
            smtp.quit()
            print("叮,您的外卖已送达，请趁热吃!")
        except smtplib.SMTPDataError:
            print("邮件发送失败!!!")
            raise

    def latest_report(self):
        lists = os.listdir(self.report)
        lists.sort(key=lambda fn: os.path.getatime(self.report + fn))
        print("new report is:" + lists[-1])
        file = os.path.join(self.report, lists[-1])
        print(file)
        print(os.path.split(file)[1])
        self.send_mail(file)


if __name__ == '__main__':
    mail = Mail()
    mail.latest_report()
