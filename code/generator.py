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
        n = n + 1
    return

l = lib(10)

for n in l:
    print(n)