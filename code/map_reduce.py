#!/usr/bin/env python3

from functools import reduce

def fun(x):
    return x+x

def fun2(x,y):
    return x+y

l = list(range(1,10))

for n in range(10):
    l = list(map(fun, l))
    print(l)
    r = reduce(fun2,l)
    print(r)


def list2int(x,y):
    return x*10+y

l = [1,2,3,4,5,6]
i = reduce(list2int,l)
print(i)

def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

i = map(char2num,'1234567')

j = reduce(list2int,map(char2num,'1234'))

print(j)


def normalize(name):
    return name[0].upper()+name[1:].lower()

str = ['jshn','apple','STORE']

str = map(normalize,str)

print(list(str))

lll = list(range(20))
print(lll[1:16:3])

def num2char(i):
    return {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}[i]


def s2list(s1,s2):
    return s1+s2

s=list(map(num2char,[1,2,3,4,5,6]))
print(s)
s=reduce(s2list,map(num2char,[1,2,3]))
print(s)
ss='1234567890'
print(ss)
