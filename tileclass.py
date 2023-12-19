
GAME_MAP_ROW = 10
GAME_MAP_COL = 15
class TileClass :
    # game map
    gamemap = None 
    mapcol,maprow = 0,0
    def __init__(self,maprow,mapcol)->None:
        self.gamemap = [[ 0 for i in range(mapcol)] for j in range(maprow)]
        self.mapcol,self.maprow = mapcol,maprow
    def get_map_height(self)->int:
        return self.maprow
    def get_map_width(self)->int:
        return self.mapcol
    def get_map_yx(self,y,x)->int:
        return self.gamemap[y][x]
    def set_map_yx(self,y,x,v)->None:
        self.gamemap[y][x] = v