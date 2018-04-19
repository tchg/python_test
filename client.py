import socket
from PIL import ImageGrab
from PIL import Image
im = ImageGrab.grab()
#im = im.load()
print(im.format)


# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #msg =  # 字符串类型， 通过msg.encode() 编码 转换为bytes类型
# server_address = ("192.168.1.138", 9002)  # 接收方 服务器的ip地址和端口号
# client_socket.sendto(im, server_address)
# client_socket.close()