import mysql.connector
conn = mysql.connector.connect(user='root', password='usestudio-1', database='test');
cursor = conn.cursor()
cursor.execute('select * from test')
values = cursor.fetchall()
print (values)
cursor.close()
conn.close()
"""连接myslq数据库"""