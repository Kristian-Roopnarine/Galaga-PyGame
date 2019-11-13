from Characteristics import Characteristics


class Player(Characteristics):

    def __init__(self,x,y,width,height,color,health,steps):
        super().__init__(x,y,width,height,color,health)
        self.steps = steps
        self.score = 0

    def moveLeft(self):
        self.x -= self.steps

    def moveRight(self):
        self.x += self.steps

    def incScore(self):
        self.score += 1





