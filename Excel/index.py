#coding=utf-8

import xlrd
import re
import pymysql.cursors

global FLAG
FLAG = 0

def open_excel(file='E:\\2016意外险新信息_14G5_2.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


def get_data_byindex(colnameindex= 1,byindex = 0):#表头列名索引,表索引
    data = open_excel()#打开excel表
    table = data.sheets()[byindex]#表索引
    nrows = table.nrows#行
    ncols = table.ncols#列
    colnames = table.row_values(colnameindex)#某一行数据
    list = []
    for rownum in range(2, nrows):#循环获取数据
        row = table.row_values(rownum)
        # if row:
        #     app = {}
        #     for i in range(len(colnames)):
        #         row[i] = re.sub(u'\xa0', '', str(row[i]))
        #         app[colnames[i]] = row[i]
        #     list.append(app)
        app = []
        for i in range(len(colnames)):
            row[i] = re.sub(u'\xa0', '', str(row[i]))
            app.append(row[i])
            list.append(app)
        if 'e' in app[-1]:
            app[-1] = int(float(app[-1]))
        sql_operation(app)
    return list
    data.close()

def get_data_byname():
    data = open_excel()
    table = data.sheet_by_name(u'sheet')
    nrows = table.nrows
    for i in range(1, nrows):
        print(table.row_values(i))


def sql_operation(value):
    config={
        'user':'root',
        'password':'usestudio-1',
        'host' : 'localhost',
        'db' : 'test',
        'port':3306,
        'charset':"utf8"
    }
    global FLAG
    
    database = pymysql.connect(**config)
    cursor = database.cursor()#游标对象
    #创建表
    if FLAG == 0:
        sql_createtable = """
              drop table if EXISTS IdCard;
              create table IdCard (id INT (4) not NULL PRIMARY KEY auto_increment,
                 name VARCHAR(20) not NULL, sex VARCHAR (4) NOT NULL, Grade VARCHAR (20) NOT NULL,
                 Class VARCHAR (20) NOT NULL, IdType VARCHAR (20) NOT NULL, IDCard VARCHAR (20)NOT NULL)
              """
        cursor.execute(sql_createtable)
        FLAG += 1

    sql_execute = """insert into idcard(name, sex, Grade, Class, IdType, IDCard) VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql_execute, value)

    cursor.close()
    
    database.commit()
    
    database.close()

def main():
    table = get_data_byindex()
    for row in table:
        pass
    # print(row)

if __name__ == "__main__":
    main()