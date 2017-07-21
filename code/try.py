#!/usr/bin/env python3
import logging

logging.basicConfig(level=logging.DEBUG)

def fun(a,b):
    print('a:',a,';','b:',b)
    try:
        print('try....')
        r = a/b
        print('result:',r)
    except ZeroDivisionError as e:
        print('except:',e)
    except ValueError as e:
        print('except:',e)
    else:
        print('no Error!')
    finally:
        print('finally.....')
    print('End')


#fun(10,0)
#fun(0,10)

def fun_log(a,b):
    print('a:', a, ';', 'b:', b)
    try:
        print('try....')
        logging.debug('a=%d' % a)
        logging.debug('b=%d' % b)
        r = a / b
        print('result:', r)
    except ZeroDivisionError as e:
        logging.exception(e)
    except ValueError as e:
        logging.exception(e)
    else:
        print('no Error!')
    finally:
        print('finally.....')
    print('End')

fun_log(10,0)