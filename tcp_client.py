#coding=utf-8
from socket import *
import os
s = socket(AF_INET, SOCK_STREAM)
ADDR = ('127.0.0.1', 8888)
s.connect(ADDR)

while 1:
    try:
        c_data=raw_input('Please input :')
        if not c_data:
            break
        s.send(c_data.encode())
        s_data=s.recv(1024)
        print('the messges from server',s_data.decode())
    except KeyboardInterrupt:
        print('异常断开')
        os._exit(0)
    except Exception as e:
        print(e)
s.close()