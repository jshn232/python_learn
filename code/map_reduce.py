#!/usr/bin/env python3

def fun(x):
    return x+x

l = list(range(1,10))
for n in range(10):
    print(l)
    l = list(map(fun, l))

