#!/usr/bin/env python3

l = list(map(lambda x:x*x,range(1,20,3)))

print(l)

#等同于
def fun(x):
    return x*x

ll = list(map(fun,range(1,20,3)))

print(ll)


f = lambda x:x*x
print(f)
print(f(3))

def ff(*args):
    for n in args:
        return lambda:n*n


lf = ff(1,2,3,4,5)
print(lf())