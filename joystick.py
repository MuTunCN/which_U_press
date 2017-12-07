import pygame, os
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
pygame.init()
size = [100, 50]
screen = pygame.display.set_mode(size,pygame.RESIZABLE)

pygame.display.set_caption("joystick show")

class Btn(pygame.sprite.Sprite):
    def __init__(self,image_path, alpha, pos):
        super(Btn, self).__init__()
        self.image = pygame.image.load(image_path)
        self.alpha = alpha
        self.postion = pos
CURRENT_PATH = os.path.dirname(__file__)
KEY_Y = Btn(os.path.join(CURRENT_PATH,'y.png'), 60, (60,0))
KEY_X = Btn(os.path.join(CURRENT_PATH,'x.png'), 60, (45,15))
KEY_A = Btn(os.path.join(CURRENT_PATH,'a.png'), 60, (60,30))
KEY_B = Btn(os.path.join(CURRENT_PATH,'b.png'), 60, (75,15))
KEY_U = Btn(os.path.join(CURRENT_PATH,'u.png'), 60, (16,5))
KEY_D = Btn(os.path.join(CURRENT_PATH,'d.png'), 60, (16,34))
KEY_L = Btn(os.path.join(CURRENT_PATH,'l.png'), 60, (0,21))
KEY_R = Btn(os.path.join(CURRENT_PATH,'r.png'), 60, (29,21))

keys_btn = pygame.sprite.Group()
keys_pos = pygame.sprite.Group()
keys_btn.add(KEY_Y)
keys_btn.add(KEY_X)
keys_btn.add(KEY_A)
keys_btn.add(KEY_B)
keys_pos.add(KEY_L)
keys_pos.add(KEY_R)
keys_pos.add(KEY_U)
keys_pos.add(KEY_D)
#Loop until the user clicks the close button.
done = False    

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
def joystick_init():
    pygame.joystick.init()
joystick_init()
    
def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)        
        target.blit(temp, location)


while done==False:
    # EVENT PROCESSING STEP

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True # Flag that we are done so we exit this loop
        if event.type == pygame.JOYAXISMOTION:
            x,y = joystick.get_axis(0),joystick.get_axis(1)
            for key_pos in keys_pos:
                key_pos.alpha = 60
            if x > 0.1:
                KEY_R.alpha = 255
                if y > 0.1:
                    KEY_D.alpha = 255
                elif  y < -0.1:
                    KEY_U.alpha = 255
            elif y > 0.1:
                KEY_D.alpha = 255
                if x > 0.1:
                    KEY_R.alpha = 255
                elif  x < -0.1:
                    KEY_L.alpha = 255
            elif  y < -0.1:
                KEY_U.alpha = 255
                if x > 0.1:
                    KEY_R.alpha = 255
                elif  x < -0.1:
                    KEY_L.alpha = 255
            elif x < -0.1:
                KEY_L.alpha = 255
                if y > 0.1:
                    KEY_D.alpha = 255
                elif  y < -0.1:
                    KEY_U.alpha = 255

        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                KEY_A.alpha = 255
            elif event.button == 1:
                KEY_B.alpha = 255
            elif event.button == 2:
                KEY_X.alpha = 255
            elif event.button == 3:
                KEY_Y.alpha = 255
        if event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                KEY_A.alpha = 60
            elif event.button == 1:
                KEY_B.alpha = 60
            elif event.button == 2:
                KEY_X.alpha = 60
            elif event.button == 3:
                KEY_Y.alpha = 60            

    screen.fill(BLACK)
    for key_btn in keys_btn:
        blit_alpha(screen,key_btn.image,key_btn.postion, key_btn.alpha)
    for key_pos in keys_pos:
        blit_alpha(screen,key_pos.image,key_pos.postion, key_pos.alpha)
    

    joystick = pygame.joystick.Joystick(0)
    joystick.init()

 


    
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(10)
    
pygame.quit ()