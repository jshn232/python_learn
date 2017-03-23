#!/usr/bin/env python3

L = ['slice1','slice2','slice3','slice4','slice5']

print(L[0:3])
print(L[2:4])

L2 = list(range(10))

print(L2[-3:])

print(L2[:])


print(tuple(range(20))[:])

print(tuple(range(20))[2::3])