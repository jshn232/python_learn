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
    print("the number is " , number, "\nsum is %d" % sum)
    return sum

print(fun(1,2,3,4,5,6,7,8))

lll = [1, 2, 3, 4, 5, 6, 7]
print(fun(*lll))

print(fun())


#关键字参数
def fun_key(key1,key2,key3='key3', **keys):
    print(key1,key2,key3,keys)
    print(keys['key_1'])
    if 'key_1' in keys:
        print('key_1 in keys is ',keys['key_1'])
    if 'key_2' in keys:
        pass
    print('key_2 in keys is ',keys['key_2'])
    return

fun_key(1,2,key_3='str_3',key_1='str_1',key_2='str_2')


def fun_key_1(key1,key2,*,key3,key4):
    print(key1)
    print(key2)
    print(key3)
    print(key4)
    return

fun_key_1(1,2,key3=3,key4=4)


def fun_key_2(*keys,key3,key4):
    print(keys)
    print(key3)
    print(key4)
    return

l = [1,2,3,4,5]
fun_key_2(l,key3=6,key4=7)

def fun_key_3(*,key3,key4,**keys):
    print(keys)
    print(key3)
    print(key4)
    return

fun_key_3(key3=1,key4=2,key5=3,key6=4)


def fun_key_4(*key1,**key2):
    print('key1 is',key1)
    print('key2 is',key2)
    return

k1 = (1,2,3,4,5,6,7,8)
k3 = (3,3,3,3,3)
k2 = {'kk1':1,'kk2':2}
fun_key_4(key1=k1,key2=k2)