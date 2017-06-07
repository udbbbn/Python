# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText    #处理文字
from email.mime.multipart import MIMEMultipart  #处理文件
from email.mime.image import MIMEImage  #处理图片
#设置服务器所需信息
#163邮箱服务器地址

#只能发送文字
def module_email_txt(recever = ['669559765@qq.com'], title ='title', mes = ['test', '测试公司']):
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
            #获取对象
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
        return ('success')
    except smtplib.SMTPException as e:
        #打印错误
        return ('error', e)

#可发送附件
def module_email_mult(recever=['669559765@qq.com'], title='title', mes=['test', '测试公司']):
    mail_host = 'smtp.163.com'
    # 163 用户名
    mail_user = 'udbbbn'
    # 密码
    mail_pass = 'zzm991228'
    # 邮箱发送方邮箱地址
    mail_sender = 'udbbbn@163.com'
    # 邮件接收方邮箱地址 用[]意味着可以群发
    mail_receivers = recever

    # 设置email信息
    # 右键内容设置
    # message = MIMEText('【' + mes[1] + '】验证码为:' + mes[0], 'plain', 'utf-8')
    #添加一个MIMEMultipart实例对象 处理正文及附件
    message = MIMEMultipart()
    # 邮件主题
    message['Subject'] = title
    # 发送方信息
    message['From'] = mail_sender

    #推荐使用html格式的正文内容 方便附加图片地址 调整格式等等
    with open('../index.html','rb') as f:
        content = f.read()
    #设置html格式参数
    part1 = MIMEText(content, 'html', 'utf-8')
    #添加一个txt附件
    with open('../abc.txt', 'rb') as h:
        content2 = h.read()
    #设置txt参数
    part2 = MIMEText(content2, 'plain', 'utf-8')
    #附件设置内容类型 方便起见 设置为二进制流
    part2['Content-Type'] = 'application/octet-stream'
    #设置附件头 添加文件名
    part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
    with open('../test.png', 'rb') as fp:
        picture = MIMEImage(fp.read())
        #与txt文件设置相似
        picture['Content-Type'] = 'application/octet-stream'
        picture['Content-Disposition'] = 'attachment;filename="1.png"'
    message.attach(part1)
    message.attach(part2)
    message.attach(picture)


    # 登录并群发邮件
    try:
        for i in mail_receivers:
            # 接收方信息
            message['To'] = i
            # 获取对象
            smtpObj = smtplib.SMTP()
            # 连接到服务器
            smtpObj.connect(mail_host, 25)
            # 登录到服务器
            smtpObj.login(mail_user, mail_pass)
            # 发送
            smtpObj.sendmail(
                mail_sender, i, message.as_string()
            )
            # 退出
            smtpObj.quit()
        return ('success')
    except smtplib.SMTPException as e:
        # 打印错误
        return ('error', e)

if __name__ == '__main__':
    value = module_email_mult(['669559765@qq.com'], '验证码', ['456153','神奇公司'])
    print(value)


#QQ邮箱需要SSL认证 所需SMTP_SSL
# #启动
# smtpObj = smtplib.SMTP()
# #连接到服务器
# smtpObj.connect(mail_host,25)
# #######替换为########
# smtpObj = smtplib.SMTP_SSL(mail_host)