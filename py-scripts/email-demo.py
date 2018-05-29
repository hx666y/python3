import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方SMTP服务
mail_host = "smtp.163.com"    # SMTP服务器
mail_user = "hx666y@163.com"  # 用户名
mail_pass = "hongxuan1992"    # 密码

sender = "hx666y@163.com"
receivers = ["614045035@qq.com"]

content = "我用python"
title = "Python SMTP 邮件测试"

def sendEmail():
    message = MIMEText(content, 'plain', 'utf-8')   # 内容，格式，编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)              # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user,mail_pass)                      # 登录验证
        smtpObj.sendmail(sender,receivers,message.as_string())  # 发送
        print("mail send sucessfully.")
    except smtplib.SMTPException as e:
        print(e)

def mail(to_host, subject, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = sender
    msg['To'] = to_host
    msg['Subject'] = Header(subject,'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)              # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user,mail_pass)                      # 登录验证
        smtpObj.sendmail(sender,to_host,msg.as_string())        # 发送
        print("mail send sucessfully.")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    #sendEmail()
    mail('614045035@qq.com','Python测试邮件','人生苦短，我用Python.')