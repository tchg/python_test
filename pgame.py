import pygame
from PIL import ImageGrab
import PIL
import io


for i in range(100):
    im = ImageGrab.grab()
    print(i)
    #im.show()
    (width,height) = im.size
    width,height = width/2,height/2
    cp = (width*1,height*1,width*2,height*2)
    im = im.crop(cp)
    mode = im.mode
    size = im.size
    data = im.tobytes()
    
    screen=pygame.display.set_mode((960,540))  
    py_image = pygame.image.fromstring(data, size, mode)
    background=py_image
    screen.blit(background,(0,0))  
    pygame.display.update()  