#!/usr/bin/python
# -*- coding:utf-8 -*-


import cgi, os
import cgitb

cgitb.enable()#在网页上显示错误信息

form = cgi.FieldStorage()#接收Web客户端发送的数据

fileitem = form['filename']#获取文件名

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open('File/' + fn, 'wb').write(fileitem.file.read())

    message = '文件 "' + fn + '" 上传成功'

else:
    message = '文件没有上传'
    
print("""\
    Content-type: text/html\n\n
    <html>
    <head>
    <title>文件上传</title>
    </head>
    <body>
    <p>%s</p>
    </body>
    </html>
"""% (message, ))

print('Content-type:text/html\n')
print('%s' % message)



# 文件下载
print ("Content-Disposition: attachment; filename='test.txt'")
print('')

fo = open("E:\\study\\study\\python\\Save_File\\cgi-bin\\foo.txt", "rb")

str = fo.read()
print(str)

fo.close()


