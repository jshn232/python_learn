#!/usr/bin/env python3

l = list(range(100)[1::3])

t = {'t1':1,'t2':2,'t3':3}

for n in l:
    print(n)


for n in t.items():
    print(n)


from collections import Iterable

def fun_Iterable(a):
    print(a,'is Iterable ?',isinstance(a,Iterable))
    return

fun_Iterable(123)
fun_Iterable((1,2,3,4))
fun_Iterable('abc')


for key,value in enumerate(t):
    print(key,value)