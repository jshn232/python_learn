#!/usr/bin/env python3
classmate = ['No.1','No.2','No.3', 'No.4']
print('classmate的长度为%02d' % len(classmate))

print('将classmate[-1]修改为\'No.5\'')
classmate[-1] = 'No.5'
print('classmate的最后一个元素为\'%s\'' % classmate[-1])


print('classmate[0]=%s' % classmate[0])
print('classmate[1]=%s' % classmate[1])
print('classmate[2]=%s' % classmate[2])

print('insert\'No.6\'在classmate[1]的位置')

classmate.insert(1,'No.6')
print('classmate[0]=%s' % classmate[0])
print('classmate[1]=%s' % classmate[1])
print('classmate[2]=%s' % classmate[2])
print('classmate[3]=%s' % classmate[3])

print('将classmate修改为tuple！')
classmate = ('No.001', 'No.002')
#classmate[0] = 'No.003'    #tuple不可以修改定义
