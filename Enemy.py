from Characteristics import Characteristics

class Enemy(Characteristics):

    def __init__(self,x,y,width,height,color,health,row):
        super().__init__(x,y,width,height,color,health)
        self.row = row
        self.canShoot = False
        self.cooldown = .5

    def spawn(self):
        pass