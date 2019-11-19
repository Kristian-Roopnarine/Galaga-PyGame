import pygame
import time

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
        self.score += (game.round * 100)

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
        self.pos = [[93,240],[268,240],[443,240],[93,140],[268,140],[443,140],[93,40],[268,40],[443,40]]
        self.width = 64
        self.height = 64
        self.health = 0
        self.canShoot = canShoot
        self.row = row
        self.reloadTime = 2
        self.time_elapsed = 0
        self.startCooldown = 0
        self.hitbox = (self.x,self.y,self.width,self.height)
        self.steps = 5
        self.path = [self.x,300]
        self.direction = 'right'

    def moveRight(self):
        self.x += self.steps
    
    def moveLeft(self):
        self.x -= self.steps

    def resetCooldown(self):
        self.startCooldown = pygame.time.get_ticks()
    
    def updateCooldown(self):
        self.time_elapsed = (pygame.time.get_ticks() - self.startCooldown) / 1000

    def onCooldown(self):
        return self.time_elapsed < self.reloadTime
    
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
    
    def changeStats(self,x,y,width,height,health,reloadTime):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.reloadTime = reloadTime

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
        self.bossFight = False
    
    def draw(self,win):
        for y in range(self.height//5):
            for x in range(self.width//5):
                rect = pygame.rect(x,y,self.block,self.block)
                pygame.draw.rect(self.win,self.background,rect)

    def generateEnemies(self):
        for x in range(9):
            if x <= 2:
                enemy = create_enemies(True,1)
            elif 2 < x <= 5:
                enemy = create_enemies(False,2)
            elif 5 < x <= 8:
                enemy = create_enemies(False,3)
            enemy.setPosition(x)
            self.enemies.append(enemy)
    
    def generateBoss(self):
        boss = create_enemies(True,1)
        boss.increaseHealth = self.round * 5
        return boss

    def drawPlayer(self):
        self.win.blit(player_image,(player.x,player.y))

    def drawbullet(self):
        for bullet in self.player_bullet_list:
            b = pygame.Rect(bullet.x,bullet.y,bullet.width,bullet.height)
            pygame.draw.rect(self.win,bullet.color,b)
        
        for bullet in self.enemy_bullet_list:
            b = pygame.Rect(bullet.x,bullet.y,bullet.width,bullet.height)
            pygame.draw.rect(self.win,bullet.color,b)

    def drawEnemies(self):
        if self.round < 5:
            for enemy in self.enemies:
                self.win.blit(enemy_image,(enemy.x,enemy.y))
        if self.round == 5:
            for boss in self.enemies:
                self.win.blit(boss_image,(boss.x,boss.y))
    
    def redraw(self):
        self.win.fill((0,0,0))
        self.drawPlayer()
        self.drawbullet()
        self.drawEnemies()
        sc = score.render('Score: ' + str(player.score),1, (255,255,255))
        lives = player_lives.render('Lives Remaining: ' + str(player.health),1,(255,255,255))
        self.win.blit(sc,(125,15))
        self.win.blit(lives,(300,15))
        pygame.display.update()


    def newRound(self):
        self.generateEnemies()
        self.drawEnemies()
        for enemy in self.enemies:
            enemy.resetCooldown()
            enemy.increaseHealth()
         
    def endGame(self):
        self.running = False

    def start(self):
        self.drawPlayer()
        self.newRound()
        print(self.round)
        player.resetCooldown()
        pygame.display.flip()
        shooters = {'row_1':0,'row_2':0,'row_3':0}
        for enemy in self.enemies:
            if enemy.row == 1:
                shooters['row_1'] += 1
            if enemy.row == 2:
                shooters['row_2'] += 1
            if enemy.row == 3:
                shooters['row_3'] += 1
            enemy.resetCooldown()
        
        while self.running:
            num_enemies = len(self.enemies)
            self.clock.tick(60)
            player.updateCooldown()

            #boss fight
            if self.bossFight:

                if boss.x < 0:
                    boss.direction = 'right'
                if boss.x > 425:
                    boss.direction = 'left'

                if boss.direction == 'right':
                    boss.moveRight()
                    boss.hitbox = (boss.x,boss.y,boss.width,boss.height)
                if boss.direction =='left':
                    boss.moveLeft()
                    boss.hitbox = (boss.x,boss.y,boss.width,boss.height)
                    
                

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
                if 800 > bullet.y > 0:
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
                if player.health == 0:
                    self.endGame()

            for enemy in self.enemies:
                #update enemies that can shoot
                if shooters['row_1'] == 0 and enemy.row == 2:
                    enemy.canShoot = True
                if shooters['row_2'] == 0 and enemy.row == 3:
                    enemy.canShoot = True

                #hit detection
                if enemy.isHit(self.player_bullet_list):
                    enemy.loseHealth()
    
                    if enemy.health == 0:
                        if enemy.row == 1:
                            shooters['row_1'] -= 1
                        if enemy.row == 2:
                            shooters['row_2'] -= 1
                        if enemy.row == 3:
                            shooters['row_3'] -= 1

                        #increase player score
                        self.enemies.pop(self.enemies.index(enemy))
                        player.incScore()
                        if self.round == 5:
                            self.endGame()
                        

                enemy.updateCooldown()

                #shoot
                if enemy.canShoot and not enemy.onCooldown():
                    enemy.createBullet(self.enemy_bullet_list)
                    enemy.resetCooldown()
            
            #check whether all enemies are done
            if num_enemies == 0:
                self.round += 1
                self.win.fill((0,0,0))
                text = round_info.render('Round ' + str(self.round), 1 ,(255,255,255))
                self.drawPlayer()
                self.win.blit(text,(225,350))
                self.player_bullet_list = []
                self.enemy_bullet_list = []
                pygame.display.update()
                time.sleep(2)

                if self.round <= 4:  
                    self.newRound()

                    #reset enemies that can shoot
                    shooters = {'row_1':0,'row_2':0,'row_3':0}
                    for enemy in self.enemies:
                        if enemy.row == 1:
                            shooters['row_1'] += 1
                        if enemy.row == 2:
                            shooters['row_2'] += 1
                        if enemy.row == 3:
                            shooters['row_3'] += 1
                        enemy.resetCooldown()

                elif self.round == 5 and not self.bossFight:
                    boss = self.generateBoss()
                    boss.changeStats(100,40,150,150,25,0.3)
                    self.enemies.append(boss)
                    self.bossFight = True


            self.redraw()
            

def resize(image,width,height):
    player_image = pygame.image.load(image).convert_alpha()
    player_image.set_colorkey((255,255,255)) 
    return pygame.transform.scale(player_image,(width,height))
    


#main loop
#enemy positions
pygame.init()
score = pygame.font.SysFont('comicsans',30)
player_lives = pygame.font.SysFont('comicsans',30)
round_info = pygame.font.SysFont('comicsans',50)
window = pygame.display.set_mode((600,800))
player = Player()
enemy_image = resize('enemy_ship.png',64,64)
player_image = resize('player_ship.png',64,64)
boss_image = resize('boss.png',150,150)
game = Game(window)
game.start()

