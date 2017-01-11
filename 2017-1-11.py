import os
from collections import Iterable

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r= []
n = 3
for i in range(n):
    r.append(L[i])
print(r)
"""高级特性"""
"""切片"""
print(L[0:3]);
print (L[-2:])
L = list(range(100))
print (L[:10])                         #取前10个数
print (L[-10:])                        #取后10个数
print (L[:10:2])                       #前10个数 每两个取一个
print (L[::5])                         #所有数 每5个取一个
print ((0,1,2,3,4,5)[:3])              #tuple也可以切片操作
print (L[:])                           #复制list
print ('ABCDE'[:3])                    #字符串也可看成list
"""迭代"""
#即用for循环
d = {'a':1,'b':2,'c':3}                #默认迭代key
for key in d:
    print (key)                        #可迭代value
for key in d.values():
    print (key)                        #key跟value都迭代
for key,value in d.items():
    print (key,value)

#判断是否是可迭代对象
print (isinstance(12,Iterable))        #Iterable可看作可迭代类型
print (isinstance('12',Iterable))

#迭代list实现下标
for i,value in enumerate(['A','B','C']):    #enumerate函数可以将list变成索引-元素
    print (i,value)                         #跟dict的items()相同作用
for i,value in [(1,1),(2,2),(3,3)]:
    print (i,value)
"""列表生成式"""
print (list(range(1,11)))               #生成1-10的list
str = [x * x for x in range(1,11)]      #生成1*1 2*2 3*3的list
print (str)
str = [x * x for x in range(1,11) if x % 2 == 0]      #生成1*1 2*2 3*3且偶数的list
print (str)
str =[m + n for m in 'ABC' for n in 'XYZ']          #两层循环
print (str)
L = ['Hello', 'World', 'IBM', 'Apple']
print ([s.lower() for s in L])              #lower函数把字符串变小写
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print ([k + '=' + v for k, v in d.items()])         #循环dict生成list
print ([d for d in os.listdir('.')])            #listdir可以列出文件和目录
                                                #需要导入os
"""生成器"""
g = (x * x for x in range(10))                  #用（）表示generator类型
for n in g:                                     #generator保存的是算法 并不是值 但有值的范围
    print (n)

def fib(max):                                   #斐波拉契数列
    n, a, b = 0, 0, 1
    while n < max:
        yield b                                 #如果函数定义中包含yield 则该函数为generator
        a, b = b, a + b
        n = n + 1
    return 'done'
v = fib(6)
print (next(v),next(v),next(v),next(v),next(v)  )