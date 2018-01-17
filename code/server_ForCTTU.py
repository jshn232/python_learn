#!/usr/bin/python3

import socket,threading,time,datetime,select

lt_socket = []
lt_port = []
lt_time_wait = [10,60,10,10,10]

addr_local = '127.0.0.1'

Max_Socket_Num = 5
Define_Port = 6000


for i in range(Max_Socket_Num):
    s_Tmp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    lt_socket.append(s_Tmp)
    lt_port.append(Define_Port + i)
    lt_socket[i].bind((addr_local,lt_port[i]))
    print('socket_%s ip:%s,port:%s'%(i,addr_local,lt_port[i]))
    print('socket time wait is %ss'%lt_time_wait[i])

def writefile(buf,no):
    with open('/Users/jshn/Desktop/%s'%(Define_Port+no),'a') as f:
        f.write(time.strftime("%Y-%m-%d %H:%M:%S\n", time.localtime()))
        f.write(buf+'\n\n')

def tcplink(sock,no):
    sock.listen(1)
    print('listen port %s'%(Define_Port+no))
    try:
        s, add = sock.accept()
    except :
        print('accept Error %s'%no)
        s.close()
        return
    print('accept port %s'%(Define_Port+no))
    writefile('accept,Wait %ss' % lt_time_wait[no], no)
    #oldtime = datetime.datetime.now()
    s.setblocking(0)

    while True:
        try:
            ready = select.select([s], [], [], lt_time_wait[no])
            if ready[0]:
                date = s.recv(256)
            else:
                writefile('No Recv Date in %ss'%lt_time_wait[no], no)
                continue
            if not date:
                s.close()
                print('socket close %s'%(Define_Port+no))
                writefile('Link cut by client', no)
                s, add = sock.accept()
                print('accept port-2 %s' % (Define_Port + no))
                continue
            else:
                #newtime = datetime.datetime.now()
                #second = (newtime-oldtime).seconds
                #if second > 10:
                    #writefile('second is %s' %second, no)
                #oldtime = newtime
                pass
        except :
            print('recv Error %s'%no)
            s.close()
            return
    return

for i in range(Max_Socket_Num):
    t = threading.Thread(target=tcplink, args=(lt_socket[i],i))
    t.start()
