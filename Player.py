from Characteristics import Characteristics 

class Player(Characteristics):

    def __init__(self,x,y,width,height,color,health,steps,):
        super().__init__(x,y,width,height,color,health)
        self.steps= steps

    def moveLeft(self):
        pass

    def moveRight(self):
        pass

    def incScore(self):
        pass

    

