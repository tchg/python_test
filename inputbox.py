from PIL import ImageGrab
import PIL
import io
im = ImageGrab.grab()
(width,height) = im.size
width,height = width/4,height/4
cp = (width*0,height*0,width*1,height*1)
im = im.crop(cp)
imgbuf = io.StringIO(im)
imgbuf.show()