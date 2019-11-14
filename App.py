import pygame
from Player import Player
from Enemy import Enemy
from Bullet import Bullet

player = Player(175,525,25,25,(255,255,255),10,5)

class App:

    def __init__(self):
        self.width = 400
        self.height = 600
        self.block = 10
        self.background = (0,0,0)
        pygame.init()
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.now = 0
        self.startPlayerCooldown = 0
        self.startEnemyCooldown = 0
        self.playerCooldown = 0
        self.enemyCooldown = 0

        
    def drawGame(self):
        for y in range(self.height//5):
            for x in range(self.width//5):
                rect = pygame.Rect(x * self.block, y * self.block, self.block, self.block)
                pygame.draw.rect(self.screen,self.background,rect)
    
    def drawPlayer(self):
        ship = pygame.Rect(player.x,player.y,player.width,player.height)
        pygame.draw.rect(self.screen,player.color,ship)
    
    def drawBullet(self,bullets):
        for bullet in bullets:
            b = pygame.Rect(bullet.x,bullet.y,bullet.width,bullet.height)
            pygame.draw.rect(self.screen,bullet.color,b)
    
    def createEnemies(self,list):
        for x in range(100-(25//2),301,100):
            for y in range(25,301,100):
                if y == 225:
                    enemy = Enemy(x,y,25,25,(255,0,0),2,True)
                else:
                    enemy = Enemy(x,y,25,25,(255,0,0),2,False)
                list.append(enemy)
                
    
    def drawEnemies(self,enemies):
        for enemy in enemies:
            e = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
            pygame.draw.rect(self.screen, enemy.color , e)
    
    def resetCooldown(self,character=None):
        if character == 'player':
            self.startPlayerCooldown = pygame.time.get_ticks()
            self.playerCooldown = 0
        elif character == 'enemy':
            self.startEnemyCooldown = pygame.time.get_ticks()
            self.enemyCooldown = 0
        else:
            self.startEnemyCooldown = pygame.time.get_ticks()
            self.startPlayerCooldown = pygame.time.get_ticks()

    def updateCooldown(self):
        self.now = pygame.time.get_ticks()
        self.playerCooldown = (self.now - self.startPlayerCooldown) / 1000
        self.enemyCooldown = (self.now - self.startEnemyCooldown) / 1000

    def playerOnCooldown(self,cooldown):
       return cooldown > self.playerCooldown
    
    def enemyOnCooldown(self,cooldown):
        return cooldown > self.enemyCooldown
        
    def endGame(self):
        self.running = False

    def startApp(self):
        player_bullet_list = []
        enemy_list = []
        enemy_bullet_list = []
        self.drawGame()
        self.createEnemies(enemy_list)
        pygame.display.flip()
        self.resetCooldown()

        while self.running:
            self.clock.tick(60)
            self.updateCooldown()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
        
            for bullet in player_bullet_list:
                if 0 < bullet.y < 600:
                    bullet.moveUp()
                    
                else:
                    player_bullet_list.pop(player_bullet_list.index(bullet))
            
            for bullet in enemy_bullet_list:
                if 600 > bullet.y > 0:
                    bullet.moveDown()
                    
                else:
                    enemy_bullet_list.pop(enemy_bullet_list.index(bullet))
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player.x > 0:
                player.moveLeft()
            
            if keys[pygame.K_RIGHT] and player.x < self.width - player.width:
                player.moveRight()
            
            if keys[pygame.K_SPACE] and not self.playerOnCooldown(player.cooldown):
                player.createBullet(player_bullet_list)
                self.resetCooldown('player')
            
            if not self.enemyOnCooldown(1):
                for enemy in enemy_list:
                    if enemy.canShoot:
                        enemy.createBullet(enemy_bullet_list)
                self.resetCooldown('enemy')
                
            if player.isHit():
                player.loseHealth()
            
            
            
            self.screen.fill(self.background)
            self.drawPlayer()    
            self.drawEnemies(enemy_list)
            self.drawBullet(player_bullet_list)
            self.drawBullet(enemy_bullet_list)
            pygame.display.update()
    
    

