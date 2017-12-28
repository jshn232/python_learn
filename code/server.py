#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8989

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen(5)

print('Server start at:%s:%s' %(HOST,PORT))

print('wait for connection.....')

while True:
    conn,addr = s.accept()
    print('Connect by',addr)

    while True:
        date = conn.recv(1024).decode(encoding='utf_8', errors='strict')
        print(date)

        date = 'recv date'
        conn.send(date.encode(encoding='utf_8', errors='strict'))

