import smtplib
import sys,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class SendMail(object):
    def __init__(self):
        # 第三方SMTP服务
        self.mail_host = "smtp.163.com"    # SMTP服务器
        self.mail_user = "hx666y@163.com"  # 用户名
        self.mail_pass = "hongxuan1992"    # 密码

        self.sender = "hx666y@163.com"

    def mail(self, subject, content, *args):
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = self.sender
        msg['To'] = ",".join(args)
        msg['Subject'] = Header(subject,'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)              # 启用SSL发信, 端口一般是465
            smtpObj.login(self.mail_user,self.mail_pass)                      # 登录验证
            smtpObj.sendmail(self.sender,args,msg.as_string())          # 发送
            print("mail send sucessfully.")
        except smtplib.SMTPException as e:
            print(e)

    # 发送带附件的方法
    def mailFile(self, subject, content, filename, *args):
        # 判断是否存在filename
        if not os.path.isfile(filename):
            print("File is not found.")
            sys.exit(0)
        else:
            # 创建一个带附件的实例
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = ",".join(args)
            msg['Subject'] = Header(subject,'utf-8')

            # 邮件正文内容
            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            # 构造附件1, 传送当前目录下的log.txt 文件
            att = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att['Content-Disposition'] = 'attachment; filename='+ filename
            msg.attach(att)
            try:
                smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)              # 启用SSL发信, 端口一般是465
                smtpObj.login(self.mail_user,self.mail_pass)                      # 登录验证
                smtpObj.sendmail(self.sender,args,msg.as_string())          # 发送
                print("mail send sucessfully.")
            except smtplib.SMTPException as e:
                print(e)

if __name__ == '__main__':
    sendmail = SendMail()
    sendmail.mailFile('Python文件传送测试邮件','日志文件','log.txt','204120021@qq.com','614045035@qq.com')
