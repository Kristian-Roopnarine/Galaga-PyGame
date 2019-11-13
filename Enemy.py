from Characteristics import Characteristics

class Enemy(Characteristics):

    def __init__(self,x,y,width,height,color,health):
        super().__init__(x,y,health,height,color,health)

    def spawn(self):
        pass