from Characteristics import Characteristics

class Enemy(Characteristics):

    def __init__(self,x,y,width,height,color,health,row):
        super().__init__(x,y,width,height,color,health)
        self.row = row

    def spawn(self):
        pass