#!/usr/bin/env python3

i = int('100')
print(i)

print(int('0x64',base=16))

print(int('01010101',base=2))

print(int('101',base=10))

print('///////////////////////')
import functools

int2 = functools.partial(int,base=16)

i2 = int2('0x1000')

print(i2)

