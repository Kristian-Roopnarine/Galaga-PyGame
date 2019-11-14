from Characteristics import Characteristics

class Enemy(Characteristics):

    def __init__(self,x,y,width,height,color,health,canShoot):
        super().__init__(x,y,width,height,color,health)
        self.canShoot = canShoot
        self.cooldown = 0.5

    def spawn(self):
        pass