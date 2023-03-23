
GAME_MAP_ROW = 10
GAME_MAP_COL = 15
class TileClass :
    # game map 
    def __init__(self,mapRow,mapCol):
        gamemap = [[ 0 for i in range(mapCol)] for j in range(mapRow)]
