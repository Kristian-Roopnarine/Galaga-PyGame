from Characteristics import *
import time

class Player(Characteristics):

    def __init__(self,x,y,width,height,color,health,steps):
        super().__init__(x,y,width,height,color,health)
        self.steps = steps
        self.score = 0
        self.cooldown = 0.4
        self.timer_ = 0
        self.start_cooldown = 0

    def moveLeft(self):
        self.x -= self.steps

    def moveRight(self):
        self.x += self.steps

    def incScore(self):
        self.score += 1
    '''
    def resetCooldown(self):
        self.start_cooldown = time.time()

    def onCooldown(self):
        self.timer_ = time.time() - self.start_cooldown
        return self.timer_ > self.cooldown
    '''





