class Bullet:

    def __init__(self,x,y,width,height,color,step):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.step = step

    def moveUp(self):
        self.y -= self.step

    def moveDown(self):
        self.y += self.step
    


    