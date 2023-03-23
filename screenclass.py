import pygame
import sys


class ScreenClass:
    bkimg=[]
    screenw,screenh = 0,0
    tiles = [] 
    def __init__(self,screenw,screenh,caption,iconimgpath,tilespath,bkimgpath,bkimgnum = 4):
        pygame.init()
        #pygame.NOFRAME
        self.screenw,self.screenh = screenw,screenh
        self.screen = pygame.display.set_mode((self.screenw,self.screenh))

        for i in range(1,bkimgnum):
            self.bkimg.append(pygame.image.load(bkimgpath + str(i) + ".png").convert_alpha())
            self.screen.blit(self.bkimg[i-1],(0,0))
        pygame.display.set_caption(caption)

        iconimg = pygame.image.load(iconimgpath).convert_alpha()
        #set icon
        pygame.display.set_icon(iconimg)
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

    def test(self):
        # blit : 33 X 33  leave 1 gap
        for i in range(3):
                self.screen.blit(self.tiles[0],(40 + 33 *i,10))
        for i in range(2):
                self.screen.blit(self.tiles[0],(40 + 33 *i,10 + 32 + 1))

        for i in range(2):
                self.screen.blit(self.tiles[4],(466 - 33 *i,10 + 198))
        for i in range(3):
                self.screen.blit(self.tiles[4],(400 + 33 *i,10 + 33 + 198))
        
        

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()