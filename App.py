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

    def endGame(self):
        self.running = False

    def startApp(self):
        self.drawGame()
        pygame.display.flip()
        bullet_list = []
        start_time = pygame.time.get_ticks()
        while self.running:
            self.clock.tick(60)
            now = pygame.time.get_ticks()
            cooldown = (now - start_time) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()

                if event.type == pygame.KEYDOWN and event.key == 32 and cooldown > player.coolDown: 
                    player.createBullet(bullet_list)
                    start_time = pygame.time.get_ticks()
                    cooldown = 0
                    
            for bullet in bullet_list:
                if bullet.y < 700:
                    bullet.moveUp()
                    #player.coolDown = True
                else:
                    bullet_list.pop(bullet_list.index(bullet))
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and player.x > 0:
                player.moveLeft()
            
            if keys[pygame.K_RIGHT] and player.x < self.width - player.width:
                player.moveRight()
            
            if keys[pygame.K_SPACE] and cooldown > player.coolDown:
                player.createBullet(bullet_list)
                start_time = pygame.time.get_ticks()
                cooldown = 0

            if player.isHit():
                player.loseHealth()
            
            
            self.screen.fill(self.background)
            self.drawPlayer()
            self.drawBullet(bullet_list)
            pygame.display.update()
    
    

