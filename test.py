from PIL import ImageGrab
from PIL import ImageChops
im1 = ImageGrab.grab()
(width,height) = im.size
width,height = width/4,height/4
print(1)
im2 = ImageGrab.grab()
out = ImageChops.logical_and(im1,im2)
out.save('1.jpg')

