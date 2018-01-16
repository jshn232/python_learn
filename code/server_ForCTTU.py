#!/usr/bin/env python3

import socket,threading

lt_socket = []
lt_port = []

addr_local = '127.0.0.1'

Max_Socket_Num = 5
Define_Port = 6000

for i in range(Max_Socket_Num):
    s_Tmp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    lt_socket.append(s_Tmp)
    lt_port.append(Define_Port + i)
    lt_socket[i].bind((addr_local,lt_port[i]))
    print('socket_%s ip:%s,port:%s'%(i,addr_local,lt_port[i]))


def tcplink(sock,no):
    sock.listen(1)
    print('listen port %s'%(Define_Port+no))
    try:
        s, add = sock.accept()
    except :
        print('Error')
        return
    print('accept port %s'%(Define_Port+no))
    while True:
        try:
            date = s.recv(10)
            if not date:
                s.close()
                print('socket close %s'%(Define_Port+no))
                s, add = sock.accept()
                print('accept port %s' % (Define_Port + no))
                continue
        except :
            print('Error')
            return
    return

for i in range(Max_Socket_Num):
    t = threading.Thread(target=tcplink, args=(lt_socket[i],i))
    t.start()
