from array import array

class Pixel:
    r = 0
    g = 0
    b = 0
    a = 255
    n = 0xFF000000
    
    def __init__(self,red=0,green=0,blue=0,alpha=255):
        self.r = red
        self.g = green
        self.b = blue
        self.a = alpha
        self.n = self.a<<24 | (self.r<<16) | (self.g<<8) | self.b
        
        
    def __eq__(self,obj):
        if isinstance(obj,Pixel):
            if self.n == obj.n:
                return True
        return False
        
    def __setitem__(Self,item,value):
        self._dict[item] = value
        self.n = self.a<<24 | (self.r<<16) | (self.g<<8) | self.b
        
    
WHITE = Pixel(255,255,255)
GREY = Pixel(192,192,192)
DARK_GREY = Pixel(128,128,128)
VERY_DARK_GREY = Pixel(64,64,64)
RED = Pixel(255)
DARK_RED = Pixel(128)
VERY_DARK_RED = Pixel(64)
YELLOW = Pixel(255,255)
DARK_YELLOW = Pixel(128,128)
VERY_DARK_YELLOW = Pixel(64,64)
GREEN = Pixel(0,255)
DARK_GREEN = Pixel(0,128)
VERY_DARK_GREEN = Pixel(0,64)
CYAN = Pixel(0,255,255)
DARK_CYAN = Pixel(0,128,128)
VERY_DARK_CYAN = Pixel(0,64,64)
BLUE = Pixel(0,0,255)
DARK_BLUE = Pixel(0,0,128)
VERY_DARK_BLUE = Pixel(0,0,64)
MAGENTA = Pixel(255,0,255)
DARK_MAGENTA = Pixel(128,0,128)
VERY_DARK_MAGENTA = Pixel(64,0,64)
BLACK = Pixel()
BLANK = Pixel(alpha=0)



class Sprite:
    width = 0
    height = 0
    colorData = None
    
    def __init__(self,width,height,colorData = None):
        self.width = width
        self.height = height
        self.colorData = array("B",[0]*width*height*4)
        if colorData:
            index = 0
            for x in colorData:
                colorData[index] = x.r
                colorData[index+1] = x.g
                colorData[index+2] = x.b
                colorData[index+3] = x.a
                index +=4

