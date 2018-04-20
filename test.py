from PIL import ImageGrab
import numpy
import PIL
import sys
im = ImageGrab.grab()
(width,height) = im.size
width,height = width/4,height/4
cp = (width*0,height*0,width*1,height*1)
im = im.crop(cp)
print(sys.getsizeof(im))
i = numpy.array(im)
print(i.shape)
print(i.ndim)
print(i.itemsize)
print(i.size)
print(type(i))
# im = PIL.Image.fromarray(i[z])




