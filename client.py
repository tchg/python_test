import socket
from PIL import ImageGrab
import numpy
import PIL
import sys
im = ImageGrab.grab()
(width,height) = im.size
width,height = width/4,height/4
cp = (width*0,height*0,width*1,height*1)
im = im.crop(cp)
i = str(numpy.array(im[0]))
print(sys.getsizeof(i))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#msg = 'zxczxc'  # 字符串类型， 通过msg.encode() 编码 转换为bytes类型
server_address = ("192.168.1.138", 9002)  # 接收方 服务器的ip地址和端口号
client_socket.sendto(i.encode(), server_address)
client_socket.close()