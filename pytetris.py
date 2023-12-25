##########
#create by wkk & ryc
##########
from screenclass import ScreenClass
from resclass import ResClass
from tileclass import TileClass

SCREENW,SCREENH = 567,303
CAPTION   = "pytetris"
INCONIMGPATH = "./resource/icon/favicon.ico"
TILESPATH = "./resource/tile/"



def main():
    resclass = ResClass()
    tileclasser = TileClass(SCREENH//33,SCREENW//33)
    screen = ScreenClass(SCREENW,SCREENH,CAPTION,INCONIMGPATH,TILESPATH,resclass,tileclasser)
    # screen.test()
    screen.run()

if __name__ == "__main__":
    main()