#!/usr/bin/env  python3
# -*- coding:utf-8 -*-

"""list  可修改数组"""
classmate = ['Michael','Bob','Tracy']
print ("classmate = ",classmate)
print(len(classmate))                           #输出list的长度          len(obj)
print(classmate[0],classmate[1],classmate[2])
print(classmate[-1])                            #输出list倒数第一个元素
classmate.append('admin')                       #添加元素到list末尾       append(obj)
print(classmate)
classmate.pop()                                 #删除list末尾元素         pop()
print(classmate)
classmate.pop(2)                                #删除list指定位置元素
print(classmate)
classmate[1] = 'ZZM'                            #替换list指定位置元素
print(classmate)
classmate.append(True)                          #list数据类型可不一致
classmate.insert(2,213)                         #插入list                insert(index,obj)
print(classmate)

"""tuple  不可修改数组"""
classmates = ('Michael','Bob','Tracy')
print(classmates)
classmates = ('Michael','Bob','Tracy',['A','B'])
print(classmates)
classmates[3][0] = 'C'
classmates[3][1] = 'D'
print(classmates)
t=(1,)                                          #定义一个元素的tuple的时候必须加一个逗号，消除歧异
print(isinstance(t,tuple))                      #类型判断           isinstance(obj,type)
print(type(t))                                  #类型判断           type(obj)

sum = 0                                         #range(int)  列出0 到 int的值
for x in range(5):                              #range(5)  =  [1,2,3,4,5]
    sum += x
print(sum)

"""获取用户输入的字符串"""
try:                                            #python3.x input等于python2.x 的raw_input
   birth = int(input('birth:'))                 #这里必须加int()否则会报错 因为input()默认获取的是string类型
   if birth < 2000:
       print('00前')
   else:
       print('00后')                            #try except 就是try catch
except ValueError:
    print("请输入数字")

"""dict set集合"""
dict = {'Michael':95,'Bob':75,'Tracy':85}       #dict 就是 object
dict['Tomes'] = 99
print('Tomes' in dict)                          #用in判断dict中有没有Tomes
print(dict.get('Tomes'))                        #用get判断dict中有没有Tomes

s = set([1,2,3])                                #set是一个不存储value的集合 key不能重复
s.add(3)
print (s)
s.remove(3)
print (s)
s1 = set([1,2,3])
s2 = set([2,3,4])
print (s1 & s2)                                 #可以进行数学上的运算 交集
print (s1 | s2)                                 #并集

"""数据类型"""
s = abs(-3*6)                                    #abs 绝对值函数
print (s)
s = max(1,2)                                     #max获取最大值
print (s)
s = int('1234')
print (s)
s = float('1433')
print (s)
s = str(321)
print (s)
s = bool('')
print (s)
s = hex(23)                                      #hex转换成16进制字符串
print (s)

"""函数"""
def my_abs(x):                                   #用def来定义函数
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-5))