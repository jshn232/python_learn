#!/usr/bin/env python3

class Screen(object):
    def __init__(self):
        self._width = 0
        self._height = 0
        self._area = 0

    def __iter__(self):
        return self

    def __next__(self):
        self._width  = self._width +1
        self._height = self._height + 1
        self._area = self._width * self._height
        if self._area > 1000:
            raise StopIteration()
        return self._area

    def __getitem__(self, item):
        for n in item

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,value):
        self._width = value

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def area(self):
        self._area = self._width * self._height
        return self._area


s = Screen()
s.width = 20
s.height = 10

print('width is %d' % s.width)
print('height is %d' % s.height)
print('area is %d' % s.area)


for n in s:
    print(n)