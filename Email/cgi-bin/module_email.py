# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址

def module_email(recever = ['669559765@qq.com'], title ='title', mes = ['test', '测试公司']):
    mail_host = 'smtp.163.com'
    #163 用户名
    mail_user = 'udbbbn'
    #密码
    mail_pass = 'zzm991228'
    #邮箱发送方邮箱地址
    mail_sender = 'udbbbn@163.com'
    #邮件接收方邮箱地址 用[]意味着可以群发
    mail_receivers = recever
    
    #设置email信息
    #右键内容设置
    message = MIMEText('【' + mes[1] + '】验证码为:' + mes[0], 'plain', 'utf-8')
    #邮件主题
    message['Subject'] = title
    #发送方信息
    message['From'] = mail_sender
    
    #登录并群发邮件
    try:
        for i in mail_receivers:
            #接收方信息
            message['To'] = i
            smtpObj = smtplib.SMTP()
            #连接到服务器
            smtpObj.connect(mail_host, 25)
            #登录到服务器
            smtpObj.login(mail_user, mail_pass)
            #发送
            smtpObj.sendmail(
                mail_sender, i, message.as_string()
            )
            #退出
            smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        #打印错误
        print('error', e)

if __name__ == '__main__':
    module_email(['669559765@qq.com'], '验证码', '456153')
