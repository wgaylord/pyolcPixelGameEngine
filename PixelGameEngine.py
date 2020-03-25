from array import array

class Pixel:
    r = 0
    g = 0
    b = 0
    a = 255
    
    def __init__(self,red=0,green=0,blue=0,alpha=255):
        self.r = red
        self.g = green
        self.b = blue
        self.a = alpha      

    def clone(self):
        return Pixel(self.r,self.g,self.n,self.a)
        
    def set(self,pix):
        self.r = pix.r
        self.g = pix.g
        self.b = pix.b
        self.a = pix.a
        
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


class HWButton:
    pressed = False
    released = False
    held = False

    def __init__(self):
        pass


class Sprite:
    width = 0
    height = 0
    colorData = None
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.colorData = [0]*(width*height)
        i = 0
        while i < len(self.colorData):
            self.colorData[i] = Pixel(alpha=0)
    
    def setPixel(self,x,y,pix):
        if (x >= 0 and x < width) and (y>=0 and y < height):
            self.colorData[y*self.width + x].set(pix)
            return True
        else:
            return False
    
    def getPixel(self,x,y):
        if (x >= 0 and x < width) and (y>=0 and y < height):
            return self.colorData[y*self.width + x]
        else:
            return Blank
    
    def clear(self,pix):
        i = 0
        while i < len(self.colorData):
            self.colorData[i].set(pix)
            
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def getData(self):
        return self.colorData
        
    
        
class PGE:
    
    app_name = "PGE"
    draw_target = None
    current_draw_target = 0
    window = None
    current_mouse_state = []
    current_mouse_state = []
    previous_mouse_state = []
    previous_key_state = []
    active = False
    screen_width = 0
    screen_height = 0
    pixel_width = 0
    pixel_height = 0
    mouse_pos_x = 0
    mouse_pos_y = 0
    font = None
    frame_timer = 0
    frame_count = 0
    mode = None
    blend_factor = 0
    func_pixel_mode = None
    
    def __init__(self,name,width,height,pixel_w,pixel_h):

        pass
            
    
    
