import random
##
# I 型方块，4个小方块组成的一条直线 
#           ####
# O 型方块，4个小方块组成的正方形 
#           ##
#           ##
# T 型方块，4个小方块组成的T型
#           ###
#            #
# Z 型方块，4个小方块组成的Z型
#           ##
#            ##
# S 型方块，4个小方块组成的S型
#           ##
#          ##
# J 型方块，4个小方块组成的J型
#           #
#           #
#          ##
# L 型方块，4个小方块组成的L型
#          #
#          #
#          ##
##
GAME_MAP_ROW = 10
GAME_MAP_COL = 15
class TileTypeClass:
    # [y_step,x_step]
    tiletypes = [
        [   # I 型
            [[0,-1],[0,0],[0,1],[0,2]],  
            [[0, 0],[1,0],[2,0],[3,0]]    
        ],
        [   # O 型
            [[0,0],[0,1],[1,0],[1,0]]
        ],
        [   # T 型
            [[0,-1],[0, 0],[0,1],[1,0]],
            [[1,-1],[0, 0],[1,0],[2,0]],
            [[0, 0],[1,-1],[1,0],[1,1]],
            [[1, 1],[0, 0],[1,0],[2,0]]
        ]
    ]


class TileClass :
    # game map
    gamemap = None 
    mapcol,maprow = 0,0
    now_pos_y,now_pos_x = maprow,0
    tile_type_index,tile_sub_type_index = 0,0
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

    def new_tiles(self):
        if self.now_pos_y > self.maprow-3:
            self.new_tile_random()
            print("here")
        else:
            self.update_tiles()

    def update_tiles(self):
        for index in range(4):
            self.gamemap[self.now_pos_y+TileTypeClass.tiletypes[self.tile_type_index][self.tile_sub_type_index][index][0]][self.now_pos_x+TileTypeClass.tiletypes[self.tile_type_index][self.tile_sub_type_index][index][1]] = 0
        self.now_pos_y += 1
        for index in range(4):
            self.gamemap[self.now_pos_y+TileTypeClass.tiletypes[self.tile_type_index][self.tile_sub_type_index][index][0]][self.now_pos_x+TileTypeClass.tiletypes[self.tile_type_index][self.tile_sub_type_index][index][1]] = 5
    #################
    #  ##
    #  ##
    #################    
    def new_tile_random(self):
        self.now_pos_y,self.now_pos_x = 1,self.mapcol//2
        self.tile_type_index = random.randint(0,2)
        self.tile_sub_type_index = random.randint(0,len(TileTypeClass.tiletypes[self.tile_type_index])-1)
        for index in range(4):
            self.gamemap[self.now_pos_y+TileTypeClass.tiletypes[self.tile_type_index][self.tile_sub_type_index][index][0]][self.now_pos_x+TileTypeClass.tiletypes[self.tile_type_index][self.tile_sub_type_index][index][1]] = 5
        
    
