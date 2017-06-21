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

print('Cla_2')
class Cla_2(object):
    id = 100
    def __init__(self,name,id):
        self.__name = name
        self.__id = id

    def print_name_id(self):
        print('%s is %s' %(self.__name,self.__id))


    def set_name(self,name):
        if 0 <= len(name) <= 10:
            print('name set done!')
            self.__name = name
        else:
            print('bad in')

    def set_id(self,id):
        if 0<= id <= 1000:
            self.__id = id
        else:
            print('bad id')
    def __get_name(self):
        print(self.__name)

    def get_name(self):
        print(self.__name)

    def get_id(self):
        return self.__id


obj_3 = Cla_2('name_1',1000)
obj_3.print_name_id()

obj_3.set_name('jace')
obj_3.set_id(20000)
obj_3._Cla_2__get_name()  #private函数的访问方法
print(obj_3._Cla_2__name)

print('bad ideas~~~~~')
obj_3.__name = 'New'
print(obj_3.__name)

obj_3.get_name()


print('Cla_2_1~~~~~~')

class Cla_2_1(Cla_2):
    def get_name(self):
        print('Cla_2_1')

def get_id(self):
    return self.id


Cla_2_1.get_id = get_id  #动态绑定

obj_4 = Cla_2_1('obj_4',200)
obj_4.get_name()

print(type(obj_4))

print('//////////////////////')
print(obj_4.get_id())