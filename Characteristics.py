from Bullet import Bullet
from datetime import date

class Characteristics:

    def __init__(self,x,y,width,height,color,health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.health = health

    def createBullet(self,bullets):
        #find middle of ship/enemy
        x = self.x + (self.width // 2)
        y = self.y + (self.height // 2)

        #create bullet
        bullet = Bullet(x,y,5,10,(255,192,203),5)

        #push bullet into list
        bullets.append(bullet)

    '''def shoot(self,bullets):
        for bullet in bullets:
            if bullet.x < 400 and bullet.x > 0:
                bullet.moveUp()'''

    def isHit(self):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def loseHealth(self):
        self.health -= 1
'''
def reset_cooldown(player):
    player.start_cooldown = date.
    print(player, player.start_cooldown)

def on_cooldown(player):
    player.timer_ = (dt.dt.now() - player.start_cooldown) / 1000
    return player.timer_ < player.cooldown 
'''