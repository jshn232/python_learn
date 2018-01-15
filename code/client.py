#!/usr/bin/env python3

import socket,time,datetime

HOST = '127.0.0.1'
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORT))

while True:

    cmd = input('input msg:')

    s.send(cmd.encode(encoding='utf_8', errors='strict'))

    data = s.recv(1024).decode(encoding='utf_8', errors='strict')

    t = time.time()
    print('now',int(round(t*1000)))

    print('>>>',data)