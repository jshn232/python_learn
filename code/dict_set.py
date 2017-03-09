#!/usr/bin/env python3
dict_d = {'port1':8990, 'port2':8991,'port3':8992}

print('port1:%s' % dict_d['port1'])

print('get \'port1\' is %d' % dict_d.get('port1'))

print('get \'port5\' is %d' % dict_d.get('port5',-1))

print('%d' % ('port4' in dict_d))
print('%d' % ('port1' in dict_d))

d_port_password = {8989:'pass1',8990:'pass2'}
print('port:%d,password:%s' % (8989,d_port_password[8989]))


s=set([1,2,3])
