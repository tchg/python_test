import socket

PORT = 9002
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("192.168.1.138", PORT)
server_socket.bind(address)
while True:
    receive_data, client_address = server_socket.recvfrom(1024)
    print("接收到了客户端 %s 传来的数据: %s" % (client_address, receive_data.decode()))