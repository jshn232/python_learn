#!/usr/bin/env python3
print('#tuple 1-5')
nums = (1,2,3,4,5)
for num in nums:
    print('%d' % num)

print('range(10)')
nums = range(10)
for num in nums:
    print('%d' % num)

print('#list(range(20))')
nums = list(range(20))
for num in nums:
    print('%d' % num)


print('#while sum:0~100')
loop = 0
sum = 0

while loop <= 100:
    sum += loop
    loop = loop + 1

print('sum = %d' % sum)



print('#break in while')

loop = 100
sum = 0

while loop >= 0:
    if(sum > 3000):
        print('loop = %d' % loop)
        print('sum = %d' % sum)
        break
    sum = sum + loop

print('loop = %d' % loop)
print('sum = %d' % sum)

loop = 0
num = 1
print('#odd in 1~10')
while(loop < 10):
    loop = loop + 1
    if(0 == loop % 2):
        continue
    print('odd in 0~10 No.%d : %d' % (num, loop))
    num = num + 1

