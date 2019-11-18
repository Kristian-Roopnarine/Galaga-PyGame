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
        self.hitbox = (self.x,self.y,self.width,self.height)
    
    def moveLeft(self):
        self.x -= self.steps

    def moveRight(self):
        self.x += self.steps

    def incScore(self):
        self.score += 1

    def resetCooldown(self):
        self.startCooldown = pygame.time.get_ticks()
    
    def updateCooldown(self):
        self.time_elapsed = (pygame.time.get_ticks() - self.startCooldown)/1000
        

    def onCooldown(self):
        return self.time_elapsed < self.reloadTime
    
    def isHit(self,bullet):
        for b in bullet:
            b_x = b.getX()
            b_y = b.getY()
            print(b_x,b_y)
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
        y = self.y 

        #create bullet
        bullet = Bullet(x,y,5,10,(255,192,203),5)

        #push bullet into list
        bullets.append(bullet)
    
class Enemy:
    def __init__(self,canShoot,row):
        self.x = 0
        self.y = 0
        self.pos = [[93,225],[268,225],[443,225],[93,125],[268,125],[443,125],[93,25],[268,25],[443,25]]
        self.width = 64
        self.height = 64
        self.health = 1
        self.canShoot = canShoot
        self.row = row
        self.reloadTime = 2
        self.time_elapsed = 0
        self.startCooldown = 0
        self.char = pygame.image.load('player_ship.png').convert_alpha()
        self.hitbox = (self.x,self.y,self.width,self.height)

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

    def setPosition(self,i):
        self.x = self.pos[i][0]
        self.y = self.pos[i][1]

    def increaseHealth(self):
        self.health += game.round

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
        return self.x
    
    def getY(self):
        return self.y
'''
def create_enemies(x,y,canShoot,row):
    return Enemy(x,y,canShoot,row)
'''
def create_enemies(canShoot,row):
    return Enemy(canShoot,row)

class Game:
    def __init__(self,win):
        self.width = 600
        self.height = 800
        self.block = 10
        self.background = (0,0,0)
        self.running = True
        self.round = 1
        self.enemies = []
        self.enemy_bullet_list = []
        self.player_bullet_list = []
        self.win = win
        self.clock = pygame.time.Clock()
        self.round = 1
        self.roundFinished = False

    
    def draw(self,win):
        for y in range(self.height//5):
            for x in range(self.width//5):
                rect = pygame.rect(x,y,self.block,self.block)
                pygame.draw.rect(self.win,self.background,rect)

    def generateEnemies(self):
        row = 1
        '''
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
                    '''
        for x in range(9):
            if row == 1:
                enemy = create_enemies(True,row)
            elif row == 2:
                enemy = create_enemies(False,row)
            elif row == 3:
                enemy = create_enemies(False,row)
            enemy.setPosition(x)
            self.enemies.append(enemy)

    def drawPlayer(self):
        self.win.blit(player_image,(player.x,player.y))

    def drawbullet(self):
        for bullet in self.player_bullet_list:
            b = pygame.Rect(bullet.x,bullet.y,bullet.width,bullet.height)
            pygame.draw.rect(self.win,bullet.color,b)

    def drawEnemies(self):
        for enemy in self.enemies:
            self.win.blit(enemy_image,(enemy.x,enemy.y))
    
    def redraw(self):
        self.win.fill((0,0,0))
        self.drawPlayer()
        self.drawbullet()
        self.drawEnemies()
        pygame.display.update()
    
    def endGame(self):
        self.running = False

    def start(self):
        self.drawPlayer()
        self.generateEnemies()
        self.drawEnemies()
        player.resetCooldown()
        pygame.display.flip()
        i=0

        while self.running:
            self.clock.tick(60)
            player.updateCooldown()
             
            #main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()

            for bullet in self.player_bullet_list:
                if 0 < bullet.y < 800:
                    bullet.moveUp()
                else:
                    self.player_bullet_list.pop(self.player_bullet_list.index(bullet))
            
            for bullet in self.enemy_bullet_list:
                if 0 > bullet.y > 800:
                    bullet.moveDown()
                else:
                    self.enemy_bullet_list.pop(self.enemy_bullet_list.index(bullet))

            #detect key presses
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player.x > 0:
                player.moveLeft()
                player.hitbox = (player.x,player.y,player.width,player.height)
            
            if keys[pygame.K_RIGHT] and player.x < self.width - player.width:
                player.moveRight()
                player.hitbox = (player.x,player.y,player.width,player.height)
            
            if keys[pygame.K_SPACE] and not player.onCooldown():
                player.createBullet(self.player_bullet_list)
                player.resetCooldown()
            
            if player.isHit(self.enemy_bullet_list):
                player.loseHealth()

            for enemy in self.enemies:
                if enemy.isHit(self.player_bullet_list):
                    enemy.loseHealth()
                    if enemy.health == 0:
                        self.enemies.pop(self.enemies.index(enemy))
                
            self.redraw()
            i += 1

def resize(image):
    player_image = pygame.image.load(image).convert()
    return pygame.transform.scale(player_image,(64,64))
    


#main loop
# enemy positions
pygame.init()
window = pygame.display.set_mode((600,800))
player = Player()
enemy_image = resize('enemy_ship.png')
player_image = resize('player_ship.png')
game = Game(window)
game.start()

