import pygame
from Player import Player
from Enemy import Enemy

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
        
    def drawGame(self):
        for y in range(self.height//5):
            for x in range(self.width//5):
                rect = pygame.Rect(x * self.block, y * self.block, self.block, self.block)
                pygame.draw.rect(self.screen,self.background,rect)
    
    def drawPlayer(self):
        ship = pygame.Rect(player.x,player.y,player.width,player.height)
        pygame.draw.rect(self.screen,player.color,ship)


    def endGame(self):
        self.running = False

    def startApp(self):
        self.drawGame()
        self.drawPlayer()
        pygame.display.flip()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.endGame()
    
    

