#!/usr/bin/python3
from PIL import ImageGrab
import datetime
old = datetime.datetime.now()
im = ImageGrab.grab()
# im.show()
#im = im.convert('RGBA')
im = im.load()
for i in range(100,200):
    for j in range(100,200):
        data = im[i,j]
        print(data)

