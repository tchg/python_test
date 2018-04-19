#!/usr/bin/python3
from PIL import ImageGrab
import datetime
old = datetime.datetime.now()
print(old)
cut = ((0,0,1,1),(1,0,2,1),(2,0,3,1),(3,0,4,1),
       (0,1,1,2),(1,1,2,2),(2,1,3,2),(3,1,4,2),
       (0,2,1,3),(1,2,2,3),(2,2,3,3),(3,2,4,3),
       (0,3,1,4),(1,3,2,4),(2,3,3,4),(3,3,4,4))

# 截屏函数，进行截屏
def Screenshot(cut):
    im = ImageGrab.grab()
    #im.save('zz.jpg')
    (width,height) = im.size
    width,height = width/4,height/4
    for i in range(16):
        Cut_up(im,width,height,cut[i]).save(str(i)+'.jpg')
        
# 进行切片处理
def Cut_up(im, width, height, cut):
    cp = (width*cut[0],height*cut[1],width*cut[2],height*cut[3])
    im = im.crop(cp)
    return im

for i in range(5):
    Screenshot(cut)
    print(1)
new = datetime.datetime.now()


print(new)
print((new-old))