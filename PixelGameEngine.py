from array import array
from enum import Enum
import sys, pygame
pygame.init()

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
    self.__surface = None
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.__surface = pygame.Surface(width,height)

    def setPixel(self,x,y,pix):
        if (x >= 0 and x < width) and (y>=0 and y < height):
            self.__surface.set_at((x,y),Color(pix.r, pix.g, pix.b,pix.a))
            
            return True
        else:
            return False
    
    def getPixel(self,x,y):
        if (x >= 0 and x < width) and (y>=0 and y < height):
            color = self.__surface.get_at((x,y))
            return Pixel(color.r,color.g,color.b,color.a)
        else:
            return Blank
    
    def clear(self,pix):
        self.__surface.fill(Color(pix.r, pix.g, pix.b,pix.a))
            
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
        

class PixelMode(Enum):
    Normal = 0
    Mask = 1
    Alpha = 2
    Custom = 3
  
        
class PGE:
    
    app_name = "PGE"
    draw_target = None
    current_draw_target = 0
    window = None
    current_mouse_state = []
    current_key_state = []
    previous_mouse_state = []
    previous_key_state = []
    active = False
    screen_width = 0
    screen_height = 0
    pixel_width = 1
    pixel_height = 1
    mouse_pos_x = 0
    mouse_pos_y = 0
    font = None
    frame_timer = 0
    frame_count = 0
    mode = None
    blend_factor = 0
    func_pixel_mode = None
    
    def __init__(self,name,width,height,pixel_w,pixel_h):
        self.app_name = name
        self.draw_target= []
        self.winodws = None
        self.previous_mouse_state = [False,False,False]
        self.previous_key_state = [False]*256
        self.current_mouse_state = [[HWButton(),HWButton(),HWButton()]]
        self.current_key_state = []
        for x in range(256):
            self.current_key_state.append(HWButton())
        self.active = True
        self.screen_width = int(width)
        self.screen_height = int(height)
        self.pixel_width = int(pixel_w)
        self.pixel_height = int(pixel_h)
        self.mouse_pos_x = 0
        self.mouse_pos_y = 0
        self.font = PGE.construct_font_sheet()
        self.frame_count = 0
        self.frame_timer = 1.0
        self.mode = PixelMode.Normal
        self.blend_factor = 1.0
        self.func_pixel_mode = None
        self._screen = None
            
    def on_user_create(self):
        return True
        
    def on_user_update(self,elapsed_time):
        return True
    
    def on_user_destroy(self):
        pass
        
    def construct_font_sheet():
        return None
        
    def start(self):
        self._screen = pygame.display.set_mode((self.width*self.pixel_width,self.height*self.pixel_height))
        self._surface = self._screen.get_surface()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            
            #Update Key States
            new_key_state = pygame.key.get_pressed()
            for x in range(256):
                if(new_key_state[x] != self.previous_key_state[x]):
                    if new_key_state[x]:
                        self.current_key_state[x].pressed = !self.current_key_state[i].held
                        self.current_key_state[x].held = True
                    else:
                        self.current_key_state[x].released = true;
                        self.current_key_state[x].held = false;
                self.previous_key_state[i] = new_key_state[i];
              
            #Update Mouse States
            new_mouse_state = pygame.mouse.get_pressed()
            for x in range(3):
                self.current_mouse_state[x].pressed = False
                self.current_mouse_state[x].released = False
                
             
                if new_mouse_state[x] != self.previous_mouse_state[x]:
                    if new_mouse_state[x]:
                        self.current_mouse_state[x].pressed = !self.current_mouse_state[i].held
                        self.current_mouse_state[i].held = True
                    else:
                        self.current_mouse_state[x].released = True
                        self.current_mouse_state[x].held = False
              
                self.previous_mouse_state[i] = new_mouse_state[i];
 
            #Update mouse pos
            
            mouse_pos = pygame.mouse.get_pos()
            
            self.mouse_pos_x = mouse_pos[0] / self.pixel_width
            self.mouse_pos_y = mouse_pos[1] / self.pixel_height
            
            if self.mouse_pos_x >= self.screen_width:
                self.mouse_pos_x = self.screen_width - 1
            if self.mouse_pos_y >= self.screen_height:
                self.mouse_pos_y = self.screen_height - 1
            if self.mouse_pos_x < 0:
                self.mouse_pos_x = 0
            if self.mouse_pos_y < 0:
                self.mouse_pos_y = 0;
                
            
            self._screen.flip()
                
            
            