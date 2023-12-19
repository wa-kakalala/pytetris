import pygame
import sys


bgpic = [
     ["./resource/background/bg1/",4],
     ["./resource/background/bg2/",4],
     ["./resource/background/bg3/",5],
     ["./resource/background/bg4/",4]
]


class ScreenClass:
    screenw,screenh = 0,0
    tiles = [] 
    bgindex = 1
    resclasser = None
    tileclasser = None
    def __init__(self,screenw,screenh,caption,iconimgpath,tilespath,resclasser,tileclasser):
        pygame.init()
        # pygame.NOFRAME
        self.screenw,self.screenh = screenw,screenh
        self.screen = pygame.display.set_mode((self.screenw,self.screenh))
        # resources class
        self.resclasser = resclasser
        # tile class
        self.tileclasser = tileclasser
        # set caption
        pygame.display.set_caption(caption)
        iconimg = pygame.image.load(iconimgpath).convert_alpha()
        # set icon
        pygame.display.set_icon(iconimg)
        # set bgimg
        self.showbg()
        self.tiles.append(pygame.image.load(tilespath + "blue.png").convert_alpha())
        self.tiles.append(pygame.image.load(tilespath + "brown.png").convert_alpha())
        self.tiles.append(pygame.image.load(tilespath + "green.png").convert_alpha())
        self.tiles.append(pygame.image.load(tilespath + "grey.png").convert_alpha())
        self.tiles.append(pygame.image.load(tilespath + "red.png").convert_alpha())
        self.tiles.append(pygame.image.load(tilespath + "yellow.png").convert_alpha())
        for index in range(len(self.tiles)):
            w,h = self.tiles[index].get_size()
            # 32 x 32
            self.tiles[index] = pygame.transform.smoothscale(self.tiles[index],(w//2,h//2))
    
    def showbg(self):
        pic_path,pic_num = self.resclasser.get_bg_pic(self.bgindex)
        for i in range(1,pic_num):
            self.screen.blit(pygame.image.load(pic_path + str(i) + ".png").convert_alpha(),(0,0))
    
    def srceenUpdate(self):
        self.showbg()
        self.test()
        self.showtilemap()

        pygame.display.update()
        
    def showtilemap(self):
        for y in range(self.tileclasser.get_map_height()):
            for x in range( self.tileclasser.get_map_width()):
                if self.tileclasser.get_map_yx(y,x) != 0:
                    self.screen.blit(self.tiles[self.tileclasser.get_map_yx(y,x)],(33 *x + 3,3+y*33)) 
    
    def test(self):
        # blit : 33 X 33  leave 1 gap
        self.tileclasser.set_map_yx(1,1,1)
        self.tileclasser.set_map_yx(1,10,5)

    def screenchangebg(self):
        self.bgindex =  1 if self.bgindex == 4 else  self.bgindex + 1
             
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        self.screenchangebg()

            self.srceenUpdate() 