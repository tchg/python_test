#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket             

s = socket.socket()        
#host = '127.0.0.1' 
host = '192.168.1.138'
port = 9999          

s.connect((host, port))

print(s.recv(1024))
s.close()  