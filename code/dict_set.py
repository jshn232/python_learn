#!/usr/bin/env python3
dict_d = {'port1':8990, 'port2':8991,'port3':8992}

print('port1:%s' % dict_d['port1'])

print('get \'port1\' is %d' % dict_d.get('port1'))

print('get \'port5\' is %d' % dict_d.get('port5',-1))

print('%d' % ('port4' in dict_d))
print('%d' % ('port1' in dict_d))
