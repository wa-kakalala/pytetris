class ResClass:
    def __init__(self) -> None:
        self.res_map = {
            "bg_pic": {
                "bg_path" : "./resource/background/",
                "bg_num"  : [0,4,4,5,4]
            },
        }
        
    def get_bg_pic(self,pic_index)-> [str,int]:
        return [
            self.res_map["bg_pic"]["bg_path"] + ("bg%d/"%(pic_index)), 
            self.res_map["bg_pic"]["bg_num"][pic_index]
        ]
