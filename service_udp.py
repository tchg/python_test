#!/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys

# 获取tcp/ip套接字
tcpsocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM) 
# 获取udp/ip套接字
udpSocket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM)

# 获取本地主机名
host = '198.13.44.158'

port = 9999

# 绑定端口号
udpSocket.bind((host, port))

# 设置最大连接数，超过后排队
tcpsocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = tcpsocket.accept()      
    print(tcpsocket.recvfrom())
    print("连接地址: %s" % str(addr))
    
    msg='欢迎访问菜鸟教程！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()