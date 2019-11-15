import pygame

class Player:
    key = (0,0,0)
    def __init__(self):
        self.x = 250
        self.y = 725
        self.width = 64
        self.height = 64
        self.health = 5
        self.steps = 5
        self.score = 0
        self.reloadTime = 0.4
        self.startCooldown = 0
        self.time_elapsed = 0
        self.char = pygame.image.load('player_ship.png').convert()
    
    def moveLeft(self):
        self.x -= self.steps

    def moveRight(self):
        self.x += self.steps

    def incScore(self):
        self.score += 1

    def resetCooldown(self):
        self.startCooldown = pygame.time.get_ticks()
    
    def updateCooldown(self):
        self.time_elapsed = pygame.time.get_ticks() - self.startCooldown

    def onCooldown(self):
        return self.time_elapsed > self.reloadTime
    
    def isHit(self,bullet):
        for b in bullet:
            b_x = b.getX()
            b_y = b.getY()
            if self.x < b_x < self.x + self.width and self.y < b_y < self.y + self.height:
                bullet.pop(bullet.index(b))
                return True
    
    def loseHealth(self):
        self.health -= 1
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def createBullet(self,bullets):
        #find middle of ship/enemy
        x = self.x + (self.width // 2)
        y = self.y + (self.height // 2)

        #create bullet
        bullet = Bullet(x,y,5,10,(255,192,203),5)

        #push bullet into list
        bullets.append(bullet)
    
class Enemy:
    def __init__(self,x,y,canShoot,row):
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64
        self.health = 3
        self.canShoot = canShoot
        self.row = row
        self.reloadTime = 2
        self.time_elapsed = 0
        self.startCooldown = 0
        self.char = pygame.image.load('player_ship.png').convert_alpha()

    def resetCooldown(self):
        self.startCooldown = pygame.time.get_ticks()
    
    def updateCooldown(self):
        self.time_elapsed = pygame.time.get_ticks() - self.startCooldown

    def onCooldown(self):
        return self.time_elapsed > self.reloadTime
    
    def isHit(self,bullet):
        for b in bullet:
            b_x = b.getX()
            b_y = b.getY()
            if self.x < b_x < self.x + self.width and self.y < b_y < self.y + self.height:
                bullet.pop(bullet.index(b))
                return True
    
    def loseHealth(self):
        self.health -= 1

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def createBullet(self,bullets):
        #find middle of ship/enemy
        x = self.x + (self.width // 2)
        y = self.y + (self.height // 2)

        #create bullet
        bullet = Bullet(x,y,5,10,(255,192,203),5)

        #push bullet into list
        bullets.append(bullet)

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
    
    def getX(self):
        return self.y
    
    def getY(self):
        return self.y
    
def create_enemies(x,y,canShoot,row):
    return Enemy(x,y,canShoot,row)

class Game:
    def __init__(self,win):
        self.width = 600
        self.height = 800
        self.block = 10
        self.background = (0,0,0)
        self.running = True
        self.enemies = []
        self.enemy_bullet_list = []
        self.player_bullet_list = []
        self.win = win
        self.clock = pygame.time.Clock()
    
    def draw(self,win):
        for y in range(self.height//5):
            for x in range(self.width//5):
                rect = pygame.rect(x,y,self.block,self.block)
                pygame.draw.rect(self.win,self.background,rect)

    def generateEnemies(self):
        row = 1
        for y_pos in y:
            for x_pos in x:
                if row == 1:
                    enemy = create_enemies(x_pos,y_pos,True,row)
                    row += 1
                elif row == 2:
                    enemy = create_enemies(x_pos,y_pos,False,row)
                    row += 1
                elif row == 3:
                    enemy = create_enemies(x_pos,y_pos,False,row)
                self.enemies.append(enemy)

    def drawPlayer(self):
        self.win.blit(player_image,(player.x,player.y))

    def drawbullet(self):
        for bullet in self.enemy_bullet_list:
            b = pygame.Rect(bullet.x,bullet.y,bullet.width,bullet.height)
            pygame.draw.rect(self.win,bullet.color,b)

    def drawEnemies(self):
        for enemy in self.enemies:
            self.win.blit(player_image,(enemy.x,enemy.y))
    
    def redraw(self):
        self.win.fill((0,0,0))
        self.drawPlayer()
        self.drawEnemies()
        pygame.display.update()
    
    def endGame(self):
        self.running = False

    def start(self):
        self.drawPlayer()
        self.generateEnemies()
        self.drawEnemies()
        pygame.display.flip()

        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player.x > 0:
                player.moveLeft()
                print(player.x)
            
            if keys[pygame.K_RIGHT] and player.x < self.width - player.width:
                player.moveRight()
                print(player.x)

            self.redraw()

    

def resize(image):
    player_image = pygame.image.load(image).convert()
    return pygame.transform.scale(player_image,(64,64))



# enemy positions
x = [87.5,187.5,287.5]
y = [225,125,25]
pygame.init()
window = pygame.display.set_mode((600,800))
player = Player()
player_image = resize('player_ship.png')
game = Game(window)
game.start()

