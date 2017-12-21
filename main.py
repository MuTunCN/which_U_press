import pygame, os, sys

class keyboard_2_btn:
    def __init__(self, up, down, left, right, a, b, x, y):
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.a = a
        self.b = b
        self.x = x
        self.y = y

def game_kb(k2b):
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    pygame.init()
    size = [100, 50]
    screen = pygame.display.set_mode(size,pygame.NOFRAME)

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
            if event.type == pygame.KEYDOWN:
                name = pygame.key.name(event.key)
                if name == "escape":
                    done=True
                if name == k2b.up:
                    KEY_U.alpha = 255
                elif name == k2b.left:
                    KEY_L.alpha = 255
                elif name == k2b.down:
                    KEY_D.alpha = 255
                elif name == k2b.right:
                    KEY_R.alpha = 255
                elif name == k2b.x:
                    KEY_X.alpha = 255
                elif name == k2b.a:
                    KEY_A.alpha = 255
                elif name == k2b.b:
                    KEY_B.alpha = 255
                elif name == k2b.y:
                    KEY_Y.alpha = 255
            if event.type == pygame.KEYUP:
                name = pygame.key.name(event.key)
                if name == k2b.up:
                    KEY_U.alpha = 60
                if name == k2b.left:
                    KEY_L.alpha = 60
                if name == k2b.down:
                    KEY_D.alpha = 60
                if name == k2b.right:
                    KEY_R.alpha = 60
                if name == k2b.x:
                    KEY_X.alpha = 60
                if name == k2b.a:
                    KEY_A.alpha = 60
                if name == k2b.b:
                    KEY_B.alpha = 60
                if name == k2b.y:
                    KEY_Y.alpha = 60
                    

        screen.fill(BLACK)
        for key_btn in keys_btn:
            blit_alpha(screen,key_btn.image,key_btn.postion, key_btn.alpha)
        for key_pos in keys_pos:
            blit_alpha(screen,key_pos.image,key_pos.postion, key_pos.alpha)
        


    


        
        pygame.display.flip()

        # Limit to 20 frames per second
        clock.tick(10)
        
    pygame.quit ()

def game_joystick():
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    pygame.init()
    size = [100, 50]
    screen = pygame.display.set_mode(size,pygame.NOFRAME)

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
if __name__ == '__main__':
    while True:
        choose = input("""
        输入显示器,选择你要的操作
        1.启动对手柄的映射(需要连接上手柄)
        2.设置键盘映射并启动
        3.启动对键盘的映射(默认映射)
        4.退出
        """)
        if choose == '1':
            game_joystick()
        elif choose == '2':
            u = input("输入<上>键的映射:")
            d = input("输入<下>键的映射:")
            l = input("输入<左>键的映射:")
            r = input("输入<右>键的映射:")
            a = input("输入<A>键的映射:")
            b = input("输入<B>键的映射:")
            x = input("输入<X>键的映射:")
            y = input("输入<Y>键的映射:")
            k2b = keyboard_2_btn(u, d, l, r, a, b, x, y)
            game_kb(k2b)
        elif choose == '3':
            k2b = keyboard_2_btn('w', 's', 'a', 'd', 'j', 'k', 'l', 'space')
            game_kb(k2b)
        elif choose == '4':
            sys.exit()
        else:
            print("憋瞎逼按！")