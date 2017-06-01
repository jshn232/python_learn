#!/usr/bin/env python3

def log(fun):
    def wrapper(*args,**kw):
        print('call %s()',fun.__name__)
        return fun(*args,**kw)
    return wrapper

@log
def now():
    print('2017-06-01')
#等效于
f = log(now)
f()

#now本身
now()

#now的name改变
print('now._name_:',now.__name__)

#log()的name
print('log._name_:',log.__name__)


print('1000 == %04X'% 1000,'== %04d' % 1000)