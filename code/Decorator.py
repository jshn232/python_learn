#!/usr/bin/env python3

import functools

def log(fun):
    @functools.wraps(fun)
    def wrapper(*args,**kw):
        print('call %s()' % fun.__name__)
        return fun(*args,**kw)
    return wrapper

@log
def now():
    print('2017-06-01')
#等效于
f = log(now)
f()
print('/////////////////')
#now本身
now()
print('/////////////////')
#now的name改变
print('now._name_:',now.__name__)

#log()的name
print('log._name_:',log.__name__)


print('1000 == %04X'% 1000,'== %04d' % 1000)


print('__name__is',__name__)



print('///////////////')
def log(fun):
    @functools.wraps(fun)
    def fo(*args,**kw):
        print('log in')
        fun(*args,**kw)
        print('log out')
    return fo

@log
def fooo(x):
    print(x+1)

fooo(4)