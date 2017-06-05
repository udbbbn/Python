#!/usr/bin/python
# -*- coding:utf-8 -*-
#接收ajax数据


import cgi, cgitb
import urllib, http

import module_email #编辑器未识别 实际可用
#module_email.module_email()
cgitb.enable()


form = cgi.FieldStorage()
recever = form.getvalue('recever')
print(form)

data=recever


print ("Content-type: text/html")
print('')
print ("<p id=name>%s,%s</p>"% (recever, form))

# print("Status: 200 OK")
# print("Content-type: text/html")
# print()  # 打印一行空白行，用于分隔HTTP Header和正文
#
# print("<h1>Hello World!</h1>")


