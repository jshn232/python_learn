#!/usr/bin/env python3

h = hex
print('%s' % h(1000))
print('0x%x' % 1000)

print('%s == 0x%x' % (h(1000),1000))


#定义函数

def add(a,b):
    return a+b


print(add(1,4))

#默认参数
def add(a,b,c=3,d=4):
    return a+b+c+d

print(add(1,2))
print(add(1,4))

#可变参数
def fun(*number):
    sum = 1
    for n in number:
        sum = sum * n
    return sum

print(fun(1,2,3,4,5,6,7,8))
