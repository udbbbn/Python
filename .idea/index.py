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
def nop():                                       #空函数pass占位符
    pass
def my_abs(x):
    if not isinstance(x,(int,float)):            #类型判断
        #raise TypeError('bad operand type')      #抛出错误
        pass
    if x >= 0:
        return x
    else:
        return -x
import math
def move(x,y,step,angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi / 6)              #返回值为tuple 数组 返回值是单一值
print (x,y)
r = move(100,100,60,math.pi / 6)
print (r)

"""可变参数函数"""
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n *n ;                       # *号代表可变参数 即不限制参数的个数
    return sum
result = calc(12,3,5)
print (result)
nums = [1,2,3,4]
result = calc(*nums)                             # 在传入的参数前加*可以让参数
print (result)                                   # 以可变参数形式传入

"""关键字参数函数 选填参数"""
def person(name,age,**kw):
    print ('name:',name,'age:',age,'other:',kw)     #带两个*号代表关键字参数
person('Michael',30)                                #关键字参数会组成一个dict
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack',24,**extra)
"""命名关键字参数函数 必填"""
def person(name, age, *args, city, job):
    print(name, age, args,city, job)
person('Jack', 24,3213,321321,city='Beijing', job='Engineer')   #必须要传入参数名 否则报错
"""
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
要注意定义可变参数和关键字参数的语法：
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
以及调用函数时如何传入可变参数和关键字参数的语法：
可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数"""

"""递归函数"""
def fact(n):
    if n == 1:
        return 1
    return n * fact(n -1)

print (fact(5))

"""尾递归"""
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1,num * product)         #return的值为纯函数即尾递归
print(fact(5))