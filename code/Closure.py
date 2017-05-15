#!/usr/bin/env python3

def sum_1(*args):
    s = 0
    for n in args:
        s = s + n
    return s


print(sum_1(1,2,3,4,5,6))


def lazy_sum(*args):
    def sum_2():
        ss = 0
        for n in args:
            ss = ss + n
        return ss
    return sum_2

print(lazy_sum)

print(lazy_sum(1,2,3,4,5,6))


f = lazy_sum(1,2,3,4,5,6)
print(f())