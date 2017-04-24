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