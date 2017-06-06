#!/usr/bin/python
# -*- coding:utf-8 -*-
#接收ajax数据


import cgi, cgitb
import random

from module_email import module_email #编辑器未识别 实际可用
cgitb.enable()#使错误信息显示在网页上


form = cgi.FieldStorage()#接收客户端发送过来的数据
recever = form.getvalue('recever')#获取数据字典中的'recever'参数

recever = recever.split(' ')#将字符串转换成数组

code = random.randint(100000, 1000000)#生成随机验证码

title = '验证码'

msg = [str(code), '郑和保险']

value = module_email(recever, title, msg)#调用email发送函数

print ("Content-type: text/html")#告诉python 现在输出的是html信息
print('')#区分页头与内容
if value == 'success':
    print('{"status":200,"code":' + str(code) + '}')
else:
    print('{value}')





