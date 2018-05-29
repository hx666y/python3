import sys,os
import sendMail

sendmsg = sendMail.SendMail()

sendmsg.mailFile('模块测试','Python','checkip.py','614045035@qq.com')


# 设置环境变量
# print(os.path.dirname(os.path.abspath(__file__)))
# dir = os.path.dirname(os.path.abspath(__file__))
# print(sys.path)
# sys.path.append(dir)