#!/usr/bin/env python3



def fun_han(n,A,B,C):
    if(n == 1):
#        print('move', A, 'to', B)
        print('move', A, 'to', C)
    else:
        fun_han(n-1,A,C,B)
#        print('move', A, 'to', B)
        print('move', A, 'to', C)
        fun_han(n-1,B,A,C)
    return


fun_han(8,'A','B','C')