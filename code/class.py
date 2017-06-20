#!/usr/bin/env python3

class Student(object):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def print_name_id(self):
        print('%s : %s' % (self.name,self.id))
    def get_name_len(self):
        print('len of name is ',len(self.name))

obj = Student('obj1',100)
obj2 = Student('jaceyo',1000)

print(Student)
print(obj)
print(obj.name)
print(obj.id)
print('///////////////////')
obj.print_name_id()
obj.get_name_len()

obj2.print_name_id()
obj2.get_name_len()

print('////////////////////')
Student.get_name_len(obj2)