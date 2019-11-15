from Characteristics import *
import time

class Enemy(Characteristics):

    def __init__(self,x,y,width,height,color,health,canShoot,row):
        super().__init__(x,y,width,height,color,health)
        self.canShoot = canShoot
        self.cooldown = 1.0
        self.row = row

    def spawn(self):
        pass

    '''
    def resetCooldown(self):
        self.start_cooldown = time.time() 

    def onCooldown(self):
        self.timer_ = time.time() - self.start_cooldown
        return self.timer_ > self.cooldown
    '''
def create_enemies(x,y,canShoot,row):
    return Enemy(x,y,25,25,(255,0,0),2,canShoot,row)
    




