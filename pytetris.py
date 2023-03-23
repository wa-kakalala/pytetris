##########
#create by wkk & ryc
##########
from screenclass import ScreenClass

SCREENW,SCREENH = 576,324
BKIMGPATH = "./resource/background/bg4/"
BKIMGNUM  = 4
CAPTION   = "pytetris"
INCONIMGPATH = "./resource/icon/favicon.ico"
TILESPATH = "./resource/tile/"

def main():
    screen = ScreenClass(SCREENW,SCREENH,CAPTION,INCONIMGPATH,TILESPATH,BKIMGPATH,BKIMGNUM)
    screen.test()
    screen.run()

if __name__ == "__main__":
    main()