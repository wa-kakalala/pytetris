##########
#create by wkk & ryc
##########
import pygame
import sys

SCREENW,SCREENH = 576,324
BKIMGPATH = "./resource/background/bg4/"
BKIMGNUM  = 4
CAPTION   = "pytetris"

class ScreenClass:
    bkimg=[]
    screenw,screenh = 0,0
    def __init__(self,screenw,screenh,caption,bkimgpath,bkimgnum = 4):
        pygame.init()
        #pygame.NOFRAME
        self.screenw,self.screenh = screenw,screenh
        self.screen = pygame.display.set_mode((self.screenw,self.screenh))

        for i in range(1,bkimgnum):
            self.bkimg.append(pygame.image.load(bkimgpath + str(i) + ".png").convert_alpha())
            self.screen.blit(self.bkimg[i-1],(0,0))
        pygame.display.set_caption(caption)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()


def main():
    screen = ScreenClass(SCREENW,SCREENH,CAPTION,BKIMGPATH,BKIMGNUM)
    screen.run()

if __name__ == "__main__":
    main()