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
fun_Iterable((x*x for x in range(10)))


for key,value in enumerate(t):
    print(key,value)


from collections import Iterator

def fun_Iterator(a):
    print(a,'is Iterator ?',isinstance(a,Iterator))
    return

fun_Iterator(123)
fun_Iterator([x*x for x in range(10)])
fun_Iterator((y+y for y in range(10)))
fun_Iterator(iter([123]))
fun_Iterator(iter('123'))


for n in [1,2,3,4,5]:
    print(n)

i = iter([1,2,3,4,5])
while True:
    try:
        for n in i:
            print('now i is ',n)
            print('next i')
        next(i)

    except StopIteration:
        break