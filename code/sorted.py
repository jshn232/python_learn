#!/usr/bin/env python3

l = ('zz','Crazy','Fun','_X','A')
l = sorted(l,key=str.lower)
print(l)

L = [('Bob',18),('Jhon',16),('Jay_z',20)]

def sort_name(t):
    return t[0].lower()

def sort_year(t):
    return t[1]

L1 = sorted(L,key=sort_name)
print(L1)

L2 = sorted(L,key=sort_year,reverse=True)
print(L2)

#待完成
d = {'port_4':8989, 'Port_2':8991, 'Port_5':9000}

def sort_key(t):
    return t.keys()

def sort_values(t):
    return t.values()

#d1 = sorted(d,key=sort_key)
#print(d1)