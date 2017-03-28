#!/usr/bin/env python3

l = (x * x for x in range(10))

print(next(l))
print(next(l))
print(next(l))

for n in l:    #注意，l已经迭代至第三个
    print(n)


def lib(max):
    n = 0
    while n < max:
        x = n * n
        yield x
        n = n + 2
    return

l = lib(10)

for n in l:
    print(n)


def triangles():
    l = []
    loop = 0
    while 1:
        l1 = []
        x = 0
        while x < len(l):
            if x == 0:
                l1.append(1)
            else:
                l1.append(l[x] + l[x-1])
            x = x + 1
        if x == len(l):
            l1.append(1)
        yield l1
        l = l1
        loop = loop + 1
    return

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

def trianges2():
    L = [1]
    while True:
        yield L
        newL = [L[i] + L[i + 1] for i in range(len(L) - 1)]
        L = newL
        L.insert(0, 1)
        L.append(1)
    return 'done'

n = 0
for t in trianges2():
    print(t)
    n = n + 1
    if n == 10:
        break


for i in range(10):
    print(i)