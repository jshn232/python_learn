#!/usr/bin/env python3

def mutiply(a,b):
    """
    >>> mutiply(1,2)
    2
    >>> mutiply(2,3)
    5
    """

    return a*b


if __name__ == '__main__':
    import doctest
    doctest.testmod()