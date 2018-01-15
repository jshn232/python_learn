#!/usr/bin/env python3

import socket,threading,time,datetime

s = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 6666
add = (ip,port)
s.bind(add)

s.listen(5)
print('listening....')

def tcplink(sock,addr):
    print('socket accept form %s %s' %addr)

    while True:
        date = sock.recv(1024)
        #time.sleep(1)
        if not date:
            break
        print('>>>>>>' , date.decode('utf-8').encode('utf-8'))
        #sock.send(('recv').encode('utf-8'))
        t = time.time()
        t = int(round(t*1000))
        time.sleep(0.001)
        sock.send(('%s'%t).encode('utf-8'))
    sock.close()
    print('connect close from %s %s'%addr)


while True:
    sock, addr = s.accept()

    t = threading.Thread(target=tcplink, args=(sock,addr))

    t.start()