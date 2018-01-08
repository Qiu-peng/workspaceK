# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header


sender = '1161158359@qq.com'
receivers = ['qiupeng_akt@163.com']

message = MIMEText('你好!!!!!!', 'plain', 'utf-8')
message['From'] = Header('来自qiu', 'utf-8')
message['To'] = Header('测试连接' 'utf-8')

subject = '无主题'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect('smtp.qq.com', 587)
    smtpObj.login(sender, 'hpreaiyzmopljbbb')
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print('发送成功')
except smtplib.SMTPException as e:
    print(e)