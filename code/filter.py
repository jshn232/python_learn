#!/usr/bin/env python3

#C的写法
def isValue(n):
    s = str(n)
    n1 = 0
    n2 = -1
    while(True):
        if s[n1]!=s[n2]:
            return False
        else:
            n1 = n1+1
            n2 = n2-1
            if n1 >= len(s)/2:
                return True
    return  True


#数组颠倒
s = '123456'
print(s)
s = s[::-1]
print(s)

#Python的写法
def isValue_2(n):
    s = str(n)
    return s == s[::-1]



#两个函数对应的输出结果
l = list(filter(isValue,range(1,1000)))
l2 = list(filter(isValue_2,range(1,1000)))

#结果是一样的
for nn in l:
    print(nn)

for nn in l2:
    print(nn)


