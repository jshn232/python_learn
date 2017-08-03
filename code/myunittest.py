#!/usr/bin/env python3

import unittest
import doctest

class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)

    def __setattr__(self, key, value):
        self[key]=value

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)


d = Dict(a=1,b=2)

print('a=',d.a)

d.b=3

print('b=',d.b)



class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=2,b=4)
        self.assertEqual(d.a,2)

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()


